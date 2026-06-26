---
status: complete
phase: 03-evaluation-hardening
mode: mvp
source: [03-01-SUMMARY.md]
user_story: "As a skill collaborator, I want to verify the skill behaves as designed across normal inquiry, boundary, and failure-mode examples, so that I can confirm the v1 package is ready to ship."
started: 2026-06-25T23:31:41Z
updated: 2026-06-25T23:41:25Z
---

## Current Test
<!-- OVERWRITE each test - shows where we are -->

[testing complete]

## Tests

<!-- MVP ordering: (A) user-flow walk-through runs first; if any step fails,
     HALT — do not run technical checks. (B) technical checks are deferred
     until the user flow passes. (C) coverage check is goal-backward against
     the user story's outcome clause ("confirm the v1 package is ready to ship"). -->

### Section A — User-flow walk-through (run first; halt on first failure)

### 1. Read the repo-root README as the collaborator entry point
expected: Opening `README.md` at the repo root shows the collaborator entry point: what the skill is, how to LOAD it, how to RUN THE CHECKS (both scripts with exact commands), how to SELF-EVALUATE (the 7-dimension rubric), the five BEHAVIORAL FIXTURES, a PACKAGE LAYOUT diagram, and a Limitations section stating "No known issues at v1 ship time" plus Out-of-scope-for-v1.
result: pass

### 2. Load the skill via SKILL.md activation frontmatter
expected: `philosophical-midwifery/SKILL.md` opens with YAML frontmatter `name: philosophical-midwifery` and a `description` field that states when to use the skill AND explicitly says "Do NOT use this skill for therapy, counseling, crisis response, medical or psychiatric advice, diagnosis, or generic reassurance." Below it: a "When NOT to use" section and the standing core inquiry loop (disturbance → concrete example → candidate beliefs → user selects/revises → normalize → examine → summary).
result: pass

### 3. Open the evaluation rubric and confirm the 7 dimensions
expected: `references/EVALUATION_RUBRIC.md` scores exactly seven dimensions verbatim from design-draft §13 (proposition clarity, user ownership, dialectical discipline, logical pressure, non-coercion, summary quality, practical usefulness), each on a 1–5 scale, with exactly ONE fully-worked scoring example (recognition-determines-worth) and an explicit statement that there is NO aggregate/roll-up score.
result: pass

### 4. Open the examples/ directory and confirm the five scenarios
expected: `philosophical-midwifery/examples/` contains five golden transcripts: `normal-inquiry.md`, `overinterpretation-prevention.md`, `advice-avoidance.md`, `high-emotion-slowdown.md`, and `safety-boundary-handling.md` — covering normal inquiry, overinterpretation prevention, advice avoidance, high-emotion slowdown, and safety-boundary handling.
result: pass

### 5. Run the package-completeness check
expected: From the repo root, `python3 philosophical-midwifery/scripts/check_package.py` prints `valid` and exits with code 0 (every required file present, every internal cross-reference resolving).
result: pass

### 6. Run the session-schema validator on a valid fixture
expected: `python3 philosophical-midwifery/scripts/validate_session_schema.py philosophical-midwifery/scripts/fixtures/valid.json` prints `valid` and exits with code 0.
result: pass

### Section B — Technical checks (deferred; run only after Section A passes)

### 7. Completeness check JSON mode
expected: `python3 philosophical-midwifery/scripts/check_package.py --json` prints a single JSON document `{"valid": true, "errors": []}` and exits 0.
result: pass

### 8. Session validator rejects the invalid fixture
expected: `python3 philosophical-midwifery/scripts/validate_session_schema.py philosophical-midwifery/scripts/fixtures/invalid.json` exits 1 and reports concrete problems (e.g., a missing required field, an invalid `phase` enum value, and a non-ISO-8601 date).
result: pass

### 9. Session validator JSON mode on valid fixture
expected: `python3 philosophical-midwifery/scripts/validate_session_schema.py philosophical-midwifery/scripts/fixtures/valid.json --json` prints a single JSON document with `"valid": true` and exits 0.
result: pass

### 10. Completeness check RED contract
expected: Against a deliberately broken package (e.g., remove a required file or strip a cross-reference), `check_package.py` exits 1 and lists each problem on its own line (presence failure or missing expected reference).
result: pass

### Section C — Coverage check (goal-backward against outcome clause)

### 11. Coverage: collaborator can confirm v1 readiness end-to-end
expected: Taken together, the shipped package gives a collaborator everything needed to confirm the v1 package is ready to ship: a README entry point, an activatable SKILL.md, a 7-dimension rubric for self-evaluation, five behavioral fixtures exercising normal/boundary/failure scenarios, and two stdlib-only scripts that mechanically verify package completeness and session artifacts — with Limitations honestly stated.
result: pass

## Summary

total: 11
passed: 11
issues: 0
pending: 0
skipped: 0
blocked: 0

## Gaps

[none yet]
