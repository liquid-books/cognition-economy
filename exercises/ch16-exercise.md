# Applied Exercise — Chapter 16: Basal-Cognitive Architecture — The Future Operating Model
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Diagnose Your Architecture and Sketch the Tissue Version

*Estimated time: 30–40 minutes. You'll produce two artifacts — a written diagnostic of one of your current workflows scored against the six dimensions of basal-cognitive architecture, and a one-page sketch of what that same workflow would look like if you redesigned it as a tissue.*

This is the book's closing lab. Use it to convert everything you have learned into a single, concrete redesign you can take into your next quarter. Pick a workflow you actually run today — something with three or more handoffs, something that currently feels brittle, something where you suspect there is a better architecture but you have not had the language to describe it. Now you have the language.

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace built for running several agents at once (Track C). Track C is the book's capstone build — the only exercise where you construct the tissue architecture this chapter argues for and run real work through it. Product names, download links, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch16-companion.
:::

### Track A — Chat Assistant

*Estimated time: under 10 minutes. The capstone concepts, worked in one conversation.*

This is the business-friendly default. You will design the tissue version of a real workflow without writing a single line of code or configuring a single agent. This track is conceptual, not technical — the thinking is the deliverable.

1. Open your chat assistant and start a new conversation.

2. Describe one workflow you currently run as a **hierarchy** — you assign tasks, you check back, you review outputs, you redirect. Pick something real: a weekly client deliverable, a hiring funnel, a content pipeline. Name the steps, the handoffs, and where you personally sit in the loop.

3. Ask: *"Redesign this workflow as a 'tissue' — a set of peer units with local decision-making and no central coordinator. What would each unit be? What would its decision boundary be? How would they sync without a manager in the loop?"*

4. Then ask: *"Run the six-perturbation robustness test on this new design. For each perturbation, tell me whether the tissue or the hierarchy holds up better."*

5. Save both outputs. Read them side by side. You now have a capstone artifact: a current architecture, a redesigned architecture, and a head-to-head robustness comparison. This IS the diagnostic from the chapter — and the closing lab of the book.

**Your Submission:** Your submission is the tissue redesign of your chosen workflow — the redesign description plus the six-perturbation robustness test results — plus your capstone reflection. Copy the redesign and test results into a document. Underneath them, write your capstone reflection (150-200 words): what is the single most important thing you are taking from this book into your professional practice? This reflection is your capstone submission. Submit the redesign + robustness test + capstone reflection.

### Track B — Terminal Agent

1. In a plain text editor, write a one-page description of the current workflow you have chosen. Name the steps. Name the handoffs. Name the people or agents involved at each step. Name where the cognitive bottleneck currently lives. Be specific — generic descriptions will produce generic redesigns.

2. Open a session in your terminal agent. (If you have never used one, the current setup walkthrough is on the companion page at cognitioneconomy.net/ch16-companion.) Paste your workflow description and ask: *"Score this workflow on the six dimensions of basal-cognitive architecture — composability, locality, resilience, observability, evolvability, and alignment. For each dimension, give me a score from 1 to 5 and explain what evidence in my description supports the score."*

3. Read the diagnostic carefully. Push back where you disagree. The goal is not to receive a verdict — it is to develop your own architectural intuition by arguing with a partner who has read every word of the framework.

4. Now ask: *"Based on this diagnostic, sketch the tissue version of this workflow. Show me the peer agents, the shared task list, the cognitive light cone of each agent, and the points of human judgment. Make zero assumptions about my current org chart — design the workflow as if I were starting from scratch."*

5. Save the response as your "tissue sketch" — a file in your working folder, owned by you. Read it next to your original workflow. Identify the three biggest structural changes. Write a single paragraph explaining which of the three you would actually implement first, and what would have to be true about your organization for that implementation to succeed.

**Your Submission:** Your submission is the six-dimension diagnostic for your workflow, the tissue redesign you built from it, and your capstone reflection. Copy the diagnostic and redesign into a document. Underneath them, write your capstone reflection (150-200 words): looking back at the 200-word redesign sketch you wrote in Module 0, how has your thinking about redesigning work evolved over the course of this book? What would you change in that sketch today? Submit the diagnostic + redesign + capstone reflection.

### Track C — Agent-Orchestration Workspace: Build the Tissue

This is the capstone build — the only exercise in the book where you construct the architecture the whole book has been arguing for and watch it run. The orchestration workspace is the no-code surface for it; the current tool name and the toggle that opens the manager view are on the companion page (cognitioneconomy.net/ch16-companion). Every step below is named for the architectural decision it sets — those decisions are the evergreen content, whatever the buttons are called this year.

1. **Open the orchestration view.** Switch from the editing surface to the manager view — the overview where several agents can run side by side and their deliverables collect in one place. Exact click-path: companion site.

2. **Set the topology dial: no orchestrator.** Create a new project that represents a single "tissue unit" — the smallest unit of your workflow that could be done by a single team of peer agents. In the project description, deliberately do *not* name an orchestrator. Instead, write: *"This project is run by three peer agents — a Sensing Agent, a Decision Agent, and a Communication Agent — sharing a single task list. There is no central controller. Each agent picks up the next task it is qualified to handle and writes back what it did."* Refusing to name a lead is the whole point of the step. Notice how strange it feels. That feeling is two hundred years of the Hierarchy Assumption talking.

3. **Set the work dial: real stakes.** In the task description, paste a real piece of work from the workflow you are redesigning. Use a task where you would normally route through a manager or an orchestrator. Then start the project and watch the three agents pick up the work asynchronously.

4. **Set the observability dial: watch the substrate.** As the agents work, observe the shared deliverables panel. Note which agent picked up which sub-task, how they communicated through the shared task list, and where (if anywhere) the absence of an orchestrator caused the work to slow or stall. This is your first empirical look at how a tissue architecture actually behaves in production — and your first live reading on dimension four, observability.

5. **Set the reuse dial: save the unit.** At the end, save the project as a template for the tissue unit — this is composability, dimension one, made concrete: a unit you can lift and reuse without redesigning it. Then write a two-paragraph reflection: where did the tissue architecture outperform the hierarchical equivalent you have been running, and where did it underperform? This reflection is your second artifact.

**Your Submission:** Your submission is the three-peer-agent project configuration you built — the project description with no named orchestrator — plus the task output from running real work through it, plus your capstone reflection. Copy the project description and task output into a document. Underneath them, write your capstone reflection (150-200 words): what does "Go build the reef" mean to you, specifically, in your professional context? What is the reef you are going to build? Submit the project configuration + task output + capstone reflection.

:::{admonition} Is this still true? A two-minute lab
:class: note

1. Ask your assistant: *"Can you run several agents in parallel as peers, without one agent directing the others?"* Log the answer and the date.
2. Ask: *"If one of those agents fails mid-task, what happens to the others?"* Whatever it says, that is your tool's current position on the Tissue Test.
3. The architecture concepts in this chapter outlive any tool's answer; the answers themselves change every release. Current surfaces that support the Track C build: cognitioneconomy.net/ch16-companion.
:::

### Reflection

Write three to four sentences capturing what you noticed in the track you ran. If you worked conversationally, did the redesign make the tissue architecture feel inevitable or optional? If you ran the capstone build, where did the absence of an orchestrator help, and where did it hurt? And, most importantly: which part of this exercise will you actually return to next quarter when you start the real restructure?

---

---
*Applied Exercise for Chapter 16 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
