# Skill 审核清单

## 审核顺序

1. 先跑官方基础校验。
2. 再人工检查触发描述、正文结构、资源分层和脚本可运行性。
3. 如项目采用增强规范，再跑本 skill 的自定义检查脚本。
4. 输出时按“必须修复 / 建议优化 / 项目约定”分级。

## 命令

官方基础校验：

```bash
python3 /Users/didi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>
```

项目增强校验：

```bash
python3 SKILL_DIR/scripts/common/check_skill_structure.py <skill-folder>
```

## 必须修复

- 缺少 `SKILL.md`。
- `SKILL.md` 没有合法 YAML frontmatter。
- frontmatter 缺少 `name` 或 `description`。
- `name` 不是 hyphen-case，或超过 64 个字符。
- `description` 为空，或完全无法判断何时触发。
- 目录名与 `name` 不一致，且没有明确原因。
- `SKILL.md` 引用了不存在的直接资源文件。

## 建议优化

- `description` 没有覆盖常见触发词、任务场景、文件类型或平台名。
- `SKILL.md` 过长，细节应拆到 `references/`。
- 详细信息在 `SKILL.md` 和 `references/` 重复维护。
- 资源导航只列文件，不说明何时读取。
- 大型 reference 文件没有目录或检索提示。
- 脚本存在但没有运行说明或代表性测试。
- 新增脚本没有错误处理、参数说明或用户友好输出。
- 缺少 `agents/openai.yaml`，导致 UI 展示信息不可控。
- 用户要求 GitHub 开源发布时，README 缺少安装、使用、校验、贡献或许可证说明。

## 项目约定

只有当团队明确采用时才作为问题：

- 固定的 `scripts/common/config.py` 配置框架。
- 固定的 `assets/knowledge/` 知识目录。
- 固定的“初始化检查”章节。
- 固定的“操作路由”表格。
- 每个操作都必须有 `references/<operation>.md`。
- 所有配置都必须支持环境变量。
- 禁止所有 README；如果 README 明确用于 GitHub 开源发布，它属于发布包装而非运行时资源。

## 输出模板

```markdown
结论：<通过 / 有必须修复项 / 仅有建议优化>

必须修复：
- <文件:行号> <问题>。原因：<为什么影响加载/触发/使用>。

建议优化：
- <文件:行号> <问题>。建议：<如何修改>。

已验证：
- <运行的命令和结果>。
```

如果没有问题，明确说明“未发现必须修复项”，并列出仍未覆盖的测试或风险。

## GitHub 发布检查

当用户准备开源：

- README 应说明这是 Codex skill，并给出安装目录。
- README 的命令应可复制运行。
- README 不应包含私有凭证、内部 API、个人绝对路径或未授权资源。
- 仓库应有明确许可证；没有许可证时，把它列为发布前风险。
