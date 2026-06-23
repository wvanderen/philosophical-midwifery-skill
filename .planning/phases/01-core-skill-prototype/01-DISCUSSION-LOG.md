# Phase 1: Core Skill Prototype - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-23
**Phase:** 1-Core Skill Prototype
**Areas discussed:** Package placement & frontmatter, Pathologos pattern inventory, Reference voice, Safety detection granularity

---

## Package placement & frontmatter

### Q1 — Where does the skill package live in the repo?

| Option | Description | Selected |
|--------|-------------|----------|
| Root = package | SKILL.md at repo root | |
| Nested subdir | philosophical-midwifery/ subdirectory at repo root | ✓ |
| skills/ dir | skills/philosophical-midwifery/ convention | |

**User's choice:** Nested subdir
**Notes:** Matches design-draft structure; separates distributable skill from .planning/, docs/, AGENTS.md.

### Q2 — How should the frontmatter `description` be tuned?

| Option | Description | Selected |
|--------|-------------|----------|
| Keep draft verbatim | Broad emotional trigger list | |
| Tighten to inquiry-intent | Require explicit examination intent | ✓ |
| Two-tier triggers | Primary explicit + secondary disturbance-and-understand | |

**User's choice:** Tighten to inquiry-intent
**Notes:** Reduces false activations on casual emotional mentions.

### Q3 — Should SKILL.md include explicit anti-triggers?

| Option | Description | Selected |
|--------|-------------|----------|
| Yes, add anti-triggers | "When NOT to use" block for therapy/crisis/medical/diagnosis | ✓ |
| No, safety file handles it | Rely on SAFETY_BOUNDARIES.md alone | |

**User's choice:** Yes, add anti-triggers
**Notes:** Prevents the skill activating then aborting on clinical-adjacent requests.

### Q4 — How should SKILL.md point to the 3 companion references?

| Option | Description | Selected |
|--------|-------------|----------|
| Named + on-demand | Name each + the situation that calls for it | ✓ |
| Load all up-front | Read all three at session start | |
| Inline essentials | Inline rules, keep references as backups | |

**User's choice:** Named + on-demand
**Notes:** Lightweight; agent loads only what each situation needs.

---

## Pathologos pattern inventory

### Q1 — How should PATHOLOGOS_PATTERNS.md be conceptually framed?

| Option | Description | Selected |
|--------|-------------|----------|
| Define + named archetypes | Coin "pathologos" up-front, catalog archetypes | ✓ |
| Plain "hidden beliefs" list | Skip coining; plain themed list | |
| Organize by emotion | Frame around affective disturbance | |

**User's choice:** Define + named archetypes
**Notes:** Gives the agent a stable vocabulary to name what it sees.

### Q2 — Which archetypes should the v1 catalog include?

| Option | Description | Selected |
|--------|-------------|----------|
| Conditional worth | Worth depends on external gauge (recognition/success) | ✓ |
| Control & responsibility | Must control outcomes; responsible for others' states | ✓ |
| Belonging & rejection | Rejected/unseen = I cease to matter | ✓ |
| Perfection & flawlessness | Any flaw = total failure | ✓ |

**User's choice:** All four (multiSelect)
**Notes:** Starter set; more can be added in later phases.

### Q3 — How should each archetype entry be structured?

| Option | Description | Selected |
|--------|-------------|----------|
| Rich entries | name + proposition + phrasings + charge + leverage | ✓ |
| Minimal entries | name + belief + 1-2 examples | |
| Rich + counter-question | Rich + most useful destabilizing move | |

**User's choice:** Rich entries
**Notes:** Counter-question deferred to avoid overlap with taxonomy.

### Q4 — How to reinforce the "candidates are hypotheses" rule?

| Option | Description | Selected |
|--------|-------------|----------|
| Lead with protocol | Binding presentation protocol stated once | ✓ |
| Per-entry reminders | Footnote on every archetype | |
| Rule in SKILL.md only | Catalog is pure reference | |

**User's choice:** Lead with protocol
**Notes:** Operationalizes the locked PROJECT.md decision cleanly.

---

## Reference voice

### Q1 — What voice should the references use?

| Option | Description | Selected |
|--------|-------------|----------|
| Agent directives | Second-person imperative to the agent | ✓ |
| Human reference | Neutral third-person explanation | |
| Hybrid | Both definition + directive per entry | |

**User's choice:** Agent directives

### Q2 — How strong should the directives be?

| Option | Description | Selected |
|--------|-------------|----------|
| Split by stakes | Safety hard MUST/NEVER; Taxonomy soft prefer/try | ✓ |
| Hard throughout | MUST/NEVER in both | |
| Soft throughout | prefer/try in both | |

**User's choice:** Split by stakes
**Notes:** Matches stakes of each domain.

### Q3 — How should the taxonomy help the agent SELECT the next question?

| Option | Description | Selected |
|--------|-------------|----------|
| Add "when to use" triggers | Signal per operation that calls for it | ✓ |
| Progression arc | Loose clarify→test→synthesize arc | |
| Flat catalog | operation + examples only | |

**User's choice:** Add "when to use" triggers
**Notes:** Teaches WHEN, not just WHAT.

### Q4 — Should the references include worked examples?

| Option | Description | Selected |
|--------|-------------|----------|
| Worked snippets, shared example | 1-2 mini-dialogues on "recognition determines worth" | ✓ |
| Example questions only | Standalone questions, no dialogues | |
| Examples only in SKILL.md | One end-to-end example in SKILL.md | |

**User's choice:** Worked snippets, shared example
**Notes:** One shared example keeps files consistent.

---

## Safety detection granularity

### Q1 — How concrete should stop-condition detection be?

| Option | Description | Selected |
|--------|-------------|----------|
| Concrete signals per condition | Signal phrases + clear/listen distinction per stop | ✓ |
| Principle-level only | 5 conditions, one-line each | |
| Principles + doubt clause | Principles + "when in doubt, pause" | |

**User's choice:** Concrete signals per condition
**Notes:** Avoids both missed detection and over-triggering.

### Q2 — How should crisis resources be handled?

| Option | Description | Selected |
|--------|-------------|----------|
| Curated set + locale ask | Small international-friendly set, ask locale if unknown | ✓ |
| Generic "local help" only | Direct to local emergency/line, no numbers | |
| Region-indexed list | Full region→resource map | |

**User's choice:** Curated set + locale ask
**Notes:** Avoids stale-number maintenance burden of a region list.

### Q3 — What is the resume gate after a safety stop?

| Option | Description | Selected |
|--------|-------------|----------|
| Explicit user re-entry | No auto-resume; user must ask + acute signal passed | ✓ |
| No resume in-session | Session ends; user starts fresh | |
| Resume when topic moves on | Agent judges conversation has moved past | |

**User's choice:** Explicit user re-entry
**Notes:** Conservative; errs toward safety.

### Q4 — Where does the "slow down when emotion is high" rule live?

| Option | Description | Selected |
|--------|-------------|----------|
| Safety file = stops only | Modulation rule lives in SKILL.md dialogue rules | ✓ |
| Safety file owns the spectrum | Both stops AND modulation in safety file | |

**User's choice:** Safety file = stops only
**Notes:** Clean separation; safety file is hard stops only.

---

## the agent's Discretion

- Exact wording of frontmatter description (must satisfy D-02 intent).
- Exact signal-phrase lists under D-13.
- Section ordering within each reference file (binding elements must be present).

## Deferred Ideas

- Additional pathologos archetypes (certainty/safety, justice/resentment, identity-fixed, emotional-truth) — future phase.
- Per-archetype counter-questions inside PATHOLOGOS_PATTERNS.md — revisit if candidate generation proves weak.
- Session-state tracking / inline session memory — Phase 2 (SESSION_SCHEMA.md).
- Region-indexed crisis resource list — deferred; v1 uses curated set + locale ask.
