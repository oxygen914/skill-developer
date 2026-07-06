# Skill Developer

Skill Developer is a Codex skill for designing, creating, improving, auditing, validating, and preparing Codex skill packages for open-source release.

It helps Codex turn rough skill ideas into maintainable skill packages: first by clarifying what the skill should do, then by deciding which guidance belongs in `SKILL.md`, which details belong in `references/`, which deterministic operations deserve scripts, and which files are only publishing material.

`README.md` is for GitHub and human readers. Codex uses `SKILL.md` as the runtime entry point.

## Highlights

- Design new skills from ambiguous requirements with an optional skill brief workflow.
- Create or refactor skills with valid `SKILL.md` frontmatter and concise runtime instructions.
- Write trigger descriptions that make skills discoverable without making them overly broad.
- Decide when to add `references/`, `scripts/`, `assets/`, and `agents/openai.yaml`.
- Audit skills with clear severity levels: required fixes, recommended improvements, and project conventions.
- Validate skill packages with the official validator and an optional project-level checker.
- Prepare a skill repository for GitHub or open-source publishing without confusing README content with runtime instructions.

## Workflow

For small, clear skills, Skill Developer can move directly from requirements to implementation.

For complex or ambiguous skills, it uses a design-first workflow:

1. Clarify the skill purpose, non-goals, trigger boundaries, and example user requests.
2. Draft a skill brief outside the final skill package, usually at `.skill-work/<skill-name>/skill-brief.md`.
3. Confirm the brief with the user before creating or heavily refactoring the skill.
4. Convert stable runtime guidance into `SKILL.md` and `references/`.
5. Add scripts or assets only when they reduce repeated work or improve reliability.
6. Run validation and, for complex skills, forward-test realistic user requests.

Temporary briefs, discussion notes, and implementation plans should not be copied into the final skill package unless they become stable runtime guidance.

## Repository Structure

```text
skill-developer/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- check-skill.md
|   |-- common-mistakes.md
|   |-- concepts.md
|   |-- config-template.md
|   |-- create-skill.md
|   |-- design-workflow.md
|   |-- full-example.md
|   |-- open-source-readme.md
|   |-- script-template.md
|   `-- skill-md-template.md
`-- scripts/
    `-- common/
        `-- check_skill_structure.py
```

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
Use $skill-developer to design a new skill for managing recurring project checklists.
```

```text
Use $skill-developer to create a new skill for PDF redaction.
```

```text
Use $skill-developer to audit this skill for Codex compatibility.
```

```text
Use $skill-developer to improve this SKILL.md and prepare a GitHub README.
```

## Reference Files

- `references/design-workflow.md`: Design ambiguous or complex skills with a confirmable brief before implementation.
- `references/create-skill.md`: Create or restructure skills using the official skill creation flow.
- `references/skill-md-template.md`: Write or repair `SKILL.md` frontmatter, trigger descriptions, workflows, and resource navigation.
- `references/check-skill.md`: Audit a skill and report required fixes, recommended improvements, and project conventions.
- `references/common-mistakes.md`: Diagnose common skill design problems.
- `references/concepts.md`: Explain core Codex skill concepts and progressive disclosure.
- `references/script-template.md`: Add deterministic CLI scripts with testable behavior.
- `references/config-template.md`: Design configuration patterns for skills that need tokens, paths, or service settings.
- `references/full-example.md`: Inspect a complete lightweight example skill.
- `references/open-source-readme.md`: Prepare README content for GitHub or open-source release.

## Validation

Run the official baseline validator:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

Run the optional project-level checker:

```bash
python3 scripts/common/check_skill_structure.py .
```

Expected project-level result:

```json
{
  "ok": true,
  "errors": [],
  "warnings": []
}
```

## Design Principles

- Keep `SKILL.md` small, action-oriented, and focused on runtime behavior.
- Put long explanations, templates, checklists, and domain details in `references/`.
- Add scripts only when deterministic execution or repeated automation is useful.
- Treat `assets/` as output resources, not reading material.
- Do not create empty directories as placeholders.
- Separate official Codex requirements from team-specific conventions.
- Keep design drafts and publishing documentation separate from runtime skill resources.

## Contributing

When changing this skill:

1. Keep trigger conditions in the frontmatter `description`.
2. Keep resource navigation in `SKILL.md` explicit: say when each reference or script should be used.
3. Add or update references instead of making `SKILL.md` overly long.
4. Run both validation commands before opening a pull request.
5. Do not include real tokens, private URLs, internal account names, personal absolute paths, or unlicensed assets.

## License

This repository does not include a `LICENSE` file yet. Choose and add an open-source license before publishing publicly on GitHub.
