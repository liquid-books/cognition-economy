# cognitioneconomy.net/ch06-companion — Companion Page: Plan Mode

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 6. The printed chapter teaches the plan-then-execute discipline and the Architect-and-Builder Pattern; this page carries the current buttons, shortcuts, and tier names.

---

## Current Product Mapping

| Book role | Current product | Where |
|---|---|---|
| Chat assistant (Track A) | Claude Desktop / claude.ai | claude.ai/download |
| Terminal agent (Track B) | Claude Code inside the Antigravity IDE's integrated terminal | antigravity.google · Claude Code docs |
| Orchestration workspace (Track C) | Antigravity IDE — Agent Manager view | antigravity.google |

## Architect-and-Builder — Current Tier Names

As of this page's verification date, Anthropic's tiers are **Opus** (flagship / Architect) and **Sonnet** (balanced / Builder), with a faster **Haiku** tier below. Other vendors' current pairs are listed on the model-roster page (cognitioneconomy.net/model-roster). The book's rule stands regardless of names: if the pricing page shows two or more models at different price points, plan on the expensive one, execute on the cheap one.

## Dedicated Planning Modes — Current State

- **Claude Code:** read-only **Plan Mode** — cycle into it with **Shift+Tab** (press twice from normal mode); the footer indicator shows the current mode; **`/plan`** also works. In Plan Mode the agent can read, search, and analyze but cannot create, modify, or execute. Approved plans persist as files (currently under `~/.claude/plans/`) that you can reopen and edit.
- **Extended/long-running planning:** the dedicated long-horizon planning feature the chapter calls **Deep Planning** currently ships under a product-specific name — check your tool's release notes; the practice predates the feature and works in any chat window.

---

## Track Sheet — Track B (Terminal Agent) · v. Fall 2026

Printed step → current buttons:

1. **Review artifact:** create *plan-review.txt* via the IDE file browser (right-click → New File) or ask Claude Code to create it.
2. *(no buttons — decision step)*
3. **Demand the plan:** either paste the printed instruction, or enter Claude Code's native Plan Mode with **Shift+Tab ×2** (read-only enforcement). Both produce a reviewable plan; the native mode guarantees nothing executes early.
4. **Critique:** open plan-review.txt in the editor pane; the terminal and editor sit side by side in the Editor surface.
5. *(no buttons — pushback happens in the terminal conversation)*
6. **Watch execution:** file creations/modifications appear live in the IDE file browser; click any changed file to open the **diff viewer** and see exactly what changed.
7. **Control experiment:** type `exit`, then `claude` for a fresh session (or open a second terminal tab).
8. **Filing:** save via the file browser; four files in your workshop folder.

## Track Sheet — Track C (Orchestration Workspace) · v. Fall 2026

1. **Open the manager view:** Antigravity IDE → **CMD+E** (Mac) / **CTRL+E** (Windows) → **Agent Manager**.
2. *(no buttons — design step)*
3. **Run 1:** **New workspace** (or New Project) → new **Agent** task → full task description → **Submit**. Output arrives as an **Artifact**.
4. **Critique notes:** any note-taking surface; Artifacts can be opened side by side with your notes.
5. **Run 2:** second workspace → new Agent task → printed plan-first instruction. The plan arrives as a **Plan Artifact**; the agent waits for your written approval in the task thread.
6. **Pushback + approval:** type your challenge in the task thread; the agent revises the Plan Artifact in place. Then type "Plan approved. Proceed to execution."
7. **Comparison:** open both final Artifacts side by side from the Agent Manager dashboard.

---

## Changelog

- **Fall 2026** — Page created from the Fall 2026 print edition. Shift+Tab / `/plan` shortcuts confirmed on current Claude Code build; plans directory confirmed at `~/.claude/plans/`; Antigravity Plan Artifact + approval-gate flow confirmed. "Ultraplan" branding retired in the book — tracked here as "Deep Planning" per the print rename.
- *(next entry goes here — date + what moved)*
