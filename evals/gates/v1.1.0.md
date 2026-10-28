# Release gate — v1.1.0

**Evaluation status: LIMITED REVIEW ACCEPTED BY MAINTAINER — NOT A MODEL A/B PASS.**

The user/maintainer explicitly approved proceeding with v1.1.0 on 2026-10-28 after reviewing the [lightweight regression review](reviews/v1.1.0-lightweight.md) and acknowledging that no controlled model-version comparison or cross-platform installation test was run. This is **risk acceptance**, not evidence that those tests passed.

## Evidence and limitations

| Check | Status | Evidence |
| --- | --- | --- |
| Historical first-draft issues reviewed | Reviewed | [Lightweight review](reviews/v1.1.0-lightweight.md) |
| Baseline vs candidate instructions | PASS (static) | v1.0.1 SKILL.md and unchanged candidate SKILL.md hash recorded in review |
| Fictional product-manager model A/B | NOT RUN | No generated output evaluated |
| Fictional engineering-lead model A/B | NOT RUN | No generated output evaluated |
| Fictional design-lead model A/B | NOT RUN | No generated output evaluated |
| Ambiguous attribution model A/B | NOT RUN | No generated output evaluated |
| Limited evidence model A/B | NOT RUN | No generated output evaluated |
| Cross-host Skills UI installation | NOT RUN | Host-specific availability; users must validate on their environment |
| Package structural verification | PASS on release candidate PR when CI completes | Shared packaging script, ZIP file set, checksum |
| Release notes and License | Included in release packaging | MIT License and bilingual version-specific notes |

## Residual risk accepted

The candidate has added instructions explicitly intended to improve narrative angle selection, role coverage, and pre-delivery editing; the actual effect can vary by model and host. Static checks cannot prove prose quality, correct follow-up questions, or no regression. Human factual review is required before posting recommendations.

If issues appear after release, add fictionalized regression cases and publish a corrective release rather than modifying an existing tag or asset.

**Release approval: APPROVED.**

Approved scope: v1.1.0 only, with the above caveats. No SKILL.md changes in this release preparation.
