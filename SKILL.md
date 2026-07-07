---
name: skill-developer
description: |
  Agent Skill 开发和审核助手，用于澄清需求、设计、创建、改进、验证和开源发布兼容 Agent Skills、Codex 和 Claude Code 的技能包。Use when the user asks to create, design, update, review, audit, validate, refactor, package, document, or publish an Agent Skill, Codex skill, or Claude Code skill; asks about SKILL.md, skill templates, skill design briefs, skill structure, skill best practices, trigger descriptions, bundled resources, references, scripts, assets, agents/openai.yaml, Claude .claude/skills, README files for GitHub publishing, or skill validation; or wants to check whether an existing skill follows Agent Skills, Codex, or Claude conventions.
---

# Skill 开发助手

使用本 skill 创建或审核 Agent Skills、Codex skills 和 Claude Code skills。默认优先遵循跨平台 Agent Skills 基础规范，再按目标平台添加 Codex 或 Claude 扩展。

## 核心原则

| 原则 | 做法 |
|---|---|
| 跨平台基础优先 | `SKILL.md` 必须存在；frontmatter 默认使用 `name` 和 `description`；`name` 使用小写字母、数字和连字符；目录名应与 `name` 一致。 |
| 按需添加资源 | 只有在能减少重复、提高可靠性或承载必要知识时，才添加 `scripts/`、`references/`、`assets/`、`agents/`。 |
| 禁止空目录 | 不要创建空的目录占位；只在有实际内容时才创建对应目录。空目录不参与 skill 运行，只会造成维护困惑。 |
| 保持入口轻量 | `SKILL.md` 只放触发、核心流程和资源导航；详细模板、示例、长文档放入 `references/`。 |
| 设计先行可选 | 需求复杂、模糊或触发边界难判断时，先产出可确认的 skill brief；小型明确任务直接实现。 |
| 平台差异显式化 | 默认写跨平台 skill；只有用户指定 Codex 或 Claude 行为时，才加入平台专属路径、校验命令或 frontmatter。 |
| 参考发现可选 | 创建复杂、陌生或准备开源的 skill 时，可先轻量查看本地 skills、GitHub 或开源 skill 社区；只提炼结构和模式，不复制大段内容。 |
| 区分必需和推荐 | 不把项目偏好当成所有 skill 的硬性规范；审核时标明”必须修复””建议优化””项目约定”。 |
| 区分运行时和发布包装 | Agent 运行时只需要 skill 必需文件；GitHub 开源时可以额外提供 `README.md` 等面向人的仓库文档。 |
| 验证真实可用 | 创建或大改后运行官方基础校验；复杂 skill 还要用真实请求做前向测试。 |

## 工作流

1. 明确用户目标和目标平台：通用 Agent Skill、Codex、Claude Code，或多平台兼容。
2. 读取目标 skill 的 `SKILL.md` 和直接相关资源；不要一次加载无关参考文件。
3. 创建或重构复杂、模糊、边界敏感的 skill 时，先读取 `references/design-workflow.md`，产出 skill brief 并与用户确认；小型明确任务跳过 brief。
4. 涉及平台安装、frontmatter、校验或发布时，先读取 `references/platforms.md`。
5. 创建或重构复杂 skill 时，按需做参考发现：先看本地已有 skills，再视情况检索 GitHub 或开源 skill 社区。
6. 根据任务选择对应参考文档。
7. 区分运行时 skill 包、临时设计材料和 GitHub 开源仓库包装；不要把 README、CHANGELOG、设计草案等材料当成触发或执行资源。
8. 实施修改时保持文件精简，避免无用 README、CHANGELOG、安装说明等辅助文档。
9. 按目标平台运行校验并根据结果修复问题。

## 交互原则

| 场景 | 原则 |
|---|---|
| 信息不足 | 能从上下文合理推断时直接继续；缺少关键决策且推断风险高时，向用户问一个简短问题。 |
| 创建新 skill | 确认名称、用途、触发场景、目标平台和是否需要脚本/引用/资产；未指定平台时默认写跨平台 Agent Skill。只创建有实际内容的目录，不创建空目录占位。 |
| 需求设计 | 对复杂或模糊需求，先用 brief 固化目标、触发边界、资源计划和验收标准；确认后再创建或重构 skill。 |
| 平台兼容 | Codex-only 内容、Claude-only frontmatter、通用 Agent Skills 字段要分开标注；不要把某个平台的扩展写成所有平台都需要。 |
| 参考开源实现 | 用户要求参考、领域陌生、skill 较复杂或准备开源时，可查本地 skills、GitHub 或开源 skill 社区；网络不可用、用户不希望联网或涉及内部隐私时跳过。 |
| 审核 skill | 先给必须修复项，再给建议优化项；用文件路径和具体原因说明；发现空目录应建议删除。 |
| 生成脚本 | 只有需要确定性执行、反复复用或易出错流程时才添加脚本；新增脚本必须实际运行代表性测试。 |
| 开源发布 | 可以编写面向人的 `README.md`，但不要让 README 替代 `SKILL.md`、`references/` 或校验脚本。 |
| 危险操作 | 删除、覆盖、发布、生产变更等不可逆操作，先展示影响范围并获得明确确认。 |

## 边界

- 不把本 skill 当成普通代码生成、业务需求分析或通用项目管理 skill。
- 不把团队偏好升级为官方硬性规范；只有加载、触发或基本执行会失败的问题才列为“必须修复”。
- 不为小型 skill 强制创建 `scripts/`、`references/`、`assets/`、配置框架或 README。
- 不把临时 skill brief、讨论记录或实现计划自动放进最终 skill 包；只有会指导未来运行的稳定内容才转为 `references/`。
- 不把 GitHub README 作为运行时资源；README 只服务开源介绍、安装和贡献说明。
- 不把 `agents/openai.yaml` 当成 Claude 必需文件；不把 Claude Code 的 `when_to_use`、`context`、`disable-model-invocation` 等扩展当成 Codex 必需字段。
- 不把开源参考当成必须步骤；不要直接复制大段第三方内容、忽略许可证，或把外部实现当作当前项目规范。

## 操作路由

按用户目标读取对应文档：

| 目标 | 何时读取 | 文档 |
|---|---|---|
| 平台兼容 | 用户提到 Codex、Claude、Claude Code、Agent Skills、安装路径、frontmatter 差异、校验方式或跨平台发布 | `references/platforms.md` |
| 创建或重构 skill | 用户要新建 skill、现有 skill 结构需要明显调整，或需要参考开源/本地同类 skill | `references/create-skill.md` |
| 需求澄清和设计 | 用户需求复杂、模糊、需要先敲定方案，或触发边界、资源分层、验收标准还不清楚 | `references/design-workflow.md` |
| 编写或修正 `SKILL.md` | 需要调整 frontmatter、触发描述、入口正文、资源导航 | `references/skill-md-template.md` |
| 生成或审核脚本 | 需要 `scripts/`、CLI、配置读取、确定性工具 | `references/script-template.md` |
| 生成或审核配置 | skill 需要 token、API key、路径、环境变量等配置 | `references/config-template.md` |
| 审核规范 | 用户要求检查、review、audit、验证 skill | `references/check-skill.md` |
| 需要完整参考 | 用户要求示例，或当前设计缺少可参照的整体形态 | `references/full-example.md` |
| 解释基础概念 | 用户不熟悉 skill、frontmatter、渐进加载或资源类型 | `references/concepts.md` |
| 排查常见问题 | 触发不准、结构臃肿、资源不可发现、脚本未验证等问题 | `references/common-mistakes.md` |
| GitHub 开源发布 | 用户要求写 README、打包发布、说明安装或贡献方式 | `references/open-source-readme.md` |

## 校验

创建或修改完成后，按目标平台校验。Codex 基础校验：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>
```

通用项目增强检查：

```bash
python3 SKILL_DIR/scripts/common/check_skill_structure.py <skill-folder> --platform agent
```

自定义检查脚本用于发现项目约定和质量建议，不应替代 Codex、Claude 或 Agent Skills 官方/参考校验。

## 审核等级

| 等级 | 含义 | 示例 |
|---|---|---|
| 必须修复 | 会影响目标平台发现、加载或基本使用 | 缺少 `SKILL.md`、frontmatter 无效、跨平台 skill 缺少 `name` 或 `description`、`name` 非 hyphen-case。 |
| 建议优化 | 不一定破坏使用，但会降低触发、维护或验证质量 | `description` 触发场景不清楚、`SKILL.md` 过长、资源导航不清晰、脚本未测试、平台扩展未标注。 |
| 项目约定 | 只在当前团队明确采用时执行 | 固定目录模板、配置文件格式、特定脚本框架、内部输出格式。 |

## 输出要求

审核时给出结论、问题清单和建议修改方向。创建 brief 时说明保存位置和待确认点。完成修改时说明改了哪些文件、运行了哪些校验、还有哪些残余风险。
