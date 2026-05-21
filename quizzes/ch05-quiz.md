# Chapter 5 Quiz: The Six Engineering Disciplines
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** A senior knowledge worker spends considerable time crafting careful, detailed prompts and consistently receives high-quality single-turn outputs. However, when starting a new session to continue a multi-week project, the AI treats the work as if it has never been discussed. The outputs become generic, and the worker must re-explain decisions made weeks ago. Which engineering discipline is most responsible for this gap — and what is the correct lever to address it?

&nbsp;&nbsp;&nbsp;&nbsp;A. Prompt engineering — the worker needs longer, more detailed prompts at the start of each session.  
&nbsp;&nbsp;&nbsp;&nbsp;B. System prompting — the standing instructions should be updated to include all project history.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Memory engineering — the worker lacks a deliberate mechanism to persist context between sessions, and the minimum fix is a maintained "Working Brief" attached at the start of relevant sessions.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Context engineering — the worker should keep one continuous conversation open rather than starting new sessions.  

---

**2.** An organization wants to deploy an AI-assisted client intake workflow. When a new inquiry email arrives, the system should automatically retrieve the sender's prior correspondence, check for any matching records, draft a personalized response in the firm's voice, and route the draft to the appropriate team member for review — all without manual initiation. Which discipline primarily governs the design of this workflow, and what does it require beyond the other five disciplines?

&nbsp;&nbsp;&nbsp;&nbsp;A. Context engineering — it governs what information flows into each AI call, which is the primary design challenge here.  
&nbsp;&nbsp;&nbsp;&nbsp;B. System prompting — a sufficiently detailed system prompt can automate all of these steps.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Harness engineering — it requires designing the triggers, tool connections, data routing, and human review checkpoints that make the workflow operate autonomously.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Meta prompting — the firm should ask the AI to design the workflow instructions, then execute them manually each time.  

---

**3.** A consultant runs a complex analysis session, attaching a 60-page industry report, three years of financial data, a competitor brief, and a client email thread — all to answer a single strategic question. The AI's response is surprisingly shallow, misses the core issue, and fixates on peripheral data from the financial appendix. Applying the discipline framework, what is the most likely cause of this failure?

&nbsp;&nbsp;&nbsp;&nbsp;A. The AI model lacks the capability to handle strategic questions and should be replaced.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The consultant failed to include examples of the desired output format.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The context window was filled with irrelevant material, reducing the AI's effective working capacity for the actual question and burying the key framing.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The system prompt was not configured for financial analysis tasks.  

---

**4.** A marketing director needs to create a reusable instruction set for producing executive briefings — a task her team performs weekly. She considers writing the instructions herself. Why would a meta-prompting approach likely produce a superior result, and what does that approach involve?

&nbsp;&nbsp;&nbsp;&nbsp;A. Meta prompting is faster but not necessarily higher quality — it trades quality for speed.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Having the AI interview her about the task surfaces implicit requirements, gaps, and unstated preferences she would overlook when writing instructions unilaterally — producing a more complete and precise instruction set.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Meta prompting accesses a library of pre-built professional templates optimized for marketing use cases.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The AI generates instructions that bypass the context window limit, allowing larger documents to be processed.  

---

**5.** Two analysts at the same firm use identical AI subscriptions and write equally well-crafted prompts. Analyst A produces outputs that consistently match her professional standards, rarely require rework, and reflect awareness of her firm's communication norms. Analyst B's outputs are competent but generic — correct in content but requiring significant revision for tone, structure, and fit. No difference in prompt quality explains the gap. What is the most precise diagnosis?

&nbsp;&nbsp;&nbsp;&nbsp;A. Analyst A has more experience with AI and her prompts are actually more skillful than they appear.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Analyst A has a well-configured system prompt that provides her professional role, communication preferences, and output standards as persistent standing context — eliminating the need to re-specify these in every prompt.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Analyst A uses a different AI model that is better suited to professional writing tasks.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Analyst A breaks complex tasks into smaller prompts, which is a prompt engineering technique Analyst B has not learned.  

---

**6.** The six engineering disciplines are described as a layered system in which each discipline multiplies the value of the one below it. A colleague argues this framing is overstated — that the skills can be learned independently and combined additively. What is the strongest argument against the additive view, grounded in how the disciplines actually interact?

&nbsp;&nbsp;&nbsp;&nbsp;A. The disciplines are branded as a system for marketing purposes; in practice they are largely independent.  
&nbsp;&nbsp;&nbsp;&nbsp;B. A well-engineered harness executing a poorly-formed prompt still produces poor output; a rich system prompt cannot compensate for context that is irrelevant or absent; memory engineering only delivers value if it feeds into sessions with proper framing. Each discipline depends on the integrity of the layers beneath it — degradation at any level propagates upward.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The multiplicative relationship only applies to harness engineering and context engineering; the other disciplines are genuinely additive.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The layered model applies only when all six disciplines are fully mastered; partial mastery produces no compounding benefit.  

---

**7.** A professional is preparing for a high-stakes client presentation. She has a strong system prompt, a well-designed meeting-prep skill, and her project's Working Brief. She is deciding between: (A) opening a fresh session and attaching the Working Brief plus the three most recent client emails, or (B) continuing a 90-message conversation from two weeks ago that has covered many related topics. Which choice reflects sound context engineering, and why?

&nbsp;&nbsp;&nbsp;&nbsp;A. Option B — the longer conversation history provides richer context and should always be preferred over starting fresh.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Option A — a fresh session with deliberately curated, relevant context gives the AI higher-quality signal. Long conversations cause early framing to degrade proportionally as new content accumulates, reducing the AI's coherence with the original purpose.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Option B — AI models are specifically optimized for long-running sessions and perform best with extended history.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Option A — only because attaching the Working Brief is faster than scrolling through an old conversation.  

---

**8.** Consider the three layers of memory engineering: conversation memory, file-based memory, and database memory. A solo consultant wants AI continuity across client engagements but has no developer resources and cannot set up database infrastructure. Which layer is the appropriate lever, what does it require in practice, and what is its key limitation compared to the most powerful layer?

&nbsp;&nbsp;&nbsp;&nbsp;A. Conversation memory is the appropriate layer — she should keep all sessions open indefinitely to preserve continuity.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Database memory is the only viable option; without it, meaningful continuity is impossible.  
&nbsp;&nbsp;&nbsp;&nbsp;C. File-based memory is the right lever — maintained as a living document (e.g., a "Working Brief") attached at the start of sessions. Its limitation is that it requires manual maintenance and cannot automatically accumulate knowledge across sessions the way database memory can.  
&nbsp;&nbsp;&nbsp;&nbsp;D. File-based memory is the right lever, and it is functionally equivalent to database memory for most professional use cases.  

---

**9.** A team deploys an AI workflow for weekly competitive intelligence reports. They have invested in prompt engineering and harness engineering but skipped system prompting and memory engineering. After two months, the reports are technically accurate but stylistically inconsistent, ignore the firm's established framing conventions, and fail to build on prior weeks' findings. Using the discipline framework, identify the two missing layers and explain why each gap produces the specific failure described.

&nbsp;&nbsp;&nbsp;&nbsp;A. Context engineering and meta prompting — the team is not managing context window usage and has not used AI to optimize their prompts.  
&nbsp;&nbsp;&nbsp;&nbsp;B. System prompting and memory engineering — the missing system prompt explains the inconsistent tone and stylistic drift (no standing definition of voice, format, or conventions); the missing memory engineering explains why each report ignores prior weeks' findings (no persistent knowledge across sessions).  
&nbsp;&nbsp;&nbsp;&nbsp;C. Meta prompting and harness engineering — the prompts were written manually and the workflow was not properly automated.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Context engineering and harness engineering — the documents are too long and the automation triggers are misconfigured.  

---

**10.** Harness engineering is described as having the highest setup cost of all six disciplines but delivering leverage that is qualitatively different from the others. What is the structural distinction that makes harness engineering categorically different — not merely incrementally better — than mastering the first five disciplines?

&nbsp;&nbsp;&nbsp;&nbsp;A. Harness engineering eliminates the need for prompt engineering once workflows are built, reducing total cognitive overhead.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Harness engineering is the only discipline that requires technical programming skills, which is why it is inaccessible to most professionals.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The first five disciplines optimize individual AI interactions — each requiring active human initiation. Harness engineering removes the human from the initiation loop entirely, enabling workflows that trigger, execute, and deliver outputs autonomously, fundamentally changing the ratio of professional time to productive output.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Harness engineering provides the most value because it combines all five disciplines into a single interface, reducing the need to learn them separately.  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | C | The failure is cross-session discontinuity — the hallmark of absent memory engineering. Prompt engineering governs single-turn quality; system prompts store role context but not project-specific history; keeping one long conversation open violates sound context engineering principles. The Working Brief is the minimum viable memory engineering practice. |
| 2 | C | Autonomous, trigger-based, multi-tool workflows are the defining domain of harness engineering. It requires more than the other disciplines because it demands designing the environment — triggers, data routing, tool connections, human review checkpoints — not just the content of individual AI interactions. |
| 3 | C | This is a context engineering failure. The context window is finite working memory; loading it with large, partially irrelevant documents crowds out the AI's effective capacity for the actual question. The financial appendix dominating the output signals the AI is processing volume rather than signal. The fix is deliberate curation — attach only what is directly relevant to the specific question. |
| 4 | B | The core argument for meta prompting is that writing good instructions requires knowing what to include — and humans systematically miss their own blind spots. The AI-driven interview process surfaces implicit requirements and unstated assumptions, producing instructions more complete than self-authored ones. |
| 5 | B | System prompting is the standing context that loads before every exchange. It defines role, tone, format preferences, and quality standards persistently, so they do not need to be re-specified in each prompt. When equally good prompts produce systematically different output fit, the difference is almost always at the system prompt layer. |
| 6 | B | The disciplines are interdependent in a layered hierarchy, not independent modules. A harness executing weak prompts scales weak outputs. A rich system prompt cannot supply context that was never engineered into the session. Memory engineering only creates value when it feeds into sessions with sound framing and context management. Failure at any layer propagates upward — this is the structural argument against additive independence. |
| 7 | B | Context engineering principles specify that: (1) context should be deliberately curated, not accumulated; (2) framing placed early has disproportionate influence; (3) long conversations cause early context to degrade proportionally. A fresh session with targeted, relevant documents gives the AI higher-quality signal than a drifted 90-message thread. |
| 8 | C | File-based memory is accessible without technical infrastructure and provides meaningful continuity when maintained as a living document. Its key limitation versus database memory is that it requires manual upkeep and cannot autonomously accumulate knowledge — it only carries what the human explicitly captures and injects. Database memory enables structured, self-accumulating persistence across unlimited sessions. |
| 9 | B | System prompting governs persistent tone, style, and conventions — its absence causes stylistic inconsistency. Memory engineering governs what knowledge carries across sessions — its absence means each weekly report starts from zero, unable to build on prior findings. The two failures map precisely to the two missing disciplines. |
| 10 | C | The first five disciplines all require a human to initiate each interaction. Harness engineering removes that requirement — workflows fire on triggers, execute autonomously, and deliver outputs to the right place without human initiation. This changes the fundamental leverage ratio, not just the quality of individual interactions. |
