# Chapter 1 Quiz: AI Basics — The Foundation Everyone Skips
*Florida Atlantic University — Graduate Course Assessment*

**Instructions:** Select the best answer for each question.

---

**1.** Which statement best describes what a large language model IS?

&nbsp;&nbsp;&nbsp;&nbsp;A. A database that stores and retrieves factual information on demand  
&nbsp;&nbsp;&nbsp;&nbsp;B. A statistical system trained on text that develops reasoning, generation, and synthesis capabilities across billions of parameters  
&nbsp;&nbsp;&nbsp;&nbsp;C. A search engine that ranks and summarizes web content in real time  
&nbsp;&nbsp;&nbsp;&nbsp;D. A rule-based expert system that applies predefined logic to structured inputs  

---

**2.** A marketing director asks an AI for help crafting a campaign strategy. The response is polished but completely generic — it could apply to any company in any industry. What is the most accurate diagnosis of this failure?

&nbsp;&nbsp;&nbsp;&nbsp;A. The model lacks sufficient intelligence to handle strategic work  
&nbsp;&nbsp;&nbsp;&nbsp;B. The model does not have access to the internet  
&nbsp;&nbsp;&nbsp;&nbsp;C. The model has the intelligence but was never given the knowledge — company context, customer data, and goals were absent from the prompt  
&nbsp;&nbsp;&nbsp;&nbsp;D. The model's training cutoff is too old to produce relevant marketing advice  

---

**3.** The Flashlight Theory describes how AI performance depends on context. Which of the following is the most accurate statement of what the theory claims?

&nbsp;&nbsp;&nbsp;&nbsp;A. Smaller, more focused models outperform larger models on specialized tasks  
&nbsp;&nbsp;&nbsp;&nbsp;B. A highly capable mind in a dark room can only reason about what the flashlight illuminates — the quality of outputs depends on what context has been placed in front of the model  
&nbsp;&nbsp;&nbsp;&nbsp;C. AI models perform best when given fewer instructions so they can reason independently  
&nbsp;&nbsp;&nbsp;&nbsp;D. The "flashlight" represents the model's training data, which cannot be expanded by the user  

---

**4.** What is the page-and-prompt pattern?

&nbsp;&nbsp;&nbsp;&nbsp;A. Submitting the same prompt multiple times and selecting the best response  
&nbsp;&nbsp;&nbsp;&nbsp;B. Writing a one-page brief before beginning any AI session  
&nbsp;&nbsp;&nbsp;&nbsp;C. Finding the relevant document or reference, pasting it into the conversation, and then asking your question — so the model has both the illuminated reference and the specific task  
&nbsp;&nbsp;&nbsp;&nbsp;D. Splitting a large document into individual pages and prompting the model on each separately  

---

**5.** A content strategist is estimating how many tokens a 3,000-word report will consume before submitting it to an AI tool. Using the standard rule of thumb, what is the best estimate?

&nbsp;&nbsp;&nbsp;&nbsp;A. Approximately 1,000 tokens  
&nbsp;&nbsp;&nbsp;&nbsp;B. Approximately 2,000 tokens  
&nbsp;&nbsp;&nbsp;&nbsp;C. Approximately 4,000 tokens  
&nbsp;&nbsp;&nbsp;&nbsp;D. Approximately 6,000 tokens  

---

**6.** Why do output tokens consistently cost more than input tokens on AI platforms?

&nbsp;&nbsp;&nbsp;&nbsp;A. Output tokens are stored permanently in the model's memory, increasing infrastructure costs  
&nbsp;&nbsp;&nbsp;&nbsp;B. Generating text requires an iterative, token-by-token process that is computationally more intensive than reading the input in a single forward pass  
&nbsp;&nbsp;&nbsp;&nbsp;C. Providers charge more for output to discourage users from requesting long responses  
&nbsp;&nbsp;&nbsp;&nbsp;D. Output tokens include the re-sent conversation history, making each response longer than it appears  

---

**7.** What is the context window?

&nbsp;&nbsp;&nbsp;&nbsp;A. The period of time during which a conversation remains active before it expires  
&nbsp;&nbsp;&nbsp;&nbsp;B. The number of response options the model evaluates before selecting an output  
&nbsp;&nbsp;&nbsp;&nbsp;C. The maximum amount of information — measured in tokens — that the model can hold in working memory at one time during a session  
&nbsp;&nbsp;&nbsp;&nbsp;D. The user interface panel that displays conversation history on screen  

---

**8.** An operations analyst pastes a 150-page process manual into an AI conversation and asks a question that depends on a section near page 75. The answer comes back noticeably weaker than responses about material from the first and last sections of the document. What phenomenon explains this?

&nbsp;&nbsp;&nbsp;&nbsp;A. The context window was exceeded, so the middle content was silently truncated  
&nbsp;&nbsp;&nbsp;&nbsp;B. The model applies stricter content filters to dense technical documents  
&nbsp;&nbsp;&nbsp;&nbsp;C. The "lost in the middle" problem — models attend most strongly to content near the beginning and end of long contexts, with reduced attention to material in the center  
&nbsp;&nbsp;&nbsp;&nbsp;D. The middle pages contained formatting characters that confused the tokenizer  

---

**9.** Which of the following is the best description of context rot?

&nbsp;&nbsp;&nbsp;&nbsp;A. The degradation of a model's performance over time as its training data becomes outdated  
&nbsp;&nbsp;&nbsp;&nbsp;B. The gradual decline in output quality that occurs as a long conversation accumulates attention dilution, conflicting instructions, and goal drift  
&nbsp;&nbsp;&nbsp;&nbsp;C. A security vulnerability in which prior conversation data leaks into unrelated sessions  
&nbsp;&nbsp;&nbsp;&nbsp;D. The tendency of models to repeat cached responses rather than generating fresh ones in long threads  

---

**10.** A product manager has been iterating on a proposal with an AI for 25 messages. She notices the model is now suggesting ideas it already proposed six turns ago and ignoring a formatting constraint she specified at the start. She decides to add a long corrective prompt to get things back on track. Which of the following is the most professionally sound response to this situation?

&nbsp;&nbsp;&nbsp;&nbsp;A. Switch to a more capable model tier, as performance degradation signals the current model is insufficient for the task  
&nbsp;&nbsp;&nbsp;&nbsp;B. Increase the specificity of subsequent prompts to override the accumulated noise in the context  
&nbsp;&nbsp;&nbsp;&nbsp;C. Distill the current goal, key decisions, and constraints into a clean summary, then open a fresh conversation with that summary at the top  
&nbsp;&nbsp;&nbsp;&nbsp;D. Re-send the original formatting constraint verbatim so it appears more recently in the context  

---

## Answer Key

| Q | Answer | Rationale |
|---|--------|-----------|
| 1 | B | An LLM is not a database, search engine, or rule-based system. It is a system trained on massive text corpora that develops emergent reasoning and generation capabilities through predicting tokens across billions of parameters. (Ch. 1.1) |
| 2 | C | This is the intelligence vs. knowledge distinction in action. The model's reasoning capability is intact; what it lacked was the specific knowledge — company context, goals, and constraints — that only the user can supply. Generic input produces generic output. (Ch. 1.1) |
| 3 | B | The Flashlight Theory holds that context is the beam illuminating what the model can reason about. The quality of the model (the 180-IQ mind) is fixed; what varies is how well the user aims the light. Options A, C, and D each misrepresent the theory. (Ch. 1.2) |
| 4 | C | The page-and-prompt pattern has three steps: find the relevant document, paste it in, then ask the question. It works because it expands the flashlight beam to include the exact information the model needs. (Ch. 1.2) |
| 5 | C | The rule of thumb is ~750 words ≈ 1,000 tokens. A 3,000-word report is 4× 750 words, yielding approximately 4,000 tokens. (Ch. 1.5) |
| 6 | B | Generating text is computationally more intensive because the model runs an iterative, token-by-token generation process — far more resource-intensive than the single forward pass used to read the input. Output tokens typically cost 2–5× more than input tokens. (Ch. 1.6) |
| 7 | C | The context window is the model's working memory for a session — the maximum token volume it can hold and attend to at one time. It is not a time limit, a UI element, or an evaluation count. (Ch. 1.7) |
| 8 | C | The "lost in the middle" problem is the empirically observed tendency for models to attend most strongly to content near the beginning and end of long contexts. Information buried in the center receives less attentional weight, producing weaker responses. (Ch. 1.7) |
| 9 | B | Context rot is the gradual quality degradation in long conversations — caused by attention dilution, accumulated assumptions, conflicting instructions, and goal drift. It is not model aging, a security issue, or a caching artifact. (Ch. 1.9) |
| 10 | C | The professionally sound response to context rot is to distill, not patch. Writing a clean summary (current goal, key decisions, constraints) and opening a fresh conversation resets the attentional slate without losing the work done so far. Adding corrective prompts to a rotted context compounds the noise rather than resolving it. (Ch. 1.9) |
