# Chapter 8 Quiz: Plugins — Extending Your Workshop
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** Which of the following best defines a plugin in the context of AI workflow architecture?

&nbsp;&nbsp;&nbsp;&nbsp;A. A saved set of instructions that shapes how an AI responds to a particular type of task  
&nbsp;&nbsp;&nbsp;&nbsp;B. A pre-built integration between an AI tool and an external service, installed through a marketplace with a single action  
&nbsp;&nbsp;&nbsp;&nbsp;C. A locally configured server that allows an AI to communicate directly with tools on your machine  
&nbsp;&nbsp;&nbsp;&nbsp;D. A system prompt template that enables AI to simulate access to external data  

---

**2.** How do plugins differ architecturally from skills?

&nbsp;&nbsp;&nbsp;&nbsp;A. Plugins are stored locally; skills are cloud-based  
&nbsp;&nbsp;&nbsp;&nbsp;B. Skills define how an AI behaves for a task; plugins provide live connections to external tools or data  
&nbsp;&nbsp;&nbsp;&nbsp;C. Plugins require developer configuration; skills install with one click  
&nbsp;&nbsp;&nbsp;&nbsp;D. Skills and plugins are functionally equivalent — the terms describe the same capability  

---

**3.** What is the primary tradeoff between using a plugin versus configuring an MCP server connection?

&nbsp;&nbsp;&nbsp;&nbsp;A. Plugins support more integrations; MCP servers are limited to Google Workspace tools  
&nbsp;&nbsp;&nbsp;&nbsp;B. MCP servers are faster at runtime; plugins have higher installation overhead  
&nbsp;&nbsp;&nbsp;&nbsp;C. Plugins offer maximum convenience with reduced control; MCP offers maximum control at the cost of greater setup effort  
&nbsp;&nbsp;&nbsp;&nbsp;D. Plugins work only in Claude; MCP works across all AI platforms  

---

**4.** What does the "friction-first" method of plugin discovery involve?

&nbsp;&nbsp;&nbsp;&nbsp;A. Browsing the full plugin marketplace and installing the highest-rated options  
&nbsp;&nbsp;&nbsp;&nbsp;B. Identifying workflow pain points — moments where you leave your AI conversation to fetch or transfer information — and mapping those to available plugins  
&nbsp;&nbsp;&nbsp;&nbsp;C. Asking your AI to recommend plugins based on your job title  
&nbsp;&nbsp;&nbsp;&nbsp;D. Starting with the most technically complex integrations and working backward to simpler ones  

---

**5.** What does plugin permission management refer to, and why does it matter?

&nbsp;&nbsp;&nbsp;&nbsp;A. The process of assigning which team members can install plugins; it prevents unauthorized use  
&nbsp;&nbsp;&nbsp;&nbsp;B. The step where you review and selectively grant the data access a plugin requests during authentication, ensuring it receives only what it genuinely needs  
&nbsp;&nbsp;&nbsp;&nbsp;C. A developer-only configuration that end users do not encounter  
&nbsp;&nbsp;&nbsp;&nbsp;D. A setting that controls how often a plugin refreshes its data connection  

---

**6.** When is building a custom plugin more appropriate than installing a marketplace plugin?

&nbsp;&nbsp;&nbsp;&nbsp;A. Always — custom plugins perform better than pre-built ones  
&nbsp;&nbsp;&nbsp;&nbsp;B. When the workflow is high frequency and the plugin will be used by more than ten people  
&nbsp;&nbsp;&nbsp;&nbsp;C. When no existing marketplace plugin addresses the specific tool, data source, or capability unique to your role or organization  
&nbsp;&nbsp;&nbsp;&nbsp;D. When the user lacks administrative rights to install marketplace plugins  

---

**7.** What does "restraint as a discipline" mean in the context of plugin selection?

&nbsp;&nbsp;&nbsp;&nbsp;A. Limiting yourself to plugins from verified enterprise vendors only  
&nbsp;&nbsp;&nbsp;&nbsp;B. Deliberately installing fewer plugins to minimize API costs  
&nbsp;&nbsp;&nbsp;&nbsp;C. Choosing to install only plugins you have a specific, articulable use case for — rather than accumulating integrations that add cognitive overhead without delivering consistent value  
&nbsp;&nbsp;&nbsp;&nbsp;D. Waiting until a plugin has been on the marketplace for at least six months before installing it  

---

**8.** What is the first step in building a custom plugin?

&nbsp;&nbsp;&nbsp;&nbsp;A. Paste the tool's API documentation into Claude and ask it to generate a full specification  
&nbsp;&nbsp;&nbsp;&nbsp;B. Define in plain language what the plugin does, what tool or data source it connects to, and what input and output it expects  
&nbsp;&nbsp;&nbsp;&nbsp;C. Build a test harness with at least five real examples before writing any specification  
&nbsp;&nbsp;&nbsp;&nbsp;D. Register the plugin in the marketplace to reserve the integration namespace  

---

**9.** A marketing analyst maps her daily workflow and identifies three points where she leaves her AI conversation: once to check a competitor's latest press release, once to pull live ad performance data from her dashboard, and once to look up a client's recent social activity. What does this friction map primarily reveal?

&nbsp;&nbsp;&nbsp;&nbsp;A. That the analyst's AI tool is misconfigured and should be reset  
&nbsp;&nbsp;&nbsp;&nbsp;B. That the analyst's tasks are too complex to benefit from AI assistance  
&nbsp;&nbsp;&nbsp;&nbsp;C. Specific, high-value integration opportunities where plugins would eliminate information transfer overhead and increase workflow continuity  
&nbsp;&nbsp;&nbsp;&nbsp;D. That the analyst would benefit from switching to a different AI platform with broader native capabilities  

---

**10.** A firm decides to build a custom plugin connecting its proprietary portfolio analytics system to its AI environment rather than waiting for a third-party integration to appear in the marketplace. What does this decision most strongly signal about the organization?

&nbsp;&nbsp;&nbsp;&nbsp;A. That the firm is over-investing in AI infrastructure relative to its actual workflow needs  
&nbsp;&nbsp;&nbsp;&nbsp;B. That the firm has reached a level of AI maturity where it treats integration gaps as engineering problems it can solve — rather than limitations it must work around  
&nbsp;&nbsp;&nbsp;&nbsp;C. That the firm's IT team lacks the vendor relationships needed to access marketplace plugins  
&nbsp;&nbsp;&nbsp;&nbsp;D. That the firm prioritizes security over usability, which will limit long-term adoption  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | B | A plugin is defined as a pre-built integration installed through a marketplace with a single action. Option A describes a skill; Option C describes an MCP server; Option D describes a prompt technique, not a real integration. |
| 2 | B | The chapter draws a clear architectural distinction: a skill shapes how the AI thinks and behaves; a plugin extends where the AI reaches. Skills define the process; plugins provide the live data that process runs on. |
| 3 | C | The chapter explicitly frames the MCP-vs-plugin choice as a control-versus-convenience tradeoff. Plugins require no configuration but offer less flexibility; MCP connections require setup but give full control. The other options misstate the actual differences. |
| 4 | B | The friction-first method begins with self-observation — identifying where you exit your AI conversation to manually fetch or move information. Those friction points become the plugin roadmap. Browsing the marketplace without a use case is the pattern the chapter warns against. |
| 5 | B | Permission management is the practice of reviewing what data access a plugin requests during authentication and granting only what is genuinely needed. The chapter frames this as judgment analogous to reviewing app permissions on a phone — a governance act, not a technicality. |
| 6 | C | The chapter states that the marketplace contains what someone else decided to build; when your specific combination of tools and workflows is not covered, building is the appropriate path. The decision is driven by gap, not preference, team size, or access rights. |
| 7 | C | Restraint as a discipline means installing only plugins with a specific, articulable use case — the chapter's test being whether you can describe the use in one sentence before installing. Unused plugins add cognitive overhead without adding value. |
| 8 | B | Step 1 in the chapter's four-step build process is to define the capability in plain English: what the plugin does, what it connects to, and what input and output it expects. Technical work (having Claude write the spec) comes in Step 2, after clarity is established. |
| 9 | C | Each friction point the analyst identified maps directly to a specific integration opportunity. The friction-first method treats these moments as a plugin roadmap — they reveal exactly where connectivity would eliminate overhead and keep the analyst inside a single working context. |
| 10 | B | Building a custom plugin when no marketplace solution exists signals organizational AI maturity — the firm is no longer waiting for the ecosystem to catch up; it is treating integration gaps as solvable engineering problems. This reflects the chapter's framing of custom plugin development as a marker of advanced adoption. |
