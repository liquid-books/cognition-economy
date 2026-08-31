# Chapters 7 & 8 — Draft Notes (AUDIT-2026-08)

Completed by a second agent after the prior agent stopped mid-task. `drafts/ch07.md` and the eight stub drafts existed; `drafts/ch08.md` did not and was written fresh in this pass. Originals in `chapters/` untouched.

## Chapter 7 (`drafts/ch07.md`) — verified against audit, two small fixes applied

Prior agent's draft was found to fully implement the audit's Chapter 7 section:

- **Opening reframe** — "Every morning, your AI knows less about you than you think it does…" uses the audit's replacement text verbatim; "at best it is a stranger holding a few notes it took about you without asking" carries the reframe through the intro. Section retitled "Why Your AI's Memory Is Not Your Memory" (was "Why AI Has No Memory").
- **Stateless section** — statelessness kept as a model-level design fact; audit sentence "whatever memory a product offers on top is a vendor feature — bolted on, vendor-specific, subject to change. The professional's solution is a memory layer that you own" in place.
- **NEW inspectable-memory paragraph** (Aug 2026 move) — present: vendors converging on unified, categorized, user-editable memory with sensitive topics off by default; "right direction, still not a substitute for the memory file you own." Built-in memory also added as the "fourth, convenient-but-opaque layer" footnote to the three tiers (audit's Ch 5/7 alignment).
- **Vendor endorsement fix** — "tools with strong privacy commitments like Claude" → "tools whose data-retention and training policies you have actually read. Those policies change; re-read them when they do."
- **CLAUDE.md** — mentioned exactly once, in the terminal-agent tip: "(Claude Code reads a file named CLAUDE.md; other agents use their own filename)"; "the context file" everywhere else. The 12 Track-B occurrences are gone with the track collapse.
- **Case date-scrub** — "Founded in 2003 / early 2024 / Big Four / Claude through Anthropic's API" → "Early in the industry's AI transition… a frontier AI assistant through the vendor's API"; "Big Four" → "the largest global consultancies." Case logic, three partner objections, discussion prompt preserved.
- **Verify sidebar** — "Is this still true?" admonition present with the audit's question ("What do you already know about me from previous sessions, and where is that stored?") plus memory-settings inspection and DPA re-read; companion pointer drlee.io/ch07.
- **Tracks collapsed** — three-surface paragraph + companion pointer; Track A retained as the body exercise; terminal-agent context-file tip kept as an admonition. Reflection rewritten for any-surface use.
- **Leave-alone preserved** — three tiers, Memory vs. Context, four properties + five-section template, "what to leave out," privacy spectrum, compounding arc, Meridian case structure, discussion guidelines.

Fixes applied in this pass:
1. Removed a doubled `---` divider before the case study (leftover from track deletion).
2. Nothing else — draft was otherwise consistent with the audit.

## Chapter 7/8 stub drafts

- `ch07-2-memory-file.md`: description scrubbed ("Where memory lives in Claude" → "the memory file you own, in a format any tool can read"). ✔ (prior agent)
- `ch08-1-what-plugins-are.md`: description scrubbed ("Plugins vs skills vs MCP servers — the clean distinction" → control-vs-convenience spectrum). ✔ (prior agent)
- `ch08-4-building-a-plugin.md`: title/description already updated to "Building Your First Custom Connection" (prior agent); **this pass** fixed the leftover figure alt-text/caption still reading "Building Your First Plugin."
- `ch07-1`, `ch07-3`, `ch07-4`, `ch08-2`, `ch08-3`: nothing perishable; drafts identical to originals by design.

## Chapter 8 (`drafts/ch08.md`) — written in this pass

- **Taxonomy reframe** — "fundamentally different layers" framing replaced with the audit's control-vs-convenience spectrum text verbatim ("Every AI integration sits on a spectrum… Vendors keep renaming both ends. The trade does not change."). Deleted the false mechanics ("plugins are cloud-based… MCP servers talk to your local machine… fifteen minutes vs. thirty seconds"); Chapter 3 connections now described as "the configure-it-yourself end," plugins as the pre-built end. Figure caption for `ch08-plugins-vs-mcp` relabeled "The Control-vs-Convenience Spectrum."
- **Vocabulary-drift sidebar** — new "Is this still true? The vocabulary will have drifted" admonition with the two-question test (Did someone else build and maintain it? Can I see and change what it's allowed to touch?) + drlee.io/ch08 pointer.
- **False search claim** — "your AI does not have it without a search plugin" → audit text: many assistants now ship live search built in; if not, first thing to add; training-data-vs-live-search awareness as the habit. Echoed in the exercise (Plugin One retitled "Live Search").
- **Live-data verification promoted** — now the centerpiece of the install section: "the one installation instruction that never expires… test it with a question only live data can answer." Click-by-click install paths ("Settings → Integrations", "Extensions menu… Click Enable") removed → shape described, mechanics to companion page.
- **"Building Your First Plugin" → "Building Your First Custom Connection"** — rewritten per audit: a custom connection is a configuration; new Step 2 (find the tool's API documentation) and Step 3 (hand the docs to the AI, ask it to generate the configuration + install walkthrough). Closes with the skill-plus-custom-connection pairing ("the skill is the recipe; the connection is the fresh ingredients") — folds in the audit's alternative framing. No longer describes a skill while calling it a plugin.
- **Duplicate Reflection deduped** — the two-sentence prompt previously appeared verbatim in Track A and in the Reflection; now appears once, in the Reflection.
- **Tracks collapsed** — three-surface paragraph + drlee.io/ch08; Track A content kept as the body exercise (with search-claim fix and custom-connection process); Track B (/mcp, claude> prompt, Antigravity Editor surface) and Track C (Extensions menu, CMD+E, Agent Manager, Artifact) replaced by a short "terminal agent or orchestration workspace" admonition noting the save-as-files payoff + companion pointer.
- **Case date-scrub** — "In early 2025" → "Two years into the industry's AI transition"; "$4.2 billion" → "roughly $4 billion"; "Claude Desktop had already been provisioned" → "the firm's primary AI assistant — a frontier vendor's desktop application"; "basic Gemini access… Google Workspace contract" → "a second assistant… productivity-suite contract"; "the Claude plugin ecosystem" → "the assistant's plugin marketplace"; "MCP server connections" in the three paths → "self-configured connections" (matches the new spectrum vocabulary); "as the marketplace matured" kept (already relative).
- **Discussion prompt updated** — now built on the spectrum ("pre-built connections at one end, self-configured at the other, skills as the process layer that runs on either"); permission-as-governance and maturity-curve questions preserved.
- **Leave-alone preserved** — powerful-vs-connected opener, app-store analogy, skill-vs-plugin distinction, "start with friction" + five categories, restraint/one-sentence-use-case discipline, Value Map figure, permissions paragraph, "plugins break" maintenance paragraph, "The Plugin That Changes Everything," Meridian three-path decision and stakeholder tension, discussion guidelines, submission format.

## FLAGS

- **Meridian naming collision (audit bug #5) — decision is Dr. Lee's, not resolved here.** Ch 7 case: *Meridian Strategy Group* (Atlanta, ~340 consultants, COO Renata Voss, KM director Darius Okafor). Ch 8 case: *Meridian Capital Group* (Atlanta, ~340 employees, COO Diana Forsythe, CCO **Sylvia Park**). Note also Ch 0–8 use Meridian as the running case firm, and ch06's Meridian Capital Advisors has a CCO surnamed **Park** as well — two Parks, three Meridians, all Atlanta, and both chapters here say "approximately 340" people. Drafts preserve the names as-is pending the dedupe decision.
- Ch 8 intro previously name-checked "Claude Desktop… Gems… Google Workspace, Firecrawl, and Supabase" — replaced with role-based references per Move 2 and the Ch 3 roll-call note ("your workspace, the open web, and a persistent store"). Flagging in case Dr. Lee prefers keeping one named example.

## FIGURES-TODO

- `ch08-plugins-vs-mcp.png` — image itself presumably titled "Plugins vs. MCP"; caption now reads "The Control-vs-Convenience Spectrum." Image should be relabeled to the spectrum framing (pre-built ⟷ self-configured) rather than product names.
- `ch08-build-a-plugin.png` — alt/caption updated to "Building a Custom Connection"; if the art contains the words "Build a Plugin," fine to leave (generic), but a retitle to "custom connection" would match the section.
- `ch08-4-infographic.png` (stub) — will eventually need art matching the new "Building Your First Custom Connection" title.
- No Chapter 7 figure changes needed; captions are date- and vendor-free.
