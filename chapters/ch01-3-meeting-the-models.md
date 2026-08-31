---
title: "Meeting the Models: A Tour of the Family"
subtitle: "Not All Intelligence Is the Same Shape"
short_title: "Meeting the Models"
description: "A practical framework for choosing among AI model tiers and families — and a dated roster for the current lineup."
label: ch01-3
tags: [ai, business, cognition-economy, chapter-1]
---

# Meeting the Models: A Tour of the Family

:::{figure} ../images/ch01-3-infographic.png
:label: fig-ch01-3-infographic
:alt: Infographic comparing AI model families — Claude, Gemini, GPT, Grok, and open-weight models — organized by capability tier with pricing context
:width: 80%
:align: center

*The AI model landscape: major families, capability tiers, and when to reach for each.*
:::

All frontier AI models have extraordinary intelligence. But they are not identical. Just as two people with the same IQ can have very different personalities, cognitive styles, and areas of strength, different models have different temperaments — different tendencies in how they reason, what they emphasize, and where they shine.

Choosing the right model for a task is not a technical decision. It is a practical one. Understanding the landscape helps you reach for the right tool without overthinking it.

---

## A Note on Version Numbers

Before we go any further: any specific model version named in this chapter will be outdated within months. AI providers release new versions constantly, and whatever names appear in the roster sidebar below will have successors by the time you read this.

**The principles do not change. The versions do.**

For the current model map — including which models are available today, what they cost, and which are recommended for which tasks — visit the companion page at **[cognitioneconomy.net/ch01-companion](https://cognitioneconomy.net/ch01-companion)**. That resource is maintained in real time.

Read this chapter for the framework of how to think about model selection. Use the companion page for the current roster.

---

## The Smartphone Analogy

Think of model tiers the way you think about smartphone lines. Apple sells the iPhone Pro Max, the iPhone Pro, and the standard iPhone. All three make calls and run apps. But the Pro Max has more capability, more processing power, and a higher price. You do not reach for the Pro Max for every task — you use the standard model for most things and the Pro Max when the stakes justify the cost.

AI models work the same way. Every major provider offers a tiered lineup:

| Tier | Analogy | Use Case |
|------|---------|----------|
| **Flagship / Frontier** | iPhone Pro Max | Complex reasoning, nuanced writing, deep analysis |
| **Balanced / Daily Driver** | iPhone Pro | Daily professional work, most business tasks |
| **Fast / Cheap** | iPhone Standard | High volume, quick lookups, speed-sensitive tasks |

Two additions to this picture have become standard across the industry. First, vendors now also ship *gated frontier tiers above the flagship* — experimental, higher-priced models available to a subset of customers before wide release. Second, the flagship you talk to increasingly *routes* your request among sub-models behind the scenes, choosing how much reasoning effort to spend. Neither changes the framework: you still choose by role, not by name.

---

## The Three Roles, By Family

In running text throughout this book, we will refer to models by role rather than by version number:

**The flagship tier** — the deepest reasoner in each family. Reach for it when the problem is genuinely complex: multi-variable business decisions, nuanced legal or strategic analysis, tasks where you need the model to think carefully before responding.

**The balanced tier** — the daily driver. An excellent balance of capability, speed, and cost. Most professionals find the balanced tier handles 90% of their work at a fraction of the flagship cost.

**The fast tier** — built for speed and volume. Use it when you need fast, lightweight responses: summarizing short documents, answering quick questions, processing large batches of content.

Every major family maps onto these roles:

- **Claude (Anthropic)** — built with a strong emphasis on careful reasoning, nuanced instruction-following, and long-context performance. Widely regarded as a top choice for complex writing, structured analysis, and tasks requiring sustained coherence across long documents.
- **Gemini (Google)** — deeply integrated with Google Workspace. If you live in Google Docs, Sheets, Gmail, or Drive, Gemini has native access to that ecosystem in ways other models do not. If you already pay for Google Workspace at the business level, some Gemini access may be included — check your organization's plan before subscribing separately.
- **GPT (OpenAI)** — the lineage that launched the current AI wave, with the largest ecosystem of third-party tools and integrations of any platform. Strong across writing, reasoning, coding, and multimodal tasks.
- **Grok (xAI)** — xAI's model, trained with a distinctive voice — direct, sometimes irreverent, with real-time access to X (formerly Twitter) data. Uniquely suited for tasks involving social media trends and current events on X.

:::{admonition} Model Roster — Fall 2026 edition
:class: note

*This sidebar is the one place in this chapter where names, versions, and prices appear. It was accurate at press time and will drift. The live roster is at [cognitioneconomy.net/ch01-companion](https://cognitioneconomy.net/ch01-companion).*

**Anthropic (Claude)** — Flagship: **Claude Opus 4.7**. Balanced: **Claude Sonnet 4.6**. Fast: **Claude Haiku 4.6**. Access at [claude.ai](https://claude.ai); free tier available; the paid consumer plan (about \$20/month at press time) unlocks the balanced and flagship tiers.

**Google (Gemini)** — Flagship: **Gemini 3.1 Pro**. Fast: **Gemini Flash**. Access at [gemini.google.com](https://gemini.google.com); free tier available; paid consumer plan comparably priced.

**OpenAI (GPT)** — Flagship: **GPT-5.5** (with a parallel-reasoning Pro variant for complex scientific, legal, or strategic problems). Access at [chatgpt.com](https://chatgpt.com); free tier available; paid consumer plan comparably priced.

**xAI (Grok)** — Access at [x.ai/grok](https://x.ai/grok) or within the X platform.
:::

---

## Open-Weight Models (Run Locally or via API)

A growing class of models are released with open weights — meaning the underlying model parameters are publicly available. This allows them to be run on your own hardware, customized for specific domains, or deployed without sending data to a third-party cloud.

```{list-table} Major Open-Weight Families
:header-rows: 1
:widths: 25 40 35

* - Family
  - Provider
  - Notable Strength
* - **Llama**
  - Meta
  - Broad capability; widely supported; runs locally
* - **Mistral**
  - Mistral AI (France)
  - Efficient; strong for European language tasks
* - **Qwen**
  - Alibaba
  - Strong multilingual; excellent for East Asian language tasks
* - **Phi**
  - Microsoft
  - Small but capable; optimized for edge/local deployment
```

Open-weight models are most relevant for organizations with strict data privacy requirements, developers building customized applications, or power users who want to run AI without subscription costs.

---

## Where to Compare Models Side by Side

The fastest way to develop model intuition is to run the same prompt through multiple models simultaneously.

At press time, we use **[arena.ai](https://arena.ai)** for side-by-side comparison — run the same prompt through two or more models at once and compare outputs instantly, no setup required. (If the platform has changed by the time you read this, the companion page at **cognitioneconomy.net/ch01-companion** points to the current recommendation.)

Use side-by-side comparison to:
- See which model handles your specific task better
- Develop personal intuition about tone and reasoning style differences
- Quickly benchmark a new model you haven't used before

---

## How to Choose

For most business professionals, the decision is simpler than it looks:

::::{grid} 1 2 2 3
:::{card} 🧠 Deep Analysis
Use the **balanced or flagship tier** for anything requiring nuanced reasoning, long-document work, or careful writing.
:::
:::{card} 📊 Google-First
Use **Gemini** when your work lives in Google Docs, Sheets, or Gmail — native integration is the differentiator.
:::
:::{card} ⚡ Speed & Volume
Use the **fast tier** when you need lightweight processing of many small tasks.
:::
::::

---

## Summary

:::{admonition} Key Takeaways — Chapter 1.3
:class: tip

1. Different models have different cognitive "temperaments" — understanding these helps you choose correctly.
2. The smartphone tier analogy applies: flagship, balanced, and fast tiers serve different needs. Choose by role, not by name.
3. Claude excels at nuanced reasoning and long-context tasks. Gemini is best when integrated with Google Workspace. GPT offers the largest third-party ecosystem.
4. Version numbers will change; the principles of model selection will not. The roster sidebar is dated for a reason — check cognitioneconomy.net/ch01-companion for current recommendations.
5. Side-by-side comparison is the fastest way to develop personal intuition about model differences.
:::

---

:::{tip} Try This
Run one real question through two different models at the same time (we use arena.ai; current instructions at **cognitioneconomy.net/ch01-companion**). Pick any question you'd actually care about the answer to. Spend 90 seconds comparing the tone and depth of the two responses — that instinct you build is worth more than any review article.
:::
