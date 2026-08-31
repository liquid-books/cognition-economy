# Applied Exercise — Chapter 13: Hooks, Channels, and Automations — Make Your AI Work While You Sleep
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Design Your Daily Briefing Agent

*Estimated time: 25–30 minutes. You'll produce a complete written specification for a daily briefing agent — the trigger, the work, the format, and the delivery channel — and, on the agent surfaces, a working automation that delivers your first briefing without you asking for it.*

The design comes first. Every track starts from the same one-page specification; the tracks differ only in what happens to it — you carry it out by hand, or you hand it to an agent and walk away.

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace built for running tasks in the background (Track C). On the two agent surfaces, the automated version of this exercise is a **scheduled-task configuration plus a delivery channel** — you specify when the briefing fires, what it checks, and where it lands. A hook enters the picture only for the event-driven finishing touch: "notify me when the briefing has been delivered." Product names, menu locations, and exact configuration syntax change too fast for print; the current versions of all three tracks — with tool names, walkthroughs, and screenshots — live on the companion page at cognitioneconomy.net/ch13-companion. The companion page is date-stamped; this book is not.
:::

### Part 1: Write the Specification (10 minutes — all tracks)

In a plain text editor, write a one-page specification for your daily briefing agent. Include: what time it should fire (this book's running example is 8:00 AM — use the time you actually start work), what sources it should check (calendar, email, news, project tracker — pick three), what format the briefing should take (length, tone, structure), and what channel it should deliver to (email, a team chat channel, your phone). Be concrete. "Pull my three most important client emails from the last twenty-four hours" is better than "check email."

This specification is the exercise's real artifact. Whichever track you run, the specification is what you are testing.

### Track A — Chat Assistant: The Manual Version

This is the business-friendly default. You will not configure the automated scheduled task. You will build the **manual** version of it — a briefing you pull on command. The output is the same; only the trigger is different.

1. Open your chat assistant.

2. Turn your specification into a Daily Briefing Prompt. Tell the AI your role, your two or three current top priorities (a specific deal, a hiring round, a launch), and ask it to produce a briefing covering three things: (a) what you should focus on today, (b) one thing to prepare for, (c) one risk worth watching. Keep it tight — one short paragraph of context is enough.

3. Run it. Read the briefing. Notice how the structure forces clarity.

4. Save that prompt somewhere you will find it every morning — a sticky note, a pinned chat, the top of your notes app. Set a phone alarm called **"AI Briefing"** for 8:00 AM each weekday.

5. That alarm IS your schedule — a scheduled task with you as the delivery mechanism. The automated version replaces the alarm with a scheduled-task configuration and replaces the copy-paste with a delivery channel; the shape is identical. Most of the value of an automation is the *discipline of the artifact*, not the cron job.

**Your Submission:** Your submission is your Daily Briefing prompt — the one you saved and will actually use — plus the first briefing it produced. Copy both into one document. Write two sentences: (1) what does this briefing tell you that you would not have thought to check on your own, and (2) describe one other proactive briefing you want to build using the same pattern. Submit the briefing prompt + first output + two sentences.

### Track B — Terminal Agent: The Scheduled Task

Your terminal agent can run work on a clock and deliver the result to a channel — the two primitives this chapter is about. The exact command names and configuration syntax are on the companion page (cognitioneconomy.net/ch13-companion); what matters here is which decision each step sets. Every instruction below is something you *say to the tool* in plain English.

1. **Set the trigger dial: a schedule, not an event.** Open a session and delegate the whole job in one sentence: *"Every weekday at 8:00 AM, assemble my briefing from the specification I am about to paste, and deliver it to [the channel where you actually read things]. Confirm what you have scheduled and show me how to inspect or cancel it."* Then paste your Part 1 specification. Notice what you did NOT ask for: a hook. A briefing that fires at 8:00 AM is time-driven — by this chapter's own taxonomy, that is a scheduled task. Hooks are for events, and one arrives in step 4.

2. **Set the channel dial: the place that gets read.** Before confirming, ask: *"Which delivery channels can you reach today?"* Pick the one you already check without thinking — your team chat, your email, the messages app on your phone. Do not invent a new surface for this output. (The current channel list for your tool, and how each one is wired up, is a companion-page question.)

3. **Read back the contract.** Have the agent restate the three components in its own words — the trigger (every weekday, 8:00 AM), the work (your specification, source by source), and the channel. If any of the three does not match what you wrote, fix it now, in conversation. This is the same plan-as-contract move you learned in Chapter 6, applied to an automation instead of a task.

4. **Add the hook — the event, not the time.** Now attach the one piece of this workflow that genuinely is event-driven: *"When the briefing has been delivered, notify me."* That is a hook: something happened, so something else fires — deterministically, every time. Saying both sentences back to back is the fastest way to feel the difference between the two primitives.

5. **Let it fire once.** Save your specification to a file named `briefing-spec.md` — that is your artifact — and leave the automation armed overnight. Tomorrow at 8:15, the briefing should be sitting in your channel, unasked for. That moment is the whole chapter. If your tool cannot yet schedule tasks or reach a channel you use, that is a logged verification answer, not a failure: note it, run Track A's manual version, and check the companion page for what has shipped since press time.

**Your Submission:** Your submission is the scheduled-task delegation as the agent confirmed it — the trigger, the sources it checks, the format, and the delivery channel — plus the first briefing it delivered without you asking. Copy both into one document. Write one sentence: what is the practical difference between pulling this briefing yourself every day and having it pushed to you automatically? Submit the confirmed configuration + first delivered briefing + one sentence.

### Track C — Agent-Orchestration Workspace: The Recurring Background Task

The orchestration workspace is the no-code surface — background tasks configured in plain English, no terminal involved. The current tool name and the toggle that opens this view are on the companion page (cognitioneconomy.net/ch13-companion).

1. **Open the orchestration view.** Switch from the editing surface to the manager view — the overview where background tasks run side by side.

2. **Set the recurrence decision at the top of the task.** Start a new task. Paste your Part 1 specification into the task description, and add one sentence above it: *"This task should run as a recurring background task every weekday at 8:00 AM and deliver its output to the channel I specify below."* The recurrence sentence is the trigger dial; the specification is the work; the channel line is the delivery. All three components of this chapter's pattern, in one task description.

3. **Watch the first run.** The workspace will produce structured deliverables as the agent executes — a draft of the briefing, a summary of the configuration, and the delivery itself. You can leave and come back; the task does not need you watching.

4. **Review the deliverable as the customer of the output.** Open the draft briefing and read it as if it were 8:00 tomorrow morning. Is this what you would actually want waiting for you? If not, refine the task description — tighten a source, cut a section, change the format — and run it again. You are editing a specification, not debugging code.

5. **Save it as recurring.** Commit the task on its schedule. From tomorrow, it fires every weekday at 8:00 AM, asynchronously, without further input from you.

**Your Submission:** Your submission is the recurring task configuration — the full task description with its schedule and channel — plus the first deliverable it produced. Copy both into one document. Write two sentences: (1) what three sources does your daily briefing pull from and why did you choose those three, and (2) what is the one thing you most want it to surface that you currently have to find manually every day? Submit the task configuration + first deliverable + two sentences.

:::{admonition} Optional Variant: The Desktop-Bound Task
:class: note
If the recurring task you most want to automate lives in a desktop application that no connector reaches and no website fronts, revisit Chapter 3's connection ladder. The last rung — computer use, where the AI works the screen directly — exists for exactly this case. Write the same specification, note that the work step requires screen-level access, and keep a human-approval gate on every run while the tool is still earning your trust.
:::

### Reflection

Write two to three sentences capturing what you noticed as you designed the specification. Did writing it feel more like drafting a contract with the AI or like delegating to a team member? If you ran Track B or C: what changed in you when the first briefing arrived without being asked for? And where else in your week did you catch yourself spotting the trigger–work–channel pattern once you started looking for it?

:::{admonition} Is this still true?
:class: note
Before you configure anything, spend two minutes checking your own tool and log the answers with today's date: (1) Ask it: *"Can you run a task on a schedule, and how would I inspect or cancel one?"* (2) Ask it: *"Which channels can you deliver output to today?"* (3) Check whether scheduled tasks live in your chat assistant, your terminal agent, or both — the capability has been migrating from infrastructure to interface since this book went to press. The primitives — trigger, work, channel — do not change; where they live does. Current details at cognitioneconomy.net/ch13-companion. Append your dated answers to your submission.
:::

---

*The deeper lesson of this exercise is not the briefing itself. It is what happens when you stop thinking of AI as something you ask and start thinking of it as something you design. The briefing is a starting point. The mindset is the destination.*

---
*Applied Exercise for Chapter 13 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
