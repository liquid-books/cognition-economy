# Quiz: Chapter 14 — Security and Trust

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 14, what is the dominant analogy the chapter uses to frame AI security for business leaders?

- A) Treating AI like a locked vault that no one can ever access
- B) Treating AI like a brilliant new employee on her first day — set up access controls, sign an NDA, build a culture, then trust the system you built
- C) Treating AI like a household pet that needs constant supervision
- D) Treating AI like an outside vendor that must be reviewed annually but otherwise ignored
- E) Treating AI like a closed-source product whose internals must never be questioned

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly argues against this — a vault metaphor would imply paranoia, but the chapter rejects the "don't use AI" posture in favor of operating inside guardrails.
- ⭐ B) ✅ The chapter states directly: "Think about hiring a brilliant new employee on her first day... You define what she can and cannot access. You write down clear policies... You sign an NDA. You build a culture where she knows what is appropriate. AI security is the same."
- C) ❌ The chapter explicitly rejects the "follow them around watching everything they touch" posture as "insulting, exhausting, and ineffective."
- D) ❌ Annual review is not the chapter's model; the chapter recommends continuous practices (least privilege, audit trails, briefings) rather than annual events.
- E) ❌ The chapter does not frame AI as a closed system; it frames AI security as something the operator actively shapes with contracts, configurations, and culture.

</details>

---

## Question 2

The chapter introduces four questions every business leader must answer before deploying any AI tool. Which TWO statements correctly describe these four questions?

- A) The four questions are technical-architecture questions intended only for the IT team
- B) One of the four questions is "Where does my data go?" — covering jurisdiction, vendor processing, and whether data leaves your network
- C) One of the four questions is "What happens if it leaks?" — covering vendor incident response and your contractual recourse and notification obligations
- D) The four questions can be safely skipped if your vendor is a well-known frontier AI lab
- E) The four questions apply only to AI tools handling regulated industries like healthcare and finance

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly states: "These four questions are not a checklist for the IT team. They are a checklist for you — the operator, the leader, the executive who is going to be answering for the choice the day the auditor walks in."
- ⭐ B) ✅ The chapter lists this as question 1: "Where does my data go? What jurisdictions does the vendor process it in? Does it leave your country? Does it leave your network at all?"
- ⭐ C) ✅ The chapter lists this as question 4: "What happens if it leaks? What is the vendor's incident-response process? What is your contractual recourse? What is your obligation to notify your clients or your regulator?"
- D) ❌ The chapter explicitly rejects vendor reputation as a substitute, noting that vendors that "deflect, hedge, or send you to a 90-page legal document are telling you something about how they think about their obligations."
- E) ❌ The chapter states the four questions apply to "every tool, not just the obvious ones" — including marketing automation chatbots, AI email assistants, and transcription services.

</details>

---

## Question 3

The chapter opens with a scene involving Vanessa Crowder, CMO of a wealth-management firm. What is the central security failure in her story?

- A) Her IT team installed an unauthorized AI tool on the firm's network
- B) Her marketing team had been pasting client portfolio data into the free consumer version of ChatGPT, where it became part of the training corpus
- C) A hacker breached her firm's enterprise AI tier and stole client records
- D) Her CISO had configured a vendor SLA incorrectly, exposing the firm to liability
- E) A foreign government compelled an AI vendor to hand over the firm's data

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit that there was "no insider threat" and no unauthorized installation by IT — the tool was a public, consumer-tier product the team chose on their own.
- ⭐ B) ✅ The chapter states: "members of Vanessa's marketing team... have been pasting client portfolio data into the free consumer version of ChatGPT... Under the terms of the firm's consumer-tier ChatGPT usage, that data became part of the training corpus."
- C) ❌ The chapter explicitly notes there were "no bad actors" and "no phishing email" — the issue was not a breach but a failure of policy and culture around consumer-tier usage.
- D) ❌ The chapter frames the failure as a cultural and policy gap — "a culture that had never sat them down for the fifteen-minute conversation" — not a CISO misconfiguration.
- E) ❌ The chapter does not invoke foreign government compulsion; the failure is internal to the firm's own usage practices.

</details>

---

## Question 4

The chapter draws a sharp distinction between consumer AI products and enterprise AI products. Which TWO statements correctly describe this distinction as the chapter presents it?

- A) Consumer and enterprise products always run on completely different underlying models
- B) In consumer products, prompts are typically used to improve the model; in enterprise products, by contract, your data is not used for training
- C) Enterprise products are slower than consumer products because of the added security overhead
- D) The contractual wrapper around the same model is "the entire point of the enterprise product"
- E) Consumer products are illegal for any business use regardless of the data involved

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly states: "Consumer AI products and enterprise AI products often run on the exact same underlying model... what is not identical... is the contract that surrounds it."
- ⭐ B) ✅ The chapter states: "In the consumer version of most AI tools, your prompts are typically used to improve the model... In the enterprise version, that bargain is reversed... your data is, by contract, not used for training."
- C) ❌ The chapter does not claim enterprise products are slower; it emphasizes that the difference is contractual, not performance-related.
- ⭐ D) ✅ The chapter states directly: "The enterprise tier exists, in large part, to make this guarantee" and the contractual wrapper "is in fact the entire point of the enterprise product."
- E) ❌ The chapter does not claim consumer products are illegal — it uses the "screenshot test" to identify when they are inappropriate, but allows them for non-sensitive personal and internal use.

</details>

---

## Question 5

The chapter introduces the "screenshot test." What is it?

- A) A technical audit method in which IT takes screenshots of every employee's AI session
- B) A simple intuitive test — before pasting anything into an AI tool, ask whether you'd be comfortable seeing it on the public internet tomorrow
- C) A vendor due-diligence procedure involving screenshots of the vendor's data center
- D) A compliance reporting tool used by regulators
- E) A type of phishing attack that uses AI-generated screenshots

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter does not describe any IT-administered screenshotting process; the screenshot test is a personal heuristic for the individual employee.
- ⭐ B) ✅ The chapter states: "Before you paste anything into an AI tool, ask yourself: would I be comfortable if someone took a screenshot of this prompt and posted it on the public internet tomorrow? If the answer is yes, the consumer tier is fine. If the answer is no, you need a tool with an enterprise contract behind it."
- C) ❌ The screenshot test in the chapter is not about vendor due diligence — it is described as "not technical" but "intuitive."
- D) ❌ The chapter does not associate the screenshot test with regulatory reporting.
- E) ❌ The chapter does not discuss phishing attacks; the screenshot test is a decision-making heuristic for employees.

</details>

---

## Question 6

What does Zero Data Retention (ZDR) mean in the chapter's definition?

- A) The vendor retains data only for thirty days before deletion
- B) The vendor processes prompt and data only long enough to generate a response, then discards them — nothing is logged, stored, or used for training
- C) The customer is required to delete all AI outputs within twenty-four hours
- D) The vendor anonymizes all data but retains it indefinitely for analytics
- E) ZDR is a technical certification that vendors must purchase from regulators

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly contrasts ZDR with the typical thirty-day retention model — ZDR is zero, not thirty days.
- ⭐ B) ✅ The chapter states: "In its purest form, the answer under a ZDR agreement is: zero. The vendor processes your prompt and your data only long enough to generate a response. The moment the response is delivered, the data is discarded. Nothing is logged. Nothing is stored. Nothing is used for training."
- C) ❌ ZDR is about the vendor's retention of data, not customer deletion obligations.
- D) ❌ Anonymization-plus-indefinite-retention is the opposite of ZDR — the chapter explicitly says "nothing is stored."
- E) ❌ ZDR is described as a contractual term negotiated between vendor and customer, not a regulatory certification.

</details>

---

## Question 7

The chapter identifies four operational practices for "building inside the guardrails." Which of the following is NOT one of those four practices?

- A) Principle of least privilege
- B) Separation of test and production environments
- C) Audit trails for every consequential AI action
- D) Mandatory annual penetration testing of all AI vendors
- E) Human approval gate for high-stakes actions

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This IS one of the four practices. The chapter states: "Practice one: principle of least privilege. Give each AI tool — and each user of each AI tool — access only to the data and systems they actually need to do their work."
- B) ❌ This IS one of the four practices. The chapter states: "Practice two: separation of test and production environments."
- C) ❌ This IS one of the four practices. The chapter states: "Practice three: audit trails. Every consequential AI action in your business should be logged."
- ⭐ D) ✅ Mandatory annual penetration testing is NOT among the four operational practices the chapter identifies. The chapter focuses on least privilege, separated environments, audit trails, and human approval gates — not on adversarial testing.
- E) ❌ This IS one of the four practices. The chapter states: "Practice four: the human approval gate for high-stakes actions."

</details>

---

## Question 8

The chapter describes the "fifteen-minute briefing" as a cultural intervention. Which TWO statements correctly describe what the briefing covers and why it works?

- A) The briefing is a one-hour technical training session led by the security team
- B) The briefing covers five things including the approved tools list, what data is sensitive, the screenshot test, who to ask, and the incident-reporting process
- C) The briefing works because most employees, given clear rules, will follow them — but given unclear rules, they will improvise
- D) The briefing is intended only for executives and managers, not line employees
- E) The briefing has been shown in academic studies to fully eliminate all AI-related security incidents

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly describes the intervention as "fifteen minutes. One page" — not a one-hour technical training, and it is meant for every employee, not led narrowly by security.
- ⭐ B) ✅ The chapter lists exactly these five things: "Here are the approved tools... Here is what data is sensitive... Here is the screenshot test... Here is who to ask... Here is what happens if you are not sure and you do it anyway."
- ⭐ C) ✅ The chapter states: "Most employees, given clear rules, will follow them. Given unclear rules, they will improvise. Given no rules, they will use whatever tool helps them get their work done."
- D) ❌ The chapter explicitly says the briefing is "delivered to every employee" — not restricted to executives.
- E) ❌ The chapter does not claim the briefing eliminates all incidents — the Pearlman & Strauss example shows it shifts behavior and surfaces uncertainty earlier, not that it eliminates incidents.

</details>

---

## Question 9

What does the chapter call the long-run pattern where teams that invest in security move faster later, while teams that skip the work face larger costs later?

- A) The Innovator's Dilemma
- B) The Trust Compound
- C) The Security Singularity
- D) The Permissions Paradox
- E) The Guardrail Inversion

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The Innovator's Dilemma is a different concept (Clayton Christensen's framework for disruption); the chapter does not use this term.
- ⭐ B) ✅ The chapter's final section is titled "The Trust Compound" and states: "This is the trust compound. It looks like the technical-debt curve from software engineering, because it is the same curve. Pay early or pay much, much more later."
- C) ❌ The chapter does not use the term "Security Singularity."
- D) ❌ The chapter does not use the term "Permissions Paradox."
- E) ❌ The chapter does not use the term "Guardrail Inversion."

</details>

---

## Question 10

The case study at Halcyon Federal Credit Union describes a near-miss in lending operations. Which TWO statements correctly describe the nature of the failure as the chapter presents it?

- A) The lending team lead had acted in bad faith and deliberately exposed client data
- B) The pre-approved tools list focused on member services and marketing, and lending operations had been mentioned only in passing during the briefing
- C) The team lead reasoned that since the denial letters were her own writing (not member-facing data), the consumer tool was acceptable — a defensible interpretation that nonetheless exposed the firm
- D) The credit union's enterprise vendor had violated its ZDR contract
- E) The firm's CISO had disabled all security controls during the pilot to test employee judgment

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly states the team lead was "a sixteen-year Halcyon employee with an unblemished record" who "had acted in good faith" — the failure was structural, not malicious.
- ⭐ B) ✅ The case study states directly: "The pre-approved tools list had focused on member services and marketing; lending operations had been mentioned only in passing during the briefing."
- ⭐ C) ✅ The case study states: "the team lead had reasoned that since her work product (the denial letters) was not member-facing data but her own writing, the consumer tool was acceptable" — a "defensible interpretation" that nonetheless created exposure.
- D) ❌ The chapter does not describe any enterprise vendor ZDR violation — the issue was unauthorized use of a consumer-tier tool, not vendor non-compliance.
- E) ❌ The chapter does not describe any deliberate disabling of controls by the CISO; security controls remained in place but did not cover the specific scenario.

</details>

---

*Quiz for Chapter 14 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
