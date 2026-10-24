# Endorse

**Thoughtful recommendations, grounded in real experience.**

Endorse is a platform-independent AI Agent Skill for writing credible, distinctive LinkedIn recommendations. It interviews the recommender when needed, identifies evidence-backed strengths, and **reviews and refines the writing before delivery**.

> **Status: Pre-release / not yet user-validated.** This repository is available for hands-on testing. No stable version, package, or GitHub Release has been published.

## What it does

1. Establishes your working relationship and what you personally observed.
2. Asks targeted follow-up questions only when important evidence is missing.
3. Finds the person's distinctive strengths rather than listing generic praise.
4. Writes a natural English LinkedIn recommendation and checks it against a rigorous editorial standard.
5. Provides a Traditional Chinese meaning-equivalent translation and a short editorial note.

## Use

Open [`SKILL.md`](SKILL.md) in an AI assistant that supports Markdown-based agent skills or custom instructions. Follow that platform's standard method for adding a skill; no particular vendor, plugin, or tool is required by Endorse.

Start with a natural-language request, for example:

> Help me write a LinkedIn recommendation for a former colleague. I was their manager for two years. They were particularly good at taking ownership of unfamiliar projects. Ask me what you need to know before writing.

You can respond in Chinese or English. Endorse will ask follow-up questions only if they materially improve the recommendation.

## Editorial philosophy

**Evidence over adjectives. Distinctiveness over templates. Judgment over compliance.**

A recommendation should be something the recommender can personally stand behind. Endorse does not invent accomplishments, overstate a person's role, or pad a recommendation to reach an arbitrary length. It also does not blindly accept edits that weaken the writing.

## Scope

- **Included:** Written LinkedIn recommendations, adaptive interview, English recommendation, Traditional Chinese translation, brief editorial notes.
- **Not included:** LinkedIn skill endorsement clicks, formal letters, reference checks, automated LinkedIn posting, external research, or platform-specific integrations.

## Project status and releases

This is an **unvalidated working version**. Please test it with real recommendation-writing conversations. A stable `v1.0.0` tag, packaged download, and GitHub Release will be created **only after the maintainer validates the skill in practice**.

## License

No license has been selected yet. Until one is added, normal copyright restrictions apply to reuse and redistribution.
