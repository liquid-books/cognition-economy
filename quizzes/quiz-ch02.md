# Quiz: Chapter 2 — Standing Up Your Cognitive Workshop

**Instructions:** Select the best answer(s) for each question. Some questions have two correct answers. Questions are drawn from the chapter readings and content.

---

## Question 1

According to Chapter 2, what is the relationship between the three tools introduced — Claude Desktop, Gemini, and Google AI Studio?

- A) They are tightly integrated into a single connected system that shares memory across tools
- B) They are three independent products from three different companies — they do not share data, do not talk to each other, and are chosen between based on what you are trying to do
- C) Gemini and AI Studio are the same product accessed through different interfaces
- D) Claude Desktop is the master tool, and the other two are plug-ins for it
- E) All three are made by Google and run on the same underlying model

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit: "they do not share data. They do not talk to each other."
- ⭐ B) ✅ The chapter states: "these three tools are completely independent of each other. They do not share data. They do not talk to each other. They are three separate products from three different companies — and you choose between them based on what you are trying to do, not use them as a connected system."
- C) ❌ The chapter is explicit that Gemini (consumer product) and AI Studio (developer/sandbox) are "entirely different product[s]."
- D) ❌ Claude Desktop is described as "a standalone thinking partner" — not a master tool.
- E) ❌ Claude is made by Anthropic. Only Gemini and AI Studio are Google products.

</details>

---

## Question 2

According to the chapter, the *primary* reason to prefer Claude Desktop over the Claude browser version is:

- A) Claude Desktop runs a more powerful model than the browser
- B) Persistence — the desktop app lets you set a system prompt that loads automatically before every conversation; the browser version does not preserve this across sessions
- C) Claude Desktop is free while the browser version is paid
- D) Claude Desktop has direct access to your Gmail and Drive
- E) Claude Desktop integrates directly with Gemini and AI Studio

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter never claims the desktop runs a more powerful model. Both connect to Claude.
- ⭐ B) ✅ The chapter states: "The reason to prefer the desktop application over the browser version is persistence. The desktop app lets you set a system prompt — a standing set of instructions — that loads before every conversation automatically... The browser version does not preserve this across sessions."
- C) ❌ Cost is not framed as the differentiator; the chapter mentions Claude Pro ($20/month) as the recommended tier.
- D) ❌ The chapter says the opposite: Claude does not connect to your Gmail or Drive — Gemini does.
- E) ❌ The chapter is explicit that the three tools do not connect to each other.

</details>

---

## Question 3

The chapter explains *why* you would use Gemini rather than Claude. Which TWO statements correctly describe Gemini's role in the workshop?

- A) Gemini is preferred when your task touches Google data — Gmail, Drive, Docs, Calendar — because it has native awareness of your Google ecosystem when you ask
- B) Gemini's **Gems** feature lets you save a configuration with its own instructions that load automatically every time you open that Gem — eliminating the need to re-explain context for repeated tasks
- C) Gemini is preferred over Claude for deep reasoning and nuanced writing tasks
- D) Gemini is the master tool that orchestrates Claude and AI Studio
- E) Gemini is faster than Claude because it runs locally on your machine

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter states: "The reason to use Gemini is... it is native to Google's ecosystem... Gemini has awareness of your Gmail, Drive, Docs, and Calendar when you explicitly ask it to use them... Claude cannot."
- ⭐ B) ✅ The chapter states: "A Gem is a saved AI configuration that lives inside Gemini. You give it instructions — a system prompt — and every time you open that Gem, it loads those instructions automatically... You do not explain yourself from scratch every session."
- C) ❌ The chapter explicitly says "Gemini is not a substitute for Claude when you need deep reasoning or nuanced writing." Claude is preferred for that work.
- D) ❌ The chapter never describes Gemini as a master tool; the three are independent.
- E) ❌ Gemini does not run locally — it runs on Google's cloud at gemini.google.com.

</details>

---

## Question 4

Google AI Studio is introduced as a third, distinct tool. According to the chapter, what is the primary thing you must obtain from AI Studio that the rest of the book will rely on?

- A) A monthly subscription receipt
- B) An API key — a unique code that identifies your account and lets other tools connect to Google's AI models on your behalf
- C) A printed certificate of authentication
- D) A new Google account separate from your personal one
- E) Antigravity IDE access

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ A subscription receipt is not mentioned anywhere in the AI Studio setup.
- ⭐ B) ✅ The chapter states: "AI Studio is where you get your access key — a unique code that identifies your account and lets other tools connect to Google's AI models on your behalf. Getting one costs nothing and takes two minutes."
- C) ❌ No certificate is involved; the API key is a copyable text string stored in a password manager.
- D) ❌ The chapter explicitly says "Same Google account" — you do not need a new one.
- E) ❌ Antigravity is referenced only in Tracks B and C of the applied exercise, not as the AI Studio output.

</details>

---

## Question 5

The chapter introduces **meta-prompting** as the recommended way to create a system prompt. What does meta-prompting actually mean, and why does the chapter argue it produces better results than writing the prompt manually?

- A) You hire a professional prompt engineer to write the prompt for you
- B) You describe yourself and your preferences to the AI, the AI interviews you with follow-up questions, and the AI then writes the system prompt — which you paste into the tool's settings
- C) You copy a generic prompt from a public template library without modification
- D) You record yourself describing your job and the prompt is generated from the audio transcript
- E) You write your system prompt in Latin so the model takes it more seriously

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ Hiring a prompt engineer is not what the chapter describes.
- ⭐ B) ✅ The chapter states: "do not write yours yourself. Use the tool to write it. You describe yourself and your preferences — the tool generates the prompt. This is called meta-prompting and it produces dramatically better results than anything written manually." The applied exercise gives the explicit interview script.
- C) ❌ The chapter explicitly recommends a *personalized* interview, not a copied template.
- D) ❌ Audio transcripts are not the mechanism described.
- E) ❌ This is a fabricated tactic not mentioned in the chapter.

</details>

---

## Question 6

The chapter argues that a system prompt should cover four things. Which TWO of the following are explicitly listed as components of a strong system prompt?

- A) Role — what job is this tool doing for you, stated specifically (e.g., "strategic advisor helping a VP of Sales at a B2B software company")
- B) Format — length, structure, headers or not, formal or direct
- C) Salary — what hourly rate you would pay the AI if it were a human
- D) Geographic location — the IP address the model should appear to operate from
- E) Encryption keys — cryptographic material the model uses to sign its outputs

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The chapter lists Role: "What job is this tool doing for you right now? Be specific. 'You are an AI assistant' is useless. 'You are a strategic advisor helping a VP of Sales at a B2B software company preparing for board presentations and customer conversations' is useful."
- ⭐ B) ✅ The chapter lists Format: "Length, structure, headers or not, formal or direct. The tool will follow your format preference consistently if you state it clearly." The four components are Role, Context, Rules, Format.
- C) ❌ Salary is never mentioned as a system prompt component.
- D) ❌ Geographic location/IP is never mentioned in the chapter's system prompt anatomy.
- E) ❌ Encryption keys are not part of a system prompt; this is a fabricated option.

</details>

---

## Question 7

The chapter argues professionals *should* give their AI a persona. According to the chapter, what is the actual definition of a "persona" in this context?

- A) A fictional character name with a backstory (e.g., "Aurora the Wise Witch")
- B) A professional role and a communication style — for example: "You are a senior business analyst. You lead with the most important finding. You are direct and you do not hedge."
- C) A visual avatar shown next to every response
- D) A voice imitation of a famous executive
- E) A legal disclaimer the AI must read before every response

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter explicitly rejects this: "A persona is not a name and a backstory."
- ⭐ B) ✅ The chapter states: "A persona is not a name and a backstory. It is a professional role and a communication style. 'You are a senior business analyst. You lead with the most important finding. You are direct and you do not hedge.' That is a persona. It tells the tool what kind of thinking to apply and how to communicate the result."
- C) ❌ Visual avatars are not mentioned anywhere in the chapter's persona definition.
- D) ❌ Voice imitation is not part of the persona concept.
- E) ❌ Legal disclaimers are not what a persona means in the chapter.

</details>

---

## Question 8

According to the chapter, what is the appropriate use of Google AI Studio in the daily workshop?

- A) As your daily driver for all writing and analysis work
- B) As a sandbox — for experimenting with new capabilities, testing parameters Gemini does not expose (like temperature), and accessing models before they reach the consumer product
- C) As a real-time backup that mirrors every Claude conversation
- D) As the primary place to draft client deliverables
- E) As a calendar and scheduling tool

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The chapter is explicit: "AI Studio is not your daily driver for most tasks. It is a sandbox."
- ⭐ B) ✅ The chapter states: "Use AI Studio when you are experimenting with something new, testing a capability before using it in real work, or accessing model parameters that Gemini does not expose... AI Studio is not your daily driver for most tasks. It is a sandbox."
- C) ❌ The chapter is explicit that the tools do not share data, so this mirroring is impossible.
- D) ❌ The chapter says daily writing work belongs in Claude or Gemini, not in the sandbox.
- E) ❌ AI Studio is not a calendar tool.

</details>

---

## Question 9

In the Meridian Strategy Group case study, two senior partners argued *against* using a configured system prompt — they believed an AI constrained by a system prompt was "by definition less useful than an unconstrained one." According to the chapter, what is the consultant Marcus Trent's *counter-argument*, drawing on the antigravity concept?

- A) Senior partners are usually right about strategic decisions and the firm should defer
- B) A well-configured AI removes friction rather than adding it — it functions like a professional who already understands the context rather than a stranger who must be re-briefed every time; without persistent configuration, AI degrades into a novelty rather than a professional instrument
- C) System prompts make AI run faster on the firm's hardware
- D) System prompts are required by Anthropic's terms of service
- E) Trent agreed with the partners and abandoned the workshop project

<details>
<summary>Show Answer & Explanations</summary>

- A) ❌ The case study explicitly describes Trent disagreeing with the partners — and being right.
- ⭐ B) ✅ The case states: "Trent, drawing on the antigravity concept he had studied — the idea that a well-configured AI *removes friction* rather than adding it, functioning like a professional who already understands the context rather than a stranger who must be re-briefed — argued the opposite: that without persistent configuration, AI degrades into a novelty rather than a professional instrument."
- C) ❌ Hardware speed is not part of the argument.
- D) ❌ No vendor terms-of-service argument is made.
- E) ❌ The case describes Trent's plan being funded for a 30-day pilot, not abandoned.

</details>

---

## Question 10

The Meridian Strategy Group case study identifies a *consistent pattern* in why the firm's first AI initiative produced disappointing results. Which TWO statements describe that pattern?

- A) Consultants treated AI as an on-demand query tool rather than a configured professional environment — opening a browser tab, describing the task minimally, getting generic output, editing heavily, and closing the tab
- B) The AI did not know who Meridian was, did not know what "our voice" meant, and did not know that Diane expected bullet points followed by a single recommendation sentence — because nothing was persisted between sessions
- C) The firm tried to use too many different AI models simultaneously, causing them to interfere with each other
- D) Consultants refused to use AI at all and continued writing everything by hand
- E) The AI replaced 80% of the consultants in the first month, causing morale to collapse

<details>
<summary>Show Answer & Explanations</summary>

- ⭐ A) ✅ The case states: "nearly every consultant was treating AI as an on-demand query tool rather than a configured professional environment. They opened a browser tab, described their task with minimal context, received a generic response, edited it heavily, and closed the tab. The next time they needed AI assistance, they started over — same tool, zero memory, no standing instructions, no persistent configuration."
- ⭐ B) ✅ The case states: "The AI did not know who Meridian was. It did not know what 'our voice' meant. It did not know that Diane expected bullet points followed by a single recommendation sentence, not three pages of hedged analysis."
- C) ❌ The case never says the firm used multiple models that interfered with each other.
- D) ❌ The case is explicit that consultants *did* use AI — just inefficiently.
- E) ❌ The case never mentions AI replacing consultants. The issue was usage quality, not headcount.

</details>

---

*Quiz for Chapter 2 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
