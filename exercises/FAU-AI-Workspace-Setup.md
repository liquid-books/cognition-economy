# Setting Up Your AI Workspace
### AI for Business Innovation — FAU Executive Education

Welcome. This guide does two things at once. On the surface, it gets your tools installed. Underneath, it teaches you the single most valuable skill in this course: **how to direct an AI to do technical work for you.** By the end you won't just have a working setup — you'll have *delegated part of that setup to Claude itself*, which is exactly how AI reshapes professional work.

**What you'll have when you finish:**
- The Claude Desktop app, plus Claude working inside Chrome
- Python and Node.js installed (the engines some AI tools run on)
- A GitHub account with real project folders, plus Netlify and Supabase accounts
- Hands-on experience adding a **connector** yourself
- Hands-on experience **prompting Claude to configure tools for you**

**Time:** about 75 minutes. Work through it in order, one part at a time.

---

> ### 📋 Before You Begin — Two Things to Know
>
> **1. Use Google Chrome** as your browser throughout.
>
> **2. This course works best on a Claude Pro plan** (about $20/month). Claude in Chrome, connectors, and the Claude Code feature all require a paid plan. *Claude Desktop itself, Python, Node, GitHub, Netlify, and Supabase are all free.* If your program provides accounts, check with the course coordinator.

---

## Part 1 — Install Claude

### 1A. Install the Claude Desktop App

1. Go to **https://claude.com/download**
2. Click the download button for your computer (**Mac** or **Windows**).
3. Open the downloaded file and install it like any normal app.
4. Open Claude from your **Applications** folder (Mac) or **Start menu** (Windows).
5. **Sign in.** No account yet? Create one at **https://claude.ai**, then sign in.

> ✅ **You're good when:** Claude opens in its own window and replies when you type.

### 1B. Add Claude to Chrome

This lets Claude see and act inside web pages. *(Requires a paid plan — skip if you're on the free tier.)*

1. In **Google Chrome**, go to **https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn**
   - Confirm the publisher is **Anthropic**.
2. Click **Add to Chrome**, then **Add extension**.
3. Click the **puzzle-piece icon** by the address bar, then **pin** "Claude."
4. Click the **Claude icon** and **sign in**.

> ✅ **You're good when:** The Claude icon is pinned and its panel opens.

---

## Part 2 — Install Python and Node.js

Some AI tools run on two free "engines" called **Python** and **Node.js**. You don't need to understand them — just install them.

> 💡 **Let Claude coach you.** Open Claude Desktop and paste:
> *"Walk me through installing Python and Node.js step by step on [Windows / Mac], and tell me how to confirm each one worked."*

### 2A. Install Python
1. Go to **https://www.python.org/downloads/**
2. Click the yellow **"Download Python 3.14"** button.
3. Open the installer.
   - **Windows — important:** On the first screen, **check "Add python.exe to PATH"** before clicking Install.
   - **Mac:** click through the screens.

### 2B. Install Node.js
1. Go to **https://nodejs.org/**
2. Click the **"LTS"** button (the stable, recommended version).
3. Open the installer and accept all the defaults.

> ✅ **You're good when:** Both installers finished without errors.

---

## Part 3 — Create Your GitHub Account, Folders, and Files

**GitHub** is a free service for storing project files online — like a tidy, shareable cloud drive. **You'll use the website only — no coding.**

### 3A. Create the Account
1. Go to **https://github.com/signup**
2. Enter your **email**, a **password**, and a **username** *(public — keep it professional)*.
3. Complete the puzzle and **verify your email**.

### 3B. Create Your First Project ("Repository")
A **repository** ("repo") is just a project folder on GitHub.
1. Click the **`+`** (top-right) → **New repository**.
2. **Name:** `my-first-project`
3. Leave it **Public**.
4. **Check "Add a README file."**
5. Click **Create repository**.

> Repeat once more to create a second repo named `my-website` — you'll need it in Part 4.

### 3C. Add Files
1. Open a repository → click **Add file** → **Upload files**.
2. **Drag files** in from your computer.
3. Click the green **Commit changes** button. *("Commit" means "save.")*

### 3D. Create a Folder
GitHub makes a folder when you put a **slash (`/`)** in a file's name.
1. **Add file** → **Create new file**.
2. Type a name with a slash, e.g. `documents/notes.txt`. The `/` creates a **documents** folder.
3. Type a sentence in the file body, then **Commit changes**.

> ✅ **You're good when:** Your repo shows uploaded files and a **documents** folder.

---

## Part 4 — Create a Netlify Account (Using GitHub)

**Netlify** is a free service for publishing websites. Sign up *through GitHub* to link them.

1. Go to **https://app.netlify.com/signup**
2. Click **Sign up with GitHub**.
3. Click the green **Authorize** button when GitHub asks.
4. Follow the short welcome steps.

> ✅ **You're good when:** You reach the Netlify dashboard, linked to GitHub.

---

## Part 5 — Create a Supabase Account

**Supabase** is a free service that gives projects a place to store data.

1. Go to **https://supabase.com/** → **Start your project**.
2. Choose **Continue with GitHub** → **Authorize**.
3. Click **New project** and fill in:
   - **Name:** `my-first-database`
   - **Database Password:** click **Generate a password**, then **copy and save it somewhere safe**.
   - **Region:** the closest to you (for South Florida, **East US**).
4. Click **Create new project** and wait ~2 minutes.

> ✅ **You're good when:** Your project dashboard finishes loading.

---

## Part 6 — Explore Connectors, Then Add One Yourself

A **connector** is how Claude plugs into an outside tool. Here's the key idea for this course:

> **A connector *is* an MCP server.** "MCP" (Model Context Protocol) is the open standard that lets any tool plug into any AI. When you add a connector, you're adding an MCP server. Same thing, friendlier name.

### 6A. Explore What's Available
1. In **Claude Desktop**, click your **initials** (bottom-left) → **Settings**.
2. Click **Connectors** in the sidebar *(it may sit under a "Customize" heading)*.
3. Click the **`+`** button.
4. **Browse the directory.** Scroll through it. You'll see connectors for Notion, Asana, Linear, Stripe, GitHub, and many more — **each one is an MCP server** that gives Claude new abilities.

> 🎓 **Take a minute here.** This directory is the AI tool ecosystem in miniature. Notice how many business systems already plug into Claude. *(You'll spot GitHub in this list — we'll connect it a different way in Part 7, on purpose, so you learn to do it yourself.)*

### 6B. Add Your First Custom Connector — Firecrawl
Not every tool is in the directory. When it isn't, you add it as a **custom connector** — and the tool's own website tells you exactly how. Let's do that with **Firecrawl**, which lets Claude read live websites.

1. **Get your Firecrawl key.** Go to **https://www.firecrawl.dev/**, sign up (you can use GitHub), and open the **API Keys** page. Copy your key — it starts with `fc-`.
2. **Read Firecrawl's own instructions.** Go to **https://docs.firecrawl.dev/mcp-server**. Firecrawl tells you plainly: your remote MCP server address is this pattern, with your key dropped in:
   ```
   https://mcp.firecrawl.dev/YOUR-fc-KEY-HERE/v2/mcp
   ```
   So if your key were `fc-abc123`, your address would be `https://mcp.firecrawl.dev/fc-abc123/v2/mcp`.
3. **Add it to Claude.** Back in **Settings → Connectors**, click the **`+`** → **Add custom connector**.
   - **Name:** `Firecrawl`
   - **URL:** paste your finished address from step 2.
   - Click **Add**.

> 🎓 **The transferable skill:** every serious tool publishes its own MCP setup instructions. You just learned the routine — *find the docs, grab your key, paste the address.* You can now add almost any tool to Claude on your own.

> ✅ **Test it:** Start a new chat. Click the **`+`** (or "Search and tools") at the bottom-left, open **Connectors**, switch on **Firecrawl**, and ask: *"Use Firecrawl to read https://www.fau.edu and summarize it."*

---

## Part 7 — The Real Lesson: Have Claude Set Things Up *For You*

Everything so far, you did by hand. Now for the skill that matters most in *AI for Business Innovation*: **delegation.** Instead of following setup steps yourself, you'll **give Claude the information it needs and let Claude do the work.** You provide a documentation link (and sometimes an access key); Claude reads, configures, and explains. You direct — the AI executes.

You'll use **Claude Code**, the building/configuration tool inside Claude Desktop.

> **Open Claude Code:** In Claude Desktop, click the **Code** tab at the top. *(Requires a paid plan. On Windows, the first time you open it you may be asked to install **Git** — if so, get it from https://git-scm.com/download/win, then restart Claude. Claude Code will tell you if it needs anything.)*

> ### 🗣️ How to prompt well — your cheat sheet
> Good delegation prompts share five habits. Use them every time:
> 1. **State the goal** plainly ("I want to add X").
> 2. **Hand over the source** — paste the official documentation link.
> 3. **Give your context** — your operating system, your constraints ("no Docker").
> 4. **Set the rules of engagement** — "explain each step in plain English" and "ask before making changes."
> 5. **Iterate** — if something errors, paste the error back and say "please fix this." Working *with* the AI is the point.

### 7A. Ask Claude to Add Chrome DevTools
**Chrome DevTools** is a tool for inspecting how websites behave. You won't install it by hand — you'll have Claude do it. In the **Code** tab, paste this prompt (fill in your OS):

> *"I'd like to add the Chrome DevTools MCP server to Claude Desktop on my [Mac / Windows] computer. Here are the official instructions: https://github.com/ChromeDevTools/chrome-devtools-mcp — please read that page, set it up for me, explain each step in plain English as you go, and ask my permission before making any changes. When you're done, tell me how to confirm it's working."*

**What happens:** Claude reads the page, proposes the steps, and asks your approval before each action. Say yes to proceed. If anything fails, paste the error message back and ask Claude to fix it. **Restart Claude Desktop** when it tells you to.

### 7B. Ask Claude to Connect GitHub — and Save It as a Skill
**Step 1 — Create a GitHub access token** (this is like a temporary password that lets Claude work with your repos):
1. Go to **https://github.com/settings/personal-access-tokens/new**
2. **Name:** `Claude`. **Expiration:** 90 days.
3. **Repository access:** All repositories. Under **Permissions → Repository**, set **Contents**, **Issues**, and **Pull requests** to **Read and write**.
4. Click **Generate token** and **copy it immediately** (GitHub shows it once).

> 🔒 **Treat that token like a password.** Only paste it into your own private Claude Code session on your own computer — never into a shared or public chat. The 90-day expiration limits the risk if it's ever exposed.

**Step 2 — Delegate the setup.** In the **Code** tab, paste:

> *"I want to connect Claude to my GitHub account using the official GitHub MCP server: https://github.com/github/github-mcp-server. I'm on [Mac / Windows] and I do NOT want to use Docker — please use the remote setup method instead. I have a GitHub personal access token ready to give you. Walk me through it, explain as you go, and ask before making changes."*

When Claude asks, **paste your token.**

**Step 3 — Make it reusable as a Skill.** Once GitHub is connected, paste this follow-up:

> *"Now create a reusable Skill that captures how I work with GitHub, and save it so it's permanently available in all my future Claude sessions."*

Claude will package the workflow into a **Skill** — a saved capability — and store it so you never have to set this up again. This is delegation compounding: you taught Claude once, and it remembers.

### 7C. Ask Claude to Connect Supabase
Same pattern. In the **Code** tab, paste:

> *"I'd like to connect Claude to my Supabase account using the official setup instructions here: https://supabase.com/docs/guides/getting-started/mcp — I'm on [Mac / Windows]. Please set up the Supabase MCP server for Claude Desktop, walk me through the browser sign-in step, explain as you go, and ask before making changes."*

*(Supabase now uses a quick browser login — no token to copy. Claude will open the sign-in for you.)* You can finish with the same "make this a permanent Skill" follow-up from 7B.

> 🎓 **What you just practiced** is the core competency of this course. You didn't memorize three different setup procedures — you learned **one repeatable habit**: find the official docs, hand them to Claude with clear instructions, supply credentials when asked, and iterate. That habit transfers to almost any tool you'll ever adopt.

---

## 🎉 Final Checklist

- [ ] Claude Desktop installed and signed in
- [ ] Claude added to Chrome *(paid plans)*
- [ ] Python and Node.js installed
- [ ] GitHub account with **two repos**, **uploaded files**, and **one folder**
- [ ] Netlify account created via GitHub
- [ ] Supabase account created, with a project running
- [ ] You explored the **Connectors** directory
- [ ] **Firecrawl** added as a custom connector — and tested
- [ ] You used **Claude Code** to add Chrome DevTools, GitHub, and Supabase
- [ ] You created at least one permanent **Skill**

---

## Troubleshooting

| If this happens... | Do this |
|---|---|
| A connector won't switch on in a chat | Add it in **Settings → Connectors** first, then enable it per-chat with the **`+`** menu. |
| Firecrawl connector won't add | Check the address has **your own `fc-` key** and ends in **`/v2/mcp`**, with no spaces. |
| The **Code** tab asks you to upgrade | Claude Code requires a paid plan. |
| The **Code** tab (Windows) asks for Git | Install Git from https://git-scm.com/download/win and restart Claude. |
| Claude Code hits an error mid-setup | **Paste the exact error back to Claude and ask it to fix it.** Iterating is normal — and it's the skill. |
| Anything is confusing | Describe what you see to Claude and ask. Delegating your confusion is also a valid move. |

---

### Every Link in One Place
- Claude Desktop: https://claude.com/download
- Claude for Chrome: https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn
- Python: https://www.python.org/downloads/
- Node.js: https://nodejs.org/
- GitHub sign-up: https://github.com/signup
- GitHub token page: https://github.com/settings/personal-access-tokens/new
- Firecrawl: https://www.firecrawl.dev/ · MCP docs: https://docs.firecrawl.dev/mcp-server
- Chrome DevTools MCP: https://github.com/ChromeDevTools/chrome-devtools-mcp
- GitHub MCP server: https://github.com/github/github-mcp-server
- Supabase MCP docs: https://supabase.com/docs/guides/getting-started/mcp
- Netlify: https://app.netlify.com/signup
- Supabase: https://supabase.com/
