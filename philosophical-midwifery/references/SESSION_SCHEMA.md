# Session Schema

This reference is the **single source of truth** for the session-state JSON shape produced by a `philosophical-midwifery` inquiry. The atomic unit of the product is **the examined proposition** (design-draft §14) — not the chat message — and this schema exists to make that atomic unit inspectable: every field below captures one step of the movement from a concrete disturbance toward a user-confirmed, examined proposition, plus any contradiction, revision, or tension that survived the examination.

This file is a sibling of Phase 1's three references under `philosophical-midwifery/references/`. It does **not** contradict the standing-instruction inquiry loop in `../SKILL.md` (steps 1–8); it names the state that loop produces turn by turn. Phase 1's `SKILL.md` is left unchanged — this schema only documents the artifacts that emerge as the loop runs.

**Single source of truth (A-2).** There is no separate JSON-Schema sidecar. The validator at `../scripts/validate_session_schema.py` encodes the required / type / enum rules defined here directly. When you change a rule below, change the validator in the same step and keep the two in sync.

**Voice.** Field definitions, types, and enums below use neutral spec prose. The brief usage guidance is directive second-person, matching the voice of `../SKILL.md` and the other references.

## The `phase` enum (5 values — A-1)

The `phase` field takes exactly one of these five values:

| Value | Meaning |
|-------|---------|
| `intake` | Identifying the presenting disturbance and securing one concrete example. (SKILL.md loop steps 1–2.) |
| `extraction` | Inferring candidate hidden beliefs as hypotheses and asking the user to select, reject, or revise one. (Steps 3–4.) |
| `normalization` | Converting the user-confirmed belief into a general, testable proposition. (Step 5.) |
| `examination` | Examining the proposition with Socratic questioning, one question at a time. (Step 6, drawing on `QUESTION_TAXONOMY.md`.) |
| `synthesis` | Locating contradiction or revision and producing the session summary. (Steps 7–8.) |

**Contradiction/revision and session-summary are sub-activities of `synthesis`, NOT separate `phase` values.** The procedural design draft (§7) describes six phases including a distinct contradiction/revision step and a session-summary step; for the state schema the canonical `phase` field is the five-value enum above, and both contradiction-tracking and summary-generation happen *within* `synthesis`. This keeps the validator's enum finite and grounded in the schema section of the design draft (§9).

## Required fields

Every required field below must be present and non-empty in a valid session JSON. The validator treats a missing key, an empty string, or an empty array/object as a failure for the fields marked required below (per D-01 strictness).

| Field | JSON type | Required | Description |
|-------|-----------|----------|-------------|
| `session_id` | string | required | A unique session identifier in UUID format (e.g., `"a1b2c3d4-..."`). One per inquiry session. |
| `created_at` | string | required | When the session began, as an ISO-8601 date-time string (e.g., `"2026-06-24T12:00:00Z"`). The validator parses this with ISO-8601 strictness. |
| `phase` | string (enum) | required | The current inquiry phase. One of the five values in the enum above. |
| `presenting_disturbance` | string | required | The felt disturbance, blockage, resentment, fear, shame, or confusion the user wants to examine, in their own framing. |
| `concrete_example` | string | required | One specific situation (not an abstraction) that carries the charge of the disturbance. |
| `candidate_beliefs` | array of objects | required | Candidate hidden beliefs inferred from the example, each offered as a hypothesis (never a diagnosis). See sub-fields below. |
| `selected_belief` | object | required | The candidate the user selected, rejected-and-restated, or revised. Examination cannot begin until this is set by the user. See sub-fields below. |
| `normalized_proposition` | string | required | The selected belief restated as a general, testable proposition the user confirms is accurate enough to examine. |
| `definitions` | object | required | Key terms in the proposition mapped to agreed meanings (e.g., `{"worth": "...", "recognition": "..."}`). May start empty and fill as the inquiry clarifies terms. |
| `implications` | array of strings | required | Consequences traced from the proposition (what must follow if it is true). Populated during examination. |
| `counterexamples` | array of strings | required | Concrete cases offered to weaken or test the proposition. Populated during examination. |
| `contradictions` | array of strings | required | Incompatibilities surfaced between commitments the user holds. A sub-activity of `synthesis`. |
| `revised_proposition` | string | required | The proposition restated more carefully after pressure, if a revision survived. May be empty until `synthesis`. |
| `unresolved_tensions` | array of strings | required | Tensions the inquiry could not resolve — affective charge that remains despite conceptual revision, or open questions. |
| `next_questions` | array of strings | required | Inquiry targets for a future session — the next proposition or counterexample worth examining. |
| `session_summary` | string | required | The rendered markdown string produced by filling in `../assets/session_summary_template.md`. See the note below (A-3). |

> The validator treats the fields above as a closed required set. Optional fields are permitted (e.g., an `affective_charge` annotation) but the validator does not require them and does not check their types.

## Sub-fields

### `candidate_beliefs[]` entries

Each entry in the `candidate_beliefs` array is an object with these fields:

| Sub-field | JSON type | Required | Description |
|-----------|-----------|----------|-------------|
| `id` | string | required | A belief identifier using the `belief_N` convention (A-4): `belief_1`, `belief_2`, … Stable within a session so `selected_belief` can reference it. |
| `text` | string | required | The candidate belief, phrased as a hypothesis (e.g., `"Recognition determines worth."`). |
| `confidence` | string (enum) | required | How strongly the evidence supports this candidate. One of `low`, `medium`, `high`. |
| `evidence` | array of strings | required | The concrete cues from the example that suggested this candidate. |

### `selected_belief`

The object recording which candidate the user owned:

| Sub-field | JSON type | Required | Description |
|-----------|-----------|----------|-------------|
| `id` | string | required | The `belief_N` id of the selected candidate, or a new id if the user restated it in their own words. |
| `text` | string | required | The belief as the user confirmed or restated it. |

## The `session_summary` field (A-3)

`session_summary` holds the **rendered markdown string** you produce by filling in `../assets/session_summary_template.md` with the examined proposition, definitions, implications, counterexamples, contradiction or weakness, revised proposition, unresolved tension, and next inquiry target. The template is the render target; the filled-in string is what this field stores.

**Validator behavior.** The validator treats `session_summary` as a **required non-empty string only**. It does **not** parse the markdown structure or check that every template heading is present. Structural completeness of the summary is a human-review concern (Phase 1's epistemic-humility stance carries over: the summary must not assert certainty beyond the conversation).

## Worked example — "recognition determines worth"

A complete, schema-valid session built on the shared Phase 1 example lives at `../scripts/fixtures/valid.json`. Its key fields:

- `phase`: `"synthesis"`
- `candidate_beliefs[0]`: `{ "id": "belief_1", "text": "Recognition determines worth.", "confidence": "medium", "evidence": [...] }`
- `selected_belief`: `{ "id": "belief_1", "text": "Recognition determines worth." }`
- `normalized_proposition`: `"The value of work depends on recognition."`
- `contradictions`: includes the incompatibility between "valuable things can go unrecognized" and "lack of recognition means lack of value in my own case."
- `revised_proposition`: `"Recognition affects visibility and opportunity, but does not determine intrinsic worth."`
- `session_summary`: the filled-in `session_summary_template.md` string for this thread.

The property-graph view of the same thread lives in `../assets/belief_graph_template.json`; the invalid sibling of this fixture lives at `../scripts/fixtures/invalid.json`. All three are threaded by the recognition-determines-worth example so cross-references stay coherent.
