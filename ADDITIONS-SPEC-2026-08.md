# Cognition Economy — Additions Specification (August 2026)

**Base:** the ORIGINAL book as restored (commit 3fa660d). The earlier "evergreen edition" was rejected and lives on branch `evergreen-edition` — do NOT re-apply it.

## What the author wants (his words, distilled)

1. **Additive.** Keep the book as written. Insert new sections and activities where relevant. Do not de-brand, do not date-scrub, do not move click-paths to companion pages. **Name products explicitly** (Claude Cowork, Claude Code, Claude in Chrome, Record a Skill, etc.).
2. **Experiential, crystal-clear activities.** Every added topic that can be *done* gets a hands-on activity with **step-by-step instructions in the chapter itself** — exact buttons, exact menus, exact prompts to paste, what the student should observe, what they record/submit. The student must *experience* the thing, not read about it. Format: either extend the chapter's existing Applied Exercise (append new parts/tracks — do not renumber or edit existing steps) or add a clearly-titled `### Try It: <topic>` block right after the new section.
3. Mixing evergreen and perishable content is EXPECTED and ACCEPTED. Write instructions for the products as they exist in Fall 2026. If a UI detail is uncertain, give the step at the level you are confident in (menu → area → action) and say "the button label may vary."
4. House format: MyST Markdown, second person, TED-talk professor voice, admonitions `:::{admonition}`, figures `:::{figure}` with `../images/` paths (add `<!-- NEW IMAGES NEEDED: ... -->` comment at chapter end for any new figure).
5. Verify product facts via web search when unsure. These products are real (verified Aug 2026): Claude Cowork (agentic workspace; web + mobile; Dispatch phone-to-desktop, launched Mar 2026), Claude Design (visual artifacts, Apr 2026), Record a Skill (programming by demonstration), Claude in Chrome (browser agent), computer use (API + consumer), Agent Skills open standard (SKILL.md, agentskills.io — adopted by OpenAI/Microsoft/Google/Cursor), MCP donated to the Agentic AI Foundation under the Linux Foundation + official registry, Claude for Excel/PowerPoint, Claude Tag for Slack, Microsoft Copilot Studio / Agent 365, Gemini Enterprise, A2A protocol, Android AppFunctions.

## Topic → chapter map (each = new section + activity where "ACT")

### Chapter 1 (LLM fundamentals)
- **Model routing** — flagships that delegate to sub-model families; how this changes the "pick a model" advice. ACT: run the same prompt in a routed flagship and a pinned specific model; compare.
- **Multimodal work** — image, PDF, video, voice-mode input as real workflows. ACT: upload a PDF and an image (a chart photo) to Claude; extract a table from each; verify one number by hand.
- **Hallucination + verification discipline** — a named section: why models fabricate, citation checking, confidence probing, the verify-before-you-forward rule. ACT: deliberately elicit a hallucination (ask for citations on an obscure topic), then verify each citation and log real vs. fabricated.
- **Prompt caching, structured output, token budgeting** — cost/reliability mechanics past token basics. ACT: request the same analysis twice, once free-form, once with an explicit output schema; compare usability.
- **Open-weight and local models** — Llama/Mistral et al.; when a business chooses them (data control, cost at scale, offline). Brief; ACT optional (observe a local-model demo page or Ollama site — do not require installation).
- **Restricted-access frontier tiers** — gated model variants and government involvement in release timing; one honest section, no activity.

### Chapter 2 (three-tool workshop)
- **Claude Cowork, explicitly and fully** — the agentic workspace as the book's literal cognitive workshop: connected folders, skills, sandboxed browser, scheduled tasks, projects, approval gates; web + mobile. ACT: set up Cowork, connect a folder, give it a real multi-step task, review at the approval gate — exact steps.
- **Mobile + cross-device** — Cowork on mobile, Dispatch (send a task from your phone, desktop executes). ACT: send a task from the phone, review the artifact at the desktop.
- **Claude Projects as a concept** — not just a UI container: project knowledge, shared context, when a Project beats a Gem/custom GPT. ACT: create a Project with 3 knowledge docs, test that answers draw on them.

### Chapter 3 (MCP/connections)
- **MCP governance** — donated to the Agentic AI Foundation (Linux Foundation); the official MCP registry; why a neutral standard matters to the book's argument. Short section, no activity (or: browse the registry, pick one server, read its manifest).
- **Claude in Chrome / agentic browsing** — the category (Claude in Chrome, ChatGPT Atlas, Gemini/Mariner auto-browse, Comet): the AI drives the browser, permission ladder. ACT: install Claude in Chrome, walk a real research task on a live site with approval prompts, observe what it asks before acting.
- **Computer use** — the API capability and the consumer version; when screen-driving beats API connections (legacy desktop apps, no-API SaaS). ACT: demonstration-level — watch/trigger a computer-use session on a sandbox task; observe the screenshot-action loop.

### Chapter 4 (skills)
- **Record a Skill / programming by demonstration** — co-equal to describe-it: record yourself doing the task, the AI writes the skill; tacit knowledge capture (cross-ref Ch 15 training-ground paradox). ACT: record a real 5-minute workflow, review the generated SKILL.md, prune it, test on three fresh inputs — exact steps.
- **Agent Skills as an open standard** — SKILL.md, agentskills.io, cross-vendor adoption (OpenAI, Microsoft, Google, Cursor); "your skills are files you own." Pair with MCP as the book's two open standards. ACT: open one of your skills as a file, read it, carry it to a second surface and run it there.

### Chapter 5 (six disciplines) or Chapter 2 — agent's judgment
- **Deep research / long-running research modes** — extended autonomous research (Claude research mode, Gemini Deep Research, ChatGPT deep research): when to use, how to brief, how to audit output. ACT: run one deep-research task on a real business question; audit its citations with the Ch 1 verification discipline.

### Chapter 7 (memory) or Chapter 3 — agent's judgment
- **Retrieval / RAG as a design pattern** — when to retrieve vs. stuff the context window vs. use a connector; project knowledge as consumer RAG. Decision framework + ACT: same question answered three ways (paste-in, project knowledge, live connector); compare accuracy and effort.

### Chapter 8 (plugins) + Chapter 11
- **Office-app integration** — Claude for Excel / PowerPoint, shared context across add-ins. Ch 8. ACT: install the Excel add-in, have it build a real model in a sheet, verify formulas.
- **Claude Tag for Slack** — Ch 8 or Ch 13, wherever channels/integrations read most naturally. ACT: tag Claude in a Slack thread, have it summarize and draft a reply.
- **Enterprise agent platforms** — Microsoft Copilot Studio / Agent 365, Gemini Enterprise: what the M365-shop reader will actually be handed at work; how the book's concepts map onto them. Ch 11 (build-vs-buy). No lab beyond a mapping exercise.
- **Managed / hosted agents as the fourth build-vs-buy option** — Ch 11: client SDK / CLI / Agent SDK / hosted (vendor-managed + independents like Manus); convenience vs. compliance.

### Chapter 12 (compounding loop)
- **Measuring results** — evals, baselines, before/after: how to know an AI workflow actually worked. A real framework (define the metric before the workflow, hold out a baseline, simple rubric evals, weekly review). ACT: take one workflow from earlier chapters, define its metric, measure a before/after on five real cases.

### Chapter 14 (security)
- **Prompt injection** — the attack that matters once AI browses and acts: hidden instructions in pages/documents/emails; why browsing agents change the threat model; defenses (permission ladders, approval gates, content isolation). ACT: safe classroom demo — hide an instruction in a document, watch the model comply or refuse, discuss.
- **Compliance and audit tooling** — name the instruments: Compliance API, session logs, skill/plugin security scanning; governance as a framework section (not just case-study mentions). No lab; a checklist.

### Chapter 16 (future)
- **Agent-to-agent protocols & agentic OS** — A2A, Android AppFunctions; agents below the app layer — runway for the tissue thesis. Short section, no activity.
- **Government involvement in release timing / restricted tiers** — one paragraph here if not already carried in Ch 1.

## Activity quality bar (the reason the last pass was rejected)
The author rejected vague pointers. Every ACT must pass this test: *a student who has never seen the tool can complete it from the printed steps alone.* That means: numbered steps; each step names the exact surface (app, menu, button, field); each step says what the student sees when it works; a fallback line when a step may differ ("if you don't see X, look under Y"); a concrete deliverable ("submit: the skill file + the three test outputs + two sentences on what you pruned").

## Coordination
- Original text: never edit existing paragraphs/steps; append or insert clearly-marked new material.
- Each agent touches only its assigned chapter files (the main chNN.md; also update the matching quizzes/case-studies/canvas-pages ONLY if you added a section that makes them incomplete — otherwise leave them).
- Write a changelog to editlogs/ (create dir) listing every insertion.
- git pull --rebase before push; retry on conflict.
