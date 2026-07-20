<p align="center">
  <img src="assets/readme/skill-developer/wordmark.webp" alt="Skill Developer 动态标题" width="720" />
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

# Skill Developer

Skill Developer 是一个用于设计、创建、重构、审核、验证和准备发布其他 Skill 的 Agent Skill，面向通用 Agent Skills、Codex 与 Claude Code。

它可以把早期想法或已有 Skill 目录整理成触发边界清楚、资源分层明确、平台差异可解释、验证流程可复现的 Skill 包。运行时事实来源是 [SKILL.md](SKILL.md)；本 README 只服务人类读者的安装、使用和维护。

## 为什么需要它

一个可用的 Skill 不只是一个写满说明的 Markdown 文件，还需要回答：

- 哪些用户请求应该触发，哪些不应该触发？
- 什么内容留在 `SKILL.md`，什么内容应该拆到 `references/`？
- 哪些重复、确定性或易错操作值得实现成脚本？
- 哪些文件属于可移植的 Agent Skills 结构，哪些只针对 Codex 或 Claude Code？
- 审核时如何区分真正影响加载的问题、质量建议和团队自己的约定？
- 哪些检查能够证明 Skill 至少可以被发现、加载并完成基础执行？

Skill Developer 会在增加目录和文件之前先明确这些决策。范围清楚的小改动可以直接实施；复杂、模糊或边界敏感的需求可以先沉淀成一份可确认的 Skill brief。

## 核心能力

- **需求设计**：明确目标、非目标、目标客户端、触发示例、输出契约、风险和验收标准。
- **创建与重构**：从最小 Skill 包开始，只在有实际用途时加入 `references/`、`scripts/`、`assets/` 或 `agents/`。
- **改进触发**：让 `description` 同时说明 Skill 能做什么以及何时应该使用。
- **资源分层**：保持运行时入口轻量，把详细规则、模板、示例和确定性工具路由到正确位置。
- **处理平台差异**：区分通用 Agent Skills 约定、Codex 元数据和 Claude Code 扩展。
- **审核现有 Skill**：按“必须修复、建议优化、项目约定”输出问题。
- **执行验证**：运行 Codex 基础校验和仓库内置的跨平台结构检查器。
- **准备公开发布**：检查仓库结构、README、验证说明、敏感信息和许可证状态。

## 支持目标

| 目标 | 核心支持 | 平台相关行为 |
| --- | --- | --- |
| Agent Skills | 带 `name`、`description` 的 `SKILL.md`，以及可选的 `references/`、`scripts/`、`assets/` | 默认使用最小跨平台结构 |
| Codex | 安装到 `${CODEX_HOME:-$HOME/.codex}/skills` | 支持 `agents/openai.yaml` 和 Codex `quick_validate.py` |
| Claude Code | 安装到个人级或项目级 `.claude/skills` 目录 | 说明斜杠命令发现方式，并显式标注 Claude 专属 frontmatter |

支持多个平台并不表示所有字段通用。例如，`agents/openai.yaml` 用于 Codex/OpenAI 展示元数据，不是 Claude Code 的必需文件。详细边界见[平台兼容指南](references/platforms.md)。

## 工作方式

### 1. 理解需求

Skill 会识别目标客户端、目标用户、典型请求、期望输出和重要非目标。已经可以从对话或仓库得到的信息不会重复询问。

### 2. 判断是否需要设计稿

修正描述、补资源路由、运行校验等小改动可以直接继续。

复杂、模糊或安全边界敏感的 Skill 可以先生成：

```text
.skill-work/<skill-name>/skill-brief.md
```

Brief 会记录触发与非触发示例、资源计划、依赖、风险和验收标准。它默认位于运行时 Skill 包之外，除非其中的内容后来被整理成稳定的运行规则。

### 3. 构建最小可用结构

最小有效结构是：

```text
<skill-name>/
└── SKILL.md
```

只有实际需要时才增加：

```text
<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── <topic>.md
├── scripts/
│   └── <deterministic-tool>
└── assets/
    └── <reusable-output-asset>
```

不会创建空目录占位。

### 4. 路由知识与操作

- `SKILL.md`：触发元数据、核心工作流、安全规则和资源导航。
- `references/`：只在相关任务中加载的详细流程、领域规则、模板、示例和检查清单。
- `scripts/`：确定性、可重复或容易出错的操作，应提供清晰接口和代表性验证。
- `assets/`：Skill 会读取、复制或输出的可复用文件。
- `agents/openai.yaml`：可选的 Codex/OpenAI UI 元数据。

### 5. 针对目标平台验证

Skill 会运行适用校验器，检查直接资源引用、脚本语法和元数据，并明确列出尚未验证的行为，而不是把静态检查描述成完整运行时证明。

## 安装

克隆仓库：

```bash
git clone https://github.com/oxygen914/skill-developer.git
cd skill-developer
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R . "${CODEX_HOME:-$HOME/.codex}/skills/skill-developer"
```

### Claude Code

个人级安装：

```bash
mkdir -p ~/.claude/skills
cp -R . ~/.claude/skills/skill-developer
```

项目级安装：

```bash
mkdir -p /path/to/project/.claude/skills
cp -R . /path/to/project/.claude/skills/skill-developer
```

安装后刷新或重启对应客户端，使其重新发现 Skill 元数据。

> 上述命令会同时复制仓库发布文件和运行时文件。如果自行构建精简发布包，应确保 `SKILL.md` 与它直接引用的所有资源一起保留。

## 快速开始

### 设计跨平台 Skill

```text
用 $skill-developer 设计一个跨平台发布检查 Skill。实现前先明确应该触发和不应该触发的请求。
```

### 创建 Codex Skill

```text
用 $skill-developer 创建一个审核 API 文档的 Codex Skill。保持 SKILL.md 轻量，只按需添加 references，并验证最终结果。
```

### 审核现有 Skill

```text
用 $skill-developer 审核当前 Skill 对 Agent Skills、Codex 和 Claude Code 的兼容性，必须修复和建议优化分开写。
```

### 准备 GitHub 发布

```text
用 $skill-developer 检查这个 Skill 是否适合公开发布，核对 README、资源路径、验证命令、敏感信息和许可证状态。
```

在 Claude Code 中，安装后也可以显式调用：

```text
/skill-developer
```

## 典型输出

| 请求类型 | 常见输出 |
| --- | --- |
| 需求设计 | 包含目标、边界、触发、资源、风险和验收标准的 Skill brief |
| 创建或重构 | 最小运行时 Skill 包和对应验证结果 |
| 审核 | 结论、必须修复、建议优化、平台约定和已验证项目 |
| 发布准备 | 面向人类的 README 检查、仓库卫生问题、验证状态和许可证风险 |

## 审核等级

Skill Developer 有意区分三种问题：

| 等级 | 含义 | 示例 |
| --- | --- | --- |
| 必须修复 | 会阻止目标客户端发现、加载或基本使用 | 缺少 `SKILL.md`、frontmatter 无效、缺少 `name` 或 `description`、直接资源引用失效 |
| 建议优化 | 不一定破坏执行，但会降低触发、维护或验证质量 | `SKILL.md` 过重、资源路由不清楚、脚本未测试、触发描述过弱 |
| 项目约定 | 只有特定客户端或团队明确采用时才适用 | 固定目录模板、内部配置模式、Claude 专属 frontmatter、可选 Codex UI 元数据 |

这种分级可以避免把项目偏好包装成所有 Agent Skills 的通用要求。

## 仓库导航

| 路径 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 运行时入口、工作流、边界和资源路由 |
| [agents/openai.yaml](agents/openai.yaml) | Codex/OpenAI 展示元数据 |
| [references/design-workflow.md](references/design-workflow.md) | 面向复杂或模糊需求的可选 Skill brief 流程 |
| [references/create-skill.md](references/create-skill.md) | 完整创建和重构流程 |
| [references/skill-md-template.md](references/skill-md-template.md) | Frontmatter、触发描述、正文和资源导航指南 |
| [references/platforms.md](references/platforms.md) | Agent Skills、Codex 与 Claude Code 差异 |
| [references/check-skill.md](references/check-skill.md) | 审核顺序、问题等级和报告格式 |
| [references/common-mistakes.md](references/common-mistakes.md) | 常见触发、结构和验证问题 |
| [references/script-template.md](references/script-template.md) | 确定性脚本和 CLI 契约指南 |
| [references/config-template.md](references/config-template.md) | 路径、环境变量和凭证配置模式 |
| [references/full-example.md](references/full-example.md) | 精简但完整的 Skill 示例 |
| [references/open-source-readme.md](references/open-source-readme.md) | 面向人类的 README 和发布清单 |
| [scripts/common/check_skill_structure.py](scripts/common/check_skill_structure.py) | 跨平台结构与可维护性检查器 |

## 验证

在仓库根目录运行 Codex 基础校验：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

分别运行内置检查器：

```bash
python3 scripts/common/check_skill_structure.py . --platform agent
python3 scripts/common/check_skill_structure.py . --platform codex
python3 scripts/common/check_skill_structure.py . --platform claude
```

成功时返回：

```json
{
  "ok": true,
  "platform": "agent",
  "skill_path": "/resolved/path/to/skill-developer",
  "errors": [],
  "warnings": []
}
```

内置检查器用于补充目标平台校验器，不能替代它们。复杂 Skill 还应使用代表性用户请求做前向测试，确认触发、引用发现和主工作流可以正常执行。

## 设计原则

- 优先建立可移植的 Agent Skills 基础，再增加客户端专属行为。
- 保持运行时入口轻量，通过渐进加载读取详细资源。
- 只有能够减少重复、提高可靠性或承载必要知识时才增加文件。
- 脚本用于确定性工作，而不是默认包裹模型推理。
- 临时计划和发布文档与运行时说明分开保存。
- 显式说明平台差异，不笼统声称所有行为完全兼容。
- 把验证结果作为证据，并标注尚未测试的内容。
- 复制第三方实现前检查许可证和署名要求。

## 使用边界

Skill Developer 不是通用代码生成器、业务需求分析器或项目管理系统。它不会：

- 强制所有 Skill 使用同一个目录模板；
- 把 Codex 或 Claude Code 扩展当作通用必需项；
- 为未来可能使用的结构创建空目录；
- 把团队偏好升级为必须修复问题；
- 把 README 或设计 brief 当作运行时指令；
- 声称静态检查能够证明所有真实调用路径；
- 代替仓库所有者选择许可证。

## 参与贡献

提交修改时：

1. 让 `SKILL.md` 聚焦触发、核心工作流和资源导航。
2. 把可复用的详细规则放入最相关的 `references/` 文件。
3. 只为确定性或反复易错操作增加脚本。
4. 用户可见行为变化时同步更新 [README.md](README.md) 与 [README-CN.md](README-CN.md)。
5. 运行 Codex 校验器和三种平台增强检查。
6. 影响触发或行为时补充代表性前向测试。

## License

当前仓库没有 `LICENSE` 文件。按当前状态，仓库未授予开源许可；在分发或将其描述为开源项目前，应先添加明确许可证。
