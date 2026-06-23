# Project Research: Architecture

## V1 Architecture

```text
User
  -> Agent with philosophical-midwifery skill loaded
  -> SKILL.md dialogue policy
  -> references/ method guidance
  -> optional structured session state
  -> session summary artifact
```

## Package Boundaries

- `SKILL.md`: Defines trigger conditions, role boundaries, core loop, and required behavior.
- `references/QUESTION_TAXONOMY.md`: Defines question operations with examples.
- `references/PATHOLOGOS_PATTERNS.md`: Defines common hidden-belief shapes as hypotheses.
- `references/SESSION_SCHEMA.md`: Defines the session state fields and JSON shape.
- `references/SAFETY_BOUNDARIES.md`: Defines when to stop inquiry and how to respond.
- `assets/session_summary_template.md`: Provides the final session artifact structure.
- `assets/belief_graph_template.json`: Seeds later graph work without making it a v1 runtime requirement.
- `scripts/validate_session_schema.py`: Validates session JSON against required fields and allowed values.

## Build Order Implications

1. Establish the package skeleton and core `SKILL.md`.
2. Add references and assets that the skill points to.
3. Add validation and fixtures so schema quality is testable.
4. Run manual transcript evaluations against the rubric and tighten prompts.

## Later Architecture

The draft's later app architecture can be revisited after the skill-only prototype works. A local harness should come before a full web application because it can test state, transcript export, and summary generation with less product surface area.
