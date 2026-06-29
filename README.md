# Skill Developer

Skill Developer is a Codex skill for creating, improving, auditing, validating, and preparing Codex skill packages for open-source release.

It helps keep `SKILL.md` concise, makes bundled resources discoverable, separates official requirements from project conventions, and provides a lightweight checker for common skill structure issues.

## What It Helps With

- Create or refactor Codex skills with valid `SKILL.md` frontmatter.
- Write trigger descriptions that make skills discoverable.
- Decide when to use `references/`, `scripts/`, `assets/`, and `agents/openai.yaml`.
- Audit skills with clear severity levels: required fixes, recommended improvements, and project conventions.
- Validate skill packages with the official validator and an optional project-level checker.
- Prepare a skill repository for GitHub open-source publishing.

## Repository Structure

```text
skill-developer/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── check-skill.md
│   ├── common-mistakes.md
│   ├── concepts.md
│   ├── config-template.md
│   ├── create-skill.md
│   ├── full-example.md
│   ├── open-source-readme.md
│   ├── script-template.md
│   └── skill-md-template.md
└── scripts/
    └── common/
        ├── check_skill_structure.py
        └── config.py
```

`README.md` is for GitHub and human readers. Codex uses `SKILL.md` as the runtime entry point.

## Installation

Clone or copy this folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill-developer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

After installation, restart or refresh Codex so the skill metadata can be discovered.

## Usage

Ask Codex to use the skill in natural language:

```text
Use $skill-developer to audit this skill for Codex compatibility.
```

```text
Use $skill-developer to create a new skill for PDF redaction.
```

```text
Use $skill-developer to improve this SKILL.md and prepare a GitHub README.
```

## Validation

Run the official baseline validator:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

Run the optional project-level checker:

```bash
python3 scripts/common/check_skill_structure.py .
```

Expected result for this repository:

```json
{
  "ok": true,
  "errors": [],
  "warnings": []
}
```

## Design Principles

- Keep `SKILL.md` small and action-oriented.
- Put long explanations, templates, and checklists in `references/`.
- Add scripts only when deterministic execution or repeated automation is useful.
- Treat `assets/` as output resources, not reading material.
- Separate official Codex requirements from team-specific conventions.
- Treat GitHub documentation as publishing material, not as Codex runtime instructions.

## Contributing

When changing this skill:

1. Keep trigger conditions in the frontmatter `description`.
2. Keep resource navigation in `SKILL.md` explicit: say when each reference or script should be used.
3. Add or update references instead of making `SKILL.md` overly long.
4. Run both validation commands before opening a pull request.
5. Do not include real tokens, private URLs, internal account names, or personal absolute paths.

## License

This repository does not include a `LICENSE` file yet. Choose and add an open-source license before publishing publicly on GitHub.
