# cognitioneconomy.net/ch02-companion — Companion Page: Standing Up Your Cognitive Workshop

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 2. The printed chapter teaches the decisions; this page carries the buttons. Everything below — product names, URLs, menu paths, keyboard shortcuts, plan names, prices — was accurate when last verified and *will* change. When it does, this page changes with it; the book does not.

---

## Current Product Mapping (the "today" column)

| Book role | Current product | Where |
|---|---|---|
| Thinking partner (desktop app / agentic workspace) | Claude (Anthropic) — desktop app; agentic workspace is **Cowork**, included in Pro | claude.ai/download |
| Ecosystem-native assistant | Gemini (Google) | gemini.google.com |
| Sandbox + API key | Google AI Studio | aistudio.google.com |
| Terminal agent (Track B) | Claude Code, running in the integrated terminal of the **Antigravity IDE** (Google) | antigravity.google (IDE) · Claude Code quickstart: see the current link below |
| Agent-orchestration workspace (Track C) | Antigravity IDE — **Agent Manager** view | antigravity.google |
| Artifact studio | **Claude Design** (Anthropic Labs) — the **Design** tab inside Claude | claude.ai → Design tab |
| Remote delegation channel | **Claude Dispatch** — part of Cowork; pair your phone from Cowork's settings | see Chapter 13 companion |

**Plans and prices (verify before quoting):** Claude Pro ≈ $20/month. Gemini paid tiers are sold under Google's current AI plan names — check the plan page; names changed within the last year. Antigravity: check current pricing; the free-preview period has ended.

**Artifact studio specifics (Fall 2026):** Claude Design launched from Anthropic Labs in April 2026 and lives as a **Design tab** inside Claude on paid plans. It is powered by the flagship model's vision tier (Opus 4.7 at launch) and produces polished visual work — designs, prototypes, slides, one-pagers — through the same describe-propose-refine conversation as the rest of the workspace. Notably, it can read a connected codebase and derive a design system from it, which pairs with Chapter 4's skills-as-reusable-assets argument.

---

## Setup Sheet — Track A (Chat Assistant)

### Part 1 — Thinking partner install & standing instructions
- **Download:** claude.ai/download → installer for your OS → sign in with your Anthropic account.
- **Standing instructions location:** Claude Desktop → **Settings → Custom Instructions**. (This label drifts between releases and vendors; ChatGPT calls the equivalent "Custom Instructions," Claude has also used "preferences" and profile fields. Whatever the label, it is the text box whose contents load before every conversation.)
- Paste the system prompt from your meta-prompting interview here.

### Part 2 — Creating a Gem
- gemini.google.com → left sidebar → **Gem Manager** (sometimes surfaced as "Explore Gems" or under the ☰ menu) → **New Gem** → paste instructions → name it → **Save**.
- The saved Gem appears in your left sidebar permanently.

### Part 3 — API key in the sandbox
- aistudio.google.com → left sidebar → **Get API key** → **Create API key** → copy immediately and store in a password manager.
- **Interface tour (current layout):** model selector at the top of the prompt view; **temperature** slider in the right-hand run-settings panel; **system instruction** field above the prompt area; saved **Prompts** (reusable templates) in the left sidebar.

---

## Track Sheet — Track B (Terminal Agent) · v. Fall 2026

Printed step → current buttons:

1. **Set up the surface.** Download the Antigravity IDE from antigravity.google and install like a standard application. Sign in with your Google account. You land in the **Editor** surface (VS Code-style: file browser left, editor center, status bar bottom). *Do not press CMD+E / CTRL+E* — that switches to Agent Manager, which is Track C's surface.
   - Open the integrated terminal: **Ctrl + `** (backtick — the key left of 1) on both Mac (Control, not Command) and Windows.
   - Install Claude Code: follow the current quickstart in Anthropic's Claude Code documentation (search "Claude Code quickstart" — the docs URL has moved before and may move again). Takes about five minutes; sign in with your Anthropic account. You are ready when the **`claude>`** prompt appears in the terminal.
2. **Set the scope dial (working folder).** At the `claude>` prompt, ask Claude Code itself: *"How do I create a new folder called my-workshop and navigate into it?"* — it will give you the exact commands for your OS.
3. **Standing-brief interview.** The context file's current standard name in Claude Code is **CLAUDE.md** (auto-read at session start in that folder). Other agents use their own filenames (e.g., AGENTS.md); check your tool's docs.
4. **Review before save.** Ask Claude Code to save the file; it appears in the IDE file browser on the left.
5. **Fresh-session test.** Type `exit` at the `claude>` prompt, then type `claude` to start a new session in the same folder.
6. **Control experiment.** claude.ai in any browser tab, new conversation, no context.

## Track Sheet — Track C (Ecosystem Assistant + Orchestration Workspace) · v. Fall 2026

1. **Container:** gemini.google.com → **Gem Manager** → **New Gem** (see Part 2 paths above).
2–4. Instructions field, naming, save, test — all inside the Gem editor; "New Chat" in the sidebar gives you the unconfigured baseline.
5. **Orchestration view:** open the Antigravity IDE → press **CMD+E** (Mac) / **CTRL+E** (Windows) to switch from the Editor to the **Agent Manager** surface — the orchestration dashboard.
6. **Project scope:** Agent Manager → **New Project** → name it → fill the **Project Description** field (this functions as the project-scoped system prompt).
7. **Background task:** inside the Project → new **Agent** task → plain-English task description → **Submit**. The agent runs asynchronously (typically 2–5 minutes for a research-and-write task).
8. **Approval gate:** when the task completes, a notification appears; click into it and open the **Artifact** — Antigravity's name for the structured deliverable.

---

## Changelog

- **Fall 2026** — Added artifact studio row and specifics (Claude Design, Anthropic Labs, launched April 2026 — Design tab, Opus 4.7 vision, codebase-to-design-system) and remote delegation row (Claude Dispatch, part of Cowork), matching the print edition's new artifact-studio paragraph and phone-driven-workspace clause.
- **Fall 2026** — Page created from the Fall 2026 print edition. Antigravity "2.0" version label and "free during preview" removed (preview period over). Claude Code docs URL replaced with a search instruction pending a stable link.
- *(next entry goes here — date + what moved)*
