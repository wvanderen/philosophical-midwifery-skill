# Roadmap: Philosophical Midwifery

**Core Value:** The skill must reliably help an agent isolate and examine a user-confirmed proposition without drifting into therapy, advice, reassurance, or essay-writing.

## Milestones

- ✅ **v1.0 MVP** — Phases 1-3 (shipped 2026-06-26) — [archive](milestones/v1.0-ROADMAP.md)
- 📋 **v2.0** — Local harness + persistent belief graph + LLM-judge (planned — define via `/gsd-new-milestone`)

## Phases

<details>
<summary>✅ v1.0 MVP (Phases 1-3) — SHIPPED 2026-06-26</summary>

- [x] Phase 1: Core Skill Prototype (1/1 plan) — completed 2026-06-24
- [x] Phase 2: Structured Session Artifacts (1/1 plan) — completed 2026-06-24
- [x] Phase 3: Evaluation & Hardening (1/1 plan) — completed 2026-06-25

**Outcome:** 15/15 v1 requirements satisfied; 6/6 E2E collaborator flows pass; MVP UAT 11/11; all human-verify gates APPROVED zero findings.

</details>

### 📋 v2.0 (Planned)

v2 scope (from REQUIREMENTS.md v2 section, to be re-confirmed at milestone start):

- [ ] Local harness (HAR-01..03): local CLI / web chat using the skill; persist JSON session state; export transcripts + summaries.
- [ ] Persistent belief graph (GRPH-01..03): persist belief records across sessions; link recurring propositions + pathologos patterns; inspectable + correctable belief map.
- [ ] LLM-judge harness for the 7-dimension rubric.

> Phases for v2 will be defined by `/gsd-new-milestone`. Phase numbering continues from 4 (never restarts at 1).

## Notes

- v1.0 roadmap archived in full at `.planning/milestones/v1.0-ROADMAP.md`.
- v2.0 scope above is carried over from the v1 REQUIREMENTS.md `## v2 Requirements` section; it will be re-validated during `/gsd-new-milestone` questioning before becoming the active roadmap.
- Known deferred tech debt from v1 (non-blocking): TD-1 no per-phase `VERIFICATION.md` (phases verified via human-verify gates + UAT); TD-2 pathologos machine-name contract is conventional, not codified (address alongside GRPH work in v2).

---
*Roadmap reorganized: 2026-06-26 after v1.0 milestone archive*
