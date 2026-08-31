# Chapter 13 Companion — Design Your Daily Briefing Agent

**cognitioneconomy.net/ch13-companion · Last verified: Fall 2026**

> This page is the perishable half of Chapter 13's exercise. The printed book gives you the decisions — trigger, work, channel — and the plain-English delegations. This page gives you the buttons: current product names, click-paths, and configuration syntax. When a vendor renames something, this page changes and the book does not.

**Changelog**
- *Fall 2026:* Initial version, verified against the tools below at press time.
- *(future entries go here — three lines max, dated)*

---

## Which tools these tracks map to (Fall 2026)

| Printed surface | Current product (Fall 2026) | Notes |
|---|---|---|
| Track A — chat assistant | Claude (claude.ai / Claude Desktop) | Any major chat assistant works. Desktop download: claude.ai/download |
| Track B — terminal agent | Claude Code | Quickstart: code.claude.com/docs/en/quickstart (~10 minutes to a working session) |
| Track C — agent-orchestration workspace | Antigravity IDE, Agent Manager view | Overview: antigravity.google/docs/ide-overview |
| Consumer-grade scheduled tasks | Claude Cowork (agentic workspace, included in Pro) | Scheduled tasks are native — plain-English schedule + work, no terminal (see Chapter 2 companion) |

---

## Track A — Chat Assistant (manual version)

The printed steps are complete; nothing here is required. For reference:

- **Step 1 (open your chat assistant):** claude.ai in a browser, or Claude Desktop from claude.ai/download.
- **Step 4 (save the prompt):** in Claude, pin the conversation or save the prompt as a Project instruction so it is one click away each morning.

## Track B — Terminal Agent (Claude Code, Fall 2026)

### Printed step 1 — "Set the trigger dial: a schedule, not an event"

- Open Claude Code in your terminal. The plain-English delegation printed in the book works as-is — Claude Code will create the scheduled task and confirm it back to you.
- To see what is scheduled: ask *"list my scheduled tasks"* or run `/tasks` in the session.
- To cancel: ask *"cancel the 8:00 AM briefing task"* — Claude Code will confirm which task and remove it.
- **Why not a hook:** Claude Code's hooks system fires on *lifecycle events* (session start, before/after a tool runs, when input is needed, when a sub-agent finishes). There is no "at 8:00 AM" hook event — a clock trigger is a scheduled task. The earlier edition of this exercise got this wrong; the current one does not. Hooks reference: the official Claude Code hooks guide (search "Claude Code hooks guide" — the docs URL moves; the current link is maintained here).

### Printed step 2 — "Set the channel dial"

- As of Fall 2026, the channels available to a Claude Code session include **Slack-style team channels, email, Telegram, Discord, and iMessage**. The set grows with releases — the in-session answer to *"which delivery channels can you reach today?"* is authoritative over this page.
- Channel setup is per-channel: team chat channels require the workspace integration to be installed by an admin; phone-messaging channels require a one-time pairing from the channels settings screen. Current walkthrough with screenshots: linked from this page's sidebar.

### Printed step 4 — "Add the hook"

- The delegation *"when the briefing has been delivered, notify me"* maps to a **post-task lifecycle hook**. Claude Code will write the hook configuration for you; read what it wrote before accepting. If you want to see the raw configuration, ask *"show me the hook you just created."*

### Printed step 5 — "Let it fire once"

- `briefing-spec.md` can live anywhere; putting it in your project folder means the scheduled task can re-read it on every run, so edits to the file update the briefing without touching the schedule.
- If the scheduled run does not fire: check that your machine (or the hosted session) is awake at 8:00 AM. Terminal-agent scheduled tasks run where the agent runs; the hosted/agentic-workspace option (Claude Cowork) fires server-side and does not need your laptop open.

## Track C — Agent-Orchestration Workspace (Antigravity IDE, Fall 2026)

### Printed step 1 — "Open the orchestration view"

- Open Antigravity IDE. Press **CMD+E** (Mac) or **CTRL+E** (Windows) to switch from the Editor surface to the **Agent Manager** — the no-code orchestration view. Orientation doc: antigravity.google/docs/ide-overview.

### Printed step 2 — "Set the recurrence decision"

- In the Agent Manager, click **New Task**. Paste your specification into the task description box, with the recurrence sentence from the book at the top. The Agent Manager parses the "every weekday at 8:00 AM" sentence into a recurring schedule — verify the parsed schedule shown in the task header before running.

### Printed step 3 — "Watch the first run"

- The Agent Manager produces **Artifacts** as the agent executes: a markdown draft of the briefing, a configuration summary, and the delivery record. Artifacts appear in the task's right-hand panel.

### Printed step 5 — "Save it as recurring"

- Use **Save as recurring background agent** on the task's overflow menu. The task then fires on schedule, asynchronously, server-side — your machine does not need to be on.

## Optional Variant — The Desktop-Bound Task (computer use, Fall 2026)

- Computer use shipped as a consumer research preview in 2026: per-application consent, a vendor-maintained blocklist, and the vendor's own caveat that it is "still early." Grant access per application, never to the whole desktop, and keep the human-approval gate on every run. Current setup path: linked from this page's sidebar.

---

## Verification lab answers (Fall 2026 baseline)

For the printed "Is this still true?" checks, the answers at press time were:

1. *Can you run a task on a schedule?* — Yes on all three surfaces above; inspect/cancel via `/tasks` (terminal agent) or the Agent Manager task list (orchestration workspace).
2. *Which channels can you deliver to?* — See the Track B channel list above; consumer messaging apps shipped first, team channels are now first-class.
3. *Where do scheduled tasks live?* — Both: the terminal agent and the agentic workspace each run them natively; the workspace version is the no-terminal path.

Log your own dated answers — where they differ from this page, your tool has moved past press time, and your log is the newer truth.
