# Applied Exercise — Chapter 5: The Six Engineering Disciplines
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Across All Six Disciplines

This exercise takes you through one complete task — from raw prompt to full harness — to give you the experience of what each discipline adds.

**Choose your task:** Pick one recurring piece of work. Something you do at least weekly. Something with real professional stakes. For the purposes of this exercise, let us use: *preparing for a client meeting.*

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks climb the same six floors on the three surface types this book uses throughout: a **chat assistant** (Track A — the desktop app you configured in Chapter 2), a **terminal agent** that lives inside a development environment (Track B — where the six floors become *files in a folder*), and an **ecosystem-native assistant paired with an agent-orchestration workspace** (Track C — where the top floors become background agents). Product names, commands, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch05-companion.
:::

### Track A — Chat Assistant

**Floor 1 — Prompt Engineering:**
Write a prompt from scratch asking your assistant to help you prepare for a client meeting. Do not overthink it. Just write what you would normally write.

Now evaluate it honestly. Is it specific enough? Does it tell the AI who the client is, what you know about them, what the meeting is for, what outcome you need? Rewrite it with those specifics. Compare the two outputs. The difference is prompt engineering.

**Floor 2 — System Prompting:**
Open your standing instructions — the system prompt you wrote in Chapter 2. (Your tool will call this *preferences*, *custom instructions*, or a *project brief*; the concept is the same.) Read it. Does it tell your assistant what kind of client relationships you manage? What industry you are in? How you prefer to receive pre-meeting briefings — format, depth, focus areas? If not, add that information. Now run the same meeting prep prompt. Notice how the output changes when the standing context is richer.

**Floor 3 — Meta Prompting:**
Ask your assistant to design a reusable *Meeting Prep Skill* for you:

> *"Design a skill for preparing me for client meetings. I will give you the client's name and the meeting objective. The skill should produce a structured brief covering: what I know about them, potential concerns they may have, the questions I should ask, and the outcome I am trying to achieve. Write the full skill instruction set."*

Save that skill in your tool's reusable container — a Project, a Gem, whatever your tool calls it. Test it on three upcoming meetings.

**Floor 4 — Context Engineering:**
Before your next real meeting prep session, deliberately assemble the context: the client's last email, any prior proposal or document, notes from the last interaction. Attach all of it. Compare the output to a session where you only provided the client's name. The difference is context engineering — and it will be substantial.

**Floor 5 — Memory Engineering:**
Write a one-page *Working Brief* about yourself today. Include: your current role, your most important active relationships, the three things you are focused on this quarter, and your preferred working style. Save it. Attach it at the start of your next five important sessions. After a week, assess whether your interactions feel more continuous and contextually aware.

**Floor 6 — Harness Engineering:**
Design a harness for meeting prep on paper — even if you do not build it today. Map out: what triggers it (calendar event created? Email from client?), what data it pulls (Drive for past documents, Gmail for recent messages, Calendar for the event details), what it produces (a structured brief in a specific format), where that output goes (a document in Drive? An email draft? A note in your project?). Drawing the harness makes it real. Building it — even partially — makes it transformative.

**Your Submission:** Your submission is five artifacts representing Floors 1–5, plus a Floor 6 description. Compile into one document: (1) your raw prompt and improved prompt side by side, (2) your standing instructions after the Floor 2 update, (3) the reusable Meeting Prep skill instructions your assistant wrote for you, (4) your one-page Working Brief, (5) one paragraph describing your ideal harness for meeting prep. Submit all five.

### Track B — Terminal Agent: The Six Floors as Files

On this surface the six floors stop being settings and become *files in a working folder* — a standing brief you can open, a specialist definition you can version, a harness specification you can hand to an engineer. That difference is the track's lesson. Open your terminal agent inside the workshop folder you created in Chapter 2; the current commands and menu paths are on the companion page (cognitioneconomy.net/ch05-companion).

1. **Floor 1 — Prompt Engineering.** At the agent's prompt, type a quick first-pass meeting-prep request: "Help me prep for a client meeting." Read the output. Now type a second, fully specific version — client name, what you know about them, meeting objective, desired outcome, any concerns you have. Compare both outputs. The gap between them is prompt engineering in action.

2. **Floor 2 — System Prompting: edit the standing brief as a file.** In the file browser, open the context file you built in Chapter 2 — the standing brief the agent reads automatically at the start of every session in this folder. Add your professional context for client meetings: your industry, the kinds of clients you work with, how you prefer briefings formatted, what you always and never want included. Save it. End the session and start a fresh one in the same folder — the brief loads automatically. Run the same meeting-prep prompt again without restating your context. Notice what you no longer have to say.

3. **Floor 3 — Meta Prompting: commission a specialist.** Ask the agent to create a reusable Meeting Prep specialist (your tool has a built-in way to define one; the current command is on the companion page). Describe the job in plain English: *"This specialist prepares me for client meetings. I give it the client name and meeting objective. It produces a one-page brief covering what I know about this client, their likely concerns or objections, the three questions I should ask in the meeting, and the specific outcome I am trying to achieve."* Let the agent generate the full definition — then read what it wrote and edit it. It is your specialist, not the tool's.

4. **Floor 4 — Context Engineering: point at real documents.** Before your next real meeting prep, navigate to a folder containing real documents about the client — a past proposal, a meeting note, a contract. Ask the agent: *"Using the documents at [path], prepare me for a meeting with [client name] about [objective]."* Compare this output to the bare-name output from Floor 1. The difference is context engineering.

5. **Floor 5 — Memory Engineering: test what the file carries forward.** Your context file is the memory layer. Test it: add one sentence about a client you meet with regularly — their priorities and your relationship. Save the file. Start a fresh session and ask about that client without quoting what you just wrote. The relevant context appears without you having to supply it — because it lives in a file you own, not in a vendor's memory feature.

6. **Floor 6 — Harness Engineering: write the specification.** Ask the agent: *"Design a harness for my meeting prep workflow. It should fire when a new calendar event is created with an external contact, pull the contact name and any prior documents about them, run my Meeting Prep specialist, and save the briefing as a file in my workshop folder. Describe each step in plain English and identify what tool connections the harness would require."* The agent will produce a detailed harness specification as a file.

7. **Organize the artifacts.** Save the outputs from all six floors as files in your workshop folder. Six floors, six files — a stack you can reread, revise, and carry to any tool.

**Your Submission:** Compile into one document: (1) raw vs. improved prompt pair from Floor 1, (2) your updated context file from Floor 2, (3) the Meeting Prep specialist definition from Floor 3, (4) the context-rich output from Floor 4 alongside the bare-name output, (5) the harness specification from Floor 6. Write one sentence: what is the cumulative weekly time savings if all six floors are fully operational for meeting prep? Submit all five items + one sentence.

### Track C — Ecosystem Assistant + Orchestration Workspace

This track climbs the lower floors in your ecosystem-native assistant and the upper floors in an agent-orchestration workspace — the surface where memory lives at project scope and the harness becomes a scheduled background agent. The current tool names, the toggle that opens the orchestration view, and every click-path are on the companion page (cognitioneconomy.net/ch05-companion).

1. **Floor 1 — Prompt Engineering (assistant).** Start a new conversation in your ecosystem-native assistant. Type a quick first-pass meeting-prep prompt. Read the response. Start a second conversation and write a fully specific version — client name, what you know, objective, desired outcome. Compare both responses. The gap is prompt engineering.

2. **Floor 2 — System Prompting: set the persona at container scope.** Create a new reusable container (a Gem, in this chapter's example) named "Meeting Prep." In its instructions field, write your professional context: your role, the type of clients you work with, how you want briefings formatted, what you always and never want. Save it. Open the container and run the same meeting-prep prompt from inside it. The instructions load silently — notice what you no longer have to explain.

3. **Floor 3 — Meta Prompting: let the container improve itself.** Inside your Meeting Prep container, ask: *"Improve the instructions for this container. I want it to always produce: a section on what I know about the client, a section on their likely concerns, three specific questions I should ask, and one sentence stating my desired outcome. Write me the complete updated instructions."* Copy the result back into the container's instruction field and save. You just used the AI to rewrite its own job description.

4. **Floor 4 — Context Engineering: run the A/B test.** Run a meeting prep request in your container twice. First, just the client name and meeting objective — nothing else. Then, with real context attached: the client's last email, a past proposal summary, any prior notes. Compare the two outputs. The richer context produces dramatically more specific and useful output.

5. **Floor 5 — Memory Engineering: set the brief at project scope.** Open your agent-orchestration workspace and create a new project called "Professional Context." In the project's description field, write your Working Brief: your role, your three most important current priorities, your key relationships, your active projects, and how you prefer outputs formatted. Save it. Start a test agent task inside this project and ask about one of your current projects without re-explaining any context. The project description is the memory layer — it loads automatically for every task in the project.

6. **Floor 6 — Harness Engineering: schedule the standing workflow.** In the orchestration workspace, create a recurring agent task. Describe it in plain English: *"Every Monday morning, prepare one-page briefings for all client meetings on my calendar this week. For each meeting: search the web for any recent news about the client's company, summarize what I know about them from the project context, and produce a briefing in the standard format."* Submit it as a scheduled task. That is the harness — a standing workflow that fires automatically, on a trigger, without you in the loop. (If your tool cannot schedule tasks yet, save the task description as your harness specification and log that gap — it is a verification answer, not a failure.)

7. You have now used both surfaces across all six floors: the assistant for the prompt and context layers, the orchestration workspace for memory and harness.

**Your Submission:** Compile into one document: (1) raw vs. improved prompt pair from Floor 1, (2) your Meeting Prep container instructions after the Floor 3 improvements, (3) the two context-engineering outputs side by side from Floor 4, (4) your project description (Working Brief) from Floor 5, (5) the harness task description from Floor 6. Write one sentence: which of the six floors produced the single biggest improvement in output quality for you? Submit all five items + one sentence.

:::{admonition} Is this still true?
:class: note
This chapter's disciplines are durable; your tool's memory behavior is not. Before you rely on anything here, run two checks:

1. **Ask your AI what it knows about you.** Open a brand-new session and ask: *"What do you already know about me from previous sessions, and where is that stored?"* Whatever it says is the memory layer you currently do not control. Decide whether you are comfortable with it — and either way, keep your own Working Brief as the system of record.
2. **Find your standing instructions.** Open your tool's settings and confirm where the standing brief lives now. The label moves between releases — *custom instructions*, *preferences*, *project brief* — but the concept does not. Current menu paths are on the companion page at cognitioneconomy.net/ch05-companion.
:::

### Reflection

After completing the six floors in one of the three tracks, answer:

*Where did you spend the most mental energy before this exercise — and how much of that energy can now be handled by the system you just built?*

That gap — between the energy you were spending and the energy the system now handles — is the measure of what these six disciplines are worth.

Bonus reflection if you ran the exercise on more than one surface: *Which surface felt right for which floor? Most professionals find prompting and context engineering feel native in a chat assistant, while harnesses feel right in an IDE-class environment — a terminal agent or an agent-orchestration workspace. Your team's adoption pattern is probably hiding inside that preference.*

---
*Applied Exercise for Chapter 5 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
