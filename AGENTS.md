# AGENTS.md

## Project

This repository contains the `philosophical-midwifery` Agent Skill project.

Read these planning files before making project changes:

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`

## Core Value

The skill must reliably help an agent isolate and examine a user-confirmed proposition without drifting into therapy, advice, reassurance, or essay-writing.

## Current Focus

Phase 1: Core Skill Prototype.

Create the usable Agent Skill and core method/safety references:

- `SKILL.md`
- `references/QUESTION_TAXONOMY.md`
- `references/PATHOLOGOS_PATTERNS.md`
- `references/SAFETY_BOUNDARIES.md`

## GSD Workflow

- Use `$gsd-discuss-phase 1` to gather phase context.
- Use `$gsd-plan-phase 1` to create the executable plan.
- Keep planning documents committed as atomic checkpoints.
- Do not skip verification for behavior that affects safety boundaries or dialogue rules.

## Implementation Principles

- Keep v1 as a pure Agent Skill package.
- Preserve user ownership of candidate beliefs and examined propositions.
- Present hidden beliefs as hypotheses, never certainties.
- Ask one substantive question at a time in the skill guidance.
- Stop philosophical inquiry when safety boundaries are crossed.
- Defer local harness, web UI, and persistent belief graph work until later phases.
