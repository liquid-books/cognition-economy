# Applied Exercise — Chapter 16: Basal-Cognitive Architecture — The Future Operating Model
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Diagnose Your Architecture and Sketch the Tissue Version

*Estimated time: 30–40 minutes. You'll produce two artifacts — a written diagnostic of one of your current workflows scored against the six dimensions of basal-cognitive architecture, and a one-page sketch of what that same workflow would look like if you redesigned it as a tissue.*

This is the book's closing lab. Use it to convert everything you have learned into a single, concrete redesign you can take into your next quarter. Pick a workflow you actually run today — something with three or more handoffs, something that currently feels brittle, something where you suspect there is a better architecture but you have not had the language to describe it. Now you have the language.

**Before starting either track**, if you have not already worked through the Claude Code quickstart, start there: [https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart).

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code:** For students using Claude Code. Reference the quickstart at code.claude.com/docs/en/quickstart.
- **Track C — Antigravity 2.0 IDE:** For students using the Antigravity 2.0 IDE Agent Manager. Reference antigravity.google/docs/ide-overview.
:::

### Track A — Claude Desktop

*Estimated time: under 10 minutes. The capstone, done in one conversation.*

This is the business-friendly default — and the most important Track C exercise in the book. You will design the tissue version of a real workflow without writing a single line of code or configuring a single agent. The capstone is conceptual, not technical.

1. Open Claude Desktop (download from [claude.ai/download](https://claude.ai/download)) or use [claude.ai](https://claude.ai) in your browser.

2. Describe one workflow you currently run as a **hierarchy** — you assign tasks, you check back, you review outputs, you redirect. Pick something real: a weekly client deliverable, a hiring funnel, a content pipeline. Name the steps, the handoffs, and where you personally sit in the loop.

3. Ask Claude: *"Redesign this workflow as a 'tissue' — a set of peer units with local decision-making and no central coordinator. What would each unit be? What would its decision boundary be? How would they sync without a manager in the loop?"*

4. Then ask: *"Run the six-perturbation robustness test on this new design. For each perturbation, tell me whether the tissue or the hierarchy holds up better."*

5. Save both outputs. Read them side by side. You now have a capstone artifact: a current architecture, a redesigned architecture, and a head-to-head robustness comparison. This IS the diagnostic from the chapter — and the closing lab of the book.

**Your Submission:** Your submission is the tissue redesign of your chosen workflow — Claude's redesign description plus the six-perturbation robustness test results — plus your capstone reflection. Copy the redesign and test results into a document. Underneath them, write your capstone reflection (150-200 words): what is the single most important thing you are taking from this book into your professional practice? This reflection is your capstone submission. Submit the redesign + robustness test + capstone reflection.

### Track B — Claude Code

1. In a plain text editor, write a one-page description of the current workflow you have chosen. Name the steps. Name the handoffs. Name the people or agents involved at each step. Name where the cognitive bottleneck currently lives. Be specific — generic descriptions will produce generic redesigns.

2. Open Claude Code. Paste your workflow description and ask: *"Score this workflow on the six dimensions of basal-cognitive architecture — composability, locality, resilience, observability, evolvability, and alignment. For each dimension, give me a score from 1 to 5 and explain what evidence in my description supports the score."*

3. Read Claude's diagnostic carefully. Push back where you disagree. The goal is not to receive a verdict — it is to develop your own architectural intuition by arguing with a partner who has read every word of the framework.

4. Now ask: *"Based on this diagnostic, sketch the tissue version of this workflow. Show me the peer agents, the shared task list, the cognitive light cone of each agent, and the points of human judgment. Make zero assumptions about my current org chart — design the workflow as if I were starting from scratch."*

5. Save Claude's response as your "tissue sketch." Read it next to your original workflow. Identify the three biggest structural changes. Write a single paragraph explaining which of the three you would actually implement first, and what would have to be true about your organization for that implementation to succeed.

**Your Submission:** Your submission is Claude Code's six-dimension diagnostic for your workflow, the tissue redesign you built from it, and your capstone reflection. Copy the diagnostic and redesign into a document. Underneath them, write your capstone reflection (150-200 words): looking back at the 200-word redesign sketch you wrote in Module 0, how has your thinking about redesigning work evolved over the course of this book? What would you change in that sketch today? Submit the diagnostic + redesign + capstone reflection.

### Track C — Antigravity 2.0 IDE

1. Open Antigravity 2.0 IDE. Press `CMD+E` (Mac) or `CTRL+E` (Windows) to switch to the Agent Manager surface — the orchestration view that lets you set up multi-agent work without code. Reference the IDE overview at [https://antigravity.google/docs/ide-overview](https://antigravity.google/docs/ide-overview) if you need orientation.

2. Create a new Project that represents a single "tissue unit" — the smallest unit of your workflow that could be done by a single team of peer agents. In the project description, deliberately do *not* name an orchestrator. Instead, write: *"This project is run by three peer agents — a Sensing Agent, a Decision Agent, and a Communication Agent — sharing a single task list. There is no central controller. Each agent picks up the next task it is qualified to handle and writes back what it did."*

3. In the task description box, paste a real piece of work from the workflow you are redesigning. Use a task where you would normally route through a manager or an orchestrator. Then start the project and watch the three agents pick up the work asynchronously.

4. As the agents work, observe the Artifacts panel. Note which agent picked up which sub-task, how they communicated through the shared task list, and where (if anywhere) the absence of an orchestrator caused the work to slow or stall. This is your first empirical look at how a tissue architecture actually behaves in production.

5. At the end, save the Project as a template for the tissue unit. Write a two-paragraph reflection: where did the tissue architecture outperform the hierarchical equivalent you have been running, and where did it underperform? This reflection is your second artifact.

**Your Submission:** Your submission is the three-peer-agent Project configuration you built in Agent Manager — the Project Description with no named orchestrator — plus the task output from running real work through it, plus your capstone reflection. Copy the Project Description and task output into a document. Underneath them, write your capstone reflection (150-200 words): what does "Go build the reef" mean to you, specifically, in your professional context? What is the reef you are going to build? Submit the Project configuration + task output + capstone reflection.

### Reflection

Write three to four sentences capturing what you noticed about how the two tools handled the same architectural redesign. Did one feel more like a thinking partner and the other more like an operating system? Which surface made the tissue architecture feel inevitable, and which made it feel optional? And, most importantly: which of the two will you actually return to next quarter when you start the real restructure?

---
*Applied Exercise for Chapter 16 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
