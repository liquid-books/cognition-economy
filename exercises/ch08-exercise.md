# Applied Exercise — Chapter 8: Plugins — Extending Your Workshop
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Install Three Plugins This Week

This exercise ends with three plugins installed, tested, and integrated into your daily workflow — one for real-time information, one for a tool you use constantly, and one you build yourself.

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code inside Antigravity IDE:** For students who want to work in a professional developer environment. Requires Antigravity 2.0 IDE (antigravity.google/docs/ide-overview) with Claude Code running in the integrated terminal.
- **Track C — Gemini + Antigravity 2.0 IDE:** For students in the Google ecosystem. Uses Gemini (gemini.google.com) for AI conversations and the Antigravity 2.0 IDE Agent Manager for orchestration.
:::

### Track A — Claude Desktop

**Plugin One: Web Search**

Find and install a web search plugin for Claude Desktop or Gemini (search "Claude web search plugin" or "Gemini search extension" for the current options — these evolve quickly). Once installed, test it with a question that requires current information:

> *"What are the three most significant AI announcements from the last seven days that are relevant to [your industry]?"*

Notice what changes: your AI is no longer limited to what it knew at training time. Current information is now part of every conversation where you need it.

Then push further. Ask it to research a competitor who released a press release this week. Ask it to find the latest pricing information for a tool you are evaluating. Ask it to surface news about a client's industry that you could reference in tomorrow's conversation. Every question that used to require a tab switch now has an answer inside the conversation. The experience of not having to leave — of your AI being genuinely current — is more significant than it sounds until you have felt it.

**Plugin Two: Your Most-Used Business Tool**

Identify the one external tool you reference most often during your work — your CRM, your project management tool, your calendar, your note-taking system. Find its plugin or integration with Claude and install it.

Test it with a question that requires real data from that tool:

> *"What are the three most important things I need to do today based on my [tool name] data?"*

The first time you ask your AI a question and it answers using your actual live data — not data you described, not data you pasted, but the live system — is a moment worth paying attention to. That is the tool becoming genuinely useful.

**Plugin Three: Build One**

Identify a small, specific capability you wish your AI had but that does not exist in any marketplace. Something narrow. Something useful. Something you would use at least twice a week.

Use the four-step process from this chapter to build it. Have Claude help you write the specification. Test it on real work. Refine once. Save it.

After completing all three, write two sentences:

*What is the most impactful thing these plugins changed about how you work? And what is the next plugin — built or installed — that would create similar impact?*

**The bigger picture:**

Your plugin library is a living system. It grows with your work, your tools, and your ambitions. Every time you find yourself switching tabs, copying and pasting between systems, or manually fetching information that your AI should already have — that friction is a plugin waiting to be installed or built.

Most professionals tolerate that friction. They adapt to the inconvenience. They build workarounds. They accept that "using AI" means working in two worlds at once — the conversation and the tab-switching outside it.

The professionals who build serious AI workflows refuse that trade. They see every friction point as a solvable problem. They install the plugin. They build the connection. They eliminate the gap.

Over a year of this practice, the accumulated effect is dramatic. Not a 10% improvement in how fast you work — a fundamental change in how your work feels. Information appears when you need it. Tools respond to natural language. Workflows run without you manually connecting the dots.

That is the promise of the connected workshop. And plugins are the layer that makes it real.

Stop tolerating friction. Build the plugin.

**Track A Your Submission:** Run the plugin on a real professional task you actually need done today — not a test. Copy the full output into a document. Write two sentences: (1) what you asked and why the plugin was necessary (what would have been missing without the live connection), and (2) what you plan to use this plugin for every week going forward. Submit the output + two sentences.

### Track B — Claude Code inside Antigravity IDE

1. Open Antigravity 2.0 IDE → Editor surface → integrated terminal → Claude Code (claude> prompt ready).
2. At the claude> prompt, type "/mcp" and press Enter. Review the list of available integrations.
3. Install a web search integration first — it is the most universally useful. Find it in the /mcp list and follow the exact command syntax Claude Code displays. Authenticate in the browser window that opens. Confirm it shows as active in the /mcp list.
4. Run a real professional query using web search: "What are the three most significant competitive developments in [your specific industry] in the last 30 days? For each one, give me: (a) what happened, (b) why it matters for someone in [your role], and (c) one specific action I should consider in response. Cite your sources with dates." Read the output and verify Claude Code is citing real, recent, specific sources.
5. In the Antigravity IDE file browser, right-click and create a new file called "industry-intel.md." Ask Claude Code to save the web search output to that file. Watch it appear and populate in the file browser.
6. Now install a second integration — one that connects to a tool you use daily. Use /mcp to find options: a file reader for your documents folder, a calendar connector, GitHub, or a project management tool. Follow the same process: find it, authenticate, confirm active.
7. Run a real query using the second integration. If you connected a file reader: "List and summarize the five documents I have modified most recently in [your folder path]. For each one, tell me its topic and whether there is anything I should act on." If you connected a calendar: "What external meetings do I have this week? For each one, tell me the attendees, the meeting purpose, and one thing I should prepare."
8. Save this second output as a new file in the IDE file browser.
9. Now design and run a combined workflow using both integrations: "Using web search and [second integration], [describe a task that requires both — for example: 'check my calendar for client meetings this week, search the web for recent news about each client's company, and produce a one-page briefing for each meeting with the news context included']."
10. Watch the Antigravity IDE file browser as Claude Code works through the combined task. Files appear and update in real time. The final combined output saves as a file you can open and share directly from the IDE.

**Your Submission:** Compile into one document: (1) your web search output with sources cited, (2) your second-integration output, (3) your combined-workflow output. Write two sentences: (1) which integration produced the most immediately useful result and why, and (2) describe one specific workflow you want to build this week that combines two of your installed integrations and name the professional problem it solves. Submit three outputs + two sentences.

### Track C — Gemini + Antigravity 2.0 IDE

1. Open Gemini (gemini.google.com) and sign in. Find the Extensions menu (look for a settings icon, plug icon, or "Extensions" in the sidebar or settings).
2. Enable the Google Workspace extension. This connects Gemini to your actual Gmail, Google Drive, Google Calendar, and Google Docs. Approve any permission prompts — you are granting Gemini read access to your own Google account.
3. Test the Gmail connection with a real question: "Find the three most important emails in my inbox from the last 48 hours that require a follow-up from me. For each one: who sent it, what do they need from me, and draft a one-sentence response I could send." Read the response and note when Gemini cites a real subject line or sender name from your actual inbox.
4. Test the Drive connection: "Find any documents in my Google Drive related to [a project you are currently working on]. For each document, tell me its title, what it contains, and whether there is anything I should review before my next relevant meeting." Verify Gemini is reading real document titles and content.
5. Test the Calendar connection: "What external meetings do I have this week? For each one, who are the attendees and what should I prepare?" Confirm Gemini is reading your real calendar entries.
6. Now open a second browser tab and try the same Gmail and Calendar questions in a plain Gemini chat with no extensions enabled. Compare the responses — without extensions, Gemini has none of your data and produces generic advice. With extensions, it cites your real emails and events.
7. Open Antigravity 2.0 IDE and press CMD+E (Mac) / CTRL+E (Windows) to switch to Agent Manager. Create a new Project or open an existing one.
8. In the Project, add a web search tool extension — this is Antigravity's own tool layer, separate from Gemini's Google extensions. Click the tools/extensions option in the Project settings and connect web search.
9. Start a new Agent task: "Search the web for the five most significant recent developments in [your industry]. For each development: what happened, why it matters, and one specific action a business professional in [your role] should consider taking. Produce this as a one-page intelligence briefing." Submit the task.
10. While the Antigravity agent runs in the background, return to Gemini and ask a follow-up question that uses the Google Workspace data you already retrieved — connecting the insights from your personal data with the broader industry picture.

**Your Submission:** Compile three outputs into one document: (1) the Gemini Gmail/Drive analysis showing your personal data, (2) the Gemini vs. no-extensions comparison from Step 6, (3) the Antigravity web intelligence Artifact. Write two sentences: (1) what surprised you most about what Gemini found in your own Gmail or Drive, and (2) describe a combined workflow that uses both your Google personal data (Gemini) and the public web (Antigravity) and the specific professional problem it would solve. Submit three outputs + two sentences.

### Reflection

After completing the plugin work in any track, write two sentences:

*What is the most impactful thing these plugins changed about how you work? And what is the next plugin — built or installed — that would create similar impact?*

If you ran more than one track: *Did the same friction point feel solvable in every surface, or did one surface make a particular integration obvious and another make it awkward?* Your answer is a map of where to invest your integration time next quarter.

---
*Applied Exercise for Chapter 8 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
