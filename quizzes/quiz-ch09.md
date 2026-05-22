# Quiz: Chapter 9 — Custom Sub-Agents: The Specialist Mindset

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 9, what is the structural reason a brilliant generalist AI conversation does not scale as your work grows?

- A) The AI model becomes less intelligent over time as the conversation lengthens
- B) Every big task pollutes the same context window, dividing the model's attention and thinning the thinking
- C) Large language models are technically incapable of doing more than one task per session
- D) Cloud providers throttle requests once a conversation crosses a token threshold
- E) The cost per query rises so steeply that long conversations become economically infeasible

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit: "You hit a wall not because the model is weak." The problem is structural, not capability-based.
- ⭐ B) ✅ The chapter states: "Every big task pollutes that context. The model has to carry it forward. Its attention divides across more material. The thinking gets thinner." This is the structural reason the generalist approach fails.
- C) ❌ LLMs are perfectly capable of multiple tasks per session — the chapter never claims a technical incapacity. The constraint is contextual, not architectural.
- D) ❌ The chapter makes no claim about provider throttling. It frames the limit as a context-management problem, not a billing problem.
- E) ❌ Cost is not the issue the chapter raises. The chapter's argument is about cognitive context pollution, not unit economics.

</details>

---

## Question 2

The chapter uses a dominant medical analogy to explain sub-agents. Which TWO statements correctly describe how that analogy maps to AI work?

- A) Your main AI conversation is the general practitioner who coordinates the case
- B) Sub-agents are the specialists who perform a focused procedure in their own operating room and return only a summary
- C) The patient is the AI model, and the doctors are the users
- D) Sub-agents must always have access to the patient's full medical history to function
- E) Every AI conversation should be a brain surgeon rather than a general practitioner

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "The GP is your main AI conversation. The specialists are sub-agents." The main conversation coordinates; specialists execute.
- ⭐ B) ✅ The chapter states: "The specialist does the procedure in their own operating room (own context), reports back the result, and your GP continues your overall care."
- C) ❌ This inverts the analogy. The user is the client/patient (or attending physician), the AI conversation is the GP, and sub-agents are the specialists. The model is not the patient.
- D) ❌ The chapter explicitly says sub-agents start fresh: "Nothing from your main conversation comes with it — unless you decide to send it." That is the opposite of carrying full history.
- E) ❌ The whole chapter argues the GP role is essential — coordination is what makes the system scale. Trying to be a brain surgeon at every turn is the problem the chapter is solving.

</details>

---

## Question 3

The chapter defines a sub-agent as having four distinct components. Which of the following is NOT one of those four components?

- A) Its own context window
- B) Its own system prompt
- C) Its own tools
- D) Its own permissions
- E) Its own billing account

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter lists this as the first component: "When you spawn a sub-agent, the AI opens a fresh, empty room."
- B) ❌ The chapter lists this as the second component: "A sub-agent has a personality you write."
- C) ❌ The chapter lists this as the third component: "You decide what the sub-agent can touch."
- D) ❌ The chapter lists this as the fourth component: "You decide what the sub-agent is allowed to do."
- ⭐ E) ✅ Billing is never mentioned as a defining component of a sub-agent. The four components in the chapter are context window, system prompt, tools, and permissions.

</details>

---

## Question 4

The chapter describes three built-in sub-agents that most AI environments provide. Which TWO statements correctly describe their roles?

- A) Explore is a fast, read-only specialist that searches and surveys material without polluting your main context
- B) Plan researches in read-only mode to gather context before proposing a plan of action
- C) General-Purpose handles only file editing tasks and refuses to do exploration
- D) Plan is designed to write final client deliverables on behalf of the user
- E) Explore is the most expensive built-in sub-agent and uses the firm's premium model by default

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter's table describes Explore as: "Searches and surveys material in read-only mode. Skims, scans, summarizes." It uses a fast/cheap model.
- ⭐ B) ✅ The chapter's table describes Plan as: "Researches in read-only mode to gather context before proposing a plan of action."
- C) ❌ General-Purpose handles tasks that need both exploration and action — not file editing exclusively. The chapter calls it the specialist for "multi-step tasks that need both exploration and action."
- D) ❌ Plan is described as a research and planning agent that runs in read-only mode. It does not write final deliverables.
- E) ❌ Explore explicitly uses a "fast/cheap" model in the chapter's table. It is the opposite of the firm's premium model.

</details>

---

## Question 5

Chapter 9 introduces a "two-cost rubric" for deciding whether to spawn a sub-agent. What are the two costs that must be weighed against each other?

- A) Token cost and API cost
- B) Delegation cost and context-pollution cost
- C) Training cost and inference cost
- D) Latency cost and bandwidth cost
- E) Human cost and machine cost

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Token and API costs are billing concerns, not the cognitive trade-off the chapter develops. The chapter is about how to organize work, not about how to minimize spend.
- ⭐ B) ✅ The chapter states explicitly: "There are two costs in every task... The first is **delegation cost**... The second is **context-pollution cost**." The rule: when context-pollution cost is bigger, spawn; when delegation cost is bigger, stay.
- C) ❌ Training and inference are technical concepts about how models are built and run — they do not appear in the chapter's decision framework.
- D) ❌ Latency and bandwidth are networking concerns. The chapter does not frame the decision as a performance question.
- E) ❌ The chapter does not contrast human and machine costs. The two costs are both cognitive, both belonging to the user's working context.

</details>

---

## Question 6

According to the chapter, when should a task STAY in your main conversation rather than become a sub-agent?

- A) When the task produces a huge amount of intermediate output you will not need to see again
- B) When the task is exploratory, conversational, and you are still thinking out loud about what you are looking for
- C) When the task is one you perform every Monday with the same exact shape
- D) When the task requires tools you do not want the main conversation to have
- E) When the task is genuinely self-contained with a clear input and a clear output

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This is one of the chapter's explicit triggers for SPAWNING a sub-agent, not for keeping the task in the main conversation. "The task produces a lot of intermediate output you will not need to see again."
- ⭐ B) ✅ The chapter states: "The task is exploratory and conversational. You are thinking out loud. You do not know what you are looking for yet... Sub-agents are bad at exploratory dialogue because they start fresh."
- C) ❌ Repetition is described as a signal to spawn a sub-agent: "Every Monday, you scan industry news... Repetition is the signal."
- D) ❌ Wanting to restrict tools or permissions is a reason to spawn, not to stay: "The task needs tools or permissions you do not want the main conversation to have."
- E) ❌ Self-contained tasks with clear input/output are textbook sub-agent candidates per the chapter: "There is a clear input, a clear output, and no real back-and-forth needed."

</details>

---

## Question 7

The chapter describes five "design dials" for building a custom sub-agent. Which of the following is the correct list?

- A) Scope, system prompt, tools, model selection, permissions
- B) Name, color, icon, owner, version
- C) Memory, hooks, MCP servers, plugins, skills
- D) Speed, accuracy, cost, latency, reliability
- E) Input, processing, output, logging, monitoring

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter labels these as the "Five Dials" in the figure caption and walks through each in order: "Dial One — Scope... Dial Two — System Prompt... Dial Three — Tools... Dial Four — Model Selection... Dial Five — Permissions."
- B) ❌ These are cosmetic and organizational attributes, not the chapter's design dials. The chapter's dials shape behavior, not appearance.
- C) ❌ These are advanced technical configurations mentioned elsewhere in AI documentation, but the chapter explicitly frames the five dials as scope, system prompt, tools, model, and permissions.
- D) ❌ These are evaluation metrics, not design dials. The chapter does not frame sub-agent design as a performance trade-off.
- E) ❌ These are generic software pipeline stages. The chapter is building a job description, not a data pipeline.

</details>

---

## Question 8

The chapter introduces the "least-privilege principle" as a habit for designing sub-agents. Which TWO statements correctly describe what this principle means and why it matters?

- A) Always grant the sub-agent every available tool so it can handle unexpected requests
- B) Give the specialist exactly what it needs to do its job — and nothing more
- C) Every additional tool granted is an additional source of distraction and an additional attack surface
- D) The least-privilege principle applies only to security teams, not to ordinary business users
- E) Once you grant a tool, you should never remove it, because the sub-agent may have learned to depend on it

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This is the exact mistake the chapter warns against: "The most common mistake first-time builders make is granting too much. 'Just give it everything, it'll be easier.' That phrase is the start of the trouble."
- ⭐ B) ✅ The chapter states: "Give the specialist exactly what it needs to do its job — and nothing more. This is called the **least-privilege principle**."
- ⭐ C) ✅ The chapter states: "Every additional tool you grant is an additional attack surface — and an additional source of distraction. The specialist with five tools will use them better than the specialist with twenty."
- D) ❌ The chapter explicitly applies the principle to business users designing sub-agents — it is borrowed from security but described as one of the most important habits any builder can develop.
- E) ❌ The chapter recommends the opposite: "If the job grows, expand the access. If the job shrinks, shrink the access." Permissions should be tuned to the current job, not frozen.

</details>

---

## Question 9

Chapter 9 argues that a personal library of sub-agents becomes more than a productivity tool — it becomes a "compounding asset." What is the strongest reason given for this?

- A) Sub-agents earn interest in a savings account managed by the AI provider
- B) Each specialist encodes a refined version of how you do a certain task, with your standards, your format, and your judgment baked in — making the library proprietary institutional knowledge
- C) The library is automatically licensed to other professionals, generating royalty income
- D) Sub-agents become smarter every time another user in the world spawns them
- E) The library's compounding effect is measured in CPU cycles saved rather than time or judgment captured

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter never describes any financial yield or interest mechanism. "Compounding" here refers to accumulating value over time, not to financial compounding.
- ⭐ B) ✅ The chapter states: "Each specialist contains a refined version of how you do a certain task. Your competitor-brief specialist is not generic — it has your industry context, your preferred output format, your standards... After six months, that library is a real asset. It is the institutional knowledge of how you work, encoded into a set of workers."
- C) ❌ The chapter does not describe any external licensing or royalty model. The library is described as a personal/firm-level asset.
- D) ❌ The chapter never claims sub-agents learn from other users' invocations. They are personal, scoped tools — not a shared learning network.
- E) ❌ The chapter measures compounding in hours of consultant time recovered and in encoded judgment — not in CPU cycles.

</details>

---

## Question 10

In the Cascade Strategy Partners case study, the senior consultants disagree about which tasks should become sub-agents. Which TWO statements correctly describe the source of the disagreement?

- A) Tomás Whittaker argued that market sizing was too core to consulting work to be fully delegated to a sub-agent because it requires nuanced judgment about sources and methodology
- B) Aisha Bello argued that competitor scraping was obviously a sub-agent task because it is high-volume, low-judgment, and repetitive
- C) All five senior consultants agreed unanimously that every production task should become a sub-agent immediately
- D) The disagreement was purely about software vendor choice, not about which tasks belong in which room
- E) Marcus Holloway refused to involve consultants in the decision because the work was strictly an IT matter

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case study states: "Tomás Whittaker, argued that market sizing was *too core* to the consulting work to be delegated to a sub-agent — it required nuanced judgment about which sources to trust, which methodology to apply, which assumptions to flex."
- ⭐ B) ✅ The case study states: "Aisha Bello, took the opposite view: she saw competitor scraping as obviously a sub-agent task — high-volume, low-judgment, repetitive, and exactly the kind of work that should disappear into a specialist's room and come back as a brief."
- C) ❌ The case study describes the working group as disagreeing "sharply" within an hour. Unanimous agreement is the opposite of what happened.
- D) ❌ The case study makes no mention of vendor choice. The disagreement is about *which tasks belong as sub-agents and which stay in the consultant's main conversation* — a strategic question about work design.
- E) ❌ Marcus convened the working group of senior consultants specifically *because* the decision was strategic, not technical: "It would shape what kind of consultants Cascade developed over the next decade."

</details>

---

*Quiz for Chapter 9 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
