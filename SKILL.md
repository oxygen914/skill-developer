---
name: skill-developer
description: |
  Codex Skill 开发和审核助手，用于创建、改进、验证和开源发布符合 Codex skill 规范的技能包。Use when the user asks to create, update, review, audit, validate, refactor, package, document, or publish a Codex skill; asks about SKILL.md, skill templates, skill structure, skill best practices, trigger descriptions, bundled resources, references, scripts, assets, agents/openai.yaml, README files for GitHub publishing, or skill validation; or wants to check whether an existing skill follows Codex conventions.
---

# Skill 开发助手

使用本 skill 创建或审核 Codex skill。优先遵循官方基础规范，再按任务复杂度添加项目增强约束。

## 核心原则

| 原则 | 做法 |
|---|---|
| 基础规范优先 | `SKILL.md` 必须存在；frontmatter 必须有 `name` 和 `description`；`name` 使用小写字母、数字和连字符；目录名应与 `name` 一致。 |
| 按需添加资源 | 只有在能减少重复、提高可靠性或承载必要知识时，才添加 `scripts/`、`references/`、`assets/`、`agents/`。 |
| 禁止空目录 | 不要创建空的目录占位；只在有实际内容时才创建对应目录。空目录不参与 skill 运行，只会造成维护困惑。 |
| 保持入口轻量 | `SKILL.md` 只放触发、核心流程和资源导航；详细模板、示例、长文档放入 `references/`。 |
| 区分必需和推荐 | 不把项目偏好当成所有 skill 的硬性规范；审核时标明”必须修复””建议优化””项目约定”。 |
| 区分运行时和发布包装 | Codex 运行时只需要 skill 必需文件；GitHub 开源时可以额外提供 `README.md` 等面向人的仓库文档。 |
| 验证真实可用 | 创建或大改后运行官方基础校验；复杂 skill 还要用真实请求做前向测试。 |

## 工作流

1. 明确用户目标：创建新 skill、更新现有 skill、审核规范，或生成模板。
2. 读取目标 skill 的 `SKILL.md` 和直接相关资源；不要一次加载无关参考文件。
3. 根据任务选择对应参考文档。
4. 区分运行时 skill 包和 GitHub 开源仓库包装；不要把 README、CHANGELOG 等发布材料当成触发或执行资源。
5. 实施修改时保持文件精简，避免无用 README、CHANGELOG、安装说明等辅助文档。
6. 运行校验并根据结果修复问题。

## 交互原则

| 场景 | 原则 |
|---|---|
| 信息不足 | 能从上下文合理推断时直接继续；缺少关键决策且推断风险高时，向用户问一个简短问题。 |
| 创建新 skill | 确认名称、用途、触发场景和是否需要脚本/引用/资产；目录默认放到用户指定路径，未指定时用 `$CODEX_HOME/skills` 或 `~/.codex/skills`。只创建有实际内容的目录，不创建空目录占位。 |
| 审核 skill | 先给必须修复项，再给建议优化项；用文件路径和具体原因说明；发现空目录应建议删除。 |
| 生成脚本 | 只有需要确定性执行、反复复用或易出错流程时才添加脚本；新增脚本必须实际运行代表性测试。 |
| 开源发布 | 可以编写面向人的 `README.md`，但不要让 README 替代 `SKILL.md`、`references/` 或校验脚本。 |
| 危险操作 | 删除、覆盖、发布、生产变更等不可逆操作，先展示影响范围并获得明确确认。 |

## 边界

- 不把本 skill 当成普通代码生成、业务需求分析或通用项目管理 skill。
- 不把团队偏好升级为官方硬性规范；只有加载、触发或基本执行会失败的问题才列为“必须修复”。
- 不为小型 skill 强制创建 `scripts/`、`references/`、`assets/`、配置框架或 README。
- 不把 GitHub README 作为 Codex 运行时资源；README 只服务开源介绍、安装和贡献说明。

## 操作路由

按用户目标读取对应文档：

| 目标 | 何时读取 | 文档 |
|---|---|---|
| 创建或重构 skill | 用户要新建 skill，或现有 skill 结构需要明显调整 | `references/create-skill.md` |
| 编写或修正 `SKILL.md` | 需要调整 frontmatter、触发描述、入口正文、资源导航 | `references/skill-md-template.md` |
| 生成或审核脚本 | 需要 `scripts/`、CLI、配置读取、确定性工具 | `references/script-template.md` |
| 生成或审核配置 | skill 需要 token、API key、路径、环境变量等配置 | `references/config-template.md` |
| 审核规范 | 用户要求检查、review、audit、验证 skill | `references/check-skill.md` |
| 需要完整参考 | 用户要求示例，或当前设计缺少可参照的整体形态 | `references/full-example.md` |
| 解释基础概念 | 用户不熟悉 skill、frontmatter、渐进加载或资源类型 | `references/concepts.md` |
| 排查常见问题 | 触发不准、结构臃肿、资源不可发现、脚本未验证等问题 | `references/common-mistakes.md` |
| GitHub 开源发布 | 用户要求写 README、打包发布、说明安装或贡献方式 | `references/open-source-readme.md` |

## 校验

创建或修改完成后，运行官方基础校验：

```bash
python3 /Users/didi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>
```

如果本 skill 的自定义检查脚本适合当前项目，再运行：

```bash
python3 SKILL_DIR/scripts/common/check_skill_structure.py <skill-folder>
```

自定义检查脚本用于发现项目约定和质量建议，不应替代官方基础校验。

## 审核等级

| 等级 | 含义 | 示例 |
|---|---|---|
| 必须修复 | 会影响发现、加载或基本使用 | 缺少 `SKILL.md`、frontmatter 无效、缺少 `name` 或 `description`、`name` 非 hyphen-case。 |
| 建议优化 | 不一定破坏使用，但会降低触发、维护或验证质量 | `description` 触发场景不清楚、`SKILL.md` 过长、资源导航不清晰、脚本未测试。 |
| 项目约定 | 只在当前团队明确采用时执行 | 固定目录模板、配置文件格式、特定脚本框架、内部输出格式。 |

## 输出要求

审核时给出结论、问题清单和建议修改方向。完成修改时说明改了哪些文件、运行了哪些校验、还有哪些残余风险。
