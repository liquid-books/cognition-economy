# cognitioneconomy.net/ch08-companion — Companion Page: Plugins and Connectors

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 8. The printed chapter teaches the control-vs-convenience spectrum and the verify-with-live-data habit; this page carries this year's labels, marketplaces, and install click-paths. The vocabulary on this page drifts faster than almost anything else in the book — run the chapter's two-question test on whatever your screen actually says.

---

## Current Product Mapping

| Book role | Current product | Where |
|---|---|---|
| Chat assistant (printed exercise steps) | Claude Desktop / claude.ai | claude.ai/download |
| Terminal agent | Claude Code inside the Antigravity IDE's integrated terminal | antigravity.google · code.claude.com/docs/en/quickstart |
| Ecosystem assistant | Gemini | gemini.google.com |
| Orchestration workspace | Antigravity IDE — Agent Manager view | antigravity.google |

## What "Plugin" Is Called This Year (Fall 2026)

| Assistant | Current label | Where the marketplace lives |
|---|---|---|
| Claude (Desktop / claude.ai) | **Connectors** (pre-built) · custom MCP connections (self-configured end) | Settings → **Connectors** → browse/search → **Connect** |
| Claude Code (terminal) | MCP servers | **`/mcp`** at the `claude>` prompt lists, adds, and authenticates them |
| Gemini | **Apps** (formerly "Extensions" — same feature, renamed) | Gemini → Settings → **Apps** → toggle on the services you want |
| ChatGPT | Connectors / apps | Settings → Connectors |
| Antigravity Agent Manager | Tools / extensions per Project | Project settings → tools/extensions |

The book's spectrum survives every rename: **Connectors/Apps** are the convenient pre-built end; **MCP** (the open standard those connectors are built on) is the configure-it-yourself end you used in Chapter 3.

## Install Click-Paths (keyed to the printed exercise)

### Plugin One — Live Search

- **Claude:** web search is **built in** — check it is enabled under Settings → feature toggles. Nothing to install.
- **Gemini:** live Google Search grounding is built in by default.
- **Claude Code:** built-in web search/fetch tools ship with the agent; `/mcp` adds specialized search servers if you want more.
- Test with the printed question either way — and check the citations to learn what came from live sources.

### Plugin Two — Your Most-Used Business Tool

- **Claude Desktop / claude.ai:** Settings → **Connectors** → search the directory (current first-party and popular entries include **Google Drive, Gmail, Google Calendar, Slack, Notion, Asana, Linear, Atlassian/Jira, HubSpot, Stripe, PayPal, Canva, Figma, Cloudflare, Zapier**) → **Connect** → authenticate in the browser window → grant permissions.
- **Gemini:** Settings → **Apps** → enable **Google Workspace** (Gmail, Drive, Docs, Calendar), **YouTube, Maps, Flights, Hotels** → approve permissions.
- **Claude Code:** `/mcp` → follow the displayed add-command syntax for the server you want (file access, calendar, GitHub, project tools) → authenticate → confirm it shows as active.
- Then run the printed live-data test immediately.

### Plugin Three — Build Your Own (where the configuration lives)

The printed four-step process ends with your AI generating "the configuration." Current locations:

| Tool | Where the custom-connection config goes |
|---|---|
| Claude Desktop | Settings → Developer → **Edit Config** (`claude_desktop_config.json`) — paste the MCP server entry your AI generated |
| claude.ai (web, paid plans) | Settings → Connectors → **Add custom connector** → paste the remote MCP server URL |
| Claude Code | `claude mcp add …` in the terminal, or edit `.mcp.json` in the project root |
| Antigravity | Project settings → tools/extensions → add MCP server |

Ask the AI generating your configuration to target your specific tool by name — it will emit the right format.

## Terminal-Agent / Orchestration Exercise (per the printed sidebar)

The printed chapter runs the three-plugin exercise on the chat assistant; the sidebar points here for the other two surfaces.

**Terminal agent:** (1) `/mcp` to list integrations; (2) install web search first, authenticate, confirm active; (3) run a real industry-intelligence query with cited sources; (4) ask the agent to save the output as *industry-intel.md* — watch it appear in the IDE file browser; (5) install a second integration (files, calendar, or GitHub) and run a real query against it; (6) combine both in one task — e.g., *"check my calendar for client meetings this week, search the web for recent news about each client's company, and produce a one-page briefing per meeting"* — and watch the files land in your workspace.

**Orchestration workspace:** (1) enable Gemini's Google Workspace app and test against your real Gmail/Drive/Calendar; (2) compare the same questions in a no-apps chat; (3) in Antigravity Agent Manager (**CMD+E** / **CTRL+E**), add web search to a Project's tools and run an intelligence-briefing task asynchronously; (4) combine your personal-data findings with the agent's web findings.

---

## Changelog

- **Fall 2026** — Page created from the Fall 2026 print edition. Claude "Connectors" label and directory confirmed; Gemini "Apps" (ex-Extensions) rename confirmed; `/mcp` flow confirmed on current Claude Code build; custom-connector paths verified per table above.
- *(next entry goes here — date + what moved)*
