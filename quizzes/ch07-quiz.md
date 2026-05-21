# Chapter 7 Quiz: Memory — How Your AI Learns You

**Instructions:** Choose the best answer for each question.

---

## Question 1

Why does a large language model have no memory of previous conversations by default?

A. It deletes memories to save server space  
B. It is designed as a stateless system where each session uses a separate, cleared context window  
C. Memory is reserved for paying subscribers only  
D. The AI is programmed to protect your privacy by erasing its own training data  

---

## Question 2

Which of the following best describes "Tier Two: File-Based Memory" in the three-tier memory framework?

A. Automatic in-session recall that disappears when the window closes  
B. A cloud database that stores structured information permanently  
C. A document you maintain about yourself and your work, attached at the start of sessions  
D. A hidden cache built into Claude Desktop that updates automatically  

---

## Question 3

What is the recommended maximum length for an effective memory file?

A. Ten pages, so the AI has rich context  
B. One to two pages  
C. As long as needed — more detail is always better  
D. Exactly 100 words  

---

## Question 4

Which of the following items should NEVER appear in a memory file?

A. Your professional role and title  
B. Key ongoing projects  
C. Passwords and authentication credentials  
D. Communication style preferences  

---

## Question 5

What is the key distinction between **memory** and **context** as defined in Chapter 7?

A. Memory is stored in the cloud; context is stored locally  
B. Memory persists between sessions as a standing brief; context is task-specific information provided within a session  
C. Memory is for personal use; context is for professional use  
D. Memory is automated; context must be purchased through an API  

---

## Question 6

According to the chapter, when should you **update** your memory file? Select the most complete answer.

A. Only when you start a new job  
B. Once a year during annual reviews  
C. When your role changes, a new project becomes a major focus, a key relationship becomes important, or you discover a recurring preference you keep re-explaining  
D. Every single day, regardless of whether anything has changed  

---

## Question 7

What is the primary risk of making a memory file too long and comprehensive?

A. It will cause the AI to crash  
B. It violates AI platform terms of service  
C. It becomes noise — the AI must process irrelevant detail before it can focus on your actual question  
D. Long memory files are automatically deleted by Claude  

---

## Question 8

Which tier of memory requires a connected database (such as Supabase via MCP) and enables the most sophisticated, fully autonomous AI workflows?

A. Tier One: Conversation Memory  
B. Tier Two: File-Based Memory  
C. Tier Three: Database Memory  
D. Tier Zero: Prompt Templates  

---

## Question 9

What does the chapter mean by the "compounding value of memory"?

A. AI tools become cheaper the longer you subscribe  
B. A well-maintained memory file delivers increasing, cumulative returns over time — making AI outputs more calibrated and relevant with each passing month  
C. The AI's model weights improve automatically as you use it more  
D. Memory files earn interest like a savings account  

---

## Question 10

A colleague suggests pasting every relevant project document into a memory file so the AI always has everything it needs. Based on Chapter 7, what is wrong with this approach?

A. Documents cannot be pasted into AI tools  
B. It violates copyright law  
C. A bloated memory file full of every detail acts as noise, not context — memory provides a standing brief, while specific documents should be provided as task-level context within individual sessions  
D. The AI will refuse to read documents longer than one page  

---

## Answer Key

1. **B** — LLMs are stateless systems; each conversation uses a context window that is cleared when the session ends. This is a deliberate design choice, not a flaw.

2. **C** — Tier Two is the file-based memory system: a document you write and maintain, then attach or paste at the start of relevant sessions.

3. **B** — One page is ideal; two pages maximum. A longer document wastes context and forces the AI to parse irrelevant information before addressing your actual request.

4. **C** — Passwords and authentication credentials should never appear in a memory file. The chapter explicitly lists them alongside "truly sensitive personal information" as things that must be excluded.

5. **B** — Memory is the persistent standing brief loaded across sessions. Context is the task-specific material (documents, data, questions) provided within a single session. Neither substitutes for the other.

6. **C** — The chapter identifies role changes, new major projects, newly important relationships, and recurring preferences as the right triggers for updates — not arbitrary time intervals.

7. **C** — An overly long memory file becomes a burden. The AI must process all of it before engaging with your actual question, reducing both speed and quality of output.

8. **C** — Tier Three: Database Memory requires an MCP-connected database (e.g., Supabase) and enables the AI to store and retrieve structured information permanently across all sessions.

9. **B** — The compounding value is accumulative: each refined session improves the memory file, which improves future sessions, creating a widening advantage over time compared to someone starting fresh.

10. **C** — Memory and context are distinct tools. A memory file should be a concise standing brief. Specific documents belong in the session as task-level context. Conflating the two creates an unmanageable, noisy memory file.
