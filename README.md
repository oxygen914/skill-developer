<p align="center">
  <img alt="Skill Developer" src="assets/skill-developer-title.svg" width="720">
</p>

# Skill Developer

Skill Developer 是一个用于设计、创建、改进、审核、验证和开源发布 Agent Skills 的辅助 skill。它默认面向跨平台 Agent Skills，同时完整兼容 Codex 和 Claude Code。

它适合把一个模糊的 skill 想法，逐步整理成可触发、可维护、可验证、可发布的标准 skill 包。它的重点不是“多生成几个文件”，而是帮你判断：哪些内容应该放进 `SKILL.md`，哪些长规则应该拆到 `references/`，哪些重复或易错流程应该做成 `scripts/`，哪些素材才需要进入 `assets/`，以及哪些内容只是面向 GitHub 的发布包装。

## 兼容性

| 平台 | 支持状态 | 说明 |
|---|---|---|
| Agent Skills 标准 | 完整兼容 | 默认使用 `SKILL.md` + `name` / `description` + `references/` / `scripts/` / `assets/` 的通用结构。 |
| Codex | 完整兼容 | 支持 `$CODEX_HOME` / `~/.codex/skills` 安装、`agents/openai.yaml` UI 元信息和 Codex 官方 `quick_validate.py`。 |
| Claude Code | 完整兼容 | 支持 `~/.claude/skills` 和项目 `.claude/skills` 安装，可用 `/skill-developer` 调用，并能设计/审核 Claude Code 扩展 frontmatter。 |

## 适合做什么

- 从模糊需求开始，先设计 skill brief，再确认实现方向。
- 创建或重构跨平台 Agent Skill、Codex skill 或 Claude Code skill。
- 编写更准确的 `description`，让 skill 更容易被正确触发。
- 区分通用字段、Codex 专属资源和 Claude Code 扩展字段。
- 判断什么时候需要 `references/`、`scripts/`、`assets/`、`agents/openai.yaml`。
- 审核现有 skill，并区分“必须修复”“建议优化”“平台约定”。
- 运行通用检查、Codex 校验和 Claude 兼容性检查。
- 为准备上传 GitHub 的 skill 编写 README 和发布说明。

## 核心工作流

简单明确的 skill，可以直接进入创建或修改。

复杂、模糊、边界敏感的 skill，建议先走设计流程：

1. 确认目标平台：通用 Agent Skills、Codex、Claude Code，或多平台兼容。
2. 澄清 skill 的用途、非目标、触发边界和典型用户请求。
3. 生成一份 skill brief，默认保存在 `.skill-work/<skill-name>/skill-brief.md`。
4. 和用户确认 brief，再开始创建或大改 skill。
5. 把稳定的运行时规则写入 `SKILL.md` 或 `references/`。
6. 只有确定性、重复性、易出错的流程才做成 `scripts/`。
7. 创建或修改完成后按目标平台运行校验，复杂 skill 再用真实请求做前向测试。

临时 brief、讨论记录、实现计划不要默认放进最终 skill 包。只有未来运行时也需要读取的稳定知识，才应该转成 `references/`。

## 安装

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill-developer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后重启或刷新 Codex，让 skill metadata 被重新发现。

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

Claude Code 中可直接调用：

```text
/skill-developer
```

也可以让 Claude 根据 `description` 自动判断是否使用本 skill。

## 使用示例

```text
Use $skill-developer to design a cross-platform skill for managing recurring project checklists.
```

```text
Use $skill-developer to create a Claude Code skill for release checklist automation.
```

```text
Use $skill-developer to audit this Codex skill for compatibility.
```

```text
Use $skill-developer to improve this SKILL.md and prepare a GitHub README.
```

中文也可以直接说：

```text
用 $skill-developer 帮我设计一个同时兼容 Codex 和 Claude Code 的周报 skill，先和我确认需求再创建。
```

## 仓库结构

```text
skill-developer/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   `-- skill-developer-title.svg
|-- references/
|   |-- check-skill.md
|   |-- common-mistakes.md
|   |-- concepts.md
|   |-- config-template.md
|   |-- create-skill.md
|   |-- design-workflow.md
|   |-- full-example.md
|   |-- open-source-readme.md
|   |-- platforms.md
|   |-- script-template.md
|   `-- skill-md-template.md
`-- scripts/
    `-- common/
        `-- check_skill_structure.py
```

## 重要文件

- `SKILL.md`：运行时入口，包含触发描述、核心原则、操作路由和校验说明。
- `agents/openai.yaml`：Codex/OpenAI UI 展示信息；Claude Code 会忽略它。
- `assets/skill-developer-title.svg`：GitHub README 顶部标题图。
- `references/platforms.md`：Agent Skills、Codex、Claude Code 的兼容性差异。
- `references/design-workflow.md`：复杂或模糊需求的 skill brief 设计流程。
- `references/create-skill.md`：创建或重构 skill 的完整流程。
- `references/skill-md-template.md`：`SKILL.md` frontmatter、触发描述、正文结构和资源导航模板。
- `references/check-skill.md`：审核清单和输出格式。
- `references/common-mistakes.md`：常见问题与修正方式。
- `references/concepts.md`：Agent Skill 核心概念说明。
- `references/script-template.md`：确定性脚本的 CLI 模板和测试建议。
- `references/config-template.md`：需要 token、路径或服务配置时的配置模式。
- `references/full-example.md`：完整轻量示例。
- `references/open-source-readme.md`：面向 GitHub 开源发布的 README 编写指南。
- `scripts/common/check_skill_structure.py`：项目增强检查器，用于发现结构、平台兼容性和维护性问题。

## 校验

运行 Codex 官方基础校验：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

运行通用 Agent Skill 检查：

```bash
python3 scripts/common/check_skill_structure.py . --platform agent
```

运行 Claude Code 兼容性检查：

```bash
python3 scripts/common/check_skill_structure.py . --platform claude
```

运行 Codex 兼容性检查：

```bash
python3 scripts/common/check_skill_structure.py . --platform codex
```

期望通用检查结果：

```json
{
  "ok": true,
  "errors": [],
  "warnings": []
}
```

## 设计原则

- 默认生成跨平台 Agent Skill，只在用户指定时加入 Codex 或 Claude Code 扩展。
- `SKILL.md` 保持轻量，只放触发、核心流程和资源导航。
- 长规则、模板、示例、检查清单放到 `references/`。
- 脚本只用于确定性、重复性或易出错的流程。
- `assets/` 只放真正会被输出或展示使用的素材。
- 不创建空目录占位。
- 不把团队偏好误判成官方硬性规范。
- 不把 GitHub README 当成运行时资源。
- 不把 `agents/openai.yaml` 写成 Claude 必需文件。
- 不把 Claude Code 扩展 frontmatter 写成 Codex 必需字段。

## 参考资料

- Claude Code Skills: <https://code.claude.com/docs/en/skills>
- Agent Skills Specification: <https://agentskills.io/specification>

## GitHub 发布前检查

- 确认 README 的目录结构和实际文件一致。
- 运行目标平台校验和项目增强检查。
- 确认没有 token、私有 URL、内部账号、个人绝对路径或未授权素材。
- 如果准备公开发布，补充明确的 `LICENSE` 文件。

## License

当前仓库还没有 `LICENSE` 文件。公开发布前建议选择并添加合适的开源许可证。
