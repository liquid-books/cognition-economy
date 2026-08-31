# drlee.io/ch05 — Companion Page: The Six Engineering Disciplines

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 5. The printed chapter teaches the six floors; this page carries the current buttons for climbing them on each surface. Product names, menu paths, commands, and filenames below were accurate when last verified and *will* change.

---

## Current Product Mapping

| Book role | Current product | Where |
|---|---|---|
| Chat assistant (Track A) | Claude Desktop (Anthropic) | claude.ai/download |
| Terminal agent (Track B) | Claude Code inside the Antigravity IDE's integrated terminal | antigravity.google · Claude Code docs (search "Claude Code quickstart") |
| Ecosystem assistant + reusable container (Track C, floors 1–4) | Gemini + Gems | gemini.google.com |
| Orchestration workspace (Track C, floors 5–6) | Antigravity IDE — Agent Manager view | antigravity.google |

---

## Track A — Current Click-Paths

- **Floor 2 (standing instructions):** Claude Desktop → **Settings → Custom Instructions**. Label drift warning: "Custom Instructions" is also ChatGPT's label for its equivalent; Claude's has been renamed before. It is the text box whose contents load before every conversation.
- **Floor 3 (reusable container):** save the Meeting Prep skill as a **Claude Project** (Projects sidebar → New Project → paste the skill instructions into the project's instructions field) or as a **Gemini Gem** (Gem Manager → New Gem). Either container works; the chapter's exercise text says "a Project, a Gem, whatever your tool calls it."
- **Floors 4–5 (attachments):** the paper-clip / attach control in the message box accepts the client documents and your Working Brief file.

## Track B — Current Click-Paths (per printed step)

1. **Floor 1:** work at the **`claude>`** prompt in the Antigravity IDE's integrated terminal (**Ctrl + `** opens it; Control+backtick on Mac, Ctrl+backtick on Windows).
2. **Floor 2 (context file):** the auto-loaded standing brief is **CLAUDE.md** in your workshop folder — open it from the IDE file browser (left panel), edit, save. Reload by typing `exit` then `claude` in the same folder.
3. **Floor 3 (specialist):** at the `claude>` prompt, type **`/agents`** → **Create new agent** → give the plain-English description → let Claude Code generate the definition → save. (The `/agents` wizard's screens change between releases; the flow is view / create / edit.)
4. **Floor 4 (real documents):** reference files by path in your request; the IDE file browser shows the paths.
5. **Floor 5 (memory test):** edit CLAUDE.md in the file browser, save, start a fresh `claude` session.
6. **Floor 6 (harness spec):** the specification arrives as a file visible in the IDE file browser.

## Track C — Current Click-Paths (per printed step)

1. **Floor 1:** gemini.google.com, ordinary new conversations.
2. **Floor 2 (container):** **Gem Manager → New Gem** → name "Meeting Prep" → instructions field → **Save**.
3. **Floor 3:** run the improve-your-own-instructions prompt inside the Gem; paste the result back into **Gem Manager → [your Gem] → edit instructions → Save**.
4. **Floor 4:** attach context with the paste/attach controls in the Gem conversation.
5. **Floor 5 (project-scope memory):** Antigravity IDE → **CMD+E** (Mac) / **CTRL+E** (Windows) → **Agent Manager** → **New Project** → name "Professional Context" → **Project Description** field = your Working Brief.
6. **Floor 6 (scheduled harness):** Agent Manager → new **recurring Agent task** → schedule field (e.g., "Every Monday at 7:30 AM") → task description → **Submit**. If your build does not show recurring tasks, that feature may be plan-gated or renamed — log it as a verification answer and check the changelog below.

---

## Changelog

- **Fall 2026** — Page created from the Fall 2026 print edition. CLAUDE.md confirmed as Claude Code's context filename; `/agents` wizard flow confirmed; Antigravity Agent Manager scheduling confirmed on current build.
- *(next entry goes here — date + what moved)*
