# Master Style Brief — The Cognition Economy
## For Chapters 9, 10, 11, 12, 13

---

## About the Book
**Title:** The Cognition Economy: A Business Person's Masterclass on AI
**Author:** Dr. Ernesto Lee
**Audience:** Business professionals, MBA students, operators, decision-makers. **NO TECHNICAL BACKGROUND ASSUMED. NOT DEVELOPERS.**
**Tone:** TED Talk energy delivered as a book. Arvin Ash style.
**Purpose:** Help readers stop *using* AI and start *redesigning work* around it.

---

## The Arvin Ash Style (MANDATORY — STUDY THIS)

Arvin Ash is a science communicator whose YouTube channel makes complex science feel obvious. His method, distilled:

1. **Open with a question or surprising fact** that creates cognitive dissonance. "If you could hire the smartest analyst alive for $20/month, would you?" Make the reader say "wait, really?"
2. **One dominant analogy per concept.** Not three. One. Pick the best and ride it.
3. **Short sentences. Short paragraphs.** No meandering prose. Two-line paragraphs are fine. One-line paragraphs hit harder.
4. **"Imagine..." and "Picture..." structures.** Always invoke a visual scenario.
5. **Always answer WHY before WHAT.** Tell them why they should care first. Then explain the mechanics.
6. **The aha-moment arc:** Setup → Vivid Analogy → Reveal → "Here's how to use this."
7. **Assume smart adults who haven't thought about this yet.** Never condescend. Never over-explain.
8. **Direct address.** Write to "you" the whole way through.
9. **Conversational authority.** State things directly. No academic hedging. No "it might be argued that..."
10. **Story-driven.** Open every section with a person, a moment, or a paradox.

**Read Arvin's "What is Time?" or "Why is the Speed of Light Constant?" for the rhythm. He makes physics PhDs feel obvious. We're doing that for AI for business.**

---

## REQUIRED CHAPTER STRUCTURE (Match ch08.md exactly)

### 1. YAML Frontmatter
```yaml
---
title: "Chapter N: [Full Title]"
short_title: "Chapter N: [Short Title]"
description: "[One sentence about what this chapter covers]"
label: chNN
tags: [relevant, tags, cognition-economy]
---
```

### 2. Opening Infographic
```
:::{figure} ../images/chNN-infographic.png
:label: fig-chNN-infographic
:alt: [Detailed alt text describing the concept visually]
:width: 80%
:align: center

*[Caption explaining the chapter's central metaphor]*
:::
```

### 3. Hook (150–250 words, NO epigraph quote needed)
A vivid scene or paradox that makes the concept concrete BEFORE you define it. Use a character, a number that surprises, a moment of realization. This is the TED-Talk opening.

### 4. Four to Six Main Sections (H2 headings, separated by `---`)

Each section MUST contain (in order):
- Opening paragraph that continues the narrative/analogy
- A figure reference: `:::{figure} ../images/chNN-X-[slug].png`
- Core explanation with ONE dominant analogy
- An `{admonition}` block with the KEY PRINCIPLE highlighted (tip/note/warning)
- A real-world business example (1-2 paragraphs)
- (Some sections) A `{list-table}` for comparisons OR `::::{grid}` for parallel concepts

Section headings should be clean H2 (e.g., `## What Sub-Agents Actually Are`), separated by horizontal rules (`---`).

### 5. Case Study (REQUIRED, 400–500 words)
Format:
```markdown
---

## Case Study: [Title — Named Company + Tension]

### Background
[150–200 words: Named company (fictional but realistic — name, location, size, industry), specific numbers, what they've been doing. Make it feel real.]

### The Situation
[150–200 words: The specific decision or challenge they face. Use concepts from THIS chapter. Multiple stakeholders. Genuine tension between competing priorities.]

### Discussion Prompt
[80–120 words: An MBA-style analytical question that requires applying chapter concepts to the case. Should reward substantive analysis, not just summary.]
```

### 6. Discussion Guidelines (verbatim from existing chapters)
```markdown
### Discussion Guidelines

**Initial Post** (due before class)
- Minimum **400 words**
- Directly address the discussion prompt using concepts from this chapter
- Include **at least one APA-formatted citation** — from the course text or a peer-reviewed source
- Avoid summary; demonstrate analysis and original thinking

**Peer Responses** (minimum 2)
- Minimum **250 words each**
- Each response must include **at least one APA-formatted citation**
- Engage substantively — build on, challenge, or offer a contrasting perspective grounded in evidence
- "I agree" or "Great post" responses do not meet the requirement
- Maintain a professional and respectful academic tone
```

### 7. Applied Exercise / Hands-On Lab (REQUIRED, ~500 words)

Title: `## Applied Exercise: [Action-Oriented Title]`

Then 5-7 numbered steps. ENTIRELY PROMPT-BASED. NO CODE. Each step:
- Names a tool (Claude Code, Antigravity 2.0 IDE)
- Gives a specific URL where applicable
- Tells the student EXACTLY what to type or click
- Produces something they keep (an artifact)

**Lab structure must include TWO PARALLEL TRACKS:**

```markdown
## Applied Exercise: [Title]

*Estimated time: 25–30 minutes. You'll produce [specific artifact].*

### Track A — Doing This in Claude Code

[5–7 step-by-step instructions. Cite https://code.claude.com/docs/en/[relevant-page]. No code.]

### Track B — Doing This in Google Antigravity 2.0 IDE

[Same exercise, done in Antigravity 2.0 IDE's Agent Manager surface. Cite https://antigravity.google/docs/ide-overview. No code.]

### Reflection
[2–3 sentences asking the student to write what they noticed about how the two tools handled the same task.]
```

---

## GOOGLE ANTIGRAVITY 2.0 IDE — GET THIS RIGHT

**Important:** Google has TWO Antigravity products. We are using the **Antigravity IDE** (developer-focused, current version 2.0). NOT the standalone "Antigravity 2.0" desktop app (which is separate).

**Antigravity 2.0 IDE** (https://antigravity.google/docs/ide-overview)
- Agentic development platform — VS Code-based AI IDE
- Three core surfaces:
  - **Agent Manager** — "no-code" orchestration view. This is what business users use. Birds-eye view of multiple agents working across workspaces. Toggle to it with `CMD+E` (Mac) or `CTRL+E` (Windows).
  - **Editor** — Full VS Code-based IDE (one workspace at a time)
  - **Browser** — Built-in browser the agent can read/actuate (for UI testing, dashboards, etc.)
- Three AI modalities inside the Editor: **Agent** (the main one), **Tab** (autocomplete), **Command** (inline)
- **Artifacts** — Anything the agent creates: markdown files, diff views, diagrams, browser recordings
- **Asynchronous agents** — Multiple agents work in parallel across workspaces
- Free during preview. Available macOS / Windows / Linux.

**The Agent Manager surface is the business-user entry point.** When the lab says "in Antigravity 2.0 IDE," it means: open the IDE, press CMD+E to switch to Agent Manager, type your task in plain English, and watch the agent work. Review the Artifacts it produces.

---

## QUIZ FORMAT (CRITICAL — ONE FILE)

File: `/home/node/openclaw/books/cognition-economy/quizzes/quiz-chNN.md`

The quiz file contains BOTH questions AND answers in the same file. Answers hidden inside `<details>` blocks. **DO NOT create a separate answer key file.** The quiz lives only on GitHub (not in the rendered book).

Format:
```markdown
# Quiz: Chapter N — [Chapter Title]

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

[Question text testing CONCEPT understanding]

- A) [Option]
- B) [Option]
- C) [Option]
- D) [Option]
- E) [Option]

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ [Specific explanation of why wrong — reference chapter text]
- ⭐ B) ✅ [Explanation of why correct — quote the chapter directly]
- C) ❌ [Specific explanation]
- D) ❌ [Specific explanation]
- E) ❌ [Specific explanation]

</details>

---
```

Rules:
- **10 questions total**
- Each question has 5 options (A–E)
- 3–4 questions should be "Which TWO statements correctly describe..." (two correct answers)
- ⭐ marks each correct answer
- Each wrong-answer explanation should explain SPECIFICALLY why it's wrong, referencing the chapter
- Each correct-answer explanation should QUOTE the chapter text
- Questions test understanding, not trivia
- End with: `*Quiz for Chapter N — The Cognition Economy © Dr. Ernesto Lee, 2026.*`

---

## WORD COUNTS

- **Main chapter content (sections 1–4 of structure above): 4,500–5,000 words**
- Case study: 400–500 words
- Applied exercise: 400–600 words
- **Total file size: roughly 6,000–6,500 words**

Count carefully. The previous attempts came in under 4,500 — DO NOT REPEAT THAT.

---

## ADMONITION CLASSES

- `{admonition} Title\n:class: tip` — Practical takeaways, positive guidance
- `{admonition} Title\n:class: note` — Important context, clarifications
- `{admonition} Title\n:class: warning` — Common mistakes, what to avoid
- `{admonition} Title\n:class: important` — Critical concepts that MUST be internalized

Each main section should have AT LEAST ONE admonition.

---

## FILE LOCATIONS (WRITE ONLY THESE)

- Main chapter: `/home/node/openclaw/books/cognition-economy/chapters/chNN.md`
- Quiz: `/home/node/openclaw/books/cognition-economy/quizzes/quiz-chNN.md`

**TWO files per chapter. That's it. No separate answer key.**

---

## TONE GUARDRAILS — DO / DON'T

✅ DO:
- "Picture a manager who just hired her first AI assistant..."
- "Here's the counterintuitive thing about sub-agents..."
- "This sounds complicated. It is not."
- "Most people get this wrong. Don't be most people."
- Use specific numbers ($23M, 40%, 3.2 seconds)
- Name real-feeling companies and people

❌ DON'T:
- "In this chapter, we will explore..." (don't announce structure)
- "It is important to note that..." (just say it)
- Long multi-clause academic sentences
- ANY code examples (this is not a developer book)
- Generic placeholders ("a company," "a manager") — always name them
- Hedge language ("perhaps," "it could be argued")

---

## SOURCE MATERIALS (PRE-FETCHED)

All source docs are saved to `/home/node/openclaw/books/cognition-economy/.sources/`:
- `ch09-claude-sub-agents.md`
- `ch10-claude-agent-teams.md`
- `ch10-claude-goal.md`
- `ch11-claude-agent-sdk.md`
- `ch13-claude-hooks.md`
- `ch13-claude-channels.md`
- `claude-quickstart.md`
- `antigravity-ide-overview.md`
- `antigravity-agent-manager.md`
- `antigravity-agent-side-panel.md`

READ THESE before writing your chapter. Do not re-fetch from the web.

---

## REFERENCE CHAPTERS (Read these to internalize tone)

- `/home/node/openclaw/books/cognition-economy/chapters/ch08.md` — best recent example, match its structure exactly
- `/home/node/openclaw/books/cognition-economy/chapters/ch07.md` — solid example of memory/learning chapter
- `/home/node/openclaw/books/ai-business-innovation-grad/quizzes/quiz-ch01.md` — quiz format reference

---

## FINAL CHECKLIST (run this before declaring done)

- [ ] Chapter is between 4,500–5,000 words of body content
- [ ] Opening hook is a vivid scene, NOT an announcement of what's coming
- [ ] Every section opens with a story, a number, or a paradox
- [ ] One dominant analogy per concept
- [ ] Short sentences and short paragraphs throughout
- [ ] Zero code examples anywhere
- [ ] Every section has a figure reference and at least one admonition
- [ ] Case study has a named company with specific numbers
- [ ] Applied Exercise has BOTH Track A (Claude Code) AND Track B (Antigravity 2.0 IDE / Agent Manager)
- [ ] Quiz has 10 questions, all in ONE file with answers in `<details>` blocks
- [ ] No separate answer key file created
- [ ] Quiz includes 3–4 "Which TWO" questions
- [ ] Every correct answer quotes the chapter
- [ ] File saved to `/home/node/openclaw/books/cognition-economy/chapters/chNN.md`
- [ ] Quiz saved to `/home/node/openclaw/books/cognition-economy/quizzes/quiz-chNN.md`
