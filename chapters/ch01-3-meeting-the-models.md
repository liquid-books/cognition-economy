---
title: "Meeting the Models: A Tour of the Family"
subtitle: "Not All Intelligence Is the Same Shape"
short_title: "Meeting the Models"
description: "A practical guide to the major AI model families, their strengths, and when to use each one."
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

Before we go any further: the specific model versions named in this chapter will be outdated within months. AI providers release new versions constantly, and the version numbers you see here — Opus 4.7, Gemini 3.1, and others — will have successors by the time you read this.

**The principles do not change. The versions do.**

For the current model map — including which models are available today, what they cost, and which are recommended for which tasks — visit **[drleee.io](https://drleee.io)**. That resource is maintained in real time.

Read this chapter for the framework of how to think about model selection. Use drleee.io for the current roster.

---

## The Smartphone Analogy

Think of model tiers the way you think about smartphone lines. Apple sells the iPhone Pro Max, the iPhone Pro, and the standard iPhone. All three make calls and run apps. But the Pro Max has more capability, more processing power, and a higher price. You do not reach for the Pro Max for every task — you use the standard model for most things and the Pro Max when the stakes justify the cost.

AI models work the same way. Every major provider offers a tiered lineup:

| Tier | Analogy | Use Case |
|------|---------|----------|
| **Frontier / Max** | iPhone Pro Max | Complex reasoning, nuanced writing, deep analysis |
| **Balanced / Pro** | iPhone Pro | Daily professional work, most business tasks |
| **Fast / Standard** | iPhone Standard | High volume, quick lookups, speed-sensitive tasks |

---

## The Claude Family (Anthropic)

Claude is built by Anthropic with a strong emphasis on careful reasoning, nuanced instruction-following, and long-context performance. It is widely regarded as the best model for complex writing, structured analysis, and tasks requiring sustained coherence across long documents.

:::{admonition} Claude Lineup
:class: note

**Claude Opus 4.7** — The deepest reasoner in the family. Reaches for this when the problem is genuinely complex: multi-variable business decisions, nuanced legal or strategic analysis, tasks where you need the model to think carefully before responding.

**Claude Sonnet 4.6** — The daily driver. Excellent balance of capability, speed, and cost. Most professionals find that Sonnet handles 90% of their work at a fraction of the Opus cost.

**Claude Haiku 4.6** — Built for speed and volume. Use when you need fast, lightweight responses: summarizing short documents, answering quick questions, processing large batches of content.
:::

**Access:** [claude.ai](https://claude.ai) — Free tier available; Pro plan (\$20/month) unlocks Sonnet and Opus.

---

## The Gemini Family (Google)

Gemini is Google's flagship model family, deeply integrated with Google Workspace. If you live in Google Docs, Sheets, Gmail, or Drive, Gemini has native access to that ecosystem in ways that other models currently do not.

:::{admonition} Gemini Lineup
:class: note

**Gemini 3.1 Pro** — Google's frontier model. Competes at the top tier for reasoning and writing. Particularly strong for tasks that involve Google products or require real-time Google Search integration.

**Gemini Flash** — Google's speed-optimized model. Excellent for high-volume applications and lightweight tasks. Extremely cost-efficient for developers and businesses running at scale.
:::

**Access:** [gemini.google.com](https://gemini.google.com) — Free tier available; Gemini Advanced (\$20/month) in Google One.

**Differentiator:** If you already pay for Google Workspace Business, Gemini may be included. Check your organization's plan before subscribing separately.

---

## The GPT Family (OpenAI)

OpenAI's GPT series is the lineage that launched the current AI wave. GPT-4o is the current flagship — multimodal (text, images, audio), fast, and deeply capable. OpenAI also operates the world's largest ecosystem of third-party plugins and integrations.

:::{admonition} Key GPT Models
:class: note

**GPT-4o** — OpenAI's primary frontier model. Strong across writing, reasoning, coding, and image analysis. The largest third-party tool ecosystem of any platform.

**o3 / o4-mini** — OpenAI's "reasoning" models, designed for slow, deliberate step-by-step problem solving. Best for mathematical, scientific, or highly structured logical problems.
:::

**Access:** [chatgpt.com](https://chatgpt.com) — Free tier (GPT-4o limited); Plus plan (\$20/month).

---

## Grok (xAI)

Grok is Elon Musk's xAI model, trained with a distinctive voice — direct, sometimes irreverent, with real-time access to X (formerly Twitter) data. This makes it uniquely suited for tasks involving social media trends, current events on X, or contexts where a more candid, unfiltered tone is appropriate.

**Access:** [x.ai/grok](https://x.ai/grok) or within the X platform.

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

**[arena.ai](https://arena.ai)** — The best current platform for side-by-side model comparison. Run the same prompt through two or more models at once and compare outputs instantly. No setup required; free to use.

Use Arena to:
- See which model handles your specific task better
- Develop personal intuition about tone and reasoning style differences
- Quickly benchmark a new model you haven't used before

---

## How to Choose

For most business professionals, the decision is simpler than it looks:

::::{grid} 1 2 2 3
:::{card} 🧠 Deep Analysis
Use **Claude Sonnet or Opus** for anything requiring nuanced reasoning, long-document work, or careful writing.
:::
:::{card} 📊 Google-First
Use **Gemini** when your work lives in Google Docs, Sheets, or Gmail — native integration is the differentiator.
:::
:::{card} ⚡ Speed & Volume
Use **Haiku or Flash** when you need fast, lightweight processing of many small tasks.
:::
::::

---

## Summary

:::{admonition} Key Takeaways — Chapter 1.3
:class: tip

1. Different models have different cognitive "temperaments" — understanding these helps you choose correctly.
2. The smartphone tier analogy applies: Frontier/Max, Balanced/Pro, and Fast/Standard serve different needs.
3. Claude excels at nuanced reasoning and long-context tasks. Gemini is best when integrated with Google Workspace. GPT-4o offers the largest third-party ecosystem.
4. Version numbers will change; the principles of model selection will not. Check drleee.io for current recommendations.
5. arena.ai is the fastest way to develop personal intuition about model differences.
:::

---

:::{tip} Try This
Go to **[arena.ai](https://arena.ai)** and run one real question through two different models at the same time. Pick any question you'd actually care about the answer to. Spend 90 seconds comparing the tone and depth of the two responses — that instinct you build is worth more than any review article.
:::
