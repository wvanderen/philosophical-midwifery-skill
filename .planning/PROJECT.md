# Philosophical Midwifery

## What This Is

Philosophical Midwifery is an Agent Skill that helps an AI agent conduct structured philosophical midwifery-style inquiry. It guides a user from a felt disturbance to a hidden belief, then to an explicit proposition that can be examined for coherence through disciplined Socratic questioning.

The project is not a therapy, coaching, advice, or reassurance system. It is a skill package for structured philosophical self-examination, with safety boundaries and session artifacts that keep the inquiry careful, non-coercive, and grounded in the user's own confirmations.

**Current state (v1.0 — shipped 2026-06-26):** a portable, zero-dependency Agent Skill package — pure Markdown + Python stdlib. 17 shipped files plus a repo-root README: `SKILL.md` entrypoint, 5 companion references (pathologos, taxonomy, safety, session schema, evaluation rubric), 2 asset templates (summary + belief-graph seed), 5 behavioral fixtures, and 2 stdlib-only checks (session validator + package-completeness). Verified by MVP UAT (11/11) and a passed milestone audit.

## Core Value

The skill must reliably help an agent isolate and examine a user-confirmed proposition without drifting into therapy, advice, reassurance, or essay-writing.

## Requirements

### Validated

- ✓ [SKL-01] Loadable `philosophical-midwifery` Agent Skill with YAML front matter — v1.0
- ✓ [SKL-02] Skill follows the loop: disturbance -> hidden belief -> explicit proposition -> examination -> contradiction/revision -> session summary — v1.0
- ✓ [SKL-03] Skill asks one substantive question at a time; prefers inquiry over assertion — v1.0
- ✓ [SKL-04] Skill presents candidate hidden beliefs as hypotheses, not conclusions — v1.0
- ✓ [SKL-05] Skill asks the user to select, reject, or revise a candidate belief before examining it — v1.0
- ✓ [MTH-01] Question taxonomy reference (clarification, universalization, implication, counterexample, necessity/sufficiency, domain separation, contradiction testing, reformulation) — v1.0
- ✓ [MTH-02] Pathologos pattern guidance that generates candidate beliefs without overclaiming certainty — v1.0
- ✓ [MTH-03] Safety boundaries stopping inquiry for self-harm, harm-to-others, acute crisis, reality-testing loss, or diagnosis requests — v1.0
- ✓ [MTH-04] Session schema capturing inquiry state fields — v1.0
- ✓ [ART-01] Session summary template capturing the full inquiry artifact without overclaiming certainty — v1.0
- ✓ [ART-02] Belief graph JSON template as a seed for later recurring-belief analysis — v1.0
- ✓ [ART-03] Local stdlib-only validator for session JSON artifacts — v1.0
- ✓ [EVAL-01] Evaluate sessions on proposition clarity, user ownership, dialectical discipline, logical pressure, non-coercion, summary quality, and practical usefulness — v1.0
- ✓ [EVAL-02] Fixtures testing normal inquiry, overinterpretation prevention, advice avoidance, and safety-boundary handling — v1.0
- ✓ [EVAL-03] Lightweight automated package-completeness check — v1.0

### Active

- [ ] [HAR-01] Local CLI or simple web chat harness using the skill (v2)
- [ ] [HAR-02] Persist JSON session state across turns (v2)
- [ ] [HAR-03] Export transcripts and generated session summaries (v2)
- [ ] [GRPH-01] Persist belief records across sessions (v2)
- [ ] [GRPH-02] Link recurring propositions and pathologos patterns (v2)
- [ ] [GRPH-03] Inspectable and correctable belief map (v2)
- [ ] LLM-judge harness scoring sessions against the 7-dimension rubric (v2)
- [ ] (Tech debt) Codify pathologos machine-name contract — add `machine_name:` tags or extend `check_package.py` (TD-2; pairs with GRPH work)

### Out of Scope

- Mental health treatment or diagnosis - the skill is for philosophical inquiry, not clinical care.
- Crisis counseling - crisis language should trigger boundary handling and human support resources, not continued inquiry.
- Generic self-help advice or coaching - the product value is examination, not guidance or encouragement.
- CBT-style reframing as the main output - contradiction and revision may occur, but the method should remain philosophical and dialectical.

## Context

**Shipped v1.0** (2026-06-26) as a pure-Markdown + Python-stdlib Agent Skill package — zero third-party dependencies, portable across compatible agents (opencode, Claude Code). 17 shipped files + repo-root README; ~5,873 LOC added across 45 files over 3 days.

**Tech stack:** Markdown references/templates, JSON fixtures, Python 3 stdlib only (`sys`, `json`, `datetime`, `argparse`, `pathlib`, `typing`). No `pip install` required for any v1 check.

**Coherence spine:** the "recognition determines worth" worked example is threaded consistently across all three phases (11 files), giving reviewers a single traceable thread from SKILL.md through the schema, fixtures, rubric, and examples.

**Verification evidence:** MVP UAT 11/11 passed; all three blocking human-verify gates APPROVED zero findings; milestone audit `tech_debt` (15/15 requirements, 6/6 E2E flows, 15/15 integration).

**Known tech debt (non-blocking, deferred to v2):**
- TD-1: No per-phase `VERIFICATION.md` — phases verified via blocking human-verify gates + UAT rather than `gsd-verifier`.
- TD-2: Pathologos machine-name contract between `belief_graph_template.json` (snake_case) and `PATHOLOGOS_PATTERNS.md` (Title-Case headings) is conventional, not mechanically guarded. Becomes load-bearing in v2 GRPH work.

**Next milestone (v2) candidate scope:** local harness (HAR-01..03), persistent belief graph (GRPH-01..03), and an LLM-judge harness scoring sessions against the shipped 7-dimension rubric.

The original design draft's package structure shipped essentially as planned:

```text
philosophical-midwifery/
  SKILL.md
  references/   (PATHOLOGOS_PATTERNS, QUESTION_TAXONOMY, SAFETY_BOUNDARIES, SESSION_SCHEMA, EVALUATION_RUBRIC)
  assets/       (session_summary_template.md, belief_graph_template.json)
  examples/     (5 behavioral fixtures)
  scripts/      (validate_session_schema.py, check_package.py, fixtures/)
```

## Constraints

- **Runtime shape**: Start as an Agent Skill package - this keeps v1 portable across compatible agents.
- **Safety**: The skill must stop normal inquiry when crisis or diagnostic boundaries are crossed.
- **Dialogue style**: Ask one substantive question at a time and prefer questions over assertions.
- **Epistemic humility**: Candidate beliefs are hypotheses, not conclusions; the user remains the authority on their experience.
- **Method boundary**: Keep logic, implication, contradiction, and reformulation as the working tools.
- **Scope**: Build the skill-only prototype before any local harness, web UI, or persistent belief graph.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Build a pure Agent Skill first | The draft explicitly says not to build a separate app first; the skill is the smallest useful artifact. | ✓ Good — shipped zero-dependency package validated by UAT + audit (v1.0) |
| Make the examined proposition the core artifact | The design principle says the examined proposition is the atomic unit of the product. | ✓ Good — session schema + summary template center on the examined proposition (v1.0) |
| Treat inferred beliefs as hypotheses requiring user confirmation | This prevents overinterpretation and preserves user ownership. | ✓ Good — binding select/reject/revise gate in SKILL.md; overinterpretation fixture demonstrates it (v1.0) |
| Put safety boundaries in the initial package | The skill handles emotionally charged material and must know when to stop philosophical probing. | ✓ Good — 5 hard-stop conditions + no-auto-resume gate; safety-boundary fixture passes (v1.0) |
| Defer local harness and belief graph work | These are valuable later milestones but would distract from validating the core skill behavior. | ✓ Good — kept v1 skill-only; carried forward cleanly as v2 HAR/GRPH scope |
| Stdlib-only validators (no third-party deps) | Keeps the package portable and sandbox-safe across runtimes. | ✓ Good — both checks run with `python3` alone; confirmed by audit mechanical re-verification (v1.0) |
| Thread one worked example ("recognition determines worth") across all phases | Cross-file coherence spine; gives reviewers a single traceable thread. | ✓ Good — present in all 11 expected files; integration check PASS (v1.0) |
| Rubric stays a 7-tuple profile with no roll-up score | A single-axis failure must not be averaged away. | ✓ Good — codified in EVALUATION_RUBRIC.md; designed for a v2 LLM-judge to reuse (v1.0) |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? -> Move to Out of Scope with reason
2. Requirements validated? -> Move to Validated with phase reference
3. New requirements emerged? -> Add to Active
4. Decisions to log? -> Add to Key Decisions
5. "What This Is" still accurate? -> Update if drifted

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check - still the right priority?
3. Audit Out of Scope - reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-06-26 after v1.0 milestone*
