# SKILL.md 模板与规范

## 最小模板

```markdown
---
name: <skill-name>
description: <一句话说明功能，并包含明确触发场景。Use when ...>
---

# <Skill 标题>

用 1-2 句话说明这个 skill 如何帮助 Codex 完成任务。

## Workflow

1. 读取或确认必要输入。
2. 按任务选择相关资源。
3. 执行、校验并汇报结果。

## Resources

- `references/<topic>.md`：当需要 <场景> 时读取。
- `scripts/<tool>.py`：当需要 <确定性操作> 时运行。
```

## Frontmatter

必需字段：

- `name`：小写字母、数字和连字符；不超过 64 个字符；目录名应与它一致。
- `description`：说明 skill 做什么，以及用户在什么任务/措辞/上下文中应触发它。

不要把触发条件只写在正文。正文只有触发后才会加载。

可选字段：

- `metadata`：可保留短说明，但不要用它替代 `agents/openai.yaml`。
- `license`、`allowed-tools`：只有项目明确需要时添加。

官方基础规范只依赖 `name` 和 `description`。如果项目允许额外字段，审核时应标成“项目约定”或“兼容性提醒”，不要把额外字段写成所有 skill 都必须采用的做法。

## 正文结构

按任务需要选择章节，不要机械套模板。

推荐章节：

- `Workflow`：核心步骤。
- `Resources`：列出何时读取哪些 `references/`，何时运行哪些 `scripts/`。
- `Validation`：创建、编辑或执行后需要跑的检查。
- `Safety`：涉及删除、覆盖、发布、生产变更等操作时的确认规则。

对于包含多类任务的大型 skill，可以用“操作路由”表替代普通 `Resources` 列表，只要明确写出何时读取每个资源。本 skill 的 `SKILL.md` 就采用了这种写法。

不推荐固定强制：

- 每个 skill 都有“初始化检查”。
- 每个 skill 都有“操作路由表”。
- 每个 skill 都有 `scripts/common/config.py`。
- 每个 skill 都有 `assets/knowledge/`。
- 每个 skill 都有 README；README 只在开源发布或仓库展示时需要。

## Description 写法

好的 `description` 应覆盖三件事：

1. skill 的能力边界。
2. 应触发的用户请求或上下文。
3. 关键文件类型、工具、平台或领域词。

示例：

```yaml
description: |
  Create and update Codex skills with compliant SKILL.md frontmatter, concise workflows, optional references/scripts/assets, agents/openai.yaml metadata, and validation. Use when the user asks to create, audit, improve, validate, or refactor a skill, or asks about skill templates, trigger descriptions, bundled resources, or skill best practices.
```

## Prompt 与语言策略

- `description` 影响 skill 触发，优先写清英文触发词；如果目标用户常用中文，可以采用中英双语。
- `agents/openai.yaml` 的 `default_prompt` 面向 UI 示例，英文通常更通用；面向中文团队内部使用时，也可以写中文或中英双语。
- `SKILL.md` 正文和 `references/` 可以使用用户或团队主要工作语言，不必为了“看起来标准”强行改英文。
- 不管使用哪种语言，都要保留关键英文领域词，如 `SKILL.md`、`Use when`、`references/`、`scripts/`、`assets/`、`agents/openai.yaml`。

示例：

```yaml
description: |
  PDF 批注和脱敏处理助手。Use when the user asks to redact, annotate, inspect, split, or export PDF files, especially when preserving layout or checking sensitive text.
```

## 资源导航示例

```markdown
## Resources

- Read `references/api.md` before calling the service API.
- Read `references/redlining.md` only when the user asks for tracked changes.
- Run `scripts/normalize.py` when converting exported data before analysis.
```

资源导航要说明“何时读取”，不要只列文件名。

## README 边界

如果用户要求开源到 GitHub，可以添加 `README.md` 介绍项目、安装、使用和贡献方式。README 面向人类读者，不参与 skill 触发；触发条件、工作流和资源导航仍必须写在 `SKILL.md`。

## 校验示例

```markdown
## Validation

After editing, run:

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>
```
```
