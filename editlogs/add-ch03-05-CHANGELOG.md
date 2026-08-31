# Changelog — Additions to Chapters 3 and 5 (+ cross-refs)

**Agent:** cea-ch03-05
**Date:** 2026-08-31
**Spec:** ADDITIONS-SPEC-2026-08.md — Ch3 items (MCP governance, agentic browsing, computer use) and the deep-research item (placed in Ch5 per agent's-judgment clause).
**Method:** Purely additive. No existing paragraphs, exercise steps, or case studies were edited. All product facts verified via web search (Anthropic/Linux Foundation announcements, Claude in Chrome permissions guide, Cowork computer-use help article, 2026 deep-research comparisons).

## chapters/ch03.md

All insertions between the end of "The Rest of the Landscape" section and the "Case Study: The Governance Gap at Meridian Health Partners" heading:

1. **New section: "Who Owns the Standard? MCP Grows Up"**
   - MCP donated by Anthropic to the Agentic AI Foundation (AAIF) under the Linux Foundation (Dec 2025), alongside Block's goose and OpenAI's AGENTS.md.
   - The official community MCP registry (registry.modelcontextprotocol.io).
   - Admonition: why neutral governance underwrites the chapter's connections-are-the-value argument ("laying pipe, not renting hose").
   - **Mini-activity: "Try It: Browse the Official MCP Registry"** (optional, 10 min) — 5 numbered steps: open registry, search a real tool, open one server, read its manifest/tool list, record server + three tools + one workflow sentence.

2. **New section: "When the AI Drives the Browser: Agentic Browsing"**
   - The category named with products: Claude in Chrome, ChatGPT Atlas (incl. its fold-in to ChatGPT/Chrome extension), Gemini agentic browsing (Project Mariner lineage → Agent Mode), Perplexity Comet.
   - The permission ladder: Manually approve (plan-first) / Automatically approve (safety-reviewed) / Skip all approvals; always-blocked actions (purchases, account creation, trades, deletions).
   - Admonition: when browsing beats a connector ("API when you can, browser when you must").
   - New figure: `../images/ch03-agentic-browsing.png`.
   - **Activity: "Try It: Run a Real Research Task with Claude in Chrome"** (25 min) — 9 numbered steps across 3 parts: install from Chrome Web Store (verify Anthropic publisher; pin icon; side-panel fallback), set Manually approve via the chat-input drop-down (label-may-vary note), run a real multi-step research prompt, observe the plan approval, mid-task "New permissions required" prompts, deliberate deny. Deliverable: brief + permission-point log + two sentences (would/would-never delegate). Fallback: Perplexity Comet or Gemini Agent Mode for locked-down machines.

3. **New section: "Computer Use: When the AI Drives the Whole Screen"**
   - The screenshot → decide → act loop; API version (sandboxed VM tool for builders) vs. consumer version (built into Claude Cowork and Claude Code; most-precise-tool-first ordering; per-application permission prompts; research-preview caveats).
   - Admonition: when screen-driving beats API connections (legacy desktop apps, no-API SaaS); hierarchy connector → browser agent → computer use.
   - New figure: `../images/ch03-computer-use-loop.png`.
   - **Activity: "Try It: Watch a Computer-Use Session Work"** (20 min, demonstration level) — Path A (Cowork on desktop): 6 numbered steps incl. harmless sandbox task, per-app permission gate observation, deliberate deny, live loop narration; Path B (fallback): watch an official Anthropic/docs.claude.com demo and narrate the loop. Deliverable: numbered action log + permission gates + one observed mistake/self-correction + two sentences on a no-API app at work.

4. **End-of-chapter:** `<!-- NEW IMAGES NEEDED -->` comment listing ch03-agentic-browsing.png and ch03-computer-use-loop.png with art direction.

## chapters/ch05.md

Insertion between the end of "Discipline Six: Harness Engineering" and the "Case Study: The Six-Floor Audit" heading:

1. **New section: "The Disciplines at Full Stretch: Deep Research Modes"**
   - The category named with products and where each mode lives: Claude research mode (Research toggle, paid plan, can use Ch3 connectors), Gemini Deep Research (editable plan before running; fastest), ChatGPT deep research (composer tools menu; slowest/most exhaustive).
   - Framed as the six disciplines compressed into one up-front brief (fits the chapter's thesis).
   - When extended autonomous research is right (and three cases when it is not).
   - How to brief: the Ch1 four components + boundaries, source guidance, decision context.
   - How to audit: explicit cross-reference to Chapter 1's verification discipline; "partners check the footnotes."
   - Admonition: the autonomy–verification tradeoff.
   - New figure: `../images/ch05-deep-research.png`.
   - **Activity: "Try It: Commission and Audit One Deep Research Run"** (60–75 min) — 10 numbered steps across 4 parts: find the mode in each of the three products (with fallback lines), write the brief from a printed skeleton, expected wait times per product, read the report, then a 5-claim citation audit with a printed audit-table template (claim / source / says-this? / quality / verdict). Deliverable: report + completed audit table + exactly two sentences on what it got wrong. Fallback: Perplexity free-tier research mode.

2. **End-of-chapter:** `<!-- NEW IMAGES NEEDED -->` comment for ch05-deep-research.png with art direction.

## One-line cross-refs (subfiles / adjacent chapters)

- `chapters/ch03-1-what-mcp-is.md` — one italic line under the H1 pointing to the new MCP governance section.
- `chapters/ch03-3-devtools.md` — one italic line under the H1 pointing to the agentic browsing + computer use sections.
- `chapters/ch03-11-universal-pattern.md` — one italic line under the H1 pointing to the official registry.
- `chapters/ch05-5-context-engineering.md` — one italic line under the H1 pointing to the deep research section.
- `chapters/ch02.md` — one sentence appended after the "What Gemini is for" paragraph pointing to Chapter 5's deep research section (spec's Ch2-placement option satisfied as a pointer).

## Placement decision

Deep research placed in **Chapter 5** (spec allowed Ch2 or Ch5): the brief-then-audit workflow is a direct application of the disciplines frame (prompt/context engineering up front, Ch1 verification on the back end), whereas Ch2 is tool setup.
