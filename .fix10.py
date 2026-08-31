import io
p='quizzes/quiz-ch10.md'
s=open(p).read()

old_q3 = """The `/goal` command in Claude Code works by setting a completion condition. According to the chapter, how does the command decide whether the goal has been met?

- A) The user must manually confirm after each turn whether the goal is met
- B) A separate small fast model runs as an evaluator after each turn and answers yes-or-no based on the conversation
- C) The same model doing the work decides when to stop
- D) The goal runs for a fixed number of turns set at the beginning, then stops automatically
- E) The goal can only be evaluated by running external scripts on the file system

<details>
<summary>Show Answer & Explanations</summary>

- A) \u274c The chapter explicitly argues that `/goal` exists to *remove* the user from the loop: "Every time the model finishes a turn and stops, waiting for you, you become a bottleneck. The /goal command says: define what done looks like, then trust the model to keep going until done."
- \u2b50 B) \u2705 The chapter states: "After each turn, a separate small fast model is automatically called as an evaluator. The evaluator reads the conversation, checks the condition, and answers a single yes-or-no question: is the goal met?"
- C) \u274c The chapter is explicit that the evaluator is *separate* from the model doing the work, so completion is decided by a fresh model \u2014 not the one investing effort into the work itself.
- D) \u274c The chapter notes that you *can* bound a goal with a stop clause like "or stop after twenty turns," but the default termination is when the condition is met, not at a fixed turn count.
- E) \u274c The chapter is clear that "the evaluator does not have its own tools \u2014 it cannot go look at a file or run a command independently. It can only read what the model has already surfaced." """

new_q3 = """A goal condition (in some tools, a `/goal` slash command) sets a finish line for the work. According to the chapter, how is it decided whether the goal has been met?

- A) The user must manually confirm after each turn whether the goal is met
- B) A separate lightweight check runs after each turn and answers a single yes-or-no question \u2014 is the condition met? \u2014 based on what is in the conversation
- C) The same model doing the work decides when to stop
- D) The goal runs for a fixed number of turns set at the beginning, then stops automatically
- E) The goal can only be evaluated by running external scripts on the file system

<details>
<summary>Show Answer & Explanations</summary>

- A) \u274c The chapter explicitly argues that a goal condition exists to *remove* the user from the loop: "Every time the model finishes a turn and stops, waiting for you, you become a bottleneck. A goal condition says: define what done looks like, then trust the model to keep going until done."
- \u2b50 B) \u2705 The chapter states: "You give the model a completion condition \u2014 a sentence describing what 'done' looks like. The model starts working. After each turn, a separate lightweight check runs and answers one question: is the condition met?"
- C) \u274c The chapter is explicit that the check is *separate* from the model doing the work, so completion is decided by a fresh evaluation \u2014 not by the model investing effort into the work itself.
- D) \u274c The chapter notes that you *can* bound a goal with a stop clause like "or stop after twenty turns," but the default termination is when the condition is met, not at a fixed turn count.
- E) \u274c The chapter is clear that the check "typically sees only what is in the conversation \u2014 it cannot go look at a file or run a command on its own" \u2014 which is exactly why conditions must be provable from the conversation itself."""

if old_q3.strip() in s:
    s = s.replace(old_q3.strip(), new_q3.strip())
else:
    # fallback: replace pieces individually
    s = s.replace("The `/goal` command in Claude Code works by setting a completion condition. According to the chapter, how does the command decide whether the goal has been met?",
                  "A goal condition (in some tools, a `/goal` slash command) sets a finish line for the work. According to the chapter, how is it decided whether the goal has been met?")
    s = s.replace("- B) A separate small fast model runs as an evaluator after each turn and answers yes-or-no based on the conversation",
                  "- B) A separate lightweight check runs after each turn and answers a single yes-or-no question \u2014 is the condition met? \u2014 based on what is in the conversation")
    s = s.replace('- A) \u274c The chapter explicitly argues that `/goal` exists to *remove* the user from the loop: "Every time the model finishes a turn and stops, waiting for you, you become a bottleneck. The /goal command says: define what done looks like, then trust the model to keep going until done."',
                  '- A) \u274c The chapter explicitly argues that a goal condition exists to *remove* the user from the loop: "Every time the model finishes a turn and stops, waiting for you, you become a bottleneck. A goal condition says: define what done looks like, then trust the model to keep going until done."')
    s = s.replace('- \u2b50 B) \u2705 The chapter states: "After each turn, a separate small fast model is automatically called as an evaluator. The evaluator reads the conversation, checks the condition, and answers a single yes-or-no question: is the goal met?"',
                  '- \u2b50 B) \u2705 The chapter states: "You give the model a completion condition \u2014 a sentence describing what \'done\' looks like. The model starts working. After each turn, a separate lightweight check runs and answers one question: is the condition met?"')
    s = s.replace("- C) \u274c The chapter is explicit that the evaluator is *separate* from the model doing the work, so completion is decided by a fresh model \u2014 not the one investing effort into the work itself.",
                  "- C) \u274c The chapter is explicit that the check is *separate* from the model doing the work, so completion is decided by a fresh evaluation \u2014 not by the model investing effort into the work itself.")
    s = s.replace('- E) \u274c The chapter is clear that "the evaluator does not have its own tools \u2014 it cannot go look at a file or run a command independently. It can only read what the model has already surfaced."',
                  '- E) \u274c The chapter is clear that the check "typically sees only what is in the conversation \u2014 it cannot go look at a file or run a command on its own" \u2014 which is exactly why conditions must be provable from the conversation itself.')

s=s.replace("- E) The user takes over and stops using the team; the fix is `/goal`","- E) The user takes over and stops using the team; the fix is a goal condition")
s=s.replace("- E) \u274c The `/goal` command is presented as solving a *different* problem (the user being a bottleneck between turns), not as the fix for the lead-doing-work failure mode.",
"- E) \u274c The goal condition is presented as solving a *different* problem (the user being a bottleneck between turns), not as the fix for the lead-doing-work failure mode.")

old_q7 = """The chapter describes two display modes for agent teams: in-process and split-pane. Which statement most accurately characterizes the choice between them for a business user?

- A) Split-pane mode is required for any meaningful team work; in-process mode is for casual use only
- B) In-process mode is the default for most users and works anywhere; split-pane mode requires advanced terminal setup like tmux or iTerm2
- C) The two modes determine whether teammates can talk to each other \u2014 only split-pane enables lateral communication
- D) In-process mode prevents teammates from claiming tasks; split-pane mode enables task claiming
- E) The choice between modes determines which model the teammates will use

<details>
<summary>Show Answer & Explanations</summary>

- A) \u274c The chapter says the opposite: "For a business user, the in-process default is fine." Split-pane is not required for meaningful work.
- \u2b50 B) \u2705 The chapter states: "In *in-process* mode, all teammates run inside your main terminal... This works anywhere. It is the default for most people. In *split-pane* mode, each teammate gets its own pane on screen... Split panes require a more advanced terminal setup."
- C) \u274c Lateral communication is enabled by the team architecture itself, not by the display mode. Both modes support teammate-to-teammate messaging.
- D) \u274c Task claiming is part of the shared task list and works identically in both display modes. The mode has no effect on task mechanics.
- E) \u274c Model selection is configured separately and is unrelated to display mode."""

new_q7 = """The chapter notes that your tool may let you either cycle through teammates one at a time in a single window or watch each teammate in its own pane. According to the chapter, how much does this choice matter?

- A) The choice is essential \u2014 one of the two views is required for any meaningful team work
- B) The choice is cosmetic \u2014 the team runs the same either way; how the work is displayed has no effect on how it executes
- C) The view determines whether teammates can talk to each other \u2014 only the multi-pane view enables lateral communication
- D) The single-window view prevents teammates from claiming tasks; the multi-pane view enables task claiming
- E) The choice of view determines which model the teammates will use

<details>
<summary>Show Answer & Explanations</summary>

- A) \u274c The chapter says the opposite \u2014 neither view is required; the difference is presentation only.
- \u2b50 B) \u2705 The chapter states: "Depending on your tool and your setup, you can either cycle through teammates one at a time in a single window or watch each teammate in its own pane \u2014 the choice is cosmetic, and the team runs the same either way."
- C) \u274c Lateral communication is enabled by the team architecture itself, not by the display. Both views support teammate-to-teammate messaging.
- D) \u274c Task claiming is part of the shared task list and works identically in both views. The display has no effect on task mechanics.
- E) \u274c Model selection is configured separately and is unrelated to how the team is displayed."""

s=s.replace(old_q7, new_q7)

s=s.replace("The chapter offers a specific framework for writing effective `/goal` conditions. According to the chapter, what makes a good goal condition?",
"The chapter offers a specific framework for writing effective goal conditions. According to the chapter, what makes a good goal condition?")
s=s.replace("- B) It should be specific and verifiable from the conversation itself, since the evaluator cannot use tools to check independently",
"- B) It should be specific and verifiable from the conversation itself, since the lightweight check cannot use tools to verify independently")
s=s.replace('- \u2b50 B) \u2705 The chapter states: "The conditions you write should be specific and verifiable from the conversation itself. The evaluator does not have its own tools... So a condition like \'the strategic brief is finished\' is too vague. \'The strategic brief is written to the shared document and contains sections on competitor moves, customer themes, and internal gaps, each with at least three specific findings backed by sources\' is something the evaluator can actually check."',
'- \u2b50 B) \u2705 The chapter states: "The conditions you write should be specific and verifiable. Because that lightweight check typically sees only what is in the conversation \u2014 it cannot go look at a file or run a command on its own \u2014 write conditions the conversation itself can prove. A condition like \'the strategic brief is finished\' is too vague. \'The strategic brief is written to the shared document and contains sections on competitor moves, customer themes, and internal gaps, each with at least three specific findings backed by sources\' is something the check can actually verify."')

s=s.replace("According to the chapter, what is the relationship between agent teams and the `/goal` command \u2014 and why does the chapter describe this pairing as particularly powerful?",
"According to the chapter, what is the relationship between agent teams and the goal condition \u2014 and why does the chapter describe this pairing as particularly powerful?")
s=s.replace("- B) `/goal` can only be used with sub-agents, not with teams","- B) A goal condition can only be used with sub-agents, not with teams")
s=s.replace("- D) `/goal` forces every teammate to work in lockstep, which slows the team down","- D) A goal condition forces every teammate to work in lockstep, which slows the team down")
s=s.replace('- B) \u274c The chapter directly contradicts this by giving an example of setting a goal on a team: "You spin up a team. You give the lead a goal: *the brief is complete and reviewed by every teammate, and the task list is empty.*"',
'- B) \u274c The chapter directly contradicts this by giving an example of setting a goal condition on a team: "You spin up a team. You give the lead a goal condition: *the brief is complete and reviewed by every teammate, and the task list is empty.*"')
s=s.replace('- \u2b50 C) \u2705 The chapter states: "A goal that runs against a team is the closest thing in current AI tooling to handing a real team a deadline and a deliverable and letting them figure out the rest."',
'- \u2b50 C) \u2705 The chapter states: "A goal condition that runs against a team is the closest thing in current AI tooling to handing a real team a deadline and a deliverable and letting them figure out the rest."')
s=s.replace("- D) \u274c The chapter does not describe `/goal` as forcing lockstep work. The teammates continue to work in parallel; `/goal` simply removes the user from the per-turn decision loop.",
"- D) \u274c The chapter does not describe the goal condition as forcing lockstep work. The teammates continue to work in parallel; the goal condition simply removes the user from the per-turn decision loop.")

open(p,'w').write(s)
print("ok")
