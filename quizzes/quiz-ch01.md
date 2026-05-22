# Quiz: Chapter 1 — AI Basics: The Foundation Everyone Skips

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 1, what is the *single most important concept* in the entire book — the distinction the chapter says explains "every failure you've ever had with an AI tool"?

- A) The distinction between open-source and closed-source models
- B) The distinction between intelligence (what the model brings) and knowledge (what you must bring)
- C) The distinction between input tokens and output tokens
- D) The distinction between training and fine-tuning
- E) The distinction between voice and text interfaces

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter does mention open-weight models, but never frames the open/closed distinction as the core equation that explains AI failures.
- ⭐ B) ✅ The chapter's "Core Equation" admonition states: "What the model brings → Intelligence (reasoning, synthesis, generation). What you must bring → Knowledge (context, data, goals, constraints). Every failure you've ever had with an AI tool can be traced to a gap in this equation."
- C) ❌ Input vs. output tokens is covered in Chapter 1.5 as a cost lever, not as the central conceptual frame.
- D) ❌ The chapter does not focus on training methodologies. The book has "no engineering prerequisites."
- E) ❌ Voice is the topic of Chapter 1.10 but is presented as an interface choice, not as the core conceptual divide.

</details>

---

## Question 2

The chapter introduces the **Flashlight Theory** (credited to Matty Squarzoni). Which TWO statements correctly describe what the theory says?

- A) A 180-IQ mind sits in a pitch-dark room — context is the flashlight, and the model can only reason about what the beam illuminates
- B) "The AI is bad at this" is almost always wrong — the more accurate diagnosis is "the room was dark"
- C) The flashlight metaphor explains why bigger models are always better than smaller ones
- D) The flashlight beam is a metaphor for the GPU memory available to the model
- E) The Flashlight Theory argues that AI should be replaced with simpler keyword search

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Picture a 180-IQ mind locked in a pitch-dark room... Whatever that flashlight illuminates, the mind can work with brilliantly. Whatever stays in the dark might as well not exist... This is the Flashlight Theory."
- ⭐ B) ✅ The chapter states: "When an AI gives you a poor output, the first instinct is often to blame the model... The Flashlight Theory dissolves this complaint almost entirely. The model isn't bad at your task. The room is dark."
- C) ❌ The chapter never claims model size is the determinant — it consistently argues that the quality of context (the beam) determines results.
- D) ❌ The chapter explicitly defines the flashlight beam as *context* (prompt, files, history, tool results), not GPU memory.
- E) ❌ The chapter argues the opposite: the model is a "reasoning partner," not a search engine to be replaced by keywords.

</details>

---

## Question 3

The chapter contrasts two consultants, Carlos and Priya. What is the central lesson?

- A) Carlos is using a less capable model than Priya
- B) Priya brings a flashlight (a 20-minute context file with the client's situation, goals, and dynamics) while Carlos brings only queries — same model, dramatically different output quality
- C) Senior consultants like Priya always outperform junior consultants
- D) AI works better in the morning, when Priya does her best work
- E) Carlos was using an older subscription tier of the same product

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly says the two use "the same model." Capability is not the variable.
- ⭐ B) ✅ The chapter states: "Before every client engagement, she spends 20 minutes creating a context file: the client's situation, their stated goals, the three questions the engagement needs to answer, the political dynamics she has observed... Carlos brings a query. Priya brings a flashlight."
- C) ❌ The chapter does not specify seniority. The difference is structural input quality, not seniority.
- D) ❌ Time of day is never mentioned in the example.
- E) ❌ Subscription tiers are not the variable. Both use the same tool — what changes is the context.

</details>

---

## Question 4

The chapter introduces the **page-and-prompt pattern** as "the most effective basic technique in this book." What are the three steps of the pattern?

- A) Open a new chat, set a system prompt, then send a question
- B) Find the relevant page/document, paste it in, then ask your question
- C) Choose the right model, write your question, then upload an image
- D) Use a free tier, validate with a paid tier, then enterprise deploy
- E) Type the question, dictate the question, then compare the outputs

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ This is close to "system prompting" but not the page-and-prompt pattern. The pattern specifically loads a *page* of reference material.
- ⭐ B) ✅ The chapter states: "1. **Find the page** — identify the relevant document, reference, data, or text that the model needs to see. 2. **Paste it in** — place it in the conversation before your question. 3. **Ask your question**."
- C) ❌ Model selection and images are unrelated to the page-and-prompt pattern.
- D) ❌ The free/paid/enterprise progression is not the pattern.
- E) ❌ This describes voice-vs-text comparison, not the page-and-prompt pattern.

</details>

---

## Question 5

According to Chapter 1's section on tokens, which of the following is the correct rule of thumb the chapter uses for English-language text?

- A) Approximately 1 token = 1 word
- B) Approximately 750 words ≈ 1,000 tokens (so 1 token ≈ ¾ of a word)
- C) Approximately 1 token = 1 character
- D) Approximately 10,000 words = 1 token
- E) Tokens and words are equivalent units that are interchangeable

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter says a token "is not a word" and gives the ratio explicitly.
- ⭐ B) ✅ The chapter's "Token Rule of Thumb" admonition states: "~750 words ≈ 1,000 tokens. A typical business email (200 words) ≈ 270 tokens."
- C) ❌ The chapter says a token is "roughly 3–4 characters of text, on average" — not one character.
- D) ❌ This is wildly off the chapter's actual rule of thumb.
- E) ❌ The chapter explicitly distinguishes them: "It is not a word. It is not a letter. It is a statistical chunk."

</details>

---

## Question 6

The chapter explains a pricing asymmetry in the AI "token economy." Which TWO statements correctly describe it?

- A) Output tokens consistently cost more than input tokens (typically 2–5× more) because generation is more computationally intensive than reading
- B) Input and output tokens always cost exactly the same amount
- C) Every message you send re-sends the entire conversation history, so long conversations compound input costs
- D) The model has persistent memory between conversations, eliminating the re-send problem
- E) The cheapest way to reduce cost is to disable the conversation history feature

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "input tokens and output tokens cost different amounts, and output tokens are consistently more expensive... typically 2–5× as much." It explains: "Generating text is computationally more intensive than reading it."
- B) ❌ The chapter is explicit that input and output prices differ. They are not symmetrical.
- ⭐ C) ✅ The chapter's "re-send problem" section states: "every message you send re-sends the entire conversation history... long conversations become expensive quickly, because the input token count grows with every exchange."
- D) ❌ The chapter is explicit that the model is *stateless* — "they have no persistent memory between API calls."
- E) ❌ Disabling history is not a tool the chapter recommends. The recommended cost levers are prompt efficiency, output constraints, and starting fresh conversations.

</details>

---

## Question 7

The chapter describes the **"lost in the middle" problem** with long context windows. According to the chapter, what is the practical implication for prompt design?

- A) Always paste documents in alphabetical order
- B) The model attends less strongly to content placed in the middle of long contexts; place critical instructions and key document sections near the top or close to the question — never bury them in the middle
- C) Always use the smallest model possible to avoid the problem
- D) The model attends equally well to all parts of the context, so placement does not matter
- E) Only use models with context windows under 8,000 tokens

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Alphabetical ordering is never recommended. The hierarchy is about *position* (top, middle, end), not order by letter.
- ⭐ B) ✅ The chapter states: "Research has shown that language models perform significantly worse on tasks that require retrieving information placed in the middle of long contexts... **Practical implication:** If there is a specific section of a long document that is critical to your task, excerpt it and place it explicitly at or near the top of your prompt."
- C) ❌ Model size is not the recommended fix; structural placement of critical content is.
- D) ❌ The chapter explicitly says the opposite: attention is *not* equal across the context.
- E) ❌ The chapter celebrates large context windows for legitimate uses; it never recommends artificially small windows.

</details>

---

## Question 8

Chapter 1.8 introduces the **Three Rules of Context Engineering**. Which TWO statements are among those rules?

- A) Lead with what matters most — your goal, your constraints, the most critical section of a document goes first
- B) Cut anything you wouldn't read yourself — if a paragraph wouldn't meaningfully change your own understanding, it won't help the model either
- C) Always use the most expensive model available
- D) Never paste any documents into a prompt — only reference them by URL
- E) Always include at least 10,000 tokens of background to be safe

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states Rule 1: "Lead With What Matters Most. The most important information — your goal, your constraints, the most critical section of a document — goes first. Not after a long preamble. Not buried. First."
- ⭐ B) ✅ The chapter states Rule 2: "Cut Anything You Wouldn't Read Yourself. If a document, paragraph, or background section would not meaningfully change your own understanding of the task, it will not meaningfully help the model either. Remove it."
- C) ❌ The chapter does not recommend always using the most expensive model. Model choice depends on the task.
- D) ❌ The chapter actively recommends pasting documents (the page-and-prompt pattern). URL-only references contradict this advice.
- E) ❌ The chapter argues the opposite: "More context is not better context... A well-curated 500-token context often outperforms a bloated 5,000-token context."

</details>

---

## Question 9

According to Chapter 1.9 ("Context Rot"), which of the following is the recommended professional response when a conversation starts showing warning signs of rot?

- A) Keep pushing on the conversation with increasingly complex prompts until quality improves
- B) Switch to a different AI provider mid-conversation
- C) Distill the current goal, key decisions, and constraints into a clean summary; open a new conversation; paste the summary in; continue from there
- D) Reduce the temperature setting of the model
- E) Re-paste the entire original document at every new turn

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly warns against this: "They do not keep pushing on a rotted conversation hoping it will get better. They do not try to 'fix' it with increasingly complex prompts."
- B) ❌ Switching providers is never recommended as a fix for context rot — the rot would follow the conversation regardless of provider.
- ⭐ C) ✅ The chapter states: "The professional response to context rot is simple: **start a new conversation**... distilling. Before closing a rotted conversation, spend two to three minutes writing a clean summary of: 1. The current goal, 2. The key decisions made, 3. The relevant constraints. Open a new conversation. Paste that summary at the top."
- D) ❌ Temperature settings are not discussed as a fix for context rot.
- E) ❌ Re-pasting at every turn compounds the problem; it doesn't solve it.

</details>

---

## Question 10

The chapter argues voice input "changes everything." Which TWO statements correctly describe the chapter's reasoning?

- A) Dictated content tends to be longer, richer, and more nuanced than typed content — and AI works better on richer prompts
- B) Speaking to the model invokes natural anthropomorphization, which produces more conversational, context-rich prompts (and the chapter treats this as a *feature* for productive AI work, not a bias to correct)
- C) Voice input is faster than typing because audio compresses to smaller token counts than text
- D) Voice input is only useful for transcribing existing audio files, not for live prompting
- E) The chapter recommends abandoning voice input because it produces lower-accuracy transcriptions than typing

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "Studies on executive communication consistently show that dictated content is longer, contains more qualifications and nuance, and is more likely to include context that the writer would have omitted when typing. For AI, more nuanced context means better outputs."
- ⭐ B) ✅ The chapter states: "Anthropomorphization of AI tools is often treated as a cognitive bias to be corrected. For the purpose of productive AI work, it is a feature. Speaking to the model as if it is a thinking partner produces more natural, more useful interactions."
- C) ❌ Token counts of audio vs text are not the chapter's argument. Both ultimately become text; speed comes from naturalness, not compression.
- D) ❌ The chapter is explicit that the voice tools (SuperWhisper, Wispr Flow) route text "wherever your cursor is" — they are for live prompting, not file transcription.
- E) ❌ The chapter recommends voice input and highlights tools that deliver "high accuracy in near-real-time."

</details>

---

*Quiz for Chapter 1 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
