# Project Retrospective

*A living document updated after each milestone. Lessons feed forward into future planning.*

## Milestone: v1.0 — MVP

**Shipped:** 2026-06-26
**Phases:** 3 | **Plans:** 3 | **Duration:** 3 days (2026-06-23 → 2026-06-25)

### What Was Built
- A portable, zero-dependency `philosophical-midwifery` Agent Skill package (17 files + repo-root README): SKILL.md entrypoint + 5 companion references (pathologos, taxonomy, safety, session schema, evaluation rubric).
- Structured session-artifacts layer: canonical SESSION_SCHEMA, summary template, optional belief-graph seed, and a stdlib-only session-JSON validator with valid/invalid fixtures.
- Evaluation & hardening layer: pure-prose 7-dimension rubric, 5 golden behavioral fixtures, stdlib-only package-completeness check, collaborator README.

### What Worked
- **Pre-locked decisions in CONTEXT (D-01..D-08) before planning.** Each plan executed verbatim with "None — plan executed exactly as written" deviations; no re-derivation mid-execution.
- **Blocking human-verify gates as the verification mechanism for safety-critical prose.** All three gates returned APPROVED with zero or minor findings, catching nothing because the pre-lock held — high signal, low cost.
- **Stdlib-only constraint.** Both validators run with `python3` alone; the audit could mechanically re-verify them live, and portability across runtimes is unconditional.
- **One threaded worked example ("recognition determines worth") across all 3 phases.** Cheap cross-file coherence spine; the integration check confirmed it present in all 11 expected files.
- **Additive-only phases.** Phase 2 and Phase 3 touched zero Phase-1 files, so no rework and no regression surface.

### What Was Inefficient
- **No per-phase `VERIFICATION.md` (TD-1).** Phases relied on blocking human-verify gates + UAT rather than `gsd-verifier`, which left a traceability gap the milestone audit had to flag as tech debt. Running `/gsd-verifier` per phase would have closed this cheaply.
- **ROADMAP.md prose format drifted from the parser's expectations.** `roadmap.analyze` reported 75% / Phase 2 partial at close because the roadmap used `### Phase N:` headers + inline "Plans: 1/1" instead of `- [x]` task checkboxes, and counted `02-PLAN-CHECK.md` as a second plan. Required manual reconciliation against STATE.md + the audit.
- **Inline planning (no subagents) due to the Codex runtime constraint.** Research and roadmap were generated in a single context, which is heavier on context budget than the parallel-subagent path.

### Patterns Established
- **Schema-as-source-of-truth + stdlib validator (no schema-language dependency).** The Markdown schema documents the rules; the validator encodes them directly. Reused verbatim by `check_package.py`.
- **Fixture-driven contracts.** Derive `valid.json` + `invalid.json` siblings from the same shared example so cross-references stay coherent and behavior is locked before code.
- **Optionality signaling via JSON header markers** (`_v1_optional` + `_note`) for any future-compatible artifact that must not be required in the current version.
- **Behavioral fixtures as clean transcripts (one-paragraph framing), separate from machine fixtures** — scored by hand against the rubric.
- **Threat-aware fixture authoring** — red-flag/safety content marked `FIXTURE DATA` so it cannot be misread as instruction.

### Key Lessons
1. **Pre-lock decisions in CONTEXT before authoring the PLAN.** When D-01..D-08 + clarifications A-1..A-5 are settled first, plans execute with zero deviation. Repeat this for every phase.
2. **Run `/gsd-verifier` per phase, not just human gates.** Human-verify gates are sufficient for safety prose but leave a traceability gap at audit. The two together are cheap and close TD-1 entirely.
3. **Keep validators stdlib-only.** It makes the package portable, sandbox-safe, and live-reverifiable by an auditor with a single `python3` command.
4. **Use one threaded worked example per milestone.** It is the cheapest coherence insurance — a single grep confirms cross-file consistency.
5. **Write ROADMAP.md phase entries as `- [x]` checkboxes the parser can count**, or treat the parser's progress number as advisory and rely on STATE.md frontmatter + the milestone audit as authoritative.

### Cost Observations
- Model profile: inherit (single-model execution; no opus/sonnet/haiku mix data captured this milestone).
- Sessions: ~6 (3 phase-context + 3 plan/execute) plus milestone audit + this close.
- Notable: coarse vertical-MVP mode (1 plan per phase) kept planning overhead low; each phase shipped in ~17-35 active minutes.

---

## Cross-Milestone Trends

### Process Evolution

| Milestone | Sessions | Phases | Key Change |
|-----------|----------|--------|------------|
| v1.0 | ~6 | 3 | Baseline: pre-locked CONTEXT decisions; blocking human-verify gates; inline planning (no subagents). |

### Cumulative Quality

| Milestone | Automated Checks | Third-Party Deps Added | Audit Status |
|-----------|------------------|------------------------|--------------|
| v1.0 | 2 (session validator, package-completeness) | 0 | tech_debt (15/15 reqs, 6/6 flows; 2 non-blocking debt items) |

### Top Lessons (Verified Across Milestones)

1. *(Seeded at v1.0 — to be cross-validated at v2.0)* Pre-lock decisions in CONTEXT before planning; plans then execute verbatim.
2. *(Seeded at v1.0)* Keep package checks stdlib-only for portability and live audit-reverifiability.

---

*Last updated: 2026-06-26 after v1.0 milestone*
