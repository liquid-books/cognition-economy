# Applied Exercise — Chapter 2: Standing Up Your Cognitive Workshop
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your Workshop in 90 Minutes

This exercise produces three things: Claude Desktop installed and configured, one Gem created and tested, and AI Studio verified with your API key in hand. Complete all three before moving to Chapter 3.

:::{figure} ../images/ch02-workshop-setup-checklist.png
:label: fig-ch02-checklist
:alt: Cognitive workshop setup checklist for all three tools independently
:width: 80%
:align: center

*Setup Checklist* — Three independent installs. Three separate configurations. Check each one off before you move on.
:::

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code inside Antigravity IDE:** For students who want to work in a professional developer environment. Requires Antigravity 2.0 IDE (antigravity.google/docs/ide-overview) with Claude Code running in the integrated terminal.
- **Track C — Gemini + Antigravity 2.0 IDE:** For students in the Google ecosystem. Uses Gemini (gemini.google.com) for AI conversations and the Antigravity 2.0 IDE Agent Manager for orchestration.
:::

### Track A — Claude Desktop

#### Part 1: Install and Configure Claude Desktop (30 minutes)

**Install:**
1. Go to claude.ai/download
2. Download and install for your operating system
3. Sign in and confirm it opens

**Write your system prompt using meta-prompting:**

Open Claude Desktop. Paste this exactly:

> *"I want to create a system prompt for you — a standing brief that loads before every conversation. To write it well, I need to interview you. Ask me up to 8 questions, one at a time, to learn: my professional role and industry, my primary goals, the tasks I do most often, how I prefer to receive information, what frustrates me about generic AI responses, and anything I always or never want from you. After the interview, write me a complete system prompt I can paste directly into your settings."*

Answer the questions with specifics, not generalities. The more honest and specific you are about your actual day and actual frustrations, the better the prompt Claude generates.

When Claude delivers the finished system prompt, read it. Edit anything that does not sound right. Go to Claude Desktop → Settings → Custom Instructions and paste it in.

Every conversation from this point forward starts with that context already loaded.

#### Part 2: Create Your First Gem in Gemini (30 minutes)

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

**Write the Gem instructions using Claude:**
Open Claude Desktop and say:

> *"I want to create a Gemini Gem that [describe the task]. My role is [your role]. The input I will typically give it is [what you paste in]. The output I need is [format, length, tone]. Write me a complete system prompt for this Gem."*

Take Claude's output. Go to Gem Manager → New Gem → paste the instructions → name the Gem → save.

Test it immediately with a real example. If the output needs adjustment, refine the instructions once and test again.

**Important:** This Gem has nothing to do with Claude. They do not know about each other. You used Claude as a writing tool to produce better Gem instructions — that is the only relationship between them.

#### Part 3: Set Up Google AI Studio (15 minutes)

Go to aistudio.google.com and sign in.

Click **Get API key** in the left sidebar → **Create API key** → copy it and store it somewhere safe — a password manager, a locked note, anywhere private. Treat it like a password: don't put it in a shared document or email it to yourself.

Create a new project called **Sandbox**. In the system instruction field, write two or three sentences about who you are and what you do. Upload one document from your actual work — a report, a brief, a proposal — and ask AI Studio a question about it. Confirm the model reads and responds to your real content correctly.

That is all. AI Studio is verified.

**Your Submission:** Your submission is your completed system prompt — the one Claude wrote for you during the meta-prompting interview, pasted into Settings → Custom Instructions. Copy the full text of your system prompt into a document. Write two sentences: (1) what you told Claude about yourself during the interview that led to the most follow-up questions, and (2) what surprised you most about the prompt it generated. Submit the system prompt + those two sentences.

### Track B — Claude Code inside Antigravity IDE

1. Go to antigravity.google/docs/ide-overview and download the Antigravity 2.0 IDE installer for your operating system. Install it like any standard application. Sign in with your Google account when prompted. The product is free during preview.

2. When the IDE opens, you land in the Editor surface — a VS Code-style interface with a file browser on the left, an editor pane in the center, and a status bar at the bottom. Do not press CMD+E or CTRL+E yet — that switches to Agent Manager, which is Track C. This track uses the Editor.

3. Open the integrated terminal: on Mac press Control and the backtick key (the key to the left of 1 on the top row). On Windows press Ctrl and the backtick key. A terminal panel opens at the bottom of the screen.

4. In the terminal, follow the Claude Code quickstart at code.claude.com/docs/en/quickstart to install and authenticate Claude Code. This takes about five minutes. You will be asked to sign in with your Anthropic account. When you see a "claude>" prompt appear in the terminal, you are ready.

5. In the terminal at the claude> prompt, create a new workshop folder for your professional work. Type a command that creates a folder — if you are not sure how, ask Claude Code directly: type "How do I create a new folder called my-workshop and navigate into it?" Claude Code will tell you the exact commands to run in your terminal.

6. Once you are inside your workshop folder, run the meta-prompting interview. At the claude> prompt, type exactly: "I want to create a CLAUDE.md file — a standing professional brief about me that you read automatically at the start of every session in this folder. Please interview me with up to 8 questions, one at a time, to learn my professional role, my goals, my most common tasks, my preferences for how information is delivered, and what frustrates me about generic AI responses." Answer each question with specific, honest details.

7. After the interview, ask Claude Code: "Now write my CLAUDE.md file based on everything I told you. Keep it under 400 words with clear labeled sections." When it produces the file, read every word. Ask for revisions on anything that does not sound accurate or useful.

8. Ask Claude Code to save the CLAUDE.md file in your workshop folder. In the Antigravity IDE file browser on the left side of the screen, you will see the CLAUDE.md file appear.

9. Test the persistent context: type "exit" at the claude> prompt to end the session. Then type "claude" again to start a fresh session in the same folder. Ask about something you are genuinely working on this week — without mentioning anything from the CLAUDE.md. Claude Code reads the file automatically before your first message. Notice how it responds with context about your professional situation.

10. Compare: open claude.ai in your browser in a separate tab. Ask the exact same question with no context. The difference in relevance between the two responses is the value of the CLAUDE.md — and the reason this track's memory layer is more powerful than Track A's Custom Instructions approach.

**Your Submission:** Copy the full text of your CLAUDE.md file into a document. Underneath it, paste the response from your Step 9 test session — the first time Claude Code responded using your CLAUDE.md automatically. Write two sentences: (1) what in the response showed that Claude Code had read your CLAUDE.md without you telling it to, and (2) how does the CLAUDE.md approach differ from the Custom Instructions approach in Track A? Submit the CLAUDE.md + test response + two sentences.

### Track C — Gemini + Antigravity 2.0 IDE

1. Open gemini.google.com in your browser and sign in with your Google account. If you do not have one, go to accounts.google.com and create one — it is free.

2. In the Gemini left sidebar, look for "Gem Manager" (you may need to click "Explore Gems" or look under the menu icon). Click it, then click "New Gem."

3. You now have a blank Gem — a saved AI configuration with its own persistent instructions. In the Instructions field, write your professional context using the Role/Context/Rules/Format framework from this chapter: (a) Role — who you are and what job the Gem is doing for you, (b) Context — your industry, your actual day-to-day work, key constraints, (c) Rules — how you want responses structured, what you always want, what you never want, (d) Format — length, bullet points or prose, formal or direct. Aim for 200-300 words.

4. If you want help writing these instructions, open claude.ai in a separate tab, describe your role and preferences, and ask Claude to write Gem instructions for you. Paste the result into the Gem Instructions field.

5. Name your Gem something specific and professional — not "My Gem" but something like "Strategy Analyst," "Client Work," or "Sales Prep." Click Save. The Gem now appears in your sidebar and loads its instructions silently every time you open it.

6. Test the Gem: click it to open a conversation inside it. Ask it something you would genuinely ask about a real task you are working on this week. Then open a standard new Gemini conversation (click "New Chat" instead of your Gem) and ask the exact same question. Compare the two responses for relevance and specificity. The difference is what a system prompt buys you.

7. Now open Antigravity 2.0 IDE. If you installed it in Track B, open it now. If not, download from antigravity.google/docs/ide-overview and install. Sign in with the same Google account.

8. When the IDE opens, press CMD+E on Mac or CTRL+E on Windows to switch to the Agent Manager surface. This is a completely different view from the Editor — a clean orchestration dashboard where you launch and monitor AI agents working asynchronously. This is your home base in Antigravity for Track C throughout this course.

9. In Agent Manager, click to create a new Project. Name it after a real piece of work on your plate this week — a client deliverable, a research question, a report you need to write. In the Project Description field, write 3-4 sentences about what this project is, who the audience is, and what a good output looks like. This description functions as the agent's system prompt for every task in this project.

10. Inside the Project, start your first asynchronous Agent task. In the task description box, write in plain English what you want the agent to do — something real and useful, not a test: "Research and write a 400-word summary of the current state of [your industry or topic], highlighting the three most significant developments in the last 90 days." Click Submit. The agent works in the background while you continue with other things.

11. When the task completes (typically 2-5 minutes), a notification appears. Click into it and open the Artifact — the rich output the agent produced. Review it for accuracy and usefulness.

**Your Submission:** Copy your Gem instruction set into a document. Underneath it, paste the Artifact from your Agent Manager task. Write two sentences: (1) what the Gem (for conversations) and the Agent Manager (for background tasks) each do best, and (2) how you plan to use both in your work going forward. Submit the Gem instructions + Agent Manager Artifact + two sentences.

### Reflection

Before closing this chapter, write three sentences:

1. Which of the three tools do you think you will use most, and for what specific task?
2. What surprised you most about the system prompt Claude wrote for you during the interview?
3. What is one task you currently do manually, every week, that you now realize could be handled entirely by a Gem?

These questions are not rhetorical. Write them down. The answers will become useful context when you read Chapter 3.

Your workshop is installed. Three tools, three separate jobs, three separate configurations. Nothing connects them except you.

---
*Applied Exercise for Chapter 2 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
