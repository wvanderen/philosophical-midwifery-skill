# Phase 2: Structured Session Artifacts - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-24
**Phase:** 2-Structured Session Artifacts
**Areas discussed:** Validator output & strictness, Belief-graph template richness

---

## Validator output & strictness

### Q1 — Strictness

| Option | Description | Selected |
|--------|-------------|----------|
| Required-fields only | Check that all mandatory session keys exist and are non-empty. Minimal, lenient, fast to write. Catches missing-field errors only. | |
| Required + type + enum | Also validate value types (string/array/object/date) and the `phase` enum. Catches realistic errors without any external dependency. Stdlib-only Python. | ✓ |
| Full JSON Schema | Adopt a jsonschema spec and use the `jsonschema` library. Most rigorous, but adds a runtime dependency to a v1 that is otherwise pure-markdown+stdlib. | |

**User's choice:** Required + type + enum
**Notes:** Keeps the package zero-dependency (consistent with Phase 1's pure-markdown approach and D-01).

### Q2 — Output format

| Option | Description | Selected |
|--------|-------------|----------|
| CLI prose + exit code | Human-readable: one line per error, exit 0 valid / 1 invalid. Simplest. | |
| Structured JSON + exit code | Machine-readable `{"valid":..., "errors":[...]}`, exit 0/1. Better for automation, less friendly for manual checks. | |
| Both via `--json` flag | Prose by default; `--json` emits structured output. Serves both manual spot-checks and Phase 3 automated checks. | ✓ |

**User's choice:** Both via `--json` flag

### Q3 — Error collection

| Option | Description | Selected |
|--------|-------------|----------|
| Collect all errors | Gather every missing/invalid field in one pass, then report. Better iteration; matches the `--json` array. | ✓ |
| Stop at first error | Report the first problem and exit. Simpler, but slow to converge. | |

**User's choice:** Collect all errors

### Q4 — Fixtures

| Option | Description | Selected |
|--------|-------------|----------|
| scripts/fixtures/, recognition-worth | Co-locate at `philosophical-midwifery/scripts/fixtures/{valid,invalid}.json`; both from the shared recognition-worth example (D-12); invalid seeds a missing-field + a bad phase value. | ✓ |
| Separate examples/ dir | `philosophical-midwifery/examples/` at package root for visibility. Splits script from test data. | |
| You decide | Planner picks location; only mandate content (1 valid + 1 invalid, invalid showing ≥2 error classes). | |

**User's choice:** scripts/fixtures/, recognition-worth

---

## Belief-graph template richness

### Q1 — Graph shape / richness

| Option | Description | Selected |
|--------|-------------|----------|
| Bare skeleton | Empty nodes/edges + field defs + node types; no instance data. Clearest "optional for v1" signal. | |
| Skeleton + 1 worked example | Skeleton schema + ONE recognition-worth example (belief → proposition → contradiction → revision). Illustrates the model; stays optional. | ✓ |
| v2-anticipating schema | Pre-build for GRPH-01..03 (cross-session IDs, recurrence counters, provenance). Most future-proof; risks over-building a v1 the success criterion calls "optional". | |

**User's choice:** Skeleton + 1 worked example

### Q2 — Data model

| Option | Description | Selected |
|--------|-------------|----------|
| Property graph (nodes + typed edges) | Nodes `{id,type,text,props}`, edges `{source,target,type}` (normalizes_to, contradicts, revises). Standard; maps to §8 stores; supports GRPH-02. | ✓ |
| Nested object tree | Nested arrays belief→propositions[]→contradictions[]. Simpler JSON, poor at cross-links. | |
| You decide | Researcher picks; mandate JSON + recognition-worth example + optional. | |

**User's choice:** Property graph (nodes + typed edges)

### Q3 — Pathologos tagging

| Option | Description | Selected |
|--------|-------------|----------|
| Yes — tag belief nodes | Optional `pathologos_pattern` field referencing Phase 1 archetypes (conditional_worth, etc.). Bridges catalog → graph → GRPH-02 at low cost. | ✓ |
| No — keep nodes generic | Avoid coupling to Phase 1 catalog; pathologos tagging waits for v2. | |
| You decide | Researcher decides coupling during Phase 2 research. | |

**User's choice:** Yes — tag belief nodes

### Q4 — Optionality signaling

| Option | Description | Selected |
|--------|-------------|----------|
| Header note + leave SKILL.md alone | JSON opens with `_v1_optional: true` + `_note`; Phase 1 SKILL.md session loop untouched. Phase 1 artifact unchanged; Phase 2 purely additive. | ✓ |
| Header note + SKILL.md one-liner | JSON marker + a one-line addition to SKILL.md noting the graph is optional. Edits the Phase 1 shipped file. | |
| You decide | Planner decides; only mandate the file clearly mark itself non-required for v1. | |

**User's choice:** Header note + leave SKILL.md alone

---

## the agent's Discretion

Gray areas scoped to Phase 2 but not selected for discussion. Tradeoffs captured in CONTEXT.md (A-1..A-4) so researcher/planner can resolve without re-asking:

- **A-1 Canonical `phase` enum** (5 values from §9 vs 6 procedural phases from §7). Recommendation: adopt §9's 5-value enum; treat contradiction/revision + summary as sub-activities of `synthesis`.
- **A-2 Schema source of truth** (markdown-only vs markdown + JSON Schema sidecar). Recommendation: SESSION_SCHEMA.md as single source; encode rules in the validator.
- **A-3 Summary template ↔ `session_summary` field relationship.** Recommendation: template is the render target; rendered markdown string populates the field; validator treats it as a non-empty string.
- **A-4 Validator CLI ergonomics** (argv shape, date format, belief id convention). Recommendation: `<path> [--json]`, ISO-8601 dates, `belief_N` ids.

## Deferred Ideas

- Belief-graph cross-session recurrence machinery (counters, first_seen_session, provenance) — GRPH-01..03 (v2).
- Session-state persistence across turns — HAR-02 (v2).
- JSON Schema sidecar file — only revisit if markdown-single-source proves untenable.
- Per-archetype counter-questions — already deferred in Phase 1.
- Behavioral/dialogue fixtures beyond schema fixtures — EVAL-02 (Phase 3).
