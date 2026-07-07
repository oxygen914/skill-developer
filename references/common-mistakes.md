# 常见问题

## 1. description 太空

问题：

```yaml
description: 文件处理工具
```

风险：agent 不知道什么请求应触发这个 skill。

改法：

```yaml
description: |
  Process local PDF and DOCX files by extracting text, splitting pages, and producing structured Markdown summaries. Use when the user asks to extract, convert, split, summarize, or inspect document files.
```

## 2. 把触发条件只写在正文

正文只有触发后才加载。触发条件必须进入 frontmatter `description`。

## 3. 固定套用大型目录

问题：小 skill 也创建空 `scripts/`、`assets/knowledge/`、`tests/`、README。

改法：从最小结构开始，只添加真正需要的资源。

## 4. SKILL.md 过长

问题：入口文件包含大量 API 文档、示例、模板和背景知识。

改法：保留核心流程，把详细资料拆到 `references/`，并在入口里说明何时读取。

## 5. 引用资源没有导航

问题：

```markdown
参考文件：api.md、faq.md、examples.md
```

改法：

```markdown
- Read `references/api.md` before calling the API.
- Read `references/examples.md` when creating a new workflow.
- Read `references/faq.md` only when answering usage questions.
```

## 6. 脚本存在但未验证

新增脚本后必须实际运行代表性命令。只检查语法不够，至少要覆盖一次正常路径和一次错误路径。

## 7. 把项目约定当官方规范

这些可以作为团队偏好，但不应默认判定所有 skill 不合格：

- 必须有“初始化检查”。
- 必须有“操作路由表”。
- 必须有 `scripts/common/config.py`。
- 必须有 `assets/knowledge/`。
- 必须有 README。
- 必须有 author/version。

## 8. 审核输出没有分级

把所有建议都写成“必须修复”会误导后续维护。输出时区分：

- 必须修复：影响加载、触发或基本使用。
- 建议优化：提升触发准确性、维护性或验证质量。
- 项目约定：只有团队采用时才执行。

## 9. README 和 SKILL.md 职责混淆

GitHub README 面向人类读者，适合写项目介绍、安装、使用示例和贡献方式。

`SKILL.md` 面向 agent，必须保留触发描述、核心流程、资源导航和校验规则。不要把运行时指令只写进 README。
