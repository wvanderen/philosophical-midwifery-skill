# Philosophical Midwifery

An Agent Skill for disciplined Socratic inquiry: help an agent move a user from a felt disturbance to a user-confirmed proposition, then examine that proposition for coherence — without drifting into therapy, advice, reassurance, or essay-writing. The atomic unit of the work is **the examined proposition**, not the chat message. This repository ships the v1 skill package plus the evaluation and verification layer that lets a reviewer score sessions, exercise the skill's behavior across five scenarios, and mechanically confirm the package is complete.

## What this is

`philosophical-midwifery` is an Agent Skill whose core value is reliably isolating and examining a user-confirmed proposition. The in-package activation doc — `philosophical-midwifery/SKILL.md` — carries the authoritative `name` and `description` frontmatter that drives skill activation and states when the skill should and should not be used; see that file for the precise trigger wording. The surrounding references, assets, scripts, and examples make the skill's behavior inspectable and its outputs consistent.

## Load the skill

`philosophical-midwifery/SKILL.md` is the in-package activation doc. Its YAML frontmatter (`name: philosophical-midwifery` plus the `description` field) is what an agent runtime reads to decide when to activate the skill. To use it, point your agent at the `philosophical-midwifery/` directory so the runtime can discover `SKILL.md`; the skill's standing instructions (core loop, dialogue rules, and "when NOT to use" routing) then persist across the session. Do not create a separate in-package README — `SKILL.md` is the activation entry point.

## Run the checks

Two stdlib-only Python scripts verify the package. They share identical ergonomics: a default prose mode and a `--json` mode that emits a single `{"valid": bool, "errors": [...]}` document, with exit code `0` when valid and `1` otherwise. Run them from the repository root.

```bash
# Validate a session-state JSON against the canonical schema:
python3 philosophical-midwifery/scripts/validate_session_schema.py <path-to-session.json> [--json]

# Check package completeness (required files present + internal cross-references resolve):
python3 philosophical-midwifery/scripts/check_package.py [--json]
```

`validate_session_schema.py` checks a session JSON's required fields, types, the 5-value `phase` enum, and ISO-8601 date format against `references/SESSION_SCHEMA.md`. `check_package.py` checks that every required package file is present and that the internal cross-references resolve (e.g., `SKILL.md` names each companion reference it consults). Neither script has third-party dependencies — only the Python standard library is used.

## Self-evaluate a session

To score a session by hand, consult `philosophical-midwifery/references/EVALUATION_RUBRIC.md`. It scores a session on seven dimensions, verbatim from design-draft §13: **proposition clarity, user ownership, dialectical discipline, logical pressure, non-coercion, summary quality, and practical usefulness**, each on a 1–5 scale. Scoring is pure-prose and human-scored — there is no mechanical or automated judge in v1 — and there is deliberately **no aggregate score**: the seven scores are recorded as a profile, so a critical single-axis failure cannot be averaged away. The rubric includes one fully-worked scoring example (the recognition-determines-worth thread) showing how each dimension scores.

## Behavioral fixtures

`philosophical-midwifery/examples/` holds five golden behavioral/dialogue transcripts that exercise the skill across its target scenarios: **normal inquiry** (a clean full-loop run), **overinterpretation prevention** (candidates as hypotheses; user selects/revises), **advice avoidance** (no advice/reassurance/essay; one question at a time), **high-emotion slowdown** (the modulation rule fires; pace slows; inquiry continues), and **safety-boundary handling** (the hard stop → curated resources → no-auto-resume pattern). These are human-review transcripts, distinct from the machine-checkable schema fixtures under `scripts/fixtures/`.

## Package layout

```
philosophical-midwifery/
├── SKILL.md                      # activation doc + core loop + dialogue rules
├── references/                   # method + safety guidance the skill consults
│   ├── PATHOLOGOS_PATTERNS.md    # candidate-belief archetypes + presentation protocol
│   ├── QUESTION_TAXONOMY.md      # the eight Socratic examination operations
│   ├── SAFETY_BOUNDARIES.md      # the five hard stop conditions + response pattern + resume gate
│   ├── SESSION_SCHEMA.md         # canonical session-state JSON shape (single source of truth)
│   └── EVALUATION_RUBRIC.md      # the seven scoring dimensions + worked example
├── assets/                       # render targets / seeds
│   ├── session_summary_template.md   # final inquiry artifact template
│   └── belief_graph_template.json    # future-compatible belief-graph seed (optional in v1)
├── scripts/                      # stdlib-only checks
│   ├── validate_session_schema.py    # session-JSON schema validator
│   ├── check_package.py              # package-completeness check
│   └── fixtures/                     # machine-checkable schema fixtures (valid.json, invalid.json)
└── examples/                     # human-review behavioral transcripts (the five SC2 scenarios)
```

## Limitations / Known Issues

No known issues at v1 ship time. The Phase 3 human review (`.planning/phases/03-evaluation-hardening/03-01-REVIEW.md`) approved all seven review checks with zero findings, so no deferred items were rolled into this section.

### Out of scope for v1

The following are deliberately deferred to v2 and later; v1 ships without them:

- **Local harness (HAR-01..03):** a local CLI or simple web chat harness that runs the skill, persists JSON session state across turns, and exports transcripts and generated session summaries. v1 validates the Agent Skill package itself; a standalone chat application is out of scope for the first milestone.
- **Persistent belief graph (GRPH-01..03):** persisting belief records across sessions, linking recurring propositions and pathologos patterns, and inspecting/correcting a belief map. v1 ships only a future-compatible belief-graph *seed*; recurrence machinery is deferred because it depends on a validated session schema and skill behavior.
- **LLM-judge harness for the rubric:** automated rubric scoring. The v1 rubric is written so a v2 LLM-judge can score sessions against the same seven criteria, but no judge ships in v1 (scoring is pure-prose, human-scored).
- **Mechanical behavioral assertions** (regex/AST checks for "one question at a time", advice-phrase detection) — behavioral properties resist mechanical assertion and risk false signals; revisit only if the v2 harness needs pre-filtering before LLM judging.
- **YAML frontmatter validation** in the completeness check — deferred (would need hand-rolled parsing under stdlib-only).
- **Mental health treatment, diagnosis, crisis counseling, and generic self-help advice** — permanently out of scope; the project is philosophical inquiry, not clinical care.

## Verifying the package is complete

After any change, run the completeness check to confirm the package is still whole:

```bash
python3 philosophical-midwifery/scripts/check_package.py
```

A `valid` result (exit 0) means every required file is present and every expected internal cross-reference resolves.
