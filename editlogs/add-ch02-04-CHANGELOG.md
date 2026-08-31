# Changelog — Additions to Chapters 2 and 4 (ADDITIONS-SPEC-2026-08)

**Agent scope:** chapters/ch02.md, chapters/ch04.md (+ one-line cross-refs in subfiles).
**Method:** Additive only. No existing paragraphs or exercise steps were edited, moved, or renumbered.
**Facts verified (Aug 2026)** via web search against support.claude.com (Cowork getting-started; Dispatch/"Assign tasks from anywhere"), claude.com/product/cowork, agentskills.io, and July 2026 Record a Skill launch coverage.

## chapters/ch02.md

1. **New section: "The Workshop Made Literal: Claude Cowork"** — inserted after "Three Independent Configurations," before the Case Study.
   - Presents Cowork as the book's cognitive workshop made literal: Chat/Cowork shared home in Claude Desktop + web + mobile; connected folders; skills/plugins; sandboxed cloud environment; scheduled tasks (`/schedule`, Scheduled sidebar); projects; the three approval modes (Manually approve / Automatically approve / Skip all approvals) verified against Anthropic's help center; availability on paid plans.
   - New figure directive: `ch02-cowork-overview.png`.
   - **New activity: "Try It: Put Cowork to Work on a Real Folder"** — 10 numbered steps from install/open through folder creation, Chat→Cowork switch, folder connect (+ menu, "label may vary" fallback), Manual mode, exact paste-in brief, plan review gate, Allow/Deny approval gates, manager-style review, follow-up correction. Concrete deliverable (INVENTORY.md + OPEN-THREADS.md + 3 sentences).

2. **New section: "The Workshop in Your Pocket: Cowork on Mobile and Dispatch"** — immediately after the Cowork section.
   - Cloud sessions following the account across desktop/web/mobile; Dispatch (Mar 2026): persistent phone↔desktop thread, desktop executes with local files/connectors/apps, push notifications, desktop-must-be-awake requirement, safety caution on phone→desktop agent chains.
   - New figure directive: `ch02-dispatch-flow.png`.
   - **New activity: "Try It: Send a Task from Your Phone, Pick Up the Artifact at Your Desk"** — 9 numbered steps: mobile app install, desktop prep incl. exact Mac/Windows sleep-settings paths, finding Dispatch (with fallback line), exact paste-in task, phone-side approval, phone review, desktop artifact pickup + session log inspection, same-thread desktop follow-up. Deliverable: screenshot + ACTION-PLAN.md + 2 sentences.

3. **New section: "Claude Projects: Context as Infrastructure"** — after the Dispatch section.
   - Project knowledge, project instructions, shared context/memory; Cowork task-projects; explicit comparison and decision rule vs. Gemini Gems and custom GPTs ("repeated process → Gem; shared assistant → custom GPT; ongoing body of work → Project").
   - New figure directive: `ch02-projects-concept.png`.
   - **New activity: "Try It: Build a Project on Real Knowledge — and Prove It Is Using It"** — 9 numbered steps: choose real corpus, gather 3 real docs, create Project (sidebar path + fallback), upload to Project knowledge panel, set instructions, document-specific question, synthesis question, **control question in a fresh non-Project chat**, corpus update + re-test. Deliverable: project name + doc list + both answers + 2 sentences.

4. **End-of-chapter comment block** `<!-- NEW IMAGES NEEDED: ... -->` listing the three new figures.

## chapters/ch04.md

1. **New section: "The Second Way to Build a Skill: Record Yourself Doing It"** — inserted after "How to Build a Skill," before "Turning Any API into a Skill." Co-equal treatment per spec.
   - Record a Skill (Claude Cowork, launched July 2026): record screen + narrate, Claude writes the skill; tacit knowledge / programming-by-demonstration framing; explicit cross-ref to Chapter 15's training-ground paradox; "generated skill is a first draft — prune it" craft note.
   - New figure directive: `ch04-record-a-skill.png`.
   - **New activity: "Try It: Record a Real Workflow and Turn It into a Skill"** — 9 numbered steps: task selection criteria (~5 min, no sensitive data on screen), Cowork session, **Record a skill in the + menu** with fallback lines + Mac screen-recording permission path, narrated recording, stop + generation, read the SKILL.md line by line, explicit pruning instructions (with example language), **test on three fresh inputs**, compare to describe-it method. Deliverable: pruned SKILL.md + 3 test outputs + 3 sentences incl. what was pruned.

2. **New section: "Your Skills Are Files You Own: The Agent Skills Open Standard"** — inserted after "Turning Any API into a Skill," before "Why Skills Compound."
   - SKILL.md format (folder + YAML frontmatter + Markdown); agentskills.io; open-standard release Dec 2025; cross-vendor adoption (OpenAI, Microsoft, Google Gemini CLI, Cursor, GitHub Copilot, VS Code); paired with MCP (cross-ref Chapter 3) as the book's two open standards; portability/ownership argument; storage-as-capital advice.
   - New figure directive: `ch04-agent-skills-standard.png`.
   - **New activity: "Try It: Open Your Skill as a File and Carry It Somewhere Else"** — 7 numbered steps: locate skill on disk (via Cowork query, path-varies note), open SKILL.md in a plain text editor, verify against agentskills.io spec, copy to owned `my-skills` folder, carry to a second surface (Claude Code `.claude/skills/` path, Cursor docs-lookup option, paste-in fallback), run same real input in both, analyze what transferred. Deliverable: SKILL.md + both outputs + 2 sentences.

3. **End-of-chapter comment block** `<!-- NEW IMAGES NEEDED: ... -->` listing the two new figures.

## Subfile cross-refs (one line each, appended)

- `chapters/ch02-3-claude-desktop.md` → pointer to Ch 2's Cowork / Dispatch / Projects sections.
- `chapters/ch04-1-what-is-a-skill.md` → pointer to Ch 4's Record a Skill section.
- `chapters/ch04-2-anatomy-of-a-skill.md` → pointer to Ch 4's Agent Skills open-standard section.

## Not touched

- All existing prose, case studies, discussion guidelines, Applied Exercise tracks and step numbering in ch02.md and ch04.md.
- Quizzes, case-studies, canvas-pages, exercises directories (existing assessments remain valid; new material is additive sections + Try It blocks).
- All other chapters (other agents' scope).
