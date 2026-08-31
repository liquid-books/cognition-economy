# Case Study — Chapter 13: Hooks, Channels, and Scheduled Tasks — The Always-On Layer
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Case Study: Hooks and Judgment at Bradford & Wynne LLP

### Background

Bradford & Wynne LLP is a sixty-attorney commercial litigation firm headquartered in Cleveland, Ohio, with secondary offices in Columbus and Pittsburgh. Now in its fifth decade, the firm specializes in complex contract disputes, employment litigation, and regulatory defense for mid-market clients across the Midwest. Total billings in the firm's most recent fiscal year reached the low forties of millions, with a partner-to-associate ratio of roughly one to four. Renee Ostrowski, the firm's Director of Operations, has overseen a steady modernization of the firm's intake, billing, and matter management infrastructure. Eighteen months into that modernization effort, Ostrowski launched what she internally called the "Front-Door Project" — a focused effort to automate the firm's new-client intake workflow.

The motivation was specific and measurable. The firm's existing intake process consumed an average of forty-two minutes of paralegal time per new matter, from the moment a prospective client submitted an inquiry form to the moment a partner received a one-page matter summary for review. With the firm receiving an average of fourteen new-client inquiries per week, the intake workflow was burning roughly twenty paralegal hours weekly — time the firm's two intake paralegals could be spending on substantive case support. More importantly, the lag between inquiry and partner review averaged seven business hours, which was costing the firm an estimated one in eight prospective clients who took their business to faster-responding competitors.

Ostrowski's Front-Door Project assembled a cross-functional team: her two intake paralegals, the firm's Chief Compliance Officer Marcus Tellman, a senior partner from the litigation group, and an outside consultant the firm had retained to help design the AI workflow. The team committed to a ninety-day pilot.

### The Situation

The proposed workflow was straightforward in concept. When a prospective client submitted the intake form on the firm's website, an automated sequence would fire: the AI would extract structured data from the form, check the firm's conflicts database for any conflicts of interest, categorize the matter type, draft a one-page matter summary, and post the result to a dedicated Slack channel that the firm's partners already monitored throughout the day. Each step compressed work that a paralegal had previously done manually.

The architectural debate, however, exposed a deeper tension. Marcus Tellman, the compliance officer, insisted that several steps in the workflow be implemented as deterministic hooks — rules that would always fire, regardless of what the AI judged or did not judge. Specifically, he required that the conflicts check always run on every intake, that every AI action in the workflow be logged to an immutable audit trail, and that any matter involving a regulated industry (healthcare, financial services, energy) automatically be flagged for senior partner review. The consultant pushed back that hard-coding too many rules would make the workflow brittle and unable to handle edge cases. The senior partner argued for the opposite — that the firm's reputation depended on never missing a conflict, never failing to log a substantive client action, and never letting a regulated-industry matter slip through without proper attention. Ostrowski found herself in the middle, trying to design a workflow that was fast enough to deliver the speed benefits her business case promised, rigorous enough to satisfy compliance, and flexible enough to handle the genuinely unusual matters that arrived a few times a month and rarely fit a clean category. The team agreed they needed a framework — a clear rule for deciding which parts of the workflow belonged in hooks and which belonged in AI judgment — before they wrote a single line of the configuration.

### Discussion Prompt

Using the distinction this chapter develops between deterministic hooks (rules that must always fire) and AI-judged steps (decisions that require interpretation), evaluate Bradford & Wynne's proposed intake workflow. Which specific steps should be implemented as hooks and which as AI judgment, and why? How should the firm handle the accountability question — when an automated intake produces an incorrect categorization or misses a subtle conflict, who is responsible, and what review structure should the firm build to make that accountability genuine rather than nominal? Finally, consider the trade-off between speed and rigor: how should the firm decide which compromises are acceptable, and what signals would tell Ostrowski that the workflow is drifting in either direction?

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

