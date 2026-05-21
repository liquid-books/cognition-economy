# Chapter 8 Quiz: Plugins — Extending Your Workshop
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** A business analyst already has MCP connections to her cloud database and a custom system prompt configured for her data workflows. A colleague suggests she replace those with equivalent marketplace plugins for simplicity. Evaluate this recommendation.

&nbsp;&nbsp;&nbsp;&nbsp;A. The colleague is correct — plugins are objectively superior because they require less ongoing maintenance.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The recommendation misunderstands the tradeoff: plugins maximize convenience but sacrifice the configurability and local-machine access that MCP provides; the analyst should keep MCP where control matters.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Both approaches are equivalent — the choice is purely aesthetic and has no workflow implications.  
&nbsp;&nbsp;&nbsp;&nbsp;D. MCP connections are always preferable because cloud-based plugins introduce unacceptable security risk for any business use.  

---

**2.** A sales team has a detailed skill that structures how the AI drafts client proposals — tone, sections, and formatting. A manager argues this is sufficient and no plugin is needed. A senior analyst disagrees. What is the analytical basis for the analyst's disagreement?

&nbsp;&nbsp;&nbsp;&nbsp;A. Skills are always less reliable than plugins and should be replaced whenever possible.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Skills define how the AI thinks and behaves; they cannot supply live client data from the CRM. Without a plugin, the AI is drafting proposals based on described context rather than actual account records.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Plugins make skills redundant once installed, so the skill should be retired.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The analyst is wrong — a well-written skill can substitute for any external data connection.  

---

**3.** A department head is evaluating the plugin marketplace and finds herself drawn to installing integrations for tools her team uses occasionally, tools that look impressive, and tools recommended by peers in other industries. Apply the chapter's discovery framework: which of these impulses is most likely to produce a useful plugin library?

&nbsp;&nbsp;&nbsp;&nbsp;A. Tools recommended by peers, because social proof indicates broad utility.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Tools that look impressive, because capability breadth signals long-term value.  
&nbsp;&nbsp;&nbsp;&nbsp;C. None of them — the correct starting point is identifying personal friction: the specific tasks currently performed outside the AI conversation that interrupt thinking and require tab-switching or manual data transfer.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Tools used occasionally, because infrequent tasks have the highest ROI when automated.  

---

**4.** During plugin installation, an AI integration requests access to a user's contacts, calendar, file system, and billing records — even though the plugin's stated function is to search a knowledge base. How should a professional evaluate and respond to this permission request?

&nbsp;&nbsp;&nbsp;&nbsp;A. Grant all permissions immediately; restricting them may cause the plugin to malfunction.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Decline all permissions and test whether the plugin works anyway.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Treat permission scope as a governance decision: grant only what is functionally necessary for the intended capability and decline anything that represents overreach — applying the same judgment used for any enterprise application.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Consult the IT department before granting any permissions, as plugin authentication is always a security vulnerability.  

---

**5.** A consultant installed 22 plugins over three months and reports that her AI workflow feels cluttered and harder to reason with, even though she uses only four of the integrations regularly. Synthesize a principle from the chapter that explains this outcome and prescribes a remedy.

&nbsp;&nbsp;&nbsp;&nbsp;A. The AI model degrades in quality when too many plugins are active simultaneously; the solution is to upgrade to a higher-tier plan.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Restraint is itself a discipline: plugins installed without a specific articulated use case add cognitive overhead without adding value. The remedy is to audit the library and remove anything without a clear, regularly-used purpose.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The problem is platform-specific and can be resolved by switching to a competing AI tool.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Twenty-two plugins is within normal range; the consultant should install additional plugins to fill remaining capability gaps before evaluating performance.  

---

**6.** An operations manager cannot find a marketplace plugin for the proprietary inventory system her firm uses. Her first instinct is to accept the gap and work around it manually. Evaluate this response against the chapter's framework for build-vs-install decisions.

&nbsp;&nbsp;&nbsp;&nbsp;A. Her instinct is correct — custom development is only appropriate for engineering teams, not business professionals.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The gap represents a build opportunity: a plugin is fundamentally a defined input-output specification connecting the AI to a data source, and the four-step build process — beginning with a plain-English capability definition — is accessible to non-developers when the AI assists with the specification.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The correct response is to switch to an inventory system that has marketplace plugin support.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Manually working around the gap is always preferable to building a custom integration, which introduces unacceptable maintenance risk.  

---

**7.** In the four-step process for building a custom plugin, Step 1 requires defining the capability in plain English before any technical work begins. What is the underlying reasoning for sequencing the process this way?

&nbsp;&nbsp;&nbsp;&nbsp;A. Plain-English documentation is a compliance requirement for enterprise AI governance.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Starting with a clear articulation of what the plugin does, what it takes as input, and what it produces as output forces the builder to validate their own mental model — vague specs produce broken tools, and ambiguity discovered early is cheaper than ambiguity discovered in production.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The sequence is arbitrary; technical specification and plain-English definition can be done in any order without affecting outcomes.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Plain-English definitions are the format required by all plugin APIs and cannot be skipped for technical reasons.  

---

**8.** Two organizations operate at different levels of AI maturity. Firm A uses only marketplace plugins. Firm B has built several custom plugins tailored to its proprietary workflows, with AI assistance at each step. What does this distinction signal about organizational capability, and what is its strategic implication?

&nbsp;&nbsp;&nbsp;&nbsp;A. Firm B is taking on unnecessary risk; marketplace plugins are always more reliable than custom-built integrations.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Firm A is more agile because it avoids the maintenance burden of custom tools.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Firm B has crossed from tool-user to tool-maker — it can create integrations that competitors using only marketplace solutions cannot replicate, because the capabilities are built around proprietary processes rather than generic use cases.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The distinction has no strategic implication; both firms have equivalent AI capability once they have covered the same functional categories.  

---

**9.** A team must choose between a cloud-based plugin and a locally-configured MCP connection for a workflow that handles sensitive client financial records. What framework should guide this architectural decision?

&nbsp;&nbsp;&nbsp;&nbsp;A. Always choose the option with faster installation time to accelerate adoption.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Always choose MCP because local connections are inherently superior to cloud integrations.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The decision should be governed by the control-vs-convenience tradeoff in the context of data sensitivity: where data governance, auditability, and configuration precision matter most, MCP's local-machine architecture justifies the additional setup cost over the convenience of a cloud-based plugin.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Cloud-based plugins offer equivalent security to local MCP connections and should always be preferred for ease of maintenance.  

---

**10.** A professional builds a workflow that combines a skill defining how the AI structures weekly client reports with a plugin that pulls live project status from the team's project management system. Compared to using either a skill or a plugin alone, what does this combination uniquely accomplish?

&nbsp;&nbsp;&nbsp;&nbsp;A. It reduces the number of prompts required but does not change the quality or accuracy of outputs.  
&nbsp;&nbsp;&nbsp;&nbsp;B. It eliminates the need for any human review before reports are sent to clients.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The skill governs process and format while the plugin supplies current reality — together they produce outputs that are both consistently structured and grounded in live data, something neither a standalone skill nor a standalone plugin can deliver.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The combination is redundant; a sufficiently detailed skill can substitute for any plugin by providing the AI with enough background context.  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | B | MCP and plugins serve different purposes: MCP offers maximum flexibility and local-machine access at the cost of configuration; plugins offer maximum convenience at the cost of control. Replacing MCP with plugins is appropriate only when convenience outweighs the need for configurability — not as a blanket improvement. |
| 2 | B | Skills shape how the AI thinks and behaves; they cannot supply live external data. A plugin is the layer that makes actual account records available in the conversation. The most powerful workflows use both — a skill that defines the process, and a plugin that provides the live data that process runs on. |
| 3 | C | The discovery framework begins with friction: the specific tasks currently performed outside the AI conversation — tab-switching, copy-pasting, manually fetching data. Social proof, impressiveness, and occasional utility are all inferior starting points because they prioritize external signals over personal workflow reality. |
| 4 | C | Permission scope is a governance decision, not a formality. Plugin authentication requires the same judgment applied to any enterprise application: grant what is functionally necessary, decline overreach. Permissions for capabilities unrelated to the plugin's stated function are a red flag warranting scrutiny. |
| 5 | B | A plugin installed without a specific use case "adds to the cognitive overhead of your setup without adding value." Restraint — articulating a specific use case before installation — is the prescribed discipline. A cluttered plugin library is the predictable outcome of violating this principle. |
| 6 | B | The chapter frames building a custom plugin as accessible to non-developers when approached correctly: define the capability in plain English, use the AI to write the specification, test on real inputs, document clearly. A marketplace gap is not a dead end — it is a build signal for workflows too specific or proprietary to attract third-party plugin development. |
| 7 | B | Plain-English definition is a forcing function for clarity. The build process begins here precisely because ambiguity in the specification produces unusable outputs. Discovering gaps in the mental model at Step 1 costs nothing; discovering them after a full specification has been generated is more expensive to resolve. |
| 8 | C | Building custom plugins signals a transition from tool-user to tool-maker — an organizational capability that cannot be replicated by competitors limited to generic marketplace solutions. Custom integrations encode proprietary processes directly into the AI workflow, creating durable operational advantages tied to the firm's specific data and practices. |
| 9 | C | The control-vs-convenience tradeoff is the central architectural framework for this decision. When data sensitivity, auditability, and configuration precision are primary concerns, MCP's local-machine architecture is the appropriate choice despite its higher setup cost. Cloud-based plugins are not inherently insecure, but they offer less control over data routing and configuration — a meaningful distinction for sensitive financial workflows. |
| 10 | C | A skill without a plugin operates on described or static context. A plugin without a skill delivers raw data without structured process. Their combination produces outputs that are simultaneously well-structured and grounded in current reality — the defining characteristic of a mature, connected AI workflow that neither component achieves independently. |
