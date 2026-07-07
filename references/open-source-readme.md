# GitHub 开源 README 指南

当用户明确要求把 skill 上传到 GitHub 或开源发布时，编写面向人类读者的 `README.md`。README 是发布包装，不是 agent 运行时资源。

## 推荐内容

- 项目名称和一句话定位。
- 这个 skill 解决什么问题。
- 目录结构，突出 `SKILL.md`、`references/`、`scripts/`、`assets/`，以及 Codex 可选的 `agents/openai.yaml`。
- 安装方式：分别说明 Codex 的 `$CODEX_HOME/skills` / `~/.codex/skills` 和 Claude Code 的 `~/.claude/skills` / `.claude/skills`。
- 使用示例：用自然语言触发 skill 的典型请求。
- 校验方式：目标平台校验命令和可选自定义检查器；Codex 项目可列出官方 `quick_validate.py`。
- 贡献方式：如何改 `SKILL.md`、references、scripts，并要求运行校验。
- License 状态：如果仓库还没有 LICENSE，提醒发布前选择许可证。

## 不要做

- 不要让 README 替代 `SKILL.md`。
- 不要把长模板重复粘贴到 README。
- 不要把 token、私有路径、内部账号或真实凭证写进 README。
- 不要承诺未实现的功能。

## 发布前检查

1. 运行目标平台基础校验。
2. 运行项目自定义检查器。
3. 确认 README 中的路径、命令和文件结构与仓库一致。
4. 确认没有私有凭证、内部 URL 或无关大文件。
5. 添加或确认开源许可证。
