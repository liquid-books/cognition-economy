# Applied Exercise — Chapter 9: Custom Sub-Agents — The Specialist Mindset
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your First Specialist

*Estimated time: 25–30 minutes. You'll produce a working "Competitor Research" sub-agent — a specialist you can call by name on any future project.*

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace built for running several agents at once (Track C). Product names, download links, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch09-companion.
:::

### Track A — Chat Assistant

This is the easy on-ramp. No installation, no terminal, no setup beyond opening a browser tab. You will *simulate* the sub-agent pattern manually so you feel what specialist framing does to an answer.

1. Open your chat assistant and start a new conversation.
2. In one paragraph, describe a real business problem you are wrestling with this week — a pricing decision, a hiring question, a market entry call, a launch trade-off.
3. Paste this exact prompt below your problem: *"Give me three separate responses to this problem — first from the perspective of a financial analyst, then a marketing strategist, then an operations manager. Label each clearly and keep each response to about a paragraph."*
4. Read all three answers in sequence. Notice how the financial analyst flags risk and unit economics, the marketing strategist talks positioning and demand, and the operations manager surfaces execution constraints. Same model. Same problem. Three different lenses.
5. That is the sub-agent concept in its rawest form. The rest of this chapter is about automating what you just did by hand — turning those three personas into installable specialists that route work to themselves without you reminding them who they are.

**Your Submission:** Your submission is two things: (1) the standing brief you would write for a specialist designed for your most painful recurring task — written in plain English using Role/Context/Rules/Format, and (2) the assistant's three-specialist response to a real business problem you chose (the analyst/strategist/ops manager exercise). Copy both into one document. Write one sentence: which specialist perspective surfaced something you had not considered? Submit the specialist brief + three-role output + one sentence.

### Track B — Terminal Agent

Your terminal agent includes a guided sub-agent creator that walks you through every dial discussed in this chapter. The exact commands and menus are on the companion page (cognitioneconomy.net/ch09-companion); what matters here is which dial each step sets.

1. **Open the agent creator.** Every terminal agent has an interface for viewing the specialists you have, creating new ones, and editing ones you already built.

2. **Set the scope dial: personal.** Create the specialist at personal scope — so it is available in every project on your machine, not tied to a single codebase. Exact click-path: companion site.

3. **Set the system-prompt dial.** Most tools will draft the job description for you from a plain-English brief. Use this one: *"A competitor research specialist that takes a single input — a competitor name — and produces a one-page brief covering five sections: positioning, recent news from the last 90 days, pricing posture, three observable strengths, and three observable weaknesses. It cites every factual claim. If a section lacks sufficient data, it says so explicitly rather than making things up."* The tool will generate the identifier, description, and system prompt. Read what it wrote and edit it — it is your specialist, not the tool's.

4. **Set the tools dial — least privilege.** Grant the specialist **web search** and **read-only file access**. Do not grant it write, edit, or send capabilities. This specialist looks. It does not act.

5. **Set the model dial.** Choose your provider's mid- or top-tier reasoning model, not its fastest and cheapest one — the work involves judgment about source quality and signal extraction, not just pattern matching. Match the brain to the job.

6. **Save and test on three real competitors.** Save the specialist. Then run it three times on real competitors from your industry. Read each one-page brief. Ask yourself: would I send this to a client? Would I make a decision on this? If yes on all three, the specialist is ready. If no on any of them, return to the system prompt and tighten it.

**Your Submission:** Your submission is the agent definition your tool generated — the identifier, description, and full system prompt for your specialist — plus the output from one real task run. Copy both into one document. Write one sentence: what would this specialist save you each week if you used it every time this task comes up? Submit the agent definition + one task output + one sentence.

### Track C — Agent-Orchestration Workspace

The orchestration workspace is the no-code surface — a birds-eye view designed for business users to spawn and oversee specialists without touching an editor or a terminal. The current tool name and the toggle that opens this view are on the companion page (cognitioneconomy.net/ch09-companion).

1. **Open the orchestration view.** Switch from the editing surface to the manager view — an overview where multiple agents can run side by side.

2. **Start a new asynchronous agent.** Asynchronous agents run in parallel — they do not block your other work, and you can spawn several at once across different workspaces.

3. **Define the task in plain English.** In the task description field, paste this: *"You are a competitor research specialist. I will give you a competitor name. Produce a one-page brief covering five sections — positioning, recent news from the last 90 days, pricing posture, three observable strengths, three observable weaknesses. Cite every factual claim. If you do not have sufficient data for a section, say so rather than fabricate."* This becomes the agent's standing instruction set.

4. **Give it the first competitor.** Type the name of a real competitor and submit. The agent begins working asynchronously. You can leave the manager view, work elsewhere, and return when the deliverable is ready.

5. **Review the deliverable.** When the agent finishes, its output appears as a structured deliverable — a brief, a diff view, a report. Open it, read it carefully, and verify the citations resolve to real sources.

6. **Spawn two more in parallel.** Now do something the main conversation could never do efficiently: queue two more competitors as separate asynchronous agents, both running at the same time. Watch the manager view track three specialists working in parallel across the same task type.

**Your Submission:** Your submission is the standing brief you wrote for your specialist, plus the deliverable from your first real task run. Copy both into one document. Write one sentence: what was the most significant difference between the specialist's deliverable and what you would have gotten from a generic AI prompt? Submit the standing brief + deliverable + one sentence.

### Reflection

After completing your track, write two or three sentences answering: *What changed when the same model was given a specialist's framing instead of a generalist's? Which of the five dials — scope, system prompt, tools, model, permissions — was hardest to set for your specialist, and why? And which recurring task in your real work is the first candidate for a specialist of its own?*

:::{admonition} Is this still true?
:class: note
Before you build, spend two minutes checking your own tool: (1) Which built-in specialist roles ship today, and what does your tool call them? (2) Which scopes can a specialist have — personal, project, shared? (3) Which models can you assign to a specialist? The names and menus change between releases; the five dials do not. Current click-paths live at cognitioneconomy.net/ch09-companion.
:::

---
*Applied Exercise for Chapter 9 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
