# cognitioneconomy.net/ch07-companion — Companion Page: Memory Engineering

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 7. The printed chapter teaches the three-tier memory system and the Working Brief; this page carries the current filenames, menu locations, and built-in memory features per assistant. Product names and paths below were accurate when last verified and *will* change.

---

## Current Product Mapping

| Book role | Current product | Where |
|---|---|---|
| Chat assistant (printed exercise steps) | Claude Desktop / claude.ai | claude.ai/download |
| Terminal agent (sidebar + walkthrough below) | Claude Code inside the Antigravity IDE's integrated terminal | antigravity.google · code.claude.com/docs/en/quickstart |
| Ecosystem assistant + container | Gemini + Gems | gemini.google.com |
| Orchestration workspace | Antigravity IDE — Agent Manager view | antigravity.google |

---

## Memory-File Locations per Surface (Fall 2026)

The chapter's "context file" and "built-in memory" pointers, made concrete:

| Surface | The file/feature | Where it lives |
|---|---|---|
| Claude Code (project scope) | **CLAUDE.md** | Root of your working folder — auto-loads every session in that folder |
| Claude Code (personal scope) | **CLAUDE.md** | `~/.claude/CLAUDE.md` — auto-loads in *every* project on your machine |
| Gemini CLI | **GEMINI.md** | Project root (same convention, different filename) |
| Claude.ai / Claude Desktop (built-in) | Memory feature + Projects | Settings → Memory (where offered on your plan); Project instructions hold per-project context |
| ChatGPT (built-in) | Memory | Settings → Personalization → Memory — view, edit, delete individual entries |
| Gemini (built-in) | **Saved info** | gemini.google.com → Settings → Saved info — the page where Gemini lists what it has retained about you; entries are user-editable |

**The chapter's rule applies to every row of the bottom half:** built-in memory is the convenient-but-opaque fourth layer. Inspect it, prune it, but keep your system of record in the memory file you own.

### The "Is this still true?" checks — Fall 2026 baseline

- *"What do you already know about me from previous sessions?"* — All three major assistants will answer this; Claude and ChatGPT cite their memory entries, Gemini cites Saved info. Whatever the answer, that is the layer you did not curate.
- *Can you see / edit / delete / export the entries?* — See, edit, delete: yes on all three as of Fall 2026. **Export to a file you keep: none of them offers this as a first-class button.** Copy-paste is the export path — which is the chapter's argument for the owned file, made by the vendors themselves.

---

## Terminal-Agent Walkthrough (keyed to the printed steps)

The printed exercise is written for the chat assistant. Here is the same exercise on the terminal agent, per the sidebar's pointer:

1. **Inventory (printed Step 1):** create *my-inventory.txt* in the IDE file browser (left panel) and answer the five printed questions in it.
2. **Shape it (printed Step 2):** at the **`claude>`** prompt: *"I'm going to paste my raw professional notes. Turn them into a CLAUDE.md — a concise memory document under 400 words with clear labeled sections — and save it as CLAUDE.md in this folder."* Paste your inventory. The file appears in the file browser.
3. **Save and use it (printed Step 3):** review CLAUDE.md word by word in the editor pane; request corrections at the prompt. Then run the honest test: type `exit`, type `claude` to start a fresh session in the same folder — CLAUDE.md loads before your first message — and ask about your real work *without mentioning anything from the file*. Compare against the same question in a plain claude.ai tab with no context.
4. **Deliberate update test:** edit CLAUDE.md, add one thing that changed this week, save, start another fresh session, and confirm it knows without being told.
5. **Monthly reminder (printed Step 4):** calendar event "Update CLAUDE.md."

## Orchestration-Workspace Walkthrough (keyed to the printed steps)

1. **Inventory:** same five questions, any editor.
2. **Shape it, twice:** ask your assistant to produce (a) **Gemini Gem instructions** and (b) an **Agent Manager Project Description** — same context, the first written for conversation, the second for task-based work; each under 300 words.
3. **Gem container:** gemini.google.com → **Gem Manager → New Gem** → name it "Working Context" → paste version (a) into the Instructions field → **Save**. Test inside the Gem vs. a plain Gemini chat.
4. **Project memory:** Antigravity IDE → **CMD+E** (Mac) / **CTRL+E** (Windows) → **Agent Manager** → **New Project** → paste version (b) into the **Project Description** field → save. Start an Agent task in the project and confirm the response reflects your context unprompted.
5. **Monthly reminder:** update both the Gem instructions and the Project Description when it fires.

---

## Changelog

- **Fall 2026** — Page created from the Fall 2026 print edition. CLAUDE.md (project + `~/.claude` personal scope) confirmed; Gemini **Saved info** page confirmed as the current name of its user-visible memory; ChatGPT memory controls confirmed under Settings → Personalization. No assistant currently offers one-click memory export.
- *(next entry goes here — date + what moved)*
