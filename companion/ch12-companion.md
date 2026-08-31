# cognitioneconomy.net/ch12-companion — Chapter 12 Companion: Self-Learning Systems

**Last verified: Fall 2026**

> This page holds the perishable layer of Chapter 12 — current product names, filenames, click-paths, and version specifics for the printed exercise tracks. The printed book teaches the loop (produce, judge, encode, recall); this page supplies the buttons and filenames. If something below no longer matches what you see on screen, check the changelog and carry on.

## Changelog

- *Fall 2026* — Initial page. Verified against the tools listed below. Note for returning readers: the original edition's Track B asked you to submit a file its steps never created, and Track C used two different names for the same rules file. Both are fixed in the current printed tracks; the artifact names below match what the print steps now produce.
- *(future entries go here — what changed since the printed edition, three lines, dated)*

---

## Current Surface Names (Fall 2026)

| Book's term | Current product (Fall 2026) |
|---|---|
| Chat assistant / thinking partner desktop app (Track A) | Claude Desktop — claude.ai/download — or claude.ai in the browser |
| Terminal agent (Track B) | Claude Code — quickstart at code.claude.com/docs/en/quickstart |
| Agent-orchestration workspace (Track C) | Antigravity IDE, Agent Manager view — antigravity.google/docs/ide-overview |

## Track A — Chat Assistant

- **Step 1 (open your assistant):** Open **Claude Desktop** (claude.ai/download) or **claude.ai** in your browser.
- Steps 2–7 are fully in print — no perishable details.

## Track B — Terminal Agent

- **Setup:** Install Claude Code per the quickstart at **code.claude.com/docs/en/quickstart**.
- **Step 1 (open the auto-loaded context file):** Claude Code's auto-loaded context file is named **CLAUDE.md**, in your project root (a personal-scope version lives at `~/.claude/CLAUDE.md`). Other terminal agents use their own filename — this is the "context file" the print steps refer to. Open it directly in your editor or ask the agent to open it.
- **Step 2 (gather the evidence):** Claude Code cannot reliably enumerate "the last five conversations" on its own — export or copy your recent session transcripts and paste them in, as the print step says. Session transcripts live under `~/.claude/projects/` if you want to pull them from disk.
- **Step 4 (save the file):** Confirm the "Operating Rules" section was actually written to CLAUDE.md — open the file and look. Your submission artifact is this updated file.
- **Step 5 (fresh-session test):** Start a new session (`claude` in a fresh terminal, or `/clear`) so the updated CLAUDE.md loads cold.
- Steps 3, 6, 7 are fully in print — no perishable details.

## Track C — Agent-Orchestration Workspace

- **Setup:** Install the Antigravity IDE; the overview at **antigravity.google/docs/ide-overview** walks through the install.
- **Step 1 (open the record):** Press **CMD+E** (Mac) or **CTRL+E** (Windows) to switch to the **Agent Manager** view. You will see a timeline of recent agent tasks and the **Artifacts** (markdown and diff artifacts) each one produced.
- **Step 2 (review the week):** Agent Manager can review artifacts produced **in this workspace over the last seven days** — the phrasing that currently works: *"Review the markdown and diff artifacts produced in this workspace over the last seven days…"* If that enumeration fails in your version, use the print fallback (paste in your last five deliverables).
- **Step 3 (the workspace rules file):** The workspace-level standing rules artifact is currently the **Project Description** (workspace settings → Project Description). Some docs call it the "project rules file" — same artifact. Whichever label your version shows, put every rule there; your submission artifact is this updated Project Description.
- **Step 5 (permanent artifact):** Ask Agent Manager to save the Friday review template **as a pinned/permanent Artifact** in the workspace so it survives task cleanup.
- Steps 4 and 6 are fully in print — no perishable details.

## Instructor Refresh Checklist (each term)

1. Re-run the chapter's "Is this still true?" checks (memory persistence; can students open their rules artifact as a file?).
2. Confirm CLAUDE.md is still Claude Code's auto-loaded filename; update the table if the convention changed.
3. Confirm the Project Description is still Antigravity's workspace-rules artifact and that the seven-day artifact review still works.
4. Bump the "Last verified" date.
