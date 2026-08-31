# Quiz: Chapter 7 — Memory: How Your AI Learns You

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 7, how does AI memory actually work at the model level — and why does the chapter say whatever memory a product offers is not enough?

- A) Models remember everything permanently; the chapter's concern is purely about cost
- B) The model core is *stateless* — each conversation is a self-contained context window that is cleared when the session ends; whatever memory a product offers on top of that core is a vendor feature — bolted on, vendor-specific, subject to change — that you did not choose, cannot always inspect, and cannot carry with you when you switch tools
- C) The model intentionally erases memory to charge you more next time
- D) Memory is a simple settings toggle, and turning it on solves the problem completely
- E) AI remembers nothing under any circumstances — no product offers any memory feature

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit that the model core does not store information between conversations.
- ⭐ B) ✅ The chapter states: "Large language models do not store information between conversations — they are designed as stateless systems... At that level, statelessness is a feature, not a failure." And: "whatever memory a product offers on top of the stateless model is a vendor feature — bolted on, vendor-specific, subject to change. You did not decide what it kept. You cannot always see what it kept. And you cannot take what it kept with you when you switch tools."
- C) ❌ Statelessness is not described as a billing mechanism.
- D) ❌ The chapter argues built-in memory — however configured — is never your system of record; the professional's solution is a memory layer you own.
- E) ❌ The chapter acknowledges some products "quietly save fragments of past conversations and surface them later" — the problem is that you don't control it.

</details>

---

## Question 2

The chapter introduces the **three tiers of memory**. Which TWO of the following correctly describe two of those tiers?

- A) Conversation Memory — automatic, available throughout a single session, disappears when the session ends and is bounded by the context window
- B) File-Based Memory — a working brief or context document you maintain about yourself and attach/paste at the start of sessions where continuity matters; manual but powerful and works with any AI tool on any platform
- C) Holographic Memory — encoded into the wallpaper of the user's office for ambient AI absorption
- D) Telepathic Memory — direct neural link between user and AI requiring no input
- E) Astral Memory — memory shared across all users of a given vendor cloud

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Tier One: Conversation Memory. This is automatic. Everything said within a single conversation is available to the AI throughout that session... The limitation is that it disappears the moment the session ends, and it is bounded by the context window."
- ⭐ B) ✅ The chapter states: "Tier Two: File-Based Memory. This is where your intentional memory engineering begins. A memory file — often called a working brief, a context document, or simply a memory file — is a document you maintain about yourself and your work. You attach or paste it at the start of sessions where continuity matters." The third tier is Database Memory (Supabase, Chapter 3).
- C) ❌ Holographic memory is a fabricated category.
- D) ❌ Telepathic memory is a fabricated category.
- E) ❌ Astral/shared-cloud memory is a fabricated category.

</details>

---

## Question 3

The chapter argues that the **memory file** has four properties that make it effective. Which is correct?

- A) Short (one page ideal, two maximum), structured (clear sections, not narrative), current (updated regularly), and yours (calibrated to your specific context — not a template)
- B) Encrypted, notarized, archived offline, and password-protected
- C) At least 50 pages, written in legal English, signed by witnesses
- D) Public, indexed by search engines, and viewable by anyone
- E) Audio-only, recorded weekly, transcribed manually

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "It is **short**. One page is ideal. Two pages maximum... It is **structured**. Not a narrative essay about yourself, but clear sections... It is **current**. A memory file from three months ago that describes projects you have finished and priorities you have moved past is actively misleading... It is **yours**. The memory file is not a template to fill in. It is a calibration of your specific context."
- B) ❌ These cryptographic properties are not in the chapter.
- C) ❌ Length, legal English, and witnesses are not requirements.
- D) ❌ Public indexing is the opposite of the chapter's privacy stance.
- E) ❌ Audio-only is not what the chapter recommends.

</details>

---

## Question 4

The chapter argues a common mistake is confusing memory with context. According to the chapter, what is the correct distinction?

- A) Memory and context are identical — the words are interchangeable
- B) **Context** is what you provide in a specific conversation (documents attached, info shared, the question asked) and exists within the session targeted to the task at hand; **memory** is what persists between sessions (a standing brief about who you are and what you are working on) — broader and less task-specific, giving the AI a foundation to work from rather than a set of instructions for a specific task
- C) Memory is paid; context is free
- D) Context only works in one vendor's tool; memory only works in another's
- E) Memory is what the AI provides; context is what the user provides

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly says they are not the same and that confusing them "leads to bad habits."
- ⭐ B) ✅ The chapter states: "**Context** is what you provide in a specific conversation — the documents you attach, the information you share, the question you ask. It exists within the session. It is targeted to the task at hand. **Memory** is what persists between sessions — the standing brief about who you are and what you are working on. It is broader and less task-specific. It gives the AI a foundation to work from, not a set of instructions for a specific task."
- C) ❌ Cost is not the distinction.
- D) ❌ The chapter is platform-agnostic about the distinction.
- E) ❌ Both memory and context are user-provided in the chapter.

</details>

---

## Question 5

According to the chapter, what is "the most important skill in memory engineering" — and what is the curation question you should ask?

- A) The most important skill is *what to leave out* of your memory file — the curation question is: "does the AI need to know this to work effectively with me on future tasks?" If yes, it belongs; if it is interesting but not operationally useful (one-time situations, non-recurring detail, task-specific nuance), it does not belong
- B) The most important skill is encrypting the memory file with a 256-bit key
- C) The most important skill is uploading the file to the largest possible cloud provider
- D) The most important skill is reading the file aloud once a week
- E) The most important skill is keeping the memory file at over 50 pages so nothing is missed

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "The most important skill in memory engineering is not what to put in your memory file. It is what to leave out... The curation question is: **does the AI need to know this to work effectively with me on future tasks?** If yes, it belongs. If it is interesting but not operationally useful — if it is context about a one-time situation, detail that will not recur, or nuance that applies only to the specific task you just finished — it does not belong."
- B) ❌ Encryption is not framed as the most important skill.
- C) ❌ Cloud provider choice is not the answer.
- D) ❌ Reading aloud is not a chapter recommendation.
- E) ❌ The chapter argues for the opposite of a 50-page file.

</details>

---

## Question 6

The chapter lists triggers for *updating* the memory file and triggers for *archiving/removing* content. Which TWO are correctly drawn from the chapter?

- A) Update when: your role or responsibilities change significantly, a new project becomes a major focus, a key relationship becomes important enough to know about, or you discover a preference/frustration you keep having to re-explain
- B) Archive/remove when: a project is complete, a priority has shifted, a relationship is no longer active, or preferences have evolved
- C) Update when the AI vendor changes its terms of service
- D) Archive when the moon enters a new lunar phase
- E) Update only on national holidays

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter lists these exact update triggers: "Your role or responsibilities change significantly. A new project becomes a major focus. A key relationship becomes important enough that the AI should know who this person is. You discover a preference or frustration that you keep having to re-explain."
- ⭐ B) ✅ The chapter lists these exact archive triggers: "A project is complete. A priority has shifted. A relationship is no longer active. Preferences have evolved."
- C) ❌ Vendor terms of service are not a chapter trigger.
- D) ❌ Lunar phases are not a chapter trigger.
- E) ❌ Holidays are not a chapter trigger.

</details>

---

## Question 7

The chapter offers a **privacy spectrum** for what does and does not belong in a memory file. Which statement best captures the chapter's guidance?

- A) Generally appropriate: your professional role, general priorities, working style, communication preferences (information you would share in a professional introduction). Requires careful thought: client names/details, sensitive business information, confidential strategic plans, financial specifics. Never include: passwords, authentication credentials, truly sensitive personal information, anything you would not want a colleague to see
- B) Anything you do not want public should always be included so the AI can protect it
- C) Memory files must include your social security number and tax filings
- D) Memory files should never contain any information about your job
- E) Memory files must be reviewed and approved by a lawyer before each use

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states these three tiers explicitly: "What is generally appropriate: your professional role, your general priorities, your working style, your communication preferences. This is the kind of information you would share in a professional introduction. What requires more careful thought: client names and details, sensitive business information, confidential strategic plans, financial specifics... What should never be in a memory file: passwords, authentication credentials, truly sensitive personal information, anything you would not want a colleague to see."
- B) ❌ The chapter is explicit that the most sensitive items should be excluded — not included for protection.
- C) ❌ SSN and tax filings would fall under the "never include" category.
- D) ❌ The chapter is explicit that professional context is appropriate to include.
- E) ❌ Legal review is not required by the chapter.

</details>

---

## Question 8

The chapter argues memory engineering produces a *compounding* effect over six months. Which statement best matches the chapter's arc?

- A) Week one: less time re-explaining yourself, sessions start faster and stay on track. End of month one: outputs are calibrated to your actual situation (specific recommendations that account for real context, constraints, relationships). End of month six: a working relationship with genuine depth — the AI has not gotten smarter, your use of it has become dramatically more sophisticated; this delivers an ever-growing advantage very difficult for someone starting from scratch to replicate
- B) The memory file produces no measurable benefit no matter how long you use it
- C) The compounding effect only works for users over 65
- D) The compounding effect requires you to retrain the model yourself
- E) After six months you must delete everything and start over to avoid bias

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "In the first week, you notice you are spending less time re-explaining yourself... Sessions start faster and stay on track. By the end of the first month, you notice the AI's outputs are calibrated to your actual situation — not generic advice, but specific recommendations that account for your real context, your real constraints, your real relationships. By the end of the sixth month, you have a working relationship that has genuine depth... The AI has not gotten smarter. Your use of it has become dramatically more sophisticated. This is the compounding value of memory engineering... an ever-growing advantage that is very difficult for someone starting from scratch to replicate."
- B) ❌ The chapter argues exactly the opposite.
- C) ❌ Age is not a chapter variable.
- D) ❌ Retraining the model is not the mechanism.
- E) ❌ The chapter recommends *updating*, not wholesale deletion every six months.

</details>

---

## Question 9

In the Meridian Strategy Group case study, what was the *root pattern* that Director of Knowledge Management Darius Okafor identified to explain why senior partners were the most dissatisfied users?

- A) The firm had deployed a stateless AI tool into a relationship-intensive business, and no one had built a memory layer to bridge the gap — consultants were treating each AI session as a discrete event rather than a continuation of an ongoing working relationship, and the result was a failure to capture and leverage the institutional knowledge that was Meridian's core differentiator
- B) The senior partners were too old to learn new technology
- C) The Big Four had hacked Meridian's AI portal
- D) The AI provider had specifically disabled features for Meridian's account
- E) The senior partners were intentionally sabotaging the rollout

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "Okafor had a background in enterprise knowledge systems and immediately recognized the pattern: the firm had deployed a stateless AI tool into a relationship-intensive business, and no one had built a memory layer to bridge the gap. Consultants were treating each AI session as a discrete event rather than a continuation of an ongoing working relationship. The result was not just inefficiency — it was a failure to capture and leverage the institutional knowledge that was Meridian's core differentiator."
- B) ❌ The case never mentions age as a factor.
- C) ❌ No hacking is mentioned.
- D) ❌ No vendor disabling is mentioned.
- E) ❌ The case says senior partners were dissatisfied users, not saboteurs.

</details>

---

## Question 10

In the Meridian case study, Okafor proposes a "Client Intelligence Brief" — a structured maintained document for each active client engagement. According to the case, what TWO objections did senior partners raise about the proposal?

- A) A partner managing a sensitive financial restructuring engagement asked: "Are you asking me to put confidential client information into a document that runs through a third-party AI system?"
- B) Another partner raised information governance: if the briefs accumulated over months of engagement, how would the firm manage what was remembered, what was updated, and what should be retired once an engagement closed?
- C) A partner demanded the briefs be written in Latin
- D) A partner refused to use any AI tool that did not include a free coffee subscription
- E) A partner argued the briefs should be public on the firm's website

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "One partner, managing a sensitive financial restructuring engagement for a regional bank, asked pointedly: 'Are you asking me to put confidential client information into a document that runs through a third-party AI system?'"
- ⭐ B) ✅ The case states: "Another raised the issue of information governance: if the briefs accumulated over months of engagement, how would the firm manage what was remembered, what was updated, and what should be retired once an engagement closed?"
- C) ❌ Latin is not a case demand.
- D) ❌ The coffee subscription is fabricated.
- E) ❌ Public website briefs would contradict the entire confidentiality concern.

</details>

---

*Quiz for Chapter 7 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
