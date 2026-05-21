---
title: "The Two Mental Models You Will Carry Through This Book"
short_title: "Two Mental Models"
description: "LLM as pure IQ (180 vs Einstein's 160) and the Flashlight Theory by Matty Squarzoni."
label: fm-two-mental-models
---

# The Two Mental Models You Will Carry Through This Book

Before Chapter 1, before the setup, before anything else — you need two ideas. Everything in this book is downstream of them. Once they click, the rest of the content will feel like applications of something you already understand.

---

## Mental Model #1 — LLM = Pure IQ

Here is the most important thing you can internalize about a large language model:

**It is intelligence. It is not knowledge.**

This sounds simple. It is not. Most people get it backwards.

When people first use a system like Claude or Gemini, they treat it like a search engine — they ask it questions and expect it to retrieve facts from some vast internal database. Sometimes that's right. Often it isn't. Models hallucinate, confabulate, and confidently state things that are wrong. This confuses people who expected knowledge.

Here is the correct frame: think of a frontier LLM as a person with an IQ of roughly 180. Einstein is estimated at around 160. These models sit above that threshold. They reason at a level that would be considered genius by any human standard.

But here is the catch — this person has amnesia. Every time you open a new conversation, they wake up with no memory of you, your project, your company, or your context. What they *do* have is intact: the reasoning, the synthesis, the pattern-matching across enormous conceptual territory. The intelligence is always there. The knowledge only comes from what you put in front of them.

This reframe changes your behavior immediately. You stop asking "does it know this?" and start asking "what do I need to *tell* it?" You stop being frustrated when it gets facts wrong and start thinking like a briefer — what does my 180-IQ analyst need to know before I ask the question?

**Intelligence is what the model brings. Knowledge is what you bring.**

That distinction, consistently applied, is worth more than any prompt trick in any tutorial you will ever watch.

---

## Mental Model #2 — The Flashlight Theory

*(Credit: Matty Squarzoni)*

Now take that 180-IQ person and put them in a pitch-black room.

Ask them: "What's on the desk?"

They cannot answer. Not because they aren't brilliant. Not because they don't know what desks usually have on them. But because **they cannot see anything**. They are reasoning in the dark, and reasoning in the dark produces hallucination — confident-sounding guesses based on what's usually true rather than what's actually here.

Now hand them a flashlight. Ask the same question. They look. They describe exactly what's there — the papers, the coffee cup, the sticky note in the corner.

Ask a follow-up question. They look again with the same beam. They're still as smart as before. Now they're also accurate.

**That flashlight is context.** And context, in an LLM interaction, is everything you include in your conversation window: your instructions, your documents, your examples, your constraints, your history.

Every technique in this book — prompt engineering, memory systems, retrieval-augmented generation, agent tools, sub-agent design — is, at its core, a method for aiming a better flashlight. Some techniques widen the beam. Some sharpen it. Some let the model hold the flashlight itself and move it around. But they are all variations on the same fundamental operation: *give the intelligence something real to see*.

The failure modes become obvious once you have this model. A model that hallucinates is usually a model working in the dark. A model that gives generic answers is usually a model seeing a generic question. A model that seems to "forget" things mid-conversation is usually a model whose context window has rotted or overflowed.

Fix the flashlight. Fix the output.

---

## Why These Two Ideas Matter Together

The IQ model tells you what the system *is*. The Flashlight Theory tells you how to *work with it*.

Together, they produce a specific posture: **respect the intelligence, own the context**. Don't ask it questions it can't answer without briefing. Don't be surprised when it's wrong about things you didn't tell it. Treat it like the world's best analyst on day one of a new engagement — brilliant, but starting cold.

Your job as an operator, a designer, a builder, is to build the systems that keep the flashlight well-aimed and the context rich.

Every module in this book is teaching you how to do that better.
