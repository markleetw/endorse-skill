# Regression evaluation

Endorse is a writing skill. Its quality cannot be established by checking whether the output merely has four paragraphs or contains a particular phrase. Evaluate **first delivery** (before any user-requested refinement), using the same input and model settings where possible.

## How to run

1. Use a **version-pinned** `SKILL.md`. Record commit SHA, host, model, date, and temperature/settings if exposed.
2. For each fictional case in `cases/`, provide only the `Input` section to an assistant with Endorse installed. Let it ask genuinely necessary questions; answer only from `Facts available on follow-up`. Never reveal `Evaluator expectations` to the assistant.
3. Save the final English/zh-TW output **privately**. Do not commit actual recommendations about identifiable people.
4. Apply `rubric.md` independently to the **first completed recommendation**, not a later edit. Compare against the last released baseline using the same cases.
5. Record case-level scores, objective failures, and notable differences. A model judge can assist, but human review is required for factual attribution, distinctiveness, and prose.
6. Before release: no critical fabrication or attribution failure, no known fixable editorial flaw openly deferred to the user, and no material regression in the core cases.

## Case coverage

| Case | What it tests |
| --- | --- |
| `product-manager.md` | Specific product judgment, team-vs-person attribution |
| `engineering-lead.md` | Detecting meaningful people-leadership evidence without a checklist |
| `design-lead.md` | Holistic design judgment, tradeoffs, pruning repetitive praise |
| `ambiguous-attribution.md` | Clarification or calibrated wording when outcomes are uncertain |
| `limited-evidence.md` | No fabricated achievements; focused questioning or narrower claims |

All characters and organizations below are fictional. These cases represent evaluation *scenarios*, not reference recommendations or expected prose templates.

## Run records and release approval

Use [run-record-template.md](run-record-template.md) to document each case and model version, and a version-specific gate under [gates/](gates/) (for example, [v1.1.0](gates/v1.1.0.md)) to compare the pinned baseline and release candidate. Release approval must record the evidence actually reviewed and any untested risks explicitly accepted by the maintainer. A limited risk-based review must not be described as a controlled A/B pass. Do not simply tick a workflow input.

**Important:** The `Facts available on follow-up` are not shown up front. Only disclose specific facts when the assistant asks about them. An omitted relevant question is part of what the test evaluates; never auto-fill missing facts or mark an unrun case as passed.

## Limitations

Passing these cases does not prove model-independent reliability. Host support, context, model behavior, and skill installation can change. Structural CI is separate from this semantic evaluation and **must not be represented as writing-quality validation**.
