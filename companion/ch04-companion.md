# cognitioneconomy.net/ch04-companion — Companion Page: Building Skills, Surface by Surface

**Last verified: Fall 2026**

> This page is the perishable layer of Chapter 4. The chapter teaches what a skill is, the four components, describe-vs-demonstrate, and the ownership test. This page carries the container names, menu locations, plan gates, and record-button locations those ideas currently map to. Container names are the fastest-drifting facts in this chapter; when they move, this page moves.

**Changelog**
- *Fall 2026:* Initial version. Verified against Claude Projects/Record a Skill, Gemini Gems, custom GPTs, Claude Code agents, and Antigravity Agent Manager at press time.
- *(future entries go here — dated, three lines max)*

---

## Current Container Mapping (what "skill" is called where)

| Vendor / surface | Container name (Fall 2026) | Where it lives | Plan gate |
|---|---|---|---|
| Claude (Anthropic) | **Project** (chat container) · **Skill** (SKILL.md file, portable) | claude.ai / Claude Desktop → Projects in the left sidebar | Projects require a paid plan (Pro ≈ \$20/mo) |
| Gemini (Google) | **Gem** | gemini.google.com → Gem Manager | Free tier includes Gems; some models inside Gems are paid-tier |
| ChatGPT (OpenAI) | **custom GPT** | chatgpt.com → Explore GPTs → Create | Building requires Plus (≈ \$20/mo) |
| Claude Code (terminal) | **agent** (and SKILL.md skills in `.claude/skills/`) | `/agents` at the `claude>` prompt | Included with Claude Code access |
| Antigravity IDE | **Project** with Project Description as the standing brief | Agent Manager (CMD+E / CTRL+E) | Check current Antigravity pricing |

## The Open Standard — SKILL.md / agentskills.io (Fall 2026 status)

- **Spec:** **agentskills.io** — the Agent Skills specification. A skill is a folder with a **SKILL.md** file (YAML frontmatter: `name`, `description`; markdown body of instructions; optional scripts/references alongside).
- **Adopter list at press time:** Anthropic (origin), OpenAI, Microsoft, Google, Cursor, and a growing list — the live adopter list is on agentskills.io itself.
- **The ownership test from the chapter, with current paths:** in Claude Code, your skills are plain folders under `~/.claude/skills/` (personal) or `.claude/skills/` (project) — open them in any editor. In chat products, use each container's export/view-instructions option and keep a copy of the instruction text in your own files. If you cannot get at the file, you do not own the skill.

## Record a Skill — Current Location

- **Claude:** the demonstration-capture feature ships as **Record a Skill**. Current location: Claude Desktop → the skills/capabilities area of **Settings** (surfaced in Cowork and the desktop app on paid plans; screen recording permission required on macOS). Start recording → perform the task, narrating as you go → stop → answer its follow-up questions → it generates a reviewable, editable skill file.
- **OpenAI:** the same programming-by-demonstration idea ships under its own labels inside ChatGPT's agent features; ask the assistant *"can you record a demonstration and turn it into a reusable task?"* — the printed book's advice to ask your tool directly is the durable path, because this feature's name and location move between releases.
- **Rollout at press time:** desktop apps on paid plans first; the fallback in the printed exercise (narrate a voice memo, paste the transcript, ask for a skill spec) works everywhere and always will.

## Applied Exercise — Click-Paths per Surface

The printed exercise says: build Skills 1 and 2 by describing, Skill 3 by demonstrating, on whichever surface you use. The current buttons:

### Chat assistant — Claude Projects

1. claude.ai or Claude Desktop → left sidebar → **Projects** → **New Project** → name it after the skill.
2. Open **Project instructions** (the "Set custom instructions" panel) → paste the skill specification your AI wrote in the meta-prompt step → save.
3. Optionally add reference files to the Project's knowledge area (your best-ever example belongs here).
4. Test: start three chats inside the Project with three real inputs.

### Chat assistant — Gemini Gems

1. gemini.google.com → left sidebar → **Gem Manager** (sometimes "Explore Gems" / under the ☰ menu) → **New Gem**.
2. Paste the specification into the **Instructions** field → name it → **Save**. The Gem sits permanently in your left sidebar.
3. Gems are the natural home for skills that touch your Google data (with the Workspace extension enabled).

### Chat assistant — custom GPTs

1. chatgpt.com → **Explore GPTs** → **+ Create** → use the Create tab conversationally or paste your spec straight into **Configure → Instructions**.
2. Name it, set it private, **Save**. Requires a Plus plan to build.

### Terminal agent — Claude Code

1. Antigravity IDE → Editor → integrated terminal (**Ctrl + `**) → `claude>` prompt.
2. Type **`/agents`** → **Create new agent** → scope **Personal** (available in every project) → **Generate with Claude** → describe the specialist in plain English (task, inputs, ideal output, hard rules, one best-ever example).
3. Read every section of the generated definition; request revisions; save. Test with three real inputs, adding one corrective instruction between runs.
4. For portable SKILL.md skills instead of agents: ask Claude Code to *"create a skill"* — it scaffolds the folder under `.claude/skills/` for you.

### Orchestration workspace — Antigravity Agent Manager

1. **CMD+E / CTRL+E** into Agent Manager → **New Project** → name it after the *category* of work.
2. Write the skill specification into the **Project Description** field (role, output standard, rules, example — 200–350 words). This is the standing brief every task in the Project inherits.
3. Run three real task submissions; refine the Description with one concrete instruction between runs; deliverables arrive as **Artifacts** (~2–4 minutes each).

## Turning an API into a Skill — Where the Docs Hide

The chapter's pattern needs a tool's API documentation. Current convention: the tool's website footer or top nav → **"Developers"** or **"API"** → the reference or "getting started" page. Copy the capability description (skip the code), paste it to your assistant with the printed prompt. Good free-tier starter APIs at press time: Firecrawl (see Ch 3 companion), OpenWeather, Alpha Vantage.

## "Is this still true?" — Fall 2026 Answers

1. **agentskills.io current?** Yes — spec live, adopter list includes all four major vendors.
2. **Can your assistant record a demonstration?** Claude: yes, Record a Skill (desktop, paid plans). Others: shipping under various labels — ask in-product.
3. **Can you open your skill as a file?** Claude Code skills: yes, plain folders. Chat containers (Projects/Gems/GPTs): instruction text is copyable but not a file on disk — keep your own copies. That is the ownership discipline the chapter asks for.

---

*Cross-reference: the meta-prompting technique used in Step 3 is Chapter 5 (and its companion); connecting skills to live tools is Chapter 3's companion.*
