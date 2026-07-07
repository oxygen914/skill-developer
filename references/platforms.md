# 平台兼容指南

本 skill 默认面向跨平台 Agent Skills，同时兼容 Codex 和 Claude Code。创建或审核 skill 时，先明确目标平台；未指定时，优先生成只使用通用字段的 Agent Skill。

## 通用 Agent Skills

通用结构：

```text
<skill-name>/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

通用 `SKILL.md` frontmatter：

```yaml
---
name: <skill-name>
description: <what the skill does and when to use it>
---
```

原则：

- `SKILL.md` 必须存在。
- `name` 和 `description` 是跨平台默认必备字段。
- `name` 使用小写字母、数字和连字符，建议与目录名一致。
- `description` 同时说明能力边界和触发场景。
- 长规则拆到 `references/`，脚本放到 `scripts/`，输出素材放到 `assets/`。
- 文件引用使用相对路径，并在 `SKILL.md` 说明何时读取。

可选通用字段：

- `license`: skill 的许可证。
- `compatibility`: 环境要求，例如目标产品、系统依赖、网络要求。
- `metadata`: 额外元信息。
- `allowed-tools`: 工具预授权，支持情况因客户端而异。

## Codex

安装位置：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R <skill-name> "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Codex 设计要点：

- frontmatter 保守使用 `name` 和 `description`。
- `description` 是触发核心，应包含任务、文件类型、平台名和常见请求措辞。
- `agents/openai.yaml` 可用于 OpenAI/Codex UI 展示；Claude 不需要它。
- 创建新 skill 时可使用 Codex 官方 `init_skill.py`。
- 修改后运行 Codex 官方 `quick_validate.py`。

Codex 校验：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>
```

## Claude Code

安装位置：

```bash
mkdir -p ~/.claude/skills
cp -R <skill-name> ~/.claude/skills/
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -R <skill-name> .claude/skills/
```

Claude Code 设计要点：

- skill 目录名决定 slash command，例如 `~/.claude/skills/skill-developer/SKILL.md` 对应 `/skill-developer`。
- `description` 帮助 Claude 自动判断何时加载 skill。
- 用户也可以直接用 `/skill-name` 调用。
- Claude Code 会按需读取 `SKILL.md` 和支持文件；长内容仍应拆到 `references/`。
- `agents/openai.yaml` 对 Claude Code 没有运行时意义，可以保留给 Codex，但不要当成 Claude 必需文件。

Claude Code 常见扩展字段：

- `when_to_use`: 额外触发说明。
- `argument-hint` / `arguments`: slash command 参数提示与位置参数。
- `disable-model-invocation`: 禁止模型自动触发，只允许手动调用。
- `user-invocable`: 是否在 `/` 菜单中展示。
- `allowed-tools` / `disallowed-tools`: skill 激活期间的工具控制。
- `model` / `effort`: skill 激活时的模型或推理强度设置。
- `context: fork`: 在 forked subagent 上下文中运行。
- `agent`: `context: fork` 时指定子代理类型。
- `hooks`, `paths`, `shell`: Claude Code 专属执行控制。

这些字段应标注为 Claude Code 扩展；如果目标是 Codex 或通用 Agent Skills，不要默认添加。

## 平台选择策略

| 目标 | 默认做法 |
|---|---|
| 跨平台发布 | 只使用 `name`、`description` 和通用资源目录；README 中分开写 Codex/Claude 安装方式。 |
| Codex 专用 | 可添加 `agents/openai.yaml`，使用 Codex `quick_validate.py`。 |
| Claude Code 专用 | 可使用 Claude Code 扩展 frontmatter；安装到 `~/.claude/skills` 或 `.claude/skills`。 |
| 不确定 | 先生成通用 Agent Skill，再在 README 或 `references/platforms.md` 中补平台说明。 |

## 审核口径

- 通用必修：`SKILL.md`、合法 frontmatter、清晰 `description`、资源引用存在。
- Codex-only 建议：`agents/openai.yaml`、Codex `quick_validate.py`。
- Claude-only 建议：目录名与 slash command 清晰、扩展 frontmatter 有明确理由。
- 不要把平台扩展字段直接列为所有平台的必须修复项。
