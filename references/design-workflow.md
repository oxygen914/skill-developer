# Skill 设计工作流

用这个流程把模糊需求转成可实现的 Codex skill。它是可选设计门：复杂、含糊或边界敏感时使用；小型明确任务直接进入 `references/create-skill.md`。

## 何时使用

- 用户只描述了想法，还没有明确 skill 要处理哪些任务。
- 触发边界容易过宽或过窄，需要定义 should trigger / should not trigger。
- 可能需要多个 `references/`、`scripts/`、`assets/`，资源分层尚不清楚。
- skill 依赖内部规则、外部 API、凭证、模板、固定输出格式或安全确认。
- 用户明确要求先设计、先写方案、先和他敲定。

## 何时跳过

- 只是修正一个 `description`、补资源导航、跑校验或做普通审核。
- 用户已经给出完整结构和验收标准。
- skill 很小，只有 `SKILL.md` 就足够。

## 交互节奏

1. 从已有上下文提炼假设，不要把能推断的信息重新问一遍。
2. 缺少关键决策时，一轮只问 1-3 个高价值问题。
3. 让问题围绕具体例子：用户会怎么请求、期望输出是什么、哪些请求不应触发。
4. 当信息足够时，先给 brief 草案，不要直接扩大实现范围。
5. 等用户确认 brief 后再创建、重构或大改 skill；小修可以在说明假设后直接继续。

## Brief 保存位置

默认把设计草案放在最终 skill 目录外，避免污染运行时包：

```text
.skill-work/<skill-name>/skill-brief.md
```

如果用户要求保存在别处，使用用户指定路径。不要把 brief 自动放进最终 skill 的 `references/`。只有稳定、未来运行时也需要读取的规则、流程或领域知识，才转成 `references/<topic>.md`。

## Brief 模板

```markdown
# <skill-name> Skill Brief

Status: draft

## Purpose
这个 skill 解决什么问题。

## Non-goals
它不应该处理什么，避免触发过宽。

## Trigger Contract
Should trigger:
- ...

Should not trigger:
- ...

## Example Requests
- 用户可能怎么说。
- 边界或复杂请求怎么说。

## Runtime Workflow
Codex 触发后应该按什么步骤工作。

## Resource Plan
- SKILL.md: 放触发说明、核心流程、资源导航。
- references/: 放长规则、领域知识、示例、检查清单。
- scripts/: 放确定性、重复性、易出错操作。
- assets/: 放输出会复制或引用的模板、图片、字体、示例项目。
- agents/openai.yaml: 放 UI 展示信息。

## Validation Plan
需要跑哪些校验、脚本测试或真实请求前向测试。

## Open Decisions
还没定的点。
```

## 从 Brief 到 Skill

- `Purpose` 和 `Trigger Contract` 进入 `SKILL.md` frontmatter `description`，用清晰的 Use when 覆盖触发场景。
- `Runtime Workflow` 精简后进入 `SKILL.md` 正文。
- 长规则、领域知识、检查清单、示例库进入 `references/`，并在 `SKILL.md` 说明何时读取。
- 确定性、重复性、易出错的操作进入 `scripts/`，脚本必须有代表性测试。
- 输出模板、素材、示例项目进入 `assets/`，不要把它们加载进上下文解释。
- 只给最终 skill 保留运行所需文件；删除初始化占位内容和不会被未来使用的草案。

## 确认点

实现前确认这些内容：

- skill 名称和安装位置。
- should trigger / should not trigger 边界。
- 资源计划是否真的需要 `references/`、`scripts/`、`assets/`。
- 是否涉及凭证、外部服务、删除、覆盖、发布或生产变更。
- 验收标准和最小测试集。

## 输出方式

给用户看 brief 摘要时，突出决策和待确认点。不要倾倒长模板；用户确认后再实施，并在最终回复里说明 brief 是否保留、哪些内容进入了最终 skill 包。
