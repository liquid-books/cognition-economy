# Applied Exercise — Chapter 6: Plan Mode — Think Before You Build
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Run a Real Task Through Plan Mode

This exercise takes one piece of work you actually need to do this week and runs it through the full Plan Mode sequence.

**Step 1: Choose the task.**
Pick something real. Something with actual stakes — a document someone will read, a decision someone will act on, a communication that shapes a relationship. Not a practice exercise. Real work.

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code inside Antigravity IDE:** For students who want to work in a professional developer environment. Requires Antigravity 2.0 IDE (antigravity.google/docs/ide-overview) with Claude Code running in the integrated terminal.
- **Track C — Gemini + Antigravity 2.0 IDE:** For students in the Google ecosystem. Uses Gemini (gemini.google.com) for AI conversations and the Antigravity 2.0 IDE Agent Manager for orchestration.
:::

### Track A — Claude Desktop

**Step 2: State the objective without specifying the approach.**
Open Claude Desktop and describe what you need to achieve — not how you want it done. The goal, the audience, the context, the constraints. Then say:

> *"Before you do anything, think through this task out loud. Tell me your plan: what you will do, in what order, what assumptions you are making, what you would need to know to do this well, and what could go wrong. Do not begin the actual work until I have reviewed and approved your plan."*

**Step 3: Read the plan critically.**
When Claude returns a plan, read it as a skeptic. Ask yourself:
- What assumptions is it making that I have not explicitly confirmed?
- Is the scope correct — not too narrow, not too broad?
- Is the sequence logical? Are there steps out of order?
- What is it not planning to do that it probably should?
- Does it know enough about the audience to produce something they will actually use?

**Step 4: Push back.**
This is the step most people skip. Do not just approve the plan because it looks reasonable. Challenge at least one assumption. Add context it was missing. Ask it to revise the approach to something you disagree with. See how it responds.

A good plan improves under scrutiny. A weak plan falls apart. You want to know which one you have before you commit to execution.

**Step 5: Approve and execute.**
Once the plan holds up — once you have pushed back, it has revised, and you are genuinely confident in the direction — give your explicit approval:

> *"The plan looks right. Proceed with execution."*

Then watch what happens. The output, built on a scrutinized and approved foundation, will be qualitatively different from what you would have gotten if you had just asked for the result directly.

**Track A Your Submission:** Your submission is the real task you ran through Plan Mode — four parts in one document: (1) Claude's original plan, (2) your pushback (what you challenged and why), (3) Claude's revised plan, (4) the final output after execution. Write one sentence at the top: what did the planning phase surface that you would not have caught until the output was already wrong? Submit the one sentence + four-part document.

### Track B — Claude Code inside Antigravity IDE

1. Open Antigravity 2.0 IDE → Editor surface → integrated terminal (Control+backtick) → Claude Code (claude> prompt ready).
2. Create a new file in the IDE file browser called "plan-review.txt." You will use this to take notes as you review Claude Code's plan.
3. Choose a real task you need to complete this week — something with actual stakes. Write down its objective, audience, and key constraints in plain English before you type anything.
4. At the claude> prompt, describe the task objective without specifying the approach — tell Claude Code what outcome you need, who it is for, and what constraints apply. Then add this exact instruction: "Before you start any work, give me your plan. Tell me what you will do in what order, what assumptions you are making, what information you still need, and what could go wrong. Do not begin executing until I explicitly approve the plan."
5. When Claude Code returns the plan, open your plan-review.txt file in the IDE editor pane and write down three things: (a) one assumption in the plan that is wrong or needs confirmation, (b) one step that is out of order or missing entirely, (c) one piece of context Claude Code does not have that would change the output significantly.
6. Return to the terminal and push back on all three issues. Give Claude Code the corrections and missing context. Ask it to revise the plan to address your feedback.
7. Read the revised plan. If it is now solid — if you cannot find a significant remaining flaw — type: "The plan looks right. Proceed with execution."
8. Watch Claude Code execute in the terminal. In the Antigravity IDE file browser, you will see files being created or modified as Claude Code works through each step of the plan. The IDE's diff viewer shows you exactly what changed in any file.
9. When execution is complete, compare the final output to what you would have gotten with no plan step — you can test this by starting a second Claude Code session and asking for the same output directly without invoking Plan Mode.
10. Save the plan, your plan-review.txt critique, the revised plan, and the final output as four files in your workshop folder.

**Your Submission:** Compile into one document: (1) Claude Code's original plan, (2) your plan-review.txt critique, (3) the revised plan after your pushback, (4) the final execution output. Write one sentence: what specifically did Plan Mode catch that a direct request would have gotten wrong? Submit the one sentence + four-part document.

### Track C — Antigravity 2.0 IDE Agent Manager

1. Open Antigravity 2.0 IDE and press CMD+E (Mac) or CTRL+E (Windows) to switch to Agent Manager.
2. Choose the same real task you would use in Track A or B — something with genuine professional stakes.
3. You will run the task twice in two separate workspaces so you can compare the results directly. This comparison is the core of the exercise.
4. **Run 1 — No Plan:** Click to create a new workspace (or new Project). Start a new Agent task. Give the agent the full task description — objective, audience, constraints — and submit it immediately, with no instruction to plan first. Let it run to completion without interruption.
5. When the Run 1 Artifact appears, click into it and review the output carefully. Open a note or document and write down: two or three places where the agent made an assumption you did not want, or produced something slightly off from what you needed.
6. **Run 2 — With Plan:** Create a second new workspace. Start a new Agent task. Begin your task description with this instruction: "Before you begin any work on this task, produce a Plan Artifact first. The plan must include: your approach in bullet points, the steps you will take in order, the assumptions you are making, and any questions you have for me. After producing the plan, stop and wait for my written approval before proceeding to execution."
7. When the Plan Artifact appears, read it as a skeptic. Type a message pushing back on at least one assumption or requesting one specific change. The agent will revise the Plan Artifact.
8. Once the revised plan looks accurate, type: "Plan approved. Proceed to execution." The agent continues and produces the final output Artifact.
9. Place the two final Artifacts side by side — Run 1 (no plan) and Run 2 (plan approved). Compare them on three dimensions: specificity to your actual requirements, accuracy of assumptions, structural quality of the output.
10. Also compare the Artifacts against the critique notes you wrote in Step 5 — did the Run 2 Artifact avoid the mistakes you identified in Run 1?

**Your Submission:** Submit a document containing: (1) the Run 1 Artifact with your critique notes from Step 5 annotated, (2) the Run 2 Plan Artifact (what the agent planned), (3) your pushback message from Step 7, (4) the Run 2 final Artifact. Write two sentences: (1) what the no-plan run got wrong that the plan-approved run got right, and (2) what category of professional tasks do you think benefits most from Plan Mode? Submit the four-part document + two sentences.

### Reflection

*What did the planning phase surface that you would not have caught until the output was already wrong?*

Write it down. That specific thing — whatever it was — is the value of Plan Mode. And it will happen every time.

If you ran more than one track: *Which surface made you push back the hardest on the plan — the conversational thread, the terminal output, or the formal plan Artifact? The surface that produces the most friction in your reviewing eye is the surface that will catch the most mistakes.*

---
*Applied Exercise for Chapter 6 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
