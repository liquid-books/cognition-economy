# Changelog — Additions to Chapters 7 and 8 (ADDITIONS-SPEC-2026-08)

**Agent scope:** chapters/ch07.md, chapters/ch08.md (+ one-line cross-refs in subfiles).
**Method:** Additive only. No existing paragraphs, case studies, exercise tracks, or step numbering were edited, moved, or renumbered.
**Facts verified (Aug 2026)** via web search/fetch against:
- claude.com/docs/office-agents/excel (Claude for Excel: GA on Pro/Max/Team/Enterprise; AppSource listing "Claude for Microsoft 365" WA200010725; supported builds web/Windows/Mac; cell-level citations; formula-safe updates; native ops; overwrite protection; no macros/VBA/data tables; prompt-injection warning; "not for final deliverables/audit-critical without verification").
- claude.com/docs/office-agents/powerpoint (template-aware slide generation, pinpoint edits, native charts/diagrams; same install route; Home-ribbon activation, Tools → Add-ins on Mac).
- claude.com/docs/office-agents (Work across M365 apps — shared context spanning Excel/PowerPoint/Word/Outlook; per-app persistent Instructions).
- slack.com/help/articles/53532192117267 (Use Claude in Slack: Marketplace install → Add to Slack → Allow; Agents & tools → Apps → Claude → Home tab → Connect Account; add to channel via channel name → Agents & apps tab; thread context = 50 most recent replies, channel = 20; note that Claude Tag replaces the Claude app in Slack starting Aug 3, 2026).
- claude.com/product/tag (Claude Tag: tag @Claude in any thread, reads context, does work, posts in-thread; standing instructions, scheduled routines, cross-thread memory, agent identity/tool access on Team & Enterprise; Teams version coming).
- support.claude.com article "Retrieval augmented generation (RAG) for projects" (Projects auto-switch from in-context to RAG mode near the context-window limit; project knowledge search tool; ~10x capacity expansion; automatic, no configuration).

## chapters/ch07.md

1. **New section: "Retrieval and RAG: The Design Pattern Behind Every Memory System"** — inserted after "The Compounding Value of Memory," before the Case Study.
   - Frames the chapter's underlying question ("how does knowledge get in front of the model?") with three answers: (1) stuff the context window, (2) retrieve (RAG, defined), (3) live connector.
   - Claude Projects presented as consumer RAG: in-context while small, automatic switch to project-knowledge-search retrieval past the window limit (verified against Anthropic support article); NotebookLM/Gemini grounding named as same pattern.
   - Plain four-question decision framework per spec: data size, freshness, provenance, cost — plus a closing mapping back onto the chapter's existing three memory tiers.
   - New figure directive: `ch07-rag-decision.png`.
   - **New activity: "Try It: One Question, Three Ways In"** — 6 numbered steps: pick a real ≥5-page document + one checkable question (identical wording reused); (a) paste-in in a fresh chat, (b) Project knowledge (sidebar → Projects → New Project, knowledge panel, fallback line), (c) live web search/connector (tools-menu toggle, label-may-vary line); a printed 6-row comparison table (answer, accuracy, effort this time, effort next 50 times, freshness, source citation); recommendation sentence with explicit permission for hybrid answers. Deliverable: completed table + recommendation sentence.

2. **End-of-chapter comment block** `<!-- NEW IMAGES NEEDED: ... -->` for the one new figure.

## chapters/ch08.md

1. **New section: "The AI Comes to Your Documents: Claude for Excel and Claude for PowerPoint"** — inserted after "The Plugin That Changes Everything," before "Building Your First Plugin."
   - Both add-ins as real Claude surfaces (official Anthropic add-ins via Microsoft AppSource; Pro/Max/Team/Enterprise; web/Windows/Mac).
   - Excel capabilities (cell-level citations, formula-preserving updates, model building, error tracing, native ops, overwrite protection) and PowerPoint capabilities (template/slide-master awareness, pinpoint edits, native charts) per docs.
   - Shared context across Excel/PowerPoint/Word/Outlook add-ins per spec.
   - "When in-app beats copy-paste" — the rule of structure (formulas/templates destroyed at the copy-paste border).
   - Two cautions carried from official docs: human verification for deliverables (cross-ref Ch 1 discipline) and prompt injection in external spreadsheets (cross-ref Ch 14).
   - New figure directive: `ch08-office-addins.png`.
   - **New activity: "Try It: Have Claude Build a Model in Your Spreadsheet — Then Check Its Math"** — 7 numbered steps: AppSource "Get it now" install with in-app route (**Home → Add-ins**, fallback lines for **Insert → Get Add-ins** on older builds and **Tools → Add-ins** on Mac, plus blocked-Office-Store fallback = personal free account at office.com); open sidebar + sign in with Claude account; real workbook or a fully-specified 6-row starter dataset; exact paste-in prompt to build a 12-month projection with live formulas; interrogate a cell for cell-level citations; **verify one formula by hand** (formula bar + hand calculation + previous-month vs. anchor-compounding trace); flex an assumption. Deliverable: workbook/screenshot + the verified formula written out + hand-calc result + one sentence on the anchoring choice. Optional PowerPoint extension noted (same add-in).

2. **New section: "Claude Tag for Slack: The AI in the Channel"** — immediately after the Office section.
   - Claude Tag as the Slack-native Claude (replacing the earlier Claude app as of Aug 3, 2026); tag @Claude in a thread → reads context → summarizes/drafts/acts → posts in-thread.
   - Positioned in the plugin/channel story as the pattern inverted (AI installed into the channel as shared cognition, not channel data pulled into a private chat); forward cross-ref to Ch 13 channels.
   - Team/Enterprise ceiling named (standing instructions, scheduled digests, cross-thread memory, audited agent identity) + one governance note.
   - New figure directive: `ch08-claude-tag-slack.png`.
   - **New activity: "Try It: Tag Claude Into a Real Thread"** — 8 numbered steps with **fallback-first workspace path** (create a free personal workspace at slack.com/get-started — the explicit no-admin-rights path per spec); Marketplace install (Add to Slack → Allow, permission-reading habit); Connect Account route (Agents & tools → Apps → Claude → Home → Connect Account) with plan-limit fallback line; create channel + add Claude via channel name → Agents & apps tab; author a 10+ message thread with planted checkable facts ("you are the answer key"); exact @Claude summary prompt; exact @Claude draft-reply prompt; a deliberate missing-fact probe tied to Ch 1's hallucination discipline. Deliverable: summary + draft screenshots/text + two sentences.

3. **End-of-chapter comment block** `<!-- NEW IMAGES NEEDED: ... -->` for the two new figures.

## Subfile cross-refs (one line each, appended)

- `chapters/ch07-1-memory-in-ai.md` → pointer to Ch 7's RAG/retrieval section.
- `chapters/ch08-1-what-plugins-are.md` → pointer to Ch 8's Office add-ins + Claude Tag sections.
- `chapters/ch08-3-installing-plugins.md` → pointer to the two new install walkthroughs.

## Not touched

- All existing prose, figures, case studies, discussion guidelines, Applied Exercise tracks and step numbering in ch07.md and ch08.md.
- Quizzes, case-studies, canvas-pages, exercises directories (new material is additive sections + Try It blocks; existing assessments remain valid).
- All other chapters (other agents' scope).
