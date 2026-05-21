# Chapter 5 Quiz: The Six Engineering Disciplines

**Instructions:** Choose the best answer for each question.

---

## Question 1

According to Chapter 5, which of the following best explains why two people using the exact same AI model can produce dramatically different results?

A. One person has a faster internet connection and experiences less latency.
B. One person has mastered more of the six engineering disciplines, which layer and compound on each other.
C. One person is paying for a higher subscription tier that unlocks more model capability.
D. One person asks more questions per session, giving the AI more data to learn from.

---

## Question 2

The chapter uses the metaphor of a "six-story building" to describe the six disciplines. What does this metaphor specifically emphasize?

A. The disciplines are unrelated tools you can pick and choose from independently.
B. Each discipline is equally important, and you should learn them in any order.
C. Most professionals never leave the lobby (prompt engineering), while the real leverage is on the floors above.
D. Harness engineering is the foundation, and prompt engineering sits at the top.

---

## Question 3

The four components of a strong prompt described in the chapter are Task, Context, Format, and Examples. A colleague writes: *"Help me write an email."* Which component is most critically missing from this prompt?

A. Format — the prompt does not specify bullet points vs. prose.
B. Examples — no sample email is provided for style calibration.
C. Task and Context — the specific purpose, audience, and constraints are entirely absent, making the instruction too vague to act on precisely.
D. Nothing is missing; brevity is a virtue in prompt engineering.

---

## Question 4

System prompting is described as "who you are before the conversation begins." Which of the following best captures what a system prompt actually does?

A. It replaces prompt engineering by handling all instructions automatically.
B. It loads silently before every exchange, defining the AI's role, tone, rules, and standing context so you do not have to re-explain yourself in every session.
C. It gives the AI access to the internet and external tools.
D. It stores conversation history between sessions so the AI can remember past chats.

---

## Question 5

Meta prompting is described as "using AI to write the instructions that AI will follow." What is the core reason this technique tends to produce better instructions than writing them yourself?

A. AI can access databases of expert-written prompts and combines the best ones.
B. The process of having AI interview you surfaces gaps, vague assumptions, and missing context that you would typically overlook when writing instructions yourself.
C. AI writes faster, so meta prompting is primarily a time-saving technique rather than a quality improvement.
D. Meta prompting bypasses the context window limit, allowing more information to be processed.

---

## Question 6

The chapter states: "More context is not always better." Which of the following best explains this counterintuitive claim?

A. AI models perform worse when they receive more than three documents at once.
B. Long documents cause the AI to hallucinate more frequently.
C. The AI's context window is finite; filling it with irrelevant information reduces the capacity available for what actually matters, degrading output quality.
D. Adding too much context makes the AI overly cautious and less creative.

---

## Question 7

According to the chapter's discussion of context engineering, which of the following practices would most improve output quality for a complex, long-running task?

A. Keep all your work in one continuous conversation so the AI retains the full history.
B. Deliberately assemble only the relevant documents, structure the framing early in the conversation, and start a fresh session when the conversation has drifted too far from its purpose.
C. Avoid attaching documents; instead, summarize everything in plain text in the prompt.
D. Ask the AI to ignore previous messages and focus only on the final question.

---

## Question 8

Memory engineering addresses "AI's dirty secret." What is that secret, and what is the minimum viable practice the chapter recommends to address it?

A. AI secretly stores your conversations for training; the fix is to delete chat history regularly.
B. AI cannot process images natively; the fix is to convert all visuals to text descriptions.
C. AI has no native long-term memory — every conversation starts at zero; the minimum fix is maintaining a one-page "Working Brief" document about yourself and attaching it at the start of important sessions.
D. AI models degrade over time without retraining; the fix is to switch models every few months.

---

## Question 9

The chapter describes three layers of AI memory. Which layer enables "genuinely autonomous AI workflows that accumulate knowledge over time" and is the most powerful?

A. Conversation memory — the automatic in-session context the AI has access to.
B. File-based memory — documents you paste or attach at the start of each session.
C. Database memory — structured, queryable, persistent storage (e.g., Supabase) that the AI can read from and write to across any number of conversations.
D. Model fine-tuning — retraining the AI on your personal data.

---

## Question 10

The harness engineering example in the chapter — where an AI reads an inbound client email, searches Drive for prior documents, checks the calendar, drafts a reply, and places it in Gmail drafts — illustrates which key principle?

A. Harness engineering is only valuable for email management tasks.
B. Harness engineering wires all six disciplines together into workflows that operate with minimal ongoing input, changing the fundamental ratio of your time to your output.
C. Harness engineering replaces the need for system prompting and context engineering once it is set up.
D. Harness engineering is the easiest discipline to learn because it requires no prompt writing.

---

## Answer Key

1. **B** — The chapter's central thesis is that output quality differences stem from which disciplines have been mastered, not model access, speed, or subscription level.

2. **C** — The "lobby" metaphor explicitly positions prompt engineering as just the entry point, with compounding leverage available on the five floors above it that most professionals never reach.

3. **C** — Task and Context are the most critical missing elements. The prompt specifies neither what kind of email, who it is for, the situation, nor the desired outcome — all of which are necessary for a precise, usable result.

4. **B** — The system prompt is described as a silent, persistent briefing that loads before every exchange, analogous to orienting a new executive assistant on day one so you never have to re-explain yourself.

5. **B** — The chapter explicitly states that the hardest part of writing good instructions is knowing what to include. The AI's interview process surfaces gaps and vague assumptions the human writer would not notice on their own.

6. **C** — Context windows are finite working memory. Irrelevant information consumes space that could hold relevant information, reducing the model's effective capacity for the actual task.

7. **B** — The chapter covers all three principles: curate relevant context, put framing early, and start fresh when conversation has drifted — rather than accumulating indefinitely in one thread.

8. **C** — The chapter calls AI's lack of native long-term memory its "dirty secret" and recommends a living one-page Working Brief as the minimum viable workaround.

9. **C** — Database memory (e.g., Supabase) is described as the most powerful layer because it enables structured, persistent knowledge that accumulates across unlimited sessions and supports autonomous workflows.

10. **B** — The example is used to illustrate harness engineering's defining characteristic: workflows that run automatically and deliver output with minimal human involvement, fundamentally changing the leverage ratio of a professional's time.
