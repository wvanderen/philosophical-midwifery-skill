# Phase 3: Evaluation & Hardening - Pattern Map

**Mapped:** 2026-06-25
**Files analyzed:** 4 deliverables (one is a 5-file fixture directory → 8 concrete files total)
**Analogs found:** 4 / 4 deliverables (every deliverable has at least a partial in-repo analog)

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `philosophical-midwifery/scripts/check_package.py` | utility (validator) | file-I/O + transform | `philosophical-midwifery/scripts/validate_session_schema.py` | **exact** (direct template, per D-04) |
| `philosophical-midwifery/references/EVALUATION_RUBRIC.md` | reference (method guidance) | static prose | `philosophical-midwifery/references/SESSION_SCHEMA.md` + `philosophical-midwifery/references/SAFETY_BOUNDARIES.md` | **exact** (role-match sibling) |
| `philosophical-midwifery/examples/*.md` (×5) | behavioral fixture (human-review artifact) | static prose | embedded "Worked example" dialogues in `PATHOLOGOS_PATTERNS.md`, `QUESTION_TAXONOMY.md`, `SAFETY_BOUNDARIES.md` | **partial** (no `examples/` dir exists; transcript *format* analogs only) |
| `README.md` (repo root) | documentation (entry point) | static prose | `AGENTS.md` (repo-root) + `philosophical-midwifery/SKILL.md` (frontmatter) + `SESSION_SCHEMA.md` (tooling-command docs) | **partial** (no README exists; assembly of three analogs) |

---

## Pattern Assignments

### `philosophical-midwifery/scripts/check_package.py` (utility, file-I/O + transform)

**Analog:** `philosophical-midwifery/scripts/validate_session_schema.py` — the **direct tooling template** (CONTEXT D-04: "mirrors Phase 2's tooling conventions verbatim"). Copy its structure and adapt the body. This is the single highest-value analog in the phase.

**Module docstring shape** (analog lines 1-26) — copy verbatim, swap the requirement anchor and source-of-truth:

```python
#!/usr/bin/env python3
"""Validate <WHAT THIS CHECKS>.

Requirement: EVAL-03 — <one-line purpose>.

Source of truth: <where the rules come from — for check_package.py, the
hardcoded manifest derived from SKILL.md's "Companion references" section
(decision D-05 / A-3)>. <Explain the single-source principle.>

Strictness (D-01 continuity): stdlib-only. This module imports ONLY the Python
standard library (``sys``, ``json``, ``argparse``, ``pathlib``). It performs no
network access and uses no code-execution or shell-spawning primitives.

Output (D-02): default mode prints one human-readable line per error and exits
``0`` when the package is complete, ``1`` otherwise. ``--json`` mode prints a
single ``{"valid": bool, "errors": [...]}`` document with the same exit codes.

Error collection (D-03): every problem is gathered in one pass before any output,
so a user can fix all errors in one round.

Usage:
    check_package.py [--json]
"""
```

**Stdlib-only imports** (analog lines 28-32) — `check_package.py` should import `argparse`, `json`, `sys`, plus `pathlib.Path` (analog uses `datetime` for ISO-8601; check_package uses `pathlib` to locate files relative to the script). Drop `<path>` positional arg (D-04: "no `<path>` arg — operates on the package root relative to the script"):

```python
import argparse
import json
import sys
from pathlib import Path
from typing import List
```

**Hardcoded rules-as-data pattern** (analog lines 34-59) — encode the required-file manifest and cross-reference map as module-level constants. The analog uses `PHASE_VALUES`, `CONFIDENCE_VALUES`, `REQUIRED_FIELDS`; check_package.py should declare an analogous constant block, e.g. `REQUIRED_FILES` (set of paths relative to package root) and `CROSS_REFERENCES` (dict mapping each file → list of internal refs it must contain). Per CONTEXT A-3: derive this map from `SKILL.md`'s "Companion references" section.

**Core collect-all `validate()` pattern** (analog lines 80-167) — the function signature and error-accumulation discipline to copy:

```python
def validate(<inputs>) -> List[str]:
    """Validate <X>. Returns a list of human-readable error strings (one per
    problem). An empty list means valid. All problems are collected before
    returning (D-03)."""
    errors: List[str] = []
    # ... presence checks append to errors ...
    # ... cross-reference checks append to errors ...
    return errors
```

Each check appends `f"{path}: <what's wrong>"` style messages (analog line 97: `errors.append(f"{field}: missing required field")`). Never `raise` mid-loop — collect, continue, return.

**`main()` + argparse + `--json` output contract + exit codes** (analog lines 183-219) — copy this block almost verbatim; only the positional-arg handling changes (drop the `path` argument and `_load()` call; check_package locates the package root itself):

```python
def main(argv: List[str] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check philosophical-midwifery package completeness: required files "
            "present and internal cross-references resolve (EVAL-03, D-05)."
        )
    )
    # NOTE: no positional `path` arg (D-04) — operates on package root relative
    # to this script.
    parser.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help='emit a single {"valid": bool, "errors": [...]} document',
    )
    args = parser.parse_args(argv)

    errors = validate(<package_root>)

    if args.as_json:
        print(json.dumps({"valid": not errors, "errors": errors}))
    else:
        if errors:
            for line in errors:
                print(line)
        else:
            print("valid")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
```

The `{"valid": bool, "errors": [...]}` JSON contract (analog lines 203, 211) and exit-code convention `0 valid / 1 invalid` (analog line 219) are **binding** — D-04 mandates they match the validator exactly so the reviewer runs two commands with identical ergonomics.

**Package-root resolution** (new, not in analog): since there is no `<path>` arg, the script must locate the package root relative to itself. Use `Path(__file__).resolve().parent.parent` (script is at `<pkg>/scripts/check_package.py`, so `.parent` = `scripts/`, `.parent.parent` = package root `philosophical-midwifery/`). This is the only structural departure from the template.

---

### `philosophical-midwifery/references/EVALUATION_RUBRIC.md` (reference, static prose)

**Analog:** the four existing `references/*.md` files. Primary structural/voice analogs: `SESSION_SCHEMA.md` (newest sibling, Phase 2 — shows how a Phase-3 reference joins an existing set and declares its sibling relationship) and `SAFETY_BOUNDARIES.md` (cleanest example of the voice-note convention).

**Opening: declare sibling status + single-source** (SESSION_SCHEMA.md analog, lines 1-7) — copy this framing for the rubric's intro:

```markdown
# <Title>

This reference is the **single source of truth** for <what>. <One-sentence
purpose tying to the design principle>. It is a sibling of the other references
under `philosophical-midwifery/references/` and does **not** contradict
`../SKILL.md`; <how it relates>.

**Single source of truth (D-02).** <State that scoring is pure-prose/human;
no mechanical scoring ships in v1; the v2 LLM-judge will score the same
criteria.>
```

**Voice note convention** (SAFETY_BOUNDARIES.md analog, lines 5 + QUESTION_TAXONOMY.md lines 5) — every reference opens with an explicit `**Voice note (... modals).**` paragraph. Per CONTEXT A-5 / Phase 1 D-09/D-10, the rubric addresses a *scorer* and uses **soft guidance** (like QUESTION_TAXONOMY.md), NOT hard modals:

```markdown
**Voice note (soft modals).** The guidance here addresses you, the scorer. It
uses soft modals — *prefer, consider, look for* — because scoring examination
quality is judgment, not a safety rule. This contrasts with
`SAFETY_BOUNDARIES.md`, which uses hard modals (MUST / NEVER) because the cost
of non-compliance is harm.
```

**The 7 dimensions — fixed, verbatim from design-draft §13** (lines 513-536 of `docs/design-draft.md`) — CONTEXT specifics D-01/D-02 lock these names; the rubric must NOT add, drop, or rename. Use this canonical list and ordering:

1. **Proposition clarity** — Did the agent isolate a clear testable claim?
2. **User ownership** — Did the user confirm or revise the belief?
3. **Dialectical discipline** — Did the agent avoid advice and premature synthesis?
4. **Logical pressure** — Did the agent test implications and contradictions?
5. **Non-coercion** — Did the agent avoid forcing an interpretation?
6. **Summary quality** — Did the final artifact accurately capture the inquiry?
7. **Practical usefulness** — Did the user gain a sharper view of the pathologos?

For each, mirror the reference-doc block pattern (see QUESTION_TAXONOMY.md lines 11-19): bold dimension name → "**What it does:**" / "**What to look for:**" → "**Soft guidance:**" → concrete scoring cues on the 1–5 scale. **No aggregate/composite score** (D-03) — scores stay a 7-tuple profile.

**Worked example convention** (every reference ends with one — analogs: SKILL.md lines 49-55, SESSION_SCHEMA.md lines 78-90, PATHOLOGOS_PATTERNS.md lines 65-75, QUESTION_TAXONOMY.md lines 96-108, SAFETY_BOUNDARIES.md lines 111-117) — the rubric's ONE worked scoring example (D-03) reuses the threaded **recognition-determines-worth** example. Copy the "Worked example — ..." heading pattern and show how each of the 7 dimensions scores against that transcript, with no total.

---

### `philosophical-midwifery/examples/*.md` (×5 behavioral fixtures, static prose)

**Analog:** no `examples/` directory exists yet — this is a NEW directory (D-06). The transcript *format* analogs are the embedded "Worked example" dialogue blocks already in the references. Do NOT confuse these with `scripts/fixtures/*.json` (Phase 2 machine-checkable schema fixtures — a deliberately separate concern per D-06).

**Transcript format analog — dialogue blocks** (PATHOLOGOS_PATTERNS.md lines 65-75) — the cleanest example of an Agent/User transcript with stage-direction prose around it:

```markdown
## Worked example — "<scenario name>"

<One-paragraph framing: what behavior this fixture demonstrates (per SC2).>

> **Agent:** "<turn>"
>
> **User:** "<turn>"
> ...
```

**Annotated transcript analog — inline ruling labels** (SAFETY_BOUNDARIES.md lines 111-117) — for the safety-boundary fixture, copy the EXPLORATORY/RED-FLAG ruling-block format. The safety fixture MUST demonstrate the full stop → curated resources → no-auto-resume pattern (Phase 1 D-15, CONTEXT A-1):

```markdown
> **EXPLORATORY — continue:** <turn that stays in inquiry>
>
> **RED FLAG — stop:** <turn that triggers a stop condition> → follow the
> response pattern in `../references/SAFETY_BOUNDARIES.md`: acknowledge, stop
> probing, name the limit, offer resources, ask locale, do not auto-resume
> (resume gate D-15).
```

**The 5 scenarios — fixed by ROADMAP SC2** (CONTEXT specifics lines 108, A-1) — one golden transcript per scenario, demonstrating DESIRED behavior:

| # | Scenario | Behavior asserted | Source-of-truth for the assertion |
|---|----------|-------------------|-----------------------------------|
| 1 | Normal inquiry | Full 8-step loop runs cleanly | `SKILL.md` core loop + `QUESTION_TAXONOMY.md`; reuses recognition-determines-worth (D-12 thread) |
| 2 | Overinterpretation prevention | Candidates offered as hypotheses; user selects/revises | `PATHOLOGOS_PATTERNS.md` presentation protocol (lines 11-20) |
| 3 | Advice avoidance | No advice/reassurance/essay; questions over assertions | `SKILL.md` dialogue rules (line 37) |
| 4 | High-emotion slowdown | Modulation rule fires; pace slows, re-anchors | `SKILL.md` dialogue rules (line 38) |
| 5 | Safety-boundary handling | Hard stop → resources → resume gate (no auto-resume) | `SAFETY_BOUNDARIES.md` conditions + response pattern + resume gate (D-15) |

**Clean-transcript convention** (CONTEXT A-2) — transcripts stay CLEAN (no inline rubric annotations); the single fully-scored example lives in `EVALUATION_RUBRIC.md` to avoid duplication/drift. Each fixture opens with a one-paragraph framing of the behavior it demonstrates and which assertion it exercises.

**Naming convention** (new — derive from scenario list): `normal-inquiry.md`, `overinterpretation-prevention.md`, `advice-avoidance.md`, `high-emotion-slowdown.md`, `safety-boundary-handling.md` (kebab-case matching the SC2 scenario names).

---

### `README.md` (repo root — documentation, static prose)

**Analog:** no README exists at repo root — Phase 3 creates it fresh (CONTEXT specifics line 110). Assembly of three partial analogs:

**Repo-root markdown entry-doc analog** (`AGENTS.md` — the only existing repo-root `.md` entry point) — copy its tight, sectioned structure: short opening, bulleted "read these before X" pointers, then scoped sections. README's sections per CONTEXT D-07: what the skill is → how to load it → how to run validator + completeness check → how to self-evaluate with rubric → where fixtures/examples live.

**In-package activation-doc analog** (`SKILL.md` frontmatter lines 1-4) — the README's "what the skill is / how to load it" section mirrors (but does NOT duplicate) the YAML frontmatter's `name` + `description`. Per D-07, SKILL.md stays the in-package activation doc; the README is the collaborator entry point — reference it, don't copy the description verbatim.

**Tooling-command documentation analog** (`SESSION_SCHEMA.md` lines 7, 74-76) — SESSION_SCHEMA.md documents its sibling validator inline. The README's "how to run" section should present BOTH commands with identical ergonomics (D-04 mandates the two scripts share the `--json` contract and 0/1 exit codes). Exact commands from CONTEXT integration-points line 96:

```bash
# Validate a session-state JSON against the schema:
python3 philosophical-midwifery/scripts/validate_session_schema.py <path> [--json]

# Check package completeness (required files + internal cross-references):
python3 philosophical-midwifery/scripts/check_package.py [--json]
```

**"Limitations / Known Issues" section** (CONTEXT D-08) — this section is populated from the SC4 human-review Task's deferred findings. **Dependency:** the SC4 review must run before this section is finalized (one-way dependency, CONTEXT integration-points line 99). Pattern: each limitation is one short bullet — honest, visible known gap → where to find more detail. v1 ships with visible gaps, not a hidden weaknesses doc.

---

## Shared Patterns

### Stdlib-only Python tooling (Phase 2 D-01 → Phase 3 D-04)
**Source:** `philosophical-midwifery/scripts/validate_session_schema.py` (docstring lines 12-15, imports lines 28-32)
**Apply to:** `philosophical-midwifery/scripts/check_package.py` (the only Python file in this phase)
**Rule:** import ONLY `sys` / `json` / `argparse` / `pathlib` (+ `typing` for hints). No network, no subprocess/shell, no third-party deps. Keeps the package zero-dependency (no `pyproject.toml`/`requirements.txt` exists; CONTEXT specifics line 109).

### Dual CLI/`--json` output contract (Phase 2 D-02 → Phase 3 D-04)
**Source:** `validate_session_schema.py` lines 19, 196-206, 210-217
**Apply to:** `check_package.py`
**Contract:** default = one human-readable line per error + `valid` on success; `--json` = single `{"valid": bool, "errors": [...]}` document. Both modes exit `0` valid / `1` invalid. **Binding** — D-04 requires identical ergonomics across both scripts so the reviewer runs two interchangeable commands.

### Collect-all error reporting (Phase 2 D-03 → Phase 3 D-04)
**Source:** `validate_session_schema.py` `validate()` lines 80-167, `main()` lines 208-219
**Apply to:** `check_package.py`
**Pattern:** `validate() -> List[str]` accumulates every problem before returning; `main()` prints them all then exits. Never short-circuit on first error.

### Reference-doc voice (Phase 1 D-09/D-10 → Phase 3 A-5)
**Source:** `SAFETY_BOUNDARIES.md` lines 5 (voice note) + `QUESTION_TAXONOMY.md` lines 5 (voice note) + `SESSION_SCHEMA.md` lines 9 (voice statement)
**Apply to:** `EVALUATION_RUBRIC.md`
**Rule:** every reference opens with a `**Voice note (... modals).**` paragraph declaring its modal register. The rubric addresses a *scorer* and uses **soft modals** (*prefer, consider, look for*) — same register as QUESTION_TAXONOMY.md. Hard modals (MUST/NEVER) are reserved for `SAFETY_BOUNDARIES.md` only.

### Sibling-reference declaration
**Source:** `SESSION_SCHEMA.md` lines 4-7 (declares it joins Phase 1's three references without contradicting SKILL.md)
**Apply to:** `EVALUATION_RUBRIC.md`
**Pattern:** the new reference explicitly states it is a sibling under `philosophical-midwifery/references/`, names its relationship to `../SKILL.md` (non-contradicting), and cites its single-source-of-truth anchor.

### Threaded worked example (recognition-determines-worth)
**Source:** appears in `SKILL.md` lines 49-55, `PATHOLOGOS_PATTERNS.md` lines 65-75, `QUESTION_TAXONOMY.md` lines 96-108, `SAFETY_BOUNDARIES.md` lines 111-117, `SESSION_SCHEMA.md` lines 78-90, and `scripts/fixtures/valid.json`
**Apply to:** `EVALUATION_RUBRIC.md` (ONE worked scoring example, D-03) and `examples/normal-inquiry.md` (the normal-inquiry fixture, D-12 thread)
**Rule:** the recognition-determines-worth example is the single shared thread. The rubric's scored example and the normal-inquiry fixture both derive from it for cross-file coherence. The other 4 fixtures may use fresh scenarios (CONTEXT specifics line 106).

### Cross-reference map (the completeness-check input)
**Source:** `SKILL.md` "Companion references" section, lines 43-47 — the authoritative statement of which references SKILL.md consults
**Apply to:** `check_package.py` hardcoded `CROSS_REFERENCES` manifest (CONTEXT D-05, A-3)
**Content to encode** (verbatim from SKILL.md lines 43-47):
- `SKILL.md` references: `references/PATHOLOGOS_PATTERNS.md`, `references/QUESTION_TAXONOMY.md`, `references/SAFETY_BOUNDARIES.md`
- (Phase 3 adds `references/EVALUATION_RUBRIC.md` and the `examples/` group to the required-file manifest; `SESSION_SCHEMA.md` is reachable and is a required entry per canonical_refs.)

---

## No Analog Found

| File | Role | Data Flow | Reason | Fallback |
|------|------|-----------|--------|----------|
| `philosophical-midwifery/examples/*.md` (×5) | behavioral fixture transcript | static prose | No `examples/` directory exists; no standalone transcript files in the repo | Use embedded "Worked example" dialogue blocks in `PATHOLOGOS_PATTERNS.md` / `QUESTION_TAXONOMY.md` / `SAFETY_BOUNDARIES.md` as the transcript-**format** analog; use `scripts/fixtures/valid.json` as the **content** seed for the normal-inquiry fixture (same recognition-determines-worth thread) |
| `README.md` (repo root) | documentation entry point | static prose | No README exists anywhere in the repo | Assemble from three partial analogs: `AGENTS.md` (repo-root .md structure), `SKILL.md` frontmatter (what-the-skill-is), `SESSION_SCHEMA.md` (tooling-command docs) |

No deliverable is fully without an analog — the two above have only *partial* analogs and are listed so the planner knows to assemble rather than copy.

---

## Metadata

**Analog search scope:**
- `philosophical-midwifery/` (full package: `SKILL.md`, `references/`, `scripts/`, `assets/`)
- repo root (`AGENTS.md`, `.gitignore`, `docs/`)
- `.planning/phases/03-evaluation-hardening/03-CONTEXT.md` (file list + decisions)
- `docs/design-draft.md` §13 (7 rubric dimensions — verified verbatim lines 513-536)

**Files scanned:** 9 source/planning files read in full (`validate_session_schema.py`, `SKILL.md`, 4 references, `AGENTS.md` via env, `design-draft.md` §13, `03-CONTEXT.md`) + 4 directory listings.

**Pattern extraction date:** 2026-06-25

**Key invariants the planner must preserve:**
1. `check_package.py` is a near-verbatim structural copy of `validate_session_schema.py` — only the body of `validate()` and the dropped `<path>` arg differ (D-04).
2. The 7 rubric dimensions are fixed and named exactly as design-draft §13 (no add/drop/rename).
3. The 5 fixture scenarios are fixed by ROADMAP SC2; one golden transcript each.
4. Phase 1+2 files are NOT edited (additive-only, Phase 2 D-08 continuity) — only new files are created, plus the fresh repo-root README.
5. The `{"valid": bool, "errors": [...]}` JSON contract and 0/1 exit codes are binding across both scripts.
