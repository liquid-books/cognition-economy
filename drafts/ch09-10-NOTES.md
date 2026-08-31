# Chapter 9 & 10 — Revision Notes (AUDIT-2026-08)

*Completed by continuation agent after prior agent died mid-task. drafts/ch09.md was verified (already complete); drafts/ch10.md was written fresh from chapters/ch10.md. Originals untouched.*

---

## Chapter 9 — VERIFIED (no changes needed)

The existing `drafts/ch09.md` fully implements the audit's CHAPTER 9 section:

- ✅ Table retitled **"Three Built-In Specialist Roles You Will Usually Find"** with Scout / Planner / Generalist rows and the footnote *"The names differ by tool and change between releases; the roles do not."*
- ✅ "Sonnet or higher" → "your provider's mid- or top-tier reasoning model, not its fastest and cheapest one — the work involves judgment about source quality…" (Track B step 5).
- ✅ Track B/C rewritten dial-per-step ("Set the scope dial: personal… Exact click-path: companion site."), all wizard steps and code.claude.com / Antigravity 2.0 / CMD+E references removed; companion pointers use cognitioneconomy.net/ch09-companion.
- ✅ Case de-branded and date-scrubbed: "$87M in 2025" → "just under $90 million in annual revenue"; "Q1 2026" gone; "Gemini Enterprise / custom GPTs for 18 months" → "enterprise licenses for two major assistants… custom specialist containers"; "ran a time-and-motion study across forty consultants" per audit.
- ✅ Reflection (bug #7) rewritten to work for any single track ("After completing your track…"), no cross-tool comparison.
- ✅ Three-track admonition collapsed per Move 1 (one paragraph describing the three surface types + cognitioneconomy.net/ch09-companion).
- ✅ "Is this still true?" sidebar present.
- **ch09 stub files** (`ch09-1/-2/-3`): originals are empty scaffolds ("Chapter coming soon") with nothing perishable — no drafts needed.

## Chapter 10 — NEW DRAFT (`drafts/ch10.md`)

### /goal section → "Setting a Finish Line"
- Section heading "The /goal Command" → **"Setting a Finish Line."** Slash command introduced once in parentheses ("Setting a goal condition (in some tools, a `/goal` slash command)…"); **"goal condition"** used everywhere else — admonition retitled "Why a Finish Line Matters More Than It Sounds," figure caption, discussion prompt ("analyze the role of the goal condition… how did setting a finish line change…"), exercise ("a working goal-condition session," Track B step 5), and closing list ("Solo, sub-agent, team, goal condition. Four moves.").
- Evaluator abstracted per audit: "a separate small fast model is automatically called as an evaluator" → "a separate lightweight check runs after each turn and answers one question: is the condition met? Because that check typically sees only what's in the conversation, write conditions the conversation itself can prove." ("Evaluator" retained only in the guardrails paragraph and case as a common noun.)
- Figure alt text updated ("Claude working" → "a model working"); label `fig-ch10-goal` preserved.

### Track B step 1 (most fragile sentence in the book)
- Replaced version 2.1.32 + `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` flag + code.claude.com URL with the audit's evergreen phrasing: "Make sure agent teams are enabled… behind an opt-in setting at press time; may be on by default by the time you read this. The one-line setup is on the companion site (cognitioneconomy.net/ch10-companion)."
- Step 5 `/goal` syntax + doc URL → set a goal condition; syntax on companion page.
- Step 3 keyboard-shortcut cycling → "Check in on each teammate's view."

### Display modes
- Two-paragraph in-process vs. split-pane discussion → one sentence: "Depending on your tool and your setup, you can either cycle through teammates one at a time in a single window or watch each teammate in its own pane — the choice is cosmetic, and the team runs the same either way." Coordination figure alt text updated to match.

### Vendor quotes paraphrased without attribution
- "The official Claude documentation describes this perfectly: 'With multiple independent investigators…'" → "Run several independent investigators who are actively trying to disprove each other, and the theory that survives is far more likely to be the real answer."
- "The official guidance is to start with three to five teammates" → **"A sensible default is three to five teammates."**

### Numbers
- "A team of four is roughly four times the cost" → **"A team of N is roughly N times the token cost"**; downstream "paid four times more" → "multiplied the cost"; admonition "four times the token cost" → "several times the token cost."
- "two years from now, will look obvious" → "in hindsight, looks obvious."

### Case (Lumenax) date-scrub
- "Founded in 2017" deleted; "crossed $42M in late 2024 and entered 2025 with…" → "had recently crossed $42M… and was facing…"; "second Tuesday of May 2026" → schedule described without a date. Intra-day clock times (8:14 a.m., 10:47, 11:43) kept — they're scene texture, not calendar rot.
- "Claude Code's agent teams feature" → "an agent team"; "`/goal` command twice" → "set goal conditions twice."

### Tracks collapsed per Move 1
- Three-track admonition ("Claude Desktop / Claude Code / Antigravity 2.0 IDE" + three doc URLs) → one paragraph describing the three surface types + **cognitioneconomy.net/ch10-companion**.
- Track A retitled "Chat Assistant," de-branded (claude.ai/download removed), prompts and structure preserved verbatim.
- Track C retitled "Agent-Orchestration Workspace"; Antigravity 2.0 / CMD+E / antigravity.google URL / "Artifacts" product term removed; same five steps, "Artifacts" → "deliverables."

### Reflection track letters (bug #8)
- Original asked everyone to compare "Track A" (lateral communication) vs "Track B" (visual workspaces) — mislabeled and assumed two tracks. Rewritten conditionally per track: Track B = lateral communication question; Track C = parallel-but-isolated question; Track A = synthesis-step question. Works for any single track.

### Added
- "Is this still true?" end-of-chapter sidebar (Move 5): teams on by default? finish-line feature name? recommended team size? — cognitioneconomy.net/ch10-companion.

### Left alone (per audit)
Priya's board-meeting opener (verbatim); Hallway Argument admonition; sub-agents vs. teams "flip one arrow" section; three conditions for team territory; lead-assigned vs. self-claim; plan-first checkpoint; naming-teammates admonition; completion-condition loop concept; three traps + maturity arc; orchestrator-doing-the-work antipattern; unused-team trap; case tension structure; Track A prompts; discussion guidelines; all figure directives, labels, and frontmatter.

## FIGURES-TODO
- **ch10-coordinating.png** — inset depicts "in-process vs. split-pane display modes" (alt text updated in draft; image itself still shows the modes). Relabel inset generically ("two ways of viewing teammates") or crop.
- **ch10-goal.png** — alt/caption said "Claude working" and "/goal pattern"; draft now says "a model working" / "finish-line pattern." If the image itself renders "/goal" text, relabel to "goal condition."
- ch09 figures: none flagged (checked; no baked-in dates/versions).

## Flags / ambiguities
- Kept "goal evaluator confirmed the condition was met" in the case and "Trust the evaluator to be strict" in guardrails — "evaluator" as a common noun seemed fine once the mechanism was abstracted; easy to sweep to "the check" if Dr. Lee prefers total consistency.
- Lumenax's "$42M ARR" retained (audit didn't flag the figure, only the dates). Move 3 rounding could apply ("low forties of millions" as in Ch 13's case) — deferred to Dr. Lee.
- Chapter frontmatter tag `goal` retained (it's a concept tag, not a command reference).
- ch10 stub files (`ch10-1/-2/-3`) are empty scaffolds like ch09's — no drafts needed.
- Meridian dedupe (bug #5) does not touch Ch 9/10 — cases here are Cascade and Lumenax.
