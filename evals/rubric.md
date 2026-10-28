# Editorial regression rubric

Score each dimension 0–3: **0** = serious failure; **1** = material weakness; **2** = acceptable; **3** = strong. Provide one concrete excerpt or observation supporting each score; avoid judging solely by fluency.

| Dimension | A 3 means |
| --- | --- |
| Grounding | Every meaningful claim is clearly supported by the provided facts or carefully qualified |
| Attribution | Distinguishes proposal, approval, team execution, and observed results |
| Distinctiveness | Specific professional judgment and recommender vantage point; not interchangeable names |
| Role coverage | Notices an important, evidenced responsibility when relevant, without forcing a checklist |
| Narrative development | Each paragraph adds evidence, a facet, or meaning; no repeated summary |
| Editorial completion | Corrects fixable defects *before* first delivery; no editorial to-do list |
| Natural English | Concise, credible professional voice; no invented inner motives or advertising language |
| zh-TW fidelity | Natural Taiwan Traditional Chinese with no extra claims or lost qualifiers |

**Critical fail (regardless of score):** fabricated metric/project/result, misattributed sole ownership, invented firsthand observation, materially inaccurate Chinese translation, or knowingly delivering a fixable issue as an editorial TODO.

For each run record: case ID, skill commit/release, platform and model, date, clarifying questions, factual deviations, each dimension score, editorial remarks, and pass/fail. Compare **per-case** changes; do not use a single overall average to hide a regression. Score variability is expected; replicate borderline cases when feasible.

**Release gate suggestion:** no critical failures across the fixed suite; all 8 dimensions at least 2 for core cases, with human sign-off on exceptions. A lack of model access or incomplete evaluation is **not** a passing result.
