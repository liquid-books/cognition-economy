# cognitioneconomy.net/ch01-companion — Companion Page: The Model Roster, Tools, and Click-Paths

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 1. The chapter teaches the frameworks — intelligence vs. knowledge, the flashlight, tiers-not-names, tokens, context, voice. This page carries the names, versions, prices, and URLs those frameworks currently point at. When a vendor renames or re-prices something, this page changes; the book does not.

**Changelog**
- *Fall 2026:* Initial version, verified against every link and price below at press time.
- *(future entries go here — dated, three lines max)*

---

## The Live Model Roster (Fall 2026)

The printed roster sidebar in Chapter 1.3 is a snapshot of this table. This is the maintained copy.

| Family | Flagship | Balanced | Fast | Access | Consumer price |
|---|---|---|---|---|---|
| **Anthropic (Claude)** | Claude Opus 4.7 | Claude Sonnet 4.6 | Claude Haiku 4.6 | claude.ai | Free tier; **Pro \$20/mo** (\$17/mo annual) unlocks Sonnet and Opus |
| **Google (Gemini)** | Gemini 3.1 Pro | — | Gemini Flash | gemini.google.com | Free tier; paid tier ≈ \$20/mo under Google's current AI plan branding (in Google One) |
| **OpenAI (GPT)** | GPT-5.5 (plus GPT-5.5 Pro, a parallel-reasoning variant for complex scientific/legal/strategic problems) | — | (flagship routes to lighter sub-models automatically) | chatgpt.com | Free tier (limited GPT-5.5); **Plus \$20/mo** |
| **xAI (Grok)** | Grok (current release) | — | — | x.ai/grok or inside X | Bundled with X subscription tiers |

Notes that go with the table:

- **Reasoning-specialist models:** OpenAI's dedicated step-by-step reasoning line (o-series — o3 / o4-mini at press time) remains the pick for heavily mathematical or formally logical problems.
- **Gated frontier tiers** above the flagship (experimental, higher-priced, limited access) now exist at every major vendor; ignore them until you have a task the flagship fails at.
- **Google Workspace note:** if your organization pays for Workspace at the business level, some Gemini access may already be included — check before subscribing.

## Vendor Documentation (the flashlight exercise, Ch 1.2)

The chapter's "paste current docs into your prompt" exercise. Current doc homes:

- **Anthropic / Claude:** code.claude.com/docs/en/overview (Claude Code and platform docs; regularly updated, freely accessible)
- **OpenAI:** platform.openai.com/docs
- **Google / Gemini:** ai.google.dev/docs

Any of these pages works for the *Try This*: copy the page text, paste it into your AI, and ask for a plain-English summary.

## Side-by-Side Comparison — arena.ai Walkthrough (Ch 1.3 and Exercise Step 1)

Current recommendation: **arena.ai** — free, no account required. The printed exercise's Step 1 ("compare three models side by side"), with today's buttons:

1. Go to **arena.ai** in your browser.
2. Click **Battle Mode** in the top navigation — the head-to-head comparison interface.
3. Select your models from the dropdowns — use **Claude**, **GPT-5.5**, and **Gemini 3.1 Pro** (one from each family) if available.
4. Paste the printed prompt into the shared prompt box.
5. Click **Send** — the same prompt runs through all models simultaneously.
6. Compare, per the printed instructions.

If arena.ai has changed or disappeared by the time you read this, this page will name the replacement; the exercise itself does not change.

## Tokenizer Tool (Ch 1.4 Try This, and Exercise Step 5)

- **Current link:** **platform.openai.com/tokenizer** — free, loads directly, no login. Paste text; the token count updates live.
- It tokenizes with OpenAI's tokenizer, but the *pattern* (word-splitting, ~¾-word average) is representative across vendors — fine for the exercise.

## Current Pricing Pages (Ch 1.5, and Exercise Step 5)

- **Anthropic API pricing:** anthropic.com/pricing — at press time, Claude Sonnet input ≈ **\$3 per million input tokens**, output ≈ **\$15 per million output tokens** (the ~3–5× input/output asymmetry the chapter teaches).
- **Consumer plan:** claude.ai/pricing — Pro **\$20/month** billed monthly, **\$17/month** billed annually; free tier available.
- **The Step 5 mental math, worked with today's digits:** a 200-token context brief × \$3/M input tokens ≈ **\$0.0006 per conversation** — about 1,600 fully briefed conversations per dollar. Briefing your AI is effectively free.
- OpenAI: openai.com/api/pricing · Google: ai.google.dev/pricing

## Context Windows (Ch 1.7 "How to Verify")

Press-time figures behind the chapter's two-tier table:

- **Standard tier:** Claude Sonnet/Haiku ≈ 200K tokens; GPT-5.5 ≈ 128K–400K depending on surface.
- **Extended tier:** Claude extended context up to 1M tokens; Gemini 3.x up to 2M tokens. Extended context is sometimes gated behind higher plans or API access — check your plan.

## Voice / Dictation Tools (Ch 1.10, and Exercise Step 6)

Current picks — the same two the chapter used as press-time examples:

| Tool | Platforms | Where | Free tier | Notes |
|---|---|---|---|---|
| **SuperWhisper** | macOS (Windows arrived recently — check the site) | superwhisper.com | Yes — sufficient for daily use | Local/offline transcription option; default activation shortcut on Mac is typically **⌘ + Shift + Space** |
| **Wispr Flow** | Mac / Windows / iOS / Android | wisprflow.ai | Yes — capped weekly words on free tier | Auto-removes filler words and false starts — output is polished text, not raw transcript |

**Exercise Step 6, with today's buttons:**

1. Download either tool from the URL above and install; grant microphone access when prompted.
2. Find your activation shortcut in the tool's settings (SuperWhisper on Mac: hold ⌘ + Shift + Space by default).
3. Open your AI in the browser, click into the chat field.
4. Hold the shortcut, speak, release — text appears at your cursor. That is the whole loop.
5. Dictate the printed test prompt.

Both tools route text wherever your cursor is — any app, browser, or field. If either has been renamed, acquired, or displaced by the time you read this, the current picks are maintained right here.

---

*Cross-reference: workshop setup (desktop apps, Gems, API keys) is Chapter 2's companion page; the setup sheet for the front-matter prerequisites is at cognitioneconomy.net/setup-companion.*
