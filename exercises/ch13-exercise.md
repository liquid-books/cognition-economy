# Applied Exercise — Chapter 13: Hooks, Channels, and Automations — Make Your AI Work While You Sleep
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Design Your Daily Briefing Agent

*Estimated time: 25–30 minutes. You'll produce a complete written specification for a daily briefing agent — the trigger, the work, the format, and the delivery channel — that you can hand to either Claude Code or Antigravity 2.0 IDE to set up for you.*

The goal is not to build the automation yourself. The goal is to design it clearly enough that an AI tool can build it from your description. Both tracks below use the same specification you write — they just differ in how that specification becomes a working agent.

**Before starting either track**, if you have never used Claude Code before, work through the official quickstart at [https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart). It is the recommended starting point and will get you to a working session in about ten minutes.

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code:** For students using Claude Code. Reference the quickstart at code.claude.com/docs/en/quickstart.
- **Track C — Antigravity 2.0 IDE:** For students using the Antigravity 2.0 IDE Agent Manager. Reference antigravity.google/docs/ide-overview.
:::

### Track A — Claude Desktop

*Estimated time: under 10 minutes. No tools to install, no agents to configure. Just a conversation.*

This is the business-friendly default. You will not build an automated hook. You will build the **manual** version of one — a briefing you pull on command. The output is the same; only the trigger is different.

1. Open Claude Desktop (download from [claude.ai/download](https://claude.ai/download)) or just go to [claude.ai](https://claude.ai) in your browser.

2. Write a Daily Briefing Prompt. Tell Claude your role, your two or three current top priorities (a specific deal, a hiring round, a launch), and ask it to produce a briefing covering three things: (a) what you should focus on today, (b) one thing to prepare for, (c) one risk worth watching. Keep it tight — one short paragraph of context is enough.

3. Run it. Read the briefing. Notice how the structure forces clarity.

4. Save that prompt somewhere you will find it every morning — a sticky note, a pinned chat, the top of your notes app. Set a phone alarm called **"AI Briefing"** for the same time each weekday.

5. That alarm IS your hook. The difference between Track C and Tracks A and B is that yours fires when you pull it, not automatically. The output is the same. Most of the value of an automation is the *discipline of the artifact*, not the cron job.

**Your Submission:** Your submission is your Daily Briefing prompt — the one you saved and will actually use — plus the first briefing it produced. Copy both into one document. Write two sentences: (1) what does this briefing tell you that you would not have thought to check on your own, and (2) describe one other proactive briefing you want to build using the same pattern. Submit the briefing prompt + first output + two sentences.

### Track B — Claude Code

1. In a plain text editor, write a one-page specification for your daily briefing agent. Include: what time it should fire, what sources it should check (calendar, email, news, project tracker — pick three), what format the briefing should take (length, tone, structure), and what channel it should deliver to (email, Slack, Telegram, iMessage). Be concrete. "Pull my three most important client emails from the last twenty-four hours" is better than "check email."

2. Open Claude Code. In your session, ask: *"Based on the specification I am about to paste, write me a hook configuration that fires this briefing at the scheduled time and delivers the result to the channel I specified."* Paste your specification.

3. Claude will produce a hook configuration in plain English describing what it does. Read it. If anything does not match what you wanted, ask Claude to adjust. Reference the official hooks guide at [https://code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) if you want to understand which lifecycle events are available.

4. To choose where the briefing gets delivered, review the channels documentation at [https://code.claude.com/docs/en/channels](https://code.claude.com/docs/en/channels) and pick one that matches where you already read. Ask Claude to update your specification to include the chosen channel.

5. Save the final specification to a file named `briefing-spec.md`. This is your artifact — you will use it in production or hand it to your IT team to deploy.

**Your Submission:** Your submission is the hook specification Claude Code produced — what it triggers on, what sources it checks, what format it produces, and what channel it delivers to — plus the first briefing output the hook generated. Copy both into one document. Write one sentence: what is the practical difference between pulling this briefing yourself every day and having it pushed to you automatically? Submit the specification + first output + one sentence.

### Track C — Antigravity 2.0 IDE

1. Open Antigravity 2.0 IDE. Press `CMD+E` (Mac) or `CTRL+E` (Windows) to switch to the Agent Manager surface — the "no-code" orchestration view that is the business-user entry point. Reference the IDE overview at [https://antigravity.google/docs/ide-overview](https://antigravity.google/docs/ide-overview) if you need orientation.

2. In the Agent Manager, start a new task. In the task description box, paste the same one-page specification you wrote in Track A's step 1. At the top of the task, add a sentence: *"This task should run as a recurring background agent every weekday at 7:00 AM and deliver its output to the channel I specify below."*

3. Watch the agent work asynchronously. The Agent Manager will produce artifacts as the agent executes — markdown drafts of the briefing, a configuration summary, and the actual delivery to the channel you specified.

4. Review the artifacts. Open the markdown draft and read it as if it were your real morning briefing. Ask yourself: is this what you would actually want to read at 7:00 AM? If not, return to the Agent Manager and refine the task description.

5. Save the final task as a recurring background agent. The Agent Manager will fire it on the schedule you specified, asynchronously, without further input from you.

**Your Submission:** Your submission is the recurring Agent Manager task configuration — the full task description with schedule and channel — plus the first Artifact it produced. Copy both into one document. Write two sentences: (1) what three sources does your daily briefing pull from and why did you choose those three, and (2) what is the one thing you most want it to surface that you currently have to find manually every day? Submit the task configuration + first Artifact + two sentences.

### Reflection

Write two to three sentences capturing what you noticed about how the two tools handled the same specification. Did one feel more like writing a contract with the AI and the other more like delegating to a team member? Which surface do you think your team would actually adopt, and why?

---

*The deeper lesson of this exercise is not the briefing itself. It is what happens when you stop thinking of AI as something you ask and start thinking of it as something you design. The briefing is a starting point. The mindset is the destination.*

---
*Applied Exercise for Chapter 13 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
