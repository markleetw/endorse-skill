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

## Install as an Agent Skill

Endorse follows the **Agent Skills** folder convention: a directory named `endorse` containing the required `SKILL.md` with YAML frontmatter. It has no scripts, dependencies, API keys, or external services.

Download `endorse-v1.0.0.zip` from the release, or copy the [SKILL.md](SKILL.md) file into an `endorse/` folder. Install the **folder**, not the README, in your agent's skills directory.

```text
endorse/
└── SKILL.md
```

**Common skill directory locations:**

| Agent | Personal skills | Workspace/repository skills |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/endorse/SKILL.md` | `.claude/skills/endorse/SKILL.md` |
| Codex (CLI / IDE) | `~/.agents/skills/endorse/SKILL.md` | `.agents/skills/endorse/SKILL.md` |
| Other Agent Skills-compatible agents | Follow the agent's documented skills location | Follow the agent's documented skills location |

If your agent has a skill installer, point it at the repository or the downloaded skill directory as supported by that installer. After installation, use your agent's skill selector or explicit skill invocation (for example, `/endorse` in Claude Code or `$endorse` in Codex), or describe the task so the agent can match the skill description. Automatic selection varies by agent.

To update, replace the installed `endorse/SKILL.md` with the newer version; restart your agent if it does not detect changes.

## Use

Start naturally in **English or Chinese**. You do not need to pre-fill a form.

**English example:**

> Help me write a LinkedIn recommendation for a former colleague. I was their manager. They handled difficult trade-offs across product, business, and operations. Interview me for any essential details, then draft and refine the recommendation.

**繁體中文範例：**

> 我要寫一篇前同事的 LinkedIn 推薦文。他擅長處理複雜的產品決策，也會主動協助其他同事。請依照 SKILL.md 訪談我，只問必要的問題，完成審稿後再交稿。

When invoked, Endorse asks focused follow-up questions **only when needed** for credibility or differentiation. Otherwise it will draft, complete its own review, and provide:

1. **English | LinkedIn Recommendation** — ready to copy into LinkedIn.
2. **繁體中文｜語意對照** — faithful to the English claims and level of certainty.
3. **Editorial judgment** — a short note about positioning and any unresolved factual uncertainty.

You retain responsibility for checking whether the account of the person and their work is accurate before publishing.

## Editorial principles

**Evidence over adjectives. Distinctiveness over templates. Judgment over compliance.**

The opening should earn attention without using a formula; the middle should show what the person *actually did* and why it mattered; the ending should offer a genuine observation that only this recommender could reasonably make. Specificity matters more than meeting a rigid word count.

Endorse never fabricates achievements, metrics, motivations, sole ownership, or business impact. A good recommendation should be convincing to an outside reader unfamiliar with the company.

## Scope and privacy

**Included:** LinkedIn written recommendations; adaptive interviewing; evidence and narrative review; English text with Traditional Chinese semantic translation.

**Not included:** LinkedIn skill endorsements, reference checks, formal reference letters, automated LinkedIn posting, independent research, or external integrations.

Avoid placing unpublished or personally identifying recommendation drafts in public issues, commits, or examples without the person's permission. The repository intentionally contains **no real-person case studies**.

## Version and distribution

- **Version:** v1.0.0 (first stable release)
- **Source of truth:** [SKILL.md](SKILL.md)
- **Package:** `endorse-v1.0.0.zip` containing the skill and bilingual documentation
- **Changes:** [Release notes](RELEASE_NOTES.md)

## License

No open-source license has been granted for this repository. Public availability is not permission to redistribute, modify, or sublicense the project. Contact the repository owner for rights beyond those GitHub's terms permit.
