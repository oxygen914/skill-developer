# 创建或重构 Skill

## 1. 收集最小必要信息

先判断已有上下文是否足够。能合理推断时直接继续；缺少关键决策时再问用户。

通常需要明确：

- `name`：小写字母、数字和连字符，建议与目录名一致。
- `description`：说明 skill 做什么，以及何时触发。
- 典型请求：用户会怎样描述这个任务。
- 资源需求：是否需要 `references/`、`scripts/`、`assets/`。
- 语言策略：面向全球用户优先英文；面向中文团队可用中文正文，并在 `description` 保留英文触发词或中英双语。
- 安装位置：未指定时使用 `$CODEX_HOME/skills`，若未设置则使用 `~/.codex/skills`。

如果需求复杂、模糊、触发边界难判断，先读取 `references/design-workflow.md`，用 skill brief 固化目标、边界、资源计划和验收标准。用户确认后再实施。小型明确 skill 可以跳过 brief。

## 2. 设计确认（复杂需求）

使用 brief 时，至少确认：

- skill 要解决的核心任务和非目标。
- should trigger / should not trigger 的边界。
- 3-5 个典型用户请求。
- 运行时流程和需要读取的资源。
- 哪些内容进入 `SKILL.md`，哪些拆进 `references/`，哪些做成 `scripts/` 或 `assets/`。
- 验收标准：官方校验、脚本测试、真实请求前向测试。

把临时 brief 保存在最终 skill 目录外，例如 `.skill-work/<skill-name>/skill-brief.md`。不要把需求讨论、设计草案或实现计划默认打包进最终 skill。

## 3. 参考发现（可选）

不要把参考发现当成所有 skill 的必经步骤。仅在这些场景使用：

- 用户明确要求“参考 GitHub / 开源社区 / 类似 skill”。
- 任务领域陌生，已有开源 skill 可能提供结构模式。
- skill 较复杂，需要判断 `references/`、`scripts/`、`assets/` 如何分层。
- 用户准备开源发布，需要对齐社区常见 README、许可和安装说明。

推荐顺序：

1. 先查本地已有 skills，避免重复设计。
2. 再按需检索 GitHub、官方示例或开源 skill 社区。
3. 只提炼可迁移的设计模式：触发描述、目录结构、资源导航、脚本接口、校验流程、README 边界。
4. 记录参考来源；如果借鉴代码、模板或大段文字，检查许可证和署名要求。

跳过条件：

- 用户不希望联网，或当前网络不可用。
- skill 很小，已有上下文足够直接实现。
- 任务包含内部业务、私有 API、凭证、客户数据或不适合外发检索的细节。
- 参考资料许可证不清楚，且需要复制代码或模板。

输出时不要直接倾倒搜索结果。只总结对当前 skill 有用的设计取舍，并说明哪些参考被采用、哪些被忽略。

## 4. 选择结构

最小结构：

```text
<skill-name>/
└── SKILL.md
```

按需添加（只在有实际内容时创建）：

```text
<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── <topic>.md
├── scripts/
│   └── <tool>.py
└── assets/
    └── <reusable-file>
```

添加规则：

- `references/`：用于长流程、领域规则、API 说明、示例、检查清单。
- `scripts/`：用于确定性操作、重复代码、易出错的流程；新增后必须运行代表性测试。
- `assets/`：用于输出中会复制或引用的模板、图片、字体、示例项目等。
- `agents/openai.yaml`：推荐添加，用于 UI 展示；只放面向界面的简短元信息。

禁止事项：

- **禁止创建空目录**：不要创建 `scripts/`、`assets/`、`agents/`、`tests/` 等空目录占位。空目录不参与 skill 运行，只会造成维护困惑。
- 不要默认创建 README、CHANGELOG、安装指南。只有当用户明确要求 GitHub 开源发布、仓库展示或贡献说明时，才添加面向人的 `README.md`；README 不能替代 `SKILL.md` 或 `references/`。

## 5. 编写 SKILL.md

Frontmatter 只需要：

```yaml
---
name: <skill-name>
description: <what the skill does and when to use it>
---
```

正文建议包含：

- 核心工作流。
- 何时读取哪些引用文件。
- 何时运行哪些脚本。
- 校验或测试步骤。
- 重要安全/确认规则。

避免：

- 把“何时使用本 skill”只写在正文，因为正文只有触发后才加载。
- 把所有细节堆进 `SKILL.md`。
- 为每个 skill 强制“初始化检查”“操作路由”“配置管理”等固定章节。
- 把 GitHub README 当作运行时说明；README 是开源包装，`SKILL.md` 才是 Codex 的入口。

## 6. 使用官方初始化脚本

创建全新 skill 时，优先使用官方脚本：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py <skill-name> --path <output-dir> --resources references,scripts
```

只传实际需要的资源类型。初始化后删除占位内容，补充真实说明和资源。

## 7. 生成 agents/openai.yaml

推荐使用官方脚本生成 UI 元信息：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/generate_openai_yaml.py <skill-folder> \
  --interface display_name="<display name>" \
  --interface short_description="<short description>" \
  --interface default_prompt="Use $<skill-name> to <example task>."
```

`default_prompt` 用英文通常更通用；如果 skill 只服务中文团队，也可以使用中文或中英双语。只在用户明确提供或项目需要时添加 icon、brand_color、依赖工具等字段。

## 8. 校验

基础校验：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>
```

项目增强校验：

```bash
python3 <path-to-skill-developer>/scripts/common/check_skill_structure.py <skill-folder>
```

复杂 skill 还要用 2-3 个真实用户请求前向测试：确认能触发、能找到所需引用、能正确执行或说明限制。

## 9. 开源发布补充

当用户准备上传到 GitHub：

- 写 `README.md`，说明定位、安装、使用示例、校验命令、贡献方式和许可证状态。
- 检查 README 中的命令和目录结构是否与实际文件一致。
- 确认没有私有 token、内部 URL、个人路径或未授权素材。
- 提醒用户在发布前添加明确的 `LICENSE` 文件；不要替用户默认选择许可证，除非用户指定。
