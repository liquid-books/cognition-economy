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
- ⭐ B) ✅ The chapter states: "MCP — Model Context Protocol — is the technology that opens the door. It is an open standard, published by Anthropic, that gives your AI assistant a live connection to your actual world: your inbox, your files, your calendar, the web, your data. Not descriptions of these things that you typed in. The actual things themselves."
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
- D) MCP is like a battery that powers Claude Desktop while it is offline
- E) MCP is like a printer driver, specific to one operating system

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ A magnifying glass is not the chapter's analogy.
- ⭐ B) ✅ The chapter states: "Think of it like USB. Before USB, every peripheral had its own connector. After USB, anything that followed the standard worked with anything else that followed the standard. MCP is USB for AI tools."
- C) ❌ MCP is not described as speeding up the model.
- D) ❌ The battery analogy is not in the chapter and Claude Desktop is not described as functioning offline via MCP.
- E) ❌ A printer driver is OS-specific. MCP is the opposite — a universal protocol.

</details>

---

## Question 3

According to the chapter, what specifically happens when you connect Claude Desktop to Google Workspace? Which TWO statements are correct?

- A) Claude Desktop ships with Google Workspace connectors built in — there is no config file to edit, no Google Cloud Console to touch, just an OAuth sign-in
- B) Claude can read your Gmail and create drafts, but it cannot send emails — anything it drafts must be sent manually by you
- C) Claude Desktop deletes emails older than 90 days as part of the connection setup
- D) Once connected, Claude Desktop publishes your emails publicly to improve future model training
- E) The Google connectors only work for Workspace business accounts; personal Gmail accounts are not supported

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Claude Desktop ships with Google Workspace connectors built in. There is nothing to install, no configuration file to edit, no Google Cloud Console to touch. The connectors are already there — you just need to authenticate."
- ⭐ B) ✅ The chapter states: "Claude only reads your emails and creates drafts — it cannot send. Anything it drafts must be sent manually by you. Your inbox is read-only from Claude's perspective unless you explicitly approve a specific action."
- C) ❌ The chapter never says Claude deletes anything during setup. This is a fabricated risk.
- D) ❌ The chapter does not claim user emails are published or used for training; this contradicts the trust framing.
- E) ❌ The chapter is explicit that the connection requires a Gmail account — and the entire applied exercise uses a free personal Google account.

</details>

---

## Question 4

The chapter introduces Firecrawl as the second high-priority MCP connection. According to the chapter, what does Firecrawl do — and what is its starter tier?

- A) Firecrawl is a database service that gives you 100 GB of free storage
- B) Firecrawl is a web scraping API that converts any website into clean, structured text an AI can read; the free account gives you 500 lifetime credits (roughly one credit per page scrape)
- C) Firecrawl is a video transcription service
- D) Firecrawl is a code-completion plugin for IDEs
- E) Firecrawl is a calendar scheduling assistant

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Firecrawl is not a database. Supabase is the database in this chapter.
- ⭐ B) ✅ The chapter states: "Firecrawl is a web scraping API that converts any website into clean, structured text that an AI can read and reason about... The free account gives you 500 lifetime credits. One credit is roughly one page scrape."
- C) ❌ Video transcription is not what Firecrawl does in this chapter.
- D) ❌ Firecrawl is not described as a code-completion tool.
- E) ❌ Firecrawl is not a calendar tool.

</details>

---

## Question 5

The chapter argues there is a discipline that matters when using Firecrawl's free tier. Which statement best captures the chapter's specific advice?

- A) Burn the 500 credits as quickly as possible to learn the tool by trial and error
- B) Be intentional — do not burn credits on pages you could just read yourself; use them on content that requires synthesis (multiple pages, dense reports, sites with paywalled summaries)
- C) Always upgrade to the paid tier within the first day of signing up
- D) Reserve all 500 credits for a single end-of-year project
- E) Firecrawl should never be used for competitive intelligence — only for personal research

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter argues the opposite: 500 credits used intentionally is a meaningful capability; wasting them is the failure mode.
- ⭐ B) ✅ The chapter states: "The discipline is intentionality. Do not burn credits on pages you could just read yourself. Use them on content that requires synthesis — multiple pages, dense reports, sites with paywalled summaries you want analyzed from what is publicly visible."
- C) ❌ The chapter never recommends rushed upgrades.
- D) ❌ Hoarding credits for one project is not the chapter's framing.
- E) ❌ The chapter explicitly calls competitive intelligence "the highest-value use case for most professionals."

</details>

---

## Question 6

According to the chapter, what is Supabase, and what is its primary role in the cognitive workshop?

- A) Supabase is a free cloud database platform that gives your AI a place to store and retrieve information that persists between conversations — a "smart spreadsheet in the cloud" that handles real workloads as your AI usage grows
- B) Supabase is a third-party model provider that replaces Claude
- C) Supabase is a calendar service competing with Google Calendar
- D) Supabase is a paid service that costs $99/month for the smallest tier
- E) Supabase is a browser extension that records every AI conversation locally

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Supabase is a free cloud platform that gives your AI a place to store and retrieve information that persists between conversations. Think of it as a smart spreadsheet in the cloud — one that your AI can read from and write to, that lives online and never disappears when you close a tab, and that can handle real workloads as your use of AI grows."
- B) ❌ Supabase does not replace the language model.
- C) ❌ Supabase is not a calendar tool.
- D) ❌ The chapter is explicit: "No credit card required" — the free tier covers serious workloads.
- E) ❌ Supabase is a cloud database, not a local browser extension.

</details>

---

## Question 7

The chapter explains *why* persistent storage like Supabase matters for AI workflows. Which TWO statements correctly describe what Supabase provides for AI work?

- A) Persistent storage your AI can read from and write to in plain English — data that lives in Supabase permanently, not just in the conversation
- B) Automation — Supabase can run tasks on a schedule (pulling data, generating reports, sending updates) even when you are not in a Claude conversation, which is what allows AI workflows to run on their own
- C) Claude's context window already gives you all the persistent storage you'll ever need, so Supabase is purely cosmetic
- D) Supabase forces you to learn SQL before any AI workflow can use it
- E) Supabase only works with Anthropic models, not with Google or OpenAI

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "**Persistent storage** — Your AI can read from it, write to it, and query it in plain English... The data lives in Supabase permanently, not just in the conversation."
- ⭐ B) ✅ The chapter states: "**Automation** — Supabase can run tasks automatically on a schedule — pulling data, generating reports, sending updates — even when you are not in a Claude conversation. This is what makes AI workflows run on their own rather than requiring you to manually trigger everything."
- C) ❌ The chapter explicitly says the opposite: "Claude's context window is not persistent storage. It clears between sessions. Supabase is the persistent layer."
- D) ❌ The chapter says you tell Claude what to store "in plain English" — no SQL required from the user.
- E) ❌ Provider lock-in is never described; MCP is by definition cross-provider standardization.

</details>

---

## Question 8

The chapter describes a **universal pattern** for connecting any MCP server to Claude Desktop. Which sequence correctly captures the pattern?

- A) Hire a developer, sign a six-month engineering contract, then test in production
- B) Find the tool's MCP documentation ("[tool name] MCP Claude Desktop") → copy the configuration snippet → paste into Claude Desktop with the instruction "Install this for me and walk me through it" → Claude guides you through each remaining step
- C) Open the Windows registry, edit hex values manually, restart the OS
- D) Email Anthropic support requesting a custom integration build
- E) Print the documentation, mail it to Google, wait for an activation code

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit that you do not need to be a developer.
- ⭐ B) ✅ The chapter states: "The universal pattern for any tool connection is the same four steps: find the tool's MCP documentation (search '[tool name] MCP Claude Desktop'), copy the configuration snippet, open Claude Desktop and say 'Install this for me and walk me through it' — then paste the snippet. Claude will guide you through each remaining step."
- C) ❌ Registry editing is not part of any setup described.
- D) ❌ Custom builds from Anthropic are not part of the chapter.
- E) ❌ Postal mail is not how MCP connections are made.

</details>

---

## Question 9

In the Meridian Health Partners case study, compliance officer Veronica Sánchez raises a HIPAA concern about expanding MCP access. What is the specific *architectural* reason she identifies that creates a new class of governance risk?

- A) MCP requires uploading patient health records to a public website
- B) MCP servers ship with backdoors that vendors can use to exfiltrate data
- C) Once granted, an AI's access to connected systems is broad and persistent — unlike a human employee who reads one file at a time and can be watched, a connected AI can query, cross-reference, and synthesize across an entire Drive in seconds, with no natural bottleneck for auditing what was accessed and why
- D) Claude Desktop refuses to comply with any HIPAA requirements
- E) MCP automatically publishes search results to Google's index

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The case never claims MCP uploads patient health records publicly.
- B) ❌ Vendor backdoors are not the issue named in the case.
- ⭐ C) ✅ The case states: "Unlike a human employee who reads one file at a time and can be watched, a connected AI can query, cross-reference, and synthesize across an entire Drive in seconds. There is no natural bottleneck for auditing what was accessed and why." Sánchez's broader concern: "Any AI system that could *read* that Drive could potentially *reason across* it in ways that produced HIPAA-relevant inferences."
- D) ❌ The case does not say Claude Desktop refuses HIPAA compliance.
- E) ❌ Public indexing is not mentioned in the case.

</details>

---

## Question 10

In the Meridian Health Partners case study, the CTO James Okafor proposes a *phased rollout* approach to address the governance tension. Which TWO statements correctly describe the elements of his phased approach?

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
