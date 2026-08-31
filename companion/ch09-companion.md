# cognitioneconomy.net/ch09-companion — Companion Page: Sub-Agents

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 9. The printed chapter teaches the five dials (scope, system prompt, tools, model, permissions) and the built-in specialist *roles*; this page carries the current commands, wizard screens, and what each vendor calls its built-ins this year.

---

## Current Product Mapping

| Book role | Current product | Where |
|---|---|---|
| Chat assistant (Track A) | Claude Desktop / claude.ai | claude.ai/download |
| Terminal agent (Track B) | Claude Code | code.claude.com/docs/en/quickstart · sub-agents doc: code.claude.com/docs/en/sub-agents |
| Orchestration workspace (Track C) | Antigravity IDE — Agent Manager view | antigravity.google/docs/ide-overview |

## Current Built-In Specialist Names (Fall 2026)

The book's role names → what your tool calls them today:

| Book's role | Claude Code | Notes |
|---|---|---|
| The Scout | **Explore** | Fast/cheap model, read-only search-and-survey |
| The Planner | **Plan** | Inherits main model; read-only research before proposing a plan |
| The Generalist | **general-purpose** | Inherits main model; multi-step read-and-act tasks |

Other terminal agents ship equivalent roles under their own names — run the chapter's "Is this still true?" check: ask your tool *"list your built-in sub-agents and what each one does."*

## Track B — Current Click-Paths (per printed step)

1. **Open the agent creator:** type **`/agents`** at the `claude>` prompt. The interface shows existing specialists and offers create/edit.
2. **Scope dial — personal:** in the `/agents` interface, choose **Create new agent** → scope **Personal** (stored under `~/.claude/agents/`, available in every project). The alternative, **Project** scope, stores under `.claude/agents/` in the current repo and is shared with anyone who works in it.
3. **System-prompt dial:** choose **Generate with Claude**, paste the printed plain-English brief, and let it draft the identifier, description, and system prompt. Then edit — the definition is a plain markdown file you own.
4. **Tools dial:** the wizard asks which tools to grant. Select **web search** and **read-only file access** only; leave write/edit/execute unchecked.
5. **Model dial:** current Anthropic tier names are **Opus** (flagship), **Sonnet** (balanced), **Haiku** (fast/cheap). Pick Sonnet or higher for the printed research specialist; "inherit" follows your main session's model.
6. **Save and test:** save, then invoke it on three real competitors — by name (*"use the competitor-research agent on …"*) or let routing pick it up.

## Track C — Current Click-Paths (per printed step)

1. **Open the orchestration view:** Antigravity IDE → **CMD+E** (Mac) / **CTRL+E** (Windows) → **Agent Manager**.
2. **New asynchronous agent:** **New Agent** action → asynchronous task. Async agents run in parallel across workspaces without blocking your other work.
3. **Standing instruction:** paste the printed specialist brief into the task description field.
4. **Run:** submit a real competitor name; leave the view; return when done.
5. **Deliverable:** finished output arrives in the **Artifacts** panel (markdown brief / diff / report). Verify the citations resolve.
6. **Parallel:** queue two more competitors as separate async agents and watch the Agent Manager track all three.

## The "Is This Still True?" Checks — Fall 2026 Answers

1. *Which built-in roles ship today?* — Claude Code: Explore, Plan, general-purpose (table above).
2. *Which scopes can a specialist have?* — Claude Code: **Personal** (`~/.claude/agents/`) and **Project** (`.claude/agents/`); project definitions can be committed and shared with a team via the repo.
3. *Which models can you assign?* — Any available tier per specialist (Opus/Sonnet/Haiku) or inherit; Antigravity task agents use the workspace's configured Gemini-family models.

---

## Changelog

- **Fall 2026** — Page created from the Fall 2026 print edition. `/agents` wizard (Library tab → Create new agent → Personal/Project scope → Generate with Claude) confirmed on current build; built-in names Explore/Plan/general-purpose confirmed; Agent Manager async-agent flow and Artifacts panel confirmed.
- *(next entry goes here — date + what moved)*
