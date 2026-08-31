# Chapter 11 Readings — The Agent SDK: When to Build vs. When to Use
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Overview

Claude Code is the meal. The Agent SDK is the kitchen. This chapter teaches business leaders to read the AI build-vs-buy landscape clearly enough to know what they are actually being sold — and to make the right call without learning to code. You will leave knowing the four real options, when each fits, and how to brief an engineering team (or a no-code platform) on the automation your business actually needs.

## What You Will Learn

- Why Anthropic's release of the Agent SDK is the "McDonald's move" — selling the system that produces the product.
- The four-question build-vs-buy framework: customer-facing? sensitive data? strategic capability? unique workflow?
- The four real options: Claude Code as a tool, vendor wrappers, no-code platforms, or a true SDK build — and when each one wins.
- What the SDK actually provides under the hood: built-in tools, the agent loop, context management, and permissions/auditability.
- The five-section project brief format (outcome, inputs, outputs, constraints, success measures) that turns a vague idea into a buildable spec.

## Chapter Summary

The chapter opens with Helena Vasquez, COO of a Tampa P&C insurance carrier, staring at three proposals for the same workflow: $400K/year from a national InsurTech vendor, $80K one-time from her own engineer using the Agent SDK, and $30K/year from a no-code platform. Same problem (9,000 first-notice-of-loss reports per year), three completely different risk profiles, and every pitch deck used the same words. The chapter is about how Helena — and you — make that call.

Dr. Lee then explains what Anthropic actually did with the SDK using the McDonald's metaphor. McDonald's is not in the hamburger business; it is in the *system* business — the kitchen, supply chain, operations manual, and training program that produces hamburgers at scale. Anthropic took the engine that powers Claude Code (the agent loop, tool orchestration, context management, permission system) and made it available so any company can build their own AI products without becoming an AI lab. The strategic shift is from being an AI customer (consumption) to being an AI builder (deployment) — without becoming an AI company.

The build-vs-buy framework comes next. Four options. Claude Code is enough if the workflow lives entirely inside your team. A vendor wrapper is right when someone has already built for a common problem. A no-code platform is the right starting point for most internal automation — established automation platforms with agent steps and newer agent-native platforms wrap SDK-level capability in a visual interface (names churn quickly; the companion site keeps a current list). A true SDK build is reserved for the small number of capabilities that are customer-facing, deeply integrated with your data, or strategically differentiated. The chapter is blunt that most leaders default to the vendor or the build when the no-code option would have done eighty percent of the job for ten percent of the price.

The chapter closes with practical skills: what the SDK actually gives you (so you can read vendor pitches critically), how to write a five-section project brief (outcome, inputs, outputs, constraints, success measures), and how to skim technical documentation as a business person — read headers, comparison tables, and license sections; skip the code blocks. The Cypress Coastal Insurance case study returns to Helena's three proposals and forces a decision: vendor, custom build, or no-code, for a firm with real data residency constraints and a four-month timeline.

## Why This Matters

The single most expensive AI decision your organization will make this year is not which model to use — it is which architectural layer to build at. Get this wrong and you spend $400K/year on a vendor that ships your data outside your firewall, or you spend $80K and four months building something a no-code platform could have done in a week. Get it right and you compose a portfolio: Claude Code for internal research, no-code for back-office automation, vendors for specialized vertical needs, and SDK builds reserved for the one or two capabilities that genuinely differentiate the firm. The four options are not competitors; they are a stack you run simultaneously.

After this chapter a leader can read a vendor proposal critically and ask the questions vendors hate: "How much of this quote is just the SDK's built-in tools wired together?" "Where does our data live?" "What's the audit trail look like?" "Could a no-code platform do 80% of this for 10% of the cost?" Those four questions alone will save most mid-sized organizations seven figures over the next three years. More importantly, the leader becomes an active partner in architectural decisions rather than a passive recipient of whatever the engineering team or the vendor recommends — and that shift in posture is what determines whether your organization is an AI consumer or an AI builder over the next decade.

## How It Applies in Your Work

- **A COO evaluating an AI automation proposal** would apply the four-question framework before any meeting: is this customer-facing, does it touch sensitive data, is it strategic or tactical, and how unique is the workflow? In Helena's situation those answers point hard toward "build inside our firewall" — but a leader who skipped the framework would have signed the $400K vendor contract because the demo was the slickest.

- **A head of operations at a mid-market law firm** would prototype every internal workflow on a no-code platform first (intake summarization, conflicts pre-check, time-entry drafting). Only when a workflow outgrows the platform — usually a customer-facing or compliance-heavy one — does it justify the SDK build. The two-track strategy (no-code first, SDK only when no-code hits a wall) is cheaper and faster than starting with the SDK.

- **A VP of Engineering being asked to "build something with AI"** would push back with the five-section brief: what outcome are we measuring? what inputs already exist? what specific output do we need? what regulatory or business constraints are non-negotiable? what does success look like at week six? Without those answers, the project becomes a two-year exploration that arrives nowhere.

- **A CMO evaluating a SaaS AI tool** would spend fifteen minutes skimming the vendor's underlying SDK documentation — read the headers, the comparison tables, and the license section; skip the code. That fifteen-minute read turns a sales conversation into a procurement conversation and exposes whether the vendor is selling real capability or just a wrapper around the same SDK you could deploy yourself.

## Read the Chapter

**→ [Chapter 11: The Agent SDK — When to Build vs. When to Use](http://cognitioneconomy.net/ch11/)**

Read the full chapter at the link above before participating in the discussion board or completing the applied exercise for this module.

*Estimated reading time: 35 minutes*

## What to Look For While Reading

As you read, pay special attention to:

- The "McDonald's Move" metaphor — selling the kitchen, not the meal — and what it means strategically.
- The four-question build-vs-buy framework: customer-facing, sensitive data, strategic, unique.
- The Cypress Coastal Insurance case study and the three competing proposals (vendor, custom SDK, no-code).
- The five-section project brief format — this structure appears directly in the discussion prompt and applied exercise.

---
*Canvas Reading Page — Chapter 11 — The Cognition Economy © Dr. Ernesto Lee, 2026.*
