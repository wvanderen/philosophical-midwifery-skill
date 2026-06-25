# Roadmap: Philosophical Midwifery

**Created:** 2026-06-23
**Mode:** coarse / vertical MVP
**Core Value:** The skill must reliably help an agent isolate and examine a user-confirmed proposition without drifting into therapy, advice, reassurance, or essay-writing.

## Overview

| Phase | Name | Goal | Requirements |
|-------|------|------|--------------|
| 1 | 1/1 | Complete   | 2026-06-24 |
| 2 | Structured Session Artifacts | Add schema, templates, and validation for session outputs. | MTH-04, ART-01, ART-02, ART-03 |
| 3 | Evaluation & Hardening | Add fixtures and checks that verify the skill's behavior and package completeness. | EVAL-01, EVAL-02, EVAL-03 |

## Phases

### Phase 1: Core Skill Prototype

**Goal:** Create a loadable `philosophical-midwifery` Agent Skill that conducts the core inquiry loop and respects method/safety boundaries.
**Mode:** mvp

**Requirements:** SKL-01, SKL-02, SKL-03, SKL-04, SKL-05, MTH-01, MTH-02, MTH-03

**Plans:** 1/1 plans complete

Plans:

- [x] 01-01-PLAN.md — Author the complete 4-file skill package (SKILL.md + 3 references) as one coherent deliverable, with a blocking human-verify checkpoint for safety-boundary prose and cross-file consistency.

**Success Criteria**:

1. `SKILL.md` exists with correct front matter, trigger conditions, role boundaries, and dialogue rules.
2. The skill explicitly guides disturbance -> candidate belief -> user-confirmed proposition -> examination -> contradiction/revision -> summary.
3. The skill forbids therapy, diagnosis, advice-giving, generic reassurance, overinterpretation, and essay-mode responses.
4. `QUESTION_TAXONOMY.md`, `PATHOLOGOS_PATTERNS.md`, and `SAFETY_BOUNDARIES.md` exist and are referenced by the skill.
5. Safety boundaries include crisis and diagnosis stop conditions with an appropriate response pattern.

**UI hint:** no

### Phase 2: Structured Session Artifacts

**Goal:** Provide the structured schema, templates, and validator that make session artifacts consistent and inspectable.
**Mode:** mvp

**Requirements:** MTH-04, ART-01, ART-02, ART-03

**Plans:** 1/1 plans complete

Plans:

- [x] 02-01-PLAN.md — Author the additive artifact layer (SESSION_SCHEMA.md + summary template + belief-graph seed) and the machine-checkable loop (stdlib validator + valid/invalid fixtures), threaded by the shared "recognition determines worth" example, with a blocking human-verify gate for voice/optionality/cross-file coherence.

**Success Criteria**:

1. `SESSION_SCHEMA.md` defines all required session state fields and allowed phase values.
2. `assets/session_summary_template.md` captures the final inquiry artifact without asserting certainty beyond the conversation.
3. `assets/belief_graph_template.json` provides a future-compatible graph seed while remaining optional for v1.
4. `scripts/validate_session_schema.py` validates representative session JSON and reports missing or invalid fields clearly.
5. At least one valid and one invalid fixture demonstrate validator behavior.

**UI hint:** no

### Phase 3: Evaluation & Hardening

**Goal:** As a skill collaborator, I want to verify the skill behaves as designed across normal inquiry, boundary, and failure-mode examples, so that I can confirm the v1 package is ready to ship.
**Mode:** mvp

**Requirements:** EVAL-01, EVAL-02, EVAL-03

**Plans:** 1/1 plans complete

Plans:

- [x] 03-01-PLAN.md — Author the evaluation/hardening layer (EVALUATION_RUBRIC.md + 5 examples/*.md fixtures + check_package.py + repo-root README + frozen review record) as one coherent additive deliverable threaded by the recognition-determines-worth example, with a blocking human-verify checkpoint for rubric voice, 7-dimension fidelity, fixture coverage, safety-stop fidelity, and cross-file coherence.

**Success Criteria**:

1. Evaluation guidance scores sessions on proposition clarity, user ownership, dialectical discipline, logical pressure, non-coercion, summary quality, and practical usefulness.
2. Fixtures or examples cover normal inquiry, overinterpretation prevention, advice avoidance, high-emotion slowdown, and safety-boundary handling.
3. A lightweight package-completeness check confirms required files are present and internally referenced.
4. Manual review notes identify any remaining prompt weaknesses before the skill is considered v1-ready.
5. README or usage notes explain how to run validation and how to test the skill manually.

**UI hint:** no

## Requirement Coverage

| Requirement | Phase | Status |
|-------------|-------|--------|
| SKL-01 | Phase 1 | Complete |
| SKL-02 | Phase 1 | Complete |
| SKL-03 | Phase 1 | Complete |
| SKL-04 | Phase 1 | Complete |
| SKL-05 | Phase 1 | Complete |
| MTH-01 | Phase 1 | Complete |
| MTH-02 | Phase 1 | Complete |
| MTH-03 | Phase 1 | Complete |
| MTH-04 | Phase 2 | Complete |
| ART-01 | Phase 2 | Complete |
| ART-02 | Phase 2 | Complete |
| ART-03 | Phase 2 | Complete |
| EVAL-01 | Phase 3 | Complete |
| EVAL-02 | Phase 3 | Complete |
| EVAL-03 | Phase 3 | Complete |

**Coverage:** 15/15 v1 requirements mapped.

## Notes

- Roadmap generation was performed inline because this Codex runtime did not allow automatic subagent spawning without explicit user authorization.
- Phase 1 should remain focused on skill behavior. Avoid pulling the local harness or belief graph forward unless the skill-only prototype proves insufficient.

---
*Roadmap created: 2026-06-23*
