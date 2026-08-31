# Applied Exercise — Chapter 14: Security and Trust — Building Inside the Guardrails
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Build Your AI Security Posture in 30 Minutes

*Estimated time: 25–30 minutes. You'll produce a one-page security posture document — a list of approved tools, the four questions answered for each, and a draft of the fifteen-minute employee briefing — that you can hand to your team next week.*

The goal of this exercise is not to design a perfect security program. The goal is to produce the artifact that closes the largest gap most businesses have today: a single page that any employee can read and understand.

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace that runs the audit as a background task (Track C). All three tracks produce the same three artifacts: an approved-tools list with the four security questions answered for each tool, a ranked list of risk gaps, and the fifteen-minute team briefing. Product names, menu locations, and exact click-paths change too fast for print; the current versions of all three tracks live on the companion page at cognitioneconomy.net/ch14-companion. The companion page is date-stamped; this book is not.
:::

### Track A — Chat Assistant

*Estimated time: under 20 minutes. A single conversation. No tools, no installs.*

1. Open your chat assistant.

2. Describe your current AI usage honestly. Which tools does your team actually use — the major assistants, the coding tools, the niche vertical products, the free trials someone installed last month? What kinds of data get pasted in (client names, contracts, financials, code, HR data)? Which subscriptions are consumer tier and which are enterprise or business with a data-protection agreement? Do not sanitize the picture — the audit only works if the inputs are true.

3. Ask the AI to produce three artifacts from what you described: *"(1) a list of our current AI tools with the four security questions answered for each, (2) a ranked list of my top three security risk gaps with what to do about each, and (3) a draft of a fifteen-minute briefing I could give my team about responsible AI use, based on those risks."* Read each carefully. Push back if anything feels off.

4. For the security questions you cannot answer for a given tool, take that as your action list — those are the vendors whose current Data Processing Addendum you need to pull this week.

5. Edit the fifteen-minute briefing for your firm's voice and your team's specific examples. The generic version will be eighty percent right; your edits make it land for your people. Save all three artifacts to a single document. That document IS the security posture and the cultural layer from this chapter. Send the briefing to your team this week.

**Your Submission:** Your submission is all three artifacts the AI produced from your security audit: the approved-tools list with the four security questions answered for each tool, the ranked risk gaps list, and the 15-minute team briefing. Copy all three into one document. Write two sentences: (1) which risk gap surprised you most and what will you do about it in the next two weeks, and (2) who on your team most needs to read the 15-minute briefing? Submit the three artifacts + two sentences.

### Track B — Terminal Agent

The terminal agent's advantage for this exercise is that the audit ends as a *file you own* — a security-posture document living in your own working folder, not a transcript trapped in a chat history. The exact commands for your tool are on the companion page (cognitioneconomy.net/ch14-companion); what matters here is which decision each step sets.

1. **Set the interview dial: one question at a time.** Open a session and paste this structured prompt: *"I am the [your role] at a [size and industry] company. Help me audit our current AI usage. Ask me one question at a time about which AI tools my team uses, what kind of data each tool touches, and what tier — consumer or enterprise — we are on. After you have a complete picture, produce three artifacts for me: (1) a list of our current AI tools with the four security questions answered for each, (2) a ranked list of the highest-risk gaps in our current setup, and (3) a draft of a fifteen-minute employee briefing in one page."* The one-question-at-a-time structure is the decision: an interview surfaces tools and data flows you would forget to volunteer in a single description.

2. **Answer honestly.** The value of the exercise comes from the accuracy of your answers, not from looking good. If your team is using consumer tools, say so. If you do not know how a vendor handles data retention, say that too — every "I don't know" is data.

3. **Turn the unanswerables into the action list.** Review the three artifacts. For every security question the audit could not answer for a given tool, the move is the same one from this chapter's verify sidebar: pull that vendor's current Data Processing Addendum this week, find the three phrases, and — where the deployment warrants it — get ZDR in writing.

4. **Edit the briefing for your firm's voice.** The generic version will be eighty percent right; your edits — your team's real examples, your firm's real tools — make it land for your people.

5. **Save the artifact as a file.** Save the final document to a file named `ai-security-posture.md` in your working folder. Schedule the briefing for the next team meeting. The artifact is the deliverable; the briefing is the activation.

**Your Submission:** Your submission is the same three artifacts the agent produced — the approved-tools list with the four questions answered, the ranked risk gaps, and the team briefing — plus a personal action plan you write yourself: three specific changes you will make to your team's AI usage within 30 days, each with a deadline. Copy everything into one document. Submit the three artifacts + personal action plan.

### Track C — Agent-Orchestration Workspace

The orchestration workspace adds something the other two surfaces cannot: before you run the audit, you audit the *workspace itself*. The current tool name and the toggle that opens the manager view are on the companion page (cognitioneconomy.net/ch14-companion).

1. **Open the orchestration view.** Switch from the editing surface to the manager view — the overview where background tasks run side by side.

2. **Run the least-privilege audit first.** Before starting a new task, review which projects or workspaces have which data-access permissions. Orchestration surfaces organize work at the project level, and each project can be scoped to specific data sources. Note any project that has broader permissions than its current work actually needs — that is Practice One from this chapter, observed live in your own tooling. Keep the notes; they feed your risk-gaps list.

3. **Start the audit task, scoped deliberately.** Start a new background task using the same structured interview prompt printed in Track B, step 1 — one question at a time, then three artifacts. Scope the task to a project with appropriate data permissions for this kind of sensitive review. Choosing the scope *is* the exercise: you are applying least privilege to the audit of your least-privilege posture.

4. **Review the deliverables as they appear.** The workspace will produce artifacts asynchronously — drafts, comparison tables, the final one-page document. Review each as it lands and provide feedback in the task, the same way you would redline a junior analyst's draft.

5. **Save the artifacts to the project.** Note for yourself which surface you found easier to think alongside, and which produced the briefing document you would actually hand to your team.

**Your Submission:** Your submission is the three artifacts the agent produced — approved-tools list, ranked risk gaps, and team briefing — plus one paragraph (100–150 words) you write describing your current security posture honestly, not aspirationally, and identifying your single highest-priority gap. Submit the three artifacts + one paragraph.

### Reflection

Write two to three sentences capturing what you noticed about your own firm's security posture during the audit. Where were you confident? Where were you uncertain? What is the single most important action — concrete, specific, doable in the next week — that this exercise made obvious to you?

---

*The deeper lesson of this exercise is not the document itself. It is what happens when you sit down to write the document and discover, often for the first time, what you do and do not actually know about your own firm's AI usage. That moment of clarity is the beginning of a real security posture. Everything after it is execution.*

---
*Applied Exercise for Chapter 14 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
