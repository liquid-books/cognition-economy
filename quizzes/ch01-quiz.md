# Chapter 1 Quiz: AI Basics — The Foundation Everyone Skips

**Instructions:** Choose the best answer for each question.

---

## Question 1

According to the Intelligence vs. Knowledge distinction in Chapter 1, which of the following best describes what a large language model (LLM) *brings* to every conversation?

A. Detailed knowledge of your company's strategy, data, and customers  
B. The ability to reason, synthesize, and generate — but not your specific business context  
C. Up-to-date information about current events and recent data  
D. A personalized memory of all your past conversations  

---

## Question 2

The Flashlight Theory, developed by Matty Squarzoni, states that an LLM can only work with what is "illuminated" in the context. What does this imply when an AI gives you a generic, unhelpful answer?

A. The model is not intelligent enough for your task  
B. You should switch to a more expensive model tier  
C. The relevant context was not placed in the beam — the room was still dark  
D. The model's training data is outdated and needs to be refreshed  

---

## Question 3

What is the **page-and-prompt pattern** described in the Flashlight Theory chapter?

A. Writing your prompt on paper before typing it into the AI  
B. Finding the relevant document, pasting it into the conversation, then asking your question  
C. Asking the AI to search the web for a relevant page before answering  
D. Breaking long prompts into pages of 500 words each  

---

## Question 4

AI model tiers are compared to smartphone lines in Chapter 1. Which tier is best suited for complex reasoning, nuanced writing, and deep analysis?

A. Fast / Standard tier (e.g., Claude Haiku, Gemini Flash)  
B. Balanced / Pro tier (e.g., Claude Sonnet)  
C. Frontier / Max tier (e.g., Claude Opus, GPT-4o, Gemini Pro)  
D. Open-weight local models (e.g., Llama, Mistral)  

---

## Question 5

Based on the token rule of thumb introduced in Chapter 1, approximately how many tokens does a 750-word document contain?

A. 100 tokens  
B. 500 tokens  
C. 1,000 tokens  
D. 5,000 tokens  

---

## Question 6

In the token economy, output tokens are consistently priced higher than input tokens. What is the primary reason for this pricing asymmetry?

A. Output tokens are longer and harder to read  
B. Generating text requires iterative processing one token at a time, which is more resource-intensive than reading input  
C. Providers charge a premium because users value responses more than prompts  
D. Output tokens consume more disk storage on the provider's servers  

---

## Question 7

The "re-send problem" in AI conversations refers to which of the following?

A. The need to rephrase your question if the AI gives a wrong answer  
B. The fact that every new message you send re-sends the entire prior conversation history to the model  
C. The model sending duplicate responses when the server is overloaded  
D. The requirement to manually paste context into every new chat session  

---

## Question 8

The **"lost in the middle" problem** refers to a limitation of the context window. Which of the following best describes it?

A. Models forget the beginning of a conversation once it exceeds a certain length  
B. Models tend to attend less to content placed in the center of a long context compared to content at the beginning or end  
C. Tokens in the middle of a word are processed less accurately than tokens at the start  
D. Models ignore documents that are pasted in the middle of a conversation  

---

## Question 9

Which of the following is **NOT** listed as a warning sign of context rot?

A. The model begins repeating suggestions it already gave earlier in the conversation  
B. Responses become more detailed and specific than earlier in the conversation  
C. The model contradicts instructions it was given earlier in the chat  
D. Output quality drops noticeably — responses feel generic or shallow  

---

## Question 10

Chapter 1 recommends **SuperWhisper** and **Wispr Flow** as tools for voice input. Beyond the speed advantage, what is identified as the deeper benefit of using voice to interact with AI?

A. Voice models are cheaper to run than text models, reducing API costs  
B. Voice input bypasses the context window, allowing unlimited prompt length  
C. Spoken prompts naturally include more nuance, context, and detail — leading to better AI outputs  
D. Voice input automatically formats your prompts using the page-and-prompt pattern  

---

## Answer Key

1. **B** — LLMs bring extraordinary intelligence (reasoning, synthesis, generation) but have no access to your specific business knowledge, data, or goals. That context must be supplied by you.

2. **C** — The Flashlight Theory teaches that poor AI outputs almost always mean the room was dark — the relevant context was missing from the beam, not that the model lacks capability.

3. **B** — The page-and-prompt pattern is the foundational technique: find the relevant document or reference, paste it into the conversation, then ask your question. This extends the flashlight beam to include the exact information the model needs.

4. **C** — Frontier / Max tier models (Claude Opus, GPT-4o, Gemini Pro) are the heavyweight reasoners best suited for complex, nuanced, and multi-step tasks. Lower tiers are optimized for speed and volume.

5. **C** — The rule of thumb is ~750 words ≈ 1,000 tokens. This approximation holds for typical English prose and is the key unit for estimating prompt cost and context size.

6. **B** — Output generation is computationally more intensive because the model generates one token at a time in an iterative process, whereas reading input requires only a single forward pass.

7. **B** — Because language models are stateless, every new message must include the full conversation history for the model to maintain continuity. This means turn 11 re-sends turns 1–10 plus the new message, compounding input costs over time.

8. **B** — Research shows models attend more strongly to content near the beginning and end of a long context, and less to content in the middle. This means critical information buried in the center of a large document may be underweighted.

9. **B** — Becoming *more* detailed and specific is the opposite of context rot. Warning signs are repetition, contradictions, confused goal orientation, and a generic quality drop — all signals that the whiteboard has become too crowded.

10. **C** — The deeper benefit of voice input is qualitative, not just quantitative. Spoken language naturally carries more nuance, context, and detail than typed prompts, which tend to be compressed. Richer prompts produce richer outputs.
