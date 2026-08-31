# Chapter 2 Revision Notes — drafts/ (August 2026 audit pass)

Scope: all `chapters/ch02*.md`. Originals untouched. Main content lives in `ch02.md`; the seven `ch02-N-*.md` files are scaffolds ("Chapter coming soon") — revised only where their titles/descriptions/frontmatter carried perishable or contradicted content.

---

## ch02.md — what changed

### Retitled tools by role (audit "Do" item 1)
- "Tool One: Claude Desktop" → **"Tool One: Your Thinking Partner (today: Claude)"**
- "Tool Two: Gemini" → **"Tool Two: Your Ecosystem-Native Assistant (today: Gemini)"**
- "Tool Three: Google AI Studio" → **"Tool Three: Your Sandbox and API Key (today: Google AI Studio)"**
- Running text refers to tools by role; product names appear once per section ("at press time…"). Frontmatter description updated to match.

### Deleted absolute isolation claims (Ch 3 contradiction)
- "three separate products from three different companies" → "out of the box, these three tools are independent of each other… Two of them come from the same company, but even those are separate products with separate jobs." (The two-Google-products fact is now acknowledged rather than misstated.)
- "It does not connect to your Google account. It does not read your email. It does not know what Gemini is doing." → audit's exact before/after: "Out of the box it is a standalone thinking partner — it does not know what your other tools are doing. (In Module 3 you will deliberately connect it to outside systems; for now, keep it isolated.)"
- "Claude cannot [see Gmail/Drive]" → "Your thinking partner, out of the box, cannot — though in Module 3 you will teach it to."
- Closing line "Nothing connects them except you." → "Nothing connects them yet except you — and in Module 3, you will change that on purpose."
- Figure captions softened accordingly ("Independent by default — until you connect them on purpose").

### Re-justified the desktop app (replacing the inaccurate persistence claim)
- Deleted "The browser version does not preserve this across sessions" (inaccurate).
- New two-part justification: (1) later modules connect the assistant to outside tools/files and that connection lives in the desktop client; (2) the desktop app is the **agentic workspace** — see NEW note below.

### NEW (Aug 2026): workshop presented through the agentic workspace (Claude Cowork)
- Tool One section now teaches the agentic-workspace shape: connected folders, saved skills, sandboxed browsing, scheduled tasks, projects, deliverables behind approval gates. Product named **once** ("Anthropic's name for this workspace is Cowork; whatever it is called in your version, learn its shape"). No GA date, no plan-inclusion claim in body (per Move 4/6 — that's setup-sheet material). Ties explicitly to the chapter's "configured professional environment" language.

### Click-paths → setup-sheet pointers (drlee.io/ch02)
- claude.ai/download, Gem Manager path, "Get API key → Create API key" path, "Settings → Custom Instructions" (×3) all replaced with one-line intents + pointer to the date-stamped setup sheet. Intent language kept in print (e.g., "Creating a Gem takes three moves: open the Gem manager, write instructions, name it and save").
- AI Studio interface tour rewritten as "three things worth finding, whatever the current layout" (model selector, temperature, system instruction) — temperature concept kept, slider location dropped.
- "$20/month" → "about as much as a streaming subscription" (Move 4). "costs nothing and takes two minutes" → "free to start and takes a couple of minutes."

### Deleted "Claude is not fast and cheap. It is thoughtful and precise."
- → "This is not the tool you reach for when fast and cheap is the point. It is the tool you configure for depth." (Positioning-by-role, not vendor-capability-as-fact.)

### Antigravity quarantined
- Track B and Track C **deleted entirely** from print. The "Choose Your Track" admonition replaced per Move 1 with one paragraph describing the three surface types (chat assistant / terminal agent in an IDE / agent-orchestration workspace) + companion pointer.
- Exercise is now single-path (the former Track A, de-branded), so the old "Track A" heading structure became Parts 1–3 directly.
- One-paragraph teaser added ("A Glimpse Ahead: The Orchestration Surface" admonition): names Antigravity once, no "2.0", no "free during preview", no CMD+E/Editor/Agent Manager/Artifact mechanics; points to drlee.io/ch02.
- All Track B/C submission blocks, CLAUDE.md walkthrough, claude> prompt, Ctrl+backtick, code.claude.com URL, antigravity.google URLs removed from print (bug 13 for this chapter's doc URLs resolved by removal).

### "The antigravity concept" resolved (bug 3)
- Replaced with a concept the book owns: **the pre-briefed professional** (introduced and defined in the chapter opening, alongside "configuration is friction removal"). Case study and Discussion Prompt now use "the concept of the pre-briefed professional" — same definition the case previously gestured at, no collision with Google's product name.

### Case study date/number scrub (Move 3)
- "In early 2024" → "When the firm first put real budget behind AI".
- "34 employees" → "about thirty-five employees". "30-day pilot" kept (a pilot length is a design choice, not a calendar date).
- Product names in the case ("Claude Desktop installation", "Gemini Gems", "Google AI Studio project") → role names ("desktop thinking-partner installation", "Gems", "sandbox project").
- Everything under "Leave alone" preserved: friction story, configured-environment vs. on-demand-query framing, case dilemma structure, Discussion Guidelines verbatim, Reflection (one pronoun fix: "Claude wrote for you" → "your thinking partner wrote for you").

### "Is this still true?" sidebar added (Move 5)
- End of chapter: three checks — which tool holds the API key; which surface saves standing instructions (label drift named); does the sandbox product still exist as a separate product; pointer to date-stamped setup sheet.

### In-line apology sweep (Move 6)
- No "as of this writing"/"these evolve quickly" hedges introduced; press-time framing used only in the sanctioned "at press time, that tool is…" role-naming pattern.

---

## Scaffold files (ch02-1 … ch02-7)

All still "coming soon" placeholders; only perishable frontmatter/titles touched:

- **ch02-1**: description "Claude as primary, Gemini as Google-native second brain, Antigravity as agent IDE" → role-based ("a thinking partner, an ecosystem-native assistant, and a sandbox — three roles, chosen by job, not by brand"). Body unchanged.
- **ch02-2**: title reframed "Setting Up Your Google Side" → "Your Ecosystem-Native Assistant (today: Gemini) and Gems". Gem/pre-aimed-flashlight description kept.
- **ch02-3**: title → "Your Thinking Partner (today: Claude) — the Desktop App as Agentic Workspace"; description now carries the Cowork-shaped framing (chat window / agentic workspace / doorway to later modules) without naming the product in frontmatter.
- **ch02-4**: was "Setting Up Your Agent Side: Google Antigravity" — retitled to the surface type the book owns: **"The Orchestration Surface: Delegating to Background Agents"**; description points current tools to the companion page. When this section is written, Antigravity belongs on drlee.io/ch02, not in print.
- **ch02-5, ch02-6**: unchanged except verbatim copy to drafts/ (nothing perishable).
- **ch02-7**: description "Claude.md, Gemini.md, Agent.md" → "One standing brief per tool — different names, same concept." (Filename triad was vendor-specific and doesn't match ch02.md's actual three configurations.)

---

## FLAGS

1. **Meridian naming (audit bug 5).** This chapter's case firm is **Meridian Strategy Group, Atlanta** — the same name Ch 7 uses, while Ch 6/Ch 8 use Meridian Capital Advisors / Meridian Capital Group, also Atlanta. Per the audit, the dedupe decision is Dr. Lee's; I preserved "Meridian Strategy Group" here unchanged. Note: Ch 2's Meridian is a *consulting* firm and Ch 7's Meridian Strategy Group is also consulting — if these are meant to be the same firm across chapters 0–8, the managing-partner names (Diane Okafor here) should be checked against other chapters.
2. **Cowork feature list.** I taught the workspace shape (connected folders, skills, sandboxed browser, scheduled tasks, projects, approval gates) without dates, plan names, or "Record a Skill" (that belongs to Ch 4's demonstrate-a-skill section). If Dr. Lee wants "included in Pro" stated anywhere, it should go on the setup sheet, not in body.
3. **Scaffold sections ch02-1…ch02-7 are unwritten.** When they are drafted, they must follow the revised ch02.md conventions (roles not brands, companion pointers, no Antigravity mechanics in print). ch02-3's planned content ("Chat, Cowork, and Code — three apps in one") named Cowork in the old description; I kept the product out of frontmatter but the concept is now the section's spine.
4. **"30-day pilot"** retained deliberately (duration, not calendar date). Flag if the style pass wants it rounded ("a one-month pilot").

## FIGURES-TODO

- **ch02-infographic.png** — baked caption/art says "Three independent tools… No connection between them" and labels tools by brand (Gemini, Claude Desktop, Google AI Studio). Relabel by role (Thinking Partner / Ecosystem-Native Assistant / Sandbox) and soften the no-connection claim ("independent by default"). Caption text already updated in draft; art still needs the change.
- **ch02-three-config-files.png** — art says "No connection between them"; same softening as above.
- **ch02-claude-desktop-setup.png** — brand-specific title art; consider role-based relabel or keep as "example at press time" (alt text updated in draft).
- **ch02-1 … ch02-7 infographics** — not yet generated; generate against the revised (role-based) titles, especially ch02-4 (no Antigravity branding in the art).
