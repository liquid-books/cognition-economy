# Chapter 3 — Revision Notes (AUDIT-2026-08)

## Files in this draft set

| File | Status |
|---|---|
| `drafts/ch03.md` | **Fully revised** — all chapter content lives here |
| `drafts/ch03-12-browser.md` | **NEW** scaffold file (see "New section" below) |
| `drafts/ch03-1` … `ch03-11` | Copied unchanged — all eleven are placeholder scaffolds ("Chapter coming soon"), no prose to revise |

Note: the entire chapter's prose is in `ch03.md`; the eleven per-section subfiles are empty scaffolds. All audit fixes were applied in `ch03.md`.

## myst.yml TOC addition

If the scaffold subfiles ever get promoted into the TOC, add after `ch03-11-universal-pattern.md`:

```yaml
- file: chapters/ch03-12-browser.md
```

Currently `myst.yml` lists only `chapters/ch03.md` (line ~68), so **no TOC change is required to ship this draft** — the new "Browser Is a Tool" and "Connection Ladder" sections are inside `ch03.md`. `ch03-12-browser.md` exists so the file set mirrors the chapter structure if/when sections are split out.

## What changed in ch03.md

### "Already wrong today" fixes
1. **Gmail can't-send (false premise) — removed.** The paragraph claiming "Claude only reads your emails and creates drafts — it cannot send" is gone. Replaced with the verifiable habit: **"Treat the permission screen as a contract"** — read the scopes at authorization, re-check after updates, assume the AI can do whatever the screen says it can. Governance point now rests on the permission screen, not on a vendor capability claim. Echoed in the exercise ("Read the permission screen before you approve it").
2. **"By default your AI cannot read [the web]" (false premise) — removed.** New justification per audit: **"searching is not the same as reading a whole site, structured, at scale"** — glance vs. research framing. The "Is this still true?" sidebar adds the verification habit (ask a question only today's news can answer).
3. **Registry line fixed.** "canonical registry is at mcp.run" → "The MCP project maintains an official registry of servers; the companion site keeps the current link." Dropped the Anthropic-GitHub-repo mention too.

### Book-wide moves applied
- **Move 1 (companion pages):** Tracks B and C deleted; three-track admonition replaced with one paragraph naming the three surface types + pointer to drlee.io/ch03. Track A kept in print (paste-a-prompt, evergreen) with its click-path softened to intent + companion pointer. All UI paths ("Customize → Connectors → +", "search 'Firecrawl MCP Claude Desktop'", "Project Settings → API"), doc-search instructions, and "five minutes/two minutes" timings moved to companion-site pointers. Config snippets now come "from the companion site."
- **Move 2 (models by role):** No model versions were named in ch03 body; product names in running text reduced — "Claude" → "your assistant/your AI" except where the concrete example is the point (Claude in Chrome, named once per the audit's "name the product once; teach the shape" convention).
- **Move 3 (sequence, not calendar):** Case study "In early 2025" removed (sentence now starts "Meridian's Chief Operating Officer…"). "Claude Desktop" in the case → "an AI desktop assistant." All other case content preserved verbatim (it's under Leave alone).
- **Move 4 (numbers → tiers):** "500 lifetime credits" (×3) → "a few hundred page reads — enough for a serious competitive analysis if you spend them deliberately"; current number delegated to companion page. "No credit card required" cut. Supabase free-tier specifics → "free tiers … sized for real personal and small-team workloads; current numbers on the companion site." "Hundreds of servers … more every week" → "large and grows continuously." Dropped "if a tool doesn't have a server today, it will within months" (replaced by evergreen ladder advice: "ask whether the tool has shipped a connector since you last checked").
- **Move 5 (claims → checklists):** Permission-screen contract habit; live-search test; **"Is this still true?" sidebar** added at end of landscape/ladder material (4 checks: permission scopes, built-in search test, connectors panel location, registry link + free-tier numbers).
- **Move 6:** No in-line apologies added; existing "as of this writing"-style hedges routed to companion pointers.
- **Move 7 (figures):** See FIGURES-TODO.

### MCP definition & governance
- New definition: "an MCP server is a small program — running on your machine or hosted by the tool's vendor — that translates your AI's requests into calls to the actual tool," with a sentence on the local→hosted/one-click shift ("Both kinds speak the same protocol. That is the point of a standard.").
- **Governance update added:** MCP created by Anthropic, donated late 2025 to a neutral foundation under the Linux Foundation (OpenAI, Google, Microsoft, AWS, Block named as backers), explicitly tied to the USB analogy: "Standards that outlive their creator's control are the ones that last." (Audit says "Agentic AI Foundation"; I wrote "a neutral industry foundation under the Linux Foundation" to be safe on the exact name — easy to insert the proper noun if Dr. Lee wants it.)

### Restructure: pattern-first
- New framing section **"The Three Roles Every Toolkit Needs"** (workspace / open web / persistent store) with vendors demoted to "our example: X" subheads and an explicit "the tools are examples; the roles are the lesson" intro + companion pointer. All Leave-alone content inside each role section preserved (three Gmail/Drive/Calendar value paragraphs, "the discipline is intentionality," Supabase-why trio, competitive-intelligence use case).

### NEW section: "The Browser Is a Tool"
- Agentic browsing defined (works in *your* browser, with logged-in credentials — vs. scraper seeing only the public web). Claude in Chrome named once as press-time example (GA on paid plans).
- **Layered trust model** as a durable governance pattern: approve-each-action / auto-with-safety-checks / full autonomy; per-site permissions; hard limits no trust level unlocks (no purchases, no account creation, no payment data, no following page-embedded instructions — framed as prompt-injection defense).
- Cross-ref to Ch 14 least-privilege ("Chapter 14's least-privilege principle rendered as product").
- **Category lesson (evergreen):** standalone AI browsers lost (OpenAI shut its down; Google folded its project into Chrome); the layer won; generalized to "bet on the layer."
- Landscape section's "Web automation" bullet cross-refs the new section.

### NEW framework: "The Connection Ladder"
- Three rungs: (1) connector/API — precise, auditable, cheap; (2) browser — no connector but has a website; (3) raw screen control (**computer use**) — consumer research preview at press time, per-app consent, blocklist, vendor's own "still early" caveat, close-sensitive-windows advice. "Each rung down trades reliability for reach." Rule of thumb: connector first, browser second, screen last; recheck for connectors periodically (ties back to betting on standards).
- The universal find→connect→verify→use pattern preserved and folded in under the ladder, updated for one-click connectors.

### Exercise
- Collapsed to single tool-agnostic track (chat-assistant surface), Track B/C content → companion pointer paragraph. Submission requirement unchanged. Reflection unchanged. Permission-screen habit inserted into Part 1.

## Leave-alone verification
Preserved verbatim or near-verbatim: locked-room analyst opening; "USB for AI tools"; "Not descriptions of these things that you typed in. The actual things themselves."; three roles + Supabase why; "the discipline is intentionality"; find → connect → verify → use; full Meridian Health case (Background/Situation/Prompt/Guidelines) with only the two date/product scrubs noted above; Reflection.

## FIGURES-TODO
- `ch03-firecrawl-use-cases.png` — caption said "500 free credits"; caption text fixed in draft, but **check whether "500" is baked into the image art**; if so, relabel to "a few hundred page reads."
- `ch03-supabase-free-tier.png` — likely bakes specific free-tier limits (storage/API-call numbers). Relabel with qualitative tiers or add "as of [edition]" stamp.
- `ch03-claude-config-file.png` — JSON config screenshot now framed as "The Manual Way" (caption rewritten in draft). Fine to keep; consider an "as of [edition]" stamp. Optionally replace with a connectors-panel illustration.
- `ch03-google-mcp-setup.png` — **dropped from the draft** (its caption was pure UI-path content, "No config files… Claude Desktop has it built in"). Restore with a vendor-neutral caption if an illustration is wanted there.
- Consider a NEW figure for the Connection Ladder (three rungs, reliability-vs-reach axis) — would carry the chapter's new framework visually.
- `ch03-infographic.png` / `ch03-mcp-landscape.png` — check for Claude-Desktop-specific labels; low priority.

## Flags / ambiguities
- **Meridian dedupe (Bug 5):** This chapter's case firm is **Meridian Health Partners** (Fort Lauderdale) — distinct from the Meridian Capital/Strategy variants flagged in ch06/ch08. Flagging per audit instructions; no change made. Final dedupe decision is Dr. Lee's.
- Chapter `description:` frontmatter updated (previously named Google/Firecrawl/Supabase/Claude Desktop; now role-based). `tags:` updated similarly. Revert if frontmatter is meant to be immutable.
- Foundation name: audit specifies "Agentic AI Foundation under the Linux Foundation"; draft says "a neutral industry foundation under the Linux Foundation" — insert the proper noun if desired.
- The eleven scaffold subfiles are not in the myst.yml TOC; if they're vestigial, consider deleting rather than filling.
