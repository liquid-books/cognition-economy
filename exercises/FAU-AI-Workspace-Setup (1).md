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

Everything you need is on **one official page: https://claude.com/download**. Use that page for *both* the desktop app and the Chrome extension — it's the only download link you should trust. (Installing from anywhere else risks fake, look-alike software.)

### 1A. Install the Claude Desktop App

1. Go to **https://claude.com/download**
2. Click the download button for your computer (**Mac** or **Windows**).
3. Open the downloaded file and install it like any normal app.
4. Open Claude from your **Applications** folder (Mac) or **Start menu** (Windows).
5. **Sign in.** No account yet? Create one at **https://claude.ai**, then sign in.

> ✅ **You're good when:** Claude opens in its own window and replies when you type.

### 1B. Add Claude to Chrome

This lets Claude see and act inside web pages. *(Requires a paid plan — skip if you're on the free tier.)*

1. Open **Google Chrome**, then go back to that same page: **https://claude.com/download**
2. Find the **Claude for Chrome** extension on the page and click its **install** button.
3. Your browser opens the official extension. Click **Add to Chrome**, then **Add extension** to confirm.
4. Click the **puzzle-piece icon** by Chrome's address bar, then **pin** "Claude" so the icon stays visible.
5. Click the **Claude icon** and **sign in** with the same account.

> ✅ **You're good when:** The Claude icon is pinned and its panel opens.

---

## Part 2 — Have Claude Install Python and Node.js for You

Some AI tools run on two free "engines" called **Python** and **Node.js**. You *could* download installers and click through them yourself — but you won't. Here is the first real lesson of this course: **don't do the work the AI can do for you.** You're going to *tell Claude to install them*, and Claude will.

For this you'll use **Claude Code** — the building tool built into Claude Desktop.

> **Open Claude Code:** In Claude Desktop, click the **Code** tab at the top of the window.
> - Claude Code requires a **paid plan**.
> - **Windows only:** the first time you open the Code tab you may be asked to install **Git**. If so, get it from **https://git-scm.com/download/win**, then restart Claude. Claude will tell you if it needs anything.

> ### 🗣️ How to Prompt Well — Your Cheat Sheet
> You'll be directing Claude to do technical work many times in this course. Good "delegation" prompts share five habits — **use them every time:**
> 1. **State the goal** plainly — *"I need you to install X."*
> 2. **Hand over the source** when there is one — paste the official link.
> 3. **Give your context** — your operating system, and any constraints.
> 4. **Set the rules of engagement** — *"explain each step in plain English"* and *"ask before making changes."*
> 5. **Iterate** — if something errors, paste the error back and say *"please fix this."* Working *with* the AI is the whole point.

### Tell Claude to Do It

In the **Code** tab, paste this prompt (fill in your operating system):

> *"I'm on [Mac / Windows]. I need you to install two things on my computer: the latest stable version of Python, and the latest LTS version of Node.js. Please make sure both are added to my system PATH so they work from any terminal, everywhere on my machine. Explain what you're doing in plain English as you go, ask my permission before each change, and when you're finished, verify both installed correctly and tell me the version numbers."*

**What happens:** Claude proposes the steps and asks your approval before running anything — just say yes to proceed. *(On a Mac, Claude may first install a helper called Homebrew. That's normal and expected.)* If anything errors, paste the message back and ask Claude to fix it.

> ✅ **You're good when:** Claude reports a version number for both — something like `Python 3.14.x` and `Node v24.x`.

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

## Part 7 — Delegate the Rest: Have Claude Set Up Your Tools

In Part 2 you had Claude install software for you. Now you'll use that same skill — **delegation** — for something more powerful: connecting Claude to outside services. Instead of following setup steps yourself, you **give Claude a documentation link (and sometimes an access key), and Claude reads it, configures everything, and explains as it goes.** You direct; the AI executes. This is the core competency of *AI for Business Innovation*.

You'll work in the **Code** tab of Claude Desktop again — the same tool you used in Part 2.

> 🗣️ **Remember the prompting cheat sheet from Part 2:** state the goal, hand over the official link, give your context (operating system, constraints), set the rules (*"explain as you go, ask before changes"*), and iterate by pasting errors back. Use it on every prompt below.

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
- [ ] You had **Claude install Python and Node.js** for you
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
- Claude Desktop **and** Claude for Chrome: https://claude.com/download
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
- Claude Code (command line) docs: https://code.claude.com/docs/en/setup
- Git for Windows (only if prompted): https://git-scm.com/download/win

---

## Appendix — Install Claude on the Command Line *(Optional — for Later)*

Later in the course you'll connect your **Antigravity IDE** to Claude. For that to work, your computer needs to be able to run Claude from a **terminal** — meaning you can type the command `claude` in any terminal window and Claude Code starts up. This appendix sets that up.

You can do it now, or come back when the course reaches that point. And true to the rest of this guide — **you won't install it by hand. You'll have Claude do it.**

1. Open the **Code** tab in Claude Desktop (the same tool you used in Parts 2 and 7).
2. Paste this prompt, filling in your operating system:

   > *"I'm on [Mac / Windows]. I want to install the Claude Code command-line tool so I can type `claude` in any terminal window to start it. Here are the official instructions: https://code.claude.com/docs/en/setup — please read them, use the recommended native installer, install it for me, and make sure the `claude` command works from any terminal on my machine. Explain what you're doing as you go, ask my permission before each change, and verify the version when you're done."*

**What happens:** Claude reads the official setup page and runs the native installer — a single command, with no Node.js required. It asks permission before each step, and confirms the version when finished.

> ✅ **You're good when:** You can open a brand-new terminal window, type `claude --version`, and see a version number. Typing just `claude` will start Claude Code right there in your terminal.

> 💡 **Why this matters:** Once `claude` runs from the terminal, tools like the Antigravity IDE — and many others — can hand work directly to Claude. You've made Claude available *everywhere* on your machine, not just inside its own window.
