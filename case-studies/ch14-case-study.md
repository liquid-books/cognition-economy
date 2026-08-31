# Case Study — Chapter 14: Security, Data, and Building Inside Guardrails
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Case Study: A Near-Miss at Halcyon Federal Credit Union

### Background

Halcyon Federal Credit Union is a $3-billion regional credit union headquartered in Spokane, Washington, with about thirty branches across the Pacific Northwest and roughly four hundred thousand members. Founded in 1957 to serve aerospace workers, Halcyon has grown into a full-service financial institution with a notably tech-forward reputation among credit unions of its size — it was the first credit union in its region to offer instant-issue debit cards, the first to deploy a fully digital mortgage application flow, and one of the first to launch a member-facing AI chatbot for routine account questions. Its Chief Information Security Officer, Marisol Renteria, joined the firm after eleven years at a large national bank, and she had built a security organization that the firm's board explicitly considered one of its competitive assets.

Early in the firm's AI adoption, Halcyon's Chief Operating Officer, Devin Yost, authorized a six-month internal experiment to evaluate generative AI tools across three departments: member services, lending operations, and marketing. The pilot was structured carefully — each department received a list of three pre-approved enterprise-tier tools, a one-page briefing on data handling, and a single point of contact in Marisol's organization for any questions. The pilot ran for five months without incident. In month six, a quarterly internal audit surfaced a finding that would test every part of the firm's security posture.

### The Situation

The finding was specific. A team lead in lending operations — a sixteen-year Halcyon employee with an unblemished record — had been using the free tier of a popular consumer AI tool to help draft denial letters for declined loan applications. She had not been told she could not. The pre-approved tools list had focused on member services and marketing; lending operations had been mentioned only in passing during the briefing, and the team lead had reasoned that since her work product (the denial letters) was not member-facing data but her own writing, the consumer tool was acceptable. Over the course of seven weeks, she had pasted approximately 340 partial loan application records into the tool — names, loan amounts, declined-reason codes, and credit context — to get faster first drafts. The drafts were excellent. None of the letters that went to members contained AI-generated errors. The work product was unimpeachable. The data exposure, however, was real: under the consumer terms, that information had left the firm's control the moment it was pasted — with no data-processing agreement, no retention commitment, and no contractual mechanism for retrieval or deletion. Whether or how the vendor used it was, from the audit committee's chair, beside the point: the firm could not say, and could not prove otherwise.

Marisol's team treated the finding as a near-miss rather than an incident — no member had been harmed, no regulatory threshold had been crossed, and the data exposure, while real, was bounded and traceable. Devin Yost, however, faced a harder question. The firm's existing controls had failed in a specific way: not because the rules were unclear, but because the rules had not anticipated the exact kind of work the team lead was doing. The team lead had acted in good faith, made a defensible interpretation, and exposed the firm anyway. The board's audit committee, briefed the following week, wanted to know three things. First, what change to the firm's controls would prevent the next variation of this scenario? Second, how would the firm assure itself that no other version of this exposure was happening, undiscovered, in other departments right now? Third, what was the right cultural response — punishment, training, restructuring, all three, or none — for an employee who had done diligent work that nonetheless created risk? The committee gave Yost thirty days to come back with a plan.

### Discussion Prompt

Using the four-question security framework from this chapter (where the data goes, how long it is retained, who can see it, and what happens if it leaks), evaluate where Halcyon's controls actually failed in the lending-operations near-miss, distinguishing failures at the contractual layer from failures at the operational and cultural layers. What specific changes to the firm's pre-approved tools list, briefing materials, and ongoing audit cadence would close the gap that allowed this scenario to develop? Then consider the cultural question Devin Yost must answer for the board: how should the firm respond to an employee who acted in good faith but created risk, and what would a response that strengthens future reporting (rather than suppressing it) actually look like in practice?

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

