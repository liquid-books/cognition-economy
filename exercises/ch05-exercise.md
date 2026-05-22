# Applied Exercise — Chapter 5: The Six Engineering Disciplines
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Across All Six Disciplines

This exercise takes you through one complete task — from raw prompt to full harness — to give you the experience of what each discipline adds.

**Choose your task:** Pick one recurring piece of work. Something you do at least weekly. Something with real professional stakes. For the purposes of this exercise, let us use: *preparing for a client meeting.*

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code inside Antigravity IDE:** For students who want to work in a professional developer environment. Requires Antigravity 2.0 IDE (antigravity.google/docs/ide-overview) with Claude Code running in the integrated terminal.
- **Track C — Gemini + Antigravity 2.0 IDE:** For students in the Google ecosystem. Uses Gemini (gemini.google.com) for AI conversations and the Antigravity 2.0 IDE Agent Manager for orchestration.
:::

### Track A — Claude Desktop

**Floor 1 — Prompt Engineering:**
Write a prompt from scratch asking Claude to help you prepare for a client meeting. Do not overthink it. Just write what you would normally write.

Now evaluate it honestly. Is it specific enough? Does it tell Claude who the client is, what you know about them, what the meeting is for, what outcome you need? Rewrite it with those specifics. Compare the two outputs. The difference is prompt engineering.

**Floor 2 — System Prompting:**
Go to your Claude system prompt (Settings → Custom Instructions). Read it. Does it tell Claude what kind of client relationships you manage? What industry you are in? How you prefer to receive pre-meeting briefings — format, depth, focus areas? If not, add that information. Now run the same meeting prep prompt. Notice how the output changes when the standing context is richer.

**Floor 3 — Meta Prompting:**
Ask Claude to design a reusable *Meeting Prep Skill* for you:

> *"Design a skill for preparing me for client meetings. I will give you the client's name and the meeting objective. The skill should produce a structured brief covering: what I know about them, potential concerns they may have, the questions I should ask, and the outcome I am trying to achieve. Write the full skill instruction set."*

Save that skill as a Gem. Test it on three upcoming meetings.

**Floor 4 — Context Engineering:**
Before your next real meeting prep session, deliberately assemble the context: the client's last email, any prior proposal or document, notes from the last interaction. Attach all of it. Compare the output to a session where you only provided the client's name. The difference is context engineering — and it will be substantial.

**Floor 5 — Memory Engineering:**
Write a one-page *Working Brief* about yourself today. Include: your current role, your most important active relationships, the three things you are focused on this quarter, and your preferred working style. Save it. Attach it at the start of your next five important Claude sessions. After a week, assess whether your interactions feel more continuous and contextually aware.

**Floor 6 — Harness Engineering:**
Design a harness for meeting prep on paper — even if you do not build it today. Map out: what triggers it (calendar event created? Email from client?), what data it pulls (Drive for past documents, Gmail for recent messages, Calendar for the event details), what it produces (a structured brief in a specific format), where that output goes (a document in Drive? An email draft? A note in your project?). Drawing the harness makes it real. Building it — even partially — makes it transformative.

**Track A Your Submission:** Your submission is five artifacts representing Floors 1–5, plus a Floor 6 description. Compile into one document: (1) your raw prompt and improved prompt side by side, (2) your system prompt from Custom Instructions, (3) the reusable Meeting Prep skill instructions Claude wrote for you, (4) your one-page Working Brief, (5) one paragraph describing your ideal harness for meeting prep. Submit all five.

### Track B — Claude Code inside Antigravity IDE

Open Antigravity 2.0 IDE → Editor surface → integrated terminal (Control+backtick on Mac, Ctrl+backtick on Windows) → Claude Code session (claude> prompt). You will work through all six floors in this environment.

1. **Floor 1 — Prompt Engineering.** At the claude> prompt, type a quick first-pass meeting-prep prompt: "Help me prep for a client meeting." Read the output. Now type a second, fully specific version — client name, what you know about them, meeting objective, desired outcome, any concerns you have. Compare both outputs. The gap between them is prompt engineering in action.
2. **Floor 2 — System Prompting.** In the Antigravity IDE file browser on the left, locate your CLAUDE.md file from Chapter 2. Open it and add your professional context for client meetings: your industry, the kinds of clients you work with, how you prefer briefings formatted, what you always and never want included. Save the file. Type "exit" at the terminal, then reopen Claude Code in the same folder. The CLAUDE.md loads automatically — run the same meeting-prep prompt again without restating your context. Notice what you no longer have to say.
3. **Floor 3 — Meta Prompting.** At the claude> prompt, type "/agents" and create a new Meeting Prep specialist. When Claude Code asks for a description, say: "This agent prepares me for client meetings. I give it the client name and meeting objective. It produces a one-page brief covering what I know about this client, their likely concerns or objections, the three questions I should ask in the meeting, and the specific outcome I am trying to achieve." Let Claude Code generate the full specialist. Save it.
4. **Floor 4 — Context Engineering.** Before your next real meeting prep, use the Antigravity IDE file browser to navigate to a folder containing real documents about the client — a past proposal, a meeting note, a contract. In the terminal, reference those files by path in your meeting-prep request. Ask Claude Code: "Using the documents at [path], prepare me for a meeting with [client name] about [objective]." Compare this output to the bare-name output from Floor 1. The difference is context engineering.
5. **Floor 5 — Memory Engineering.** Your CLAUDE.md is the memory layer. Test it: open it in the IDE file browser and add one sentence about a client you meet with regularly — their priorities and your relationship. Save the file. Start a fresh Claude Code session and ask about that client without quoting what you just wrote. Claude Code reads the CLAUDE.md automatically. The relevant context appears without you having to supply it.
6. **Floor 6 — Harness Engineering.** Ask Claude Code: "Design a harness for my meeting prep workflow. It should fire when a new calendar event is created with an external contact, pull the contact name and any prior documents about them, run my Meeting Prep specialist, and save the briefing as a file in my workshop folder. Describe each step in plain English and identify what tool connections the harness would require." Claude Code will produce a detailed harness specification as a file you can see in the IDE file browser.
7. Save the outputs from all six floors as files in your workshop folder. Use the Antigravity IDE file browser to organize them.

**Your Submission:** Compile into one document: (1) raw vs. improved prompt pair from Floor 1, (2) your updated CLAUDE.md from Floor 2, (3) Meeting Prep specialist definition from Floor 3, (4) the context-rich output from Floor 4 alongside the bare-name output, (5) the harness specification from Floor 6. Write one sentence: what is the cumulative weekly time savings if all six floors are fully operational for meeting prep? Submit all five items + one sentence.

### Track C — Gemini + Antigravity 2.0 IDE

Open Gemini (gemini.google.com) and sign in. Open Antigravity 2.0 IDE and press CMD+E (Mac) / CTRL+E (Windows) to switch to Agent Manager. You will use both surfaces through all six floors.

1. **Floor 1 — Prompt Engineering (Gemini).** Start a new Gemini conversation. Type a quick first-pass meeting-prep prompt. Read the response. Start a second conversation and write a fully specific version — client name, what you know, objective, desired outcome. Compare both responses. The gap is prompt engineering.
2. **Floor 2 — System Prompting (Gemini Gem).** Open Gem Manager → New Gem. Name it "Meeting Prep." In the instructions field, write your professional context: your role, the type of clients you work with, how you want briefings formatted, what you always and never want. Save the Gem. Open it and run the same meeting-prep prompt from inside the Gem. The instructions load silently — notice what you no longer have to explain.
3. **Floor 3 — Meta Prompting (Gemini).** Inside your Meeting Prep Gem, ask: "Improve the instructions for this Gem. I want it to always produce: a section on what I know about the client, a section on their likely concerns, three specific questions I should ask, and one sentence stating my desired outcome. Write me the complete updated Gem instructions." Copy the result back into the Gem's instruction field and save.
4. **Floor 4 — Context Engineering (Gemini).** Run a meeting prep request in your Gem twice. First, just the client name and meeting objective — nothing else. Then, with a real context attachment: paste in the client's last email, a past proposal summary, or any prior notes. Compare the two outputs. The richer context produces dramatically more specific and useful output.
5. **Floor 5 — Memory Engineering (Agent Manager).** In Antigravity Agent Manager, create a new Project called "Professional Context." In the Project Description field, write your Working Brief: your role, your three most important current priorities, your five key relationships, your active projects, and how you prefer outputs formatted. Save it. Start a test Agent task inside this Project and ask about one of your current projects without re-explaining any context. The Project Description is the memory layer — it loads automatically.
6. **Floor 6 — Harness Engineering (Agent Manager).** Create a new recurring Agent task in the Agent Manager. In the task description, write: "Every Monday at 7:30 AM, prepare one-page briefings for all client meetings on my calendar this week. For each meeting: search the web for any recent news about the client's company, summarize what I know about them from the project context, and produce a briefing in the standard format." Submit it as a scheduled task. That is the harness — a standing workflow that fires automatically.
7. You have now used both surfaces across all six floors: Gemini for conversations and prompt layers, Agent Manager for memory and harness.

**Your Submission:** Compile into one document: (1) raw vs. improved prompt pair from Floor 1, (2) your Meeting Prep Gem instructions after Floor 3 improvements, (3) the two context-engineering outputs side by side from Floor 4, (4) your Project Description (Working Brief) from Floor 5, (5) the harness task description from Floor 6. Write one sentence: which of the six floors produced the single biggest improvement in output quality for you? Submit all five items + one sentence.

### Reflection

After completing the six floors in one of the three tracks, answer:

*Where did you spend the most mental energy before this exercise — and how much of that energy can now be handled by the system you just built?*

That gap — between the energy you were spending and the energy the system now handles — is the measure of what these six disciplines are worth.

Bonus reflection if you ran more than one track: *Which surface felt right for which floor? Most professionals find prompting and context engineering feel native in a conversational tool (Desktop or Gemini), while harnesses feel right in an IDE-class environment (Claude Code or the Agent Manager). Your team's adoption pattern is probably hiding inside that preference.*

---
*Applied Exercise for Chapter 5 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
