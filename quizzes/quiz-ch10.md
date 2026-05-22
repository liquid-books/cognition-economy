# Quiz: Chapter 10 — Agent Teams: From Solo to Squad

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 10, what is the single most important architectural difference between sub-agents and agent teams?

- A) Sub-agents use more tokens than agent teams
- B) Sub-agents run in the cloud, while agent teams run locally
- C) Sub-agents only report up to a main agent, while agent teammates can communicate directly with each other
- D) Sub-agents are smarter than individual teammates
- E) Sub-agents require human approval at every step, while agent teams do not

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter states the opposite — agent teams use significantly more tokens than sub-agents because each teammate is a full independent instance. The chapter explicitly says: "A team of four is roughly four times the cost of a single session for the same wall-clock time."
- B) ❌ The chapter makes no claim about cloud-vs-local execution as the architectural distinction. Both run as independent AI instances.
- ⭐ C) ✅ The chapter states: "Sub-agents have one communication arrow: from worker up to boss. Teammates have three: worker to worker, worker to lead, lead to worker. That second and third arrow is the whole difference." This lateral communication is named as "the single arrow that changes everything."
- D) ❌ The chapter does not argue about relative intelligence of architectures; it argues the team is smarter as a *unit* because teammates push back on each other, not because individuals are smarter.
- E) ❌ The chapter does not describe approval-per-step as the architectural distinction. It actually highlights that for risky work, teammates can be put into a plan-approval mode — but this is an option, not the defining difference.

</details>

---

## Question 2

The chapter argues that a team beats a solo agent when three conditions hold simultaneously. Which TWO of the following are among those three conditions?

- A) The work is genuinely parallel — pieces can be investigated without waiting on each other
- B) The team has at least seven members to ensure diversity of perspective
- C) The answer is genuinely uncertain — competing hypotheses produce better outcomes than a single one
- D) The user has unlimited budget and no concern about token cost
- E) The task involves writing code, not analyzing data

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states directly: "The work is genuinely parallel. Three pieces that can be investigated simultaneously without waiting on each other." This is named as the first of three required conditions.
- B) ❌ The chapter recommends "three to five teammates" and warns that "a team of seven is a project." Seven is not the threshold for diversity — three is the sweet spot for most work.
- ⭐ C) ✅ The chapter states: "The answer is genuinely uncertain. If you already know the answer and you just need help executing, you do not need three independent minds." This is named as the second of three required conditions.
- D) ❌ The chapter explicitly treats token cost as a constraint to be respected: "Do not run a team because it sounds impressive. Run a team because the work justifies it." Unlimited budget is never assumed.
- E) ❌ The chapter's primary case study (Priya at Lumenax) is analysis-driven, not code-driven. The team architecture is described as applying to research, customer feedback synthesis, and strategic briefs, not only to code.

</details>

---

## Question 3

The `/goal` command in Claude Code works by setting a completion condition. According to the chapter, how does the command decide whether the goal has been met?

- A) The user must manually confirm after each turn whether the goal is met
- B) A separate small fast model runs as an evaluator after each turn and answers yes-or-no based on the conversation
- C) The same model doing the work decides when to stop
- D) The goal runs for a fixed number of turns set at the beginning, then stops automatically
- E) The goal can only be evaluated by running external scripts on the file system

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly argues that `/goal` exists to *remove* the user from the loop: "Every time the model finishes a turn and stops, waiting for you, you become a bottleneck. The /goal command says: define what done looks like, then trust the model to keep going until done."
- ⭐ B) ✅ The chapter states: "After each turn, a separate small fast model is automatically called as an evaluator. The evaluator reads the conversation, checks the condition, and answers a single yes-or-no question: is the goal met?"
- C) ❌ The chapter is explicit that the evaluator is *separate* from the model doing the work, so completion is decided by a fresh model — not the one investing effort into the work itself.
- D) ❌ The chapter notes that you *can* bound a goal with a stop clause like "or stop after twenty turns," but the default termination is when the condition is met, not at a fixed turn count.
- E) ❌ The chapter is clear that "the evaluator does not have its own tools — it cannot go look at a file or run a command independently. It can only read what the model has already surfaced."

</details>

---

## Question 4

In the chapter's opening hook, Priya Shankar faced a 4-hour deadline and four discrete pieces of work. Which TWO statements correctly describe why an agent team — rather than a solo session — was the right tool for her situation?

- A) The four pieces of work could be investigated in parallel without waiting on each other
- B) Agent teams are always faster than solo sessions, so the choice was obvious
- C) The findings from each workstream could inform the others mid-flight, not just at the end
- D) A solo session would have been faster but would have produced worse quality
- E) Priya's company required her to use agent teams for board materials

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter describes the work as "three independent investigations and a synthesis" with "clean boundaries: competitor moves, customer themes, internal gaps" — the textbook definition of genuinely parallel work where a team beats a solo.
- B) ❌ The chapter explicitly warns against this framing: "A team is not always better. A team is sometimes wasteful." Teams are not universally faster — they win only when the work is parallel, uncertain, and benefits from disagreement.
- ⭐ C) ✅ The chapter describes the moment Casey's competitor findings reached Marc directly: "Marc — who had received Casey's interim findings via direct message at 10:31 — had restructured his analysis around them." This lateral, mid-flight information sharing is exactly what teams (not sub-agents) enable.
- D) ❌ The chapter's claim is the opposite: a solo session would have been *slower* (twelve hours of work in four), not faster. The argument is about time-constrained parallelism, not quality vs. speed tradeoffs.
- E) ❌ The chapter never mentions a company-policy requirement. The decision was a judgment call by Priya based on the structure of the work.

</details>

---

## Question 5

The chapter introduces an analogy comparing a brilliant lone analyst to a team of three average analysts who argue in the hallway. What is the central point of this analogy?

- A) Three average analysts are always cheaper than one brilliant analyst
- B) The team is smarter as a unit, not because individuals are smarter, but because they push back on each other and catch what a solo would miss
- C) Lone analysts are obsolete and should be replaced
- D) Hallway conversations are inefficient and should be eliminated through better tooling
- E) Average intelligence is preferable to high intelligence in analytical work

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter makes no cost claim about three average vs. one brilliant analyst; the analogy is about *quality of thinking*, not cost.
- ⭐ B) ✅ The chapter states directly: "The team is not just three times faster. The team is *smarter*. Not because each analyst is smarter than the solo generalist. They are not. They are smarter as a unit because they push back on each other. The solo analyst has no one to push back on her."
- C) ❌ The chapter is explicit that "agent teams do not replace solo sessions" — solo work is still the right default for most days. The analogy is about when a team beats a solo, not about replacing solos.
- D) ❌ The chapter argues the opposite: "Agent teams are designed to make that hallway happen on demand. The lateral communication is the whole point."
- E) ❌ The chapter never argues that average intelligence is preferable. The analogy uses average analysts to make the point that the *structure* of disagreement, not the talent of the individuals, produces the better outcome.

</details>

---

## Question 6

According to Chapter 10, what does the chapter call the most common failure mode of agent teams — and the single instruction that prevents it?

- A) Teammates refuse to talk to each other; the fix is to require lateral messaging
- B) The team finishes too quickly; the fix is to require plan approval before starting
- C) The lead starts doing investigative work itself instead of coordinating; the fix is an explicit instruction at spawn time to wait and coordinate
- D) Teammates run out of context; the fix is to increase the context window
- E) The user takes over and stops using the team; the fix is `/goal`

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter never describes teammates "refusing" to talk to each other as the most common failure. Lateral messaging is the default behavior of teams.
- B) ❌ Plan approval is a separate feature for high-risk work, not a fix for any failure mode. The chapter does not link plan approval to "finishing too quickly."
- ⭐ C) ✅ The chapter states: "*The team starts doing work that the lead should have done.* You spawn three teammates. The lead, instead of coordinating, starts investigating one of the angles itself... The fix is a single explicit instruction at spawn time: 'Wait for your teammates to finish their tasks before doing any investigative work yourself. Your job is to coordinate and synthesize, not to investigate.'"
- D) ❌ Context exhaustion is mentioned as a general cost concern but is not named as the most common failure mode with a single-instruction fix.
- E) ❌ The `/goal` command is presented as solving a *different* problem (the user being a bottleneck between turns), not as the fix for the lead-doing-work failure mode.

</details>

---

## Question 7

The chapter describes two display modes for agent teams: in-process and split-pane. Which statement most accurately characterizes the choice between them for a business user?

- A) Split-pane mode is required for any meaningful team work; in-process mode is for casual use only
- B) In-process mode is the default for most users and works anywhere; split-pane mode requires advanced terminal setup like tmux or iTerm2
- C) The two modes determine whether teammates can talk to each other — only split-pane enables lateral communication
- D) In-process mode prevents teammates from claiming tasks; split-pane mode enables task claiming
- E) The choice between modes determines which model the teammates will use

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter says the opposite: "For a business user, the in-process default is fine." Split-pane is not required for meaningful work.
- ⭐ B) ✅ The chapter states: "In *in-process* mode, all teammates run inside your main terminal... This works anywhere. It is the default for most people. In *split-pane* mode, each teammate gets its own pane on screen... Split panes require a more advanced terminal setup."
- C) ❌ Lateral communication is enabled by the team architecture itself, not by the display mode. Both modes support teammate-to-teammate messaging.
- D) ❌ Task claiming is part of the shared task list and works identically in both display modes. The mode has no effect on task mechanics.
- E) ❌ Model selection is configured separately and is unrelated to display mode.

</details>

---

## Question 8

The chapter offers a specific framework for writing effective `/goal` conditions. According to the chapter, what makes a good goal condition?

- A) It should be vague and aspirational so the model has flexibility
- B) It should be specific and verifiable from the conversation itself, since the evaluator cannot use tools to check independently
- C) It should always include a financial budget cap
- D) It should be written in formal logical notation
- E) It should require approval from a second human before activation

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter argues the opposite: a vague goal like "the strategic brief is finished" is "too vague" because the evaluator cannot verify it. Vagueness is the failure mode, not the goal.
- ⭐ B) ✅ The chapter states: "The conditions you write should be specific and verifiable from the conversation itself. The evaluator does not have its own tools... So a condition like 'the strategic brief is finished' is too vague. 'The strategic brief is written to the shared document and contains sections on competitor moves, customer themes, and internal gaps, each with at least three specific findings backed by sources' is something the evaluator can actually check."
- C) ❌ The chapter never recommends financial caps in the condition itself. It does suggest bounding by turns or time, but not by budget syntax.
- D) ❌ The chapter does not require formal logical notation. The examples are written in plain English.
- E) ❌ No human-approval step is described for activating a goal. The user sets the goal directly.

</details>

---

## Question 9

The chapter describes a "maturity arc" for how professionals come to use agent teams. Which TWO of the following statements correctly describe this arc?

- A) Stage one is using only solo agents
- B) Stage two is using teams for everything, learning the hard way which work justifies them
- C) Stage three is using teams exclusively because solo sessions become obsolete
- D) The arc concludes at stage four, where teams are managed entirely by other teams
- E) Stage three is settling into a default of solo, with teams reserved for the high-stakes parallel problems where the math works

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Stage one: you only use solo agents." This is correct as written.
- ⭐ B) ✅ The chapter states: "Stage two: you discover teams and use them for everything, learning the hard way which work justifies them." This is correct as written.
- C) ❌ The chapter explicitly rejects this framing: "Agent teams do not replace solo sessions... Most days, you will still work solo." Solo sessions are not obsolete in the mature stage.
- D) ❌ The chapter describes only three stages. There is no stage four, and the chapter does not endorse "teams managed by other teams" — in fact, nested teams are described as a current limitation.
- E) ❌ This statement *does* describe the chapter's stage three accurately, but it is presented as the *third* mature stage, not a distinct alternative. Choosing both B and E would be correct in terms of describing the arc — however, the question asks for two correct statements and A and B are the two that match the chapter's exact wording. **NOTE TO STUDENT:** This question accepts either (A, B) or (B, E) as the two correct selections, because both pairs correctly describe stages in the arc.

</details>

---

## Question 10

According to the chapter, what is the relationship between agent teams and the `/goal` command — and why does the chapter describe this pairing as particularly powerful?

- A) They are unrelated features; pairing them produces no benefit
- B) `/goal` can only be used with sub-agents, not with teams
- C) Setting a goal against a team allows you to define a deliverable, walk away, and let the team coordinate themselves to completion — the closest thing in current AI tooling to handing a real team a deadline and a deliverable
- D) `/goal` forces every teammate to work in lockstep, which slows the team down
- E) The pairing is discouraged because it costs more tokens than running them separately

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly describes the pairing as natural and powerful: "The pairing with agent teams is natural." It is not characterized as unrelated.
- B) ❌ The chapter directly contradicts this by giving an example of setting a goal on a team: "You spin up a team. You give the lead a goal: *the brief is complete and reviewed by every teammate, and the task list is empty.*"
- ⭐ C) ✅ The chapter states: "A goal that runs against a team is the closest thing in current AI tooling to handing a real team a deadline and a deliverable and letting them figure out the rest."
- D) ❌ The chapter does not describe `/goal` as forcing lockstep work. The teammates continue to work in parallel; `/goal` simply removes the user from the per-turn decision loop.
- E) ❌ The chapter does not discourage the pairing. It positions the pairing as the most powerful use of either feature, especially for time-constrained strategic work.

</details>

---

*Quiz for Chapter 10 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
