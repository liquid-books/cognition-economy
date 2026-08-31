# Case Study — Chapter 8: Plugins — Extending Your Workshop
*Florida Atlantic University — Graduate Course*

---

## Case Study: The Integration Crossroads at Brightline Capital Group

### Background

Brightline Capital Group is a mid-sized private equity and asset management firm headquartered in Atlanta, Georgia, with approximately 340 employees and roughly $4 billion in assets under management. The firm operates across three divisions — deal origination, portfolio management, and investor relations — each with distinct information workflows and tool ecosystems. Two years into the industry's AI transition, Brightline's Chief Operating Officer, Diana Forsythe, launched what she called the "Intelligent Workflow Initiative," a structured effort to embed AI into the firm's daily operations.

The initiative was not born from enthusiasm about technology. It was born from a specific bottleneck. Brightline's deal analysts were spending an estimated 90 minutes per day manually moving information between systems — pulling market data from Bloomberg terminals, copying deal pipeline updates from Salesforce, summarizing board memos from SharePoint, and pasting all of it into a shared document before weekly deal committee meetings. The process was tedious, error-prone, and deeply resistant to the firm's growing deal velocity. Forsythe hired a small internal AI task force — three analysts and an IT architect named Rafael Mendez — to evaluate options.

Mendez's team began by cataloging the firm's existing tool stack: Salesforce for CRM, Bloomberg for market data, SharePoint for document management, Slack for internal communication, and a proprietary portfolio analytics platform built in-house seven years earlier. The question was not whether to extend their AI capabilities. The firm's primary AI assistant — a frontier vendor's desktop application — had already been provisioned firm-wide for six months, and a second assistant was available through the firm's productivity-suite contract. The question was *how* — through plugin installation, self-configured connections, or custom-built skill definitions — and with what level of control.

What complicated the decision was Brightline's regulatory environment. As a registered investment adviser, the firm operated under SEC oversight, with strict obligations around data governance, access controls, and audit trails. Any AI integration that touched client data, portfolio positions, or deal flow records had to satisfy the firm's compliance team, led by Chief Compliance Officer Sylvia Park. Park had a single, non-negotiable requirement: any AI integration with client-facing or deal-sensitive data must produce a log of every query and every response, accessible to her team on demand. Convenience was not her concern. Accountability was.

### The Situation

Mendez's team identified three viable paths. The first was to install available marketplace plugins — Salesforce, workspace, and Slack connectors were all available in the assistant's plugin marketplace — and accept the convenience they offered at the cost of reduced visibility into what permissions those plugins held and how queries were logged. The second path was to build self-configured connections directly to each tool, which would give the firm full configuration control, detailed logging capabilities, and the ability to scope permissions precisely — but required two to three weeks of setup per integration and ongoing maintenance. The third path was hybrid: install plugins for low-sensitivity workflows (web search, general research), build controlled connections for anything touching deal or client data, and use skills to codify the analytical processes the deal team ran repeatedly, so that AI behavior was consistent and auditable regardless of which data source it drew from.

The tension Forsythe and Mendez faced was not simply technical. It was organizational. The deal analysts wanted speed — they had been promised a tool that would reduce their 90-minute daily overhead, and they were watching that promise recede with every week of planning. The compliance team wanted control. The IT team wanted a solution they could maintain. And Forsythe wanted a decision that the firm could grow into rather than one it would have to undo in eighteen months. The three paths each optimized for a different stakeholder's priorities, and no path satisfied all of them simultaneously. Choosing among them required a framework — not just for this decision, but for how Brightline would make AI integration decisions going forward, as the marketplace matured and new options continued to emerge.

### Discussion Prompt

Using the control-versus-convenience spectrum developed in this chapter — pre-built connections at one end, self-configured connections at the other, and skills as the process layer that runs on either — evaluate Brightline's three integration paths against the competing organizational constraints the firm faces. Which position on the spectrum best fits Brightline's regulatory obligations, and how does the concept of permission management as governance (rather than as a technical configuration step) change the strategic calculus? What signals in this case suggest where Brightline sits on the organizational maturity curve for AI adoption, and how should those signals influence the sequencing of their integration decisions?

---

### Discussion Guidelines

**Initial Post** (due before class)
- Minimum **400 words**
- Directly address the discussion prompt using concepts from this chapter
- Include **at least one APA-formatted citation** — from the course text or a peer-reviewed source
- Avoid summary; demonstrate analysis and original thinking

**Peer Responses** (minimum 2)
- Minimum **250 words each**
- Each response must include **at least one APA-formatted citation**
- Engage substantively — build on, challenge, or offer a contrasting perspective grounded in evidence
- "I agree" or "Great post" responses do not meet the requirement
- Maintain a professional and respectful academic tone

---

