# Endorse

**LinkedIn recommendations that sound personal because they are grounded in firsthand experience.**

**English** · [繁體中文（台灣）](README.zh-TW.md) · [Skill instructions](SKILL.md) · [Releases](https://github.com/markleetw/endorse-skill/releases)

Endorse is a platform-independent, Markdown-based AI Agent Skill for writing distinctive and credible LinkedIn recommendations. It interviews you only when necessary, identifies evidence-backed professional strengths, and **revises its own writing before delivering the first recommendation**.

**Output:** a ready-to-review English recommendation, a faithful Traditional Chinese (Taiwan) meaning check, and a short editorial judgment. The recommender remains responsible for checking factual accuracy and choosing whether to publish.

## Why Endorse?

- **Evidence instead of flattering adjectives.** Ground claims in firsthand decisions, behaviors, contributions, and observed effects.
- **Distinctive perspective instead of a template.** Look for the insight that this recommender is uniquely positioned to share.
- **Credible attribution.** Separate individual proposals, manager approval, team execution, and verifiable outcomes; never invent metrics or causal impact.
- **Editing before delivery.** Perform evidence and narrative reviews, rewrite fixable weak passages, and avoid passing an editorial to-do list to the user.
- **Selective interviews.** Ask focused questions only when a missing fact could materially improve accuracy or reveal a defining contribution.

## Quick start

1. Download **[endorse.zip from the latest release](https://github.com/markleetw/endorse-skill/releases/latest)**.
2. Install the ZIP using a compatible platform's Skills interface:

| Platform | Installation |
| --- | --- |
| **ChatGPT** (eligible workspaces) | **Plugins → Skills → Create → Upload from your computer**. Availability depends on plan and workspace settings. |
| **Claude** (where Skills are supported) | Open the Skills area in Claude's settings and use its skill upload option. UI labels may vary by version and plan. |
| **Other compatible agents** | Follow the agent's own instructions for installing skills. |

The ChatGPT upload flow is documented in the [official ChatGPT Skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt). Uploading a ZIP as an ordinary chat attachment is **not equivalent** to installing a Skill.

3. Ask your assistant to use **Endorse**. Where supported, you may invoke it with `/endorse`:

```text
/endorse Write a LinkedIn recommendation for a former direct report. Ask me only what you need.
/endorse 我想推薦一位以前合作的工程主管，請先問我必要的問題。
/endorse Refine this draft and check which claims I can actually support.
```

The exact invocation mechanism depends on the host. Endorse does not connect to or publish on LinkedIn.

## How it works

1. **Establish firsthand context:** your relationship, responsibilities, and relevant observations.
2. **Find a defensible distinction:** connect strengths to specific behavior; check for overlooked dimensions only when material.
3. **Choose a narrative angle:** privately compare supported framings, then build one coherent portrait.
4. **Review twice:** verify evidence and attribution; then substantively edit structure, clarity, opening, ending, and repeated points.
5. **Deliver bilingually:** English recommendation, meaning-equivalent zh-TW translation, and a concise editorial judgment.

For the complete behavior specification, see [SKILL.md](SKILL.md).

## A small illustrative example

All people and organizations in this example are **fictional**. The comparison demonstrates a *kind of improvement*, not a promised output or prescribed sentence pattern.

**Generic input:** “Sam is a brilliant PM and a great team player.”

**Better evidence:** “When a new discovery feature had no agreed solution, Sam compared user feedback with engineering constraints, proposed a narrower experiment, and helped the team make a decision. I reviewed the prioritization; the team built the experiment.”

**A possible recommendation excerpt:**

> What I appreciated about working with Sam was the way they made uncertain product decisions easier to discuss. When our team had no agreed solution for a discovery problem, Sam helped us compare user needs with engineering constraints and proposed a smaller experiment we could actually learn from. That judgment was valuable well before any feature shipped.

Endorse should **not** infer an uplift, claim Sam single-handedly shipped the feature, or force this structure on another person.

## Compatibility and limitations

Endorse is a text-only Agent Skill: no runtime dependencies, external services, LinkedIn API access, or automated posting. Installation and instruction-following vary by AI platform, model, permissions, and context. A valid Markdown skill file does not guarantee identical behavior across hosts. Output is intended for **human factual review** before publication.

## Quality and privacy

The project maintains a [fictional regression evaluation suite](evals/README.md) and [editorial rubric](evals/rubric.md). These describe how to assess grounding, attribution, distinctiveness, role coverage, editing, and translation fidelity. They are **not a claim of comprehensive model validation**.

Do not publish identifiable colleagues' drafts, private performance discussions, or unpublished company details in public issues or PRs. Public test cases are fictional.

## Contributing and releases

- [How to contribute](CONTRIBUTING.md) · [Security reporting](SECURITY.md)
- [Changelog](CHANGELOG.md) · [GitHub Releases](https://github.com/markleetw/endorse-skill/releases)
- **Release ZIP:** a versioned snapshot. **`main`:** ongoing development, which may contain newer instructions than the latest ZIP.
- **Current published version:** [v1.0.1](https://github.com/markleetw/endorse-skill/releases/tag/v1.0.1). A future v1.1.0 is planned but has **not** been released.

## License

No open-source license has yet been granted. Public visibility alone does not authorize redistribution, derivative works, or sublicensing. The license is under review; until one is selected, the existing copyright restrictions apply.
