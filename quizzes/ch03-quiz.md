# Chapter 3 Quiz: Tools and the MCP Revolution
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** Model Context Protocol (MCP) is best described as:

&nbsp;&nbsp;&nbsp;&nbsp;A. A proprietary Claude feature that allows the model to browse the internet automatically  
&nbsp;&nbsp;&nbsp;&nbsp;B. An open standard that defines how AI assistants connect to external tools, data sources, and live systems  
&nbsp;&nbsp;&nbsp;&nbsp;C. A cloud database that stores conversation history between AI sessions  
&nbsp;&nbsp;&nbsp;&nbsp;D. An API authentication layer that replaces OAuth for enterprise applications  

---

**2.** Before MCP existed, integrating an AI assistant with an external tool such as a CRM or email system required:

&nbsp;&nbsp;&nbsp;&nbsp;A. Purchasing a separate AI model trained specifically on that tool's data  
&nbsp;&nbsp;&nbsp;&nbsp;B. Custom code, API wrappers, and significant per-integration engineering effort  
&nbsp;&nbsp;&nbsp;&nbsp;C. Exporting data to CSV and pasting it manually into the chat window each session  
&nbsp;&nbsp;&nbsp;&nbsp;D. Using a third-party middleware platform such as Zapier, which MCP has now made obsolete  

---

**3.** The "USB analogy" for MCP means that:

&nbsp;&nbsp;&nbsp;&nbsp;A. MCP connections are physical hardware interfaces built into enterprise workstations  
&nbsp;&nbsp;&nbsp;&nbsp;B. Any MCP-compliant tool can plug into any MCP-supporting AI, just as any USB device works with any USB port  
&nbsp;&nbsp;&nbsp;&nbsp;C. MCP transfers data at fixed bandwidth rates comparable to USB 3.0 standards  
&nbsp;&nbsp;&nbsp;&nbsp;D. MCP is a hardware abstraction layer managed by the operating system, not the AI model  

---

**4.** In an MCP architecture, an MCP server functions as:

&nbsp;&nbsp;&nbsp;&nbsp;A. A cloud instance that hosts the AI model and handles user authentication  
&nbsp;&nbsp;&nbsp;&nbsp;B. A software intermediary that runs alongside the AI client, translates its requests into calls to an external tool, and returns results  
&nbsp;&nbsp;&nbsp;&nbsp;C. A security firewall that monitors and rate-limits the AI's queries to connected systems  
&nbsp;&nbsp;&nbsp;&nbsp;D. A training pipeline that fine-tunes the AI model on data from connected tools  

---

**5.** When Claude Desktop is connected to Gmail via MCP, which of the following best characterizes the access it has by default?

&nbsp;&nbsp;&nbsp;&nbsp;A. Write access — Claude can read, draft, and send emails autonomously on behalf of the user  
&nbsp;&nbsp;&nbsp;&nbsp;B. Read-only access — Claude can read and draft emails, but sending requires explicit user action  
&nbsp;&nbsp;&nbsp;&nbsp;C. Selective access — Claude can only read emails the user manually forwards to it in the conversation  
&nbsp;&nbsp;&nbsp;&nbsp;D. No access — Claude summarizes emails from metadata only, never reading the full message body  

---

**6.** A healthcare organization connects its AI assistant to Google Drive via MCP with read-only access. The compliance officer argues this still poses a governance risk. Which reasoning best supports her position?

&nbsp;&nbsp;&nbsp;&nbsp;A. Read-only access is technically impossible to enforce at the MCP protocol layer  
&nbsp;&nbsp;&nbsp;&nbsp;B. Even without write access, an AI can query, cross-reference, and synthesize across an entire Drive in seconds, producing inferences that carry regulatory risk  
&nbsp;&nbsp;&nbsp;&nbsp;C. Google Drive's OAuth tokens automatically escalate to write access after 30 days of read-only use  
&nbsp;&nbsp;&nbsp;&nbsp;D. HIPAA prohibits any AI system from accessing cloud storage, regardless of permission level  

---

**7.** An AI assistant that stores client records in a persistent database between sessions is more strategically valuable than one relying solely on its context window because:

&nbsp;&nbsp;&nbsp;&nbsp;A. Persistent storage allows the AI to operate without an internet connection  
&nbsp;&nbsp;&nbsp;&nbsp;B. Context windows are encrypted end-to-end, making them unsuitable for business data  
&nbsp;&nbsp;&nbsp;&nbsp;C. Information in the context window is cleared between sessions, while a database preserves accumulated data that the AI can query over time  
&nbsp;&nbsp;&nbsp;&nbsp;D. Persistent databases reduce the AI's token consumption, lowering operational costs to near zero  

---

**8.** A static AI assistant (no MCP connections) and a connected AI assistant (MCP-enabled) both start at the same capability baseline on Day 1. Over six months, which of the following most accurately describes their divergence?

&nbsp;&nbsp;&nbsp;&nbsp;A. The connected assistant becomes faster at text generation; the static assistant develops better reasoning from accumulated conversation history  
&nbsp;&nbsp;&nbsp;&nbsp;B. Both remain equivalent because intelligence is determined by the underlying model, not the tools available to it  
&nbsp;&nbsp;&nbsp;&nbsp;C. The connected assistant accumulates organizational context, live data, and workflow history — compounding its usefulness — while the static assistant remains dependent on what users manually provide each session  
&nbsp;&nbsp;&nbsp;&nbsp;D. The static assistant outperforms over time because it avoids the latency and error risk introduced by external tool calls  

---

**9.** Which of the following best represents the range of system types that can be connected to an AI assistant via MCP?

&nbsp;&nbsp;&nbsp;&nbsp;A. Only cloud-based SaaS platforms with published REST APIs  
&nbsp;&nbsp;&nbsp;&nbsp;B. Only tools developed by the same organization that created the AI model  
&nbsp;&nbsp;&nbsp;&nbsp;C. Email, file storage, calendars, databases, web content, code repositories, workflow automation platforms, and infrastructure services  
&nbsp;&nbsp;&nbsp;&nbsp;D. Any system, provided the user has developer-level programming skills to build a custom integration  

---

**10.** The strategic implication of MCP as an open standard — rather than a proprietary protocol owned by a single vendor — is best described as:

&nbsp;&nbsp;&nbsp;&nbsp;A. It prevents any single AI provider from monetizing tool connections, keeping all integrations permanently free  
&nbsp;&nbsp;&nbsp;&nbsp;B. It creates a shared integration ecosystem where tools built once to the standard work across any compliant AI platform, compounding value as the ecosystem grows  
&nbsp;&nbsp;&nbsp;&nbsp;C. It limits competition by requiring all AI developers to license the protocol from Anthropic  
&nbsp;&nbsp;&nbsp;&nbsp;D. It standardizes AI output formats, ensuring that responses from different models are interchangeable  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | B | MCP is defined as an open standard published by Anthropic that enables any compliant AI to connect to any compliant tool. It is not proprietary, not a database, and not an authentication layer. |
| 2 | B | Before MCP, connecting AI to external tools required custom code, API wrappers, and significant per-integration engineering effort — every integration was a one-off project. |
| 3 | B | The USB analogy illustrates protocol standardization: just as any USB device works with any USB port, any MCP-compliant tool works with any MCP-supporting AI. |
| 4 | B | An MCP server is a small piece of software that runs alongside Claude Desktop, translates Claude's requests into calls to the actual tool, and returns results — a software intermediary, not a hosting or security layer. |
| 5 | B | Claude creates drafts but cannot send emails; sending requires manual action by the user — making Gmail access effectively read-and-draft rather than full write access. |
| 6 | B | The Meridian case study articulates this risk precisely: even read-only access allows the AI to query, cross-reference, and synthesize across an entire Drive in seconds, producing HIPAA-relevant inferences without a human bottleneck. |
| 7 | C | Claude's context window is non-persistent (clears between sessions); persistent storage (e.g., Supabase) allows data to accumulate and be queried over time — the core functional distinction for AI workflows. |
| 8 | C | Connected AI accumulates organizational context and workflow history over time, while static AI remains dependent on manual input each session — the capability gap widens, not narrows. |
| 9 | C | The MCP landscape spans email, file storage, calendars, databases, web content, code repositories, workflow automation, and infrastructure — far broader than SaaS-only or developer-only scope. |
| 10 | B | An open standard creates a shared ecosystem where any tool built once to the standard works with any compliant AI platform. This compounds network value across the entire landscape rather than siloing integrations within one vendor. |
