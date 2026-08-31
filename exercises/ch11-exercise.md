# Applied Exercise — Chapter 11: The Agent SDK — When to Build vs. When to Use
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Applied Exercise: Brief an SDK Project Without Writing a Line of Code

*Estimated time: 25–30 minutes. You'll produce a one-page SDK project brief you could hand to an engineering team — or take to a no-code platform — to build the automation you actually want.*

:::{admonition} One Exercise, Three Surfaces
:class: tip
You only need to complete **one track** for this chapter. The three tracks teach the same concept on the three surface types this book uses throughout: a chat assistant (Track A), a terminal agent that lives inside a development environment (Track B), and an agent-orchestration workspace built for running several agents at once (Track C). Product names, download links, and exact click-paths change too fast for print; the current versions of all three tracks are on the companion page at cognitioneconomy.net/ch11-companion.
:::

### Track A — Chat Assistant

The SDK is ultimately a decision-making exercise: *do I build, buy, or keep doing this by hand?* You can run that decision today, in any chat surface, in under ten minutes — without writing a line of code.

1. Open your AI assistant — the chat surface you configured in Chapter 2.
2. Describe your most painful recurring workflow — the one you do manually every week or every month that eats the most time. Be specific: how often, how long, what the inputs are, what the output looks like.
3. Paste this prompt: *"Evaluate this workflow. Should I customize an AI specialist for this task, buy an off-the-shelf tool, or keep doing it manually? Give me a clear recommendation with reasoning — cost, time-to-value, switching cost, and how often the workflow changes."*
4. Read the recommendation. If the assistant says *build a specialist*, paste this follow-up: *"Draft the standing instructions for that specialist — what it does, what it does not do, what inputs it expects, what format the output takes, and how I should review its work."*
5. What you just produced is an SDK spec in plain English. Engineers wrap that spec in code. You wrote the part that actually matters — the part most teams skip.

**Your Submission:** Your submission is the assistant's build-vs-buy recommendation for your most painful recurring workflow, plus the plain-English standing instructions for the specialist (if it recommended building). Copy both into one document. Write one sentence: do you agree with the recommendation, and if not, what would change your mind? Submit the recommendation + standing instructions + one sentence.

### Track B — Terminal Agent

The terminal agent is your thinking partner for this track — you will not write code. You will use the agent to draft a project brief an engineer could act on. The exact setup steps and the current link to the vendor's SDK overview page are on the companion page (cognitioneconomy.net/ch11-companion).

Start by identifying a real workflow in your work that consumes too many hours. Not a hypothetical. A real one. Write down the name of the workflow and the approximate hours per week it consumes.

1. **Open your terminal agent.** Have the vendor's Agent SDK overview page open beside it — this is the same page you skimmed in "Reading SDK Documentation Like a Business Person." Current link: companion site.
2. **Provide context.** Paste the following into the agent: *"I want to draft a business-grade Agent SDK project brief for an automation in my organization. I am not a developer — I am the business owner. I will describe the workflow in plain English, and I want you to help me structure a one-page brief that includes outcome, inputs, outputs, constraints, and success measures — using the framework from Chapter 11 of The Cognition Economy."*
3. **Describe the workflow.** Tell the agent, in plain English, what the workflow does today. Who does it? What inputs do they work from? What outputs do they produce? How long does it take? Where does it live (which tools, which systems)?
4. **Ask for the brief.** Prompt the agent: *"Now draft the five-section project brief. Be specific. Make it short enough that an engineer could read it in five minutes."*
5. **Stress-test it.** Ask the agent: *"What are the three red flags in this brief that an experienced AI engineer would push back on? What constraints am I likely missing?"*
6. **Save the artifact.** Save the finished brief as a markdown file. This is what you would hand to your engineering team — or upload to a no-code platform — to start the project.

**Your Submission:** Your submission is the one-page Agent SDK project brief your terminal agent helped you draft — outcome, inputs, outputs, constraints, and success measures. Copy the full brief into a document. Write two sentences: (1) who in your organization would need to review and approve this brief before development could begin, and (2) what is the most important constraint you included that you almost left out? Submit the brief + two sentences.

### Track C — Agent-Orchestration Workspace

The orchestration workspace gives you something the other two tracks cannot: a front-row seat to the agent loop itself — the same loop the SDK packages for engineers. The current tool name and the toggle that opens the manager view are on the companion page (cognitioneconomy.net/ch11-companion).

1. **Open the orchestration view.** Switch from the editing surface to the manager view — the overview built for delegating tasks to agents and reviewing what they produce. Confirm you are in the orchestration view, not the editor. Exact click-path: companion site.
2. **Start a new agent task.** Create a new task with the prompt: *"Help me draft a business-grade Agent SDK project brief for an automation I want to build. I am a business leader, not a developer."*
3. **Observe the agent loop.** Watch how the agent works through the request — pulling context, structuring sections, producing artifacts. You are observing the same agent loop pattern that powers any SDK-based agent, including the one you would commission your engineering team to build.
4. **Describe your workflow.** Provide the same plain-English description of the workflow you would automate.
5. **Review the artifacts.** The agent will produce one or more structured deliverables as it works. Open them, review them, and notice how the agent has structured your raw description into a usable project brief.
6. **Refine and export.** Ask the agent to tighten any section that feels weak, then export the final brief as a markdown file you can share.

**Your Submission:** Your submission is the Agent SDK project brief the orchestration agent produced, plus your written agreement or disagreement with it. Copy the brief into a document. Underneath it, write one paragraph (75–100 words) either confirming the agent got the brief right or correcting the specific things it missed. Submit the brief + your one paragraph.

### Reflection
Write two or three sentences about what you noticed. Did the build-buy-or-manual recommendation match the instinct you walked in with — and if not, what specifically shifted your thinking? If you ran more than one surface, where did they handle the same task differently — which felt more like a thinking partner, and which more like an autonomous worker? And — most importantly — could you imagine handing the brief you just produced to a real engineering team or a no-code platform on Monday morning?

---
*Applied Exercise for Chapter 11 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
