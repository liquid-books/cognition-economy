# Applied Exercise — Chapter 9: Custom Sub-Agents — The Specialist Mindset
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your First Specialist

*Estimated time: 25–30 minutes. You'll produce a working "Competitor Research" sub-agent — a specialist you can call by name on any future project.*

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code:** For students using Claude Code. Reference the quickstart at code.claude.com/docs/en/quickstart.
- **Track C — Antigravity 2.0 IDE:** For students using the Antigravity 2.0 IDE Agent Manager. Reference antigravity.google/docs/ide-overview.
:::

### Track A — Claude Desktop

This is the easy on-ramp. No installation, no terminal, no setup beyond opening a browser tab. You will *simulate* the sub-agent pattern manually so you feel what specialist framing does to an answer.

1. Open **Claude Desktop** (download at claude.ai/download) or just go to **claude.ai** in your browser and start a new conversation.
2. In one paragraph, describe a real business problem you are wrestling with this week — a pricing decision, a hiring question, a market entry call, a launch trade-off.
3. Paste this exact prompt below your problem: *"Give me three separate responses to this problem — first from the perspective of a financial analyst, then a marketing strategist, then an operations manager. Label each clearly and keep each response to about a paragraph."*
4. Read all three answers in sequence. Notice how the financial analyst flags risk and unit economics, the marketing strategist talks positioning and demand, and the operations manager surfaces execution constraints. Same model. Same problem. Three different lenses.
5. That is the sub-agent concept in its rawest form. The rest of this chapter is about automating what you just did by hand — turning those three personas into installable specialists that route work to themselves without you reminding them who they are.

**Your Submission:** Your submission is two things: (1) the standing brief you would write for a specialist designed for your most painful recurring task — written in plain English using Role/Context/Rules/Format, and (2) Claude's three-specialist response to a real business problem you chose (the analyst/strategist/ops manager exercise). Copy both into one document. Write one sentence: which specialist perspective surfaced something you had not considered? Submit the specialist brief + three-role output + one sentence.

### Track B — Claude Code

Claude Code includes a guided sub-agent creator that walks you through every dial discussed in this chapter. Reference: https://code.claude.com/docs/en/sub-agents.

1. **Open the agents interface.** Inside Claude Code, type `/agents` and press Enter. The interface lets you view existing specialists, create new ones, and edit ones you already built.

2. **Create a new personal agent.** Switch to the Library tab, select **Create new agent**, and choose **Personal**. Personal scope means the specialist is available in every project on your machine — not tied to a single codebase.

3. **Generate with Claude.** When prompted, select **Generate with Claude** and describe the specialist in plain English. Use this brief: *"A competitor research specialist that takes a single input — a competitor name — and produces a one-page brief covering five sections: positioning, recent news from the last 90 days, pricing posture, three observable strengths, and three observable weaknesses. It cites every factual claim. If a section lacks sufficient data, it says so explicitly rather than making things up."* Claude will generate the identifier, description, and system prompt for you.

4. **Pick your tools — least-privilege.** When asked which tools the specialist should have access to, select **web search** and **read-only file access**. Do not grant it write, edit, or send capabilities. This specialist looks. It does not act.

5. **Pick a model.** For competitor research, choose a strong model — Sonnet or higher. The work involves judgment about source quality and signal extraction, not just pattern matching. Match the brain to the job.

6. **Save and test on three real competitors.** Save the specialist. Then run it three times on real competitors from your industry. Read each one-page brief. Ask yourself: would I send this to a client? Would I make a decision on this? If yes on all three, the specialist is ready. If no on any of them, return to the system prompt and tighten it.

**Your Submission:** Your submission is the agent definition Claude Code generated — the identifier, description, and full system prompt for your specialist — plus the output from one real task run. Copy both into one document. Write one sentence: what would this specialist save you each week if you used it every time this task comes up? Submit the agent definition + one task output + one sentence.

### Track C — Antigravity 2.0 IDE

Google Antigravity 2.0 IDE's Agent Manager is the no-code orchestration surface — a birds-eye view designed for business users to spawn and oversee specialists without touching the editor. Reference: https://antigravity.google/docs/ide-overview.

1. **Open the Agent Manager.** Launch Antigravity. Press **CMD+E** (Mac) or **CTRL+E** (Windows) to toggle from the Editor view to the Agent Manager. You will see a clean orchestration view where multiple agents can run side by side.

2. **Start a new asynchronous agent.** Click the **New Agent** action and select an asynchronous task. Asynchronous agents run in parallel — they do not block your other work, and you can spawn several at once across different workspaces.

3. **Define the task in plain English.** In the task description field, paste this: *"You are a competitor research specialist. I will give you a competitor name. Produce a one-page brief covering five sections — positioning, recent news from the last 90 days, pricing posture, three observable strengths, three observable weaknesses. Cite every factual claim. If you do not have sufficient data for a section, say so rather than fabricate."* This becomes the agent's standing instruction set.

4. **Give it the first competitor.** Type the name of a real competitor and submit. The agent begins working asynchronously. You can leave the Agent Manager, work elsewhere, and return when the artifact is ready.

5. **Review the Artifacts panel.** When the agent finishes, its output appears as an Artifact — a structured deliverable like a markdown brief, diff view, or report. Open the artifact, read it carefully, and verify the citations resolve to real sources.

6. **Spawn two more in parallel.** Now do something the main conversation could never do efficiently: queue two more competitors as separate asynchronous agents, both running at the same time. Watch the Agent Manager track three specialists working in parallel across the same task type.

**Your Submission:** Your submission is the Project Description (standing brief) you wrote for your specialist Agent in Agent Manager, plus the Artifact from your first real task run. Copy both into one document. Write one sentence: what was the most significant difference between the specialist's Artifact and what you would have gotten from a generic AI prompt? Submit the Project Description + Artifact + one sentence.

### Reflection

After completing both tracks, write two or three sentences answering: *What did you notice about how each tool handled the same task? Where did the Claude Code experience feel sharper — and where did Antigravity's parallel orchestration surface a capability the chat-style experience could not match? Which one fits the shape of your actual work better?*

---
*Applied Exercise for Chapter 9 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
