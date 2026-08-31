# Applied Exercise — Chapter 10: Agent Teams — From Solo to Squad
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Run Your First Agent Team

*Estimated time: 25–30 minutes. You'll produce a short comparative-research brief and a working goal-condition session.*

The point of this lab is to feel the difference between solo work, sub-agent work, and team work — in one sitting, on a problem you actually care about. Pick a real research question from your work before you start. Something with at least two angles that could be investigated in parallel: two competitors, two customer segments, two strategic options. The exercise loses its value if you use a made-up topic.

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace built for running several agents at once (Track C). Product names, download links, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch10-companion.
:::

### Track A — Chat Assistant

You do not need parallel agents to feel what a team does. You can simulate the choreography — parallel briefs, then synthesis — in a single chat window.

1. Open your chat assistant and start a new conversation.
2. Describe a real project on your plate that naturally breaks into three workstreams. A product launch is the cleanest example: *marketing*, *operations*, and *finance*. A hiring push works too: *sourcing*, *interviewing*, *onboarding*.
3. Paste this prompt: *"Break this project into three parallel tracks. For each track, write a one-paragraph brief addressed to the person who will lead it — what they own, what 'done' looks like, what they need from the other two tracks."*
4. Read the three briefs. Then paste a follow-up: *"Now act as the project lead. Synthesize those three briefs into a single coordinated plan with sequencing, dependencies, and the first three actions for each track."*
5. You just ran a team. One assistant played three roles, then put on a fourth hat to coordinate them. That is exactly what a multi-agent system does — only the system does it in parallel, in separate workspaces, without you holding the thread.

**Your Submission:** Your submission is the assistant's full output from the team simulation — the three parallel workstream briefs and the coordinated synthesis. Copy all four parts into one document. Write two sentences: (1) which team brief was most useful and why, and (2) how does the synthesized plan differ from what you would have produced working on one workstream at a time? Submit the four-part output + two sentences.

### Track B — Terminal Agent

1. **Make sure agent teams are enabled in your terminal agent.** When this book went to press the feature was behind an opt-in setting; it may be on by default by the time you read this. The one-line setup is on the companion site (cognitioneconomy.net/ch10-companion).

2. Open a new session. Tell the agent in plain English: *"Create a two-teammate agent team to investigate [your research question]. Name them Alex and Sam. Alex investigates [angle one]. Sam investigates [angle two]. Have them message each other when one of them finds something the other should know about. The deliverable is a one-page comparative brief."*

3. Watch the team start. You will see the lead spawn Alex and Sam. The shared task list will appear. Each teammate will start their investigation in parallel. Check in on each teammate's view to watch what each is doing. Do not interrupt for the first five minutes.

4. After five minutes, message one teammate directly with a sharpening question. Something like, *"Alex, what specific evidence supports your strongest finding so far?"* Notice that the message goes only to Alex, not to Sam. This is the lateral channel in action.

5. **Set a goal condition** so the work finishes without you having to prompt for the rest of it: *the one-page comparative brief is complete, includes findings from both Alex and Sam with at least three specific data points each, and the task list is empty.* The exact command syntax for your tool is on the companion page. Walk away for ten minutes.

6. Come back. Read the brief. Ask the lead to clean up the team. Save the brief as your artifact.

**Your Submission:** Your submission is the synthesis document the agent team produced — the final briefing after the parallel investigations were combined. Copy the full synthesis into a document. Write two sentences: (1) what did the parallel investigation approach surface that a sequential single-agent approach would have missed, and (2) what real research or strategy task in your work would benefit most from running as a parallel team? Submit the synthesis + two sentences.

### Track C — Agent-Orchestration Workspace

1. **Open the orchestration view.** Switch from the editing surface to the manager view — the birds-eye surface designed for overseeing multiple parallel agents across workspaces. The current tool name and the toggle that opens this view are on the companion page (cognitioneconomy.net/ch10-companion).

2. From the manager view, start two new agent tasks in two separate workspaces. Workspace one: *"Investigate [angle one] of [your research question]. Produce findings with sources."* Workspace two: *"Investigate [angle two] of [your research question]. Produce findings with sources."* The manager view will now show both agents working in parallel — this is the visual equivalent of the team you ran in Track A, just expressed differently.

3. Watch the dashboard. Each agent will produce structured deliverables as it works — the documents, notes, and outputs of its investigation. Click into either agent's tile to see what it is doing in detail, the same way you would check in on a teammate's session in Track B.

4. When both agents have produced initial findings, start a third agent in a synthesis workspace. Give it both prior workspaces as context and ask it to produce the one-page comparative brief.

5. Review the deliverables. Save the brief.

**Your Submission:** Your submission is all three deliverables from your workspaces — the two parallel investigation outputs and the synthesis that combined them. Copy all three into one document. Write two sentences: (1) what was different about the two parallel investigations and how did the synthesis reconcile them, and (2) name one recurring project in your work that you could restructure as a parallel agent team and what the two parallel workstreams would be. Submit three deliverables + two sentences.

### Reflection

Write two or three sentences answering: *If you completed Track B, where did the lateral communication between teammates produce something that isolated parallel work would not have? If you completed Track C, where did the parallel-but-isolated workspace structure leave synthesis work that a communicating team would have done mid-flight? And if you completed Track A, what did the synthesis step surface that the three separate briefs, read on their own, did not?* The honest answer is the foundation of knowing when to reach for which shape.

The bigger lesson: agent teams and parallel workspace orchestration are not the same shape, but they solve overlapping problems. The professional skill is recognizing which shape fits the work in front of you, and using the right one — not because it is the trendy choice, but because it is the right tool for the job. Solo, sub-agent, team, goal condition. Four moves. Use them deliberately.

:::{admonition} Is this still true?
:class: note
Before you run your first team, spend two minutes checking your own tool: (1) Are agent teams available on your plan, and are they on by default or behind a setting? (2) What does your tool call the finish-line feature, and how strict is its evaluator? (3) How many teammates does your tool recommend as a starting point? The names and settings change between releases; the architecture — lead, teammates, shared task list, lateral messages, goal condition — does not. Current details live at cognitioneconomy.net/ch10-companion.
:::

---
*Applied Exercise for Chapter 10 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
