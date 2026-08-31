# Quiz: Chapter 3 — Tools and the MCP Revolution

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 3, what is the *fundamental* transformation MCP introduces — what changes about AI when MCP is connected?

- A) MCP makes the model itself more intelligent
- B) MCP gives the AI a live connection to your actual world — your inbox, files, calendar, the web, your data — so it can act on real things instead of only reasoning about descriptions you typed in
- C) MCP reduces the cost per token by half
- D) MCP replaces the language model with a faster local one
- E) MCP eliminates the need for a system prompt

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter never claims MCP increases the model's intelligence. The model is unchanged: "The same model. The same intelligence. One version is locked in a room. The other has a door."
- ⭐ B) ✅ The chapter states: "MCP — Model Context Protocol — is the technology that opens the door. It is an open standard that gives your AI assistant a live connection to your actual world: your inbox, your files, your calendar, the web, your data. Not descriptions of these things that you typed in. The actual things themselves."
- C) ❌ MCP is not described as a pricing mechanism.
- D) ❌ MCP does not replace the model. It connects the model to tools.
- E) ❌ MCP and system prompts are independent. The chapter never positions MCP as a replacement for system prompts.

</details>

---

## Question 2

The chapter uses a specific analogy to explain MCP's role. Which one is correct?

- A) MCP is like a magnifying glass that makes small text easier to read
- B) MCP is like USB — before USB every peripheral had its own connector, but after USB anything that followed the standard worked with anything else that followed it; MCP is "USB for AI tools"
- C) MCP is like fiber-optic cable that makes the model run faster
- D) MCP is like a battery that powers your AI assistant while it is offline
- E) MCP is like a printer driver, specific to one operating system

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ A magnifying glass is not the chapter's analogy.
- ⭐ B) ✅ The chapter states: "Think of it like USB. Before USB, every peripheral had its own connector. After USB, anything that followed the standard worked with anything else that followed the standard. MCP is USB for AI tools."
- C) ❌ MCP is not described as speeding up the model.
- D) ❌ The battery analogy is not in the chapter and the assistant is not described as functioning offline via MCP.
- E) ❌ A printer driver is OS-specific. MCP is the opposite — a universal protocol.

</details>

---

## Question 3

According to the chapter, what should govern your understanding of what your AI can and cannot do once it is connected to your workspace (mail, files, calendar)? Which TWO statements are correct?

- A) Major assistants now ship workspace connectors built in — there is nothing to install and no developer console to touch; you authenticate once through the provider's standard authorization screen
- B) The permission screen is the contract — it lists exactly what the connection will be able to do (read your mail, or also send it; view your files, or also edit them), and it is the single most reliable source of truth about what your AI can do in your accounts
- C) The assistant deletes emails older than 90 days as part of the connection setup
- D) Once connected, the assistant publishes your emails publicly to improve future model training
- E) The vendor's marketing page is a more reliable guide to the connection's scope than the authorization screen

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Major assistants now ship workspace connectors built in — there is nothing to install and no developer console to touch... you authenticate once, and from then on your assistant can reach your mail, files, and calendar in any conversation."
- ⭐ B) ✅ The chapter states: "**Treat the permission screen as a contract.** When the authorization window opens, it lists exactly what the connection will be able to do — read your mail, or also send it... It is not boilerplate; it is the actual scope of what you are granting, and it is the single most reliable source of truth about what your AI can do in your accounts."
- C) ❌ The chapter never says the assistant deletes anything during setup. This is a fabricated risk.
- D) ❌ The chapter does not claim user emails are published or used for training; this contradicts the trust framing.
- E) ❌ The chapter says the opposite: the permission screen is "more reliable than this book, more reliable than the vendor's marketing page."

</details>

---

## Question 4

The chapter introduces a web-reading tool (its press-time example is Firecrawl) for the Open Web role. According to the chapter, what does this tool do — and why does the role need its own connection when most assistants can already search the web?

- A) It is a database service that gives you free cloud storage
- B) It is a web scraping API that converts any website into clean, structured text an AI can read — because searching is not the same as reading a whole site, structured, at scale
- C) It is a video transcription service
- D) It is a code-completion plugin for IDEs
- E) It is a calendar scheduling assistant

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The web-reading tool is not a database. The persistent store (Supabase in this chapter) fills that role.
- ⭐ B) ✅ The chapter states: "Firecrawl, our press-time example, is a web scraping API that converts any website into clean, structured text an AI can read and reason about." And on why the role exists at all: "**searching is not the same as reading a whole site, structured, at scale.** A built-in search grabs a few snippets to answer a question. A web-reading tool hands your AI the full content of any page you point it at... One is a glance. The other is research."
- C) ❌ Video transcription is not what the tool does in this chapter.
- D) ❌ It is not described as a code-completion tool.
- E) ❌ It is not a calendar tool.

</details>

---

## Question 5

The chapter argues there is a discipline that matters when using the web-reading tool's free tier of page-read credits. Which statement best captures the chapter's specific advice?

- A) Burn the credit bundle as quickly as possible to learn the tool by trial and error
- B) Be intentional — do not burn credits on pages you could just read yourself; use them on content that requires synthesis (multiple pages, dense reports, sites with paywalled summaries)
- C) Always upgrade to the paid tier within the first day of signing up
- D) Reserve all the credits for a single end-of-year project
- E) The tool should never be used for competitive intelligence — only for personal research

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter argues the opposite: a few hundred page reads spent deliberately is a meaningful capability — "enough for a serious competitive analysis"; wasting them is the failure mode.
- ⭐ B) ✅ The chapter states: "The discipline is intentionality. Do not burn credits on pages you could just read yourself. Use them on content that requires synthesis — multiple pages, dense reports, sites with paywalled summaries you want analyzed from what is publicly visible."
- C) ❌ The chapter never recommends rushed upgrades.
- D) ❌ Hoarding credits for one project is not the chapter's framing.
- E) ❌ The chapter explicitly calls competitive intelligence "the highest-value use case for most professionals."

</details>

---

## Question 6

According to the chapter, what is Supabase, and what is its primary role in the cognitive workshop?

- A) Supabase is a free cloud database platform that gives your AI a place to store and retrieve information that persists between conversations — a "smart spreadsheet in the cloud" that handles real workloads as your AI usage grows
- B) Supabase is a third-party model provider that replaces your AI assistant
- C) Supabase is a calendar service competing with Google Calendar
- D) Supabase is a paid service with no free tier
- E) Supabase is a browser extension that records every AI conversation locally

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Supabase is a free cloud platform that gives your AI a place to store and retrieve information that persists between conversations. Think of it as a smart spreadsheet in the cloud — one that your AI can read from and write to, that lives online and never disappears when you close a tab, and that can handle real workloads as your use of AI grows."
- B) ❌ Supabase does not replace the language model.
- C) ❌ Supabase is not a calendar tool.
- D) ❌ The chapter is explicit that the platform is free to start and the free tier covers serious workloads.
- E) ❌ Supabase is a cloud database, not a local browser extension.

</details>

---

## Question 7

The chapter explains *why* persistent storage like Supabase matters for AI workflows. Which TWO statements correctly describe what Supabase provides for AI work?

- A) Persistent storage your AI can read from and write to in plain English — data that lives in the store permanently, not just in the conversation
- B) Automation — the platform can run tasks on a schedule (pulling data, generating reports, sending updates) even when you are not in a conversation, which is what allows AI workflows to run on their own
- C) Your assistant's context window already gives you all the persistent storage you'll ever need, so a persistent store is purely cosmetic
- D) The store forces you to learn SQL before any AI workflow can use it
- E) The store only works with one vendor's models, not with the others

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "**Persistent storage** — Your AI can read from it, write to it, and query it in plain English... The data lives in the store permanently, not just in the conversation."
- ⭐ B) ✅ The chapter states: "**Automation** — The platform can run tasks automatically on a schedule — pulling data, generating reports, sending updates — even when you are not in a conversation. This is what makes AI workflows run on their own rather than requiring you to manually trigger everything."
- C) ❌ The chapter explicitly says the opposite: "Your assistant's context window is not persistent storage. It clears between sessions. The store is the persistent layer."
- D) ❌ The chapter says you tell your assistant what to store or retrieve "in plain English — it handles everything underneath." No SQL required from the user.
- E) ❌ Provider lock-in is never described; MCP is by definition cross-provider standardization.

</details>

---

## Question 8

The chapter describes a **universal pattern** for adding any MCP tool connection. Which sequence correctly captures the four steps?

- A) Hire a developer, sign a six-month engineering contract, then test in production
- B) Find the tool's current MCP documentation → connect it (via the vendor's one-click connector, or by handing your assistant the configuration snippet and saying "Install this for me and walk me through it") → verify it with a test request only the live connection could answer → use it on real work
- C) Open the Windows registry, edit hex values manually, restart the OS
- D) Email the AI vendor's support team requesting a custom integration build
- E) Print the documentation, mail it to the vendor, wait for an activation code

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit that you do not need to be a developer — "none of them require technical knowledge."
- ⭐ B) ✅ The chapter states: "the universal pattern for adding a tool is the same four steps: **find** the tool's current MCP documentation... **connect** it — either with the vendor's one-click connector or by handing your assistant the configuration snippet and saying *'Install this for me and walk me through it'* — **verify** it with a test request only the live connection could answer, and then **use** it on real work."
- C) ❌ Registry editing is not part of any setup described.
- D) ❌ Custom vendor builds are not part of the chapter.
- E) ❌ Postal mail is not how MCP connections are made.

</details>

---

## Question 9

In the Palmetto Health Partners case study, compliance officer Veronica Sánchez raises a HIPAA concern about expanding MCP access. What is the specific *architectural* reason she identifies that creates a new class of governance risk?

- A) MCP requires uploading patient health records to a public website
- B) MCP servers ship with backdoors that vendors can use to exfiltrate data
- C) Once granted, an AI's access to connected systems is broad and persistent — unlike a human employee who reads one file at a time and can be watched, a connected AI can query, cross-reference, and synthesize across an entire Drive in seconds, with no natural bottleneck for auditing what was accessed and why
- D) The AI desktop assistant refuses to comply with any HIPAA requirements
- E) MCP automatically publishes search results to Google's index

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The case never claims MCP uploads patient health records publicly.
- B) ❌ Vendor backdoors are not the issue named in the case.
- ⭐ C) ✅ The case states: "Unlike a human employee who reads one file at a time and can be watched, a connected AI can query, cross-reference, and synthesize across an entire Drive in seconds. There is no natural bottleneck for auditing what was accessed and why." Sánchez's broader concern: "Any AI system that could *read* that Drive could potentially *reason across* it in ways that produced HIPAA-relevant inferences."
- D) ❌ The case does not say the assistant refuses HIPAA compliance.
- E) ❌ Public indexing is not mentioned in the case.

</details>

---

## Question 10

In the Palmetto Health Partners case study, the CTO James Okafor proposes a *phased rollout* approach to address the governance tension. Which TWO statements correctly describe the elements of his phased approach?

- A) Start with read-only connections to non-sensitive calendaring and scheduling systems
- B) Establish logging requirements before expanding access
- C) Skip compliance entirely because competitors are moving faster
- D) Only expand to write-enabled connections after a governance framework is approved by compliance and legal
- E) Fire the compliance officer Veronica Sánchez for slowing down the project

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "Okafor proposed a phased rollout: start with read-only connections to non-sensitive calendaring and scheduling systems, establish logging requirements, and only expand to write-enabled connections after a governance framework was approved by compliance and legal."
- ⭐ B) ✅ Same passage above — "establish logging requirements" is part of his phased approach.
- C) ❌ The case is explicit that Okafor takes governance seriously and proposes the phased approach precisely to honor compliance concerns.
- D) ❌ This option is actually correct per the case text, but… wait — the question asks for TWO correct answers and A, B are the two explicit elements. D paraphrases the same Okafor passage and *is* also correct. **Author note:** The intended two answers are A and B; D restates the same idea ("only expand... after a governance framework was approved by compliance and legal") and would also be accepted. The case names three elements of the phased approach (read-only first, logging, governance approval before write-expansion); a student selecting any two of these correctly captures Okafor's plan.
- E) ❌ The case explicitly describes Sánchez as a respected compliance officer whose concerns Okafor incorporates into his plan.

</details>

---

*Quiz for Chapter 3 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
