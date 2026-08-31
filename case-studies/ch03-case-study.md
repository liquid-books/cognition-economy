# Case Study — Chapter 3: Tools and the MCP Revolution
*Florida Atlantic University — Graduate Course*

---

## Case Study: The Governance Gap at Palmetto Health Partners

### Background

Palmetto Health Partners is a mid-sized regional healthcare management organization headquartered in Fort Lauderdale, Florida, with approximately 1,400 employees across twelve affiliated clinics and three administrative centers. The organization manages insurance credentialing, patient scheduling, billing operations, and clinical staff coordination on behalf of its affiliated practices. Unlike hospital systems with large IT departments, Palmetto operates with a lean technology team of eight — a structure common to regional healthcare management companies that grew rapidly through acquisition rather than organic digital transformation.

Palmetto's Chief Operating Officer, Diana Ruiz, attended a continuing education seminar on AI adoption in healthcare administration. What she brought back to leadership was not a vendor proposal — it was a framework. She had seen a live demonstration in which an AI assistant, connected to a live Google Workspace environment via MCP, pulled a week's worth of scheduling conflicts, cross-referenced them against insurance authorization windows in a connected database, and drafted staffing adjustment memos — in under four minutes. The equivalent task at Palmetto required two full-time coordinators and typically took two days. Ruiz returned to Fort Lauderdale with a mandate: evaluate whether MCP-enabled AI could be integrated into Palmetto's administrative operations within the fiscal year.

Palmetto's CTO, James Okafor, was cautiously supportive. His team had already piloted an AI desktop assistant for individual productivity tasks — drafting internal communications, summarizing meeting notes — and the results were positive. But the demonstrations Ruiz described were fundamentally different in kind. Connecting the AI to live systems — Palmetto's Google Workspace, its patient scheduling database, its credentialing file archive — meant the AI was no longer a drafting assistant operating on information employees manually provided. It would be reading, and potentially writing, directly into Palmetto's operational environment. Okafor recognized that the technical setup was not the hard part. The governance was.

Palmetto's compliance officer, Veronica Sánchez, immediately flagged the HIPAA implications. Even though the MCP connections being discussed did not directly touch patient health records, Palmetto's Google Drive contained hundreds of documents with quasi-identifiable administrative data — scheduling patterns, insurance claim summaries, staffing assignments cross-referenced with clinic locations. The line between operational data and protected health information was not always clean. Any AI system that could *read* that Drive could potentially *reason across* it in ways that produced HIPAA-relevant inferences. Sánchez had seen this problem before in the context of cloud storage audits. MCP, she argued, created the same risk surface at a new layer of abstraction.

### The Situation

Leadership at Palmetto now faced a decision that went beyond technology procurement. They had identified a genuine operational advantage — MCP-connected AI could compress two-day coordination cycles into four-minute workflows — but the architecture that enabled that advantage also introduced a new class of governance risk. The protocol's universality, the very feature that made it powerful, meant that once granted, an AI's access to connected systems was broad and persistent. Unlike a human employee who reads one file at a time and can be watched, a connected AI can query, cross-reference, and synthesize across an entire Drive in seconds. There is no natural bottleneck for auditing what was accessed and why.

Okafor proposed a phased rollout: start with read-only connections to non-sensitive calendaring and scheduling systems, establish logging requirements, and only expand to write-enabled connections after a governance framework was approved by compliance and legal. Ruiz supported the phased approach but worried about competitive timing — two of Palmetto's largest competitors had already announced AI workflow pilots, and the organization's board was asking about differentiation. The strategic tension was real: moving carefully protected compliance, but moving slowly ceded ground. Sánchez's position was that Palmetto should not expand MCP access beyond read-only until a formal AI access policy — including data classification rules, access logging standards, and a defined approval process for new MCP tool connections — was ratified by the compliance committee.

### Discussion Prompt

Using the frameworks presented in this chapter, analyze the strategic and governance tension Palmetto faces. How does the architectural shift MCP represents — from AI as a drafting tool to AI as a live participant in operational systems — change the risk calculus for organizations in regulated industries? Consider specifically the distinction between read and write access, the compounding intelligence advantage of connected AI over time, and the organizational costs of governance delay. What decision framework would you recommend Palmetto's leadership adopt, and what conditions would need to be satisfied before expanding from read-only to write-enabled MCP connections?

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

