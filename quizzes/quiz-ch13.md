# Quiz: Chapter 13 — Hooks, Channels, and Automations

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 13, what is the fundamental difference between reactive AI and proactive AI?

- A) Reactive AI uses smaller models, while proactive AI uses larger frontier models
- B) Reactive AI is a conversation where you type and it answers; proactive AI fires on schedules and triggers without being asked
- C) Reactive AI is cheaper, while proactive AI requires enterprise licensing
- D) Reactive AI runs on your local machine, while proactive AI must run in the cloud
- E) Reactive AI is older technology that has been replaced by proactive AI

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Model size is not the distinction. The chapter explicitly frames the difference as one of *initiation* — who or what starts the work — not technical capability.
- ⭐ B) ✅ The chapter states: "Reactive AI is a conversation. You type. It types back... Proactive AI is a factory. The line runs whether you are watching it or not." This shift from being the input to being the customer of the output is the entire chapter's thesis.
- C) ❌ Pricing tiers are never discussed as the dividing line between the two modes.
- D) ❌ Local vs. cloud is irrelevant to the distinction; both modes can run in either environment.
- E) ❌ The chapter explicitly states most professionals still operate reactively — it is not obsolete, merely incomplete. The chapter argues for adding proactive workflows *on top of* reactive use.

</details>

---

## Question 2

The chapter uses the analogy of a factory floor forty years ago versus the same factory today to make a point about AI. Which TWO statements correctly describe the analogy's lesson?

- A) The old factory represents reactive AI, where every step requires a human standing at a station watching it
- B) The modern automated factory represents proactive AI, where humans focus on judgment calls instead of watching parts move
- C) The analogy argues that the goal of AI is to eliminate all human involvement from work
- D) The analogy proves that AI cannot match the quality of human-supervised work
- E) The analogy is meant to show that AI is a passing trend like prior factory automation

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Imagine a factory floor forty years ago. Every step requires a human operator standing at a station, watching, adjusting, deciding when to move the part to the next station..." — this is the reactive mode, where the human is the bottleneck.
- ⭐ B) ✅ The chapter states: "The humans are still there — but they are at the control room, watching dashboards, making the judgment calls that actually need judgment. Not watching parts move." This is explicitly mapped to proactive AI.
- C) ❌ The chapter explicitly preserves the human role — "you review the output and make the calls that actually require you." The point is *not* eliminating humans, but moving them from watching to judging.
- D) ❌ The chapter never argues AI is lower quality than human-supervised work. Quality is not the dimension being discussed.
- E) ❌ The chapter treats AI automation as a durable structural shift, not a passing trend. The analogy is to a permanent change in factories, not a fad.

</details>

---

## Question 3

In Chapter 13, what is the precise definition of a "hook"?

- A) An AI agent that judges whether a workflow should run based on the current context
- B) A trigger that fires at a specific lifecycle moment and runs a deterministic, predefined action
- C) A scheduled task that runs on a regular calendar cron schedule
- D) A user prompt that initiates an AI conversation
- E) A data connector that links the AI to external SaaS tools

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly contrasts hooks with AI judgment: "The thing the hook does is *not* AI judgment. It is a deterministic rule." Confusing the two is exactly the mistake the chapter warns against.
- ⭐ B) ✅ The chapter states: "A hook is a trigger. Something happens — a file is saved, a message arrives, a session ends, a tool is about to execute — and the hook fires. When it fires, it does one specific, predefined thing." Determinism is the defining property.
- C) ❌ This describes a scheduled task, which the chapter discusses as a separate concept. Hooks fire on events; scheduled tasks fire on time.
- D) ❌ A user prompt initiates a reactive conversation. Hooks fire automatically without a user typing anything.
- E) ❌ This describes a plugin or MCP integration (covered in earlier chapters), not a hook.

</details>

---

## Question 4

The chapter offers a "useful test" for deciding whether something should be a hook or AI judgment. What is that test?

- A) "Would I trust an intern to do this?"
- B) "Would the cost of doing this manually be greater than $50?"
- C) "Would I be comfortable explaining this to a regulator?" — if yes because it always happens this way, it is a hook
- D) "Has the AI done this correctly more than ten times in a row?"
- E) "Is the result something the CEO would read?"

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter never references this test. It is a common-sense framing but not the one the chapter offers.
- B) ❌ Cost thresholds are never used as the deciding factor between hooks and judgment.
- ⭐ C) ✅ The chapter states: "A useful test, when you are deciding whether something belongs in a hook, is to ask: *Would I be comfortable explaining this to a regulator?* If the answer is 'yes, because it always happens this way,' it is a hook. If the answer is 'well, it depends on the situation,' it is judgment."
- D) ❌ Track record is not the test. The chapter argues that determinism, not historical accuracy, is what makes something a hook.
- E) ❌ The audience for the output is irrelevant to whether the underlying action is a rule or a judgment.

</details>

---

## Question 5

According to the chapter, why are channels (Slack, Telegram, iMessage, email) so important for AI workflows?

- A) Because chat interfaces inside AI tools are too slow for professional use
- B) Because regulatory bodies require AI outputs to be delivered through approved channels only
- C) Because the value of an AI output is partly determined by the probability that the right human will actually read it, and channels deliver outputs to where attention already lives
- D) Because most AI tools cannot run inside a browser
- E) Because channels are the only way to get AI to respond in real time

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter does not argue chat interfaces are technically slow. The issue is behavioral, not technical.
- B) ❌ No regulatory channel requirement is mentioned in the chapter.
- ⭐ C) ✅ The chapter states: "The value of an AI output is not just its content — it is the probability that the right human will actually read it. A brilliant briefing posted to a dashboard nobody opens has zero value. A merely decent briefing posted to a channel everyone reads has enormous value."
- D) ❌ This is technically inaccurate and unrelated to the chapter's argument about channels.
- E) ❌ Channels are about *delivery location*, not response time. The chapter never frames channels as a real-time mechanism.

</details>

---

## Question 6

Which TWO statements correctly describe the Sapient Bio example used in the Channels section?

- A) The team's adoption of AI-generated experiment results jumped from 20% to 94% when the output channel changed from a custom dashboard to a Slack channel
- B) The change in adoption proved that the *quality* of the AI output had improved dramatically
- C) The change in adoption proved that the *location* of the AI output, not its content, was the binding constraint on use
- D) The team abandoned AI workflows altogether after the dashboard failed
- E) Sapient Bio is described in the chapter as a 900-person pharmaceutical company in San Diego

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Adoption jumped from twenty percent to ninety-four percent of the team in three weeks."
- B) ❌ The chapter explicitly says: "The intelligence did not change. The location of the intelligence did." Quality was not the variable.
- ⭐ C) ✅ The chapter explicitly states this: "The intelligence did not change. The location of the intelligence did." The whole point of the example is that channel choice, not content quality, was the binding constraint.
- D) ❌ The team did not abandon AI; they redirected its output. The lesson is about channel selection, not AI abandonment.
- E) ❌ Sapient Bio is described as a 90-person genomics startup in Boston, not a 900-person pharma in San Diego.

</details>

---

## Question 7

The chapter describes the "morning briefing agent" pattern. Which of the following best captures what it does and why it matters?

- A) It is a one-time AI conversation that helps you plan your day when you first sit down
- B) It is an AI agent that fires every weekday at a set time, pulls from calendar, email, projects, and news, composes a one-page briefing, and delivers it to the user's preferred channel before they start work
- C) It is a chatbot you message when you want a summary of your morning meetings
- D) It is a dashboard the user opens to view AI-generated insights on demand
- E) It is a custom-built AI model trained on the user's personal data

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This describes a reactive AI conversation, which is the *opposite* of the briefing pattern the chapter advocates. The briefing fires on its own, before you sit down.
- ⭐ B) ✅ The chapter states: "Every weekday at 7:00 AM, an AI agent wakes up. It checks your calendar for today's meetings. It pulls the most recent emails from your three most important clients... By 7:15, before you have had your first sip of coffee, the briefing is waiting." This is the canonical example of a scheduled task.
- C) ❌ This is again reactive use, not scheduled proactive use. The chapter emphasizes that the briefing arrives without being asked.
- D) ❌ A dashboard is a pull mechanism; the briefing is a push mechanism delivered to the user's existing channel.
- E) ❌ The briefing agent uses standard AI tools; no custom-trained model is involved or required.

</details>

---

## Question 8

In the law firm intake example, which TWO of the following steps does the chapter say should be implemented as deterministic hooks rather than AI judgment?

- A) The conflicts database check before opening a new matter
- B) The categorization of the matter (contract, tort, employment, regulatory)
- C) The audit log entry for every AI action in the workflow
- D) The drafting of the matter summary in the firm's voice
- E) The recommendation of which partner should be assigned to the matter

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "There is no scenario — none — where the firm wants to open a new matter without checking the conflicts database. So that is a hook. It fires whenever a new matter intake form is submitted. It does not ask the AI's opinion. It just checks."
- B) ❌ The chapter states matter categorization is "a judgment call. Is this intake a contract dispute, a tort claim, an employment matter, a regulatory action? The answer depends on reading the form carefully and applying domain knowledge. That is AI work."
- ⭐ C) ✅ The chapter states: "The audit log is a hard rule. Every AI action in the workflow gets logged with a timestamp and the user's credentials. No exceptions. Hook."
- D) ❌ The chapter explicitly classifies drafting as judgment: "The draft of the matter summary is judgment. It requires synthesizing the facts, identifying the relevant precedents, and writing in the firm's voice. AI work."
- E) ❌ The chapter classifies partner assignment as AI work: "The recommendation on which partner should take the matter is judgment. It requires reading the matter's complexity, the partners' current workloads, and the relevant expertise. AI work."

</details>

---

## Question 9

The chapter describes the "automation stack" as composed of five layers. Which of the following correctly names those five layers?

- A) GPUs, models, prompts, channels, and dashboards
- B) Memory, sub-agents, hooks, channels, and scheduled tasks
- C) Cloud, API, SDK, CLI, and IDE
- D) Marketing, sales, operations, finance, and IT
- E) Training data, fine-tuning, deployment, monitoring, and retirement

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ These are infrastructure components, not the conceptual layers the chapter describes. The chapter's stack is at the workflow level, not the infrastructure level.
- ⭐ B) ✅ The chapter states: "Memory is what the department knows... Sub-agents are the workers... Hooks are the standard operating procedures... Channels are the report distribution... Scheduled tasks are the calendar." These are the five composing layers of the automation stack.
- C) ❌ These are software-engineering terms unrelated to the chapter's framework.
- D) ❌ These are business functions, not layers of an AI automation stack.
- E) ❌ These are stages of an ML development lifecycle, not the workflow composition layers the chapter describes.

</details>

---

## Question 10

The chapter raises an "accountability question" about automated workflows. According to the chapter, when an automation fires wrong and produces a bad outcome, who is responsible?

- A) The AI model, which should be replaced with a more reliable version
- B) The vendor of the AI tool, who must be sued for damages
- C) The human who designed the workflow and the human who reviewed the output — never "the AI"
- D) Nobody is responsible because automated systems are inherently exempt from accountability
- E) The end client, who agreed to interact with an AI-powered system

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly rejects this: "The answer is never 'the AI.'" Treating the model as the responsible party is the failure mode the chapter warns against.
- B) ❌ Vendor liability is never discussed as the answer. The chapter places responsibility on the human designer, not the tool provider.
- ⭐ C) ✅ The chapter states: "When automation fires wrong, who is responsible? The answer is never 'the AI.' The answer is the human who designed the workflow — and the human who reviewed the output." It also prescribes the structure: "Build your automations so that high-stakes outputs... always include a human review step before they leave your organization. The AI drafts. The human signs. That is the contract."
- D) ❌ The chapter argues the opposite — that accountability must be designed *into* the workflow precisely because automation does not create immunity.
- E) ❌ The chapter never shifts responsibility to the end client. Responsibility stays with the workflow designer and the reviewer.

</details>

---

*Quiz for Chapter 13 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
