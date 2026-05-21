# Applied Exercise — Chapter 2: Standing Up Your Cognitive Workshop
*Florida Atlantic University — Graduate Course*

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

### Part 1: Install and Configure Claude Desktop (30 minutes)

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

### Part 2: Create Your First Gem in Gemini (30 minutes)

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

### Part 3: Set Up Google AI Studio (15 minutes)

Go to aistudio.google.com and sign in.

Click **Get API key** in the left sidebar → **Create API key** → copy it and store it somewhere safe — a password manager, a locked note, anywhere private. Treat it like a password: don't put it in a shared document or email it to yourself.

Create a new project called **Sandbox**. In the system instruction field, write two or three sentences about who you are and what you do. Upload one document from your actual work — a report, a brief, a proposal — and ask AI Studio a question about it. Confirm the model reads and responds to your real content correctly.

That is all. AI Studio is verified.

### Reflection

Before closing this chapter, write three sentences:

1. Which of the three tools do you think you will use most, and for what specific task?
2. What surprised you most about the system prompt Claude wrote for you during the interview?
3. What is one task you currently do manually, every week, that you now realize could be handled entirely by a Gem?

These questions are not rhetorical. Write them down. The answers will become useful context when you read Chapter 3.

Your workshop is installed. Three tools, three separate jobs, three separate configurations. Nothing connects them except you.

