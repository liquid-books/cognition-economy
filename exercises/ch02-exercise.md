# Applied Exercise — Chapter 2: Standing Up Your Cognitive Workshop
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your Workshop in 90 Minutes

This exercise produces a configured workshop. On Track A that means three things: your thinking partner installed and configured, one Gem created and tested, and your sandbox verified with your API key in hand. Tracks B and C build the equivalent configurations on the other two surfaces. Complete one track before moving to Chapter 3.

:::{figure} ../images/ch02-workshop-setup-checklist.png
:label: fig-ch02-checklist
:alt: Cognitive workshop setup checklist for all three tools independently
:width: 80%
:align: center

*Setup Checklist* — Three independent installs. Three separate configurations. Check each one off before you move on.
:::

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a **chat assistant** (Track A — a conversation window, the surface every reader has and the one this chapter's three tools live on); a **terminal agent** that lives inside a development environment (Track B); and an **agent-orchestration workspace** built for delegate-and-review work (Track C). Product names, download links, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch02-companion. The companion page is date-stamped; this book is not.
:::

### Track A — Chat Assistant

#### Part 1: Install and Configure Your Thinking Partner (30 minutes)

**Install:**
1. Download the desktop application (the current link is on the setup sheet at cognitioneconomy.net/ch02-companion)
2. Install it for your operating system
3. Sign in and confirm it opens

**Write your system prompt using meta-prompting:**

Open the app. Paste this exactly:

> *"I want to create a system prompt for you — a standing brief that loads before every conversation. To write it well, I need to interview you. Ask me up to 8 questions, one at a time, to learn: my professional role and industry, my primary goals, the tasks I do most often, how I prefer to receive information, what frustrates me about generic AI responses, and anything I always or never want from you. After the interview, write me a complete system prompt I can paste directly into your settings."*

Answer the questions with specifics, not generalities. The more honest and specific you are about your actual day and actual frustrations, the better the prompt the AI generates.

When it delivers the finished system prompt, read it. Edit anything that does not sound right. Then open the app's standing-instructions setting — the setup sheet has the current menu path — and paste it in.

Every conversation from this point forward starts with that context already loaded.

#### Part 2: Create Your First Gem (30 minutes)

**Sign in:**
Go to gemini.google.com and sign in with your Google account. Nothing to install.

**Choose your use case:**
Look at the last two weeks of your actual work. What task do you do at least three times a week where you currently start from scratch every time? Some common answers:

- Preparing for meetings with someone you just googled
- Drafting responses to emails that need thought but not a lot of time
- Turning messy notes into a clean summary
- Making decisions where you want a structured second opinion
- Analyzing something a competitor said or did

Pick the one that will save you the most time starting Monday.

**Write the Gem instructions using your thinking partner:**
Open your thinking partner and say:

> *"I want to create a Gemini Gem that [describe the task]. My role is [your role]. The input I will typically give it is [what you paste in]. The output I need is [format, length, tone]. Write me a complete system prompt for this Gem."*

Take the output. Create a new Gem, paste in the instructions, name the Gem, and save — the current click-path is on the setup sheet.

Test it immediately with a real example. If the output needs adjustment, refine the instructions once and test again.

**Important:** This Gem has nothing to do with your thinking partner. They do not know about each other. You used one tool as a writing instrument to produce better instructions for another — that is the only relationship between them.

#### Part 3: Set Up Your Sandbox (15 minutes)

Go to aistudio.google.com and sign in.

Create an API key — the setup sheet shows where the button lives — then copy it and store it somewhere safe: a password manager, a locked note, anywhere private. Treat it like a password: don't put it in a shared document or email it to yourself.

Create a new project called **Sandbox**. In the system instruction field, write two or three sentences about who you are and what you do. Upload one document from your actual work — a report, a brief, a proposal — and ask a question about it. Confirm the model reads and responds to your real content correctly.

That is all. Your sandbox is verified.

**Your Submission:** Your submission is your completed system prompt — the one the AI wrote for you during the meta-prompting interview, pasted into your standing instructions. Copy the full text of your system prompt into a document. Write two sentences: (1) what you told the AI about yourself during the interview that led to the most follow-up questions, and (2) what surprised you most about the prompt it generated. Submit the system prompt + those two sentences.

### Track B — Terminal Agent

The terminal agent is the same thinking partner wearing different clothes: instead of a chat window with settings screens, it lives in a development environment and reads its configuration from *files in a folder*. That difference is the lesson of this track — a standing brief you can open, version, and carry is a different mental model from one buried in a settings menu. The current install steps, tool names, and download links are on the companion page (cognitioneconomy.net/ch02-companion); what matters here is which decision each step sets.

1. **Set up the surface.** Install a development environment with an integrated terminal, and install a terminal agent inside it. Both installs are ordinary applications; the exact downloads and the sign-in flow are on the companion page. When the agent greets you with a prompt in the terminal, you are ready. Do not open the environment's agent-orchestration view yet — that is Track C's surface. This track works in the editor-and-terminal view.

2. **Set the scope dial: one working folder.** Create a folder called something like *my-workshop* and start the agent inside it. This is the track's first real decision: a terminal agent's context is anchored to a *place*, not an account. Everything you configure in this folder applies whenever you work here — and nowhere else. If you are unsure how to create the folder, ask the agent; giving you the exact commands for your machine is its job.

3. **Set the standing-brief dial by interview.** Every terminal agent reads a context file — a standing professional brief that loads automatically at the start of each session in the folder. (Each tool has its own standard filename for this file; the current names are on the companion page.) Do not write it by hand. Tell the agent: *"I want to create your context file — a standing professional brief about me that you read automatically at the start of every session in this folder. Interview me with up to 8 questions, one at a time, to learn my professional role, my goals, my most common tasks, my preferences for how information is delivered, and what frustrates me about generic AI responses."* Answer with specifics, not generalities.

4. **Review before you save.** After the interview, ask the agent to write the context file — under 400 words, clear labeled sections — and save it in your workshop folder. Then read every word in the editor's file browser, where it now appears as an ordinary file. Revise anything that does not sound accurate. This is the moment the track teaches: your standing brief is *a file you own*, sitting in a folder you control, in a format any tool can read.

5. **Verify persistence with a fresh session.** End the session, then start a new one in the same folder. Ask about something you are genuinely working on this week — without mentioning anything from the brief. The agent reads the context file before your first message; notice how it responds already knowing your professional situation.

6. **Run the control experiment.** Open an unconfigured chat assistant in your browser and ask the exact same question with no context. The difference in relevance between the two responses is the value of the context file — and the reason file-based configuration is a more powerful memory layer than a settings screen: you can see it, edit it, version it, and take it with you.

**Your Submission:** Copy the full text of your context file into a document. Underneath it, paste the response from your Step 5 test session — the first time the agent responded using your standing brief automatically. Write two sentences: (1) what in the response showed that the agent had read your brief without you telling it to, and (2) how does the file-based approach differ from the settings-screen approach in Track A? Submit the context file + test response + two sentences.

### Track C — Ecosystem Assistant + Orchestration Workspace

This track configures two surfaces: a reusable container inside your ecosystem-native assistant (for conversations) and an agent-orchestration workspace (for delegate-and-review work — the surface where you hand a task to an agent, let it work in the background, and review what it brings back). The current tool names, the toggle that opens the orchestration view, and every click-path are on the companion page (cognitioneconomy.net/ch02-companion); what matters here is which decision each step sets.

1. **Open your ecosystem-native assistant** and create a new reusable container — a saved configuration with its own persistent instructions (this chapter's Gems are one example; the current click-path is on the companion page).

2. **Set the persona dial by hand.** In the container's instructions field, write your professional context using this chapter's Role/Context/Rules/Format framework: (a) *Role* — who you are and what job the container is doing for you; (b) *Context* — your industry, your actual day-to-day work, key constraints; (c) *Rules* — how you want responses structured, what you always want, what you never want; (d) *Format* — length, bullets or prose, formal or direct. Aim for 200–300 words. If you want help, open your thinking partner in a separate tab, describe your role and preferences, and ask it to write the instructions — then paste the result in. (The two tools still do not know about each other; one is just a writing instrument for the other.)

3. **Set the naming dial.** Name the container something specific and professional — not "My Assistant" but "Strategy Analyst," "Client Work," or "Sales Prep." Save it. The name is a scope statement: it tells future-you exactly what job this configuration does.

4. **Test against the unconfigured baseline.** Open the container and ask it something you would genuinely ask about a real task this week. Then open a plain new conversation — outside the container — and ask the exact same question. Compare the two responses for relevance and specificity. The difference is what a persistent system prompt buys you.

5. **Open the orchestration workspace.** Now switch surfaces. Open your agent-orchestration workspace and find its manager view — the birds-eye surface for launching and monitoring agents that work asynchronously, in the background, while you do something else. This will be your home base for delegate-and-review work throughout this course.

6. **Set the project-scope dial.** Create a new project and name it after a real piece of work on your plate this week — a client deliverable, a research question, a report. In the project's description field, write three or four sentences: what this project is, who the audience is, and what a good output looks like. That description functions as the standing brief for every task in the project — the same persona decision as Step 2, set at project scope instead of conversation scope.

7. **Delegate your first background task.** Start an asynchronous agent task inside the project. Describe, in plain English, something real and useful — for example: *"Research and write a 400-word summary of the current state of [your industry or topic], highlighting the three most significant recent developments."* Submit it and go do something else. This is the decision the surface exists for: work you hand off rather than supervise.

8. **Review at the approval gate.** When the task completes, open the deliverable the agent produced. Read it critically — for accuracy, for usefulness, for whether the project description shaped it the way you intended. Nothing an agent produces is finished until you have signed off on it. That habit starts now.

**Optional Step 9 — Commission a visual artifact.** If your workshop includes an artifact studio (the surface from earlier in this chapter whose deliverable is a polished visual rather than text — current tool names on the companion page), give it the deliverable from Step 7 and say: *"Turn this into a one-page visual summary I could hand to a client — clear headline, three key points, professional layout."* Then apply the same approval gate: would you actually hand this to a client? Note what you had to fix. The lesson is the same one this whole exercise teaches — describe, delegate, review — applied to work you *show* instead of work you read.

**Your Submission:** Copy your container instruction set into a document. Underneath it, paste the deliverable from your orchestration-workspace task. Write two sentences: (1) what the reusable container (for conversations) and the orchestration workspace (for background tasks) each do best, and (2) how you plan to use both in your work going forward. Submit the container instructions + deliverable + two sentences.

### Reflection

Before closing this chapter, write three sentences:

1. Which of the three tools do you think you will use most, and for what specific task?
2. What surprised you most about the standing brief that came out of your configuration step — whether an AI interview wrote it for you (Tracks A and B) or you wrote it by hand using Role/Context/Rules/Format (Track C)?
3. What is one task you currently do manually, every week, that you now realize could be handled entirely by a Gem?

These questions are not rhetorical. Write them down. The answers will become useful context when you read Chapter 3.

Your workshop is installed. Three tools, three separate jobs, three separate configurations. Nothing connects them yet except you — and in Module 3, you will change that on purpose.

:::{admonition} Is This Still True?
:class: note
Tool names, menu paths, and even whole products change between releases. Before you rely on this chapter's specifics, run three checks:

1. **Which tool holds your API key?** Open your sandbox tool and confirm the key you saved still works — and that the sandbox product still exists as a separate product. Vendors regularly fold experimental tools into their consumer assistants.
2. **Which surface saves your standing instructions?** Open each tool's settings and find where its standing brief lives now. The label changes — *custom instructions*, *preferences*, *project brief* — but the concept does not.
3. **Check the setup sheet.** cognitioneconomy.net/ch02-companion is date-stamped and updated whenever any of the above moves.
:::

---
*Applied Exercise for Chapter 2 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
