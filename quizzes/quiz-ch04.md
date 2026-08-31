# Quiz: Chapter 4 — Skills: Teaching Your AI New Tricks

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 4, what is the *fundamental* distinction between a prompt and a skill?

- A) A prompt is written in English; a skill is written in code
- B) A prompt is a set of instructions you give an AI for a specific task in a specific conversation — it ends when the conversation ends; a skill is a packaged, named, reusable capability with a consistent trigger that lives permanently in your AI setup
- C) A prompt only works in one vendor's tool; a skill only works in another's
- D) A prompt is paid; a skill is free
- E) A prompt is for individuals; a skill is for enterprise customers

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Both are written in natural language in the chapter — code is never the differentiator.
- ⭐ B) ✅ The chapter states: "A **prompt** is a set of instructions you give an AI for a specific task, in a specific conversation. It gets the job done in the moment. When the conversation ends, the prompt ends with it... A **skill** is a packaged, named, reusable capability. It has a consistent trigger... It lives in your AI setup permanently."
- C) ❌ Skills work across vendors — the chapter is explicit that the concept is the same inside every container (a Project, a Gem, a custom GPT, an agent).
- D) ❌ Cost is never the distinction.
- E) ❌ The chapter targets individual professionals, not enterprise tiers.

</details>

---

## Question 2

The chapter uses a vivid analogy to explain skills. Which one is correct?

- A) A chef who improvises every meal vs. a chef who writes down recipes, standardizes them, and executes them the same way every night — your AI is the kitchen, skills are the recipes
- B) A doctor diagnosing patients without lab tests
- C) A surgeon performing without anesthesia
- D) An accountant balancing books with an abacus
- E) A teacher grading papers without a rubric

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Imagine you are a chef. Every time a customer orders pasta carbonara, you could stand at the stove and think through the recipe from scratch... But a great chef writes the recipe down, standardizes it, trains their team on it, and executes it the same way every night... Your AI is the kitchen. Skills are your recipes. And right now, most people are improvising every single meal."
- B) ❌ Lab tests are not the chapter's analogy.
- C) ❌ Surgery without anesthesia is not the chapter's analogy.
- D) ❌ Accounting/abacus is not the chapter's analogy.
- E) ❌ Teaching/rubrics is not the chapter's analogy.

</details>

---

## Question 3

The chapter argues that a well-built skill has four components. Which TWO of the following are correctly described in the chapter?

- A) A name and trigger — a clear, descriptive identifier so you know exactly what the skill does six months from now (e.g., "Competitor Brief," not "Thing 3")
- B) Output format — a defined output structure (headers or no headers, bullets or prose, short or detailed) stated explicitly because an AI without format instructions will improvise, and improvised format is inconsistent format
- C) An admin password that only the IT department can use to invoke it
- D) A monthly recurring fee per use
- E) A physical hardware dongle plugged into your laptop

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "A name and trigger. This is how you call the skill into action... The name should describe the action clearly enough that you know exactly what it does six months from now without having to open it. *'Competitor Brief'* is a name. *'Thing 3'* is not."
- ⭐ B) ✅ The chapter states: "Every skill should have a defined output structure. Headers or no headers. Bullet points or prose. Short or detailed. The format should be specified explicitly — because an AI without format instructions will improvise, and improvised format is inconsistent format." The four components are name/trigger, instructions, context, and output format.
- C) ❌ Admin passwords are not one of the four components.
- D) ❌ The chapter never says skills have a per-use fee.
- E) ❌ No hardware dongle is described or required.

</details>

---

## Question 4

The chapter describes a "Pre-Call Intelligence" skill as one concrete example. Which statement best matches the chapter's description of what that skill does?

- A) It books the meeting on your behalf and sends calendar invites to the prospect
- B) You type the prospect's name and company into the skill, and in ten seconds you get a one-page brief on who they are, what their company does, their recent news, their competitors, what they are likely worried about this quarter, and three opening questions calibrated to their situation
- C) It records the actual call and creates a transcript
- D) It rates the prospect's social media activity
- E) It locks you out of the meeting until you complete a 200-question intake form

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Scheduling is not what the chapter describes for this skill.
- ⭐ B) ✅ The chapter states: "You type their name and company into your *Pre-Call Intelligence* skill. In ten seconds you have: a one-page brief on who they are, what their company does, their recent news, their competitors, what they are likely worried about this quarter, and three opening questions calibrated to their situation."
- C) ❌ Call recording is not the function of the Pre-Call Intelligence skill in this chapter.
- D) ❌ Social media rating is not mentioned for this skill.
- E) ❌ A 200-question intake form is the opposite of what skills do — skills minimize input friction.

</details>

---

## Question 5

According to the chapter, what is the recommended four-step process for building a skill?

- A) Buy expensive software, hire a consultant, deploy in production, audit annually
- B) Identify a repeating task → describe the ideal output (find your best-ever example) → have your AI write the skill instructions (meta-prompting from your example) → test and refine on three real examples
- C) Memorize the entire user manual, configure firewall settings, write unit tests, then deploy
- D) Wait for IT to provision an enterprise instance, then file a ticket
- E) Apply for an API key, submit a budget request, host a kickoff meeting, attend training

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This bureaucratic path is the opposite of the chapter's lightweight approach.
- ⭐ B) ✅ The chapter states the four steps: "Step 1: Identify a repeating task... Step 2: Describe the ideal output... find the best example of this task you have ever produced... Step 3: Have your AI write the skill instructions... Step 4: Test and refine. Run the skill on three real examples from your work."
- C) ❌ This technical path is not what the chapter describes.
- D) ❌ IT provisioning is not part of the chapter's process — the chapter is explicitly for non-developer business users.
- E) ❌ Budget requests and kickoff meetings are not part of the four-step process.

</details>

---

## Question 6

The chapter explains how to "turn any API into a skill." Which TWO statements correctly describe the chapter's approach?

- A) You find a tool's developer documentation, understand the *capability* (what it does, what it takes in, what it gives back) — you do not need to read the technical parts to use it
- B) You paste the documentation into your assistant and ask it to write the skill instructions, including what the AI needs to send to the API and how to present the results
- C) You must complete a four-year computer science degree before using any API
- D) You must rewrite the API in Python yourself before your AI can use it
- E) APIs only work with paid enterprise AI tiers

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "You go to a tool's website and look for their documentation... You do not need to read the technical parts. You just need to understand the *capability*: what can this thing do, what do you give it, and what does it give back?"
- ⭐ B) ✅ The chapter states: "Then you open your assistant and say: 'Here is the documentation for [tool name]. I want to build a skill that uses this API to [describe what you want it to do]. Write me the instructions for this skill, including what the AI needs to send to the API and how to present the results.'" The AI reads the documentation. The AI writes the skill.
- C) ❌ The chapter explicitly says no engineering prerequisites are needed.
- D) ❌ Rewriting the API yourself is not part of the chapter's process.
- E) ❌ The chapter is explicit that this works on standard tiers — and many APIs are free or extremely cheap.

</details>

---

## Question 7

The chapter argues that skills *compound*. According to the chapter's math, what does a year of deliberate skill-building look like in terms of investment and outcome?

- A) Twenty skills over a year (one new skill every ~2.5 weeks) — not aggressive — produces a system that does your routine work automatically at a quality level you defined yourself, freeing your time for the problems only you can solve; this is a structural advantage competitors cannot easily see, copy, or catch up to
- B) Twenty skills over a year requires hiring four new employees
- C) Skills depreciate — after a year you must rebuild them all from scratch
- D) After a year, skills cease to work because models change too quickly
- E) Building skills produces no measurable time savings — the benefit is purely psychological

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Build a library of twenty skills over the next year — which is not aggressive, it is one new skill every two and a half weeks — and you have created something that has no good analog in the history of professional tools. You have a system that does your routine work automatically, at a level of quality you defined yourself, releasing your time and attention for the problems only you can solve. This is not productivity hacking... This is a structural advantage. The kind that takes years to build — and that competitors cannot see, cannot copy, and cannot catch up to without putting in the same work."
- B) ❌ The chapter never says you must hire staff to build skills.
- C) ❌ Skills compound rather than depreciate per the chapter.
- D) ❌ The chapter argues the opposite — skills get *better* over time as you refine them.
- E) ❌ The chapter is very specific about measurable time savings.

</details>

---

## Question 8

In the Meridian Capital Partners case study, Rachel Osei discovers that two equally talented associates — Marcus and Priya — are producing dramatically different results from AI tools despite similar effort. Which TWO statements correctly describe the *reason* the chapter identifies for the gap?

- A) Marcus spent three weekends building a "recipe book" — a library of fifteen named AI skills covering every repeating task, each with clear names, specific standing instructions, defined context about Meridian's evaluation criteria, and locked output formats
- B) Priya was rewriting her prompts from scratch every session — good prompts, thoughtful prompts, but one-time prompts that vanished the moment she closed the chat window
- C) Marcus was using a more expensive subscription tier than Priya
- D) Priya was working fewer hours than Marcus
- E) Marcus had a side deal with an AI vendor that gave him a private model

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "Marcus had spent three weekends building what he called his 'recipe book' — a library of fifteen named AI skills covering every repeating task in his workflow... Each skill had a clear name, specific standing instructions, defined context about Meridian's evaluation criteria, and a locked output format."
- ⭐ B) ✅ The case states: "Priya, by contrast, was rewriting her prompts from scratch every session — good prompts, thoughtful prompts, but one-time prompts that vanished the moment she closed the chat window. She was improvising every meal in a kitchen that had no recipes."
- C) ❌ The case never mentions a tier difference; it explicitly says both used the same tools.
- D) ❌ The case says they were "spending roughly the same amount of time doing it" and both "working hard."
- E) ❌ No private vendor deal is mentioned in the case.

</details>

---

## Question 9

In the Meridian Capital Partners case study, the operating committee weighed an upfront investment to build a centralized skill library. What was that investment, and what *competitive intelligence signal* arrived at the same time?

- A) Forty hours of senior associate time spread over six weeks; a peer firm in Atlanta of similar size and deal focus was rumored to have cut average due diligence timeline by 30% over the previous twelve months — without hiring additional staff
- B) Two million dollars in AI software licensing; a peer firm announced it was shutting down
- C) Zero hours of investment was required; no competitive signal was observed
- D) Fifteen years of training; the peer firm had been acquired by Goldman Sachs
- E) Hiring a new managing director; the peer firm filed for bankruptcy

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "The estimated investment was forty hours of senior associate time spread over six weeks — a non-trivial cost during an active deal period." And: "A peer firm in Atlanta — similar size, similar deal focus — was rumored to have cut its average due diligence timeline by thirty percent over the previous twelve months. Sources suggested the firm had not hired additional staff."
- B) ❌ Neither figure nor event in this option appears in the case.
- C) ❌ The case is explicit that the investment was non-trivial and a peer signal was observed.
- D) ❌ Goldman Sachs and 15-year training timelines are not in the case.
- E) ❌ No bankruptcy is mentioned.

</details>

---

## Question 10

The chapter ends with a vivid characterization of what a professional with a year of deliberate skill-building has, compared to peers. Which statement best matches the chapter's framing?

- A) They are working harder than everyone else
- B) They are working in a *fundamentally different way* — they have converted their professional expertise (the stuff that lives in their head) into a system that executes that expertise consistently, at scale, without them having to be present for every instance of it; that is not productivity — that is *leverage*
- C) They are working less effectively but feel more productive
- D) They have outsourced their judgment to a vendor and lost their professional edge
- E) They have automated themselves out of a job

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly says the opposite: "They are *not* working harder than everyone else."
- ⭐ B) ✅ The chapter states: "The professional who has spent a year building and refining their skill library is not working harder than everyone else. They are working in a fundamentally different way." And: "They have converted their professional expertise — the stuff that lives in their head — into a system that executes that expertise consistently, at scale, without them having to be present for every instance of it. That is not productivity. That is leverage."
- C) ❌ The chapter argues these professionals work *more* effectively, not less.
- D) ❌ The chapter is explicit that judgment stays with the human; skills handle the processing.
- E) ❌ The chapter frames skills as freeing time for higher-value judgment work, not eliminating the job.

</details>

---

*Quiz for Chapter 4 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
