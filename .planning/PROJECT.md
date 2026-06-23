# Philosophical Midwifery

## What This Is

Philosophical Midwifery is an Agent Skill that helps an AI agent conduct structured philosophical midwifery-style inquiry. It guides a user from a felt disturbance to a hidden belief, then to an explicit proposition that can be examined for coherence through disciplined Socratic questioning.

The project is not a therapy, coaching, advice, or reassurance system. It is a skill package for structured philosophical self-examination, with safety boundaries and session artifacts that keep the inquiry careful, non-coercive, and grounded in the user's own confirmations.

## Core Value

The skill must reliably help an agent isolate and examine a user-confirmed proposition without drifting into therapy, advice, reassurance, or essay-writing.

## Requirements

### Validated

(None yet - ship to validate)

### Active

- [ ] Provide a `SKILL.md` that teaches the core inquiry loop: disturbance -> hidden belief -> explicit proposition -> examination -> contradiction/revision -> session summary.
- [ ] Provide a question taxonomy reference covering clarification, universalization, implication, counterexample, necessity/sufficiency, domain separation, contradiction testing, and reformulation.
- [ ] Provide a session schema that tracks the presenting disturbance, concrete example, candidate beliefs, selected belief, normalized proposition, definitions, implications, counterexamples, contradictions, revised proposition, unresolved tensions, next questions, and summary.
- [ ] Provide safety boundaries that stop normal philosophical inquiry for self-harm intent, intent to harm others, acute crisis, psychosis-like loss of reality testing, or requests for medical/psychiatric diagnosis.
- [ ] Provide a session summary template that captures the inquiry artifact without overclaiming certainty.
- [ ] Provide validation support for the session schema so generated artifacts can be checked mechanically.
- [ ] Preserve the dialogue discipline: one substantive question at a time, candidate beliefs offered as hypotheses, user ownership of belief selection, and no premature reassurance or advice.

### Out of Scope

- Mental health treatment or diagnosis - the skill is for philosophical inquiry, not clinical care.
- Crisis counseling - crisis language should trigger boundary handling and human support resources, not continued inquiry.
- Generic self-help advice or coaching - the product value is examination, not guidance or encouragement.
- CBT-style reframing as the main output - contradiction and revision may occur, but the method should remain philosophical and dialectical.
- A standalone chat app in v1 - the first milestone is a pure Agent Skill package.
- Persistent belief graph or recurring pathologos detection in v1 - these belong after the skill-only prototype and local harness exist.

## Context

The design draft defines the working name as `philosophical-midwifery` and proposes a package structure:

```text
philosophical-midwifery/
  SKILL.md
  references/
    QUESTION_TAXONOMY.md
    PATHOLOGOS_PATTERNS.md
    SESSION_SCHEMA.md
    SAFETY_BOUNDARIES.md
  assets/
    session_summary_template.md
    belief_graph_template.json
  scripts/
    validate_session_schema.py
```

The primary use case begins when a user brings a felt disturbance, blockage, recurring emotional pattern, resentment, fear, shame, or confusion. The skill should help the agent clarify one concrete situation, infer candidate hidden beliefs without certainty, ask the user to select or revise a candidate, normalize the chosen belief into a testable proposition, and examine it with Socratic question operations.

The draft's key example is resentment when work goes unrecognized. The skill should move from the concrete instance to candidate beliefs such as "Recognition determines worth" or "Being overlooked means being diminished," then test terms, implications, counterexamples, and contradictions until a revised proposition or unresolved tension is available.

The later product architecture in the draft includes a frontend chat UI, orchestrator, belief extractor, proposition normalizer, Socratic planner, safety classifier, session state store, belief graph store, summary generator, and database. This remains useful context, but the MVP intentionally starts with a portable skill rather than a separate app.

Evaluation should score sessions on proposition clarity, user ownership, dialectical discipline, logical pressure, non-coercion, summary quality, and practical usefulness. The atomic unit of the product is the examined proposition, not the chat message.

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
| Build a pure Agent Skill first | The draft explicitly says not to build a separate app first; the skill is the smallest useful artifact. | - Pending |
| Make the examined proposition the core artifact | The design principle says the examined proposition is the atomic unit of the product. | - Pending |
| Treat inferred beliefs as hypotheses requiring user confirmation | This prevents overinterpretation and preserves user ownership. | - Pending |
| Put safety boundaries in the initial package | The skill handles emotionally charged material and must know when to stop philosophical probing. | - Pending |
| Defer local harness and belief graph work | These are valuable later milestones but would distract from validating the core skill behavior. | - Pending |

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
*Last updated: 2026-06-23 after initialization*
