# Phase 1: Core Skill Prototype - Context

**Gathered:** 2026-06-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Deliver a loadable `philosophical-midwifery` Agent Skill package — pure markdown, no code — consisting of four files that teach an agent the core inquiry loop and its method/safety boundaries:

- `philosophical-midwifery/SKILL.md`
- `philosophical-midwifery/references/QUESTION_TAXONOMY.md`
- `philosophical-midwifery/references/PATHOLOGOS_PATTERNS.md`
- `philosophical-midwifery/references/SAFETY_BOUNDARIES.md`

This phase covers SKL-01..05 and MTH-01..03. `SESSION_SCHEMA.md`, summary templates, belief-graph template, and the validator script are explicitly **Phase 2** and must NOT be pulled forward. No local harness, no web UI, no persistent belief graph in v1.

</domain>

<decisions>
## Implementation Decisions

### Package placement & frontmatter
- **D-01:** Skill package lives in a nested `philosophical-midwifery/` subdirectory at the repo root (matches the design-draft structure; keeps the distributable skill cleanly separated from `.planning/`, `docs/`, `AGENTS.md`).
- **D-02:** The `SKILL.md` frontmatter `description` is tightened to require an explicit inquiry/examination intent rather than the draft's broad emotional-trigger list. Activate on "wants to examine the beliefs behind a recurring disturbance," not on casual emotional mentions. Reduces false activations.
- **D-03:** `SKILL.md` includes an explicit "When NOT to use" / anti-trigger block naming therapy, crisis, medical, and diagnosis requests. This is in addition to (not instead of) the exit behavior in SAFETY_BOUNDARIES.md.
- **D-04:** `SKILL.md` references the three companion files by name with on-demand read guidance (e.g., "consult `references/QUESTION_TAXONOMY.md` when selecting your next question"). The agent loads references only when the situation calls for them — not all up-front.

### Pathologos pattern inventory
- **D-05:** `PATHOLOGOS_PATTERNS.md` opens by defining the coined working term "pathologos" (the belief beneath the suffering — the generalized proposition operating under a disturbance), then catalogs named archetypes.
- **D-06:** The v1 catalog contains four archetypes: **Conditional worth**, **Control & responsibility**, **Belonging & rejection**, **Perfection & flawlessness**. More can be added in later phases.
- **D-07:** Each archetype entry is rich: name + core generalized proposition + 2-3 concrete phrasings a user might say + typical affective charge + the distortion/leverage point to examine. (No per-archetype counter-question — that belongs to the taxonomy.)
- **D-08:** The file leads with a binding **presentation protocol**: candidates are always offered as hypotheses ("these might be operating — treat as guesses"), never asserted; the user always selects, rejects, or revises before any examination. This operationalizes the locked PROJECT.md decision that inferred beliefs require user confirmation.

### Reference voice
- **D-09:** Both `QUESTION_TAXONOMY.md` and `SAFETY_BOUNDARIES.md` are written as **agent directives** — second-person imperative ("When the user uses a vague term, ask for a definition before testing it."), not neutral third-person reference.
- **D-10:** Directive force is split by stakes: **SAFETY_BOUNDARIES.md** uses hard modals (MUST stop, NEVER continue); **QUESTION_TAXONOMY.md** uses soft guidance (prefer, try, consider) so the agent keeps flexibility in live dialogue.
- **D-11:** `QUESTION_TAXONOMY.md` gives each of the 8 operations a **"when to use" trigger** (what state of the proposition signals this move), not just a definition + examples. Teaches selection, not only the inventory.
- **D-12:** Each reference includes 1-2 short worked dialogue snippets (2-3 turns) anchored on the shared "recognition determines worth" example from the design draft. One shared example across files keeps them consistent.

### Safety detection granularity
- **D-13:** Each of the 5 stop conditions (self-harm intent, intent to harm others, acute crisis, psychosis-like reality-testing loss, diagnosis request) gets **concrete signal phrases** plus a clear/listen distinction (what is exploratory vs what is a red flag). Avoids both missed detection and over-triggering.
- **D-14:** Crisis resources are a **curated small set** of well-known/international-friendly resources (e.g., 988 for US, guidance to find a local line, emergency-services reminder) with an explicit instruction that the agent asks for the user's locale if unknown. No region-indexed list.
- **D-15:** **Resume gate** is explicit user re-entry: after a stop, the agent MUST NOT auto-resume; it states the boundary, offers resources, and returns to philosophical inquiry only if the user explicitly asks to continue AND the acute signal has clearly passed.
- **D-16:** `SAFETY_BOUNDARIES.md` covers **hard stop conditions only**. The "slow down when emotional intensity is high" modulation rule lives in `SKILL.md`'s dialogue rules (where the draft already has it). Clean separation: safety file = stops; skill file = modulation.

### the agent's Discretion
- Exact wording of frontmatter description (must satisfy D-02 intent).
- Exact signal-phrase lists under D-13 (must be concrete and clinically reasonable).
- Section ordering within each reference file, as long as the binding elements above are present.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Design & scope
- `docs/design-draft.md` — the primary design reference. Contains the SKILL.md draft (§6), session phases (§7), question taxonomy with examples (§10), safety boundaries (§11), state schema (§9, but note schema is Phase 2), and the evaluation rubric (§13, Phase 3). The "recognition determines worth" example threaded throughout is the shared worked example for this phase (D-12).
- `.planning/REQUIREMENTS.md` — requirement definitions SKL-01..05, MTH-01..03 are in Phase 1 scope; MTH-04, ART-01..03 are explicitly Phase 2; EVAL-01..03 are Phase 3.
- `.planning/ROADMAP.md` §"Phase 1: Core Skill Prototype" — phase goal, requirements list, and the 5 success criteria that verify this phase.
- `.planning/PROJECT.md` — "Key Decisions" table (pure skill first, examined proposition as atomic unit, beliefs as hypotheses, safety in initial package, defer harness/graph) and "Constraints" (runtime shape, safety, dialogue style, epistemic humility, method boundary, scope). These are locked and must not be re-litigated.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- None. Greenfield skill-authoring project — no source code exists. This phase produces the first authored artifacts.

### Established Patterns
- Agent Skill package convention: `SKILL.md` with YAML frontmatter (`name`, `description`) at the package root, companion references under `references/`. The nested-subdir placement (D-01) follows the structure in `docs/design-draft.md` §5.

### Integration Points
- The skill package is loaded by any compatible coding/chat agent via its `SKILL.md` frontmatter. No code integration points in this phase.

</code_context>

<specifics>
## Specific Ideas

- The "recognition determines worth" example from the design draft is the **single shared worked example** across SKILL.md and all three references (D-12). Using one consistent example makes the cross-references coherent and lightens the authoring load.
- "Pathologos" is a coined working term and must be defined in-place in `PATHOLOGOS_PATTERNS.md` (D-05) — do not assume the reader/agent knows it.
- The 8 taxonomy operations in `docs/design-draft.md` §10 (clarify, universalize, implication, counterexample, necessity/sufficiency, domain separation, contradiction test, reformulation) are the required set for MTH-01; each needs a "when to use" trigger per D-11.

</specifics>

<deferred>
## Deferred Ideas

- Additional pathologos archetypes beyond the v1 four (e.g., certainty/safety, justice/resentment, identity-fixed, emotional-truth) — future phase, once the v1 catalog is validated.
- Per-archetype counter-questions inside PATHOLOGOS_PATTERNS.md — deferred to avoid overlap with QUESTION_TAXONOMY.md; revisit if candidate-belief generation proves weak without them.
- Session-state tracking / inline session memory in v1 — belongs to Phase 2 (SESSION_SCHEMA.md).
- Region-indexed crisis resource list — deferred; v1 uses the curated set + locale ask (D-14).

</deferred>

---

*Phase: 1-Core Skill Prototype*
*Context gathered: 2026-06-23*
