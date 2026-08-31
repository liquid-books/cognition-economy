# Applied Exercise — Chapter 12: Self-Learning Systems — How Your AI Gets Smarter Over Time
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your Reflection Loop This Week

*Estimated time: 25–30 minutes. You will produce a personal reflection template, a refreshed standing brief, and a recurring Friday review block on your calendar.*

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace built for running several agents at once (Track C). Product names, download links, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch12-companion.
:::

### Track A — Chat Assistant

Self-learning systems sound exotic. The loop underneath them is not. It is *do the work, judge the work, write down the lesson, paste the lesson next time.* You can run that loop today in a single chat tab.

1. Open your AI assistant — the chat surface you configured in Chapter 2.
2. Ask it to do a real recurring task you actually need done — a status email, a weekly summary, a one-page analysis, a customer reply draft.
3. Read the output and give explicit feedback, out loud, in the chat: *"This was good because X. This missed Y. Next time, do Z instead."* Be specific. Vague feedback teaches nothing.
4. Ask the assistant to revise the task using your feedback. Read the second version. Confirm the lesson stuck.
5. Copy that feedback into a plain text note titled with the task name — *email-drafts-memory.txt*, *weekly-summary-memory.txt*. The next time you run this task, paste the memory note at the top of a fresh conversation before your request.
6. Now run the review half of the loop. Gather notes or transcripts from your last five significant AI sessions and paste them in. Ask: *"Identify any moments where I had to redirect you more than once, or where the output needed substantial editing. What patterns do you see? Propose three to five candidate rules — written as direct instructions — that would prevent these patterns from recurring."* Accept the rules that match something you have noticed more than once; reject the situational ones. Add the keepers to your standing brief under a section called "Operating Rules."
7. Create a recurring calendar event for every Friday at 4:00 PM titled "AI Learning Review — 30 min." In the event description, paste the three-step weekly review process from this chapter: scan outputs, identify failure patterns, update standing brief. Set it to recur weekly with no end date.

That is the entire self-learning loop: produce, judge, encode, recall — plus a standing appointment to keep it alive. The systems in this chapter automate the encoding and recall. You are doing it by hand — and that is the right place to start.

**Your Submission:** Your submission is your feedback loop in four parts: (1) the assistant's original output on the real recurring task you chose, (2) the explicit feedback you gave — what was good, what missed, what to do differently, (3) the revised output after incorporating the feedback, and (4) the "Operating Rules" you added to your standing brief after the five-session review. Copy all four into one document. Write one sentence: what specific instruction in your feedback produced the biggest visible improvement in the revised output? Submit the four-part document + one sentence.

### Track B — Terminal Agent

The terminal agent runs the same loop as Track A with one structural difference that changes what you learn: the lessons live in a *file*, not a settings screen. Your terminal agent loads a context file automatically at the start of every session — the file you built in Chapter 7. Whatever you write there persists, inspectably, in a format you own. This track turns that file into a self-improving one. The current filename conventions and setup steps are on the companion page (cognitioneconomy.net/ch12-companion); what matters here is which decision each step encodes.

1. **Open your memory layer as a file.** In your terminal agent, open the auto-loaded context file — the standing context document you built in Chapter 7, or a fresh one if you skipped that exercise. This file is where the loop's lessons will live. Current filename for your tool: companion site.
2. **Gather the evidence.** Collect notes or transcripts from your last five significant sessions with the agent and paste them in. Then ask: *"Identify any moments where I had to redirect you more than once, or where the output needed substantial editing. What patterns do you see?"* Read what comes back without arguing with it.
3. **Turn patterns into candidate rules.** Based on those patterns, ask the agent to propose three to five candidate refinements to your context file — written as direct instructions, not narrative. For example: *"When drafting client emails, lead with the ask before the context."*
4. **Curate — accept the recurring, reject the situational.** Review the candidates. Accept the ones that match a pattern you have noticed more than once. Reject the ones that feel like one-offs. Have the agent add the accepted rules to a new section of the context file called "Operating Rules," and save the file. This is the pruning discipline from this chapter, applied at the moment of writing.
5. **Test that the lesson persists.** Start a fresh session — so the agent loads the updated file cold — and run one of the recurring tasks that produced the old failure pattern. Confirm the new rule shows up in the output without you restating it. If it does not, the rule is written too vaguely; tighten it and test again.
6. **Make reflection reusable.** Ask the agent to generate a reflection prompt you can paste at the end of any significant task. It should ask the two-question pattern from this chapter — what worked, what to change — and write the answers to a journal file. Save that prompt where you can find it.
7. **Put the review on the calendar.** Create a recurring calendar event for every Friday at 4:00 PM titled "AI Learning Review — 30 min." In the event description, paste the three-step weekly review process from this chapter: scan outputs, identify failure patterns, update the context file. Set it to recur weekly with no end date.

**Your Submission:** Your submission is the updated context file — with its new "Operating Rules" section — plus the output from the fresh-session test that showed a refinement working without being restated. Copy both into one document. Write one sentence: what was the most important rule you added to the context file, and what specific improvement did it produce? Submit the updated context file + test output + one sentence.

### Track C — Agent-Orchestration Workspace

The orchestration workspace adds one thing the other tracks lack: a reviewable record. Every agent task leaves behind structured deliverables you can look back over — which makes the review half of the loop a first-class activity instead of an act of memory. The current tool name, the toggle that opens the manager view, and the exact name of the workspace-level rules file are on the companion page (cognitioneconomy.net/ch12-companion).

1. **Open the record.** Switch to the manager view — the surface that shows your recent agent tasks and the deliverables each one produced. This visible history is the raw material of reflection.
2. **Review the week's deliverables for failure patterns.** In a new conversation in the manager view, ask the agent to review the deliverables this workspace produced over the past week. If your tool cannot enumerate its own past outputs, paste in the deliverables from your last five agent tasks instead — the review works the same either way. Then ask: *"Identify recurring patterns where my instructions needed to be repeated or where output required substantial revision. Summarize as a short list of failure patterns."*
3. **Encode the lessons at workspace scope.** From that summary, identify two or three rules that would prevent the patterns from recurring. Open the workspace's standing rules file — the project-level instructions every agent in this workspace loads — and add the rules as plain-English instructions. (Create the file if it does not exist; your tool's name for it is on the companion site. Whatever it is called, use the same file for every rule you add from here on.)
4. **Re-run and verify.** Start a new agent task that repeats one of the jobs that produced a failure pattern. Review the deliverable. Confirm the new rules changed the output without you restating them. Save this improved deliverable — it is half of your submission.
5. **Make the review a permanent artifact.** Ask the agent to generate a "Friday review template" — a short checklist that walks through scanning the week's deliverables, identifying patterns, and updating the workspace rules file. Save it as a permanent artifact in the workspace.
6. **Put the review on the calendar.** Block a recurring 30-minute window every Friday at 4:00 PM titled "Workspace Review." Link the review template in the calendar event so you can open it with one click when the time arrives.

**Your Submission:** Your submission is the updated workspace rules file (after the feedback loop) plus the improved deliverable from the re-run task. Copy both into one document. Write two sentences: (1) what specific rule you added to the workspace rules file produced the biggest improvement, and (2) if you tracked the quality of this task over 12 weeks of the self-learning loop, what metric would you use to measure whether the system is actually getting better? Submit the updated rules file + improved deliverable + two sentences.

### Reflection

After completing your track, write two or three sentences. What surprised you about the patterns the AI surfaced in your recent work? Were they the patterns you would have identified yourself, or did the AI's review reveal something you had been blind to? Save this reflection — it is the first entry in your journal.

:::{admonition} Is this still true?
:class: note
A two-minute check before you rely on the loop: (1) In a fresh session, ask your assistant whether it remembers the feedback you gave it earlier — did the lesson persist *without* your memory note? Write down the answer; it tells you which memory layer you currently control. (2) Ask your tool where its standing rules live — a settings screen, a context file, a workspace rules file — and whether you can open that artifact directly. If you cannot open it as a file, you do not own it. Current filenames and menu locations live at cognitioneconomy.net/ch12-companion.
:::

---
*Applied Exercise for Chapter 12 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
