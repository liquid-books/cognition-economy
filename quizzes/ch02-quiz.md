# Chapter 2 Quiz: Standing Up Your Cognitive Workshop
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** A knowledge worker reports that every new AI conversation begins the same way: they spend the first several exchanges re-explaining their professional role, output preferences, and recurring context before the tool becomes useful. This friction most directly undermines which cognitive workshop design principle?

&nbsp;&nbsp;&nbsp;&nbsp;A. Tool independence — each tool should perform a distinct job without overlap  
&nbsp;&nbsp;&nbsp;&nbsp;B. Persona specificity — each tool should have a clearly defined professional role  
&nbsp;&nbsp;&nbsp;&nbsp;C. Persistent configuration — standing instructions should load automatically before every session  
&nbsp;&nbsp;&nbsp;&nbsp;D. Meta-prompting — the tool should generate its own instructions based on user input  

---

**2.** A financial analyst wants to draft a system prompt directive that ensures their AI consistently produces concise, bulleted executive summaries — without being reminded of this preference in every conversation. Which of the four system prompt components most directly addresses this requirement?

&nbsp;&nbsp;&nbsp;&nbsp;A. Role — specifies what professional function the AI is performing  
&nbsp;&nbsp;&nbsp;&nbsp;B. Context — provides background about the user's industry and responsibilities  
&nbsp;&nbsp;&nbsp;&nbsp;C. Rules — governs what the AI should or should not include in its responses  
&nbsp;&nbsp;&nbsp;&nbsp;D. Format — specifies length, structure, and presentation preferences  

---

**3.** A sales director needs to pull relevant emails from the past week, cross-reference a proposal stored in cloud storage, and draft a structured meeting summary — all in one workflow. What architectural feature makes one category of AI tool best suited for this task?

&nbsp;&nbsp;&nbsp;&nbsp;A. A standalone desktop application, because it provides the strongest long-form reasoning capabilities  
&nbsp;&nbsp;&nbsp;&nbsp;B. A Google-native AI assistant, because it has awareness of Gmail, Drive, and Calendar data when those are explicitly invoked  
&nbsp;&nbsp;&nbsp;&nbsp;C. A developer sandbox environment, because it exposes raw API access for data retrieval pipelines  
&nbsp;&nbsp;&nbsp;&nbsp;D. Any of the three tools equally, since modern AI models all have access to the same underlying data  

---

**4.** A manager manually writes a 150-word system prompt listing preferences like "be professional," "be concise," and "avoid jargon." A colleague generates their system prompt through meta-prompting instead. What is the most significant structural advantage of the meta-prompting approach?

&nbsp;&nbsp;&nbsp;&nbsp;A. It produces shorter prompts that consume fewer tokens per conversation  
&nbsp;&nbsp;&nbsp;&nbsp;B. It generates a prompt that is compatible with all tools in the cognitive workshop simultaneously  
&nbsp;&nbsp;&nbsp;&nbsp;C. It allows the AI to ask targeted clarifying questions that surface specific preferences the user would not have thought to articulate  
&nbsp;&nbsp;&nbsp;&nbsp;D. It ensures the configuration does not need to be updated when the user's role changes  

---

**5.** You are designing an AI persona for a communications director who regularly prepares executive-level briefings. Which of the following persona descriptions best reflects the principles of effective persona design for a cognitive workshop?

&nbsp;&nbsp;&nbsp;&nbsp;A. "You are a helpful and professional assistant who is good at summarizing information clearly."  
&nbsp;&nbsp;&nbsp;&nbsp;B. "Your name is Jordan. You have 15 years of communications experience and enjoy helping leaders succeed."  
&nbsp;&nbsp;&nbsp;&nbsp;C. "You are a senior communications strategist. You lead with the core message. You write in tight, declarative sentences. You flag ambiguous language and recommend revisions without being asked."  
&nbsp;&nbsp;&nbsp;&nbsp;D. "You are an AI assistant specialized in executive communications. Always be accurate and cite your sources when possible."  

---

**6.** A team configures all three tools in their cognitive workshop with identical system prompts to ensure consistent output across their workflow. What is the primary conceptual flaw in this approach?

&nbsp;&nbsp;&nbsp;&nbsp;A. Identical prompts prevent the tools from accessing their respective integrations and data sources  
&nbsp;&nbsp;&nbsp;&nbsp;B. Each tool serves a distinct function, and a uniform configuration prevents any tool from being calibrated to its specific job  
&nbsp;&nbsp;&nbsp;&nbsp;C. System prompts are not transferable across tools from different vendors  
&nbsp;&nbsp;&nbsp;&nbsp;D. Duplicate configurations will cause the tools to produce redundant outputs, creating workflow inefficiencies  

---

**7.** A project manager is evaluating whether to create a dedicated saved AI configuration for a specific task. Which scenario most strongly justifies investing in a purpose-built, persistent configuration?

&nbsp;&nbsp;&nbsp;&nbsp;A. A one-time competitive analysis that requires deep reasoning for a single deliverable  
&nbsp;&nbsp;&nbsp;&nbsp;B. An occasional brainstorming session where creative unpredictability is actually desirable  
&nbsp;&nbsp;&nbsp;&nbsp;C. A recurring weekly task — such as meeting prep — where the same structured output is needed from varying inputs each time  
&nbsp;&nbsp;&nbsp;&nbsp;D. A complex, long-form writing project that will be completed over several months  

---

**8.** A consultant has used their cognitive workshop for six months. A recent promotion changed their primary responsibilities from individual contributor to team lead. What is the most principled response to this change?

&nbsp;&nbsp;&nbsp;&nbsp;A. Delete all configurations and start from scratch, as prior context may produce misleading outputs  
&nbsp;&nbsp;&nbsp;&nbsp;B. Update only the primary daily-use tool, since it handles the majority of work  
&nbsp;&nbsp;&nbsp;&nbsp;C. Leave existing configurations in place — the AI tools will adapt to new inputs organically over time  
&nbsp;&nbsp;&nbsp;&nbsp;D. Update each tool's configuration independently, since each tool has a different job whose context has now shifted  

---

**9.** The characterization of a system prompt as "the DNA of every conversation" most precisely captures which functional property?

&nbsp;&nbsp;&nbsp;&nbsp;A. It is unique to each user and cannot be copied or replicated by others  
&nbsp;&nbsp;&nbsp;&nbsp;B. It is expressed in every interaction and shapes all subsequent responses from the first message forward  
&nbsp;&nbsp;&nbsp;&nbsp;C. It operates invisibly at the model level and controls underlying inference parameters  
&nbsp;&nbsp;&nbsp;&nbsp;D. It must be rewritten at the start of each new conversation to remain effective  

---

**10.** A professional uses their primary reasoning-focused AI tool to draft the instruction set for a task-specific saved configuration in a second tool — even though the two tools are completely independent and share no data. What principle does this workflow illustrate?

&nbsp;&nbsp;&nbsp;&nbsp;A. When tools are independent, outputs must be manually transferred between them, adding overhead  
&nbsp;&nbsp;&nbsp;&nbsp;B. Tool independence is a limitation that should be designed around using API integrations  
&nbsp;&nbsp;&nbsp;&nbsp;C. One tool can be used instrumentally to improve the configuration quality of another, while both tools remain fully independent in operation  
&nbsp;&nbsp;&nbsp;&nbsp;D. System prompt authorship should always involve a second AI review before deployment  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | C | The core problem described — having to re-explain role and context at the start of every session — is precisely the problem that persistent configuration (standing instructions that auto-load) is designed to eliminate. Tool independence (A) and persona specificity (B) are related concepts but do not directly address session-restart friction. Meta-prompting (D) is a technique for creating the configuration, not the configuration itself. |
| 2 | D | Format governs how output is structured: length, bullet vs. prose, headers, level of formality. Role (A) defines what job the AI is performing; Context (B) provides user background; Rules (C) govern what to include or avoid — none of these specify presentation structure as directly as Format. |
| 3 | B | A Google-native AI assistant is specifically designed with awareness of Gmail, Drive, and Calendar data when invoked. Standalone desktop applications (A) excel at reasoning but have no ecosystem data access. Developer sandboxes (C) are for experimentation, not production workflows. Option D is false — the three tools are independent and have different data access architectures. |
| 4 | C | Meta-prompting's structural advantage is the interview dynamic: targeted questions surface specific preferences, frustrations, and working styles that a user composing the prompt manually would typically omit or underspecify. It does not inherently produce shorter prompts (A), cross-tool compatibility (B), or eliminate the need for future updates (D). |
| 5 | C | Option C defines a professional role, specifies a cognitive posture ("leads with the core message"), sets a communication style ("tight, declarative sentences"), and includes a behavioral directive ("flags ambiguous language"). Options A and D are generic and unspecific. Option B confuses persona with backstory — a name and years of experience are not a functional cognitive posture. |
| 6 | B | Each tool has a different job: one may serve as a deep reasoning partner, another as a task-specific executor, another as an experimentation sandbox. A uniform configuration treats all three as interchangeable, which defeats the purpose of maintaining distinct, purpose-calibrated tools. Options A, C, and D describe secondary concerns or inaccuracies. |
| 7 | C | A recurring task with consistent structure and varying inputs is the ideal use case for a persistent, pre-configured setup: the instructions are written once, and the configuration does the framing work automatically each time. One-time tasks (A, D) and unpredictability-requiring sessions (B) do not benefit from rigid pre-configuration. |
| 8 | D | Each tool is configured for a specific job. When the user's role changes, each tool's job context changes independently — the primary reasoning tool, task-specific saved configurations, and sandbox setups each need to reflect the new context separately, since they are not linked. Options A and B are disproportionate or incomplete responses; Option C incorrectly assumes AI tools adapt without explicit reconfiguration. |
| 9 | B | "DNA of every conversation" captures the idea that the system prompt is expressed in every interaction — it shapes tone, reasoning approach, output structure, and role from the first response onward. It is not about uniqueness (A), invisibility at the model layer (C), or per-session rewriting (D). |
| 10 | C | This workflow illustrates that tool independence does not prevent one tool from being used instrumentally to produce better inputs for another. The two tools remain fully independent in operation — they share no memory or history — but one's output (a well-crafted instruction set) can be pasted as configuration into the other. This is a deliberate, human-mediated workflow, not a data integration. |
