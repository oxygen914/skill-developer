<p align="center">
  <img src="assets/readme/skill-developer/wordmark.webp" alt="Skill Developer animated wordmark" width="720" />
</p>

<p align="center">
  <strong>English</strong> · <a href="README-CN.md">简体中文</a>
</p>

# Skill Developer

Skill Developer is an Agent Skill for designing, creating, refactoring, auditing, validating, and preparing other skills for publication across Agent Skills-compatible clients, Codex, and Claude Code.

It turns an early idea or an existing skill directory into a package with clearer trigger boundaries, deliberate resource organization, platform-aware metadata, and reproducible validation. The runtime source of truth is [SKILL.md](SKILL.md); this README is the human-facing installation and usage guide.

## Why use it?

Creating a useful skill involves more than writing instructions in a Markdown file. A skill also needs to answer:

- Which user requests should trigger it, and which should not?
- What belongs in `SKILL.md`, and what should move into `references/`?
- Does a repeated or error-prone operation justify a deterministic script?
- Which files are portable Agent Skills resources, and which are specific to Codex or Claude Code?
- How should failures, recommendations, and project conventions be distinguished during an audit?
- Which checks demonstrate that the package can actually be discovered and used?

Skill Developer makes these decisions explicit before adding structure. Small, well-defined changes can be implemented directly; complex or boundary-sensitive requests can first be captured in a reviewable skill brief.

## Capabilities

- **Design** — define goals, non-goals, target clients, trigger examples, output contracts, risks, and acceptance criteria.
- **Create and refactor** — build a minimal skill package and add `references/`, `scripts/`, `assets/`, or `agents/` only when they have a concrete purpose.
- **Improve triggering** — write descriptions that communicate both capability and when the skill should be invoked.
- **Separate resources** — keep the runtime entry point concise while routing detailed rules, templates, examples, and deterministic tooling to the appropriate files.
- **Handle platform differences** — separate portable Agent Skills conventions from Codex metadata and Claude Code extensions.
- **Audit existing skills** — report findings as required fixes, recommended improvements, or project-specific conventions.
- **Validate** — run Codex's base validator and the bundled cross-platform structural checker.
- **Prepare for publication** — review repository structure, README content, validation instructions, sensitive data, and license status.

## Supported targets

| Target | Core support | Platform-specific behavior |
| --- | --- | --- |
| Agent Skills | `SKILL.md` with `name` and `description`; optional `references/`, `scripts/`, and `assets/` | Uses the smallest portable structure by default |
| Codex | Installation under `${CODEX_HOME:-$HOME/.codex}/skills` | Supports `agents/openai.yaml` and Codex `quick_validate.py` |
| Claude Code | Personal or project installation under a `.claude/skills` directory | Documents slash-command discovery and clearly labels Claude-only frontmatter extensions |

Platform support does not mean every field is shared. For example, `agents/openai.yaml` controls Codex/OpenAI presentation metadata and is not required by Claude Code. See [Platform compatibility](references/platforms.md) for the detailed boundary.

## How it works

### 1. Understand the request

The skill identifies the target clients, intended users, representative requests, expected output, and important non-goals. It reuses information already available in the conversation or repository instead of asking for it again.

### 2. Decide whether a design brief is needed

A small change—such as fixing a description, adding resource routing, or running validation—can proceed immediately.

A complex, ambiguous, or safety-sensitive skill can first produce:

```text
.skill-work/<skill-name>/skill-brief.md
```

The brief records trigger and non-trigger examples, resource plans, dependencies, risks, and acceptance criteria. It stays outside the runtime package unless its content is later converted into stable runtime guidance.

### 3. Build the smallest useful package

The minimum valid package is:

```text
<skill-name>/
└── SKILL.md
```

Additional directories are created only when needed:

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

Empty placeholder directories are intentionally avoided.

### 4. Route knowledge and operations

- `SKILL.md` contains triggering metadata, the core workflow, safety rules, and resource routing.
- `references/` contains detailed procedures, domain rules, templates, examples, or checklists that are loaded only when relevant.
- `scripts/` contains deterministic, repeatable, or error-prone operations and should include a clear interface and representative validation.
- `assets/` contains reusable files consumed or emitted by the skill.
- `agents/openai.yaml` contains optional Codex/OpenAI UI metadata.

### 5. Validate against the target clients

The skill runs applicable validators, checks direct resource references, inspects script syntax and metadata, and reports remaining unverified behavior instead of treating static inspection as runtime proof.

## Installation

Clone the repository:

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

Personal installation:

```bash
mkdir -p ~/.claude/skills
cp -R . ~/.claude/skills/skill-developer
```

Project installation:

```bash
mkdir -p /path/to/project/.claude/skills
cp -R . /path/to/project/.claude/skills/skill-developer
```

Refresh or restart the target client after installation so it can rediscover the skill metadata.

> These commands copy the repository's publication files as well as its runtime files. If you maintain a packaged distribution, keep `SKILL.md` and every resource it references together.

## Quick start

### Design a cross-platform skill

```text
Use $skill-developer to design a cross-platform skill for recurring release
checklists. Define trigger and non-trigger examples before implementation.
```

### Create a Codex skill

```text
Use $skill-developer to create a Codex skill that audits API documentation.
Keep SKILL.md concise, add references only when needed, and validate the result.
```

### Audit an existing skill

```text
Use $skill-developer to audit this skill for Agent Skills, Codex, and Claude
Code compatibility. Separate required fixes from recommendations.
```

### Prepare a repository for GitHub

```text
Use $skill-developer to review this skill for public release. Check its README,
resource paths, validation commands, sensitive data, and license status.
```

In Claude Code, the installed skill can also be invoked explicitly with:

```text
/skill-developer
```

## Typical outputs

The exact response depends on the request:

| Request | Typical output |
| --- | --- |
| Design | A skill brief with goals, boundaries, triggers, resources, risks, and acceptance criteria |
| Create or refactor | A minimal runtime package plus the validation results |
| Audit | A conclusion followed by required fixes, recommended improvements, platform conventions, and verified checks |
| Publish preparation | A human-facing README review, repository hygiene findings, validation status, and license warning when applicable |

## Audit severity model

Skill Developer deliberately separates three kinds of findings:

| Level | Meaning | Examples |
| --- | --- | --- |
| Required fix | Prevents discovery, loading, or basic use on the target client | Missing `SKILL.md`, invalid frontmatter, missing `name` or `description`, broken direct resource reference |
| Recommended improvement | Does not necessarily break execution but weakens triggering, maintainability, or verification | Overloaded `SKILL.md`, unclear resource routing, an untested script, weak trigger wording |
| Project convention | Applies only when a client or team has explicitly adopted it | Fixed folder templates, internal configuration patterns, Claude-only frontmatter, optional Codex UI metadata |

This prevents a project preference from being presented as a universal Agent Skills requirement.

## Repository guide

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Runtime entry point, workflow, boundaries, and resource router |
| [agents/openai.yaml](agents/openai.yaml) | Codex/OpenAI display metadata |
| [references/design-workflow.md](references/design-workflow.md) | Optional skill-brief workflow for ambiguous or complex requests |
| [references/create-skill.md](references/create-skill.md) | End-to-end creation and refactoring process |
| [references/skill-md-template.md](references/skill-md-template.md) | Frontmatter, trigger description, body, and resource-routing guidance |
| [references/platforms.md](references/platforms.md) | Agent Skills, Codex, and Claude Code differences |
| [references/check-skill.md](references/check-skill.md) | Audit order, severity levels, and report format |
| [references/common-mistakes.md](references/common-mistakes.md) | Common triggering, structure, and validation failures |
| [references/script-template.md](references/script-template.md) | Guidance for deterministic scripts and their CLI contracts |
| [references/config-template.md](references/config-template.md) | Configuration patterns for paths, environment variables, and credentials |
| [references/full-example.md](references/full-example.md) | A compact complete skill example |
| [references/open-source-readme.md](references/open-source-readme.md) | Human-facing README and publication checklist |
| [scripts/common/check_skill_structure.py](scripts/common/check_skill_structure.py) | Cross-platform structural and maintainability checker |

## Validation

Run the Codex base validator from the repository root:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

Run the bundled checker for each target:

```bash
python3 scripts/common/check_skill_structure.py . --platform agent
python3 scripts/common/check_skill_structure.py . --platform codex
python3 scripts/common/check_skill_structure.py . --platform claude
```

A successful bundled check returns:

```json
{
  "ok": true,
  "platform": "agent",
  "skill_path": "/resolved/path/to/skill-developer",
  "errors": [],
  "warnings": []
}
```

The bundled checker complements platform validators; it does not replace them. For complex skills, validation should also include representative user requests that exercise triggering, reference discovery, and the main workflow.

## Design principles

- Prefer a portable Agent Skills foundation before adding client-specific behavior.
- Keep the runtime entry point concise and progressively load detailed resources.
- Add files only when they reduce repetition, improve reliability, or carry necessary knowledge.
- Use scripts for deterministic work, not as a default wrapper around model reasoning.
- Keep temporary plans and publication documents separate from runtime instructions.
- Make platform differences explicit rather than implying universal compatibility.
- Treat validation output as evidence, and label anything not tested.
- Never copy third-party implementations without reviewing license and attribution requirements.

## Boundaries

Skill Developer is not a general-purpose code generator, business-requirements analyst, or project-management system. It does not:

- force every skill into one directory template;
- treat Codex or Claude Code extensions as universal requirements;
- create empty folders merely to suggest future structure;
- promote team preferences to required fixes;
- treat a README or design brief as a runtime instruction source;
- guarantee that static validation proves every real invocation path;
- choose a license on behalf of a repository owner.

## Contributing

When proposing a change:

1. Keep `SKILL.md` focused on triggering, the core workflow, and resource routing.
2. Put detailed reusable guidance in the most relevant file under `references/`.
3. Add scripts only for deterministic or repeatedly error-prone work.
4. Update both [README.md](README.md) and [README-CN.md](README-CN.md) when user-facing behavior changes.
5. Run the Codex validator and all three bundled platform checks.
6. Include representative forward tests for changes that affect triggering or behavior.

## License

This repository currently does not include a `LICENSE` file. No open-source license is granted by the repository as it stands. Add an explicit license before distributing or presenting the project as open source.
