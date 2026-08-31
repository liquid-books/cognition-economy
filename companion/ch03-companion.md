# cognitioneconomy.net/ch03-companion — Companion Page: MCP Connections, Click-by-Click

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 3. The chapter teaches the three roles (workspace, open web, persistent store), the browser-as-tool, and the connection ladder. This page carries the product names, menu paths, free-tier numbers, and configuration steps those roles currently map to. Menu names move between releases; when they do, this page moves with them.

**Changelog**
- *Fall 2026:* Initial version. All click-paths verified against Claude Desktop, Firecrawl, Supabase, and Claude in Chrome at press time.
- *(future entries go here — dated, three lines max)*

---

## Current Product Mapping

| Book role | Current product (Fall 2026) | Where |
|---|---|---|
| Your workspace | Google Workspace connectors (Gmail, Drive, Calendar) — built into Claude Desktop | claude.ai/download |
| The open web | Firecrawl | firecrawl.dev |
| Persistent store | Supabase | supabase.com |
| The browser as a tool | Claude in Chrome (GA on paid plans) | Chrome Web Store → "Claude in Chrome" |
| Raw screen control | Anthropic computer use (consumer research preview) | Claude Desktop settings — see Ch 13 companion |
| Official registry | MCP project registry | registry.modelcontextprotocol.io (also: the servers list in the modelcontextprotocol GitHub org) |

---

## Role One — Google Workspace in Claude Desktop

**The current connectors-panel path** (referenced by the chapter body and Exercise Part 1):

1. Open **Claude Desktop** (the browser version does not carry connectors).
2. Left sidebar → **Customize** → **Connectors** → click the **+** icon → select **Google Workspace**.
3. A browser window opens for Google sign-in. **Read the permission screen** — note read vs. draft vs. send scopes — then approve.
4. Gmail, Google Drive, and Google Calendar now show as active connectors. No config files, no developer console.

Alternate path: just ask Claude a question that needs your Google data — it detects the need, asks permission, and opens the same OAuth window.

**Permission notes at press time:** Google's OAuth screen mentions email sending, but Claude only reads mail and creates drafts — it cannot send; anything drafted must be sent manually by you. Responses cite the specific emails/documents/events used, with links back to the originals. Re-check scopes after major updates.

## Role Two — Firecrawl

- **Free tier at press time:** **500 lifetime credits**, roughly one credit per page scrape. No credit card.
- **Setup:**
  1. Go to **firecrawl.dev** → create a free account.
  2. Dashboard → copy your **API key**; store it in a password manager.
  3. Find the current config snippet: search **"Firecrawl MCP Claude Desktop"** — Firecrawl's own setup docs are the first result.
  4. Copy the snippet, open Claude Desktop, and paste it with: *"Here is the Firecrawl MCP configuration. Install this in Claude Desktop for me and tell me what to do step by step."* Paste the API key when asked. ~5 minutes.
  5. **Verify:** ask Claude to read a specific URL and summarize it.

## Role Three — Supabase

- **Free tier at press time:** ~500 MB database storage, generous API-request allowance, edge functions, and up to ~50,000 monthly auth users — sized well beyond any personal or small-team project. No credit card required.
- **Setup:**
  1. **supabase.com** → create a free account → **New Project** → name it. Provisioning takes ~2 minutes.
  2. Find the current config snippet: search **"Supabase MCP Claude Desktop"** (Supabase's MCP docs page).
  3. Paste the snippet into Claude Desktop with: *"Here is the Supabase MCP configuration. Install this in Claude Desktop for me and walk me through each step."*
  4. When asked for your **project URL** and **public (anon) key**: Supabase dashboard → **Project Settings → API** — both are there.
  5. **Verify:** ask *"What information is stored in my Supabase project?"*

## The Rest of the Landscape — Current Names for the Chapter's Category Map

The chapter's landscape section, and the eleven connections we demonstrate in the live course, currently map to:

| # | Connection | Current server / route | Notes (Fall 2026) |
|---|---|---|---|
| 1 | GitHub | Official GitHub MCP server (github.com/github/github-mcp-server) — remote/hosted option available | Read, write, and manage repos; sign in with your GitHub account |
| 2 | Chrome DevTools | Chrome DevTools MCP (Google) | Drives a real browser — forms, clicks, logged-in pages a scraper can't reach; largely superseded for everyday use by Claude in Chrome (below) |
| 3 | Firecrawl | See Role Two above | |
| 4 | GoDaddy | GoDaddy MCP | Domain management from a conversation; needs a GoDaddy API key from developer.godaddy.com |
| 5 | Dice | Dice job-market MCP | Talent-market scanning; niche but a good demo of a vertical data connector |
| 6 | Pipedream | Pipedream MCP (mcp.pipedream.com) | One connection → thousands of app integrations; trigger-and-action engine |
| 7–9 | Google products (Gmail / Drive / Calendar) | Built-in connectors — see Role One | |
| 10 | Supabase | See Role Three | |
| 11 | Netlify | Netlify MCP | Deploy sites and web apps directly from a conversation |
| — | The browser itself | **Claude in Chrome** | See below |

**Finding anything else:** the MCP project's official registry (table above), plus community directories. The universal pattern: search **"[tool name] MCP"**, copy the config snippet, hand it to your assistant with *"Install this for me and walk me through it."*

## The Browser Is a Tool — Claude in Chrome (Fall 2026)

- **Status:** general availability on paid Claude plans, as an extension for the Chrome you already use.
- **Install:** Chrome Web Store → search "Claude in Chrome" → **Add to Chrome** → sign in with your Anthropic account → pin the extension.
- **The layered trust model in the current settings:** extension icon → settings → per-site permissions (which sites Claude may act on at all) and the autonomy level (approve-each-action ↔ supervised autonomy). Hard limits no setting unlocks: no purchases, no account creation, no payment data, no following instructions embedded in pages.
- Run the chapter's habit here: the permission screen is the contract — check what your settings actually allow before assuming this paragraph still holds.

## The Applied Exercise on the Other Two Surfaces

The printed exercise is written for the chat assistant (click-paths in Role One above). The equivalents:

### Terminal agent (Claude Code inside the Antigravity IDE)

1. Antigravity IDE → Editor surface → integrated terminal (**Ctrl + `**) → start Claude Code (`claude>` prompt).
2. Type **`/mcp`** → the list of available/connected MCP integrations appears.
3. Enable one (web search is the zero-account starting point); Claude Code displays the exact syntax and opens any browser auth needed. Confirm with `/mcp` again.
4. Run a live-data query the model couldn't answer from training; then connect a second integration you actually use; then ask Claude Code to combine both in one workflow. Files it creates appear in the IDE's left-hand file browser in real time.

### Orchestration workspace (Gemini + Antigravity Agent Manager)

1. gemini.google.com → Settings → **Extensions** (plug/grid icon) → enable the **Google Workspace** extension → test against your real inbox and Drive.
2. Antigravity IDE → **CMD+E / CTRL+E** → Agent Manager → **New Project** → add a web-search tool extension in Project settings.
3. Submit an asynchronous agent task (e.g., an industry intelligence briefing); the **Artifact** arrives in ~2–4 minutes; compare it with your Gemini personal-data outputs.

---

*Cross-reference: security posture for connections is Chapter 14 and its companion; scheduled/automated use of these connections is Chapter 13's companion.*
