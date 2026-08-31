# Retrofit Pass — Chapters 2, 5, 6 (DIAL restoration)

Per Dr. Lee's decision after HANDS-ON-STRATEGY.md: the COLLAPSE pattern applied to ch02/ch05/ch06 is retired. Tracks B and C are **restored in print, DIAL-style** (the ch09/ch10 pattern): full exercise structure in print, every step named for the evergreen decision it sets, de-branded to the book's three surface types, with literal click-paths/menu names/shortcuts moved to one-line companion pointers. Originals in chapters/ untouched. Track A kept exactly as it stood in the drafts (heading level adjusted only where a Track A wrapper heading was needed).

## Pattern applied (all three chapters)

- Replaced the COLLAPSE-era "one paragraph + pointer" with the standard **"One Exercise, Three Surfaces"** admonition used in ch09/ch10 ("You only need to complete one track… current versions of all three tracks are on the companion page at drlee.io/chNN").
- De-branding vocabulary: *terminal agent inside a development environment*, *agent-orchestration workspace / manager view*, *ecosystem-native assistant*, *reusable container*, *context file* (introduced generically per Ch 7's convention — no CLAUDE.md in print), *deliverable* (not Artifact), *change viewer* (not diff viewer, in ch06 it's "the environment's change viewer"), *read-only planning state* (no Shift+Tab//plan).
- Steps named for decisions: scope (working folder / personal / project), standing-brief-by-interview, persona (Role/Context/Rules/Format), naming-as-scope-statement, least-friction baseline comparisons, approval gate, plan-as-contract, run-twice control.
- No regressions of prior audit fixes verified by grep: no Antigravity / "2.0" / CMD+E / Ctrl+backtick / claude> / CLAUDE.md / Agent Manager / capital-A Artifact / code.claude.com / Ultraplan / Opus-Plus in any of the three drafts. Isolation language, Architect-and-Builder, Deep Planning, date scrubs, and all "Is this still true?" boxes preserved.

## ch02.md

- Exercise intro line updated ("produces a configured workshop… Complete one track before moving to Chapter 3").
- Former Parts 1–3 wrapped as **Track A — Chat Assistant** (Parts demoted to ####). Content unchanged.
- **Track B — Terminal Agent** restored from original steps 1–10, compressed to 6 decision-named steps: surface setup → scope dial (one working folder; "context anchored to a place, not an account") → standing-brief interview (original interview prompt kept nearly verbatim, CLAUDE.md → "context file… each tool has its own standard filename") → review-before-save ("a file you own") → fresh-session persistence test → browser control experiment. Original submission restored, adjusted to new step names/terms.
- **Track C — Ecosystem Assistant + Orchestration Workspace** restored from original steps 1–11, compressed to 8 steps: container creation → persona dial by hand (Role/Context/Rules/Format kept; the "ask your thinking partner to write it" option kept with the tools-don't-know-each-other caveat) → naming dial → baseline test → orchestration view → project-scope dial ("same persona decision… set at project scope") → first background task (original example prompt kept, "last 90 days" → "recent") → approval-gate review (ties to the Cowork-shape approval-gate teaching in the body). Submission restored ("Agent Manager Artifact" → "deliverable from your orchestration-workspace task").
- The COLLAPSE-era **"A Glimpse Ahead: The Orchestration Surface" teaser admonition deleted** — Track C now *is* the preview, so the teaser (which named Antigravity and Agent Manager) is redundant. This also removes the last product mention of Antigravity from the chapter body. Flag if Dr. Lee wants a one-line product mention somewhere; my read is the companion page is the right home.
- Reflection Q2 adjusted to be track-safe: "the standing brief that came out of your configuration step — whether an AI interview wrote it for you (Tracks A and B) or you wrote it by hand using Role/Context/Rules/Format (Track C)." Q1 and Q3 unchanged (Q3's Gem reference is fine — Gems are in the printed chapter body).
- Left intact: closing lines, "Is This Still True?" sidebar, case study, all body sections.

## ch05.md

- Track A unchanged (already tool-agnostic per the audit pass), wrapped under **Track A — Chat Assistant**; its submission kept verbatim.
- **Track B — Terminal Agent: The Six Floors as Files** restored (title per HANDS-ON 3.1's suggestion). Lesson sentence added up front: floors become *files in a folder*. Six floors mapped: F1 prompt pair at the agent prompt; F2 edit the Chapter-2 context file + fresh-session reload; F3 commission a Meeting Prep specialist ("/agents" wizard → "your tool has a built-in way to define one; current command on companion page"; original job description kept verbatim; added ch09-style "read what it wrote and edit it"); F4 point at real documents by path; F5 memory test via the file ("a file you own, not a vendor's memory feature" — consistent with the audit's Discipline Five rewrite); F6 harness specification (original prompt kept verbatim); step 7 organize artifacts. Submission restored, "CLAUDE.md" → "context file."
- **Track C — Ecosystem Assistant + Orchestration Workspace** restored. F1 assistant prompt pair; F2 container ("a Gem, in this chapter's example" — allowed: Gems are taught in Ch 2 body); F3 container improves its own instructions (original prompt kept); F4 A/B context test; F5 Working Brief at **project scope** in the orchestration workspace; F6 **scheduled recurring task** = the harness ("Every Monday morning" — time-of-day removed from print; original said 7:30 AM, now companion detail) + a can't-schedule-yet fallback line ("log that gap — it is a verification answer, not a failure," echoing HANDS-ON 3.3's ch13 move). Submission restored ("Gem instructions" → "container instructions," "Project Description" kept lowercase generic).
- Reflection lead-in restored to the original's "in one of the three tracks." Bonus multi-surface reflection kept as the audit pass wrote it (already surface-neutral).
- "Is this still true?" box untouched, still sits between Track C and Reflection.

## ch06.md

- Surface-pointer paragraph (COLLAPSE remnant) deleted; replaced with the standard three-surfaces admonition **after Step 1** (Choose the task), so the task choice stays common to all tracks — mirrors the original's structure.
- Track A unchanged except: wrapped under **Track A — Chat Assistant**, and **new Step 6 "Run the control experiment"** added per HANDS-ON 3.3 item 2 (the run-twice experiment brought into print; "the most persuasive ten minutes in this chapter"). Track A submission extended from four parts to five to include the control output.
- **Track B — Terminal Agent** restored from original steps 1–10 as 8 decision-named steps: review artifact (plan-review.txt kept — it's a filename the student invents, not a product path) → fix the objective before the tool → demand the plan (original instruction verbatim; native read-only planning state mentioned generically with companion pointer — consistent with the ch06-3 stub's audit language) → written skeptical critique (a/b/c kept) → push back on all three → approve and watch the contract execute ("change viewer" for diff viewer; ties to "It can look, but it cannot touch") → control experiment (was original step 9) → file four artifacts. Submission restored + extended to include the control output (five parts).
- **Track C — Agent-Orchestration Workspace** restored from original steps 1–10 as 7 steps: manager view → design the comparison → Run 1 no-plan → written critique → Run 2 plan-first with approval gate (original instruction kept; "Plan Artifact" → "written plan"/"plan deliverable") → skeptical pushback + approval → side-by-side comparison on the original three dimensions + check against critique notes. Submission restored (four parts + two sentences, de-branded).
- Reflection: kept the audit pass's fixed wording ("formal plan artifact in an orchestration workspace," "more than one surface") — already track-safe for three tracks.
- "Is this still true?" pricing-page box untouched.

## Companion pages created (new companion/ directory)

- **companion/ch02-companion.md**, **companion/ch05-companion.md**, **companion/ch06-companion.md** — drafts for the drlee.io pages. Each: "Last verified: Fall 2026" header, current product mapping table, per-track click-path sheets keyed to the printed step numbers (per HANDS-ON 3.5 "mirroring the printed step numbers"), and a changelog stub. Perishables parked there: claude.ai/download, Settings → Custom Instructions, Gem Manager → New Gem, Get API key → Create API key, temperature-slider location, Antigravity IDE + Agent Manager + CMD+E/CTRL+E, Ctrl+backtick, Claude Code + `claude>` + CLAUDE.md + `/agents`, exit/claude reload, Shift+Tab ×2 + `/plan` + `~/.claude/plans/` + diff viewer, Plan/final Artifacts, Opus/Sonnet/Haiku tier names, 7:30 AM Monday scheduling example.
- Deliberate omissions from companion pages: "Antigravity 2.0" version label and "free during preview" (audit says delete at minimum — noted in each changelog); code.claude.com URL replaced with "search 'Claude Code quickstart'" since the audit flags all such doc URLs (bug 13) as unstable — Dr. Lee can pin a live URL at publish time.

## Flags

1. **ch02 orchestration teaser removed** (see above) — confirm Dr. Lee is happy losing the in-body Antigravity name mention entirely; the companion page carries it.
2. **Step-count drift vs. originals:** Tracks were compressed (ch02 B: 10→6, ch02 C: 11→8, ch06 B: 10→8, ch06 C: 10→7) by merging button-only steps into their decision steps. Companion track sheets are keyed to the **new printed step numbers**. If print/companion parity ever needs the old granularity, split from the companion side, not print.
3. **ch05 Track C F6 time-of-day** ("7:30 AM") demoted to companion example; print says "Every Monday morning." Matches the audit's ch13 "briefing time varies — pick one" spirit.
4. **ch06 Track A submission grew to five parts** (control experiment). Downstream files (quizzes/canvas/case-studies) that describe the four-part submission would need the same bump in their own pass.
5. Companion pages assert current-state facts (Shift+Tab, plans directory, Cowork-in-Pro, ≈$20 pricing) **as of Fall 2026 per the audit's landscape table** — these are drafts and should be re-verified against live products before drlee.io publication.

## FIGURES-TODO

No new items. Pre-existing items in ch02-NOTES.md and ch05-06-NOTES.md still stand (role-based relabels; Architect-and-Builder and Deep Planning art renames; ch06-ultraplan.png filename still referenced by the draft so the build doesn't break).
