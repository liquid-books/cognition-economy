# Chapter 5 Readings — The Six Engineering Disciplines
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Overview

Everyone has heard of prompt engineering. Almost nobody knows there are five disciplines above it — and those are the ones that actually separate power users from everyone else. This chapter is the elevator from the lobby (prompting) to the top floor (harness engineering), and explains why two people with identical AI access can produce dramatically different outputs.

## What You Will Learn

- Why prompt engineering is real, valuable, and the *least* powerful of the six disciplines.
- The six-floor stack — Prompt Engineering → System Prompting → Meta Prompting → Context Engineering → Memory Engineering → Harness Engineering — and how each layer multiplies the value of the one below it.
- The four-component anatomy of a strong prompt: Task, Context, Format, Examples.
- Meta-prompting — using AI to write the instructions that AI will follow — and why it produces better instructions faster than writing them yourself.
- The three tiers of memory engineering (conversation, file-based, database) and how to build continuity into a stateless system.
- Harness engineering — designing the entire environment your AI operates in, including the workflows that run without you in the loop.

## Chapter Summary

Chapter 5 reframes 2023's "prompt engineer" job-title hype as the lobby of a six-story building. Writing a good prompt is the front door. The leverage — the compounding, structural, career-defining leverage — lives on the floors above. The chapter walks readers up the stack floor by floor.

**Floor 1, Prompt Engineering**, is the foundation: AI responds to specificity, and a well-engineered prompt covers four things — Task (the specific output you want), Context (what the AI needs to know to do it well), Format (how the output should be structured), and Examples (when precision matters, show one). **Floor 2, System Prompting**, is the standing brief that loads before every conversation, defining the AI's role, rules, tone, and standards. The executive-assistant analogy: a system prompt is the two-hour onboarding briefing that shapes every interaction that follows.

**Floor 3, Meta Prompting**, is the counterintuitive technique introduced in Chapter 2 and elevated here to a discipline. Using AI to write the instructions AI will follow sounds circular until you try it once — at which point it becomes how you do almost everything. The rule of thumb: if instructions will be used more than once, do not write them yourself. **Floor 4, Context Engineering**, addresses the deliberate management of what information enters a conversation, in what order, with what signal-to-noise ratio. More context is not better context. The order matters. And context degrades over a long conversation.

**Floor 5, Memory Engineering**, confronts AI's dirty secret: it does not remember you. Three layers solve this. Conversation memory is automatic (within a session). File-based memory is a one-page Working Brief that you maintain and attach at the start of sessions where continuity matters. Database memory (via Supabase from Chapter 3) is structured, queryable, persistent storage that enables genuinely autonomous workflows. **Floor 6, Harness Engineering**, is where everything composes. Not a single prompt, not a single skill — the entire ecosystem: tools connected, workflows defined, triggers that set things in motion, outputs routed to the right places. The example: a client email arrives → Gmail connector reads it → Drive searches prior documents → Calendar checks availability → AI drafts a reply in your voice → draft sits in your Gmail drafts folder for review. You appeared in the loop for thirty seconds at the end.

The chapter closes with the **Castellan Wealth Partners** case study: a wealth management firm with 22% AI utilization and frustrated senior advisors. The audit revealed the firm had deployed AI but stopped at Floor 1 — leaving the value on Floors 3 through 6 untouched. The consultant's phased rollout — refreshing prompt engineering, building a standardized system prompt, introducing meta-prompting and a Skills library, then context, memory, and finally a harness pilot — is the blueprint for any organization currently stuck on Floor 1.

## Why This Matters

This chapter is the strategic map for the second half of the book. Every later chapter (Plan Mode, Memory, Plugins, Sub-Agents, the SDK, Self-Learning Systems, Automations) is a specific application of one or more of the six disciplines. Without this map, the later chapters can feel like a disconnected list of techniques. With it, every technique slots into a clear architectural picture of how leverage actually compounds in knowledge work.

For organizations, the chapter reframes the AI adoption conversation from "are people using the tool?" (a Floor 1 question) to "how high up the stack have we built capability?" (the right question). The Castellan Wealth case is the diagnostic pattern most firms will recognize: high utilization, low satisfaction, generic outputs, advisors quietly returning to old workflows. The fix is not better training on prompting. The fix is building the missing layers — system prompts, skills, context protocols, memory architecture, and eventually harnesses. Each layer adds leverage that compounds with the others. Stopping at any single floor leaves most of the value on the table.

## How It Applies in Your Work

- **An individual professional** would use this chapter as a personal capability roadmap: spend one month on each floor, building one concrete artifact (a refined prompt template, a system prompt, three skills via meta-prompting, a context protocol, a Working Brief, and a draft harness design). Six months of disciplined practice produces a capability stack that 99% of professionals never build.
- **A head of operations or chief of staff** would use the six-floor framework to audit their organization's current state and identify the highest-ROI investment for the next quarter. Most organizations need to invest in Floors 2 and 3 (system prompts and meta-prompted skills) before attempting Floor 6 harnesses. Sequencing matters.
- **A consultant advising on AI strategy** would use the Castellan Wealth case as the diagnostic framework. The "we use AI but the outputs aren't great" complaint is almost always a Floor 1 ceiling problem. The recommendation is rarely "use it more"; it is "build the next floor."
- **A founder or product leader** would treat harness engineering (Floor 6) as the eventual destination — and recognize that the path there runs through every floor below it. A founder who tries to skip straight to autonomous workflows without building the system prompt, skills, context, and memory layers will get expensive, fragile automation that breaks the first time anything changes.

## Read the Chapter

**→ [Chapter 5: The Six Engineering Disciplines](http://cognitioneconomy.net/ch05/)**

Read the full chapter at the link above before participating in the discussion board or completing the applied exercise for this module. The chapter is the primary content for this week — everything in the discussion and exercise draws directly from it.

*Estimated reading time: 23 minutes*

## What to Look For While Reading

As you read, pay special attention to:

- The six-floor building metaphor — and the claim that most professionals never leave the lobby. Memorize the order: Prompt → System → Meta → Context → Memory → Harness.
- The four components of a strong prompt (Task, Context, Format, Examples) — this is the most concrete, actionable framework on Floor 1.
- The three tiers of memory (conversation, file-based, database) — Floor 5 is the layer most readers underinvest in, and the chapter's mini-tutorial on the Working Brief is the highest-ROI takeaway.
- The Castellan Wealth Partners case study — particularly the question of how to sequence a six-floor rollout when business pressure pushes for fast visible wins (Floors 1–2) but the real value sits on Floors 4–6.

---
*Canvas Reading Page — Chapter 5 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
