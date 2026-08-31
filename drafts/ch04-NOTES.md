# Chapter 4 Revision Notes — drafts/ch04*

Source spec: AUDIT-2026-08.md, "CHAPTER 4" section + seven book-wide moves.
Originals untouched. Revised files:

- `drafts/ch04.md` — full revised chapter
- `drafts/ch04-5-demonstrate.md` — NEW standalone section file (see TOC note below)
- `drafts/ch04-NOTES.md` — this file

## What changed in ch04.md

1. **Naming paragraph inverted → open-standard framing.** The old "skill concept vs. Skills product" collision paragraph did not actually exist in the source (the source never addressed naming at all), so I added the naming discussion where it belongs — immediately after the prompt/skill definitions in "The Difference Between a Prompt and a Skill." It does double duty per the audit: (a) skill-as-concept vs. container names (Project, Gem, custom GPT, agent — four components identical); (b) **Agent Skills as a cross-vendor open standard** (SKILL.md, agentskills.io, adopters incl. OpenAI/Microsoft/Google/Cursor), with the key line *"Your skills are files you own, in a format every major vendor reads,"* explicitly paired with MCP as the book's two open standards (cross-ref to Ch 3's "USB for AI"). Named a handful of adopters rather than the full roster to limit rot.

2. **NEW prominent subsection "Two Ways to Build a Skill — Describe It or Demonstrate It"** inserted between "How to Build a Skill" and "Turning Any API into a Skill" (it builds directly on Step 3's meta-prompt, so this is the natural slot). Content per audit: programming by demonstration as the durable concept; Record a Skill named once (Anthropic), OpenAI convergence noted without product-label detail; two co-equal paths (describe = judgment-heavy/explainable; demonstrate = click-heavy/tacit); same reviewable artifact, same discipline (read, prune, test on three real cases); shareable + combinable with scheduled tasks; Ch 15 cross-ref (capturing tacit expertise before it retires); menu location / plan lineup / platform-first status pushed to companion page (drlee.io/ch04). Includes one `tip` admonition ("The rule of thumb").

3. **Tracks collapsed into one tool-agnostic exercise** (Move 1). The three-track admonition, Track B (/agents wizard, Antigravity 2.0, claude> prompt, Ctrl+backtick), and Track C (CMD+E, Agent Manager, Project Description, Artifact) are gone. Replaced with one paragraph naming the three surface types (chat assistant / terminal agent in an IDE / agent-orchestration workspace) + companion pointer. The best evergreen bits of B/C were folded in: the "one specific instruction per gap" calibration loop (kept the concrete example "Always open with a one-sentence executive summary…") and the three-real-examples test cadence.

4. **Exercise updated to two-by-interview, one-by-recording.** Skills 1–2 described (meta-prompt); Skill 3 (the tedious/autopilot task) demonstrated — deliberately, since the tedious task is the one that lives in muscle memory. Added a fallback for tools without recording (narrate into a voice memo → paste narration → ask for a spec), keeping the exercise tool-agnostic. Submission updated: three skills + one real output each + one line on what the student deleted/corrected in the recorded skill (enforces the review discipline) + the savings sentence. Kept the three-question opener and the Compounding Practice verbatim.

5. **Anachronism/price fixes:** "In early 2024" (case study) → "About a year into the firm's AI adoption" (Move 3). "$500 an hour" → "several hundred dollars an hour" (Move 4). "a tool you could not have used six months ago" → "a tool you could never have used on your own" (removes the time-stamp; the other two "six months" instances are durable — figure caption and "six months from now" in naming advice — left alone).

6. **Product-name sweep in instructional prose:** "Open Claude Desktop and say" ×2 → "Open a fresh session / open your assistant and say"; "have Claude write it for you" → "have your AI write it for you"; "Create a Gem in Gemini … or save it as a Claude Project" → "save it in your tool's skill container — a Project, a Gem, a custom GPT, an agent; the label varies, the four components do not." Track A's claude.ai/download URL removed with the track block.

7. **Reflection fixed** per audit: Q2 now reads "a chat-based container, a terminal agent, or a background agent manager." Q3 extended with "— and should it be described or demonstrated?" to close the loop on the new subsection.

8. **"Is this still true?" sidebar added** (Move 5) at the end of the exercise: check agentskills.io/spec currency, ask your assistant whether it can record a demonstration, and try to open one of your own skills as a file ("If you cannot get at the file, you do not own the skill").

## Preserved verbatim (audit "Leave alone")

Chef/recipe analogy; four-component anatomy section; all eight business vignettes (only the $500 figure touched); four-step build process + both meta-prompts; "That is not productivity. That is leverage."; the entire "Why Skills Compound" section; three-question exercise opener; Meridian case logic, Situation, Discussion Prompt, Discussion Guidelines; all figure directives, labels, anchors, frontmatter.

## TOC / structural notes for Dr. Lee

- **TOC addition needed:** `myst.yml` lists only `chapters/ch04.md` (line ~70). If the ch04-N section files enter the TOC, add `chapters/ch04-5-demonstrate.md` after `ch04-4-api-to-skill.md`. Numbering check done: existing sections are ch04-1 … ch04-4, so ch04-5 is the correct next slot (label `ch04-5`).
- **Section scaffolds:** `ch04-1` through `ch04-4` are placeholder stubs ("Chapter coming soon") with no perishable content — nothing to revise, so no draft copies were made. When they are written, ch04-2 (Anatomy) and ch04-4 (API-to-skill) should inherit the tool-agnostic phrasing from the revised ch04.md, and ch04-1 should carry the open-standard naming frame.
- `drafts/ch04-5-demonstrate.md` duplicates the new subsection as a standalone section file (per task instructions), styled to match the ch04-N section-file conventions (frontmatter, infographic figure block). The same content lives inline in `drafts/ch04.md`; at layout time pick ONE home for it — inline in ch04.md (my recommendation, since ch04.md is the only file in the TOC and the section leans on Step 3's meta-prompt) or the standalone file, not both.

## Flags

- **Meridian dedupe (book-wide bug #5):** This chapter's case firm is **Meridian Capital Partners, Miami** (MD Rachel Osei). Ch 6/8 reportedly use Meridian Capital Advisors / Meridian Strategy Group / Meridian Capital Group, Atlanta. FLAGGED — final dedupe decision is Dr. Lee's; I changed nothing about the firm identity. Note: this chapter also mentions "a peer firm in Atlanta" in The Situation — worth checking it doesn't collide with whichever Meridian survives in Atlanta.
- **Adopter roster risk:** The open-standard paragraph names four adopters (OpenAI, Microsoft, Google, Cursor). Perishable at the margin; the audit explicitly supplies the list, so I kept a short subset + "a long list of others." Companion page carries the full current roster.
- **drlee.io/ch04 convention:** audit says `drlee.io/chNN`; I used `drlee.io/ch04` (no zero-padding). If other chapter agents used `ch04`, harmonize.

## FIGURES-TODO

- **NEW: `ch04-5-infographic.png`** — referenced by `drafts/ch04-5-demonstrate.md` (caption marked "*Figure to be produced.*"). Concept: two paths converging on one skill file — an interview bubble ("Describe it") and a screen-recording icon with a voice waveform ("Demonstrate it") both feeding a single SKILL.md document. Only needed if the standalone section file is adopted; the inline version in ch04.md deliberately carries no new figure.
- `ch04-skill-creation-process.png` — caption/art says four steps ("Identify, describe, write, test"). Still accurate for the describe path, but the chapter now teaches two build paths. Optional relabel: "The describe path: identify, describe, write, test." Not blocking.
- No date/version-baked art in existing ch04 figures; none of the seven audit-flagged figures are in this chapter.
