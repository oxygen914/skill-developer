# 完整示例：轻量文件整理 Skill

这个示例展示“按需添加资源”的形态，不是所有 skill 都必须照抄。

## 目录

```text
organize-files/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── rules.md
└── scripts/
    └── organize.py
```

## SKILL.md

```markdown
---
name: organize-files
description: |
  Organize local files into project-specific folders using deterministic naming rules and optional dry-run previews. Use when the user asks to sort, rename, clean up, or reorganize files in a directory, especially when they want a preview before changes.
---

# Organize Files

Use this skill to inspect a directory, propose deterministic file moves, and apply them only after confirmation.

## Workflow

1. Read `references/rules.md` before proposing a file organization plan.
2. Run `scripts/organize.py --dry-run <dir>` to preview moves.
3. Show the user a concise summary of affected files.
4. Apply changes only after explicit confirmation.
5. Run the dry-run again or list the target directories to verify the result.

## Resources

- `references/rules.md`: Naming and grouping rules.
- `scripts/organize.py`: Dry-run and apply file moves.

## Safety

Never delete files. For move/rename operations, show source and destination counts before applying.
```

## agents/openai.yaml

```yaml
interface:
  display_name: "Organize Files"
  short_description: "Sort and rename files with previews"
  default_prompt: "Use $organize-files to preview a cleanup plan for this folder."
```

## references/rules.md

```markdown
# File Organization Rules

- Group documents by extension first, then by date prefix when available.
- Preserve original filenames unless the user asks for renaming.
- Never overwrite existing files; append a numeric suffix when needed.
- Use dry-run mode before any move.
```

## scripts/organize.py

Use the CLI style from `references/script-template.md`: parse arguments, support `--dry-run`, emit JSON, and return nonzero on errors.

## 校验

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py organize-files
python3 organize-files/scripts/organize.py --dry-run ./sample-folder
```
