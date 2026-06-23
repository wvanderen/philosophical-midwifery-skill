# Project Research: Pitfalls

## Pitfall: Therapy Drift

- **Warning signs**: The agent reassures, diagnoses, validates emotions as the main activity, or gives coping advice.
- **Prevention**: Put non-goals and stop conditions in `SKILL.md` and `SAFETY_BOUNDARIES.md`.
- **Phase**: Phase 1.

## Pitfall: Overinterpretation

- **Warning signs**: The agent says "you believe..." instead of offering candidate beliefs as hypotheses.
- **Prevention**: Require candidate-belief language and user selection/revision before examination.
- **Phase**: Phase 1.

## Pitfall: Essay Mode

- **Warning signs**: The agent explains philosophy instead of asking a next question.
- **Prevention**: Include strict dialogue rules and transcript-level evaluation criteria.
- **Phase**: Phase 1 and Phase 3.

## Pitfall: Schema Without Behavior

- **Warning signs**: The package validates JSON but the dialogue does not actually isolate a proposition.
- **Prevention**: Pair schema validation with manual conversation fixtures and rubric scoring.
- **Phase**: Phase 3.

## Pitfall: Safety Boundary Ambiguity

- **Warning signs**: The agent continues Socratic probing after self-harm, harm-to-others, acute crisis, or diagnosis requests.
- **Prevention**: Make boundary triggers explicit and test them with fixture prompts.
- **Phase**: Phase 1 and Phase 3.
