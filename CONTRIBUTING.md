# Contributing to Endorse

Thank you for helping make professional recommendations more credible and personal.

## Before opening an issue

- Check the current [Skill](SKILL.md), [evaluation scenarios](evals/README.md), and existing issues.
- State whether the problem concerns factual grounding, attribution, missed role evidence, narrative quality, translation, installation, or distribution.
- Provide a minimal, **fictionalized** reproduction. Do not submit a real person's recommendation, personnel feedback, or confidential work details without explicit authorization.
- Distinguish model/host-specific failures from an instruction issue. Include relevant platform, model, and Skill commit when known.

## Proposing a change

- Explain the user-visible quality problem and why the existing rules do not address it.
- Prefer simplifying or clarifying current instructions over adding duplicate directives.
- For changes to `SKILL.md`, add or revise fictional eval cases, run the [rubric](evals/rubric.md) against the current release and proposed revision, and document regressions.
- Update both `README.md` and `README.zh-TW.md` for user-facing behavioral, installation, or compatibility changes.
- Do not claim that passing structural CI proves writing quality.

## Pull requests

Use a descriptive title, explain expected behavior and tradeoffs, link related issues, and list tests actually performed. A maintainer may request human review of generated prose. Please avoid publishing real-person recommendation examples.

## Licensing status

The repository has not yet adopted an open-source license. Public pull requests do not automatically grant third parties a license to reuse this repository; please check the current [README](README.md) and discuss substantial contributions with the maintainer until licensing is resolved.
