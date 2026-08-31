# Chapters 5 & 6 — Revision Notes (AUDIT-2026-08)

Status: COMPLETE. A prior agent produced drafts/ch05.md, drafts/ch06.md, all seven ch05 stubs, and seven of twelve ch06 stubs, then died. This pass verified those drafts against the audit spec, found them fully compliant, and created the five missing ch06 stub drafts. Originals in chapters/ untouched.

## Chapter 5 — ch05.md (verified complete; no gaps found)

- **Opening rewrite:** "In 2023, 'prompt engineer' … $300,000 a year" → "When generative AI first went mainstream, 'prompt engineer' briefly became one of the hottest job titles…"; salary → "salaries that made the news."
- **Discipline Four → heuristics:** "the order of context matters" restated as working rules ("as a working rule, put framing first… How strongly this matters varies between models and releases"); third point reframed as "treat long conversations with suspicion" with a behavioral signal.
- **Discipline Five rewrite (the big one):** "AI has a dirty secret. It does not remember you… This is not a bug. It is the design." → "AI memory is unreliable by default. Some tools remember nothing… others remember a little, on their own terms… you do not control what persists." Three layers kept verbatim; added the fourth "convenient-but-opaque" built-in-memory layer paragraph per audit. Figure caption updated to "Memory you do not control is not your memory."
- **Discipline Six:** added present-tense harness example (office add-ins sharing conversation context across documents) per audit's optional item.
- **Meta-prompting section:** "Claude" → "your assistant"; "Creating a Gem" → "Configuring a reusable container (a Project, a Gem)."
- **Case (Meridian Wealth Partners):** "early 2024" deleted (initiative now undated); "$4.2 billion … 1,800 relationships" → "roughly $4 billion … nearly two thousand"; "Claude enterprise subscription" → "enterprise AI subscription"; "library of Skills" → "library of reusable skills." Discussion prompt unchanged (evergreen).
- **Exercise:** Tracks B/C collapsed to companion pointer (cognitioneconomy.net/ch05-companion); three-track admonition replaced with one paragraph naming the three surface types. Track A rewritten tool-agnostic.
  - **ChatGPT menu-label bug fixed:** "Go to your Claude system prompt (Settings → Custom Instructions)" → "Open your standing instructions — the system prompt you wrote in Chapter 2 (your tool will call this preferences, custom instructions, or a project brief)."
  - **Gem/Track bug fixed:** "Save that skill as a Gem" (in the Claude track) → "Save that skill in your tool's reusable container — a Project, a Gem, whatever your tool calls it."
- **Verify box added** ("Is this still true?" admonition): (1) ask the AI what it knows about you — "whatever it says is the memory layer you currently do not control"; (2) find your standing instructions; companion pointer.
- **Reflection:** bonus reflection reworded surface-neutral (no Desktop/Gemini/Claude Code/Agent Manager names).

## Chapter 5 stubs — ch05-1 … ch05-7

Evergreen (scaffold-only, no perishable content). Copied verbatim; verified byte-identical to originals via diff.

## Chapter 6 — ch06.md (verified complete; no gaps found)

- **Architect-and-Builder rename everywhere:** section heading, figure label (fig-ch06-opus-sonnet → fig-ch06-architect-builder), alt text, caption, frontmatter tag (opus-sonnet → architect-builder), and the **discussion prompt** ("Opus-Plus-Sonnet model routing pattern" → "Architect-and-Builder model routing pattern"). Opus/Sonnet named once in the prescribed parenthetical ("As this book went to press, Anthropic's tiers were called Opus and Sonnet; the names will change, the shape of the lineup will not.").
- **Body sentence swap:** "Claude Opus 4.7, for instance…" → audit's tiered-lineup sentence verbatim.
- **Ultraplan → Deep Planning:** heading, figure label (fig-ch06-ultraplan → fig-ch06-deep-planning), alt, caption, body; added parenthetical "Some tools now offer a dedicated long-running planning mode for exactly this; the practice predates the feature." "a planning conversation in Claude Desktop" → "with your assistant."
- **Multi-agent section:** "different Gems, different Claude Projects" → "separate configured containers (the reusable projects and personas you built in Chapters 2 and 4)."
- **Case date-scrubs (Meridian Capital Advisors):** "In early 2024" → "Eighteen months into the firm's AI adoption"; "before the Q2 2024 reporting cycle" → "before the next quarterly reporting cycle"; "write the Q2 market commentary" → "write the quarterly market commentary"; "$4.8 billion" → "roughly $5 billion."
- **Tracks B/C collapsed:** three-track admonition and Track B/C step lists removed; replaced with one surface-types paragraph + cognitioneconomy.net/ch06-companion pointer (describes what each online variant teaches). Track A rewritten tool-agnostic ("Claude" → "the AI"/"your assistant").
- **Verify box added:** pricing-page check ("If there are two or more models at different price points, the pattern applies"), per audit's verify-sidebar spec.
- **Reflection:** "plan Artifact" → "formal plan artifact in an orchestration workspace"; "more than one track" → "more than one surface."

## Chapter 6 stubs — status per file

All stubs are scaffolds ("Chapter coming soon") — only frontmatter titles/descriptions carry content. Pre-existing drafts verified; five missing drafts created this pass:

| Stub | Status | Change |
|---|---|---|
| ch06-1, -2, -4, -6, -7, -11, -12 | pre-existing drafts, verified identical to originals | none needed (descriptions evergreen) |
| **ch06-3-activating-plan-mode** | **created** | description scrubbed: "Shift+Tab twice. The footer indicator. The /plan slash command." → "Entering and leaving the read-only planning state. Exact shortcuts and commands vary by tool and release — current paths on the companion page." |
| **ch06-5-plan-as-contract** | **created** | description scrubbed: "Plans persist in ~/.claude/plans/. Ctrl+G to edit. Read every line." → "The approved plan fixes scope, sequence, and assumptions. Plans persist as files you can reopen and edit. Read every line before you sign." |
| **ch06-8-opus-plus-sonnet** | **created** | full rename: title/short_title/H1/description/alt/caption → "The Architect-and-Builder Pattern"; description "Opus for planning, Sonnet for execution" → "The flagship model plans, the lighter model executes." Filename kept (drafts mirror source filenames per audit convention). |
| **ch06-9-plans-that-compound** | **created** | description "capture it in Claude.md" → "capture it in your context file" (matches Ch 7's introduce-once convention). |
| **ch06-10-ultraplan** | **created** | full rename: title/H1/description → "Deep Planning: The Extended Plan"; description scrubbed of cloud-product framing ("Richer review surface. Section-level commenting. Approve and teleport." → practice-first phrasing with the predates-the-feature note). Filename kept per convention. |

**Judgment calls (left as-is, flagging):** ch06-4's description says "The Explore subagent" and ch06-11's says "worktrees plus subagents" — product-flavored but conceptual, no shortcuts/paths/versions; the prior agent copied them verbatim and I concur. Easy to neutralize later if Dr. Lee prefers ("the read-only research subagent" / "parallel working copies").

## FIGURES-TODO

- **ch06 Architect/Builder diagram** (`images/ch06-opus-sonnet-pattern.png`, referenced at fig-ch06-architect-builder): image bakes in Opus/Sonnet names. Relabel as Architect (flagship tier) / Builder (fast tier); consider renaming file to ch06-architect-builder-pattern.png and updating the figure directive when regenerated. Draft currently points at the existing filename so the build doesn't break.
- **ch06 Deep Planning infographic** (`images/ch06-ultraplan.png`, fig-ch06-deep-planning): retitle art from "Ultraplan" to "Deep Planning"; same filename-rename consideration.
- **ch06-8 / ch06-10 stub infographics** (`images/ch06-8-infographic.png`, `images/ch06-10-infographic.png`): placeholders "coming soon" — when generated, use the new names (Architect-and-Builder; Deep Planning).

## Meridian naming flag (audit bug #5 — decision is Dr. Lee's)

- **Ch 5 case:** "Meridian Wealth Partners," Charlotte NC, COO **Sandra Reyes**, tech head Marcus Webb.
- **Ch 6 case:** "Meridian Capital Advisors," Atlanta GA, COO Dana Whitfield, director **Marcus Reyes**, CCO **Sandra Park**.
- The audit names three Meridians across chs 0–8 (Capital Advisors / Strategy Group / Capital Group) with two CCOs surnamed Park. Note additionally: ch5 vs ch6 reuse the first names Sandra and Marcus across firms ("Sandra Reyes" / "Marcus Reyes" is especially collision-prone). Drafts preserve all names pending Dr. Lee's dedupe decision.

## Other flags

- Downstream files still using old names (NOT in scope, not modified): `case-studies/ch06-case-study.md`, `quizzes/quiz-ch06.md`, `canvas-pages/canvas-ch06.md` all reference Opus-Plus-Sonnet and/or Ultraplan and will need the same renames in their own pass.
- ch05.md case retains the specific "22% adoption" figure (used three times; the discussion prompt leans on it) — treated as illustrative, kept.

---

## Retrofit pass (post-HANDS-ON-STRATEGY)

The "Tracks B/C collapsed" items above are superseded for both chapters: Tracks B and C were **restored in print, DIAL-style** (de-branded, decision-named steps, click-paths → companion pages), ch06 Track A gained the run-twice control experiment as Step 6 (submission now five parts), and ch05 Track B is titled "The Six Floors as Files." Companion-page drafts created at companion/ch05-companion.md and companion/ch06-companion.md. All other audit fixes noted above (renames, date scrubs, verify boxes, ChatGPT-label bug, Gem/Track bug) are preserved unchanged. Full details in drafts/retrofit-ch02-05-06-NOTES.md.
