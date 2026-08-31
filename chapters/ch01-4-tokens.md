---
title: "Tokens: The Atoms of Machine Language"
subtitle: "How AI Models Actually Read Text"
short_title: "Tokens"
description: "Tokens are the fundamental unit of AI language processing — not words, not characters, but chunks — and understanding them changes how you work."
label: ch01-4
tags: [ai, business, cognition-economy, chapter-1]
---

# Tokens: The Atoms of Machine Language

:::{figure} ../images/ch01-4-infographic.png
:label: fig-ch01-4-infographic
:alt: Infographic showing how text is broken into tokens — words, subwords, and characters — with the strawberry example and a token-to-word ratio guide
:width: 80%
:align: center

*Tokens are the atoms of machine language: not words, not characters, but chunks that models actually process.*
:::

The word "understanding" does not mean anything to a language model. Neither does "business" or "strategy." What the model actually processes is a sequence of numbers — each number representing a small chunk of text called a **token**.

This distinction sounds technical, but it has immediate, practical consequences for how you write prompts, estimate costs, and understand what the model is doing when it responds to you.

---

## What a Token Is

A token is roughly 3–4 characters of text, on average. That works out to approximately three-quarters of a typical English word. It is not a word. It is not a letter. It is a statistical chunk that the model's vocabulary was trained to recognize as a meaningful unit.

In practice, common words tend to be single tokens. Unusual, long, or compound words often split into multiple tokens. Punctuation, spaces, and special characters each consume tokens too.

Here is a rough rule of thumb that will serve you throughout this book:

:::{admonition} The Token Rule of Thumb
:class: tip

**\~750 words ≈ 1,000 tokens**

A typical business email (200 words) ≈ 270 tokens.  
A one-page memo (500 words) ≈ 670 tokens.  
A 10-page report (2,500 words) ≈ 3,300 tokens.
:::

This approximation will not be exact for every document — code, tables, and non-English text tokenize differently — but it is close enough for planning and cost estimation.

---

## The Strawberry Problem

For a period, language models famously failed a simple test: counting the letters in the word "strawberry." A model would confidently state that "strawberry" contains two R's when it contains three.

This was a tokenization artifact. The model does not read "s-t-r-a-w-b-e-r-r-y" as individual letters. It reads it as one or two tokens — a chunk — and was not directly processing the character-level content the way a human would when counting.

:::{admonition} Why This Matters Beyond Strawberries
:class: note

This example illustrates a broader point: the model does not process text the way you do. It processes tokens. This means that tasks requiring precise character-level analysis — counting specific letters, detecting exact spacing, parsing raw character strings — are harder for models than tasks requiring semantic understanding.

For the work in this book, you will almost never hit this limitation. But knowing it exists helps you understand *why* models occasionally stumble on what seem like trivial tasks.
:::

Modern frontier models have improved significantly on character-level tasks, partly through chain-of-thought reasoning that effectively makes the model "spell out" what it is analyzing. But the underlying tokenization architecture remains.

---

## Why Tokens Are Your Business Unit

Tokens are how AI providers measure and charge for usage. You are not paying per question. You are paying per token — for every token sent to the model (input) and every token the model generates in response (output).

This reframes how you think about your prompts. A prompt is not just a question — it is an expenditure. A conversation is not just a dialogue — it is a running tab.

```{list-table} Token Cost Awareness — Rough Reference Points
:header-rows: 1
:widths: 40 30 30

* - Content
  - Approximate Words
  - Approximate Tokens
* - A tweet
  - 30
  - 40
* - A business email
  - 200
  - 270
* - A one-page brief
  - 500
  - 670
* - A 10-page report
  - 2,500
  - 3,300
* - A full book chapter
  - 5,000
  - 6,700
* - A typical contract (15 pages)
  - 7,500
  - 10,000
```

None of these figures should alarm you — even a 15-page contract's worth of tokens costs a small fraction of a dollar to process. But the *pattern* matters as your usage scales, and understanding the unit helps you make informed decisions about prompt length, document inclusion, and conversation management.

---

## Tokens Across Languages

One important nuance: tokenization is not language-neutral. English text is typically the most efficient — it was heavily represented in the training data that shaped most tokenizers. Other languages, particularly those with non-Latin scripts (Chinese, Arabic, Japanese, Korean), often require more tokens to represent the same amount of information.

A sentence in English might consume 15 tokens. The equivalent sentence in Japanese might consume 30–50 tokens, depending on the model and tokenizer.

If you are doing significant work in non-English languages — or with multilingual documents — factor this into your token estimates. The cost per unit of meaning will be higher.

---

## Seeing Tokens in Action

The fastest way to build an intuition for tokenization is to see your own text broken apart. OpenAI's tokenizer tool lets you paste any text and watch it get chunked in real time — with each token highlighted in a different color.

This is not an abstract exercise. Once you have seen how your own sentences tokenize, you start to develop a feel for what makes prompts efficient — and which habits (unnecessary preambles, redundant restatements, verbose throat-clearing) are burning tokens without adding value.

---

## Summary

:::{admonition} Key Takeaways — Chapter 1.4
:class: tip

1. A token is approximately 3–4 characters, or roughly three-quarters of an English word.
2. The rule of thumb: \~750 words ≈ 1,000 tokens.
3. The "strawberry problem" illustrates that models process chunks, not characters — a real but limited constraint.
4. Tokens are the business unit of AI: you pay per token, so understanding token volume helps you manage cost and efficiency.
5. Non-English languages typically require more tokens per unit of meaning than English.
:::

---

:::{tip} Try This
Open a tokenizer tool (OpenAI publishes a free one; the current link is at **drlee.io/ch01**) and paste in the last email you wrote. Watch how it breaks into tokens. Notice which words split into multiple pieces — that is your text as the model actually reads it.
:::
