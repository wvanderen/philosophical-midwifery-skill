# Phase 3: Evaluation & Hardening - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-24
**Phase:** 3-Evaluation & Hardening
**Areas discussed:** Evaluation rubric artifact, Completeness check shape, README & review notes

---

## Area selection

| Option | Description | Selected |
|--------|-------------|----------|
| Behavioral fixture format | Illustrative markdown vs structured JSON cases; manual vs mechanical scoring | |
| Evaluation rubric artifact | Where the 7-dimension rubric lives; manual vs LLM-judge; worked example + aggregation | ✓ |
| Completeness check shape | Script vs shell vs extend validator; check depth; fixture location | ✓ |
| README & review notes | README placement/scope; SC4 review-notes form | ✓ |

**User's choice:** Rubric, Completeness check, README & review notes. Behavioral-fixture format left to agent discretion (resolved via the rubric mechanization decision → D-02/D-06).

---

## Evaluation rubric artifact

### Q1 — Rubric location

| Option | Description | Selected |
|--------|-------------|----------|
| references/ (Recommended) | New references/EVALUATION_RUBRIC.md; guidance prose like the 4 existing references (Phase 1 D-01) | ✓ |
| assets/ | Alongside templates; treat as a reusable scoring artifact | |
| You decide | Defer to researcher/planner | |

**User's choice:** references/EVALUATION_RUBRIC.md (D-01)

### Q2 — Scoring mechanization

| Option | Description | Selected |
|--------|-------------|----------|
| Pure prose, human-scored (Recommended) | Prose rubric + 1–5 scale; fixtures are illustrative transcripts; no mechanical scoring; LLM-judge deferred to v2 | ✓ |
| Structured + LLM-judge-ready | Per-dimension structured fields; JSON fixture cases with expected scores; primes v2 automation | |
| Hybrid | Prose rubric + separate fillable scoring template; no automated judging | |

**User's choice:** Pure prose, human-scored (D-02). This also resolved the deferred behavioral-fixture format question → EVAL-02 fixtures are illustrative markdown transcripts.

### Q3 — Worked example + aggregation

| Option | Description | Selected |
|--------|-------------|----------|
| Worked example + no aggregate (Recommended) | One recognition-determines-worth worked example; 7-tuple profile, no composite score | ✓ |
| Worked example + simple average | Same example + unweighted x/5 average alongside profile | |
| No worked example, no aggregate | Pure criteria + scale; fixtures serve as examples | |

**User's choice:** Worked example + no aggregate (D-03)

---

## Completeness check shape

### Q1 — Check form

| Option | Description | Selected |
|--------|-------------|----------|
| Python script, sibling to validator (Recommended) | New scripts/check_package.py; mirrors stdlib-only / --json / collect-all conventions (Phase 2 D-01/D-02/D-03) | ✓ |
| Shell script | scripts/check_package.sh; lighter but diverges from Python-tooling pattern | |
| Extend the validator | Add --check-completeness mode to validate_session_schema.py; conflates two contracts | |

**User's choice:** Python script, sibling to validator (D-04)

### Q2 — Check depth

| Option | Description | Selected |
|--------|-------------|----------|
| Presence + cross-refs (Recommended) | SC3 literal wording; required files exist AND internal references resolve; manifest hardcoded | ✓ |
| Presence only | Files exist, no reference resolution; under-delivers on SC3 | |
| Presence + cross-refs + frontmatter | Also parse SKILL.md YAML frontmatter; needs hand-rolled parsing | |

**User's choice:** Presence + cross-refs, manifest hardcoded (D-05)

### Q3 — Behavioral-fixture location

| Option | Description | Selected |
|--------|-------------|----------|
| examples/ subdir (Recommended) | New philosophical-midwifery/examples/ for 5 markdown transcripts; separated from scripts/fixtures/*.json | ✓ |
| scripts/fixtures/ mixed | Alongside JSON schema fixtures; mixes machine-checkable with human-review | |
| assets/ | Alongside templates; semantic drift (templates vs review transcripts) | |

**User's choice:** examples/ subdir (D-06)

---

## README & review notes

### Q1 — README placement & scope

| Option | Description | Selected |
|--------|-------------|----------|
| Repo-root README.md (Recommended) | Top-level entry point: what skill is, load it, run tooling, self-evaluate, fixture locations | ✓ |
| In-package philosophical-midwifery/README.md | Self-documenting package; unusual (SKILL.md is the package doc) | |
| Both | Repo-root overview + in-package usage; duplication/drift risk | |

**User's choice:** Repo-root README.md (D-07)

### Q2 — SC4 review-notes form

| Option | Description | Selected |
|--------|-------------|----------|
| Planning artifact + README Limitations (Recommended) | Blocking review Task → frozen .planning/ record; deferred findings → README "Limitations" section | ✓ |
| Planning artifact only | Review notes solely in .planning/; no surfaced known gaps | |
| Shipped docs/REVIEW_NOTES.md | Dedicated shipped weaknesses doc; can read as unfinished, may go stale | |

**User's choice:** Planning artifact + README Limitations (D-08)

---

## Agent's Discretion

- **A-1** Behavioral-fixture coverage breadth — one golden transcript per scenario (SC2 minimum); safety-boundary shows stop→resources→no-auto-resume (Phase 1 D-15).
- **A-2** Transcript annotation style — clean transcripts in examples/; the single scored example lives in EVALUATION_RUBRIC.md (D-03).
- **A-3** Completeness-check manifest + cross-reference map — derived from shipped file set + SKILL.md "Companion references" section.
- **A-4** README section order/wording + Limitations content — populated from SC4 review findings.
- **A-5** Rubric voice — Phase 1 D-09/D-10 directive second-person; soft guidance (addresses a scorer).

## Deferred Ideas

- LLM-judge harness — v2 (HAR-* scope).
- Mechanical behavioral assertions (regex/AST) — out of v1; revisit only if v2 harness needs pre-filtering.
- Per-scenario paired failure examples — unless SC4 review flags ambiguity.
- YAML frontmatter validation in completeness check — deferred (stdlib-only constraint).
- Structured behavioral-fixture format (JSON cases) — v2 concern tied to LLM-judge harness.
- Region-indexed crisis resources / additional pathologos archetypes / per-archetype counter-questions — carried from Phase 1 deferrals.
