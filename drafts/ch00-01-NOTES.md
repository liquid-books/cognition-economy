# Chapters 0 & 1 — Revision Notes (AUDIT-2026-08)

Completion pass: a prior agent drafted the ch00/ch01 section files and ch00.md but died before
touching the monolithic `drafts/ch01.md` (it was still byte-identical to the original). This pass
verified every existing draft against the audit, applied all Chapter 1 fixes to the monolith, and
normalized the companion-URL convention. Originals in `chapters/` untouched.

## Companion URL convention
Standardized on **`cognitioneconomy.net/ch01-companion`** (zero-padded, matching fm/ch02/ch03/ch04 agents' `chNN` usage).
The prior agent had used `cognitioneconomy.net/ch1` in four section files; all normalized to `ch01`.
Chapter 0 has no tool click-paths and therefore no companion pointer was needed.

## Note on Tracks B/C
Chapters 0 and 1 contain **no three-track exercise blocks** (those start in Chapter 2), so there was
nothing to collapse to companion pointers here. The book-wide move is moot for these two chapters;
the exercise click-paths that did exist (arena.ai, tokenizer, voice-tool setup) were converted to
companion pointers per the CHAPTER 1 audit section instead.

---

## CHAPTER 0 — changes (all files: `ch00.md`, `ch00-1`, `ch00-2`, `ch00-3`)

All by prior agent; verified complete against the audit this pass.

- **Maya vignette:** "It's 2019…" → "A few years ago…"; "replay the same scene in 2025" → "with
  today's tools"; "the 2019 version of her" → "the earlier version of her."
- **Electricity paragraph:** "the 2025 version of 'we have electricity'" → "this era's version";
  "Right now, in 2025… Within three years" → "As this book goes to press… Within a few years of
  your reading it"; "standing in a different place by 2028" → "by then."
- **Marcus/Yuki:** "2025" dropped; "in March / By April / By May / By December" → "Within a month /
  Within two months / By the end of the year."
- **"$20 per month" ×2** → "less than the price of a business lunch each month" (both occurrences,
  §muscle-economy payoff and window-closing paragraph).
- **Roadmap:** "MCP tools (Module 3)" → "Connected tools (Module 3 — today, the connection standard
  is called MCP)"; "Skills (Module 4)" → "Reusable procedures (Module 4 — today: Skills)"; "Plan
  mode" → "Planning before acting"; "Plugins" → "Pre-built extensions"; "the SDK" → "the agent
  toolkit vendors ship for builders." Also fixed "makes AI compounds value" → "compound value" (typo).
- **Meridian/CogniCare case:** "In the spring of 2024" → "Early in the industry's adoption of AI
  platforms"; "Implementation began in June" → "within the quarter"; "By December 2024, both
  hospitals had been live for six months" → "Six months after go-live." Dollar figures ($1.2M
  contract, $2.3M rework savings) left as-is — they are case-internal invented figures, not market
  prices; audit's rounding rule was applied where market-priced (the $20 subscriptions).
- **Figure ch00-7:** alt text de-dated ("from the Transformer paper to autonomous agents"); caption
  now reads "*(a fixed window: 2017 to press time)*" per the audit's explicit-fixed-window option.
  Art change itself → FIGURES-TODO below.
- **Left alone (verified intact):** Arkwright, four leverage points, Thomas vs. George,
  adopt-vs-reorganize, era/bottleneck table, five-step redesigning work, three commitments, both
  exercises, Meridian/CogniCare case logic, discussion guidelines.

## CHAPTER 1 — changes

### `drafts/ch01.md` (monolith — done this pass; prior agent never edited it)
- **§1.1:** "For twenty dollars a month" → "For the price of a lunch each month" (opening + key
  takeaway #5); named-version tier sentence (Opus 4.7 / GPT-5.5 / Gemini 3.1 Pro / Haiku / Flash)
  → tier language ("flagship frontier tier… fast, light tier").
- **§1.2:** two `code.claude.com` doc URLs → vendor-neutral phrasing + `cognitioneconomy.net/ch01-companion` pointers
  (body sentence and Try This).
- **§1.3 replaced end-to-end** with the framework version from `drafts/ch01-3-meeting-the-models.md`
  (adapted to monolith spacing): smartphone-tier grid relabelled Flagship/Balanced/Fast; new "The
  Three Roles, By Family" section (role-first prose; Grok now "xAI's model," Elon Musk cut); all
  vendor lineup boxes + prices demoted into ONE boxed **"Model Roster — Fall 2026 edition"**
  sidebar with cognitioneconomy.net/ch01-companion pointer (the single place names/versions/prices survive; the one
  allowed literal "$20/month at press time" lives here); **o3/o4-mini deleted** (GPT-5.5 Pro noted
  as parenthetical parallel-reasoning variant); "Gemini Advanced (\$20/month) in Google One" cut
  (retired plan name) → "paid consumer plan comparably priced"; `drleee.io` typo → cognitioneconomy.net/ch01-companion;
  arena.ai demoted from "best current platform" to "at press time, we use…" + companion fallback;
  added the audit's required evergreen sentence (gated frontier tiers above the flagship; flagships
  routing among sub-models).
- **§1.4:** "at current pricing, even 10,000 tokens costs less than a dollar" → relative phrasing;
  tokenizer Try This URL → companion pointer.
- **§1.5:** **Restored the empty "Pricing Asymmetry" admonition (bug #1, ~line 674)** — the
  original had a heading + framing sentence with NO bullet content. Now filled with the ratio-based
  version: output 3–5× input; higher tiers ~an order of magnitude over lighter tiers; "check the
  vendor's pricing page; the ratio is what to remember." Task-cost list → order-of-magnitude
  language ("about a cent… a dollar or two… prices fall roughly an order of magnitude every couple
  of years; the direction matters more than the digits") with relative bullets; "$20/month for a
  pro subscription" → "a consumer subscription"; takeaway "2–5×" → "3–5×"; anthropic.com/pricing
  Try This → vendor-neutral.
- **§1.7:** per-model context table (Claude 1M / Gemini 2M / GPT-5.5 128K / 200K) → two-row tier
  table (Standard: a few hundred thousand tokens — a long novel; Extended: a million+ — a trilogy)
  + new **"How to Verify" box**; lost-in-the-middle claim now cites **Liu et al. 2023**; "Claude's
  extended context" → "an extended-context model"; takeaway updated; Try This de-branded.
- **§1.8:** worked example "difficult 2024" → "difficult past year."
- **§1.10:** section retitled **"Voice Tools (Two Examples at Press Time)"** with companion-pointer
  lead-in; setup Step 1, takeaway #3, and Try This de-hardcoded (tools kept as named press-time
  examples, links → cognitioneconomy.net/ch01-companion); the two soft "research shows" claims reworded as verifiable/
  analogy-grounded statements (dictation studies → "a pattern documented… one you can verify on
  your own transcripts"; "strong cognitive science evidence" → rubber-duck-debugging analogy).
- **Case study:** "In early 2025" deleted; "rolled out access to Claude Sonnet 4.6 … in February
  2025" → "rolled out access to a balanced-tier frontier model." Case logic untouched.
- **Exercise:** **Step 1 rewritten** — arena.ai Battle-Mode click path collapsed to "we use
  arena.ai; current instructions and the click-path are at cognitioneconomy.net/ch01-companion"; prompt and comparison
  goal preserved. **Steps 2–4 preserved verbatim** per audit. **Step 5 rewritten** — tokenizer URL
  → companion pointer; "$20/$17 plan prices," "\$3 per million," "1,600 conversations for \$1"
  → "look up the current per-million input price… a thousand-plus fully briefed conversations cost
  about a dollar." **Step 6 rewritten** — tool-specific dual paths merged into one tool-agnostic
  5-step shape; `⌘+Shift+Space` default shortcut dropped; filler-word cleanup kept as a
  feature-to-look-for; test prompt preserved. Deliverable unchanged.
- **Figure ch01-12 caption:** "GPT-5.5, Claude Opus 4.7, and Gemini 3.1 Pro compared" → "The
  flagship, balanced, and fast tiers compared." Art → FIGURES-TODO.

### Section files `ch01-1` … `ch01-10` (prior agent; verified + touched up this pass)
- All fixes mirror the monolith (the prior agent's section edits were correct and complete,
  including the section-file copy of the Pricing Asymmetry admonition — which in the section files
  had the stale $-figures rather than being empty; the truly empty one was only in the monolith).
- This pass: normalized `cognitioneconomy.net/ch1` → `cognitioneconomy.net/ch01-companion` in ch01-2/-3/-4/-10; applied the two
  "research shows" rewordings to ch01-10 (the prior agent had left them).
- `ch01-6` and `ch01-9` are intentionally unchanged from originals (audit: leave alone; verified
  clean of perishables).
- **ch01-10-voice.md** (where the prior agent reportedly died): checked line-by-line against the
  audit — retitle ✓, setup steps ✓, exercise Step 1/5/6 rewrites ✓, Steps 2–4 preserved ✓,
  deliverable ✓, closing admonition ✓. File was complete, not truncated. Only the two research-claim
  rewordings and URL normalization were missing; both applied.
- **"A Note on Version Numbers"** expanded (not cut) per audit: now frames the roster sidebar and
  points to the companion page.

## Flags / ambiguities
1. **Meridian dedupe (bug #5):** Chapter 0's case firm is **Meridian Health System** (Fort
   Lauderdale); Chapter 1's is **Meridian Advisory Group** (Atlanta, 340 employees, ~$62M). Two
   different fictional Meridians within the first two chapters, plus the Capital/Strategy variants
   in ch06–ch08 flagged by other agents. Final dedupe decision is Dr. Lee's.
2. **`exercises/ch01-exercise.md` duplicates the chapter exercise verbatim** (with the old arena.ai
   Battle-Mode click path, $20/$17 prices, ⌘-shortcut). Same likely true of other chapters'
   `exercises/` and `case-studies/` standalone files. Out of scope for this draft set (convention:
   drafts mirror `chapters/`), but they must be regenerated from the revised chapters or they will
   reintroduce every perishable the drafts removed.
3. **Roster sidebar edition stamp:** used "Fall 2026" to match the fm agent's copyright-page
   edition stamp. Update both together if edition changes.
4. **Landscape-table note:** the audit's reference table says Claude 5 / GPT-5.6 shipped; per Move
   2 the roster sidebar retains the *drafted* press-time names (Opus 4.7 / Sonnet 4.6 / GPT-5.5 /
   Gemini 3.1 Pro). If the roster should be bumped to the actual Fall-2026 lineup before print,
   that's a one-box edit in `ch01-3-meeting-the-models.md` + `ch01.md` (§1.3 sidebar) — flagged for
   Dr. Lee since the audit says body text must not quote versions but is silent on refreshing the
   sidebar's digits.
5. **ch00 case dollar figures** ($1.2M contract, $2.3M savings, 71%→89% clean-claim rate) kept:
   invented composite-case internals, not market prices; the front-matter composite disclaimer
   (added by fm agent) covers them.

## FIGURES-TODO
- **ch00-7-ai-revolution-timeline.png** — art shows "2017–2025." Either end the axis at "today"
  or keep the fixed window and label it explicitly (caption now says "a fixed window: 2017 to press
  time"; art should match — e.g., final tick labeled "press time"). Alt text already de-dated.
- **ch01-12-ai-model-selection-guide.png** — matrix compares named versions (GPT-5.5, Claude Opus
  4.7, Gemini 3.1 Pro). Relabel columns **Flagship / Balanced / Fast** per Move 7. Caption already
  updated to tier language.
