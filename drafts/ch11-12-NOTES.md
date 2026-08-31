# Chapters 11 & 12 — Revision Notes (per AUDIT-2026-08.md)

Drafts written to `drafts/ch11.md` and `drafts/ch12.md`. Originals untouched. The seven numbered subfiles (ch11-1..3, ch12-1..4) are empty scaffolds with evergreen titles ("When to Reach for the SDK," "The Compounding Loop," etc.) — no perishable content or titles to scrub, so they were copied over unchanged.

---

## CHAPTER 11 — What Changed

**Thesis paragraph (McDonald's Move).** Replaced the wrong-timeline paragraph ("Anthropic, in 2024… For two years… quietly released") with the audit's exact rewrite: "Anthropic made the McDonald's move with AI. The headline product was Claude Code… the assistant is the demo; the SDK is the business."

**Skim Checklist / worked example.** The Skim Checklist admonition stays as body (unchanged). The worked doc-page material (code.claude.com URL, "Memorize the table," page-structure specifics, quoted opening sentence) was pulled out of the four instruction paragraphs — those are now generalized ("A good SDK overview will tell you…"; comparison-table sentence uses the audit's language: "Any SDK overview worth reading compares itself to its siblings — the raw API client, the interactive CLI, the hosted option. That table is the vendor's own build-vs-buy matrix") — and the specifics were demoted into a new boxed sidebar: **"Worked Example: One SDK Overview Page, as of August 2026"**, ending with "The page will have moved on by the time you read this. Run the checklist on whatever is there."

**Helena's three facts → three categories.** "She would learn that the SDK has built-in permissions… runs on Amazon Bedrock or Google Vertex AI… supports subagents" rewritten as three category questions — compliance (permissions/audit), residency (runs in her existing cloud), architecture (decomposes into specialists) — closed with "At the time of writing all three answers were yes." Bedrock/Vertex product names removed.

**No-code roster.** Zapier/Make/Lindy/Relevance AI + "growing weekly" + Zapier technical claim ("pulling in the Anthropic agent loop") collapsed to two categories with max two names: established automation platforms with agent steps (Zapier as canonical example) and agent-native platforms (Lindy as example), plus "Names in the second group churn quickly; the companion site (drlee.io/ch11) keeps a current list." Option-three paragraph in the four-options section likewise de-rostered ("A whole category of platforms wraps…").

**Managed Agents update (NEW).** Added a paragraph at the end of "When You Actually Need the SDK" (after the portfolio nuance): hosted harness as the fifth doorway completing the build-vs-buy spectrum (client library / CLI / Agent SDK / hosted), flagged as "in beta as this book goes to press," with the convenience-vs-compliance nuance (not ZDR/HIPAA-eligible at launch) and a Ch 14 cross-reference. Also mentioned in the worked-example sidebar as one of the comparison-table siblings.

**Date-scrub.** "Anthropic, in 2024" (fixed via thesis rewrite); "over the next three years" → "the companies that will pull ahead"; "this year" → dropped ("the most important AI decision your organization will make"); case study "In late 2025" → removed (review just "initiated"); "approximately 480 employees and roughly $720 million" → "about five hundred employees and roughly $700 million" (rounding invented precision per Move 3); "Claude or ChatGPT today" → "a frontier chat assistant today"; "take Anthropic's kitchen" → "take the vendor's kitchen" (generalizes the every-lab-makes-this-move thesis).

**Illustrative-figures flag.** Added one sentence after the three proposals in the opener: "(The dollar figures in Helena's story are illustrative — it is the ratios among them, not the digits, that matter.)" The $400k/$80k/$30k figures then stand unflagged elsewhere, per audit ("if flagged once as illustrative").

**Option one.** "Claude Code (or Antigravity, or any equivalent agent IDE)" → "Claude Code or an equivalent agent-equipped tool"; heading kept concept-first ("the assistant is enough"). Kept Claude Code by name where it's the thesis's own example (the meal/SDK pairing is the chapter's spine — Leave alone).

**"Is this still true?" sidebar (Move 5).** Added at end of body (before case study): verify the comparison-table siblings, check hosted-option compliance status, check companion site for the no-code list.

**Exercise collapse (Move 1).** Three-track admonition + Track B + Track C replaced with the one-paragraph three-surface-types admonition pointing to **drlee.io/ch11**. Track A retained (it was already evergreen paste-a-prompt) as "The Exercise," with "Claude Desktop (claude.ai/download)" → "your AI assistant — the chat surface you configured in Chapter 2." Reflection rewritten for single-surface (old one asked to compare "the two tools" students never both used — same class of bug as ch09/ch10). Track B's brief-drafting and stress-test steps and Track C's agent-loop observation move to the companion page (flagged below for the companion-page author).

**Leave alone — preserved verbatim:** McDonald's system-vs-hamburger and meal-vs-kitchen; Helena's three proposals; four options + Build-vs-Buy checklist and its application; four SDK components; general-contractor/lumberyard; sessions paragraph; five-section engineering brief + Red Flags box; start-narrow-and-deep; Two-Track Strategy; Skim Checklist; case study structure/tension/discussion prompt; discussion guidelines.

## CHAPTER 12 — What Changed

**Product names stripped from body.** "They all got Claude Desktop and the same starter prompts" → "the same AI assistant, the same license tier, the same starter prompts" (audit's exact phrase). "with Claude's help" → "with your AI's help"; "Claude will produce a short note" → "The AI will produce…". Case study: "rolled out Claude Desktop and a custom GPT environment" → "provisioned the same AI assistant, the same license tier, and the same starter prompt templates."

**Dates → relative.** "In the first quarter of 2025" → "Early in the company's AI rollout"; "By the end of the third quarter" → "Two quarters in"; "asked me last year" → "once asked me"; "In ten years" → "A decade from now."

**Frontier-release phrasing.** "leapfrogged by frontier labs every six months" → "leapfrogged by the next frontier release."

**Under-deployed hedge.** "the most under-deployed concept" → "one of the most under-deployed concepts."

**Invented precision rounded.** Mara's "win rate… went up by eleven points" → "pulled visibly ahead of the team average — a double-digit gap." "$58 million ARR" → "annual recurring revenue in the tens of millions." "more than thirty percent" (case) and "thirty percent productivity gap" (discussion prompt) → "roughly a third" — kept exactly once in body ("a measurable productivity gap of roughly a third"); the discussion prompt now says "productivity gap of roughly a third" as its single reference (the audit says the prompt hinges on it — the body mention + prompt mention are the one working pair; no other percentage remains).

**Exercise (Move 1 + feature assumptions + submission mismatches).** Three tracks collapsed to one chat-surface exercise + three-surface-types admonition + **drlee.io/ch12** pointer. Track A's produce-judge-encode-recall loop kept as steps 1–5. Track B's session review folded in as step 6 using the audit's exact reframe: "Gather notes or transcripts from your last five significant AI sessions and paste them in…" — removes the silent assumption that the tool can "review the last five conversations we had this week" or enumerate "artifacts over the last seven days." Track B's Friday-calendar step kept as step 7 (evergreen).
- **Submission mismatch fixes:** Track B asked to submit "the updated CLAUDE.md" that its steps never created — gone with the track; the merged submission asks for the four artifacts the steps actually produce (original output, feedback, revised output, Operating Rules). Track C's "project rules file" vs. "Project Description" mismatch likewise dissolved with the track; companion-page author should keep artifact naming consistent when rebuilding those tracks online.

**Leave alone — preserved verbatim:** two-consultants parable; "reflection is programming the future"; two-question habit + admonition; journal → lesson file → standing brief; "if I deleted this, would outputs get worse?"; recency test; pruning-is-half-the-practice; weekly review (all); personal vs. organizational memory; curator role; Ravi anecdote; path-dependent-advantage moat section; Astoria case tension and structure; discussion guidelines; final Reflection (adapted only from "your track" to "the exercise").

---

## Flags for Dr. Lee / downstream agents

1. **Companion pages to author:** drlee.io/ch11 needs the Track B (Claude Code brief-drafting + stress-test) and Track C (Agent Manager) exercise steps, plus the current no-code platform list and the SDK doc link. drlee.io/ch12 needs the Track B (context-file/CLAUDE.md) and Track C (project-rules) exercise variants — and when rebuilt, fix the submission-artifact naming so the steps create what the submission asks for.
2. **Managed Agents compliance status** ("not ZDR/HIPAA-eligible at launch") is stated as press-time fact and routed to the Is-this-still-true sidebar — Ch 14 agent should cross-reference from their side.
3. **Ch 11 description frontmatter** still names Claude Code ("Claude Code is the meal…") — left as-is since Claude Code remains named in the thesis (the chapter's one sanctioned product anchor). Confirm this is acceptable for metadata.
4. **Meridian dedupe (Bug 5):** no Meridian appears in ch11/ch12 — nothing to flag here.
5. **Case-study composite disclaimer:** relies on the front-matter line added by the FM agent (already in drafts/fm-*, per audit Move 3).

## FIGURES-TODO

- **fig-ch11-decision-matrix** (`ch11-decision-matrix.png`): alt text and art show a four-option matrix (Claude Code / vendor wrappers / no-code / SDK). With Managed Agents added as a fifth (hosted) option in the body, consider adding "hosted agents" to the art, or leave the 2×2 and note the hosted option textually. Not regenerated.
- **fig-ch11-skim-the-docs**: fine as-is (generic doc page, no dated content).
- **ch12 figures**: no dated/versioned content; no changes needed.

---

## Retrofit pass (per HANDS-ON-STRATEGY.md — DIAL restoration, Aug 2026)

The COLLAPSE applied to both exercises in the first draft pass has been reversed. Tracks B and C are restored **in print** in both chapters, per Dr. Lee's decision (strategy doc Part 3.1 / Immediate Action item 5), using the ch09/ch10 DIAL pattern: full track structure in print; de-branded to the three surface types (chat assistant / terminal agent / agent-orchestration workspace); steps named for the evergreen decision they set; only literal click-paths, filenames, shortcuts, and URLs deferred to one-line companion pointers (drlee.io/ch11, drlee.io/ch12). Body text was NOT touched — all audit fixes from the first pass (thesis rewrite, Managed Agents paragraph, date scrubs, rounded figures, no-code de-roster, worked-example sidebar, ch11 "Is this still true?" body sidebar) stand as drafted. Originals in chapters/ untouched.

### Ch 11 exercise — what changed in this pass

- Audit said "Leave alone: all three exercise tracks"; the collapse was an unforced loss (flagged by the strategy doc). **Tracks B and C restored as close to the originals as possible**, applying only book-wide de-branding:
  - Three-track admonition restored using the ch09/ch10 standard "One Exercise, Three Surfaces" text (track letters + surface types + drlee.io/ch11).
  - "The Exercise" re-headed **Track A — Chat Assistant**; its rebuilt (audit-fixed) steps kept verbatim — not reverted to the original's Claude Desktop wording.
  - **Track B**: original's six steps kept nearly verbatim; "Claude Code" → "your terminal agent" / "the agent"; the code.claude.com/agent-sdk/overview URL → "the vendor's Agent SDK overview page… current link: companion site" (audit Bug 13), with a tie-back to the Skim Checklist section. Original submission (brief + two sentences) restored intact, de-branded.
  - **Track C**: original's six steps kept nearly verbatim; "Antigravity 2.0 IDE / Agent Manager / CMD+E / antigravity.google URL" → "orchestration workspace / manager view / exact click-path: companion site"; "markdown artifacts" → "structured deliverables." Original submission (brief + 75–100-word agree/disagree paragraph) restored intact.
  - **Reflection**: merged — keeps the single-surface-safe rewrite from the first pass, restores the original's two-tool comparison as a conditional ("If you ran more than one surface…"). No track-label bugs introduced.

- Ch 12 fell under the strategy doc's "keep collapsed" list, but Dr. Lee opted to restore; done in **DIAL style** (decision-named steps) rather than near-verbatim, since the originals carried two submission bugs (audit Bug 9):
  - Three-track admonition restored (standard text + drlee.io/ch12). "The Exercise" re-headed **Track A — Chat Assistant**; steps 1–7 from the first pass kept verbatim — including the rebuilt evidence-gathering step 6 ("Gather notes or transcripts from your last five significant AI sessions…"), which also remains the template for the restored B/C review steps (no silent enumerate-my-history feature assumptions).
  - **Track B (7 steps, DIAL)**: framed as "lessons live in a file you own" (ties to Ch 7). Steps named for decisions: open the memory layer as a file / gather the evidence (paste transcripts — audit-safe phrasing) / patterns → candidate rules / curate (accept recurring, reject situational) / **test that the lesson persists (fresh session)** / reusable reflection prompt / Friday calendar block. CLAUDE.md not named in print — "auto-loaded context file… current filename: companion site."
  - **Bug 9a fixed in the restored track:** the original's steps never created the "updated CLAUDE.md" its submission demanded. Now step 4 explicitly writes the Operating Rules into the context file and saves it, and step 5 produces the fresh-session test output — the submission asks for exactly those two artifacts (updated context file + test output + one sentence).
  - **Track C (6 steps, DIAL)**: framed on the workspace's reviewable record. Steps: open the record / review deliverables for failure patterns (with print fallback if the tool can't enumerate history) / **encode lessons at workspace scope** / re-run and verify / permanent review-template artifact / Friday calendar block ("Workspace Review" replaces the branded "Antigravity Review").
  - **Bug 9b fixed in the restored track:** original said "project rules file" in the steps but demanded "updated Project Description" in the submission. Print now uses one consistent de-branded term throughout — "the workspace's standing rules file" — with an explicit instruction to use the same file regardless of the vendor's label; submission asks for "the updated rules file." The Project-Description-vs-rules-file naming is resolved on the companion page as a current-product detail.
  - Track C's re-run-and-verify step (new vs. the original, which never re-ran the task) exists so the submission's "improved deliverable" is actually produced by a step — same class of fix as Bug 9a.
  - **Reflection**: "After completing the exercise" → "After completing your track" (single-track-safe; unchanged otherwise).
  - **Verification lab added** (strategy doc 3.2 gap list — "ch12 light"): two active checks — does the lesson persist without your memory note (which memory layer do you control), and can you open your rules artifact as a file (if not, you don't own it) — closing with the drlee.io/ch12 pointer.

### Companion pages authored (new)

- **companion/ch11-companion.md** and **companion/ch12-companion.md** created (companion/ dir is new). Structure per strategy doc 3.5: "Last verified: Fall 2026" header, changelog stub, current-surface-names table, per-track/per-step perishable details extracted from chapters/ch11.md and chapters/ch12.md (claude.ai/download, code.claude.com quickstart + agent-sdk/overview URLs, Antigravity install URL, CMD+E/CTRL+E, Agent Manager, Artifacts, Project Description, CLAUDE.md + `~/.claude/` paths, no-code roster incl. Make/Relevance AI which were de-rostered from print), plus an instructor refresh checklist. The ch12 changelog notes the two original-edition submission bugs for returning readers.
- This **partially supersedes Flag 1** in the notes above: the companion pages now exist as content files; they still need to be published to drlee.io and get QR codes in the print layout.

### Not done / for downstream

- QR codes in exercise headers (strategy doc 3.5) — layout concern, not manuscript.
- "Do This Now" inline boxes (strategy doc 3.4) — scoped to the ch01–ch09 pass, not these chapters.
- Versioned track-sheet formatting ("Ch 11 · Track B · v. Fall 2026") on the live site — the content files here are the source material.
- Submission blocks do not yet append the verification log (strategy doc 3.2 "make them submittable") — that is a book-wide convention change awaiting Dr. Lee's sign-off; not applied unilaterally here.
