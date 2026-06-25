# Phase 3: Evaluation & Hardening - Context

**Gathered:** 2026-06-24
**Status:** Ready for planning

<domain>
## Phase Boundary

Deliver the evaluation + verification layer that sits on top of the shipped Phase 1+2 skill package — making the skill's behavior inspectable by a human reviewer and the package mechanically checkable for completeness. Four additive deliverables, all under `philosophical-midwifery/` (plus one repo-root file):

- `references/EVALUATION_RUBRIC.md` (EVAL-01) — prose guidance scoring sessions on the 7 design-draft §13 dimensions, with one worked example.
- `examples/*.md` (EVAL-02) — five behavioral/dialogue fixture transcripts covering normal inquiry, overinterpretation prevention, advice avoidance, high-emotion slowdown, and safety-boundary handling.
- `scripts/check_package.py` (EVAL-03) — lightweight package-completeness check confirming required files are present and internally referenced.
- Repo-root `README.md` (SC5) — usage notes: load the skill, run the validator + completeness check, self-evaluate with the rubric.
- A frozen human-review record in `.planning/phases/03-evaluation-hardening/` (SC4) — blocking review whose deferred findings roll into a README "Limitations" section.

This phase covers EVAL-01, EVAL-02, EVAL-03. Phase 1's four files and Phase 2's six files are NOT edited (continuing Phase 2 D-08's additive-only pattern); the only exception is the repo-root `README.md`, which is created fresh (no prior README exists). No local harness, no LLM-judge automation, no persistence — those remain v2 (HAR-*/GRPH-*).

</domain>

<decisions>
## Implementation Decisions

### Evaluation rubric (EVAL-01)
- **D-01:** The 7-dimension rubric lives at `philosophical-midwifery/references/EVALUATION_RUBRIC.md`, joining the four existing references. It is guidance prose the reviewer/agent consults — consistent with Phase 1 D-01 (references/ holds method guidance). Voice follows Phase 1 D-09/D-10: directive second-person addressing the scorer.
- **D-02:** Scoring is **pure prose, human-scored**. Per-dimension criteria + the 1–5 scale from design-draft §13. There is **no mechanical/regex scoring** of behavioral properties (they resist it and risk false signals). EVAL-02 behavioral fixtures are illustrative markdown transcripts a human scores by hand. An LLM-judge harness is deferred to v2 (HAR-* scope); the rubric is written so a v2 judge can score against the same criteria, but no judge ships in v1.
- **D-03:** The rubric includes **ONE worked scoring example** using the shared recognition-determines-worth transcript (coherent with Phase 1 D-12 / Phase 2 D-04), showing how each of the 7 dimensions scores. There is **NO aggregate/composite score** — scores stay as a 7-tuple profile. Rationale: the dimensions measure different things (e.g., non-coercion vs. clarity), and a total can mask a critical single-axis failure.

### Package-completeness check (EVAL-03)
- **D-04:** A new `philosophical-midwifery/scripts/check_package.py`, sibling to `validate_session_schema.py`. It mirrors Phase 2's tooling conventions verbatim: **stdlib-only** (no third-party deps), **dual output** (CLI prose default + `--json`), **collect-all** error reporting, exit `0` valid / `1` invalid. One consistent Python-tooling story; the reviewer runs two `python3` commands.
- **D-05:** Check depth = **presence + internal cross-references** (SC3's literal wording). It asserts every required file exists AND that internal references resolve (e.g., SKILL.md names each `references/*` file it consults; references cross-link where expected; SESSION_SCHEMA.md is reachable). The required-file manifest is **hardcoded in the script** (mirrors the validator's "encode rules directly" pattern, Phase 2 A-2). It does **not** parse YAML frontmatter (would need hand-rolled parsing under stdlib-only; out of scope for v1 — see Deferred).

### Behavioral fixtures (EVAL-02)
- **D-06:** A new `philosophical-midwifery/examples/` directory holds the five behavioral/dialogue fixture transcripts as markdown. This cleanly separates human-review transcripts from `scripts/fixtures/*.json` (Phase 2's machine-checkable schema fixtures) — a deliberate concern split. The completeness-check manifest lists the `examples/` group. (Fixture format was left to agent discretion by the user; resolved here as illustrative markdown transcripts per D-02.)

### README & review notes (SC4, SC5)
- **D-07:** A repo-root `README.md` is the primary user/collaborator entry point. It covers: what the skill is, how to load it, how to run the validator + completeness check (exact commands), how to self-evaluate with the rubric, and where fixtures/examples live. `SKILL.md` frontmatter remains the in-package activation doc (no in-package README — would duplicate/drift).
- **D-08:** SC4 manual review is a **blocking human-review Task** (same gate pattern as Phase 1/2 Task 3). It produces a frozen review record in `.planning/phases/03-evaluation-hardening/` capturing findings + disposition (fixed-now vs. deferred). Findings marked "deferred" roll up into a short **"Limitations / Known Issues" section** in the repo-root README, so v1 ships with honest, visible known gaps rather than a standalone weaknesses doc.

### Agent's Discretion
Gray areas resolved by recommendation; researcher/planner may adjust within these bounds without re-asking the user.

- **A-1 — Behavioral-fixture coverage breadth.** SC2 requires the 5 scenario types be covered. **Recommendation:** ONE transcript per scenario (satisfies the SC2 minimum), each demonstrating the DESIRED ("golden") behavior. The safety-boundary transcript must show the full stop → curated resources → no-auto-resume pattern (Phase 1 D-15). If the SC4 reviewer finds a scenario ambiguous, a paired failure example may be added during review.
- **A-2 — Transcript annotation style.** Whether each `examples/` transcript carries inline rubric annotations or stays a clean transcript. **Recommendation:** clean transcripts in `examples/`; the single fully-worked scored example lives in `EVALUATION_RUBRIC.md` (D-03) to avoid duplication/drift.
- **A-3 — Completeness-check manifest + cross-reference map.** The precise list of which file references which, encoded directly in `check_package.py`. **Recommendation:** derive from the shipped file set + SKILL.md's "Companion references" section (the authoritative cross-reference source).
- **A-4 — README section order/wording + Limitations content.** Populated from the SC4 review findings (D-08 dependency: review runs before Limitations is finalized).
- **A-5 — Rubric voice specifics.** Follow Phase 1 D-09/D-10: directive second-person for guidance; hard modals reserved for safety (the rubric itself uses soft guidance since it addresses a scorer, not a crisis path).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Design & scope
- `docs/design-draft.md` §13 Evaluation Rubric — the canonical 7 scoring dimensions + 1–5 scale. **Primary source for EVAL-01 (D-01/D-02/D-03).** Do not add or rename dimensions.
- `docs/design-draft.md` §12 Milestone 1 success criteria — "test manually in real conversations"; "agent consistently isolates a proposition / asks one question at a time / does not drift into advice / user leaves with a session artifact." Anchors what the behavioral fixtures (EVAL-02) and rubric (EVAL-01) must exercise.
- `docs/design-draft.md` §7 Phase 6 (Session Summary) + §11 (Safety Boundaries) — source material for the safety-boundary and summary-quality fixture scenarios.
- `docs/design-draft.md` §14 Design Principle — "the examined proposition is the atomic unit." North star for what the rubric's "proposition clarity" and "practical usefulness" dimensions measure.
- `.planning/REQUIREMENTS.md` — EVAL-01, EVAL-02, EVAL-03 definitions (Phase 3 scope).
- `.planning/ROADMAP.md` §"Phase 3: Evaluation & Hardening" — phase goal + the 5 success criteria (the verification target).
- `.planning/PROJECT.md` — "Constraints" (runtime shape, safety, dialogue style, epistemic humility, method boundary) and "Key Decisions" (examined proposition as atomic unit; defer harness/graph). Locked.

### Phase 1 outputs (must integrate; do not re-litigate)
- `.planning/phases/01-core-skill-prototype/01-CONTEXT.md` — D-01 (package placement in `philosophical-midwifery/`), D-09/D-10 (directive voice + soft/hard modal split), D-12 (shared recognition-determines-worth example → reused for the rubric worked example + normal-inquiry fixture), D-15 (resume gate → safety-boundary fixture must demonstrate it), D-16 (safety = hard stops in SAFETY_BOUNDARIES.md; modulation = SKILL.md dialogue rules).
- `philosophical-midwifery/SKILL.md` — shipped skill. Its "Companion references" section is the **authoritative source for the cross-references the completeness check must verify** (D-05, A-3); its "When NOT to use" + dialogue rules define what the advice-avoidance / overinterpretation / high-emotion fixtures assert against.
- `philosophical-midwifery/references/{QUESTION_TAXONOMY,PATHOLOGOS_PATTERNS,SAFETY_BOUNDARIES}.md` — Phase 1 references. `EVALUATION_RUBRIC.md` joins these as a sibling (D-01). The safety-boundary fixture must be consistent with SAFETY_BOUNDARIES.md's 5 stop conditions.

### Phase 2 outputs (must integrate; do not re-litigate)
- `.planning/phases/02-structured-session-artifacts/02-CONTEXT.md` — D-01 (stdlib-only validator), D-02 (`--json` dual output), D-03 (collect-all), D-04 (fixtures location + shared example), A-2 (schema as single source of truth, rules encoded directly). `check_package.py` mirrors ALL of these (D-04/D-05).
- `philosophical-midwifery/scripts/validate_session_schema.py` — the **direct tooling template** `check_package.py` copies: module docstring structure, argparse shape, `--json` output contract (`{"valid": bool, "errors": [...]}`), collect-all `validate() → List[str]` pattern, exit-code convention. Stdlib-only imports (`sys`/`json`/`argparse`/`pathlib`).
- `philosophical-midwifery/references/SESSION_SCHEMA.md` — canonical session shape; the rubric's summary-quality dimension and the fixtures reference this shape. Must remain a completeness-check manifest entry.
- `philosophical-midwifery/scripts/fixtures/{valid,invalid}.json` — Phase 2's machine-checkable schema fixtures; Phase 3's `examples/*.md` transcripts are a DIFFERENT concern (human review, not validation) per D-06 — do not merge the directories.

### Project-level
- `.planning/STATE.md` — confirms Phase 3 builds on the canonical schema + validator; recognition-determines-worth thread stays coherent across all three phases.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `philosophical-midwifery/scripts/validate_session_schema.py` — the direct template for `check_package.py`. Copy its module-docstring structure, argparse shape, `--json` output contract, collect-all `validate()` pattern, and exit-code convention. Adapt: no `<path>` arg (operates on the package root relative to the script), `--json` unchanged.
- `philosophical-midwifery/SKILL.md` "Companion references" section — the authoritative cross-reference map the completeness check encodes (D-05, A-3).
- The recognition-determines-worth example (threaded across Phase 1 + 2) — the content seed for the rubric worked example (D-03) and the "normal inquiry" behavioral fixture.

### Established Patterns
- **Tooling conventions (Phase 2 D-01..D-03):** stdlib-only Python, dual CLI/`--json` output, collect-all reporting, exit 0/1. `check_package.py` follows this verbatim (D-04).
- **Voice (Phase 1 D-09/D-10):** directive second-person for agent/reviewer guidance; `EVALUATION_RUBRIC.md` addresses the scorer. Hard modals reserved for safety; the rubric uses soft guidance.
- **Shared worked example (Phase 1 D-12, Phase 2 D-04/D-05):** recognition-determines-worth threads all files; Phase 3 reuses it for the rubric worked example + normal-inquiry fixture for cross-file coherence. The other 4 fixtures may use fresh scenarios (they exercise different behaviors).
- **Additive-only (Phase 2 D-08):** Phase 1+2 shipped files are NOT edited; Phase 3 adds new files only (`EVALUATION_RUBRIC.md`, `check_package.py`, `examples/*`, repo-root `README.md`).

### Integration Points
- `check_package.py` runs manually (`python3 philosophical-midwifery/scripts/check_package.py [--json]`) and is documented in README alongside the validator.
- `EVALUATION_RUBRIC.md` is referenced from README's self-evaluation section and is itself a completeness-check manifest entry.
- `examples/*.md` are referenced from README (how to test manually) and are completeness-check manifest entries as a group.
- The SC4 human-review Task's deferred findings flow INTO the README "Limitations" section (D-08) — a one-way dependency: the review must run before README Limitations is finalized.

</code_context>

<specifics>
## Specific Ideas

- The **recognition-determines-worth example** remains the single shared worked example. The rubric's ONE worked scoring example (D-03) and the "normal inquiry" behavioral fixture both derive from it. The other 4 behavioral fixtures (overinterpretation, advice, high-emotion, safety) need NOT all use it — they can use fresh scenarios tailored to the behavior they exercise.
- The **7 rubric dimensions are fixed** by design-draft §13: proposition clarity, user ownership, dialectical discipline, logical pressure, non-coercion, summary quality, practical usefulness. Do NOT add, drop, or rename.
- The **5 fixture scenarios are fixed** by ROADMAP SC2: normal inquiry, overinterpretation prevention, advice avoidance, high-emotion slowdown, safety-boundary handling.
- Python 3.14.6 at `/opt/homebrew/bin/python3`; no `pyproject.toml`/`requirements.txt` exists. `check_package.py` MUST be stdlib-only to keep the package zero-dependency (Phase 2 D-01 continuity).
- No repo-root `README.md` exists yet — Phase 3 creates it fresh (no merge concerns).

</specifics>

<deferred>
## Deferred Ideas

- **LLM-judge harness** for automated rubric scoring — v2 (HAR-* local-harness scope). The v1 rubric is written so a v2 judge can score against the same criteria, but no judge ships in v1.
- **Mechanical behavioral assertions** (regex/AST checks for "one question at a time", advice-phrase detection) — deliberately out of v1; behavioral properties resist mechanical assertion and risk false signals. Revisit only if the v2 harness needs pre-filtering before LLM judging.
- **Per-scenario paired failure examples** (good + bad transcript per scenario) — deferred unless the SC4 review flags a scenario as ambiguous; v1 ships one golden transcript per scenario (A-1).
- **YAML frontmatter validation** in the completeness check — deferred (would need hand-rolled parsing under stdlib-only); revisit if frontmatter drift becomes a real problem.
- **Structured behavioral-fixture format** (JSON cases with expected scores) — resolved as markdown transcripts for v1 (D-02/D-06); structured cases are a v2 concern tied to the LLM-judge harness.
- **Region-indexed crisis resources / additional pathologos archetypes / per-archetype counter-questions** — already deferred in Phase 1; stays deferred.

</deferred>

---

*Phase: 3-Evaluation & Hardening*
*Context gathered: 2026-06-24*
