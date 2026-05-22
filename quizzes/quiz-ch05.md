# Quiz: Chapter 5 — The Six Engineering Disciplines

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 5, what is the chapter's central claim about prompt engineering — the "hot job title" of 2023?

- A) Prompt engineering is the single most valuable AI skill and the rest of the disciplines are unnecessary
- B) Prompt engineering is real and valuable but is the *least powerful* of six disciplines that determine how much value you extract from AI — it is the lobby of a six-story building, and the leverage lives on the floors above
- C) Prompt engineering is overrated and produces no measurable value
- D) Prompt engineering can only be done by people with a computer science degree
- E) Prompt engineering is being replaced by automated prompt generators and will not exist as a discipline by 2026

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter argues the opposite: "If all you know how to do is write a good prompt, you are standing in the lobby of a six-story building."
- ⭐ B) ✅ The chapter states: "Here is the thing about prompt engineering: it is real, it is valuable, and it is the least powerful of the six disciplines that determine how much value you actually extract from AI. If all you know how to do is write a good prompt, you are standing in the lobby of a six-story building. You know how to open the front door. But the leverage — the compounding, structural, career-defining leverage — lives on the floors above you."
- C) ❌ The chapter is explicit that prompt engineering is "real" and "valuable" — just not the ceiling.
- D) ❌ No engineering prerequisites are stated in the chapter.
- E) ❌ The chapter does not predict the disappearance of prompt engineering as a discipline.

</details>

---

## Question 2

The chapter lists six engineering disciplines in stack order. Which TWO of the following are among the six?

- A) Prompt engineering — crafting individual instructions that produce high-quality outputs
- B) Harness engineering — designing the environment your AI operates within (tools, workflows, triggers, output routing)
- C) Acoustic engineering — calibrating the audio quality of voice-to-AI dictation tools
- D) Marketing engineering — generating brand awareness for your AI assistant
- E) Financial engineering — structuring tax shelters around AI deployments

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter lists Discipline One: "Prompt engineering is the skill of crafting individual instructions that produce high-quality outputs."
- ⭐ B) ✅ The chapter lists Discipline Six: "Harness engineering is the discipline of designing the *environment* your AI operates within. Not a single prompt. Not a single conversation. The entire ecosystem: the tools connected, the workflows defined, the triggers that set things in motion, the outputs that route to the right places." The six are prompt, system, meta, context, memory, and harness engineering.
- C) ❌ Acoustic engineering is not one of the six disciplines.
- D) ❌ Marketing engineering is not one of the six disciplines.
- E) ❌ Financial engineering is not one of the six disciplines.

</details>

---

## Question 3

The chapter argues that a well-engineered prompt has four components. Which is the correct list?

- A) Task, Context, Format, Examples
- B) Token, Temperature, Top-K, Top-P
- C) Input, Output, Latency, Throughput
- D) Subject, Verb, Object, Modifier
- E) Login, Session, Cookie, Cache

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "**The four components of a strong prompt: Task** — What exactly do you want produced?... **Context** — What does the AI need to know to do this well?... **Format** — How should the output be structured?... **Examples** — When precision matters, show one."
- B) ❌ These are model hyperparameters, not the four components of a prompt.
- C) ❌ These are performance metrics, not prompt components.
- D) ❌ Grammar parts of speech are not the chapter's framework.
- E) ❌ Web session concepts are unrelated.

</details>

---

## Question 4

The chapter explains what makes a *system prompt* different from a regular prompt. Which statement best captures the chapter's framing?

- A) A system prompt is identical to a regular prompt but more expensive
- B) A system prompt is a standing instruction that loads silently before every exchange — it defines the AI's role, rules, tone, boundaries, and understanding of who it is working for; the AI reads it first, every time, before reading your message
- C) A system prompt is a message sent by the AI to the user at the end of the conversation
- D) A system prompt is the AI's response to the question "how do you work?"
- E) A system prompt is the legal disclaimer required for compliance

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter never claims system prompts cost extra.
- ⭐ B) ✅ The chapter states: "A system prompt is a standing instruction that loads silently before every exchange. It defines the AI's role, its rules, its tone, its boundaries, and its understanding of who it is working for. The AI reads it first, every time, before it reads your message."
- C) ❌ The system prompt is set by the user, not generated by the AI.
- D) ❌ The system prompt is not a self-description by the AI.
- E) ❌ Legal disclaimers are not what a system prompt is.

</details>

---

## Question 5

According to the chapter, what is **meta prompting**, and what is the recommended rule of thumb for when to use it?

- A) Meta prompting is using AI to write the instructions that AI will use — and the rule of thumb is: if you are about to write instructions that will be used more than once, do not write them yourself; let Claude write them
- B) Meta prompting is asking the AI questions about itself
- C) Meta prompting is writing prompts in Greek so models pay closer attention
- D) Meta prompting is illegal under most AI vendors' terms of service
- E) Meta prompting is only useful for academic researchers

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Meta prompting is the practice of using AI to write the instructions that AI will use. You are not writing the prompt. You are asking AI to write the prompt — and then using that prompt to do the actual work." And: "The rule of thumb: if you are about to write instructions that will be used more than once, do not write them yourself. Let Claude write them."
- B) ❌ Asking the AI about itself is introspection, not meta-prompting.
- C) ❌ Language is not the variable in meta-prompting.
- D) ❌ The chapter never describes meta-prompting as forbidden — it is a recommended practice.
- E) ❌ The chapter applies meta-prompting to system prompts, Gems, skills, and workflows — all business use cases, not academic.

</details>

---

## Question 6

The chapter argues there are *three reasons* context engineering matters. Which TWO of the following are reasons the chapter explicitly gives?

- A) More context is not always better — the AI's working memory is finite, and filling it with irrelevant information leaves less room for what matters
- B) The order of context matters — information placed early in a conversation has more influence on the AI's framing than information placed late
- C) Context engineering is only useful for tasks involving images, not text
- D) Context engineering doubles your monthly subscription cost
- E) Context engineering is performed automatically by all major models without user intervention

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "First: more context is not always better. The AI's working memory — the context window we covered in Chapter 1 — is finite. Fill it with irrelevant information and the AI has less room for what matters."
- ⭐ B) ✅ The chapter states: "Second: the order of context matters. Information placed early in a conversation has more influence on the AI's framing than information placed late."
- C) ❌ The chapter discusses text-based context throughout; the modality limit claim is fabricated.
- D) ❌ Cost is never the chapter's reason for context engineering.
- E) ❌ The chapter argues the opposite — context engineering must be *deliberate*; nothing about it is automatic.

</details>

---

## Question 7

According to the chapter, what is the "dirty secret" of AI that memory engineering addresses?

- A) AI's training data is incomplete
- B) AI does not remember you — every conversation begins at zero; close a chat, open a new one, and the model has no idea who you are, what you have discussed, what decisions you have made, or what you are working on
- C) AI's responses are cached and never original
- D) AI generates answers by copying directly from Wikipedia
- E) AI requires a daily reboot to function

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Training data completeness is not the chapter's framing of the "dirty secret."
- ⭐ B) ✅ The chapter states: "AI has a dirty secret. It does not remember you. Every conversation begins at zero. Close a chat window, open a new one, and the model has no idea who you are, what you have talked about, what decisions you have made, or what you are working on. Whatever felt like a productive working relationship in yesterday's session is completely gone today."
- C) ❌ The chapter never claims responses are cached copies.
- D) ❌ Wikipedia copying is not the chapter's claim.
- E) ❌ Daily reboots are not mentioned in the chapter.

</details>

---

## Question 8

The chapter describes three *layers* of memory engineering. Which TWO of the following correctly describe layers named in the chapter?

- A) Conversation memory — what the AI knows within a single session (automatic, but disappears when the session ends)
- B) File-based memory — what you explicitly save and inject into future conversations, such as a one-page "Working Brief" or "My Context" document attached at the start of important sessions
- C) Telepathic memory — the AI's ability to read your mind across distance without input
- D) Genetic memory — DNA-encoded model weights inherited from previous AI generations
- E) Photographic memory — an exact pixel-level recall of every screenshot you have taken

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "**Conversation memory** is what the AI knows within a single session. This is automatic — the AI sees everything that has been said in the current conversation. No engineering required, but it disappears when the session ends."
- ⭐ B) ✅ The chapter states: "**File-based memory** is what you explicitly save and inject into future conversations... Many professionals maintain a living document called something like *'My Context'* or *'Working Brief'* — updated weekly — that they paste or attach at the start of important sessions." The three layers are conversation, file-based, and database memory.
- C) ❌ Telepathic memory is a fabricated category.
- D) ❌ Genetic memory is a fabricated category.
- E) ❌ Photographic memory of screenshots is a fabricated category.

</details>

---

## Question 9

The chapter gives a vivid example of **harness engineering** in action: an email from a prospective client. Which statement correctly summarizes the example?

- A) An email arrives → the harness fires automatically: AI reads the email via the Gmail connector, searches Drive for prior documents related to the contact, checks Calendar for availability, drafts a reply in your voice, and places the draft in your Gmail drafts folder flagged for review — you appear at the end, for thirty seconds, to confirm and send
- B) The harness sends every email to a human assistant in another country for processing
- C) The harness ignores the incoming email and waits for you to manually respond
- D) The harness automatically sends a response without any human review
- E) The harness deletes the email and notifies you nothing happened

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "you get an email from a prospective client. Your harness — a set of rules you have defined — triggers automatically. Your AI reads the email via the Gmail connector. It searches your Drive for any prior documents related to this contact. It checks your calendar for availability. It drafts a reply in your voice. It places that draft in your Gmail drafts folder, flagged for your review. You review, adjust if needed, and send. You were not in that loop. You appeared at the end, for thirty seconds, to confirm and send."
- B) ❌ The chapter never describes outsourcing to human assistants.
- C) ❌ The whole point of a harness is that it *acts* automatically.
- D) ❌ The chapter is explicit that the draft goes to your drafts folder for *review* — the human reviews before sending.
- E) ❌ Deleting incoming emails is not what the harness does.

</details>

---

## Question 10

In the Meridian Wealth Partners case study, the consultant offered an unexpected framing of the firm's adoption failure. Which TWO statements correctly describe the diagnosis and the proposed phased solution?

- A) The firm's problem was not that advisors were bad at prompting — it was that the firm had stopped at Floor 1 in a six-floor building, and the value they were looking for was on Floors 3 through 6
- B) Phase 3 introduced meta prompting — rather than improvising new prompts from scratch for each recurring task, advisors would work with the AI to design and refine a library of Skills for the firm's highest-frequency use cases (client meeting prep, portfolio commentary, prospecting outreach, regulatory disclosure summaries)
- C) The consultant recommended firing the 78% of advisors who had abandoned the tool
- D) The consultant recommended cancelling the AI subscription and returning to manual workflows entirely
- E) The consultant said no investment in disciplines beyond prompt engineering was warranted

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "the firm's problem was not that its advisors were bad at prompting. It was that the firm had stopped at Floor 1 in a six-floor building — and the value they were looking for was on Floors 3 through 6."
- ⭐ B) ✅ The case states: "Phase 3 would introduce meta prompting: rather than individual advisors improvising new prompts from scratch for each recurring task, they would work with the AI to design and refine a library of Skills for the firm's highest-frequency use cases — client meeting prep, portfolio commentary, prospecting outreach, and regulatory disclosure summaries."
- C) ❌ The case never recommends firing advisors.
- D) ❌ The case never recommends cancelling the subscription.
- E) ❌ The case is explicit that the consultant recommended building all six floors.

</details>

---

*Quiz for Chapter 5 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
