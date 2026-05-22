# Applied Exercise — Chapter 11: The Agent SDK — When to Build vs. When to Use
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Brief an SDK Project Without Writing a Line of Code

*Estimated time: 25–30 minutes. You'll produce a one-page SDK project brief you could hand to an engineering team — or take to a no-code platform — to build the automation you actually want.*

:::{admonition} Choose Your Track
:class: tip
You only need to complete **one track** for this chapter. Pick the tool you have installed or want to learn. All three tracks teach the same concept — they just use different surfaces.

- **Track A — Claude Desktop:** The simplest starting point. Use claude.ai in your browser or download Claude Desktop at claude.ai/download.
- **Track B — Claude Code:** For students using Claude Code. Reference the quickstart at code.claude.com/docs/en/quickstart.
- **Track C — Antigravity 2.0 IDE:** For students using the Antigravity 2.0 IDE Agent Manager. Reference antigravity.google/docs/ide-overview.
:::

### Track A — Claude Desktop

The SDK is ultimately a decision-making exercise: *do I build, buy, or keep doing this by hand?* You can run that decision today, in a browser, in under ten minutes — without writing a line of code.

1. Open **Claude Desktop** (claude.ai/download) or **claude.ai** in your browser.
2. Describe your most painful recurring workflow — the one you do manually every week or every month that eats the most time. Be specific: how often, how long, what the inputs are, what the output looks like.
3. Paste this prompt: *"Evaluate this workflow. Should I customize an AI specialist for this task, buy an off-the-shelf tool, or keep doing it manually? Give me a clear recommendation with reasoning — cost, time-to-value, switching cost, and how often the workflow changes."*
4. Read the recommendation. If Claude says *build a specialist*, paste this follow-up: *"Draft the standing instructions for that specialist — what it does, what it does not do, what inputs it expects, what format the output takes, and how I should review its work."*
5. What you just produced is an SDK spec in plain English. Engineers wrap that spec in code. You wrote the part that actually matters — the part most teams skip.

**Your Submission:** Your submission is Claude's build-vs-buy recommendation for your most painful recurring workflow, plus the plain-English standing instructions for the specialist (if Claude recommended building). Copy both into one document. Write one sentence: do you agree with Claude's recommendation, and if not, what would change your mind? Submit the recommendation + standing instructions + one sentence.

### Track B — Claude Code

Start by identifying a real workflow in your work that consumes too many hours. Not a hypothetical. A real one. Write down the name of the workflow and the approximate hours per week it consumes.

1. **Open Claude Code.** Reference the Agent SDK overview documentation at https://code.claude.com/docs/en/agent-sdk/overview. You will not write code in this exercise — you will use Claude Code as your thinking partner to draft a project brief.
2. **Provide context.** Paste the following into Claude Code: *"I want to draft a business-grade Agent SDK project brief for an automation in my organization. I am not a developer — I am the business owner. I will describe the workflow in plain English, and I want you to help me structure a one-page brief that includes outcome, inputs, outputs, constraints, and success measures — using the framework from Chapter 11 of The Cognition Economy."*
3. **Describe the workflow.** Tell Claude Code, in plain English, what the workflow does today. Who does it? What inputs do they work from? What outputs do they produce? How long does it take? Where does it live (which tools, which systems)?
4. **Ask for the brief.** Prompt Claude Code: *"Now draft the five-section project brief. Be specific. Make it short enough that an engineer could read it in five minutes."*
5. **Stress-test it.** Ask Claude Code: *"What are the three red flags in this brief that an experienced AI engineer would push back on? What constraints am I likely missing?"*
6. **Save the artifact.** Save the finished brief as a markdown file. This is what you would hand to your engineering team — or upload to a no-code platform — to start the project.

**Your Submission:** Your submission is the one-page Agent SDK project brief Claude Code helped you draft — outcome, inputs, outputs, constraints, and success measures. Copy the full brief into a document. Write two sentences: (1) who in your organization would need to review and approve this brief before development could begin, and (2) what is the most important constraint you included that you almost left out? Submit the brief + two sentences.

### Track C — Antigravity 2.0 IDE

1. **Open Antigravity 2.0 IDE.** Press CMD+E (or CTRL+E on Windows) to switch to Agent Manager. Reference https://antigravity.google/docs/ide-overview to confirm you are in the orchestration view, not the editor.
2. **Start a new agent task.** In Agent Manager, create a new task with the prompt: *"Help me draft a business-grade Agent SDK project brief for an automation I want to build. I am a business leader, not a developer."*
3. **Observe the agent loop.** Watch how the Antigravity agent works through the request — pulling context, structuring sections, producing artifacts. You are observing the same agent loop pattern that powers any SDK-based agent, including the one you would commission your engineering team to build.
4. **Describe your workflow.** Provide the same plain-English description of the workflow you would automate.
5. **Review the artifacts.** Antigravity will produce one or more markdown artifacts as it works. Open them, review them, and notice how the agent has structured your raw description into a usable project brief.
6. **Refine and export.** Ask the agent to tighten any section that feels weak, then export the final brief as a markdown file you can share.

**Your Submission:** Your submission is the Agent SDK project brief the Antigravity agent produced, plus your written agreement or disagreement with it. Copy the brief into a document. Underneath it, write one paragraph (75-100 words) either confirming the agent got the brief right or correcting the specific things it missed. Submit the brief + your one paragraph.

### Reflection
Write two or three sentences about what you noticed. Where did the two tools handle the same task differently? Which felt more like a thinking partner, and which felt more like an autonomous worker? And — most importantly — could you imagine handing the brief you just produced to a real engineering team or a no-code platform on Monday morning?

---
*Applied Exercise for Chapter 11 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
