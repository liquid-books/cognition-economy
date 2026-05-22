# Quiz: Chapter 16 — Basal-Cognitive Architecture: The Future Operating Model

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 16, why is "the company is a brain" the wrong metaphor for an AI-augmented organization?

- A) Brains are too slow to keep up with modern AI processing speeds
- B) The brain is one of the rarest organizational forms in nature, not one of the most common, and most successful biological systems organize through distributed sensing and local decisions
- C) Modern AI literally requires a different metaphor because it cannot model brain-like behavior
- D) The brain metaphor was invented by Alfred Sloan in 1956 and only ever applied to General Motors
- E) Brain-style organizations are illegal under new EU AI regulations

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter does not argue brains are too slow — it argues they are structurally wrong for the *type* of work AI enables. Speed is not the issue.
- ⭐ B) ✅ The chapter states: "Three billion years of biological evolution have run an extraordinary experiment in how living systems organize themselves. The result is overwhelmingly clear: most successful biological systems are not hierarchical. The brain is one of the rarest organizational forms in nature, not one of the most common."
- C) ❌ The chapter never claims AI cannot model brain behavior — it argues that organizational design should not be modeled on the brain, which is a separate point.
- D) ❌ Sloan applied the metaphor to GM, but the chapter explicitly states the brain metaphor has been used for organizations "for two centuries" and predates Sloan.
- E) ❌ There is no reference to regulations in this argument. The chapter's case is structural and biological, not legal.

</details>

---

## Question 2

The chapter identifies four predictable failure modes of hierarchical orchestration when AI is bolted onto an existing pyramid. Which TWO of the following are among those failure modes?

- A) Brittleness — a single bad call at the top wastes a thousand executions at the bottom
- B) Cost overruns from buying too many GPUs
- C) Coordination overhead — 60 to 75 percent of compute being spent on context handoffs rather than actual work
- D) Loss of intellectual property to foreign competitors
- E) Inability to comply with data residency laws

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter explicitly lists brittleness as a failure mode: "When the master prompt is wrong, every sub-agent below it inherits the wrongness... The pyramid amplifies errors instead of catching them. One bad call at the top wastes a thousand executions at the bottom."
- B) ❌ GPU cost overruns are not among the four named failure modes. The chapter focuses on architectural, not financial, failures.
- ⭐ C) ✅ The chapter explicitly states: "organizations routinely discover that 60 to 75 percent of their AI compute is being spent on coordination, not cognition. They are paying to organize the work, not to do it."
- D) ❌ IP loss is not discussed as a failure mode of hierarchical orchestration in this chapter.
- E) ❌ Data residency laws are not among the four failure modes. The four named modes are brittleness, drift, propagation errors, and coordination overhead.

</details>

---

## Question 3

What is a "cognitive light cone" as the chapter uses the term, and why does the chapter call it the most important design parameter in AI architecture?

- A) The visible spectrum of light an AI vision model can perceive, which determines image quality
- B) The region of time and space across which an agent can sense, integrate information, and act — and its size determines the size of decisions the unit can make well
- C) A physics concept that has no real application to AI design
- D) The total token budget available to a single agent session
- E) The maximum number of sub-agents an orchestrator can supervise

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter borrows the *physics* concept of light cone, not the visual spectrum. The cognitive light cone has nothing to do with visible light.
- ⭐ B) ✅ The chapter states: "Every agent — biological or artificial — has a cognitive light cone: the region of time and space across which it can sense, integrate information, and act... the size of that cone is determined by you, the designer." The chapter calls this "the single most useful design parameter for AI architecture."
- C) ❌ The chapter is explicit that the concept transfers from physics through cognitive science to AI design, calling it the most useful design parameter.
- D) ❌ Token budget is a related but distinct concept. The cognitive light cone is about what the agent can sense and act on, not just how much text it can process.
- E) ❌ This describes a span-of-control concept from hierarchies, not the cognitive light cone.

</details>

---

## Question 4

The chapter describes the shift from "agent corporations" to "agent tissues." Which TWO statements correctly capture this shift?

- A) Agent corporations use an orchestrator that decomposes tasks and hands chunks to sub-agents; agent tissues use peer agents that coordinate through a shared task board with no orchestrator
- B) Agent corporations are always more accurate than agent tissues because hierarchy reduces ambiguity
- C) In an agent tissue, each agent has its own local context and only escalates upward when local sensing tells it the situation exceeds local authority
- D) Agent tissues require fewer agents than agent corporations to handle the same workload
- E) The agent corporation model was abandoned by every major AI lab by 2023

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "In an agent corporation, there is an orchestrator and there are sub-agents... In an agent tissue, the architecture is inverted. There is no orchestrator. There are peer agents... They coordinate through a shared task board, not a chain of command."
- B) ❌ The chapter argues the opposite — hierarchical agent corporations amplify errors at scale and suffer drift through the layers, making them *less* accurate on open-ended tasks.
- ⭐ C) ✅ The chapter states: "Each agent has its own local context... Each agent senses its environment, makes local decisions, and only escalates upward when local sensing tells it the situation exceeds local authority."
- D) ❌ The chapter never claims tissue architectures use fewer agents. The number of agents is similar — the architecture differs.
- E) ❌ The chapter says "every major AI lab that has tried to build agent corporations has quietly walked away from the architecture," but no specific 2023 date is given. Agent corporations remain useful for bounded tasks.

</details>

---

## Question 5

According to the chapter, which of the following is the **single one-question test** for whether your AI architecture is brain or tissue?

- A) Does your CEO use AI personally on a daily basis?
- B) Do you have more than 100 agents in production?
- C) Can a single agent in your system fail without breaking the whole?
- D) Is your AI vendor on the Forbes Global 2000 list?
- E) Did you spend more than $10 million on AI infrastructure in the last year?

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Executive AI literacy matters, but the chapter does not propose this as the brain/tissue test.
- B) ❌ Scale alone does not determine architecture — you can have 100 agents in either configuration.
- ⭐ C) ✅ The chapter states in "The Tissue Test" admonition: "Here is a one-question test for whether your AI architecture is brain or tissue. Can a single agent in your system fail without breaking the whole? If yes, you are tissue. If a single sub-agent failure cascades into a system failure, you are brain."
- D) ❌ Vendor reputation is irrelevant to the architectural diagnosis the chapter is making.
- E) ❌ Spend has no relationship to the brain/tissue diagnostic. The chapter explicitly notes some of the worst architectures had the largest budgets.

</details>

---

## Question 6

The chapter introduces six dimensions of basal-cognitive architecture. Which dimension is described as "the speed of the system" — the difference between a unit that has to ask permission for every move and one that can act on local signals within its cognitive light cone?

- A) Composability
- B) Locality
- C) Resilience
- D) Observability
- E) Alignment

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Composability is described as "the difference between Lego bricks and a sculpture" — about reusability, not speed.
- ⭐ B) ✅ The chapter states: "Locality is the speed of the system. A unit that has to ask permission for every move is slow regardless of how powerful its underlying model is. A unit that can act on local signals — within its cognitive light cone — is fast and adaptive."
- C) ❌ Resilience is about what happens when a single unit fails, not about speed.
- D) ❌ Observability is "the difference between flying a plane with a cockpit and flying it through a curtain" — about visibility, not speed.
- E) ❌ Alignment is about whether the unit's local objective aligns with the system's global objective — not about speed of execution.

</details>

---

## Question 7

The chapter introduces the principle "design for the smallest unit, then compose." Which TWO statements correctly describe the implications of this principle?

- A) The fractal property of tissue architectures means the same pattern works at one agent, ten agents, or ten thousand agents
- B) You should start by mapping your current org chart and assigning AI to each existing box
- C) The discipline is to ignore the org chart entirely when designing your AI architecture and start with the smallest unit of work that can be done by a single agent within a single cognitive light cone
- D) Composition only works if all agents share the same underlying model from the same vendor
- E) The smallest unit principle only applies to startups under 50 employees

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "When you design your AI systems on tissue principles, you get the fractal property for free. The same patterns you use for a single agent — clean inputs, local context, peer communication, observable state — work for a team of agents."
- B) ❌ This is the opposite of what the chapter recommends. The chapter explicitly warns: "Most companies do the reverse. They design for the org chart they already have, then try to squeeze AI into the boxes. This guarantees the AI inherits all the dysfunctions of the existing hierarchy."
- ⭐ C) ✅ The chapter states: "The discipline is to ignore the org chart entirely when you design your AI architecture. Start with the smallest unit of work that can be done by a single agent within a single cognitive light cone."
- D) ❌ The chapter argues the opposite under the Evolvability dimension — a tissue should be *model-agnostic*, with agents from different models composable together.
- E) ❌ The chapter applies this principle universally and uses the Calder Industries case study (38,000 employees, $14.3B revenue) as the example. There is no size restriction.

</details>

---

## Question 8

The chapter describes a "Robustness Test" with six perturbations. Which of the following correctly describes the "Model Swap" perturbation and what it tests?

- A) Swap the entire vendor and check whether the contract penalty was worth it — tests procurement risk
- B) Replace the underlying model of one agent with a different model and check whether the system continues to function — tests whether the system was tightly coupled to a specific model's behavior
- C) Switch from a language model to a vision model to see if the system can handle multimodal input
- D) Run the system on a different cloud provider to test latency
- E) Use a smaller model to save money and measure how much accuracy drops

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The perturbation is technical, not contractual. The chapter does not discuss vendor procurement penalties as part of the robustness test.
- ⭐ B) ✅ The chapter states: "Replace the underlying model of one of your agents with a different model — same family, different size, or even a different vendor. Does the system continue to function, or do you discover that the system was tightly coupled to the specific behavior of the original model? A tissue is model-agnostic. A brain is hostage to its model."
- C) ❌ The chapter does not describe a modality swap; it specifies same family, different size, or different vendor — all within the language-model class.
- D) ❌ The chapter tests latency in a separate perturbation (Latency Injection), not Model Swap.
- E) ❌ Cost reduction is not the goal of the test. The test is about coupling — whether the system depends on one specific model's quirks.

</details>

---

## Question 9

In the Calder Industries case study, what is the central architectural decision Marcus Vance faces in the March 4, 2026 board meeting?

- A) Whether to acquire a smaller AI-native competitor or build internal capability
- B) Whether to invest in the "Augmented Hierarchy" (adding AI capabilities to every existing box on the org chart while keeping the six-layer pyramid) or the "Tissue Restructure" (dissolving the hierarchy into roughly 240 small semi-autonomous operating units with peer AI agents and no division presidents)
- C) Whether to move the headquarters from Chicago to Silicon Valley
- D) Whether to outsource all AI development to an external vendor
- E) Whether to delay the AI transformation by five years to wait for better technology

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Acquisition is not part of the case study. The decision is internal architecture, not M&A.
- ⭐ B) ✅ The chapter states the two sides explicitly: "the 'Augmented Hierarchy.' Under this plan, Calder would invest $400 million in adding AI capabilities to every existing box on the org chart" versus "the 'Tissue Restructure.' Under their plan, Calder would dissolve the six-layer hierarchy across the next 36 months and reorganize into roughly 240 small, semi-autonomous operating units."
- C) ❌ Headquarters relocation is not part of the case study.
- D) ❌ Outsourcing is not part of the case study. Both options involve internal capability building.
- E) ❌ Delay is not an option presented in the case study. The board has given Vance a five-year window starting now.

</details>

---

## Question 10

The chapter's closing argument restates the book's core thesis. Which TWO statements correctly capture that thesis as expressed in "The End of the Book and the Start of the Career"?

- A) The Industrial Revolution made muscle rentable, and the operators who redesigned around the new leverage built the modern economy
- B) The most important skill in AI is learning to write better prompts
- C) The AI Revolution is making cognition rentable, and the operators who redesign around that leverage will build the next economy
- D) The future belongs to whichever company has the largest AI infrastructure budget
- E) The cognition economy will be dominated by a single AI vendor by 2030

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter restates: "The Industrial Revolution made muscle rentable, and the operators who redesigned around the new leverage built the modern economy."
- B) ❌ Prompts are tactical. The chapter's thesis is about architectural redesign at the organizational level, not prompt quality.
- ⭐ C) ✅ The chapter restates: "The AI Revolution is making cognition rentable, and the operators who redesign around that leverage will build the next one."
- D) ❌ The chapter explicitly rejects budget as the determining factor — the Calder case study and the consulting firm post-mortem both feature the larger-budget player losing to the better-architected player.
- E) ❌ The chapter never predicts vendor consolidation. The Evolvability dimension explicitly argues for model-agnostic architectures specifically to avoid vendor lock-in.

</details>

---

*Quiz for Chapter 16 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
