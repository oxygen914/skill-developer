#!/usr/bin/env python3
"""Project-level Agent Skill checker.

This checker complements platform-specific validators. It treats load/trigger
problems as errors and reports portability or project hygiene items as warnings.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path
from typing import Any

import yaml


BASE_FRONTMATTER_KEYS = {
    "name",
    "description",
}

AGENT_SKILLS_FRONTMATTER_KEYS = BASE_FRONTMATTER_KEYS | {
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}

CODEX_FRONTMATTER_KEYS = BASE_FRONTMATTER_KEYS | {
    "license",
    "allowed-tools",
    "metadata",
}

CLAUDE_FRONTMATTER_KEYS = AGENT_SKILLS_FRONTMATTER_KEYS | {
    "when_to_use",
    "argument-hint",
    "arguments",
    "disable-model-invocation",
    "user-invocable",
    "disallowed-tools",
    "model",
    "effort",
    "context",
    "agent",
    "hooks",
    "paths",
    "shell",
}

PLATFORM_KEYS = {
    "agent": AGENT_SKILLS_FRONTMATTER_KEYS,
    "codex": CODEX_FRONTMATTER_KEYS,
    "claude": CLAUDE_FRONTMATTER_KEYS,
}

# 这些目录属于内部/工具产物，不应作为 skill 运行时内容，空目录检测时跳过。
IGNORED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
}


class SkillChecker:
    def __init__(self, skill_path: str, platform: str = "agent"):
        # resolve() 把 "." 等相对路径转成绝对路径，确保 .name 拿到真实目录名。
        self.skill_path = Path(skill_path).resolve()
        self.platform = platform
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def check_all(self) -> tuple[bool, list[str], list[str]]:
        frontmatter, body = self._check_skill_md()
        if frontmatter is not None:
            self._check_name(frontmatter)
            self._check_description(frontmatter)
            self._check_referenced_resources(body)

        self._check_agents_metadata()
        self._check_scripts()
        self._check_extraneous_docs()
        self._check_empty_dirs()

        return len(self.errors) == 0, self.errors, self.warnings

    def _check_skill_md(self) -> tuple[dict[str, Any] | None, str]:
        skill_md = self.skill_path / "SKILL.md"
        if not skill_md.exists():
            self.errors.append("缺少必需文件: SKILL.md")
            return None, ""

        content = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n?", content, re.DOTALL)
        if not match:
            self.errors.append("SKILL.md: 缺少合法 YAML frontmatter")
            return None, content

        try:
            frontmatter = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            self.errors.append(f"SKILL.md: frontmatter YAML 解析失败: {exc}")
            return None, content[match.end() :]

        if not isinstance(frontmatter, dict):
            self.errors.append("SKILL.md: frontmatter 必须是 YAML 字典")
            return None, content[match.end() :]

        keys = set(frontmatter)
        standard_optional = sorted(
            keys & (AGENT_SKILLS_FRONTMATTER_KEYS - BASE_FRONTMATTER_KEYS)
        )
        if standard_optional:
            self.warnings.append(
                "SKILL.md: frontmatter 使用了可选字段 "
                f"{standard_optional}; 跨平台最小结构只需要 name 和 description"
            )

        allowed_keys = PLATFORM_KEYS[self.platform]
        unexpected = sorted(keys - allowed_keys)
        if unexpected:
            self.warnings.append(
                f"SKILL.md: frontmatter 包含 {self.platform} 平台未定义字段 "
                f"{unexpected}; 如不影响目标平台加载和触发，可作为项目约定保留"
            )

        if self.platform == "codex":
            codex_extension_keys = sorted(keys - BASE_FRONTMATTER_KEYS)
            if codex_extension_keys:
                self.warnings.append(
                    "SKILL.md: Codex 官方基础校验最稳妥的是只使用 name 和 description；"
                    f"当前额外字段: {codex_extension_keys}"
                )

        if "name" not in frontmatter:
            self.errors.append("SKILL.md: frontmatter 缺少 name")
        if "description" not in frontmatter:
            self.errors.append("SKILL.md: frontmatter 缺少 description")

        return frontmatter, content[match.end() :]

    def _check_name(self, frontmatter: dict[str, Any]) -> None:
        name = frontmatter.get("name")
        if not isinstance(name, str) or not name.strip():
            self.errors.append("SKILL.md: name 必须是非空字符串")
            return

        name = name.strip()
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            self.errors.append(
                f"SKILL.md: name '{name}' 应使用小写字母、数字和连字符"
            )
        if len(name) > 64:
            self.errors.append(f"SKILL.md: name 过长 ({len(name)} > 64)")

        if self.skill_path.name != name:
            self.warnings.append(
                f"目录名 '{self.skill_path.name}' 与 SKILL.md name '{name}' 不一致"
            )

    def _check_description(self, frontmatter: dict[str, Any]) -> None:
        description = frontmatter.get("description")
        if not isinstance(description, str) or not description.strip():
            self.errors.append("SKILL.md: description 必须是非空字符串")
            return

        desc = description.strip()
        if len(desc) > 1024:
            self.errors.append(f"SKILL.md: description 过长 ({len(desc)} > 1024)")

        trigger_terms = ("Use when", "use when", "当", "用于", "asks", "用户")
        if not any(term in desc for term in trigger_terms):
            self.warnings.append(
                "SKILL.md: description 建议明确写出适用场景和触发请求"
            )

    def _check_referenced_resources(self, body: str) -> None:
        refs = set(
            re.findall(
                r"`((?:agents|references|scripts|assets)/[^`\\s]+)`",
                body,
            )
        )
        for rel_path in sorted(refs):
            path = self.skill_path / rel_path
            if not path.exists():
                self.errors.append(f"SKILL.md: 引用了不存在的资源: {rel_path}")

    def _check_agents_metadata(self) -> None:
        agents_file = self.skill_path / "agents" / "openai.yaml"
        if not agents_file.exists():
            if self.platform == "codex":
                self.warnings.append("Codex 发布建议添加 agents/openai.yaml 作为 UI 元信息")
            return

        try:
            data = yaml.safe_load(agents_file.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            self.errors.append(f"agents/openai.yaml: YAML 解析失败: {exc}")
            return

        interface = data.get("interface", {})
        if not isinstance(interface, dict):
            self.errors.append("agents/openai.yaml: interface 必须是字典")
            return

        for key in ("display_name", "short_description", "default_prompt"):
            if not interface.get(key):
                self.warnings.append(f"agents/openai.yaml: 建议填写 interface.{key}")

    def _check_scripts(self) -> None:
        scripts_dir = self.skill_path / "scripts"
        if not scripts_dir.exists():
            return

        for script in scripts_dir.rglob("*.py"):
            try:
                ast.parse(script.read_text(encoding="utf-8"))
            except SyntaxError as exc:
                rel = script.relative_to(self.skill_path)
                self.errors.append(f"{rel}: Python 语法错误: {exc}")

        runnable_scripts = [
            p for p in scripts_dir.rglob("*.py") if p.name != "__init__.py"
        ]
        if runnable_scripts and not (
            self.skill_path / "references" / "script-template.md"
        ).exists():
            self.warnings.append(
                "存在脚本时，建议在 SKILL.md 或 references/ 中说明运行方式和测试方法"
            )

    def _check_extraneous_docs(self) -> None:
        readme = self.skill_path / "README.md"
        if readme.exists() and not self._is_publish_readme(readme):
            self.warnings.append(
                "README.md: skill 包内通常不需要 README；如用于 GitHub 开源发布，请说明安装、使用、校验、贡献和许可证状态"
            )

        for name in ("CHANGELOG.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md"):
            if (self.skill_path / name).exists():
                self.warnings.append(f"{name}: skill 包内通常不需要额外说明文档")

    def _is_publish_readme(self, readme: Path) -> bool:
        try:
            text = readme.read_text(encoding="utf-8").lower()
        except UnicodeDecodeError:
            return False

        publish_markers = ("github", "open source", "开源", "repository", "仓库")
        skill_markers = (
            "skill.md",
            "agent skill",
            "codex skill",
            "claude code",
            "codex",
        )
        required_sections = ("install", "安装", "usage", "使用", "validation", "校验")
        return (
            any(marker in text for marker in publish_markers)
            and any(marker in text for marker in skill_markers)
            and any(section in text for section in required_sections)
        )

    def _check_empty_dirs(self) -> None:
        """检测空目录占位。

        空目录不参与 skill 运行，只造成维护困惑（见 check-skill.md 的“建议优化”）。
        输出为 warning，不影响 ok。跳过 .git/、缓存等内部目录。
        """
        for path in sorted(self.skill_path.rglob("*")):
            if not path.is_dir() or path.name in IGNORED_DIRS:
                continue
            # 跳过被忽略目录内部的子目录（如 .git/objects）
            if any(part in IGNORED_DIRS for part in path.relative_to(self.skill_path).parts):
                continue
            try:
                has_child = next(path.iterdir(), None) is not None
            except (PermissionError, OSError):
                continue
            if not has_child:
                rel = path.relative_to(self.skill_path)
                self.warnings.append(
                    f"{rel}/: 空目录占位；空目录不参与 skill 运行，建议删除"
                )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_path", nargs="?", default=".")
    parser.add_argument(
        "--platform",
        choices=sorted(PLATFORM_KEYS),
        default="agent",
        help="Target platform rules to check: agent, codex, or claude.",
    )
    args = parser.parse_args()

    checker = SkillChecker(args.skill_path, platform=args.platform)
    ok, errors, warnings = checker.check_all()
    result = {
        "ok": ok,
        "platform": args.platform,
        "skill_path": str(Path(args.skill_path).resolve()),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
