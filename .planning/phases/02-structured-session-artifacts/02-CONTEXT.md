# Phase 2: Structured Session Artifacts - Context

**Gathered:** 2026-06-24
**Status:** Ready for planning

<domain>
## Phase Boundary

Deliver the structured-artifact layer that sits alongside the Phase 1 skill package — making inquiry outputs consistent, inspectable, and mechanically checkable. Four artifacts, all under `philosophical-midwifery/`:

- `references/SESSION_SCHEMA.md` (MTH-04) — defines all required session-state fields and allowed `phase` values.
- `assets/session_summary_template.md` (ART-01) — the final inquiry artifact; captures the examined proposition and inquiry trace without overclaiming certainty.
- `assets/belief_graph_template.json` (ART-02) — a future-compatible graph seed; optional for v1.
- `scripts/validate_session_schema.py` (ART-03) — validates representative session JSON and reports missing/invalid fields clearly; ships with one valid + one invalid fixture.

This phase covers MTH-04 and ART-01..03. No local harness, no persistence, no recurring-belief analysis — those are v2 (HAR-*/GRPH-*). Phase 1's four shipped files are NOT edited (see D-08); Phase 2 is purely additive.

</domain>

<decisions>
## Implementation Decisions

### Validator output & strictness
- **D-01:** Strictness = **required + type + enum**, stdlib-only Python (no `jsonschema`, no third-party deps). Checks: every required key exists and is non-empty; value types match the schema (string/array/object/date); the `phase` field validates against the canonical enum (see "the agent's Discretion" A-1 for the enum itself).
- **D-02:** Output = **both via a `--json` flag**. Default: CLI prose, one human-readable line per error, exit `0` valid / `1` invalid. With `--json`: a structured `{"valid": bool, "errors": [...]}` document for scripts, Phase 3 fixture checks, and the v2 harness.
- **D-03:** Error collection = **collect-all**. Gather every missing/invalid field in one pass before reporting. Pairs cleanly with the `--json` errors array and lets a user fix everything in one round.
- **D-04:** Fixtures live at `philosophical-midwifery/scripts/fixtures/{valid,invalid}.json`, **both derived from the shared "recognition determines worth" example** (Phase 1 D-12) for cross-file coherence. `invalid.json` seeds **at least two distinct error classes** — a missing required field AND a bad `phase` value — so one fixture exercises both the required-field and the enum checks while keeping the fixture count at the success-criterion minimum.

### Belief-graph template richness
- **D-05:** Richness = **skeleton schema + ONE worked example**, seeded from the recognition-determines-worth thread (belief → normalized proposition → contradiction → revision as linked nodes/edges). The skeleton documents the shape; the single example illustrates the model. Stays optional per success criterion #3.
- **D-06:** Data model = **property graph**. Nodes: `{id, type, text, props}`; Edges: `{source, target, type}` with typed edges such as `normalizes_to`, `contradicts`, `revises`. Maps cleanly to the later relational stores in design-draft §8 (beliefs/propositions/contradictions/revisions) and natively supports GRPH-02 cross-session linking.
- **D-07:** Belief nodes carry an optional **`pathologos_pattern`** field referencing the Phase 1 archetypes (`conditional_worth`, `control_responsibility`, `belonging_rejection`, `perfection_flawlessness` — Phase 1 D-06). Bridges the Phase 1 catalog → the graph → GRPH-02 pattern-linking at the cost of one optional field.
- **D-08:** Optionality signaling = the JSON opens with a **header marker** (e.g., `"_v1_optional": true` + a `_note` field explaining it's a future seed) AND **Phase 1's `SKILL.md` session loop is left untouched**. Graph population is not a required v1 step. Phase 1's locked artifact stays unchanged; Phase 2 is purely additive.

### the agent's Discretion
Gray areas that were scoped to Phase 2 but not selected for discussion. Tradeoffs noted so the researcher/planner can resolve them without re-asking the user.

- **A-1 — Canonical `phase` enum (5 vs 6 values).** `docs/design-draft.md` §9 lists 5 values (`intake | extraction | normalization | examination | synthesis`) while §7 describes 6 procedural phases (adding contradiction/revision and session-summary as distinct steps). **Recommendation:** adopt the 5-value enum from §9 as canonical for the `phase` field (it is the schema's own definition), and document in `SESSION_SCHEMA.md` that contradiction/revision and session-summary are sub-activities of `synthesis`, not separate phase values. This keeps the validator's enum finite and grounded in the draft's schema section.
- **A-2 — Schema source of truth (markdown-only vs markdown + JSON Schema sidecar).** Whether `references/SESSION_SCHEMA.md` is the single source (validator encodes required/type/enum rules directly in `validate_session_schema.py`) OR is accompanied by a machine-readable JSON Schema sidecar that both the markdown and the validator reference. **Recommendation:** given D-01 (stdlib-only) and Phase 1's pure-markdown convention, default to SESSION_SCHEMA.md as the single source of truth with rules encoded in the validator. Only add a JSON Schema sidecar if the planner finds the duplication untenable.
- **A-3 — Summary template ↔ `session_summary` field relationship.** The schema's `session_summary` is a string; ART-01 is a markdown template. **Recommendation:** the template is the render target the agent fills, and the rendered markdown string populates `session_summary`. The validator treats `session_summary` as a required non-empty string and does NOT parse markdown structure.
- **A-4 — Validator CLI ergonomics & format details.** Exact argv shape, date-format strictness, belief `id` convention. **Recommendation:** `validate_session_schema.py <path> [--json]`; enforce ISO-8601 for date fields; keep the `belief_N` id convention from §9.

### Folded Todos
None — no pending todos matched this phase.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Design & scope
- `docs/design-draft.md` §9 State Schema — the canonical JSON session shape (`session_id`, `created_at`, `phase` enum, `presenting_disturbance`, `concrete_example`, `candidate_beliefs[]`, `selected_belief`, `normalized_proposition`, `definitions`, `implications[]`, `counterexamples[]`, `contradictions[]`, `revised_proposition`, `unresolved_tensions[]`, `next_questions[]`, `session_summary`). **Primary source for `SESSION_SCHEMA.md` (MTH-04).**
- `docs/design-draft.md` §7 Session Phases — the 6-phase procedural flow (intake → belief extraction → proposition normalization → socratic examination → contradiction/revision → session summary). Source of A-1 enum tension and of the summary-template content.
- `docs/design-draft.md` §7 Phase 6 — the Session Summary markdown template. **Primary source for `assets/session_summary_template.md` (ART-01).**
- `docs/design-draft.md` §8 Later Product Architecture — the `beliefs` / `propositions` / `contradictions` / `revisions` stores. **Primary source for `belief_graph_template.json` node types (ART-02).**
- `docs/design-draft.md` §14 Design Principle — "the examined proposition is the atomic unit." North star for artifact design.

### Phase 1 outputs (must integrate; do not re-litigate)
- `.planning/phases/01-core-skill-prototype/01-CONTEXT.md` — Phase 1 decisions D-01..D-16. Especially: D-01 (package placement in `philosophical-midwifery/` with `references/`), D-05 (pathologos defined in-place), D-06 (4 archetypes → reused verbatim in D-07 here), D-09/D-10 (directive second-person voice + soft/hard modal split), D-12 (shared "recognition determines worth" worked example → reused for fixtures + graph example).
- `philosophical-midwifery/SKILL.md` — the shipped skill file. Its session loop (steps 1–8) is left untouched per D-08.
- `philosophical-midwifery/references/{QUESTION_TAXONOMY,PATHOLOGOS_PATTERNS,SAFETY_BOUNDARIES}.md` — Phase 1 references. `SESSION_SCHEMA.md` joins these as a sibling in `references/`; voice should match (directive second-person where it gives the agent guidance, neutral schema-spec where it defines fields).

### Project-level
- `.planning/REQUIREMENTS.md` — MTH-04, ART-01, ART-02, ART-03 definitions (Phase 2 scope).
- `.planning/ROADMAP.md` §"Phase 2: Structured Session Artifacts" — phase goal and the 5 success criteria (the verification target).
- `.planning/PROJECT.md` — "Constraints" (runtime shape, safety, dialogue style, epistemic humility, method boundary, scope) and "Key Decisions" (examined proposition as atomic unit; defer harness/graph). Locked.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- No source code exists yet — Phase 1 shipped pure markdown. The reusable asset is the **package convention** established in Phase 1: `SKILL.md` at the `philosophical-midwifery/` root with YAML frontmatter; companion files under `references/`. Phase 2 adds two new sibling dirs: `philosophical-midwifery/assets/` and `philosophical-midwifery/scripts/`. `SESSION_SCHEMA.md` joins `philosophical-midwifery/references/`.

### Established Patterns
- **Voice:** directive second-person imperative for agent guidance; neutral spec prose for definitions (Phase 1 D-09/D-10). `SESSION_SCHEMA.md` should follow this split.
- **Shared worked example:** "recognition determines worth" threads all Phase 1 files (D-12). Phase 2 reuses it for both fixtures (D-04) and the graph worked example (D-05) to keep cross-references coherent.
- **Python:** Python 3.14.6 at `/opt/homebrew/bin/python3`. No `pyproject.toml` / `requirements.txt` exists. The validator MUST be **stdlib-only** (no `jsonschema`, no `pyyaml`) to keep the package zero-dependency (D-01).

### Integration Points
- `scripts/validate_session_schema.py` is invoked manually (`python3 scripts/validate_session_schema.py <path> [--json]`) and, in Phase 3, by the package-completeness/fixture check (EVAL-02/03).
- The session-JSON shape it validates is consumed (in v2) by HAR-01/HAR-02 (local harness + persistence).
- `belief_graph_template.json`'s property-graph shape anticipates GRPH-01..03 (v2 cross-session belief graph).

</code_context>

<specifics>
## Specific Ideas

- The **"recognition determines worth" example** (Phase 1 D-12) is the single shared worked example. Both `scripts/fixtures/valid.json` + `invalid.json` AND the belief-graph worked example must derive from it for cross-file coherence.
- `invalid.json` seeds **≥2 distinct error classes** (missing required field + bad `phase` value) so one fixture demonstrates multiple validator behaviors while holding the fixture count to the success-criterion minimum (one valid + one invalid).
- The belief-graph worked example traces: belief("Recognition determines worth", `pathologos_pattern: conditional_worth`) —`normalizes_to`→ proposition("The value of work depends on recognition") —`contradicts`→ contradiction(...) —`revises`→ revised_proposition("Recognition affects visibility and opportunity, but does not determine intrinsic worth."). This is derived directly from `docs/design-draft.md` §7 Phase 5 so the example stays consistent with the design reference.

</specifics>

<deferred>
## Deferred Ideas

- **Belief-graph cross-session recurrence machinery** (recurrence counters, `first_seen_session`, `provenance`) — GRPH-01..03 (v2). The v1 property-graph model leaves room for it (typed edges + node ids support it) but does not implement it.
- **Session-state persistence across turns** (HAR-02) — the schema defines the shape; persistence is v2 local-harness work.
- **JSON Schema sidecar file** — only revisit if the markdown-single-source approach (A-2) proves untenable during planning.
- **Per-archetype counter-questions / pattern-specific examination prompts** — already deferred in Phase 1; stays deferred.
- **Behavioral / dialogue fixtures** beyond the valid/invalid schema fixtures — EVAL-02 (Phase 3) covers overinterpretation-prevention, advice-avoidance, high-emotion slowdown, and safety-boundary handling.

### Reviewed Todos (not folded)
None — no todos were reviewed.

</deferred>

---

*Phase: 2-Structured Session Artifacts*
*Context gathered: 2026-06-24*
