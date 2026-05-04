---
title: "Context: The Working Memory of the AI"
subtitle: "The Beam, Made Concrete"
short_title: "Context"
description: "Context is everything the model can see right now — and understanding what lives inside it is the foundation of effective AI work."
label: ch01-6
tags: [ai, business, cognition-economy, chapter-1]
---

# Context: The Working Memory of the AI

:::{figure} ../images/ch01-6-infographic.png
:label: fig-ch01-6-infographic
:alt: Infographic showing the layers of context in an AI conversation — system prompt, conversation history, attached files, tool results — arranged as concentric rings or stacked layers
:width: 80%
:align: center

*Context is the AI's working memory: everything the model can see right now, structured in layers.*
:::

In Chapter 1.2, you met the Flashlight Theory — context is the beam, and the model can only reason about what the beam illuminates. Now it is time to open the flashlight and look inside.

Context is not a vague concept. It is a specific, structured collection of information that gets loaded into the model's working memory for a given session. Understanding what it contains — and what controls each layer — is what separates casual users from professionals.

---

## The Model Does Not Remember. It Re-Reads.

This is the most important thing to understand about how AI memory works: **the model has no persistent memory between sessions**. When you close a conversation and open a new one, the model starts with a completely blank slate.

What *feels* like memory — the model knowing what you discussed earlier in a conversation — is not memory in the human sense. It is re-reading. Every time you send a message, the model reads the entire conversation history from the beginning, as if seeing it for the first time.

:::{admonition} The Re-Reading Model of Memory
:class: note

Think of the model not as a person who remembers your previous conversations, but as an exceptionally fast reader who re-reads every document in the stack before responding to your latest question.

What you put in the stack determines what it "knows." Nothing you said in a different conversation — or even in a different chat session today — is available unless you explicitly include it.
:::

This has a practical implication that most users miss: **context is not automatic continuity. It is deliberate construction.**

---

## What Lives Inside the Context

At any given moment in a conversation, the model's context contains some combination of the following layers:

::::{grid} 1 1 2 2
:::{card} 🔧 System Prompt
Standing instructions that set the model's role, behavior, tone, and rules for the session. In tools like Claude Projects or custom GPTs, this is set once and persists across all conversations in that project. You don't see it in the chat, but the model does.
:::
:::{card} 💬 Conversation History
Everything that has been said in the current session — your messages and the model's responses — in sequence. This grows with every exchange.
:::
:::{card} 📎 Attached Files
Documents, spreadsheets, PDFs, images, or code files you have explicitly added to the conversation. These are parsed and added to the context in full.
:::
:::{card} 🔌 Tool Results
When the model has access to external tools — search, database queries, connected services via MCP — the results of those tool calls are also injected into the context.
:::
::::

Everything in this list is part of the beam. Everything outside it is darkness.

---

## A Practical Example: The Analyst and the Report

An analyst is preparing a quarterly business review. She needs the model to reason about her company's Q3 performance data. Without context, the model knows nothing — it has no access to her company's numbers, her industry benchmarks, or her internal targets.

She uploads the Q3 report (50 pages, pasted as text into the conversation). Immediately, the model can reason about Q3 data. She also pastes in a competitor's public earnings release. Now the model can compare. She adds a note specifying that her audience is the executive team and that she needs the tone to be direct and data-forward.

The context now contains:
- Her role and the output goal (typed instruction)
- The Q3 internal report (attached file)
- The competitor earnings release (pasted text)
- The audience and tone specification (explicit instruction)

The output she receives is specific, comparative, and appropriately styled — because the flashlight beam is fully illuminated.

---

## The Hierarchy of Context: What Gets Prioritized

Not all context elements carry equal weight in how the model processes them. Research and practical experience suggest a rough priority order:

```{list-table} Context Priority Hierarchy
:header-rows: 1
:widths: 20 45 35

* - Priority
  - Element
  - Practical Implication
* - **Highest**
  - Explicit instructions stated clearly and near the current message
  - Put your most important requirements close to your question
* - **High**
  - System prompt (if set)
  - Use project-level system prompts for standing rules and role definitions
* - **Medium**
  - Recent conversation history
  - Recency matters — things said recently carry more weight than messages far back
* - **Lower**
  - Early conversation history and large attached documents
  - Critical information buried in the middle of long contexts may be underweighted
* - **Variable**
  - Tool results
  - Depends on placement and how the tool result is formatted in context
```

This hierarchy is not absolute — frontier models are increasingly sophisticated about long-context processing — but it is a reliable guide for structuring important information in your prompts.

---

## Context as a Design Problem

Here is the shift that changes how you work: stop thinking of a conversation as a dialogue and start thinking of it as **a document you are constructing for the model to read**.

When you design a conversation this way, different questions arise:

- What does the model need to see to give me the best output?
- Is the most important information near the top, or buried in a long preamble?
- Have I specified my role, my goal, and my constraints explicitly?
- Are the documents I've included actually relevant, or am I cluttering the beam?

This design mindset — the editor's mindset — is the subject of Chapter 1.8 (Context Engineering). For now, hold the core idea: context is something you construct, not something that happens automatically.

---

## Summary

:::{admonition} Key Takeaways — Chapter 1.6
:class: tip

1. The model has no persistent memory. It re-reads the full context on every message.
2. Context contains four main layers: system prompt, conversation history, attached files, and tool results.
3. What is not in the context does not exist for the model. Context is deliberate construction.
4. Explicit, specific instructions placed near your question carry the most weight.
5. Think of a conversation as a document you are designing for the model to read — not a dialogue that happens automatically.
:::

---

:::{tip} Try This
Think about the last time an AI gave you a disappointing answer. Now ask: what was actually in the context when you asked? Was your role specified? Was the relevant document included? Was your goal stated explicitly? Chances are, something important was missing from the beam.
:::
