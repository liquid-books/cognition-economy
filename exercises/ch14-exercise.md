# Applied Exercise — Chapter 14: Security and Trust — Building Inside the Guardrails
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your AI Security Posture in 30 Minutes

*Estimated time: 25–30 minutes. You'll produce a one-page security posture document — a list of approved tools, the four questions answered for each, and a draft of the fifteen-minute employee briefing — that you can hand to your team next week.*

The goal of this exercise is not to design a perfect security program. The goal is to produce the artifact that closes the largest gap most businesses have today: a single page that any employee can read and understand. Both tracks below use AI to help you do the analysis. They differ in how the work feels.

**Before starting either track**, if you have never used Claude Code before, work through the official quickstart at [https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart). It is the recommended starting point and will get you to a working session in about ten minutes.

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code:** For students using Claude Code. Reference the quickstart at code.claude.com/docs/en/quickstart.
- **Track C — Antigravity 2.0 IDE:** For students using the Antigravity 2.0 IDE Agent Manager. Reference antigravity.google/docs/ide-overview.
:::

### Track A — Claude Desktop

*Estimated time: under 10 minutes. A single conversation. No tools, no installs.*

This is the business-friendly default. You will do the security audit and draft the team briefing as a plain conversation — the same artifacts Tracks A and B produce, just pulled out of a chat window instead of an agent run.

1. Open Claude Desktop (download from [claude.ai/download](https://claude.ai/download)) or use [claude.ai](https://claude.ai) in your browser.

2. Describe your current AI usage honestly. Which tools does your team actually use (ChatGPT, Claude, Copilot, Gemini, Perplexity, niche vertical tools)? What kinds of data get pasted in (client names, contracts, financials, code, HR data)? Which subscriptions are consumer tier and which are enterprise or business with a data-protection agreement? Do not sanitize the picture — the audit only works if the inputs are true.

3. Ask Claude: *"Based on what I've described, what are my top three security risks and what should I do about each?"* Read the answer carefully. Push back if anything feels off.

4. Ask a follow-up: *"Draft a 15-minute briefing I could give my team about responsible AI use, based on the risks you just identified."*

5. Save both outputs to a single doc. That document IS the security posture and the cultural layer from this chapter. Send the briefing to your team this week.

**Your Submission:** Your submission is all three artifacts Claude produced from your security audit: the approved-tools list with the four security questions answered for each tool, the 15-minute team briefing, and the ranked risk gaps list. Copy all three into one document. Write two sentences: (1) which risk gap surprised you most and what will you do about it in the next two weeks, and (2) who on your team most needs to read the 15-minute briefing? Submit the three artifacts + two sentences.

### Track B — Claude Code

1. In your Claude Code session, paste the following structured prompt: *"I am the [your role] at a [size and industry] company. Help me audit our current AI usage. Ask me one question at a time about which AI tools my team uses, what kind of data each tool touches, and what tier (consumer or enterprise) we are on. After you have a complete picture, produce three artifacts for me: (1) a list of our current AI tools with the four security questions answered for each, (2) a draft of a fifteen-minute employee briefing in one page, and (3) a list of the highest-risk gaps in our current setup, ranked."*

2. Answer Claude's questions honestly. The value of the exercise comes from the accuracy of your answers, not from looking good. If your team is using consumer tools, say so. If you do not know how a vendor handles data retention, say that too.

3. Review the three artifacts Claude produces. For the security questions you cannot answer for a given tool, take that as your action list — those are the vendors you need to contact for clarification this week.

4. For the fifteen-minute briefing draft, edit it for your firm's voice and your team's specific examples. The generic version will be eighty percent right; your edits make it land for your people.

5. Save the final document to a file named `ai-security-posture.md`. Schedule the briefing for the next team meeting. The artifact is the deliverable; the briefing is the activation.

**Your Submission:** Your submission is the same three artifacts Claude Code produced — approved-tools list, team briefing, and risk gaps — plus a personal action plan you write yourself: three specific changes you will make to your team's AI usage within 30 days, each with a deadline. Copy everything into one document. Submit the three artifacts + personal action plan.

### Track C — Antigravity 2.0 IDE

1. Open Antigravity 2.0 IDE. Press `CMD+E` (Mac) or `CTRL+E` (Windows) to switch to the Agent Manager surface — the no-code orchestration view that is the business-user entry point. Reference the IDE overview at [https://antigravity.google/docs/ide-overview](https://antigravity.google/docs/ide-overview) if you need orientation.

2. Before starting a new task, take a moment to review which Projects in the Agent Manager have which data access permissions. Antigravity organizes work at the project level, and each project can be scoped to specific data sources. This itself is a useful audit — note any project that has broader permissions than it actually needs for its current work.

3. Start a new task with the same structured prompt from Track A's step 1, adapted for the Antigravity surface: *"Audit my team's current AI usage and produce a one-page security posture document. Ask me one question at a time. When you are done, produce three artifacts: an approved-tools list, a fifteen-minute briefing, and a ranked list of the highest-risk gaps."* Scope the task to a project with appropriate data permissions for this kind of sensitive review.

4. Watch the agent work asynchronously. The Agent Manager will produce artifacts as the work progresses — markdown drafts, comparison tables, and the final one-page document. Review each artifact as it appears and provide feedback.

5. Save the final artifacts to the project. Note for yourself: which surface did you find easier to think alongside? Which produced the briefing document you actually want to hand to your team?

**Your Submission:** Your submission is the three artifacts the Antigravity agent produced — approved-tools list, team briefing, and risk gaps list — plus one paragraph (100-150 words) you write describing your current security posture honestly, not aspirationally, and identifying your single highest-priority gap. Submit the three artifacts + one paragraph.

### Reflection

Write two to three sentences capturing what you noticed about your own firm's security posture during the audit. Where were you confident? Where were you uncertain? What is the single most important action — concrete, specific, doable in the next week — that this exercise made obvious to you?

---

*The deeper lesson of this exercise is not the document itself. It is what happens when you sit down to write the document and discover, often for the first time, what you do and do not actually know about your own firm's AI usage. That moment of clarity is the beginning of a real security posture. Everything after it is execution.*

---
*Applied Exercise for Chapter 14 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
