# Chapter 1 Quiz: AI Basics — The Foundation Everyone Skips
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** A marketing director pastes her company's full 80-page brand guidelines into an AI conversation, then asks: *"What tone should I use for a press release about our new product launch?"* The response is generic and ignores several explicit tone rules buried in the middle of the document. What is the most likely explanation — and the correct intervention?

&nbsp;&nbsp;&nbsp;&nbsp;A. The model lacks the capability to process brand documents; she should switch to a more powerful model tier.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The relevant tone guidelines were likely buried in the middle of the document, where model attention is weakest; she should excerpt and place that section immediately before her question.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The model's training data doesn't include brand voice concepts, so no amount of additional context will help.  
&nbsp;&nbsp;&nbsp;&nbsp;D. She should break the press release task into smaller sub-questions to avoid overloading the context window.  

---

**2.** A consultant receives a strong AI-generated analysis on Monday using a detailed, well-structured prompt. By Friday, in the same conversation thread after 35 additional exchanges, she asks nearly the same question and receives a shallow, contradictory response. She has not changed models or subscription plans. What is the most defensible diagnosis?

&nbsp;&nbsp;&nbsp;&nbsp;A. The model provider pushed an update between Monday and Friday that changed the model's behavior.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Context rot has degraded output quality — accumulated history, conflicting instructions, and goal drift have collapsed the signal-to-noise ratio of the conversation.  
&nbsp;&nbsp;&nbsp;&nbsp;C. She exceeded the context window's hard token limit, which caused the model to revert to default behavior.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The model requires a periodic re-authentication to maintain session performance across multiple days.  

---

**3.** An operations analyst must decide whether to continue a 40-exchange AI conversation or start a fresh one. The thread contains early format instructions, several mid-conversation pivots to new sub-topics, and growing repetition in recent responses. Which principle should govern her decision?

&nbsp;&nbsp;&nbsp;&nbsp;A. She should always continue existing conversations — starting fresh means losing all accumulated context.  
&nbsp;&nbsp;&nbsp;&nbsp;B. She should continue only if output quality is still high and goals remain coherent; otherwise she should distill key conclusions into a clean summary and open a new conversation.  
&nbsp;&nbsp;&nbsp;&nbsp;C. She should start fresh whenever a conversation exceeds 20 exchanges, regardless of current output quality.  
&nbsp;&nbsp;&nbsp;&nbsp;D. She should copy and re-paste the entire prior conversation into a new chat to preserve continuity while resetting attentional bias.  

---

**4.** A manager compares three approaches for a high-stakes strategic analysis: (A) a frontier-tier model with a vague one-sentence prompt; (B) a balanced-tier model with a well-structured, context-rich prompt including role, constraints, and relevant data; (C) a speed-tier model with a minimal prompt. What does the intelligence vs. knowledge framework predict about the relative output quality?

&nbsp;&nbsp;&nbsp;&nbsp;A. Approach A will produce the best output — frontier models have sufficient reasoning capability to compensate for vague prompts.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Approach C is adequate for most strategic tasks because speed-tier models have access to the same training data.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Approach B will likely outperform A — well-supplied, relevant knowledge activates a capable model's reasoning more effectively than raw model tier alone.  
&nbsp;&nbsp;&nbsp;&nbsp;D. All three approaches will produce equivalent output because the intelligence ceiling is the binding constraint, not context quality.  

---

**5.** A legal team is evaluating AI-assisted contract review for a multilingual portfolio — contracts in English, Japanese, and Arabic at roughly equal volume. They need to set a monthly token budget. Which factor is most critical to accurate cost planning?

&nbsp;&nbsp;&nbsp;&nbsp;A. Non-English scripts tokenize less efficiently than English, so Japanese and Arabic contracts will consume significantly more tokens per page and carry higher processing costs per unit of content.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Token costs are language-neutral; once word counts are known, budget planning is straightforward.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The team should translate all documents to English before processing to reduce token costs, since translation is computationally cheaper.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Input token costs for multilingual documents are negligible; only output token costs require careful budgeting.  

---

**6.** A product manager's AI conversation spans 40 messages. By the final messages, the model is re-explaining concepts it covered in message 5 and contradicting output specifications she locked in at message 1. Which structural property of AI conversations most directly explains this degradation?

&nbsp;&nbsp;&nbsp;&nbsp;A. The model has a hard session limit that resets working context every 15–20 messages.  
&nbsp;&nbsp;&nbsp;&nbsp;B. LLMs are stateless — each new message re-sends the full conversation history, and as that history accumulates, early instructions compete for attention against a growing volume of later content.  
&nbsp;&nbsp;&nbsp;&nbsp;C. High message frequency within a session triggers a cost-reduction mode in which the provider substitutes a smaller model.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Conversations with frequent topic pivots are flagged by the platform and receive reduced processing priority.  

---

**7.** An executive drafts a 900-word context brief covering her company's full history, all current projects, team roster, and personal background. A colleague recommends trimming it to 150–200 focused words covering only her current role, active project, and output preferences. What principle most strongly supports the colleague's recommendation?

&nbsp;&nbsp;&nbsp;&nbsp;A. AI providers penalize prompts that exceed 500 words, resulting in lower-quality outputs by design.  
&nbsp;&nbsp;&nbsp;&nbsp;B. A well-curated, high-signal context consistently outperforms a bloated one — irrelevant information dilutes the signal-to-noise ratio and competes with what actually matters for the task at hand.  
&nbsp;&nbsp;&nbsp;&nbsp;C. The colleague is incorrect; more context always produces better outputs because the model has a larger information base to draw from.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Longer context briefs automatically trigger the lost-in-the-middle problem, causing the model to discard the entire document.  

---

**8.** A CFO asks an AI: *"How should we manage Q4 cash flow?"* and receives a generic textbook response about receivables cycles. She then pastes in her current balance sheet, 90-day receivables aging report, and payroll calendar before asking the same question. The second response is specific, ranked, and immediately actionable. Which explanation best accounts for the difference?

&nbsp;&nbsp;&nbsp;&nbsp;A. The second prompt used more precise financial vocabulary, which activated the model's specialized finance module.  
&nbsp;&nbsp;&nbsp;&nbsp;B. The model's intelligence was unchanged; what changed is that specific, relevant knowledge was supplied — extending the flashlight beam to include exactly what was needed for targeted analysis.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Pasting structured financial documents causes the model to run a distinct inference process optimized for numerical reasoning.  
&nbsp;&nbsp;&nbsp;&nbsp;D. The model learned from the first inadequate response and self-corrected on the second attempt using reinforcement signals.  

---

**9.** A researcher argues that voice input for AI work is primarily valuable because it is faster than typing. A colleague counters that the deeper benefit is qualitative. Which evidence most directly supports the colleague's position?

&nbsp;&nbsp;&nbsp;&nbsp;A. Voice transcription accuracy is now equivalent to typing accuracy, making them interchangeable in terms of output quality.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Dictated content is consistently longer, more nuanced, and contains more contextual qualifications than typed content — and richer prompts produce qualitatively better AI outputs, independent of the speed advantage.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Voice tools cost less to operate than text interfaces, making them the cost-optimal channel for high-frequency AI use.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Voice input bypasses the context window entirely, enabling prompts of unlimited length.  

---

**10.** An organization is designing an enterprise AI usage policy to maximize output quality while managing costs as volume scales. Which combination of practices is most coherent with the principles developed across Chapter 1?

&nbsp;&nbsp;&nbsp;&nbsp;A. Maximize prompt length for every task; use frontier models exclusively; never start a new conversation to avoid losing context continuity.  
&nbsp;&nbsp;&nbsp;&nbsp;B. Curate context to a high signal-to-noise ratio; match model tier to task complexity; reset conversations when quality degrades with a distilled clean summary; constrain output length when depth is not required.  
&nbsp;&nbsp;&nbsp;&nbsp;C. Keep all prompts minimal to reduce input token costs; rely on the model's general training knowledge rather than supplying task-specific context; use speed-tier models for all tasks.  
&nbsp;&nbsp;&nbsp;&nbsp;D. Use the context window at maximum capacity for every task; prioritize output quantity; rotate model providers weekly to benchmark performance.  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | B | The lost-in-the-middle problem predicts that information buried in the center of a long document receives less model attention; the correct fix is to excerpt the critical section and place it near the question. |
| 2 | B | The four mechanisms of context rot — attention dilution, accumulated assumptions, conflicting instructions, and goal drift — collectively explain the quality degradation without requiring any external model change. |
| 3 | B | The professional standard is output-quality-driven, not length-driven: continue if quality holds; distill and reset when warning signs appear, preserving insights while discarding accumulated noise. |
| 4 | C | The intelligence vs. knowledge framework predicts that supplied knowledge is the binding variable; a well-briefed capable model will typically outperform an under-briefed frontier model on the same task. |
| 5 | A | Non-Latin-script languages tokenize less efficiently than English — Japanese and Arabic text may require 2–3× more tokens per equivalent unit of meaning, making script composition a material cost variable at scale. |
| 6 | B | LLMs are stateless: every turn re-sends the full conversation history as input, and as that history grows, early instructions face increasing attentional competition from later content — the direct structural cause of the described degradation. |
| 7 | B | The signal-to-noise principle holds that a tightly curated context consistently outperforms a bloated one containing the same core information buried in irrelevant background that the model must filter. |
| 8 | B | The flashlight analogy precisely explains this outcome: the model's intelligence was unchanged; what changed is the knowledge supplied — specific financial documents extended the beam and enabled targeted, actionable analysis. |
| 9 | B | Research on dictated content shows it is longer and more nuanced than typed content; the chapter explicitly identifies this qualitative enrichment — richer prompts producing richer outputs — as the deeper benefit, not merely speed. |
| 10 | B | This option synthesizes Chapter 1's core frameworks: context curation (signal-to-noise), model-tier matching (smartphone analogy), conversation management (context rot discipline), and output constraints (token economy). |
