<p align="center">
  <img src="assets/readme/skill-developer/wordmark.gif" alt="Skill Developer animated wordmark" width="720" />
</p>

# Skill Developer

面向 Agent Skills、Codex 与 Claude Code 的 Skill 设计与审核助手：把模糊想法整理成可触发、可维护、可验证、可发布的 Skill 包。

它关注的不只是“生成文件”，而是先明确触发边界与平台差异，再决定规则应进入 `SKILL.md`、`references/`、`scripts/` 还是 `assets/`。运行时规范以 [SKILL.md](SKILL.md) 为准。

## 能做什么

- 从需求澄清和 Skill brief 开始设计复杂 Skill。
- 创建、重构或审核跨平台 Agent Skill。
- 改进 `description`、资源分层和渐进加载结构。
- 区分 Agent Skills 基础约定、Codex 扩展与 Claude Code 扩展。
- 运行结构、兼容性与发布前检查，并按严重程度报告问题。
- 为 GitHub 开源发布准备 README、目录结构和验证说明。

## 兼容性

| 平台 | 安装位置 | 项目支持 |
| --- | --- | --- |
| Agent Skills | 客户端约定的 Skills 目录 | `SKILL.md`、`references/`、`scripts/`、`assets/` |
| Codex | `${CODEX_HOME:-$HOME/.codex}/skills` | UI 元信息与 Codex 校验 |
| Claude Code | `~/.claude/skills` 或 `.claude/skills` | 个人级、项目级安装与 `/skill-developer` 调用 |

## 安装

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill-developer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Claude Code

个人级安装：

```bash
mkdir -p ~/.claude/skills
cp -R skill-developer ~/.claude/skills/
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -R skill-developer .claude/skills/
```

安装后刷新或重启对应客户端，使 Skill metadata 被重新发现。

## 快速开始

把目标与平台直接写进请求：

```text
用 $skill-developer 设计一个同时兼容 Codex 和 Claude Code 的周报 Skill，先确认触发边界和资源分层。
```

也可以直接审核现有目录：

```text
Use $skill-developer to audit this skill for Codex and Claude Code compatibility.
```

复杂或边界敏感的需求会先形成 Skill brief；明确的小改动会直接实施并验证。

## 工作方式

1. 明确目标平台、用途、非目标和典型触发请求。
2. 必要时在 `.skill-work/<skill-name>/skill-brief.md` 形成可确认的设计稿。
3. 保持 `SKILL.md` 轻量，把长规则、模板与示例路由到 `references/`。
4. 只把确定性、重复性或易错流程实现为 `scripts/`。
5. 按目标平台校验，并区分“必须修复”“建议优化”“项目约定”。

## 验证

在仓库根目录运行：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
python3 scripts/common/check_skill_structure.py . --platform agent
python3 scripts/common/check_skill_structure.py . --platform claude
python3 scripts/common/check_skill_structure.py . --platform codex
```

增强检查器成功时返回：

```json
{
  "ok": true,
  "errors": [],
  "warnings": []
}
```

## 仓库导航

- [SKILL.md](SKILL.md)：运行时入口、核心原则与资源路由。
- [平台差异](references/platforms.md)：Agent Skills、Codex 与 Claude Code 的安装和字段边界。
- [设计工作流](references/design-workflow.md)：复杂需求的 Skill brief 流程。
- [创建与重构](references/create-skill.md)：从结构设计到验证的完整路径。
- [审核清单](references/check-skill.md)：问题分级与审核输出格式。
- [结构检查器](scripts/common/check_skill_structure.py)：跨平台增强检查。

## 设计边界

- 不把团队偏好描述成所有平台的硬性规范。
- 不创建空目录，也不为简单 Skill 强制增加脚本或配置。
- 不把 README、临时 brief 和实现计划当作运行时资源。
- 不把 `agents/openai.yaml` 说成 Claude Code 的必需文件。
- 不复制未核对许可证的第三方实现。

## License

当前仓库尚未提供 `LICENSE` 文件。公开发布前请先选择并补充合适的开源许可证。
