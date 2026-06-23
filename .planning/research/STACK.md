# Project Research: Stack

## Recommendation

Build v1 as a filesystem-backed Codex Agent Skill package, not an app.

## Standard Stack

- **Skill manifest**: `SKILL.md` with YAML front matter and explicit usage instructions.
- **Reference docs**: Markdown files in `references/` for reusable method guidance.
- **Assets**: Markdown and JSON templates in `assets/` for session outputs and optional structured artifacts.
- **Validation**: Python script in `scripts/validate_session_schema.py` using the standard library where possible.
- **Tests**: Lightweight fixture-based tests for schema validation and package completeness.

## Why This Stack

- The draft's MVP is a pure Agent Skill, so static Markdown plus a small validator is enough.
- Keeping references separate prevents `SKILL.md` from becoming a long essay while still giving the agent precise material to load.
- A schema validator gives quick feedback without requiring an application runtime.

## What Not To Use For v1

- Do not build a frontend chat UI first; it delays validation of the core dialogue behavior.
- Do not introduce a database in v1; persistent belief graphs are a later milestone.
- Do not use a therapy, coaching, or diagnostic framework as the main organizing abstraction.

## Confidence

High. This matches the design draft and the existing Codex skill ecosystem visible in this workspace.
