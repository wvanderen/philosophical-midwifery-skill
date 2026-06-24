# Phase 1: Core Skill Prototype - Research

**Researched:** 2026-06-23
**Domain:** Agent Skill authoring (pure markdown) — Socratic inquiry, cognitive-distortion/REBT belief modeling, and crisis-safety phrasing conventions
**Confidence:** HIGH (skill-packaging conventions verified against two authoritative sources; source-framework mappings verified against Wikipedia-grounded Burns/REBT/Paul-Elder and 988/findahelpline)

<user_constraints>
## User Constraints (from CONTEXT.md)

> Copied verbatim from `.planning/phases/01-core-skill-prototype/01-CONTEXT.md`. These decisions are LOCKED. Research grounds the prose quality of the four deliverables; it does NOT re-litigate D-01..D-16.

### Locked Decisions

**Package placement & frontmatter**
- **D-01:** Skill package lives in a nested `philosophical-midwifery/` subdirectory at the repo root.
- **D-02:** The `SKILL.md` frontmatter `description` is tightened to require an explicit inquiry/examination intent rather than the draft's broad emotional-trigger list. Activate on "wants to examine the beliefs behind a recurring disturbance," not on casual emotional mentions.
- **D-03:** `SKILL.md` includes an explicit "When NOT to use" / anti-trigger block naming therapy, crisis, medical, and diagnosis requests.
- **D-04:** `SKILL.md` references the three companion files by name with on-demand read guidance. The agent loads references only when the situation calls for them — not all up-front.

**Pathologos pattern inventory**
- **D-05:** `PATHOLOGOS_PATTERNS.md` opens by defining the coined working term "pathologos" (the belief beneath the suffering — the generalized proposition operating under a disturbance), then catalogs named archetypes.
- **D-06:** The v1 catalog contains four archetypes: **Conditional worth**, **Control & responsibility**, **Belonging & rejection**, **Perfection & flawlessness**.
- **D-07:** Each archetype entry is rich: name + core generalized proposition + 2-3 concrete phrasings + typical affective charge + the distortion/leverage point to examine.
- **D-08:** The file leads with a binding **presentation protocol**: candidates are always offered as hypotheses, never asserted; the user always selects, rejects, or revises before any examination.

**Reference voice**
- **D-09:** Both `QUESTION_TAXONOMY.md` and `SAFETY_BOUNDARIES.md` are written as **agent directives** — second-person imperative.
- **D-10:** Directive force is split by stakes: **SAFETY_BOUNDARIES.md** uses hard modals (MUST stop, NEVER continue); **QUESTION_TAXONOMY.md** uses soft guidance (prefer, try, consider).
- **D-11:** `QUESTION_TAXONOMY.md` gives each of the 8 operations a **"when to use" trigger**, not just a definition + examples.
- **D-12:** Each reference includes 1-2 short worked dialogue snippets (2-3 turns) anchored on the shared "recognition determines worth" example.

**Safety detection granularity**
- **D-13:** Each of the 5 stop conditions gets **concrete signal phrases** plus a clear/listen distinction (exploratory vs red flag).
- **D-14:** Crisis resources are a **curated small set** (988 for US, guidance to find a local line, emergency-services reminder) with an explicit instruction that the agent asks for the user's locale if unknown. No region-indexed list.
- **D-15:** **Resume gate** is explicit user re-entry: after a stop, the agent MUST NOT auto-resume; it states the boundary, offers resources, and returns to philosophical inquiry only if the user explicitly asks to continue AND the acute signal has clearly passed.
- **D-16:** `SAFETY_BOUNDARIES.md` covers **hard stop conditions only**. The "slow down when emotional intensity is high" modulation rule lives in `SKILL.md`'s dialogue rules.

### the agent's Discretion
- Exact wording of frontmatter description (must satisfy D-02 intent).
- Exact signal-phrase lists under D-13 (must be concrete and clinically reasonable).
- Section ordering within each reference file, as long as the binding elements above are present.

### Deferred Ideas (OUT OF SCOPE)
- Additional pathologos archetypes beyond the v1 four — future phase.
- Per-archetype counter-questions inside PATHOLOGOS_PATTERNS.md — deferred to avoid overlap with QUESTION_TAXONOMY.md.
- Session-state tracking / inline session memory in v1 — Phase 2.
- Region-indexed crisis resource list — deferred; v1 uses the curated set + locale ask (D-14).
- `SESSION_SCHEMA.md`, summary templates, belief-graph template, and validator script — explicitly Phase 2.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| SKL-01 | User can load a `philosophical-midwifery` Agent Skill with YAML front matter that describes when to use it. | §Standard Stack + §Architecture Patterns + §Code Examples (frontmatter): verified `name`+`description` convention from both Anthropic Claude Code and opencode docs; D-02/D-03 tighten the description and add an anti-trigger block. |
| SKL-02 | Skill follows the loop: disturbance -> hidden belief -> explicit proposition -> examination -> contradiction/revision -> summary. | §Architecture Patterns (Pattern: Core inquiry loop); the loop is the §7 session phases of `docs/design-draft.md`, restated as standing instructions per the skill-content-lifecycle convention. |
| SKL-03 | Skill asks one substantive question at a time and prefers inquiry over assertion. | §Dialogue Discipline; grounded in Paul/Elder "disciplined, systematic" Socratic questioning and the "state what to do, not narrate" + standing-instruction skill convention. |
| SKL-04 | Skill presents candidate hidden beliefs as hypotheses, not conclusions. | §Pathologos Source Material + §Dialogue Discipline; REBT "beliefs offered for dispute/question, not asserted" + Beck "open position that respects internal logic." Encoded as the D-08 presentation protocol. |
| SKL-05 | Skill asks the user to select, reject, or revise a candidate belief before examining it. | Same as SKL-04; the D-08 selection gate is the operational form. |
| MTH-01 | Question taxonomy covers clarification, universalization, implication, counterexample, necessity/sufficiency, domain separation, contradiction testing, reformulation. | §Socratic Questioning Taxonomy; the 8 operations are mapped 1:1 to Paul/Elder's 6 categories + Beck's CBT-Socratic set, each with a D-11 "when to use" trigger. |
| MTH-02 | Pathologos pattern guidance that helps generate candidate beliefs without overclaiming certainty. | §Pathologos Source Material; the 4 archetypes (D-06) are each grounded by Burns cognitive distortions + Ellis REBT irrational beliefs, with the D-07 entry fields and D-08 hypothesis protocol. |
| MTH-03 | Safety boundaries that stop normal inquiry for self-harm intent, intent to harm others, acute crisis, psychosis-like loss of reality testing, or diagnosis requests. | §Safety Conventions; the 5 stop conditions (D-13) draw signal phrases from the 988 warning-signs list; D-14 resources from findahelpline.com/988; D-15 resume gate from standard AI-safety protocol. |
</phase_requirements>

## Project Constraints (from AGENTS.md)

All AGENTS.md directives are enforced as locked constraints. The planner must verify compliance:

- **Keep v1 as a pure Agent Skill package** — no code, no DB, no harness, no web UI in this phase. The four deliverables are pure markdown.
- **Preserve user ownership** of candidate beliefs and examined propositions (→ D-08, SKL-05).
- **Present hidden beliefs as hypotheses, never certainties** (→ D-08, SKL-04).
- **Ask one substantive question at a time** in the skill guidance (→ SKL-03, dialogue rules).
- **Stop philosophical inquiry when safety boundaries are crossed** (→ MTH-03, D-13/15/16).
- **Defer local harness, web UI, and persistent belief graph** to later phases.
- **Do not skip verification for behavior that affects safety boundaries or dialogue rules** — these are the highest-stakes prose in the phase.

## Summary

Phase 1 produces four pure-markdown artifacts that teach a compatible agent the philosophical-midwifery inquiry loop and its method/safety boundaries. There is **no code, no packages to install, no runtime, no database** — the entire phase is skill-authoring. The research risk is therefore *not* technical-stack risk but **prose-quality and convention-conformance risk**: will the authored skill reliably activate, load its references on demand, stay out of therapy/advice/essay mode, offer candidate beliefs as hypotheses, and stop cleanly on crisis signals?

The good news is that all sixteen locked decisions (D-01..D-16) align cleanly with established practice, and several are *natively supported* by the target runtimes — most importantly **D-04 (on-demand reference loading) is the default behavior of both Anthropic Agent Skills and opencode skills**: an agent sees only the `name`+`description` until it invokes the skill, then loads the full `SKILL.md`, and companion reference files are read only when `SKILL.md` names them and the situation calls for them [VERIFIED: docs.claude.com/en/docs/claude-code/skills; opencode.ai/docs/skills]. No special mechanism is required; the planner only needs `SKILL.md` to name each reference and say when to read it.

For the method content, the four pathologos archetypes (D-06) are each robustly grounded by two independent, well-established frameworks — Burns's "Ten Forms of Twisted Thinking" (CBT cognitive distortions) and Ellis's REBT irrational beliefs — which together supply the generalized propositions, concrete phrasings, affective charges, and the leverage points the D-07 entry schema requires [CITED: en.wikipedia.org/wiki/Cognitive_distortion (citing Burns 1980, *Feeling Good*); en.wikipedia.org/wiki/Rational_emotive_behavior_therapy]. The 8 taxonomy operations (MTH-01) map 1:1 onto Paul & Elder's six Socratic-questioning categories plus Beck's CBT-Socratic set [CITED: en.wikipedia.org/wiki/Socratic_questioning (citing Paul & Elder 2006, *The Thinker's Guide to the Art of Socratic Questioning*)]. For safety, the 988 Suicide & Crisis Lifeline warning-signs list and findahelpline.com's 175+ country routing service give authoritative, copyable signal phrasing and the curated resource set [VERIFIED: 988lifeline.org; findahelpline.com].

**Primary recommendation:** Author the four files against verified conventions — `name`+`description` frontmatter with the tightened inquiry-intent description and an explicit "when NOT to use" block (D-02/D-03); a concise standing-instruction `SKILL.md` that names the three references with on-demand load guidance (D-04); directive-voice references split by modal force (D-09/D-10); the 8 taxonomy operations each with a "when to use" trigger (D-11); the 4 archetypes each grounded by Burns+REBT distortion mappings (D-07); and the 5 stop conditions with 988-derived signal phrases, a clear/listen distinction, the findahelpline/988 curated set + locale ask, and an explicit no-auto-resume gate (D-13/14/15). Use the "recognition determines worth" example as the single shared worked example across all four files (D-12).

## Architectural Responsibility Map

This phase has one tier — the **Agent Skill package** — but the *responsibilities* that the four files must own map to distinct conceptual layers. Mapping them now prevents the planner from, e.g., putting crisis-stop logic in `QUESTION_TAXONOMY.md` or question-selection triggers in `SAFETY_BOUNDARIES.md`.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Skill activation / anti-trigger | `SKILL.md` frontmatter | — | Only the `description` is in context pre-invocation; it is the sole activation surface. (D-02/D-03) |
| Core inquiry loop orchestration | `SKILL.md` body | — | The loop (disturbance→belief→proposition→examination→revision→summary) is standing instruction that must persist across the session. (SKL-02) |
| Dialogue discipline (one question, hypotheses, no advice) | `SKILL.md` dialogue rules | `PATHOLOGOS_PATTERNS.md` presentation protocol | Rules belong with the loop; the hypothesis protocol is reinforced in the pathologos file. (SKL-03/04/05; D-08) |
| Emotional-intensity modulation (slow down) | `SKILL.md` dialogue rules | — | D-16 explicitly places this here, NOT in the safety file. |
| Question selection (which operation, when) | `QUESTION_TAXONOMY.md` | — | D-11 "when to use" triggers live here; soft modals (D-10). (MTH-01) |
| Candidate-belief generation vocabulary | `PATHOLOGOS_PATTERNS.md` | — | D-05/D-06/D-07 archetype inventory + D-08 hypothesis protocol. (MTH-02) |
| Crisis/diagnosis hard-stop + resource handoff | `SAFETY_BOUNDARIES.md` | — | Hard modals (D-10); the only file that stops inquiry. (MTH-03; D-13/14/15) |
| Package completeness / cross-reference integrity | `SKILL.md` (names all 3 references) | the 3 references | SKILL.md is the entrypoint; it must name and route to its companions. (Success Criterion 4) |

## Standard Stack

This is a **pure-markdown authoring phase**. There is no library/dependency stack to install. The "stack" is the **Agent Skill package convention** itself. The Package Legitimacy Audit and the Standard Stack table below therefore catalog *conventions*, not packages.

### Core (the skill package format)
| Artifact | Role | Why Standard |
|---------|------|--------------|
| `SKILL.md` (YAML frontmatter + markdown body) | Entrypoint; the only file an agent sees pre-invocation | Verified convention in both Anthropic Claude Code and opencode [VERIFIED]. `name`+`description` frontmatter is the activation surface. |
| `references/*.md` | On-demand loaded companion docs | Native progressive-disclosure pattern: "long reference material costs almost nothing until you need it" [VERIFIED: docs.claude.com]. |
| Nested-subdir placement (`philosophical-midwifery/SKILL.md`) | Distributable package unit | D-01; matches design-draft §5 and opencode's one-folder-per-skill discovery [VERIFIED: opencode.ai/docs/skills]. |

### Frontmatter fields (verified against both runtimes)
| Field | opencode | Anthropic Claude Code | Phase 1 use |
|-------|----------|----------------------|-------------|
| `name` | **required**; 1-64 chars; lowercase-alphanumeric + single hyphens; must match directory name (regex `^[a-z0-9]+(-[a-z0-9]+)*$`) | optional (defaults to dir name); display label only | `name: philosophical-midwifery` — **must match the `philosophical-midwifery/` dir** per opencode rule. |
| `description` | **required**; 1-1024 chars; "specific enough for the agent to choose correctly" | **recommended**; combined `description`+`when_to_use` truncated at **1,536 chars** in the skill listing; "put the key use case first" | Tightened per D-02 (inquiry intent, not emotional triggers) + explicit "when NOT to use" per D-03. |
| `license`, `compatibility`, `metadata` (opencode) / `when_to_use`, `allowed-tools`, etc. (Claude Code) | optional | optional | **Out of scope for v1** — keep frontmatter minimal (name + description only) for cross-runtime portability, unless the planner decides a `when_to_use` field aids activation. |

> [VERIFIED: opencode.ai/docs/skills (frontmatter, name validation, length rules); docs.claude.com/en/docs/claude-code/skills (frontmatter reference, 1,536-char cap, "put key use case first", skill-content lifecycle)]

### What is deliberately NOT in the stack (Phase-2/3)
- `SESSION_SCHEMA.md`, `assets/session_summary_template.md`, `assets/belief_graph_template.json`, `scripts/validate_session_schema.py` — all Phase 2 (D-deferred; REQUIREMENTS MTH-04/ART-01..03).
- Any code, runtime, CLI, web UI, or database — explicitly out of scope (PROJECT.md Constraints; AGENTS.md).

**Installation:** *None.* `npm install` / `pip install` / `cargo add` are all N/A. The deliverable is four markdown files written directly to disk.

**Package Legitimacy Audit:** *Not applicable.* This phase installs zero external packages. (No `package.json`, `requirements.txt`, or `Cargo.toml` changes are in scope.) Per the protocol, the audit is required "whenever this phase installs external packages" — it does not.

## Architecture Patterns

### System Architecture Diagram

The "system" is a dialogue loop driven by an agent that has loaded the skill. Data flow is conceptual (turns of conversation), not request/response:

```text
User turn (felt disturbance / concrete example)
   │
   ▼
┌─────────────────────────────────────────────────────────────┐
│  SKILL.md (always in context once invoked)                   │
│  ├── frontmatter description  ←  activation/anti-trigger     │
│  ├── core inquiry loop (6 stages)                            │
│  ├── dialogue rules (one question, hypotheses, modulate)     │
│  └── names + on-demand routes to references ─────────┐       │
└──────────────────────────────────────────────────────┼───────┘
        │ load when needed                              │
        ▼                                               ▼
┌──────────────────────────┐   ┌────────────────────────────────┐
│ QUESTION_TAXONOMY.md     │   │ PATHOLOGOS_PATTERNS.md          │
│ (8 ops, each w/ trigger) │   │ (define "pathologos"; 4         │
│  soft modals — SELECT    │   │  archetypes; hypothesis         │
│  next question           │   │  presentation protocol)         │
└──────────────────────────┘   └────────────────────────────────┘
        │  candidate belief (hypothesis) ── user confirms/edits
        ▼
   proposition examination ──► contradiction/revision
        │
        ▼  (if a stop condition fires at ANY stage)
┌─────────────────────────────────────────────────────────────┐
│  SAFETY_BOUNDARIES.md  ←  HARD stop; hard modals (MUST/NEVER) │
│  acknowledge → stop probing → offer resources → resume gate   │
└─────────────────────────────────────────────────────────────┘
```

A reader tracing the primary use case: a disturbance enters → SKILL.md's loop drives intake → PATHOLOGOS_PATTERNS.md supplies candidate-belief vocabulary (offered as hypotheses per D-08) → user confirms → QUESTION_TAXONOMY.md guides which question to ask next → if any of the 5 stop conditions fires, SAFETY_BOUNDARIES.md halts the loop and routes to resources.

### Recommended Project Structure
```text
philosophical-midwifery/
├── SKILL.md                              # entrypoint: frontmatter, loop, dialogue rules, ref routing
└── references/
    ├── QUESTION_TAXONOMY.md              # 8 ops + D-11 triggers; soft modals (D-10)
    ├── PATHOLOGOS_PATTERNS.md            # "pathologos" def + 4 archetypes + D-08 protocol
    └── SAFETY_BOUNDARIES.md              # 5 stop conditions; hard modals (D-10); resources; resume gate
```
(D-01 places the package at repo root as `philosophical-midwifery/`.)

### Pattern 1: Progressive Disclosure / On-Demand Reference Loading (D-04)
**What:** `SKILL.md` is concise standing instruction; the three references are loaded only when `SKILL.md` tells the agent to read them and the dialogue situation calls for it.
**When to use:** This is the *native* skill-loading model — the planner does not build anything; it only writes SKILL.md so that it names each reference and says when to load it.
**Why standard:** Both target runtimes load the full SKILL.md only on invocation and companion files only on explicit read [VERIFIED]. Claude Code guidance: "Reference supporting files from `SKILL.md` so Claude knows what each file contains and when to load it" and "Keep SKILL.md under 500 lines. Move detailed reference material to separate files."
**Example routing phrasing (for SKILL.md):**
```markdown
## Companion references (read on demand, not all at once)
- `references/QUESTION_TAXONOMY.md` — consult when selecting your next examination question.
- `references/PATHOLOGOS_PATTERNS.md` — consult when inferring candidate hidden beliefs.
- `references/SAFETY_BOUNDARIES.md` — consult (and obey) the moment any crisis/diagnosis signal appears; it overrides the inquiry loop.
```

### Pattern 2: Standing-Instruction Body (SKL-02/SKL-03)
**What:** SKILL.md's body is written as *standing instructions that apply throughout the session*, not one-time steps.
**Why standard:** Once invoked, "the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session. [The runtime] does not re-read the skill file on later turns, so write guidance that should apply throughout a task as standing instructions rather than one-time steps." [VERIFIED: docs.claude.com — skill content lifecycle]
**Implication:** Dialogue rules ("ask one substantive question at a time", "offer candidates as hypotheses") must be phrased as durable rules, not as a numbered startup checklist the agent runs once and abandons.

### Pattern 3: Description-as-Activation-Surface with Anti-Trigger (D-02/D-03, SKL-01)
**What:** The frontmatter `description` is the *only* text in context before invocation, so it must (a) state the activating intent precisely and (b) name what NOT to activate on.
**Why standard:** Claude Code: description is "What the skill does and when to use it... Put the key use case first" [VERIFIED]. Anti-trigger phrasing ("Use when X; do NOT use for therapy/crisis/diagnosis") is the established way to encode negation in the activation surface.
**Example (satisfies D-02 + D-03):**
```yaml
---
name: philosophical-midwifery
description: Use when the user wants to examine the beliefs behind a recurring disturbance, resentment, fear, shame, blockage, or confusion through disciplined Socratic inquiry. Do NOT use this skill to provide therapy, counseling, crisis response, medical/psychiatric advice, diagnosis, or generic reassurance — route those to appropriate human resources instead.
---
```

### Pattern 4: Modal-Force Split by Stakes (D-09/D-10)
**What:** SAFETY_BOUNDARIES.md uses hard modals (MUST / NEVER) because the cost of non-compliance is harm; QUESTION_TAXONOMY.md uses soft modals (prefer / try / consider) so the agent retains live-dialogue flexibility.
**Why standard:** Matches prompt-engineering practice for safety-critical vs. judgment-critical instructions [ASSUMED — general practice]; aligns with the CBT-Socratic principle of maintaining "an open position that respects the internal logic to even the most seemingly illogical thoughts" for the inquiry tier [CITED: en.wikipedia.org/wiki/Socratic_questioning (Beck)].

### Anti-Patterns to Avoid
- **Loading all references up-front** — defeats progressive disclosure; bloats context. Each reference loads on-demand only. (D-04)
- **Putting the slow-down-on-emotion rule in SAFETY_BOUNDARIES.md** — D-16 forbids this; safety file = stops only.
- **Putting per-archetype counter-questions in PATHOLOGOS_PATTERNS.md** — deferred (overlaps QUESTION_TAXONOMY.md).
- **A long essay-style SKILL.md** — Claude Code: keep under 500 lines, "every line is a recurring token cost. State what to do rather than narrate how or why."
- **Asserting candidate beliefs ("You believe X")** — violates D-08/SKL-04; must always be hypothesis-framed.
- **Auto-resuming inquiry after a crisis stop** — violates D-15.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| The 8 Socratic operations and their selection triggers (MTH-01, D-11) | A bespoke question typology invented from scratch | Paul & Elder's 6 Socratic-questioning categories + Beck's CBT-Socratic set, mapped to the 8 required ops | Authoritative, decades-old framework; avoids reinventing a well-validated taxonomy [CITED]. |
| The 4 pathologos archetypes' content (D-07) | Inventing generalized propositions / phrasings / leverage points from intuition | Burns "Ten Forms of Twisted Thinking" + Ellis REBT irrational-belief inventory, mapped per-archetype | Two independent established frameworks that already name the propositions, distortions, and the logical leverage points [CITED]. |
| Crisis signal phrases (D-13) | Guessing what language signals self-harm / crisis | The 988 Suicide & Crisis Lifeline warning-signs list (verbatim phrasings) | Authoritative, clinically-grounded, copyable [VERIFIED: 988lifeline.org]. |
| The crisis resource set + locale logic (D-14) | A region-indexed directory | Curated set: 988 (US), findahelpline.com (global, 175+ countries), local emergency services; ask locale if unknown | findahelpline.com is the canonical routing service that powers major AI crisis responses [VERIFIED: findahelpline.com]. |
| Suicide-safer language | "Commit suicide" / clinical jargon | "Died by suicide", "suicide attempt", person-first phrasing | Established safer-language convention; 988 uses this framing [CITED]. |
| Skill activation/anti-trigger mechanism (D-02/D-03) | A custom routing/activation layer | Standard `name`+`description` frontmatter with intent + negation | Native to both target runtimes [VERIFIED]. |

**Key insight:** Every deceptively-hard content problem in this phase (question taxonomy, belief-archetype modeling, crisis-signal phrasing, resource routing) already has an authoritative source framework. The authoring work is *mapping and phrasing*, not invention. Inventing substitutes risks both lower quality and clinical-safety errors.

## Common Pitfalls

### Pitfall 1: Therapy / Advice / Reassurance Drift (Success Criterion 3)
**What goes wrong:** The agent validates emotions, offers coping advice, or reassures ("That sounds really hard; you're going to be okay") instead of asking the next examination question.
**Why it happens:** Models are RLHF-biased toward empathetic/helpful responses; without hard standing rules, the gravitational pull is toward support.
**How to avoid:** Make dialogue rules *standing instructions* (Pattern 2), phrase them as forbiddings ("Do NOT reassure, advise, diagnose, or validate emotions as the main activity"), and re-state the non-goals in SKILL.md. The 988 grounding also gives crisp stop-conditions that preempt the gray zone.
**Warning signs in prose:** any rule phrased as a one-time checklist rather than a durable rule; absence of an explicit non-goals block.

### Pitfall 2: Overinterpretation / Assertion of Beliefs (SKL-04/SKL-05)
**What goes wrong:** The agent says "You believe recognition determines your worth" instead of "One possible belief operating here might be... treat this as a guess."
**Why it happens:** Inferring a belief and stating it confidently is shorter and feels more decisive.
**How to avoid:** D-08 binding presentation protocol at the TOP of PATHOLOGOS_PATTERNS.md; require user select/reject/revise before examination (SKL-05). REBT models the correct stance: beliefs are offered for *dispute and question*, never asserted [CITED].
**Warning signs:** archetype entries that read as diagnoses rather than hypotheses; missing selection gate.

### Pitfall 3: Essay Mode (Success Criterion 3)
**What goes wrong:** The agent explains the philosophy of recognition-and-worth in three paragraphs instead of asking "What do you mean by recognition?"
**Why it happens:** Models default to comprehensive exposition.
**How to avoid:** Hard rule "Ask one substantive question at a time. Prefer questions over assertions. Do not produce philosophical essays." (design-draft §6 dialogue rules). Keep SKILL.md concise per Claude Code's under-500-lines guidance.
**Warning signs:** SKILL.md body longer than ~150 lines of prose; taxonomy examples that are paragraphs rather than one-line questions.

### Pitfall 4: Safety-Boundary Ambiguity / Over- or Under-Triggering (MTH-03, D-13)
**What goes wrong (under-trigger):** The agent continues Socratic probing after a self-harm signal. **(over-trigger):** The agent halts inquiry whenever any negative emotion appears, because the stop conditions are too vague.
**Why it happens:** Without concrete signal phrases AND a clear/listen distinction, the model can't tell exploratory mention from acute red flag.
**How to avoid:** D-13's concrete signal phrases (drawn verbatim-style from 988) + an explicit "exploratory vs red-flag" distinction per stop condition. Hard modals (MUST stop) remove ambiguity.
**Warning signs:** a stop condition described only by category name ("self-harm intent") with no example phrases; no clear/listen distinction.

### Pitfall 5: Auto-Resume After a Stop (D-15)
**What goes wrong:** After routing to resources, the agent cheerfully continues the inquiry loop on the next turn.
**Why it happens:** Standing instructions re-assert the loop; without an explicit gate, the loop wins.
**How to avoid:** D-15 explicit resume gate: MUST NOT auto-resume; only resume on explicit user request AND clear acute-signal resolution. State this in BOTH SAFETY_BOUNDARIES.md and SKILL.md's routing note.

### Pitfall 6: Description Too Broad → False Activation (D-02)
**What goes wrong:** The skill activates on any emotional mention ("I'm sad") because the description lists distress emotions as triggers.
**Why it happens:** The design-draft §6 description is a broad emotional-trigger list.
**How to avoid:** D-02 requires explicit inquiry/examination *intent* ("wants to examine the beliefs behind..."), not mere emotional mention. Anti-trigger block (D-03) adds the negation.

### Pitfall 7: Reference Cross-Reference Incoherence (Success Criterion 4)
**What goes wrong:** The four files use different examples, terms, or inconsistent safety phrasing, so cross-references break.
**How to avoid:** D-12's single shared worked example ("recognition determines worth") across all four files. The planner should enforce one canonical example-thread.

## Code Examples

Verified patterns / templates the planner can hand to the implementer. Sources cited inline.

### Example 1: SKILL.md frontmatter (satisfies SKL-01, D-02, D-03)
```yaml
---
name: philosophical-midwifery
description: Use when the user wants to examine the beliefs behind a recurring disturbance, resentment, fear, shame, blockage, or confusion through disciplined Socratic inquiry — moving from a concrete instance to a candidate hidden belief, then to an explicit proposition tested for coherence. Do NOT use for therapy, counseling, crisis response, medical/psychiatric advice, diagnosis, or reassurance.
---
```
*Source convention: [VERIFIED: docs.claude.com/en/docs/claude-code/skills (frontmatter reference, "put the key use case first"); opencode.ai/docs/skills]. Description tightened per D-02; anti-trigger per D-03. Kept well under the 1,536-char listing cap.*

### Example 2: SKILL.md standing-instruction dialogue rules (satisfies SKL-02/03/04/05)
```markdown
## Dialogue rules (apply throughout the session)
- Ask ONE substantive question at a time. Prefer questions over assertions.
- Offer candidate hidden beliefs only as hypotheses ("one possible belief might be…"). Never assert what the user believes.
- Before examining any candidate belief, ask the user to select, reject, or revise it.
- Do not reassure, advise, diagnose, validate emotions as the main activity, or write philosophical essays.
- Keep the inquiry anchored to the user-confirmed proposition.
- If emotional intensity is high, slow down and ground the inquiry before continuing.
- Make uncertainty explicit; treat the user as the authority on their own experience.

## Companion references (read on demand — do not load all at once)
- `references/PATHOLOGOS_PATTERNS.md` — consult when inferring candidate hidden beliefs. Obey its presentation protocol.
- `references/QUESTION_TAXONOMY.md` — consult when selecting your next examination question.
- `references/SAFETY_BOUNDARIES.md` — obey the moment any crisis or diagnosis signal appears. It overrides this loop.
```
*Source: design-draft §6 dialogue rules, restated as standing instructions per [VERIFIED: docs.claude.com — skill content lifecycle].*

### Example 3: QUESTION_TAXONOMY.md entry template (satisfies MTH-01, D-09, D-11, D-12)
```markdown
### Universalization
**What it does:** Test whether the claim applies generally, not just to the user.
**When to use it (trigger):** Use once the proposition is stated and its key terms are defined, and you want to expose whether the user is applying a rule to themselves that they would not apply to others.
**Soft guidance:** Prefer phrasing that asks the user to consider another person in the same situation.
**Example questions:**
- "Would this be true for everyone, or only for you?"
- "If someone else were overlooked, would that make them less valuable?"
**Worked snippet ("recognition determines worth"):**
> User: "If no one notices my work, it has no value."
> Agent: "If a colleague's excellent work went unnoticed, would that make it worthless? … Then what makes your own case different?"
```
*Source framework: [CITED: en.wikipedia.org/wiki/Socratic_questioning — Paul & Elder "alternative viewpoints and perspectives" + Beck CBT "distancing/double-standard"]. Soft modals per D-10; trigger per D-11; shared example per D-12.*

### Example 4: The 8 operations → source-framework mapping (MTH-01)
| Required operation | Grounding source | "When to use" trigger basis |
|--------------------|------------------|------------------------------|
| Clarification | Paul/Elder #1 (clarify thinking); Beck (evidence) | A vague/loaded term ("worth", "failure") needs defining before testing. |
| Universalization | Paul/Elder #4 (alternative viewpoints); Beck (distancing) | Proposition stated + defined; test self/other asymmetry. |
| Implication | Paul/Elder #5 (implications/consequences) | Ask what follows if the belief is true. |
| Counterexample | Paul/Elder #4 (viewpoints); Beck (alternatives) | Find a concrete case that weakens the proposition. |
| Necessity / sufficiency | Paul/Elder #3 (probe evidence/reasons) | Test logical dependency: is X *required*? is X *enough*? |
| Domain separation | Paul/Elder #1 (clarify/distinguish concepts) | User has fused two domains (visibility vs value; status vs worth). |
| Contradiction test | Paul/Elder #2 (challenge assumptions) + #3 (consistency) | User holds two commitments that can't both be true. |
| Reformulation | Paul/Elder #6 (meta); Beck (effect of thinking differently) | A contradiction/weakness surfaced; invite a more coherent version. |
*CITED: en.wikipedia.org/wiki/Socratic_questioning (Paul & Elder 2006; Beck 1995).*

### Example 5: PATHOLOGOS_PATTERNS.md — definition + presentation protocol (D-05, D-08, MTH-02)
```markdown
## What "pathologos" means here
A **pathologos** is the belief beneath the suffering — the generalized proposition operating
under a felt disturbance. It is a *hypothesis*, never a diagnosis.

## Presentation protocol (binding)
1. Offer candidates ONLY as hypotheses: "These might be operating — treat them as guesses."
2. Never assert what the user believes.
3. The user ALWAYS selects, rejects, or revises a candidate before any examination begins.
4. If none fit, say so and ask the user to restate the belief in their own words.
```
*Source: D-05 (coined-term definition) + D-08 (protocol). REBT models the "offered for dispute, not asserted" stance [CITED: REBT].*

### Example 6: One archetype entry (D-06, D-07) — "Conditional worth", grounded by Burns+REBT
```markdown
### Conditional worth
**Core generalized proposition:** "My worth as a person depends on [achievement / recognition / others' approval]."
**Concrete phrasings a user might say:**
- "If my work goes unrecognized, it has no value."
- "If I fail at this, I'm nothing."
- "Being overlooked means I don't matter."
**Typical affective charge:** shame, resentment, hollow even on success, dread of invisibility.
**Distortion / leverage point to examine (grounded):** global human-worth rating (REBT "depreciation") + all-or-nothing thinking + disqualifying the positive + "should" statements (Burns). Leverage operations: universalization, domain separation (separate *worth* from the *condition*), necessity/sufficiency.
```
*Source: [CITED: en.wikipedia.org/wiki/Cognitive_distortion (Burns); en.wikipedia.org/wiki/Rational_emotive_behavior_therapy (REBT "depreciation/global human-worth rating")].*

### Example 7: SAFETY_BOUNDARIES.md — one stop condition with clear/listen distinction (D-13, D-10)
```markdown
### Stop condition 1 — Self-harm / suicide intent
**You MUST stop philosophical inquiry and follow the response pattern below if the user expresses:**
- talking about wanting to die or to kill themselves;
- looking for a way to hurt themselves;
- feeling hopeless or having no reason to live;
- feeling trapped or in unbearable pain;
- feeling they are a burden to others.

**Clear vs listen (do not over-trigger):**
- EXPLORATORY (continue inquiry, stay attentive): a past reference to having been low; a conceptual question about suffering.
- RED FLAG (stop now): present-tense intent, a plan/means, hopelessness with finality language.

**Response pattern (hard — MUST):**
1. Acknowledge seriousness directly.
2. STOP all Socratic probing.
3. Offer resources (see Resources section); ask the user's locale if unknown.
4. Do NOT auto-resume. Resume only if the user explicitly asks AND the acute signal has clearly passed.
```
*Source: signal phrasings adapted from [VERIFIED: 988lifeline.org — Warning Signs]. Clear/listen distinction per D-13; hard modals per D-10; resume gate per D-15.*

### Example 8: Curated resources + locale ask (D-14)
```markdown
## Resources (curated small set — offer these, then ask locale)
- **United States:** 988 Suicide & Crisis Lifeline — call or text 988, or chat at chat.988lifeline.org.
- **Anywhere else / to find your local line:** findahelpline.com (verified helplines in 175+ countries).
- **Immediate danger:** contact your local emergency services (911 in the US, 112 in the EU, 999 in the UK).

If you do not know the user's country/region, ASK before giving a region-specific number.
```
*Source: [VERIFIED: 988lifeline.org; findahelpline.com]. findahelpline.com powers major AI-platform crisis responses.*

## Pathologos Source Material — the 4 archetypes grounded

Each archetype mapped to the two verified frameworks. Implementer can write entries directly from this table (D-07 fields filled). [CITED framework sources: Burns cognitive distortions; Ellis REBT irrational beliefs.]

| Archetype (D-06) | Core generalized proposition | Grounding: Burns distortions | Grounding: REBT irrational belief | Affective charge | Primary leverage operations |
|------------------|------------------------------|------------------------------|-----------------------------------|------------------|------------------------------|
| **Conditional worth** | "My worth depends on X (achievement / recognition / approval)." | all-or-nothing; labeling/mislabeling; disqualifying the positive; should-statements | **Depreciation** — global human-worth rating | shame; resentment; hollow success; dread of invisibility | universalization; domain separation (worth ≠ condition); necessity/sufficiency |
| **Control & responsibility** | "I must control / am responsible for X I cannot in fact control." | personalization & blaming; catastrophizing; fallacy of change; control fallacy | **Demands** (must/should) + **Awfulizing** + **Low Frustration Tolerance** | guilt; anxiety; rage; burnout; helplessness | domain separation (what is/isn't in one's control); necessity/sufficiency; counterexample |
| **Belonging & rejection** | "Rejection/exclusion means I am unworthy/unlovable." | mind reading; fortune-telling; overgeneralizing; emotional reasoning | **approval-MUST** ("others MUST treat me well / accept me") | hurt; jealousy; social anxiety; shame; withdrawal | counterexample; implication; domain separation (status ≠ worth) |
| **Perfection & flawlessness** | "I must be flawless; mistakes are catastrophic." | all-or-nothing; should-statements; mental filtering; catastrophizing | **performance-MUST** ("I MUST perform outstandingly and win approval") | anxiety; self-criticism; procrastination; shame on any error | necessity/sufficiency; counterexample; universalization (does this apply to others?); reformulation |

> Cross-cutting note: REBT is explicitly **Stoic-derived** (Ellis cites Epictetus: "Men are disturbed not by things, but by the views which they take of them") [CITED]. This makes REBT a *philosophically aligned* source for the midwifery method — the leverage points above are dialectical, not clinical, which keeps the skill out of therapy territory (PROJECT.md "Method boundary: logic, implication, contradiction, reformulation").

> Young Schema Therapy (defectiveness/shame, social isolation, unrelenting standards, approval-seeking/recognition-seeking, etc.) is **corroborating source material** for the affective-charge field but is NOT required to populate the four entries; Burns+REBT fully cover D-07. Schema-therapy specifics are tagged [ASSUMED] (schematherapy.com source could not be fetched this session) — see Assumptions Log.

## Safety Conventions — grounding for SAFETY_BOUNDARIES.md

| Element (decision) | Authoritative source | Key content for the implementer |
|--------------------|----------------------|---------------------------------|
| Signal phrases for self-harm / crisis (D-13) | [VERIFIED: 988lifeline.org/.../warning-signs] | 988's verbatim warning-signs list (see Example 7); flagged "especially if the behavior is new, has increased, or seems related to a painful event, loss, or change." |
| Intent-to-harm-others signal phrases (D-13) | [ASSUMED — derived by analogy to 988 self-harm list; no single authoritative list fetched] | present-tense intent + plan/target; mirror the self-harm clear/listen structure. **Flag for human review of exact phrasing** (planner discretion per CONTEXT.md). |
| Acute-crisis & psychosis-like reality-testing-loss signals (D-13) | [ASSUMED — no single authoritative source fetched this session] | disorientation, beliefs that external reality is unsafe/unreal in a way that impairs judgment; hallucination reports. **Flag for human review.** |
| Diagnosis-request stop (D-13) | PROJECT.md Out of Scope + REQUIREMENTS MTH-03 | "Do you think I have depression/BPD/…?" → stop, clarify the skill does not diagnose, route to a qualified professional. |
| Curated resources + locale ask (D-14) | [VERIFIED: 988lifeline.org; findahelpline.com] | 988 (US, call/text/chat); findahelpline.com (global, 175+ countries, powers major AI crisis responses); local emergency services (911/112/999). Ask locale if unknown. |
| Resume gate (D-15) | [ASSUMED — standard AI-safety protocol; no single canonical source fetched] | No auto-resume; explicit user re-entry + clear acute-signal resolution required. |
| Suicide-safer language | [CITED: 988lifeline.org usage — "died by suicide", "attempt", person-first] | Avoid "commit suicide"; use "died by suicide" / "suicide attempt"; person-first phrasing throughout. |
| Modulation rule (slow down on high emotion) | D-16 | Lives in **SKILL.md dialogue rules**, NOT in SAFETY_BOUNDARIES.md. |

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Agent Skills as Anthropic-only / Claude-Code-only | Open **Agent Skills standard** (agentskills.io) adopted across Claude Code, opencode, and others | 2025 | The skill is portable; `name`+`description` frontmatter works cross-runtime. Minimal frontmatter maximizes portability. [VERIFIED] |
| Crisis routing = hard-coded per-region phone lists | Curated small set + global routing service (findahelpline.com) + locale ask | ~2020s | D-14's curated-set approach is now the standard; a region-indexed list would be stale on arrival. [VERIFIED] |
| "Commit suicide" | "Died by suicide" / "suicide attempt" | ~2010s+ (media/journalism guidelines, 988 adoption) | Suicide-safer language is now expected in any crisis-adjacent content. [CITED] |
| CBT reframing as main output | Philosophical/dialectical examination (logic, implication, contradiction) | project decision (PROJECT.md) | The skill must NOT collapse into CBT-style reframing; REBT is a *source* for belief vocabulary, not the method. |

**Deprecated/outdated to avoid in v1 prose:**
- "Commit suicide" → use "died by suicide" / "attempt".
- Region-indexed phone directories → use findahelpline.com + locale ask.
- Treating pathologos archetypes as diagnoses → they are hypothesis-generators (D-08).
- `name` not matching the directory name → fails opencode validation [VERIFIED].

## Assumptions Log

Claims tagged `[ASSUMED]` that the planner/discuss-phase may want to confirm. CONTEXT.md marks the exact signal-phrase lists as agent-discretion, so the first three are explicitly the implementer's call — they are flagged here for human-verify checkpoints, not as blockers.

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Exact signal-phrase wording for "intent to harm others", "acute crisis", and "psychosis-like reality-testing loss" (no single authoritative list was fetched; derived by analogy to the verified 988 self-harm list) | Safety Conventions; D-13 | Phrasing could under-trigger (miss a real signal) or over-trigger. **Mitigation:** planner adds a `checkpoint:human-verify` review of SAFETY_BOUNDARIES.md prose before the phase is considered done (AGENTS.md already mandates verification for safety-boundary behavior). |
| A2 | The "resume gate" phrasing (no auto-resume; explicit user re-entry + acute-signal resolution) reflects standard AI-safety practice; no single canonical source fetched | Safety Conventions; D-15 | Low — D-15 itself locks the behavior; only the prose framing is assumed. |
| A3 | Young Schema Therapy schema names (defectiveness/shame, social isolation, unrelenting standards, approval-seeking) provide useful affective-charge vocabulary | Pathologos Source Material | Low — schema therapy is *corroborating* only; Burns+REBT (both verified) fully populate the four entries. The implementer may cite schema-therapy vocabulary but must not depend on it. |
| A4 | Hard-MUST vs soft-prefer modal split improves directive reliability (general prompt-engineering practice, not measured in-session) | Pattern 4 (D-09/D-10) | Low — D-10 locks the split regardless; the claim only justifies *why*. Real reliability is validated in Phase 3 (EVAL-02). |
| A5 | Minimal frontmatter (name + description only, no `when_to_use`/`allowed-tools`) maximizes cross-runtime portability | Standard Stack | Low — adding optional fields would not break anything; the recommendation is conservative. Planner may add a `when_to_use` field if it aids activation on a specific target runtime. |

## Open Questions

1. **Target runtime(s) for v1.** The skill is portable, but if a *primary* runtime is intended (Claude Code vs opencode), the planner may add runtime-specific optional frontmatter (e.g., Claude Code `when_to_use` for richer activation, or `disable-model-invocation` if inquiry should be user-invoked only).
   - What we know: both runtimes accept `name`+`description` and load references on-demand.
   - What's unclear: whether the user wants `/philosophical-midwifery` to be user-invocable, model-invocable, or both.
   - Recommendation: default to model-invocable (both user and agent can invoke) with minimal frontmatter; revisit if false-activation occurs in Phase 3 evals.

2. **Exact stop-condition signal phrasing (A1).** The three non-self-harm stop conditions (harm-to-others, acute crisis, reality-testing loss) have no single fetched authoritative phrase list.
   - Recommendation: planner adds a `checkpoint:human-verify` task reviewing SAFETY_BOUNDARIES.md prose; the implementer drafts from the structure in Example 7, and a human confirms the phrasing is neither under- nor over-triggering.

3. **Whether to include schema-therapy vocabulary.** It enriches the affective-charge field (D-07) but isn't required.
   - Recommendation: use Burns+REBT as primary citations; optionally cite schema-therapy schema names where they sharpen an entry, tagged as corroborating.

## Environment Availability

> This phase has **no external dependencies** — it produces four markdown files via a text editor / the agent's own Write tool. No compilers, runtimes, databases, package managers, or CLI tools are required. Per the protocol's skip condition, this section is included only to state that explicitly.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Text authoring (agent Write tool / editor) | all four deliverables | ✓ | — | — |
| Git | committing planning + skill docs (commit_docs: true) | ✓ | — | — |

**Missing dependencies with no fallback:** none.
**Missing dependencies with fallback:** none.

## Security Domain

> `security_enforcement` is not set in `.planning/config.json` → treated as enabled. This is a pure-markdown phase with no code, no input handling, no auth, no crypto. The "security surface" of this phase IS the **safety-boundary content** — the very thing MTH-03/D-13/D-14/D-15 deliver. The ASVS categories otherwise relevant to a runtime (V2 auth, V3 sessions, V4 access control, V6 crypto) do not apply to markdown authoring; the only applicable category is content-level.

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no | N/A — no code, no auth. |
| V3 Session Management | no | N/A — no runtime session (skill-content lifecycle is an agent-runtime concern, not this phase's). |
| V4 Access Control | no | N/A. |
| V5 Input Validation | no (in the code sense) | The analogue is **signal-phrase detection quality** in SAFETY_BOUNDARIES.md — validated by human review (A1) and Phase 3 fixtures (EVAL-02). |
| V6 Cryptography | no | N/A. |

### Known Threat Patterns for the skill content

| Pattern | STRIDE | Standard Mitigation (in-scope for this phase) |
|---------|--------|-----------------------------------------------|
| Therapy/advice/diagnosis drift | (behavioral, not STRIDE) | Standing dialogue rules + non-goals block + anti-trigger in description (Pitfalls 1, 6). |
| Over-assertion of beliefs (harms user agency) | Tampering (with user ownership) | D-08 hypothesis protocol + SKL-05 selection gate (Pitfall 2). |
| Missed crisis signal | (safety, high severity) | Concrete 988-grounded signal phrases + hard modals + human-verify checkpoint (Pitfall 4, A1). |
| Over-triggering (halts legitimate inquiry) | Denial of service (to the inquiry) | D-13 clear/listen distinction per stop condition (Pitfall 4). |
| Auto-resume after stop | (safety) | D-15 explicit resume gate (Pitfall 5). |

**Key security insight:** The single most important verification in this phase is human review of SAFETY_BOUNDARIES.md prose for neither under- nor over-triggering. AGENTS.md already mandates "Do not skip verification for behavior that affects safety boundaries." The planner should encode this as an explicit review checkpoint.

## Sources

### Primary (HIGH confidence)
- **docs.claude.com/en/docs/claude-code/skills** — Anthropic Agent Skills (Claude Code) canonical docs: frontmatter reference, `name`/`description`/`when_to_use`, 1,536-char listing cap, "put the key use case first", skill-content lifecycle (standing instructions), under-500-lines guidance, on-demand supporting-file loading, anti-trigger via `disable-model-invocation`. Also references the open **agentskills.io** standard.
- **opencode.ai/docs/skills** — opencode Agent Skills docs: `name` (required, regex `^[a-z0-9]+(-[a-z0-9]+)*$`, must match dir), `description` (required, 1-1024 chars), on-demand `skill` tool loading, one-folder-per-skill discovery.
- **988lifeline.org (.../warning-signs)** — 988 Suicide & Crisis Lifeline warning-signs list (verbatim phrasings for D-13); "died by suicide"/person-first usage (suicide-safer language).
- **findahelpline.com** — ThroughLine's global crisis-routing service (175+ countries, verified daily, powers Google/OpenAI/Anthropic crisis responses) — grounds D-14 curated set + locale ask.
- **gsd-discuss-phase/SKILL.md, gsd-plan-phase, and other installed opencode skills** — local convention reference for `name`+`description` frontmatter + structured body sections.

### Secondary (MEDIUM confidence)
- **en.wikipedia.org/wiki/Cognitive_distortion** (citing Burns 1980 *Feeling Good* / *Feeling Good Handbook*; Beck 1972 *Depression: Causes and Treatment*) — the "Ten Forms of Twisted Thinking": all-or-nothing, overgeneralization, mental filter, disqualifying the positive, jumping-to-conclusions (mind reading/fortune telling), magnification/catastrophizing, emotional reasoning, should-statements, labeling, personalization/blaming. Grounds the pathologos archetype mappings.
- **en.wikipedia.org/wiki/Rational_emotive_behavior_therapy** (citing Ellis) — REBT 4 core irrational beliefs (Demands, Awfulizing, Low Frustration Tolerance, Depreciation/global worth-rating), 3 core MUST philosophies, Stoic/Epictetus provenance. Grounds the archetypes + the philosophical alignment of the method.
- **en.wikipedia.org/wiki/Socratic_questioning** (citing Paul & Elder 2006 *The Thinker's Guide to the Art of Socratic Questioning*; Beck 1995 *Cognitive Therapy: Basics and Beyond*) — 6 Socratic-questioning categories + Beck's CBT-Socratic set. Grounds the 8 taxonomy operations (MTH-01).

### Tertiary (LOW confidence — flagged for human verify)
- Exact phrasing for harm-to-others / acute-crisis / reality-testing-loss stop conditions (A1) — derived by analogy, not from a fetched authoritative source.
- Young Schema Therapy schema names (A3) — corroborating only; source could not be fetched this session.

## Metadata

**Confidence breakdown:**
- Skill-packaging conventions (SKL-01, D-01..04): **HIGH** — two independent authoritative runtime docs agree, plus local installed-skill convention.
- Method taxonomy (MTH-01, D-11): **MEDIUM-HIGH** — grounded in cited Paul & Elder + Beck frameworks via Wikipedia; the 8-op mapping is the researcher's derivation but each operation has a clear source anchor.
- Pathologos archetypes (MTH-02, D-05..08): **MEDIUM-HIGH** — Burns + REBT (both cited) fully populate the 4 entries; schema-therapy corroboration is LOW (unfetched).
- Safety boundaries (MTH-03, D-13..15): **HIGH for self-harm + resources** (988 + findahelpline verified); **LOW for the three non-self-harm signal-phrase sets** (A1 — needs human review).
- Dialogue discipline (SKL-02..05): **HIGH** — grounded in verified skill-content-lifecycle convention + cited CBT/REBT/Socratic stance.

**Research date:** 2026-06-23
**Valid until:** 2026-07-23 (30 days; conventions and crisis resources are stable, but crisis-line numbers and the findahelpline routing should be re-confirmed at Phase 3 fixture time).

## RESEARCH COMPLETE
