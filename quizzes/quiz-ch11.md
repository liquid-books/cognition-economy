# Quiz: Chapter 11 — The Agent SDK: When to Build vs. When to Use

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

The chapter opens with Helena Vasquez, COO of a regional insurance carrier, evaluating three proposals to automate claims pre-screening. What is the central argument the chapter makes about how she should approach this decision?

- A) She should always pick the cheapest option to maximize ROI on her first AI deployment
- B) She should pick the most polished vendor demo because vendor maturity reduces implementation risk
- C) She should match the option to the actual shape of the problem — using a four-question framework rather than the demo quality
- D) She should default to building custom because vendor dependencies are always a strategic risk
- E) She should outsource the decision to her engineering team because the choice is fundamentally technical

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly warns against picking by price — the $30,000 no-code option might be right, but only if it fits the four-question framework, not because it is cheap.
- B) ❌ The chapter specifically calls the polished vendor demo "a distraction" in Helena's case — polish does not equal fit.
- ⭐ C) ✅ The chapter states: "This is the work of leadership in the agent era — not picking the most impressive demo, but matching the option to the actual shape of your problem." The four-question framework (customer-facing? sensitive data? strategic? unique?) is the explicit method.
- D) ❌ The chapter argues for a portfolio approach across all four options — defaulting to "build" is treated as a common but expensive mistake.
- E) ❌ The chapter is explicit that this is a business decision, not a technical one, and that delegating it to engineering produces poor outcomes.

</details>

---

## Question 2

The chapter uses the "McDonald's Move" as its central analogy for the Agent SDK. Which TWO statements correctly describe how the analogy maps to Anthropic's product strategy?

- A) Claude Code is the hamburger; the Agent SDK is the kitchen system that produces hamburgers at scale
- B) McDonald's sells franchisees the system for making hamburgers, not the hamburger itself — and the Agent SDK is Anthropic doing the same thing with AI agents
- C) The Agent SDK is a single licensed AI model, while Claude Code is the franchise relationship
- D) The McDonald's analogy is offered as a cautionary tale — companies that try to replicate the SDK approach fail
- E) The McDonald's analogy applies only to consumer-facing AI products, not enterprise deployments

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Claude Code is the *kitchen* that produces Claude Code. It is the engine." (And explicitly: "Claude Code is what you *use*. The Agent SDK is what you *deploy*.") The hamburger/kitchen mapping is the central image.
- ⭐ B) ✅ The chapter states: "Anthropic, in 2024, made the McDonald's move with AI" — describing how the SDK packages the same system Anthropic built for itself so any company can build their own products on top of it.
- C) ❌ The chapter does not describe the SDK as a "licensed AI model" — it explicitly describes it as "the engine — the agent loop, the tool orchestration, the context management, the permission system."
- D) ❌ The analogy is offered as a positive strategic insight, not a warning. The chapter explicitly endorses the McDonald's move as the right framing.
- E) ❌ The chapter applies the analogy broadly across consumer and enterprise deployments — no such restriction is made.

</details>

---

## Question 3

According to the chapter's four-question build-vs-buy framework, what should a leader ask before approving any SDK project?

- A) What is the projected ROI, what is the payback period, what is the IRR, and what is the NPV?
- B) Which vendor has the largest market share, the best brand, and the most case studies?
- C) Is the workflow customer-facing or internal; does it touch sensitive data; is it a one-time problem or a strategic capability; and how unique is the workflow?
- D) Which AI model is best, which cloud provider is cheapest, which language should engineers use, and how many tokens will it consume?
- E) Who is the executive sponsor, who is the budget owner, who is the technical lead, and who is the compliance signoff?

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Financial metrics matter, but they are not the chapter's framework — the chapter argues the more important question is fit, not return.
- B) ❌ The chapter explicitly criticizes vendor-selection-by-brand as the "polished demo distraction" trap.
- ⭐ C) ✅ The chapter lists these four questions verbatim in the Build-Vs-Buy Checklist admonition: customer-facing or internal, sensitive data, one-time vs. strategic, and uniqueness.
- D) ❌ These are implementation questions for engineers, not strategic framing questions for leaders — the chapter explicitly separates these layers.
- E) ❌ Governance roles matter but are not the chapter's decision framework — the framework is about matching option to problem, not assigning ownership.

</details>

---

## Question 4

The chapter identifies four components the Agent SDK provides "for free" to engineers building agents. Which of the following is NOT one of those four components?

- A) Built-in tools (reading files, searching the web, running queries)
- B) The agent loop (the read-decide-act-evaluate cycle)
- C) Context management (deciding what to remember, summarize, or discard)
- D) Pre-trained industry-specific models (insurance, healthcare, legal, finance)
- E) Permissions and auditability (controlling which tools the agent can use)

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This IS one of the four — the chapter states: "The built-in tools. The SDK comes with a standard set of capabilities every agent gets for free."
- B) ❌ This IS one of the four — the chapter explicitly describes the agent loop as "the thinking part."
- C) ❌ This IS one of the four — the chapter describes context management as handling "what to remember, what to summarize, what to discard."
- ⭐ D) ✅ The chapter does NOT list industry-specific pre-trained models among the SDK's components. The SDK is model-agnostic infrastructure — the four components are tools, loop, context, and permissions/auditability. Pre-trained vertical models are a separate product category.
- E) ❌ This IS one of the four — the chapter calls it "the part that matters most for business deployments and the part vendors talk about least."

</details>

---

## Question 5

The chapter describes a five-section structure for a useful SDK project brief. Which TWO of the following sections are part of that structure?

- A) The outcome — what success looks like in human terms, not technical terms
- B) The technical stack — which programming language, framework, and cloud provider will be used
- C) The constraints — regulatory rules, data residency limits, and required human approval points
- D) The vendor comparison matrix — a side-by-side analysis of all available SDK alternatives
- E) The marketing plan — how the agent will be announced internally and to customers

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter lists "the outcome" as Section One: "What does success look like in human terms? Not 'build an AI claims pre-screener.'"
- B) ❌ Technical stack decisions belong to engineering, not the business brief — the chapter explicitly warns against over-briefing with implementation details.
- ⭐ C) ✅ The chapter lists "the constraints" as Section Four: "What regulatory rules apply? What data must never leave certain systems? What decisions must require human approval before they go live?"
- D) ❌ A vendor comparison matrix is a buying-process artifact, not a project brief — the chapter does not include it among the five sections.
- E) ❌ A marketing plan is not part of the SDK brief structure as described in the chapter.

</details>

---

## Question 6

The chapter lists several "red flags" to watch for in early engineering conversations about an SDK project. Which phrase is identified as a red flag and what does it actually mean?

- A) "We'll figure out the data model as we go" — translation: we have not thought about your data
- B) "We will use the latest model version" — translation: we are technically savvy and current
- C) "We'll deploy on AWS" — translation: we have made cloud architecture decisions already
- D) "We'll write unit tests for the agent" — translation: we are following engineering best practices
- E) "We'll use TypeScript instead of Python" — translation: we have language expertise in-house

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter lists this exact phrase as a red flag with this exact translation: "'We'll figure out the data model as we go.' (Translation: we have not thought about your data.)"
- B) ❌ This is not listed as a red flag — model currency is a legitimate engineering decision.
- C) ❌ This is not listed as a red flag — cloud choice is a normal architectural decision, not a warning sign.
- D) ❌ This is not listed as a red flag — testing is a legitimate engineering practice, not a warning sign.
- E) ❌ This is not listed as a red flag — language choice is an engineering preference, not a warning sign. The chapter's red flags are about scope, audit logging, permissions, and motivation — not implementation language.

</details>

---

## Question 7

The chapter argues that no-code platforms (Zapier, Make, Lindy, Relevance AI) deserve serious consideration alongside vendor solutions and custom SDK builds. Which TWO statements correctly capture the chapter's argument?

- A) No-code platforms wrap the same fundamental SDK capabilities (agent loop, built-in tools, context, permissions) in a visual interface
- B) No-code platforms can deliver 80% of what a custom SDK build does, at a fraction of the cost and timeline
- C) No-code platforms are only suitable for personal productivity tasks, not business workflows
- D) No-code platforms always require an engineering team to deploy, defeating their purpose
- E) No-code platforms exist only on the Anthropic ecosystem and cannot integrate with other AI providers

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "What these platforms have in common: they wrap the same fundamental capabilities the SDK provides — the agent loop, the built-in tools, the context management, the permissions — into a visual experience."
- ⭐ B) ✅ The chapter states: "A no-code platform might let you build 80% of what a custom SDK build could do" and recommends "Track 1 — No-code first" as the default starting point.
- C) ❌ The chapter explicitly recommends no-code for business workflows: "claims pre-screening, lead enrichment, support ticket triage, vendor invoice review."
- D) ❌ The whole point of no-code is that it does not require engineering — the chapter says someone in operations can build with "two hours of training instead of four months of engineering."
- E) ❌ The chapter cites multiple no-code platforms across different ecosystems (Zapier, Make, Lindy, Relevance AI) — they are not tied to any single AI provider.

</details>

---

## Question 8

The chapter argues that vendor-built AI solutions are often a weak fit for problems with high regulatory and customization needs. Applied to Helena Vasquez's case at Cypress Coastal Insurance, why does the chapter call the $400,000 vendor proposal "actually the *weakest* fit"?

- A) Because the vendor proposal was the most expensive — and cost is the primary factor in any AI decision
- B) Because the vendor's demo was less polished than the no-code alternative
- C) Because the vendor solution requires Helena's data to leave her firewall, has limited customization for her firm's specific policy language, and has the highest cost — even though the demo was the most polished
- D) Because vendors are categorically untrustworthy and should be avoided in regulated industries
- E) Because the vendor proposal did not include AI capabilities, only traditional automation

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter does not argue that price is the primary factor — fit is. The vendor's price is a symptom of misfit, not the cause.
- B) ❌ The chapter explicitly notes the vendor demo was more polished than the no-code platform's demo, not less.
- ⭐ C) ✅ The chapter states: "Her data leaves the building. Her customizations are limited. Her costs are highest. The shiny demo was a distraction." This is the explicit rationale for calling the vendor proposal the weakest fit.
- D) ❌ The chapter is not categorically anti-vendor — it explicitly endorses vendor solutions when the problem is common and the workflow is non-strategic.
- E) ❌ The vendor proposal did include AI capabilities — the issue was fit, not capability.

</details>

---

## Question 9

The chapter teaches a "skim the docs" method for business leaders reading technical documentation like the Agent SDK overview. Which of the following best describes the method?

- A) Read every code block carefully and ignore the prose, since the code contains the actual capabilities
- B) Forward the documentation to engineering immediately and wait for their summary
- C) Read the first paragraph fully, read every section header, read every comparison table, skip code blocks, and read the licensing and branding sections — total time around 15 minutes
- D) Read only the marketing summary on the homepage and skip the documentation entirely
- E) Read the documentation cover to cover until you understand the code examples

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly says: "Skip every code block." The code is for engineers; the strategic information is in the prose.
- B) ❌ The chapter explicitly criticizes this approach: "slow and lossy."
- ⭐ C) ✅ The chapter's Skim Checklist lists exactly these steps in order: "Read the first paragraph in full. Read every section header. Read every comparison table. Read every paragraph that does not have code in it. Skip every code block. Read the license, branding, and pricing sections. Total time investment: 15 minutes."
- D) ❌ The chapter argues for reading the actual documentation, not marketing materials, to be "conversant" with engineers.
- E) ❌ The chapter argues you do not need to understand code examples — the point is to skim for strategic information, not master implementation.

</details>

---

## Question 10

The chapter recommends a "two-track strategy" for organizations deciding when to use no-code vs. SDK builds. Which TWO statements correctly describe this strategy?

- A) Every internal automation idea should be prototyped on a no-code platform first; if it works there, ship it there
- B) The SDK should be used only when no-code hits a hard wall — usually for customer-facing, deeply integrated, or strategically differentiated workflows
- C) Companies should always start with the SDK to ensure maximum capability from day one
- D) No-code and SDK should never be used in the same organization — pick one and standardize
- E) The two-track strategy applies only to startups; large enterprises should always use SDK builds

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Track 1 — No-code first. Every internal automation idea gets prototyped on a no-code platform first. If it works there, you ship it there."
- ⭐ B) ✅ The chapter states: "Track 2 — SDK only when no-code hits a wall. A small number of workflows — usually customer-facing, deeply integrated, or strategically differentiated — outgrow what no-code can support."
- C) ❌ The chapter explicitly warns: "Companies that start with the SDK and discover later that no-code could have done it have wasted six months and a great deal of money."
- D) ❌ The chapter advocates running both tracks in parallel — the two-track strategy is the opposite of pick-one-and-standardize.
- E) ❌ The chapter does not restrict the strategy by company size — it applies universally to any organization making these decisions.

</details>

---

*Quiz for Chapter 11 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
