# cognitioneconomy.net/ch10-companion — Companion Page: Agent Teams

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 10. The printed chapter teaches the architecture — lead, teammates, shared task list, lateral messages, goal condition; this page carries the current enablement flag, display modes, command syntax, and doc URLs.

---

## Current Product Mapping

| Book role | Current product | Where |
|---|---|---|
| Chat assistant (Track A) | Claude Desktop / claude.ai | claude.ai/download |
| Terminal agent (Track B) | Claude Code — **agent teams** feature | code.claude.com/docs/en/agent-teams |
| Orchestration workspace (Track C) | Antigravity IDE — Agent Manager view | antigravity.google/docs/ide-overview |

## Track B Step 1 — Enabling Agent Teams (Fall 2026)

The printed step says "make sure agent teams are enabled." Current one-line setup:

- Update Claude Code and confirm you are on **version 2.1.32 or later**.
- The feature is behind an opt-in flag: set **`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`** to **`1`** (environment variable or settings file), then restart Claude Code.
- Official setup guidance: **code.claude.com/docs/en/agent-teams**.
- If your build no longer requires the flag, the feature went default-on — log it and skip this step.

## Display Modes (the "cycle vs. panes" choice in print)

- **In-process mode (default):** all teammates run inside your main terminal; cycle through them with the keyboard shortcut (currently **Shift+Tab** cycles; check the footer hints in your build). Works everywhere.
- **Split-pane mode:** each teammate gets its own pane so you watch all of them at once. Requires a multiplexer-capable terminal setup (e.g., tmux). Cosmetic either way — the team runs the same.

## Track B Step 5 — Goal-Condition Syntax (Fall 2026)

The printed finish-line feature is currently the **`/goal`** slash command:

```
/goal the one-page comparative brief is complete, includes findings from
both Alex and Sam with at least three specific data points each, and the
task list is empty
```

- Full syntax reference: **code.claude.com/docs/en/goal**.
- After each turn, a separate small fast model is called as the evaluator; it reads the conversation and answers yes/no against your condition. It has no tools of its own — write conditions the conversation itself can prove (the printed guidance).
- Bound it with a stop clause if you want: *"…or stop after twenty turns."*
- Clearing: setting a new `/goal` replaces the old one; the condition clears automatically when met.

## Track C — Current Click-Paths (per printed step)

1. **Open the orchestration view:** Antigravity IDE → **CMD+E** (Mac) / **CTRL+E** (Windows) → **Agent Manager**. Docs: antigravity.google/docs/ide-overview.
2. **Two parallel workspaces:** start two new agent tasks in two separate workspaces (one per investigation angle). The dashboard shows both running in parallel.
3. **Watch:** each agent produces **Artifacts** as it works; click an agent's tile to inspect in detail.
4. **Synthesis:** start a third agent in a synthesis workspace with both prior workspaces as context.
5. **Save the brief** from the Artifacts panel.

## The "Is This Still True?" Checks — Fall 2026 Answers

1. *Available on your plan / default or setting?* — Claude Code: all paid plans, behind the experimental flag above (not yet default-on at verification time).
2. *What is the finish-line feature called, and how strict is its evaluator?* — `/goal`; evaluator is deliberately strict — repeated "not yet" usually means the condition is genuinely unmet.
3. *Recommended starting team size?* — Official guidance: **3–5 teammates**; most work is best at 3.

---

## Changelog

- **Fall 2026** — Page created from the Fall 2026 print edition. `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` flag confirmed on Claude Code ≥ 2.1.32; `/goal` command and docs URLs confirmed; in-process vs. split-pane modes confirmed; Agent Manager parallel-workspace flow confirmed.
- *(next entry goes here — date + what moved)*
