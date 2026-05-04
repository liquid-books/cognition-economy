---
title: "Context Engineering"
subtitle: "Curation Is the Highest-Leverage Skill in the AI Era"
short_title: "Context Engineering"
description: "Context engineering is the art of putting the right information in front of the model at the right time — and it matters more than prompting."
label: ch01-8
tags: [ai, business, cognition-economy, chapter-1]
---

# Context Engineering

:::{figure} ../images/ch01-8-infographic.png
:label: fig-ch01-8-infographic
:alt: Infographic illustrating context engineering — the signal-to-noise concept, the three rules of context curation, and the editor vs. prompter framing with a before/after prompt comparison
:width: 80%
:align: center

*Context engineering: signal-to-noise curation, the three rules, and the editor's mindset.*
:::

Everyone focuses on the prompt. The better leverage is in everything *around* the prompt.

Prompt engineering — crafting clever, well-structured questions — is a real skill. But it is downstream of something more important: what information you have placed in the context before asking. You can write the world's best question and still get a mediocre answer if the model is looking at the wrong documents, missing your constraints, or drowning in irrelevant background.

Context engineering is the discipline of deciding what goes in, what stays out, and in what order — before you even start typing your question.

---

## The Signal-to-Noise Problem

Adding more context is not the same as adding better context. The model has to process everything you put in front of it. Irrelevant, redundant, or poorly organized material does not just fail to help — it actively dilutes the quality of the response by competing with what actually matters.

:::{admonition} More Context ≠ Better Answers
:class: warning

Think of it like a briefing package for a consultant. If you hand them a tight, well-organized five-page brief with exactly what they need, they can do excellent work. If you dump a filing cabinet on their desk — 400 pages of loosely related documents — they will spend most of their time filtering noise, and their output will reflect that.

The model is the same. A well-curated 500-token context often outperforms a bloated 5,000-token context with the same information buried in it.
:::

The goal is high signal-to-noise ratio. Every element in the context should be there for a reason. If you cannot articulate why a document or paragraph is included, cut it.

---

## The Three Rules of Context Engineering

These three principles will improve the quality of your AI outputs immediately. Apply them before any complex or important task.

::::{grid} 1 1 1 3
:::{card} Rule 1: Lead With What Matters Most
The most important information — your goal, your constraints, the most critical section of a document — goes first. Not after a long preamble. Not buried. First.
:::
:::{card} Rule 2: Cut Anything You Wouldn't Read Yourself
If a document, paragraph, or background section would not meaningfully change your own understanding of the task, it will not meaningfully help the model either. Remove it.
:::
:::{card} Rule 3: Keep the Goal at the Top
State what success looks like before you dive into background. The model should know where it is going before it starts reading.
:::
::::

These rules map directly to the lost-in-the-middle findings from Chapter 1.7. The model attends most strongly to what appears early and what appears close to the question. Structure your context accordingly.

---

## The Editor vs. the Prompter

Here is the most useful reframe in this entire chapter:

**The person who gets the best AI outputs is not the best prompt writer. It is the best editor.**

An editor does not just know how to ask good questions. An editor knows what to include, what to cut, and how to organize material so that the most important things are visible. An editor reads the full context before sending it, the way you would read a brief before handing it to a colleague.

:::{admonition} The Editor's Checklist
:class: tip

Before sending any complex prompt, quickly run through these:

- [ ] Is my goal stated clearly at or near the top?
- [ ] Have I cut documents or sections that are not directly relevant?
- [ ] Is the most critical piece of information placed close to my question?
- [ ] Have I specified my constraints (audience, length, tone, format)?
- [ ] Is there anything in this context that would *mislead* the model — outdated data, irrelevant examples, conflicting instructions?
:::

The checklist takes 30 seconds. For important tasks, it routinely produces better outputs than any prompt-engineering trick.

---

## A Practical Rewrite

Here is a before-and-after that demonstrates the three rules in action.

::::{grid} 1 1 2 2
:::{card} ❌ Before (Common Pattern)
*"Hi! I'm working on a strategic planning document for my company. We're a mid-size SaaS company in the HR tech space. We've been around for about 7 years. We have about 85 employees. Last year was tough because of the market. Anyway, I was wondering if you could help me think through some things. Here is a very long document I've been putting together... [2,000 words of disorganized notes]. Based on all this, what should my Q4 priorities be?"*
:::
:::{card} ✅ After (Context-Engineered)
*"Goal: I need clear Q4 strategic priorities for my SaaS HR tech company.*  
*Context: 85 employees, 7-year-old company, difficult 2024 due to market contraction.*  
*Constraints: Output should be three priorities max, written for the executive team, with one-sentence rationale for each.*  
*Below is the relevant section of our current strategy doc:*  
[Excerpt: the 300 most relevant words, not the full 2,000]*  
*Given this, what are the three highest-leverage Q4 priorities?"*
:::
::::

Same underlying information. Dramatically different quality of output — because the context is curated, ordered, and constrained.

---

## When Context Engineering Is Worth the Effort

For quick, simple tasks — "summarize this paragraph" or "fix the grammar in this sentence" — context engineering is overkill. Just ask.

For tasks that matter — strategic documents, important communications, complex analysis, anything you would normally spend significant time on — the investment in context engineering pays dividends. Five minutes of curation before a complex prompt often saves thirty minutes of iterating on mediocre outputs.

The rule of thumb: if you care about the output quality, spend time on the input quality first.

---

## Summary

:::{admonition} Key Takeaways — Chapter 1.8
:class: tip

1. More context is not better context. Signal-to-noise ratio is what matters.
2. The three rules: lead with what matters most, cut anything you wouldn't read yourself, keep the goal at the top.
3. The best AI outputs come from the best editors, not the best prompt writers.
4. Run the editor's checklist before any important prompt: goal stated, irrelevant material cut, constraints specified.
5. Context engineering is most valuable for high-stakes outputs; for quick tasks, just ask.
:::

---

:::{tip} Try This
Take a prompt you are about to send — or one you sent recently that got a mediocre response — and apply Rule 1 before sending it: move your actual goal or question to the very first sentence. No preamble, no background first. Just the goal. Then add context below. Send it and compare.
:::
