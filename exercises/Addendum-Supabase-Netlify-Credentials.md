# Addendum — Connecting Supabase & Netlify to Claude
### Companion to *Setting Up Your AI Workspace* — AI for Business Innovation, FAU Executive Education

This addendum shows you how to get everything you need to wire **Supabase** and **Netlify** into your Claude Desktop environment.

There are **two ways** to give Claude the powers of an outside service. This document covers both, for each service:

- **Route A — Connect its MCP server.** An MCP server is a ready-made connector that plugs the service's abilities straight into Claude. *Fastest, official, recommended — start here.*
- **Route B — Use an access token to build a Skill.** You get a secret access code from the service, hand it to Claude, and have Claude build a reusable **Skill** around the service's API. *Use this when you want a custom, repeatable workflow, or finer control than the MCP server gives.*

Either way, the result is the same: Supabase and Netlify fully connected inside Claude Desktop.

> **Two quick definitions, in plain English:**
> - A **personal access token** (or **API key**) is a long secret code that works like a temporary password — it lets Claude act in a service on your behalf. **Treat it like a password.**
> - A **Skill** is a reusable capability you teach Claude once, so you never have to set it up again.

> 💡 You'll use the **Code** tab in Claude Desktop for the delegation prompts below — the same tool from Parts 2 and 7 of the main guide. Remember the prompting cheat sheet: state the goal, hand over the link, give your context, set the rules, and iterate.

---

## Section 1 — Supabase

### 1A. Get Your Supabase Credentials

Supabase has **two different kinds** of credentials. Here's what each is for:

**(i) Personal Access Token** — lets Claude *manage your Supabase account* (create projects, tables, run queries). This is the one used for building Skills.
1. Sign in at **https://supabase.com/dashboard**
2. Click your **avatar** (top-right) → **Account** → **Access Tokens** *(direct link: https://supabase.com/dashboard/account/tokens)*
3. Click **Generate new token**, give it a name like `Claude`, and click generate.
4. **Copy it immediately** — Supabase shows it only once. It begins with `sbp_`.

**(ii) Project API Keys** — let an *app you build* talk to one specific project's database. You'll need these later if you build software on Supabase.
1. Open your project → **Project Settings** → **API Keys**.
2. You'll see a **publishable key** (`sb_publishable_…`, safe to use in a website) and a **secret key** (`sb_secret_…`, server-side only — treat like a password).
3. *(Older projects show legacy `anon` and `service_role` keys instead. Those still work, but the new keys are recommended.)*

### 1B. Route A — Connect the Supabase MCP Server *(Recommended)*

Supabase's official MCP server is **remote** — it lives at `https://mcp.supabase.com/mcp` and signs you in through your browser, so **no token is needed for this route.**

In the **Code** tab of Claude Desktop, paste this (fill in your operating system):

> *"I'm on [Mac / Windows]. Please connect Claude to my Supabase account using the official Supabase MCP server. Here are the instructions: https://supabase.com/docs/guides/getting-started/mcp — set it up for Claude Desktop, walk me through the browser sign-in step, explain what you're doing as you go, and ask my permission before each change."*

> 💡 **To limit Claude to one project** (a good safety habit), tell it to use this address instead: `https://mcp.supabase.com/mcp?project_ref=YOUR-PROJECT-REF`. Your **project ref** is the code in your project's dashboard web address.

### 1C. Route B — Build a Supabase Skill from the API

If you'd rather have a tailored, reusable workflow, hand Claude your Personal Access Token from step 1A(i) and let it build a Skill. In the **Code** tab:

> *"I have a Supabase personal access token I'll give you. Using the Supabase Management API, please create a reusable Skill that lets me manage my Supabase projects through Claude, and save it so it's permanently available in all my future sessions. Explain what you're doing as you go, and ask before each change."*

When Claude asks, paste your token.

> ✅ **You're connected when:** You can ask Claude in a normal chat *"List my Supabase projects"* and it answers.

---

## Section 2 — Netlify

### 2A. Get Your Netlify Credential

Netlify uses **one** credential for everything: a **Personal Access Token**. *(Netlify has no separate "API key" — the personal access token is the API key.)*

1. Sign in at **https://app.netlify.com**
2. Click your **avatar** → **User settings**.
3. Go to **Applications** → **Personal access tokens**.
4. Click **New access token**. Give it a name like `Claude`, and set an **expiration date** (90 days is reasonable).
5. Click **Generate token**, then **copy it immediately** — Netlify shows it only once.

### 2B. Route A — Connect the Netlify MCP Server *(Recommended)*

Netlify's official MCP server is the package `@netlify/mcp`. It signs you in through your browser. *(It runs on Node.js — which Claude already installed for you in Part 2 of the main guide.)*

In the **Code** tab of Claude Desktop, paste this (fill in your operating system):

> *"I'm on [Mac / Windows]. Please connect Claude to my Netlify account using Netlify's official MCP server, the package @netlify/mcp. Here are the instructions: https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/ — set it up for Claude Desktop, walk me through signing in, explain what you're doing as you go, and ask my permission before each change."*

### 2C. Route B — Build a Netlify Skill from the API

To build a tailored, reusable workflow instead, hand Claude the Personal Access Token from step 2A and let it build a Skill. In the **Code** tab:

> *"I have a Netlify personal access token I'll give you. Using the Netlify API, please create a reusable Skill that lets me deploy and manage my Netlify sites through Claude, and save it so it's permanently available in all my future sessions. Explain what you're doing as you go, and ask before each change."*

When Claude asks, paste your token.

> ✅ **You're connected when:** You can ask Claude in a normal chat *"List my Netlify sites"* and it answers.

---

## 🔒 A Word on Keeping Tokens Safe

These tokens are powerful — anyone holding one can act on your account. A few simple habits:

- **Treat every token like a password.** Only paste it into your own private Claude Code session on your own computer — never into a shared chat, an email, or a document.
- **Always set an expiration date** when the service offers one. It limits the damage if a token is ever exposed.
- **If a token leaks, revoke it immediately** and create a new one:
  - Supabase: **Account → Access Tokens**, delete the old token.
  - Netlify: **User settings → Applications → Personal access tokens**, delete the old token.
- **Use the narrowest access you can.** For Supabase, scoping the MCP server to a single project (the `project_ref` tip in 1B) is good practice.

---

## Quick Reference

| | **Supabase** | **Netlify** |
|---|---|---|
| Personal access token | Account → Access Tokens — https://supabase.com/dashboard/account/tokens | User settings → Applications → Personal access tokens |
| API keys | Project Settings → API Keys *(publishable + secret)* | Not applicable — the access token is the API key |
| MCP server | Remote URL: `https://mcp.supabase.com/mcp` | npm package: `@netlify/mcp` |
| MCP setup docs | https://supabase.com/docs/guides/getting-started/mcp | https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/ |
| Sign-in for MCP | Browser login (no token needed) | Browser login (no token needed) |

**Recommended approach:** Start with **Route A (MCP server)** for both services — it's official, maintained, and needs no token. Reach for **Route B (token + Skill)** when you want a custom, reusable workflow of your own design.
