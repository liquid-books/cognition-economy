# Chapter 6 Quiz: Plan Mode — Think Before You Build
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** A marketing director asks an AI to draft a full go-to-market strategy. She provides her industry, product, and a brief description of her "target business professional." The AI returns 3,000 polished words — later found to be calibrated entirely to mid-level managers, not the C-suite executives she actually sells to. Which statement best explains the root cause of this failure?

&nbsp;&nbsp;&nbsp;&nbsp;A. The AI model lacked sufficient knowledge of enterprise marketing strategies.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The AI executed a well-defined task correctly, but the task itself was built on an unchallenged assumption that was never surfaced before execution.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The output was too long; shorter prompts would have produced more accurate results.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The director should have reviewed the output in stages rather than waiting for a complete draft.  

---

**2.** During the planning phase, an AI is permitted to read documents, map dependencies, identify risks, and ask clarifying questions — but is explicitly prohibited from drafting any portion of the final output. What is the primary strategic purpose of maintaining this read-only constraint?

&nbsp;&nbsp;&nbsp;&nbsp;A. It reduces API token consumption during the planning phase, lowering overall cost.  
&nbsp;&nbsp;&nbsp;&nbsp;B. It forces the AI to externalize its assumptions and decision points before they become embedded in completed work, where they are far harder to detect and correct.  
&nbsp;&nbsp;&nbsp;&nbsp;C. It ensures the planning agent and execution agent operate from separate context windows for security purposes.  
&nbsp;&nbsp;&nbsp;&nbsp;D. It prevents the AI from anchoring too strongly to its first draft, encouraging more creative output later.  

---

**3.** A consultant reviews an AI-generated project plan and approves it with the comment: "Looks fine — proceed." Two weeks later, the deliverable omits a key stakeholder audience that was never mentioned in the plan. The consultant argues the AI "should have known." Evaluate this outcome using the plan-as-contract framework.

&nbsp;&nbsp;&nbsp;&nbsp;A. The consultant is correct; the AI bears full responsibility because it produced the plan and should have anticipated the gap.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The failure was in execution — the AI deviated from its approved scope without authorization.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The consultant's approval converted the plan into a mutual agreement on scope, sequence, and assumptions; the omitted audience represents a gap in the plan the consultant confirmed as complete. The failure is diagnostic of the planning phase, not execution.  
&nbsp;&nbsp;&nbsp;&nbsp;D. This outcome is unavoidable because AI cannot independently identify unknown stakeholders.  

---

**4.** A product manager must decide whether to use Plan Mode for two upcoming tasks: (A) writing a one-sentence status update for Slack, and (B) drafting a board-level strategic memo that will inform a $2M budget decision. Applying the complexity-irreversibility framework, which assessment is most defensible?

&nbsp;&nbsp;&nbsp;&nbsp;A. Both tasks warrant Plan Mode because any communication involving leadership carries reputational risk.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Neither task warrants Plan Mode because experienced professionals should be able to guide the AI intuitively without a formal planning gate.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Only Task A warrants Plan Mode because short outputs are more likely to be misinterpreted.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Only Task B warrants Plan Mode — it combines high complexity with high irreversibility. Task A is simple and trivially correctable, making planning overhead with no proportionate return.  

---

**5.** An engineering lead splits AI work across two models: she uses a high-capability reasoning model to interrogate assumptions, map risks, and produce a structured plan, then passes that approved plan to a faster, lighter model for code generation and documentation. A colleague argues this adds unnecessary complexity. What is the strongest counterargument?

&nbsp;&nbsp;&nbsp;&nbsp;A. The split is necessary because different models are trained on different data and must be sequenced to prevent hallucination.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The two-phase approach matches model capability to cognitive demand: deep reasoning belongs at planning, where quality differences are most consequential, while execution — bounded by an approved plan — proceeds reliably at lower cost and higher speed.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Using a powerful model for execution is cost-prohibitive at enterprise scale, making the split an unavoidable budget constraint rather than a strategic choice.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Lighter models produce better output because they are less likely to over-engineer solutions.  

---

**6.** A law firm has used Plan Mode for client proposal work for eighteen months, refining its plan template after each engagement. A new partner observes that proposals are now produced faster and with fewer revision cycles than at peer firms. Which concept best explains this competitive advantage?

&nbsp;&nbsp;&nbsp;&nbsp;A. The firm has automated its proposal process, eliminating the need for human judgment on scope decisions.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Recurring plans tested and improved through real executions accumulate institutional knowledge over time — each iteration surfaces and resolves a category of error, compounding into a framework that works reliably at scale.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The firm's AI models have been fine-tuned on its internal documents, improving domain accuracy.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Faster proposals indicate the planning phase is being appropriately skipped in routine cases, freeing capacity for complex work.  

---

**7.** An executive faces a restructuring decision with multi-year financial and operational consequences. She dedicates two full days to planning before any execution begins: she generates a comprehensive plan, challenges its assumptions, requests revisions, reviews it again with fresh eyes the following morning, and commits to execution only after the plan holds up under repeated scrutiny. A peer calls this over-preparation. What principle most directly justifies her approach?

&nbsp;&nbsp;&nbsp;&nbsp;A. AI-generated plans have a known systematic error rate that requires multiple regenerations to eliminate.  
&nbsp;&nbsp;&nbsp;&nbsp;B. For decisions combining high stakes and high complexity, the ratio of planning time to execution time among high-performing professionals is often one-to-one or greater — the planning phase is not overhead, it is the work that determines whether execution produces the intended outcome.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Longer planning periods reduce legal liability if the restructuring is later challenged by stakeholders.  
&nbsp;&nbsp;&nbsp;&nbsp;D. AI plan quality improves with each regeneration iteration, so repeated passes are always worth the cost.  

---

**8.** A content operations team builds a workflow where a research agent gathers sources, a writing agent drafts sections, an analysis agent critiques logical gaps, and a formatting agent produces the final document. The team lead emphasizes that without a pre-approved plan, this workflow collapses. Why is the plan specifically load-bearing in a multi-agent context?

&nbsp;&nbsp;&nbsp;&nbsp;A. Plans prevent agents from overwriting each other's outputs by enforcing file-level locking.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The plan defines each agent's scope, required inputs, and expected output format — making handoffs between specialized agents explicit and auditable rather than implicit and fragile. Without it, agents operate without coordination context and the workflow becomes chaotic.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Multi-agent systems require a plan because individual agents lack persistent memory across separate sessions.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Plans assign priority levels to agents, ensuring the most capable model handles the highest-stakes subtask automatically.  

---

**9.** Consider the following parallel: a surgeon who skips the pre-operative review — forgoing scan analysis, complication mapping, and approach confirmation — in order to reach the operating table faster. This is characterized not as efficiency but as recklessness. What does this parallel reveal about AI-assisted professional work?

&nbsp;&nbsp;&nbsp;&nbsp;A. AI tools should only be used by domain-certified professionals who can independently verify outputs.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Skipping the planning phase to reach output faster does not save time — it trades a brief upfront investment for a high probability of foundational errors that are far more costly to correct after the fact than to prevent.  
&nbsp;&nbsp;&nbsp;&nbsp;C. AI-generated work should be reviewed by a second professional before delivery, just as surgeons work with an anesthesiology team.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The parallel illustrates that AI is inherently high-risk and should be reserved for situations where human alternatives are unavailable.  

---

**10.** A colleague argues that Plan Mode is most valuable for users unfamiliar with AI, but experienced users can skip it because they intuitively know how to guide a model to a correct output. Evaluate this claim.

&nbsp;&nbsp;&nbsp;&nbsp;A. The claim is valid — experienced users have internalized planning heuristics and can execute them mentally without a formal phase.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The claim is partially valid — Plan Mode is only necessary when the user lacks domain expertise in the subject matter of the task.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The claim inverts the actual risk: more capable AI produces more sophisticated, voluminous, convincing output in the wrong direction before errors surface. Prompt expertise does not eliminate foundational misalignment — it only makes flawed output arrive faster and look more credible. Plan Mode is most critical precisely when AI capability and task stakes are both high.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The claim is correct for most tasks but incorrect for code generation, where compilers and tests independently surface errors regardless of planning.  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | B | The AI executed correctly against the brief it received — "business professional" mapped by default to middle management, an assumption never challenged before execution. This is the compounding error problem: a small misalignment at the start became a foundational error by completion. The AI succeeded at the wrong task because the gap between what was asked and what was meant was never closed. |
| 2 | B | The read-only constraint forces the AI's assumptions and decision points into the open before they are embedded in completed work. Most damage in a bad AI output happens invisibly — assumptions filled silently, choices made without flagging. The constraint converts invisible decisions into visible ones that can be evaluated and corrected before they become locked into the work. |
| 3 | C | Approving a plan creates a mutual agreement on scope, sequence, and assumptions. The omitted audience was a gap in the plan that the consultant confirmed as complete. This is diagnostic of the planning phase: the plan was approved without scrutinizing whether all relevant stakeholders were represented. The AI executed faithfully against what was agreed upon. |
| 4 | D | The complexity-irreversibility framework identifies Plan Mode as warranted when tasks are both complex and hard to undo. Task B is high on both dimensions: multi-stakeholder strategic scope and a $2M decision with long-term consequences. Task A is low on both — simple and trivially correctable. Applying Plan Mode uniformly regardless of these variables wastes planning overhead on work that does not require it. |
| 5 | B | The two-phase split allocates model capability where it delivers the most value. Planning requires deep reasoning across multiple considerations simultaneously — this is where model quality differences are most consequential. Execution against an approved plan is a more bounded task a capable lighter model handles well at lower cost and higher speed. The handoff is the strategic feature, not the inefficiency. |
| 6 | B | Plans for recurring tasks improve through iteration — each execution tests the plan against real work, exposes a category of error, and produces a refinement. After sufficient iterations, the plan has been validated across every scenario it has encountered. Individual learning compounds into organizational-level institutional knowledge: a framework that works reliably at scale because it has earned that reliability through repeated refinement. |
| 7 | B | For high-stakes, high-complexity decisions, the ratio of planning to execution time among professionals — architects, surgeons, lawyers, consultants — is often one-to-one or greater. The planning phase on these engagements is not preparation for the work; it is the work that determines whether execution produces the intended outcome. A plan that does not hold up under scrutiny before execution would have produced a costly failure during it. |
| 8 | B | In a multi-agent workflow, the plan is the coordination substrate. It defines each agent's scope, required inputs, and expected output format — making handoffs explicit and auditable. Without a plan, agents receive ambiguous inputs and produce outputs of undefined format, leaving the next agent with no reliable basis for its work. The plan transforms an ad-hoc chain into a repeatable production system. |
| 9 | B | The surgeon analogy establishes that preparation time before acting is not overhead — it is the work that makes execution safe and effective. Skipping it to move faster trades a small upfront investment for a high probability of a hard-to-reverse failure. The same principle governs AI-assisted work: moving to execution without a planning gate does not save time when foundational errors must be torn down and rebuilt from scratch. |
| 10 | C | The claim inverts the actual risk profile. The more capable the AI, the more polished, voluminous, and convincing its output — even when built on a flawed foundation. An experienced prompter who skips planning does not eliminate foundational misalignment; they accelerate the production of sophisticated work in the wrong direction. Plan Mode is most critical when AI capability is high and task stakes are high — the exact conditions where experienced users are most likely to feel they can skip it. |
