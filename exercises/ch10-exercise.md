# Applied Exercise — Chapter 10: Agent Teams — From Solo to Squad
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Run Your First Agent Team

*Estimated time: 25–30 minutes. You'll produce a short comparative-research brief and a working `/goal` session.*

The point of this lab is to feel the difference between solo work, sub-agent work, and team work — in one sitting, on a problem you actually care about. Pick a real research question from your work before you start. Something with at least two angles that could be investigated in parallel: two competitors, two customer segments, two strategic options. The exercise loses its value if you use a made-up topic.

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code:** For students using Claude Code. Reference the quickstart at code.claude.com/docs/en/quickstart.
- **Track C — Antigravity 2.0 IDE:** For students using the Antigravity 2.0 IDE Agent Manager. Reference antigravity.google/docs/ide-overview.
:::

### Track A — Claude Desktop

You do not need parallel agents to feel what a team does. You can simulate the choreography — parallel briefs, then synthesis — in a single Claude Desktop window.

1. Open **Claude Desktop** (claude.ai/download) or **claude.ai** in your browser.
2. Describe a real project on your plate that naturally breaks into three workstreams. A product launch is the cleanest example: *marketing*, *operations*, and *finance*. A hiring push works too: *sourcing*, *interviewing*, *onboarding*.
3. Paste this prompt: *"Break this project into three parallel tracks. For each track, write a one-paragraph brief addressed to the person who will lead it — what they own, what 'done' looks like, what they need from the other two tracks."*
4. Read the three briefs. Then paste a follow-up: *"Now act as the project lead. Synthesize those three briefs into a single coordinated plan with sequencing, dependencies, and the first three actions for each track."*
5. You just ran a team. One Claude played three roles, then put on a fourth hat to coordinate them. That is exactly what a multi-agent system does — only the system does it in parallel, in separate workspaces, without you holding the thread.

**Your Submission:** Your submission is Claude's full output from the team simulation — the three parallel workstream briefs and the coordinated synthesis. Copy all four parts into one document. Write two sentences: (1) which team brief was most useful and why, and (2) how does the synthesized plan differ from what you would have produced working on one workstream at a time? Submit the four-part output + two sentences.

### Track B — Claude Code

1. Update Claude Code to the latest version. Confirm you are on version 2.1.32 or later. Open Claude Code's settings file and enable agent teams by adding the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` flag set to `1`. The official setup guidance lives at https://code.claude.com/docs/en/agent-teams. Restart Claude Code so the setting takes effect.

2. Open a new session. Tell Claude in plain English: *"Create a two-teammate agent team to investigate [your research question]. Name them Alex and Sam. Alex investigates [angle one]. Sam investigates [angle two]. Have them message each other when one of them finds something the other should know about. The deliverable is a one-page comparative brief."*

3. Watch the team start. You will see the lead spawn Alex and Sam. The shared task list will appear. Each teammate will start their investigation in parallel. Use the keyboard shortcut to cycle through teammates and watch what each is doing. Do not interrupt for the first five minutes.

4. After five minutes, message one teammate directly with a sharpening question. Something like, *"Alex, what specific evidence supports your strongest finding so far?"* Notice that the message goes only to Alex, not to Sam. This is the lateral channel in action.

5. Set a goal to finish the work without you having to prompt for the rest of it. Type `/goal the one-page comparative brief is complete, includes findings from both Alex and Sam with at least three specific data points each, and the task list is empty`. Reference https://code.claude.com/docs/en/goal for the full syntax. Walk away for ten minutes.

6. Come back. Read the brief. Ask the lead to clean up the team. Save the brief as your artifact.

**Your Submission:** Your submission is the synthesis document the agent team produced — the final briefing after the parallel investigations were combined. Copy the full synthesis into a document. Write two sentences: (1) what did the parallel investigation approach surface that a sequential single-agent approach would have missed, and (2) what real research or strategy task in your work would benefit most from running as a parallel team? Submit the synthesis + two sentences.

### Track C — Antigravity 2.0 IDE

1. Open Google Antigravity 2.0 IDE. Press `CMD+E` (Mac) or `CTRL+E` (Windows) to switch into the Agent Manager surface. This is the birds-eye view Google designed for managing multiple parallel agents across workspaces. The official documentation is at https://antigravity.google/docs/ide-overview.

2. From Agent Manager, start two new agent tasks in two separate workspaces. Workspace one: *"Investigate [angle one] of [your research question]. Produce findings with sources."* Workspace two: *"Investigate [angle two] of [your research question]. Produce findings with sources."* The Agent Manager view will now show both agents working in parallel — this is the visual equivalent of the team you ran in Track A, just expressed differently.

3. Watch the Agent Manager dashboard. Each agent will create Artifacts as it works — the documents, notes, and outputs the agents produce. Click into either agent's tile to see what they are doing in detail, the same way you would tab into a teammate's pane in Claude Code.

4. When both agents have produced initial findings, start a third agent in a synthesis workspace. Give it both prior workspaces as context and ask it to produce the one-page comparative brief.

5. Review the Artifacts. Save the brief.

**Your Submission:** Your submission is all three Artifacts from your Agent Manager workspaces — the two parallel investigation Artifacts and the synthesis that combined them. Copy all three into one document. Write two sentences: (1) what was different about the two parallel investigations and how did the synthesis reconcile them, and (2) name one recurring project in your work that you could restructure as a parallel agent team and what the two parallel workstreams would be. Submit three Artifacts + two sentences.

### Reflection

Write two or three sentences answering: *Where did the lateral communication in Track A produce something the parallel-but-isolated structure of Track B did not? And where, if anywhere, did Track B's visual workspace separation produce clarity that Track A's terminal-cycling did not?* The honest answer to those two questions is the foundation of knowing when to reach for which tool.

The bigger lesson: agent teams and parallel workspace orchestration are not the same shape, but they solve overlapping problems. The professional skill is recognizing which shape fits the work in front of you, and using the right one — not because it is the trendy choice, but because it is the right tool for the job. Solo, sub-agent, team, goal. Four moves. Use them deliberately.

---
*Applied Exercise for Chapter 10 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
