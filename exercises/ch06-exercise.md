# Applied Exercise — Chapter 6: Plan Mode — Think Before You Build
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Run a Real Task Through Plan Mode

This exercise takes one piece of work you actually need to do this week and runs it through the full Plan Mode sequence.

**Step 1: Choose the task.**
Pick something real. Something with actual stakes — a document someone will read, a decision someone will act on, a communication that shapes a relationship. Not a practice exercise. Real work.

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks run the same plan-then-execute sequence on the three surface types this book uses throughout: a **chat assistant** (Track A — the simplest starting point; the planning prompt transfers everywhere), a **terminal agent** inside a development environment (Track B — where you *watch* the approved plan execute, step by step, against real files), and an **agent-orchestration workspace** (Track C — where you run the same task twice, once without a plan and once with one, and compare the results side by side). Product names, commands, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch06-companion.
:::

### Track A — Chat Assistant

**Step 2: State the objective without specifying the approach.**
Open your assistant and describe what you need to achieve — not how you want it done. The goal, the audience, the context, the constraints. Then say:

> *"Before you do anything, think through this task out loud. Tell me your plan: what you will do, in what order, what assumptions you are making, what you would need to know to do this well, and what could go wrong. Do not begin the actual work until I have reviewed and approved your plan."*

**Step 3: Read the plan critically.**
When the AI returns a plan, read it as a skeptic. Ask yourself:
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

**Step 6: Run the control experiment (10 minutes, any surface).**
Now convert the chapter's thesis from claim to experienced fact. Open a fresh session and run the same task once *cold* — the full task description, submitted directly, with no plan step. Put the two outputs side by side: the planned one and the unplanned one. Add both to your submission with one sentence on the difference. This experiment needs nothing but a second chat window, and it is the most persuasive ten minutes in this chapter.

**Your Submission:** Your submission is the real task you ran through Plan Mode — five parts in one document: (1) the AI's original plan, (2) your pushback (what you challenged and why), (3) the revised plan, (4) the final output after execution, (5) the no-plan control output with one sentence on the difference. Write one sentence at the top: what did the planning phase surface that you would not have caught until the output was already wrong? Submit the one sentence + five-part document.

### Track B — Terminal Agent

On this surface you do not just approve the plan — you *watch it execute*, step by step, against real files, with every change visible. That visibility is the track's lesson: a plan is a contract, and the terminal agent shows you the contract being fulfilled clause by clause. Open your terminal agent in your workshop folder; the current commands and menu paths are on the companion page (cognitioneconomy.net/ch06-companion).

1. **Set up the review artifact.** Create a file called *plan-review.txt* in your workshop folder. You will use it to take notes as you read the agent's plan — a written critique forces sharper skepticism than a mental one.

2. **Choose the task and fix the objective.** Pick a real task you need to complete this week — something with actual stakes. Write down its objective, audience, and key constraints in plain English before you type anything to the agent. Deciding the outcome before the tool is involved is itself a planning discipline.

3. **Demand the plan before the work.** Describe the task objective to the agent without specifying the approach — what outcome you need, who it is for, what constraints apply. Then add this exact instruction: *"Before you start any work, give me your plan. Tell me what you will do in what order, what assumptions you are making, what information you still need, and what could go wrong. Do not begin executing until I explicitly approve the plan."* (Most terminal agents also ship a dedicated read-only planning state that enforces this — it can look but not touch; the current way to enter it is on the companion page.)

4. **Read the plan as a skeptic — in writing.** When the plan arrives, open your plan-review.txt and write down three things: (a) one assumption in the plan that is wrong or needs confirmation, (b) one step that is out of order or missing entirely, (c) one piece of context the agent does not have that would change the output significantly.

5. **Push back on all three.** Return to the agent with your corrections and the missing context. Ask it to revise the plan to address your feedback. A good plan improves under scrutiny; a weak one falls apart. You want to know which you have before anything executes.

6. **Approve and watch the contract execute.** If the revised plan is solid — if you cannot find a significant remaining flaw — say: *"The plan looks right. Proceed with execution."* Now watch. You will see files being created and modified as the agent works through each step of the approved plan, and the environment's change viewer shows you exactly what changed in any file. This is the read-only-then-write discipline made visible: nothing was touched until the plan was signed.

7. **Run the control experiment.** Start a second, fresh session and ask for the same output directly, with no plan step. Compare the two results. The difference is the chapter.

8. **File the artifacts.** Save the original plan, your plan-review.txt critique, the revised plan, and the final output as four files in your workshop folder.

**Your Submission:** Compile into one document: (1) the agent's original plan, (2) your plan-review.txt critique, (3) the revised plan after your pushback, (4) the final execution output, (5) the no-plan control output with one sentence on the difference. Write one sentence at the top: what specifically did the planning phase catch that a direct request would have gotten wrong? Submit the one sentence + five-part document.

### Track C — Agent-Orchestration Workspace

On this surface the run-twice comparison *is* the exercise: two agents, two workspaces, same task — one goes straight to work, one must produce a formal plan and wait at an approval gate. The current tool name, the toggle that opens the manager view, and every click-path are on the companion page (cognitioneconomy.net/ch06-companion).

1. **Open the orchestration view** — the manager surface where multiple agents run side by side — and choose the same real task you would use in the other tracks. Something with genuine professional stakes.

2. **Design the comparison.** You will run the task twice in two separate workspaces so you can compare the results directly. The comparison is the core of the exercise; do not skip the first run.

3. **Run 1 — no plan.** Create a workspace and start an agent task. Give the agent the full task description — objective, audience, constraints — and submit it immediately, with no instruction to plan first. Let it run to completion without interruption.

4. **Critique Run 1 in writing.** When the output arrives, review it carefully. In a note, write down two or three places where the agent made an assumption you did not want, or produced something slightly off from what you needed. These notes are your measuring stick for Run 2.

5. **Run 2 — plan first, with an approval gate.** Create a second workspace and start a new agent task. Begin the task description with this instruction: *"Before you begin any work on this task, produce a written plan first. The plan must include: your approach in bullet points, the steps you will take in order, the assumptions you are making, and any questions you have for me. After producing the plan, stop and wait for my written approval before proceeding to execution."*

6. **Read the plan as a skeptic and push back.** When the plan deliverable appears, challenge at least one assumption or request one specific change. The agent revises the plan. Only when it holds up do you type: *"Plan approved. Proceed to execution."*

7. **Compare the two deliverables.** Place the final outputs side by side — Run 1 (no plan) and Run 2 (plan approved). Compare them on three dimensions: specificity to your actual requirements, accuracy of assumptions, structural quality. Then check Run 2 against your Step 4 critique notes — did the planned run avoid the mistakes you identified in the unplanned one?

**Your Submission:** Submit a document containing: (1) the Run 1 output with your critique notes from Step 4 annotated, (2) the Run 2 plan (what the agent proposed), (3) your pushback message from Step 6, (4) the Run 2 final output. Write two sentences: (1) what the no-plan run got wrong that the plan-approved run got right, and (2) what category of professional tasks do you think benefits most from Plan Mode? Submit the four-part document + two sentences.

:::{admonition} Is this still true?
:class: note
One claim in this chapter is worth verifying against the market before you rely on it: the Architect-and-Builder Pattern assumes your vendor ships more than one model tier. Open your vendor's pricing page. If there are two or more models at different price points, the pattern applies — plan on the expensive one, execute on the cheap one. The tier names on that page will not match this book's parenthetical for long; the price gap between thinking and producing is the part that lasts. Current tier names and any dedicated planning-mode features are tracked on the companion page at cognitioneconomy.net/ch06-companion.
:::

### Reflection

*What did the planning phase surface that you would not have caught until the output was already wrong?*

Write it down. That specific thing — whatever it was — is the value of Plan Mode. And it will happen every time.

If you ran the exercise on more than one surface: *Which surface made you push back the hardest on the plan — the conversational thread, the terminal output, or the formal plan artifact in an orchestration workspace? The surface that produces the most friction in your reviewing eye is the surface that will catch the most mistakes.*

---
*Applied Exercise for Chapter 6 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
