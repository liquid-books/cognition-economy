# Chapter 6 Readings — Plan Mode: Think Before You Build
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Overview

This is the most counterintuitive chapter in the book. The most capable your AI is, the more damage it does when it heads in the wrong direction — because it produces sophisticated, polished, convincing work in entirely the wrong direction before you realize what happened. Plan Mode is the discipline that separates professionals who get great results from those who do a lot of impressive-looking work that misses the point.

## What You Will Learn

- The compounding error problem: why a small misalignment at the start of a complex AI task becomes an enormous one by the end.
- What Plan Mode actually is — a deliberate separation of the thinking phase from the doing phase, with explicit human approval between them.
- The Read-Only Toolkit principle: during planning, the AI can read, analyze, and question, but cannot produce.
- The plan-as-contract concept: when you approve a plan, you are agreeing on scope, sequence, assumptions, and what success looks like — not just saying "proceed."
- When to use Plan Mode (complex AND irreversible) and when to skip it (simple OR easy to redo).
- The Architect-and-Builder pattern — use the most powerful model for planning, the faster model for execution — and how it delivers planning-quality thinking at execution-speed cost.
- Deep Planning and multi-agent planning for genuinely high-stakes work.

## Chapter Summary

Chapter 6 opens with a paradox: faster AI makes the planning problem worse, not better. A slow tool that goes wrong wastes a little time before you correct it. A fast, highly capable tool that goes wrong produces 3,000 polished words of strategy built around the wrong customer profile — and tearing that down to start over costs more than if you had never started. This is the compounding error problem, and Dr. Lee names it as the single most common reason professionals feel frustrated with AI results despite using excellent tools.

The solution is **Plan Mode** — not a feature you turn on, but a practice you adopt. Before asking an AI to do anything significant, you ask it to **plan**, not execute. The instruction is simple: *"Think through this task out loud. What are you going to do, in what order, and why? What assumptions are you making? Show me your plan and wait for my approval before you begin."* The AI then externalizes its reasoning — its understanding of the task, its planned steps, its assumptions, what it does not know. You review, push back, correct, approve. Then it executes. The output, built on a scrutinized foundation, is dramatically better.

During planning, the AI is on a **read-only toolkit**: it can analyze, search, map dependencies, ask clarifying questions, propose sequences, and flag what it does not know — but it cannot write, build, or produce. This forces invisible decisions into the open where you can evaluate them. The chapter then introduces the **plan-as-contract** concept: approving a plan is not "looks good, go ahead." It is an explicit agreement on scope, sequence, assumptions, and success criteria. If execution diverges later, you can point back to the contract.

The chapter explains when to invoke Plan Mode — when complexity AND irreversibility are both present — and when to skip it (simple tasks, easy-to-redo outputs). Two professional patterns close the chapter. **Architect-and-Builder**: use your vendor's flagship reasoning model for the planning phase, then hand the approved plan to its faster, cheaper sibling for execution. You get the architect's judgment and the builder's throughput — every major vendor now ships a tiered lineup, so the pattern applies whatever the tiers are called this year. **Deep Planning and multi-agent planning**: for genuinely high-stakes work, the planning phase deserves its own project, multiple rounds of review, and specialized agents handling each step of the executed plan. The chapter analogizes to architects, surgeons, and pilots — none of whom would consider acting without filed, reviewed, approved plans.

The **Sagamore Capital Advisors** case study closes the chapter. An investment advisory firm rolled out AI for quarterly client reporting without designing a planning phase. The AI, asked to "write the Q2 market commentary section for Client X" with no explicit context about benchmarks, risk posture, or compliance language, filled the gaps with statistically plausible defaults. Across 16 reports, those defaults compounded into 17 compliance violations and 11 analyst-days of remediation — eating all of the pilot's promised time savings. The root cause was structural: the workflow moved directly from prompt to output with no planning phase between them.

## Why This Matters

Every high-stakes AI workflow you will ever build needs Plan Mode baked into it. Without it, you accumulate invisible technical debt — assumptions the AI made that you never confirmed — until the day a compliance officer, a client, or a board member surfaces them all at once. The Sagamore Capital Advisors case is not an outlier; it is the predictable consequence of skipping the planning phase in a high-stakes domain. Reading this chapter changes how you scope every significant AI request: from "write me X" to "plan how you would write X, wait for my approval, then execute."

For organizations deploying AI in regulated industries — financial services, healthcare, legal, regulated marketing — Plan Mode is not a best practice. It is a professional obligation, comparable to how architects file drawings, surgeons brief their teams, and pilots file flight plans. The chapter gives you the language and framework to require Plan Mode as part of your AI governance policy, and the case study provides the evidence to make the case to skeptical executives who view planning as overhead.

## How It Applies in Your Work

- **A consultant drafting a client deliverable** would use Plan Mode for every section where misalignment with the client's framing would cost rework. Ask Claude to plan the section — its structure, assumptions about the audience, the implicit framework — then push back on whatever sounds generic before approving execution.
- **A compliance officer at a regulated firm** would mandate Plan Mode for any AI-assisted client-facing document. The plan becomes the audit artifact — a record of what assumptions the AI was operating under when it produced the output, separable from the output itself.
- **A founder designing AI workflows** would use the Architect-and-Builder pattern to control cost without sacrificing quality. Planning conversations happen in the most expensive model; execution happens in the cheaper one. The savings on token volume are significant when workflows run hundreds of times a month.
- **A team lead supervising junior AI users** would establish a team norm: any output that takes more than 15 minutes to produce gets a Plan Mode review before execution. This eliminates the rework cycles that plague teams whose junior members are working fast but in subtly wrong directions.

## Read the Chapter

**→ [Chapter 6: Plan Mode — Think Before You Build](http://cognitioneconomy.net/ch06/)**

Read the full chapter at the link above before participating in the discussion board or completing the applied exercise for this module. The chapter is the primary content for this week — everything in the discussion and exercise draws directly from it.

*Estimated reading time: 20 minutes*

## What to Look For While Reading

As you read, pay special attention to:

- The compounding error analogy — the marketing strategy written for a 35-year-old middle manager when the actual customer is a 55-year-old C-suite executive. This is the cleanest example of why Plan Mode matters.
- The Read-Only Toolkit principle — during planning, the AI can look but cannot touch. The professionals who internalize this constraint produce far better outputs.
- The plan-as-contract framing — approving a plan is an agreement on scope, sequence, assumptions, and success criteria. The discussion prompt directly tests your understanding of this.
- The Sagamore Capital Advisors case — 17 compliance findings across 16 client reports, traced back to the absence of a planning phase. The case is the textbook example of what skipping Plan Mode costs in regulated industries.

---
*Canvas Reading Page — Chapter 6 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
