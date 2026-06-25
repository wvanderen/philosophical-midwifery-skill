---
phase: 03-evaluation-hardening
plan: 01
subsystem: evaluation
tags: [agent-skill, evaluation-rubric, behavioral-fixtures, package-completeness, python-stdlib, markdown, readme]

# Dependency graph
requires:
  - "Phase 1 skill package (SKILL.md + 3 references) — the rubric is a sibling that must not contradict the shipped loop; the fixtures assert against SKILL.md dialogue rules and SAFETY_BOUNDARIES.md's 5 stop conditions"
  - "Phase 2 session artifacts (SESSION_SCHEMA.md + validate_session_schema.py + assets) — check_package.py is a near-verbatim structural copy of the validator (D-04); the rubric's summary-quality dimension references the session_summary shape"
provides:
  - "Pure-prose human-scored evaluation rubric (EVALUATION_RUBRIC.md) — the 7 design-draft §13 dimensions verbatim, 1-5 scale, ONE recognition-determines-worth worked example, NO roll-up score; sibling to the Phase 1+2 references (D-01/D-02/D-03, A-5)"
  - "Five golden behavioral/dialogue fixtures (examples/*.md) — the 5 SC2 scenarios: normal inquiry, overinterpretation prevention, advice avoidance, high-emotion slowdown, safety-boundary handling (EVAL-02, D-06, A-1/A-2)"
  - "Stdlib-only package-completeness check (check_package.py) — required-file presence + internal cross-reference resolution; collect-all reporting; dual CLI/--json output; 0/1 exit codes (EVAL-03, D-04/D-05, A-3)"
  - "Repo-root collaborator README — what/load/run-both-checks/self-evaluate/fixtures/package-layout/Limitations/Out-of-scope-for-v1 (SC5, D-07/D-08, A-4)"
  - "Frozen SC4 human-review record (03-01-REVIEW.md) — APPROVED zero findings; all seven review checks passed (SC4, D-08)"
affects: [v2-local-harness, v2-belief-graph, v2-llm-judge]

# Tech tracking
tech-stack:
  added:
    - "python3 (stdlib only — sys, json, argparse, pathlib, typing) — no third-party packages; check_package.py mirrors validate_session_schema.py (D-04)"
  patterns:
    - "Rubric-as-sibling-reference: EVALUATION_RUBRIC.md joins the four Phase 1+2 references under references/ with a sibling declaration + single-source-of-truth + soft-modals voice note, mirroring SESSION_SCHEMA.md's entry pattern"
    - "Behavioral-fixture transcripts as a separate concern from machine fixtures: examples/*.md (human review) is deliberately split from scripts/fixtures/*.json (machine validation) per D-06"
    - "Cross-reference manifest derived from SKILL.md's 'Companion references' section, encoded directly in check_package.py as REQUIRED_FILES + CROSS_REFERENCES (A-3) — no YAML parsing, no external manifest"
    - "Threaded worked example (recognition-determines-worth) spanning the rubric's single scored example AND the normal-inquiry fixture for cross-file coherence (D-03/A-2/D-12, continuing Phase 1+2's pattern)"
    - "Clean transcripts with NO inline rubric annotations (A-2) — the single fully-scored example lives only in the rubric to avoid duplication/drift"

key-files:
  created:
    - philosophical-midwifery/references/EVALUATION_RUBRIC.md
    - philosophical-midwifery/examples/normal-inquiry.md
    - philosophical-midwifery/examples/overinterpretation-prevention.md
    - philosophical-midwifery/examples/advice-avoidance.md
    - philosophical-midwifery/examples/high-emotion-slowdown.md
    - philosophical-midwifery/examples/safety-boundary-handling.md
    - philosophical-midwifery/scripts/check_package.py
    - README.md
    - .planning/phases/03-evaluation-hardening/03-01-REVIEW.md
  modified: []

key-decisions:
  - "Rubric is a sibling reference under references/ voiced in soft modals addressing the scorer (D-01, A-5) — hard modals reserved for SAFETY_BOUNDARIES.md only"
  - "Scoring is pure-prose, human-scored with NO mechanical/regex scoring in v1; the rubric is written so a v2 LLM-judge can score the same criteria (D-02)"
  - "Exactly ONE recognition-determines-worth worked example and NO aggregate/composite/total score — scores stay a 7-tuple profile so a single-axis failure cannot be averaged away (D-03)"
  - "check_package.py is a near-verbatim structural copy of validate_session_schema.py (D-04) — only validate()'s body and the dropped <path> arg differ; package root resolved via Path(__file__).resolve().parent.parent"
  - "Completeness check uses a hardcoded REQUIRED_FILES manifest + CROSS_REFERENCES map derived from SKILL.md's companion-references section; no YAML frontmatter parsing (D-05, A-3)"
  - "examples/ is a new directory (D-06) holding 5 markdown transcripts — deliberately separate from scripts/fixtures/*.json; one golden transcript per SC2 scenario (A-1)"
  - "Repo-root README.md is the sole collaborator entry point; NO in-package README (D-07) — SKILL.md frontmatter remains the in-package activation doc"
  - "SC4 is a blocking human-review Task whose frozen record captures findings + disposition; deferred findings roll into README Limitations (D-08). Review returned ZERO findings, so Limitations states 'No known issues at v1 ship time' (A-4)"

patterns-established:
  - "Pattern: package-completeness check as a sibling validator — same docstring/argparse/--json/exit-code ergonomics as the session validator, giving the reviewer two interchangeable commands"
  - "Pattern: behavioral fixtures as clean transcripts with one-paragraph framing — separate from machine fixtures, scored by hand against the rubric"
  - "Pattern: threat-aware fixture authoring — red-flag/safety content clearly marked FIXTURE DATA so it cannot be misread as instruction or a real cry for help (T-03-03)"

requirements-completed:
  - EVAL-01
  - EVAL-02
  - EVAL-03

# Metrics
duration: "~35 min active (wall-clock ~8h45m including the blocking human-verify gate pause)"
completed: 2026-06-25
status: complete
---

# Phase 3: Evaluation & Hardening Summary

**Eight additive files that make the shipped skill inspectable by a human reviewer and mechanically verifiable as complete — a pure-prose 7-dimension rubric threaded by recognition-determines-worth, five golden behavioral fixtures, a stdlib-only completeness check sibling to the validator, and an honest repo-root README — with Phase 1+2's package left untouched and the v1 milestone signed off.**

## Performance

- **Duration:** ~35 min active (wall-clock ~8h45m including the blocking human-verify gate pause between Task 2 and Task 3)
- **Started:** 2026-06-25T15:06:49Z
- **Completed:** 2026-06-25T23:12:17Z
- **Tasks:** 3 (2 auto + 1 blocking human-verify checkpoint, APPROVED zero findings)
- **Files created:** 9 (8 package/repo files + 1 in-.planning/ review record); zero Phase 1 or Phase 2 files modified

## Accomplishments
- Authored `references/EVALUATION_RUBRIC.md` (EVAL-01, D-01/D-02/D-03, A-5) — the single source of truth for scoring a v1 session: a sibling-declaration + single-source + soft-modals voice note opening; a 1–5 anchor table; the seven design-draft §13 dimensions verbatim and in order, each with What-it-does / What-to-look-for scoring cues; an explicit "no roll-up score" section; and exactly ONE recognition-determines-worth worked example scored across all seven dimensions with no total.
- Authored five golden behavioral fixtures under a new `examples/` directory (EVAL-02, D-06, A-1/A-2) — `normal-inquiry.md` (clean full-loop recognition-determines-worth run), `overinterpretation-prevention.md` (candidates as hypotheses, user selects/revises), `advice-avoidance.md` (declines advice/reassurance/essay, returns to one question), `high-emotion-slowdown.md` (modulation rule fires, pace slows, inquiry continues — NOT a hard stop), and `safety-boundary-handling.md` (EXPLORATORY/RED-FLAG ruling; stop → 988/findahelpline → ask locale → MUST NOT auto-resume; red-flag content marked FIXTURE DATA).
- Authored `scripts/check_package.py` (EVAL-03, D-04/D-05, A-3) — a near-verbatim structural copy of `validate_session_schema.py`: stdlib-only, hardcoded `REQUIRED_FILES` (the full shipped package) + `CROSS_REFERENCES` (derived from SKILL.md's companion-references section), collect-all `validate(package_root) -> List[str]`, dual CLI/`--json` output, 0/1 exit codes, package root resolved via `Path(__file__).resolve().parent.parent`. Passed both GREEN (complete package) and RED (deliberately-broken temp copy) contracts.
- Authored repo-root `README.md` (SC5, D-07/D-08, A-4) — the sole collaborator entry point: what-this-is / load / run-both-checks / self-evaluate / behavioral-fixtures / package-layout / Limitations ("No known issues at v1 ship time") / Out-of-scope-for-v1. No in-package README created.
- Passed the blocking Task 3 human-verify gate — reviewer APPROVED with zero findings on all seven checks (rubric voice + sibling declaration; 7 dimensions + ONE worked example + NO roll-up; 5-fixture coverage; safety-stop fidelity to SAFETY_BOUNDARIES.md; recognition-determines-worth cross-file coherence; non-contradiction with SKILL.md; check_package ergonomics). The frozen record is `03-01-REVIEW.md`.
- Cross-cutting: the recognition-determines-worth thread stays coherent across all three phases — Phase 1 (SKILL.md + 3 references), Phase 2 (schema + graph + fixtures), and Phase 3 (rubric worked example + normal-inquiry fixture). Phase 1+2 files were not edited (Phase 2 D-08 additive-only continuity verified via `git diff`).

## Task Commits

Each task was committed atomically:

1. **Task 1: Author the evaluation layer — EVALUATION_RUBRIC.md + five examples/*.md fixtures** — `4c9770a` (feat)
2. **Task 2: Author the package-completeness check — check_package.py (TDD GREEN/RED)** — `d654ae8` (feat)
3. **Task 3: Blocking human review + post-approval deliverables (REVIEW + README)** — `62848b8` (docs); review checkpoint APPROVED zero findings

## Files Created/Modified
- `philosophical-midwifery/references/EVALUATION_RUBRIC.md` — Pure-prose human-scored rubric over the 7 design-draft §13 dimensions; 1–5 scale; ONE recognition-determines-worth worked example; no roll-up score (EVAL-01).
- `philosophical-midwifery/examples/normal-inquiry.md` — Golden full-loop recognition-determines-worth transcript (SC2 scenario 1).
- `philosophical-midwifery/examples/overinterpretation-prevention.md` — Candidates as hypotheses; user selects/revises (SC2 scenario 2).
- `philosophical-midwifery/examples/advice-avoidance.md` — No advice/reassurance/essay; one question at a time (SC2 scenario 3).
- `philosophical-midwifery/examples/high-emotion-slowdown.md` — Modulation rule fires; pace slows; inquiry continues (SC2 scenario 4).
- `philosophical-midwifery/examples/safety-boundary-handling.md` — EXPLORATORY/RED-FLAG; stop → resources → no-auto-resume (SC2 scenario 5; Phase 1 D-15).
- `philosophical-midwifery/scripts/check_package.py` — Stdlib-only package-completeness check; presence + cross-references; collect-all; dual output (EVAL-03).
- `README.md` — Repo-root collaborator entry point (SC5, D-07).
- `.planning/phases/03-evaluation-hardening/03-01-REVIEW.md` — Frozen SC4 review record; APPROVED zero findings (SC4, D-08).

## Decisions Made
- All eight CONTEXT decisions (D-01..D-08) and five clarifications (A-1..A-5) were pre-locked before execution; this plan executed them without re-derivation. No new architectural decisions were introduced.
- The completeness-check manifest was derived conservatively from the shipped file set and SKILL.md's "Companion references" section (A-3); only cross-references that genuinely appear in the shipped prose were encoded, verified by grep before encoding.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Reworded the rubric's "no aggregate score" section to avoid tripping the Task 1 automated substring gate**
- **Found during:** Task 1 (running the automated `<verify>` heredoc)
- **Issue:** The Task 1 automated check forbids the literal substrings "aggregate score", "composite score", and "total score" anywhere in EVALUATION_RUBRIC.md. The initial draft section heading ("No aggregate score (D-03)") and body phrasing ("total, average, or composite score") contained those exact substrings — even though the section's intent was to *forbid* such scores, not provide one.
- **Fix:** Reworded the section to "Scores stay a profile, not a roll-up (D-03)" and the body to "no sum, average, or composite figure" / "a roll-up '5.1 / 5.0' would hide" — preserving the no-roll-up intent (D-03) while satisfying the binding automated gate. No change to substance.
- **Files modified:** `philosophical-midwifery/references/EVALUATION_RUBRIC.md`
- **Verification:** Re-ran the Task 1 automated heredoc; printed "ALL TASK 1 CHECKS PASSED".
- **Committed in:** `4c9770a` (Task 1 commit)

---

**Total deviations:** 1 auto-fixed (1 bug).
**Impact on plan:** Cosmetic wording adjustment to satisfy the binding automated gate; no scope creep and no change to the substantive D-03 (no-aggregate) requirement. The remaining content was executed exactly as planned.

## Issues Encountered
None.

## User Setup Required
None — `check_package.py` is stdlib-only (no `pip install`). Run with: `python3 philosophical-midwifery/scripts/check_package.py [--json]`.

## Self-Check: PASSED
- All 9 created files exist on disk (verified).
- All three task commits (`4c9770a`, `d654ae8`, `62848b8`) present in `git log`.
- Task 1, Task 2, and Task 3 automated gates all printed their PASSED lines.
- `git diff --name-only 5eecaa3..HEAD` shows only the 8 new package/repo files + the in-.planning/ review record + this SUMMARY + STATE/ROADMAP — no Phase 1 or Phase 2 file (SKILL.md, the four Phase 1+2 references, the two assets, validate_session_schema.py, the schema fixtures) appears.

## Next Phase Readiness
- The v1 milestone is complete: all 15 v1 requirements (SKL-*, MTH-*, ART-*, EVAL-*) are satisfied across the three phases.
- The 8 files landed at the paths v2 expects, so the v2 local harness (HAR-*), persistent belief graph (GRPH-*), and LLM-judge harness can find them.
- The rubric is written so a v2 LLM-judge can score sessions against the same seven criteria without rewriting the rubric.
- `check_package.py` is the contract enforcer for package completeness; v2 may extend the manifest but should not duplicate the cross-reference logic.
- Cross-cutting: the recognition-determines-worth thread remains coherent across all three phases, giving v2 a stable shared example.

---

*v1 milestone sign-off: Phase 3 APPROVED zero findings on 2026-06-25. EVAL-01, EVAL-02, EVAL-03 complete. The skill package is v1-ready.*

*Phase: 03-evaluation-hardening*
*Completed: 2026-06-25*
