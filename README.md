# Endorse

**Thoughtful LinkedIn recommendations, grounded in real experience.**

[繁體中文](README.zh-TW.md) · **English** · [Skill instructions](SKILL.md) · [v1.0 release notes](RELEASE_NOTES.md)

Endorse is a platform-independent AI Agent Skill for creating distinctive, credible LinkedIn recommendations. It interviews the recommender only when essential details are missing, finds evidence-backed strengths, and **edits the recommendation before showing the first draft**.

The result is a publish-ready **English recommendation**, a meaning-equivalent **Traditional Chinese translation**, and a brief editorial assessment.

## Why Endorse

- **Specific, not generic.** It anchors the recommendation in firsthand observations, judgments, and concrete contributions rather than a list of flattering adjectives.
- **Natural openings.** It avoids defaulting to “I worked with…” or “I managed…” and opens with a meaningful, person-specific insight when the evidence supports one.
- **Earned endings.** The conclusion explains something the recommender genuinely values or learned about working with this person; it does not merely repeat compliments.
- **Honest attribution.** It separates an individual's proposal or ownership from team execution and verified outcomes. It does not invent results.
- **Two editorial passes, built in.** Evidence and attribution are checked first; voice, structure, clarity, and concision are refined second. You should not need to request “review and refine.”

## Install

Download the latest `endorse.zip` from [Releases](https://github.com/markleetw/endorse-skill/releases/latest).

| AI Tool | How to install |
| --- | --- |
| ChatGPT | Upload the ZIP in a ChatGPT conversation and ask it to install the Skill. |
| Claude | Settings → Skills → Add → Upload Skill |

## Use

Start with `/endorse` (if your tool supports skill commands), or simply ask the assistant to use Endorse. For example:

```text
/endorse Write a LinkedIn recommendation for my former colleague. I was their manager.
/endorse 我想幫以前的同事寫 LinkedIn 推薦文，他很擅長產品決策。
/endorse 請幫我精修這篇舊推薦文，保留事實但讓文字更自然。
```

Endorse will ask only for essential missing facts, then independently review and refine the recommendation before delivering English and Traditional Chinese versions.


## Editorial principles

**Evidence over adjectives. Distinctiveness over templates. Judgment over compliance.**

The opening should earn attention without using a formula; the middle should show what the person *actually did* and why it mattered; the ending should offer a genuine observation that only this recommender could reasonably make. Specificity matters more than meeting a rigid word count.

Endorse never fabricates achievements, metrics, motivations, sole ownership, or business impact. A good recommendation should be convincing to an outside reader unfamiliar with the company.

## Scope and privacy

**Included:** LinkedIn written recommendations; adaptive interviewing; evidence and narrative review; English text with Traditional Chinese semantic translation.

**Not included:** LinkedIn skill endorsements, reference checks, formal reference letters, automated LinkedIn posting, independent research, or external integrations.

Avoid placing unpublished or personally identifying recommendation drafts in public issues, commits, or examples without the person's permission. The repository intentionally contains **no real-person case studies**.

## Version and distribution

- **Version:** v1.0.1 (documentation update; skill instructions unchanged)
- **Source of truth:** [SKILL.md](SKILL.md)
- **Package:** `endorse.zip` (latest release; skill and bilingual documentation)
- **Changes:** [Release notes](RELEASE_NOTES.md)

## License

No open-source license has been granted for this repository. Public availability is not permission to redistribute, modify, or sublicense the project. Contact the repository owner for rights beyond those GitHub's terms permit.
