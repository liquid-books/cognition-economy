# Changelog — Additions to Chapters 11 and 12 (ADDITIONS-SPEC-2026-08)

**Agent scope:** chapters/ch11.md, chapters/ch12.md (+ one-line cross-refs in subfiles).
**Method:** Additive only. No existing paragraphs, case studies, discussion guidelines, or Applied Exercise steps were edited, moved, or renumbered.
**Facts verified (Aug 2026)** via web search: Claude Managed Agents (Anthropic hosted agent service, launched April 8, 2026; treated as first-class alternative in the Agent SDK docs comparison); Manus (debuted spring 2025, acquired by Meta December 2025, Trust Center at trust.manus.im, not HIPAA-compliant per third-party reviews); Microsoft Agent 365 (announced Ignite, November 18, 2025 — "control plane" for agents, agent IDs in Entra); Microsoft Copilot Studio terminology (instructions / knowledge sources / topics / tools [formerly actions] / triggers; Power Platform connectors, 1000+); Gemini Enterprise (launched October 9, 2025, replaced Agentspace; Agent Designer no-code builder; prebuilt connectors incl. Drive, SharePoint, Salesforce, ServiceNow, Confluence; Gemini Enterprise Agent Platform added April 2026).

## chapters/ch11.md

1. **New section: "The Fifth Option: Managed and Hosted Agents"** — inserted after "The No-Code Path to SDK Power," before "Reading SDK Documentation Like a Business Person."
   - Positions hosted agents as an addition to the chapter's existing four build-vs-buy options (which the original text already enumerates as four — hence "fifth" in-chapter; this is the spec's "hosted" option).
   - Two flavors named explicitly: **Claude Managed Agents** (Anthropic-run agent loop/sandbox/tooling, session logs, April 2026) and independents (**Manus**, incl. Meta acquisition Dec 2025).
   - Convenience-vs-compliance trade-off developed both directions; hosted option run through the chapter's existing four-question checklist; portfolio placement (public-data research + disposable experiments); "email-to-a-stranger" rule-of-thumb admonition; Helena/Cypress worked example (FNOL disqualified, competitor landscape scan approved).
   - New figure directive: `ch11-hosted-agents.png`.
   - **New activity: "Try It: Screen a Hosted Agent Against a Compliance Checklist"** — 6 numbered steps, documentation-only (no account/admin rights): pick offering, printed 8-question compliance checklist (execution location, retention, training opt-out, session logs, SOC 2/ISO, BAA, sub-processors, human approval), exact starting URLs (trust.manus.im, manus.im/privacy, trust.anthropic.com, code.claude.com/docs/en/agent-sdk/overview) with search fallback, honest-gap rule ("Could not determine…"), two-part verdict. Deliverable: checklist table with URLs + verdict paragraph.

2. **New section: "The Platforms Your Employer Will Actually Hand You"** — inserted immediately after the hosted-agents section, before "Reading SDK Documentation Like a Business Person."
   - Microsoft Copilot Studio vocabulary mapped to book terms (instructions→system prompt, knowledge sources→project knowledge, topics/tools→skills, triggers→scheduled tasks/hooks, Power Platform connectors→MCP connections).
   - Microsoft Agent 365 as control plane = approval gates/permission ladders promoted to corporate infrastructure (agent IDs in Entra, fleet auditing).
   - Gemini Enterprise (Oct 2025, ex-Agentspace): Agent Designer, prebuilt connectors, central governance; April 2026 Agent Platform noted.
   - Five-row Rosetta Stone mapping table (book concept → Microsoft → Google); "mapping matters more than the platform" admonition; open-standards convergence note (Agent Skills + MCP cross-refs to Ch 3/4).
   - New figure directive: `ch11-enterprise-platforms-map.png`.
   - **New activity: "Try It: Find the Book's Concepts Inside Your Employer's Platform"** — 7 numbered steps, documentation-only, no admin rights: identify employer's ecosystem (Outlook/Teams vs Gmail/Drive heuristic), four-column mapping doc, exact starting doc URLs (learn.microsoft.com Copilot Studio overview + connectors page; cloud.google.com/gemini-enterprise; docs.cloud.google.com/gemini/enterprise/docs/agent-designer; Agent 365 announcement URL) with URL-moved fallbacks, locate equivalents of three book concepts (skill, connection, approval gate), one-sentence same/different comparison per row with worked example. Deliverable: 3-row mapping table with exact product terms + URLs + three comparison sentences.

3. **End-of-chapter comment block** `<!-- NEW IMAGES NEEDED: ... -->` listing the two new figures.

## chapters/ch12.md

1. **New section: "Measuring Results: How to Know It Actually Worked"** — inserted after "The Weekly Review Practice," before "Personal Memory vs. Organizational Memory" (so it can reference the Friday cadence and be referenced by the moat/case-study material without editing either).
   - Names and dismantles **anecdote-driven ROI** (selection effect: highlight reel ≠ metric).
   - Five-part framework exactly per spec: (1) define the metric BEFORE deploying ("This workflow succeeds if ___" — time + quality bar), (2) hold a baseline (retrospective vs prospective, outside your memory), (3) simple rubric evals (3 criteria, 1–5 human scoring, written anchors; desk-scale human evaluation), (4) before/after comparison on sampled real cases (five cases; count your own cleanup time), (5) weekly review cadence (folds into the chapter's existing Friday review; drift detection).
   - **Verdict Rule** admonition: keep / fix / kill — "If you have never killed a workflow, you are not measuring — you are cheerleading."
   - Ties measurement into the chapter's compounding-loop thesis (numbers choose the lessons) and into the Astoria case study's board-ROI question (Tessa Iyer name-checked, no case-study text touched).
   - New figure directive: `ch12-7-measuring-results.png`.
   - **New activity (experiential): "Try It: Measure One Workflow You Already Built"** — 8 numbered steps: pick a workflow built earlier in the book (Ch 4 skill or Ch 2 Cowork task or this chapter's Track A loop), write the success sentence before anything runs, build a printed 3-criterion rubric with default 1/3/5 anchors (Accuracy / Fit for purpose / Voice-format), five hand-done baseline cases (timed + scored), five fresh real cases through the workflow (end-to-end timing including review/fix), score finals with same anchors, compute four comparison averages, verdict paragraph ending in bold **keep**/**fix**/**kill** with fix→standing-brief lesson and keep→quarterly re-measure. Deliverable: ten-row scores table + four comparison numbers + verdict paragraph.

2. **End-of-chapter comment block** `<!-- NEW IMAGES NEEDED: ... -->` for the new figure.

## Subfile cross-refs (one line each, appended)

- `chapters/ch11-1-when-to-reach-for-sdk.md` → pointer to Ch 11's hosted-agents + enterprise-platforms sections.
- `chapters/ch12-4-continuous-improvement.md` → pointer to Ch 12's Measuring Results section.

## Not touched

- All existing prose, figures, admonitions, case studies (Cypress Coastal, Astoria CloudWorks), discussion guidelines, and Applied Exercise tracks/step numbering in ch11.md and ch12.md.
- Quizzes, case-studies, canvas-pages, exercises directories.
- All other chapters (other agents' scope).
