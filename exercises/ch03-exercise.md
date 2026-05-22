# Applied Exercise — Chapter 3: Tools and the MCP Revolution
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Connect Google to Claude Desktop and Prompt Your Real World

By the end of this exercise you will have Gmail, Google Drive, and Google Calendar connected to Claude Desktop — and you will have prompted against your actual data. This is the moment the workshop becomes real.

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code inside Antigravity IDE:** For students who want to work in a professional developer environment. Requires Antigravity 2.0 IDE (antigravity.google/docs/ide-overview) with Claude Code running in the integrated terminal.
- **Track C — Gemini + Antigravity 2.0 IDE:** For students in the Google ecosystem. Uses Gemini (gemini.google.com) for AI conversations and the Antigravity 2.0 IDE Agent Manager for orchestration.
:::

### Track A — Claude Desktop

**What you need:**
- Claude Desktop installed (Chapter 2)
- A Google account — free at gmail.com if you do not have one
- 15 minutes

**Part 1: Connect Your Google Account (5 minutes)**

Open Claude Desktop. In the left sidebar, click **Customize** → **Connectors** → the **+** icon → select **Google Workspace**.

A browser window opens asking you to sign in with Google and grant permissions. Sign in with your Google account and approve the permissions. That is it. No config files. No developer console. No credentials to manage. Claude Desktop handles the entire authentication flow.

Once connected, you will see Gmail, Google Drive, and Google Calendar listed as active connectors. Claude now has access to all three whenever you ask for them.

**Part 2: Prompt Against Your Gmail**

Type this into Claude Desktop:

> *"Search my Gmail for any emails I received in the last 7 days that I have not replied to. For each one, give me the sender's name, the subject line, and one sentence describing what they need from me. Sort them by urgency."*

Read what comes back. Notice that Claude is citing actual emails with links back to the originals. This is not a simulation — it is reading your real inbox.

If you have a clean inbox, try:

> *"Who has emailed me most frequently in the last 30 days? Give me the top five senders and roughly what each conversation has been about."*

**Part 3: Prompt Against Your Google Drive**

> *"Search my Google Drive for any documents I have edited in the last two weeks. List them by title, when they were last modified, and one sentence on what each one appears to be about."*

Then go deeper on one:

> *"Open [name of a specific document you know is in your Drive] and summarize it in five bullet points."*

**Part 4: Prompt Against Your Calendar**

> *"Look at my Google Calendar for the next 14 days. What does my schedule look like? Which days are the most packed? Where is my biggest uninterrupted block of time, and what day is it on?"*

Follow up with:

> *"Based on my calendar for this week, when would be the best time to block two hours for deep focused work? Suggest three options and explain why each one works."*

**Your Submission:** Run the connected tool on a real professional task — not a test, but something you actually need answered today. Copy the full output into a document. Write two sentences: (1) what you asked and why it was genuinely useful, and (2) what the output would have looked like if you had given Claude only your description of the data rather than the live connection. Submit the output + two sentences.

### Track B — Claude Code inside Antigravity IDE

1. Open Antigravity 2.0 IDE → Editor surface → open the integrated terminal (Control+backtick on Mac, Ctrl+backtick on Windows) → start Claude Code (you should see "claude>" when ready).

2. At the claude> prompt, type "/mcp" and press Enter. A list of available MCP integrations appears — these are the external tools Claude Code can connect to: web search, file system readers, calendar, GitHub, Google Drive, Notion, and others depending on your installation.

3. Choose one integration to connect. Web search is the easiest starting point and requires no separate account setup. Find it in the /mcp list and type the command to enable it — Claude Code will display the exact syntax. Follow any browser-based authentication prompts that open.

4. Confirm the integration is active: type "/mcp" again and verify it shows as connected.

5. Now run a real professional query that requires live data — not a question Claude can answer from training. For web search: "What are the three most important developments in [your specific industry] in the last two weeks? Cite specific sources with dates." For a file reader: "List and summarize the five documents I have modified most recently in [folder path]." For a calendar connector: "What meetings do I have this week and what should I prepare for each one?"

6. Read the output carefully. Notice that Claude Code is citing real, current information — not training data from months ago. The Antigravity IDE file browser on the left side of the screen will show any files created as part of this interaction.

7. Now connect a second integration — one that touches a tool you use in your actual daily work. Common options: a file reader pointed at your documents folder, a calendar connector, or a project management tool. Follow the same process: find it in /mcp, authenticate, confirm active.

8. Run a second real query using the new integration. Ask something that genuinely matters to your work this week.

9. Finally, ask Claude Code to combine both integrations in one workflow: "Using [integration 1] and [integration 2], [describe a task that requires both]." For example: "Search the web for news about my client's industry, then save a briefing to my documents folder as client-brief.md."

10. Watch the Antigravity IDE file browser as Claude Code works. If it creates or modifies a file, you will see it appear in the left panel in real time.

**Your Submission:** Copy three outputs into a single document: (1) your first integration query result with sources cited, (2) your second integration query result, (3) the combined-integration workflow result. Write two sentences: (1) which integration produced the most immediately useful output and why, and (2) describe one workflow you could build this week that combines two or more of your connected tools. Submit the three outputs + two sentences.

### Track C — Gemini + Antigravity 2.0 IDE

1. Open Gemini (gemini.google.com) and sign in with your Google account.

2. Click the settings or Extensions icon (look for a plug or grid icon, or go to Settings → Extensions). Enable the Google Workspace extension — this connects Gemini to your actual Gmail, Google Drive, Google Calendar, and Google Docs.

3. Once enabled, test with a real question that requires your actual data: "Find the three most important emails I have received in the last 48 hours that require a follow-up from me. For each one: who sent it, what do they need, and what would a good response look like?" Gemini will search your real inbox.

4. Note when Gemini cites a real email subject line or sender name from your actual account — that is the tool connection working. The response is grounded in your real data, not a generic example.

5. Run a second query using your Google Drive: "Find any documents in my Drive related to [a project you are currently working on]. Tell me what each document contains and whether there is anything I should review before my next meeting." Confirm Gemini is referencing real document titles.

6. Now open Antigravity 2.0 IDE and press CMD+E (Mac) or CTRL+E (Windows) to switch to Agent Manager.

7. Create a new Project. Add a tool extension to the Project — click the tool or extension option in the Project settings and connect a web search capability. This is Antigravity's own tool layer, separate from Gemini's Google extensions.

8. Start a new asynchronous Agent task inside the Project: "Search the web for the five most relevant recent developments in [your industry or area of work]. Produce a one-page intelligence briefing with findings and their strategic implications." Submit the task.

9. While the agent runs in the background (typically 2-4 minutes), go back to your Gemini window. Ask a follow-up question that builds on the Gmail or Drive data you already retrieved — you are using both surfaces simultaneously.

10. When the Antigravity Artifact arrives, compare it to your Gemini outputs. You now have two types of live-data AI responses: Gemini accessing your personal Google data, and the Antigravity agent accessing the public web.

**Your Submission:** Copy three outputs into a document: (1) the Gemini inbox analysis, (2) the Gemini Drive document search, (3) the Antigravity web intelligence Artifact. Write two sentences: (1) which data source — your personal Google data or the public web — produced the more immediately actionable result for your work, and (2) describe a workflow that would combine both and what problem it would solve. Submit three outputs + two sentences.

### Reflection

Write one sentence before you close this chapter:

*Now that Claude can see your inbox, your files, and your calendar — what is the first task you are handing off to it completely, starting this week?*

That sentence is your commitment. The rest of this book is about making it bigger.

---
*Applied Exercise for Chapter 3 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
