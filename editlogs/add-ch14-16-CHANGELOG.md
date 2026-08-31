# Changelog — Additions to Chapters 14 and 16 (ADDITIONS-SPEC-2026-08)

**Date:** 2026-08-31
**Spec:** ADDITIONS-SPEC-2026-08.md — Ch14 items (prompt injection, compliance & audit tooling) and Ch16 items (A2A protocol, AppFunctions, agentic OS).
**Method:** Additive only. No existing paragraphs, case studies, discussion guidelines, or Applied Exercise steps were edited, moved, or renumbered.

## chapters/ch14.md

Two new sections inserted before the Case Study (after "The Trust Compound — Why Security Pays Back"):

1. **New section: "Prompt Injection — The Attack You Did Not Know to Defend Against"**
   - Defines prompt injection: adversary hides instructions inside content the agent reads (web pages, PDFs, emails); agent follows them as if from the user.
   - Three concrete named attack patterns (white-text-on-white-background, résumé-tainting, email-footer delete).
   - "Why Agentic Browsing Changes the Threat Model" subsection: permission ladder as the attacker's shopping list; Manually approve vs. Skip all approvals as the architectural difference.
   - Admonition: "The Principle of Minimal Permission" — grant at task time, revoke when done.
   - Four named defenses: permission ladder, approval gates on irreversible actions, content isolation (reading agent ≠ acting agent), skepticism-as-instruction in the system prompt.
   - New figure directive: `../images/ch14-prompt-injection.png`.
   - **New activity: "Try It: The Classroom Injection Demo (15 min)"** — Part A: student creates a .txt with injected instruction, uploads to a fresh chat, observes whether the model complies or refuses (3 steps); Part B: student pastes a direct debrief prompt asking the model how it would handle a discovered injection (2 steps); Part C: debrief (3 steps). Deliverable: model response + debrief response + two-sentence permission-removal answer.

2. **New section: "Compliance and Audit Tooling — The Instruments of Governance"**
   - Framing: governance without records is intention; governance with records is evidence.
   - **Session Logs** subsection: enterprise-tier session logs on Claude (admin console), Copilot Studio (Power Platform run history), Gemini Enterprise (Workspace audit logs); what logs give you that memory cannot; practical implication for regulated workflows.
   - **Skill and Plugin Security Scanning** subsection: four questions to answer before deploying any skill; enterprise platform controls (Claude Enterprise admin controls, Copilot Studio connector approval workflow, Google Workspace API controls); same four questions applied to self-written skills.
   - **Compliance API** subsection: Claude Enterprise Compliance API for programmatic conversation-record access; use case (automated compliance monitoring); implication that conversation trail is structured data, queryable and reportable.
   - Admonition: "The Governance Checklist" — five questions to answer in writing before any team deployment, cross-referencing Ch3 (permission ladder), Ch14 (data usage, ZDR).
   - No activity (per spec).

## chapters/ch16.md

One new section inserted before the Case Study (after "The Robustness Test"):

1. **New section: "Agents Below the App Layer — Protocols, Operating Systems, and What Comes Next"**
   - Framing: natural endpoint of the tissue architecture — agents that find, negotiate with, and delegate to other agents without human orchestration.
   - **"Agent-to-Agent Protocols: A2A"** subsection: Google's A2A protocol (April 2025); agent card format (machine-readable capability description); task lifecycle (submitted → working → completed/failed); practical implication for tissue architecture (orchestrator reads agent cards, no custom API contracts needed); cross-platform adoption (OpenAI, Microsoft, Anthropic compatibility statements).
   - **"Agents Below the App: Android AppFunctions"** subsection: AppFunctions announced Google I/O 2025, deployed late 2025; typed action registry inside Android apps; Gemini composing across app boundaries at OS level; architectural implication (function-as-unit replaces app-as-unit; platform lock-in dissolves).
   - Closing trajectory paragraph: MCP (Ch3) → Agent Skills (Ch4) → A2A → AppFunctions as successive composition layers.
   - Admonition: "What This Means for Governance" — A2A/AppFunctions make Ch14 governance questions more urgent; approval gates must operate at delegation level not just action level; permission ladder applies to agent-to-agent calls.
   - New figure directive: `../images/ch16-agent-protocols.png`.
   - No activity (per spec).

## Images generated

- `images/ch14-prompt-injection.png` — 500KB, via Nano Banana Pro (OpenRouter). Shows the injection flow: user → agent → injected webpage → hijacked action.
- `images/ch16-agent-protocols.png` — 483KB, via Nano Banana Pro (OpenRouter). Shows the 4-layer agent coordination stack: User → Applications → A2A/AppFunctions coordination layer → Specialist agents.

## Not touched

- All existing prose, figures, admonitions, case studies, discussion guidelines, and Applied Exercise tracks/step numbering in ch14.md and ch16.md.
- Quizzes, case-studies, canvas-pages, exercises directories.
- All other chapters.

## Spec completion status

All 25+ topics from ADDITIONS-SPEC-2026-08.md are now complete. No remaining items.
