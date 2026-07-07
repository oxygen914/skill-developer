# 核心概念

## Agent Skill

Agent Skill 是 AI agent 的可复用能力包。它通过 `SKILL.md` 提供触发描述、工作流和资源导航，让 Codex、Claude Code 或其他兼容 Agent Skills 的客户端在特定任务中获得额外流程知识、脚本或素材。

## SKILL.md

`SKILL.md` 是唯一必需文件。通用 Agent Skills 默认使用 `name` 和 `description`；Claude Code 还支持 `when_to_use`、`disable-model-invocation`、`context` 等扩展字段。正文只在触发后加载。

## Progressive Disclosure

把信息分层放置：

- `description`：简短但覆盖触发场景。
- `SKILL.md`：核心流程和资源导航。
- `references/`：长说明、领域规则、示例、API 文档。
- `scripts/`：确定性或重复性操作。
- `assets/`：输出会用到的模板、图片、字体、示例项目等。

## 必需与推荐

必需：

- `SKILL.md`
- `name`
- `description`
- 合法 frontmatter

推荐：

- 目录名与 `name` 一致。
- Codex 发布添加 `agents/openai.yaml` 作为 UI 元信息；Claude Code 不需要它。
- 大型或多变内容拆到 `references/`。
- 新增脚本后运行代表性测试。

按需（只在有实际内容时创建）：

- `scripts/`：需要确定性操作时创建。
- `references/`：有长文档需要拆分时创建。
- `assets/`：有输出资源时创建。
- 配置文件：项目需要时创建。
- 测试目录：需要测试时创建。

禁止：

- 创建空目录占位（如空的 `scripts/`、`assets/`、`agents/`）。空目录不参与 skill 运行，只会造成维护困惑。

## 审核思路

先确认能加载和触发，再看可维护性：

1. 目标平台基础校验是否通过。
2. `description` 是否足够明确。
3. `SKILL.md` 是否简洁，有没有把长细节拆出去。
4. 引用文件是否存在，导航是否说明何时读取。
5. 脚本是否真的需要，是否可运行。
6. 是否存在空目录或不必要的辅助文档。
