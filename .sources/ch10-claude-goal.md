# Scraped: https://code.claude.com/docs/en/goal

[Skip to main content](https://code.claude.com/docs/en/goal#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Automation

Keep Claude working toward a goal

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/agents) [Administration](https://code.claude.com/docs/en/admin-setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) [What's New](https://code.claude.com/docs/en/whats-new) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

`/goal` requires Claude Code v2.1.139 or later.

The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds. If not, Claude starts another turn instead of returning control to you. The goal clears automatically once the condition is met.Use a goal for substantial work with a verifiable end state:

- Migrating a module to a new API until every call site compiles and tests pass
- Implementing a design doc until all acceptance criteria hold
- Splitting a large file into focused modules until each is under a size budget
- Working through a labeled issue backlog until the queue is empty

This page covers how to:

- [Compare autonomous workflow approaches](https://code.claude.com/docs/en/goal#compare-to-other-autonomous-workflows): `/loop`, Stop hooks, and auto mode
- [Set a goal](https://code.claude.com/docs/en/goal#set-a-goal) and [write an effective condition](https://code.claude.com/docs/en/goal#write-an-effective-condition)
- [Check status](https://code.claude.com/docs/en/goal#check-status), [clear early](https://code.claude.com/docs/en/goal#clear-a-goal), and [run non-interactively](https://code.claude.com/docs/en/goal#run-non-interactively)
- See [how evaluation works](https://code.claude.com/docs/en/goal#how-evaluation-works) and [requirements](https://code.claude.com/docs/en/goal#requirements)

## [​](https://code.claude.com/docs/en/goal\#compare-to-other-autonomous-workflows)  Compare to other autonomous workflows

Three approaches keep the current session running between prompts. Pick based on what should start the next turn:

| Approach | Next turn starts when | Stops when |
| --- | --- | --- |
| `/goal` | The previous turn finishes | A model confirms the condition is met |
| [`/loop`](https://code.claude.com/docs/en/scheduled-tasks#run-a-prompt-repeatedly-with-%2Floop) | A time interval elapses | You stop it, or Claude decides the work is done |
| [Stop hook](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks) | The previous turn finishes | Your own script or prompt decides |

`/goal` and a Stop hook both fire after every turn. `/goal` is a session-scoped shortcut: you type a condition and it’s active for the current session only. A Stop hook lives in your settings file, applies to every session in its scope, and can run a script for deterministic checks or a prompt for model-evaluated ones.[Auto mode](https://code.claude.com/docs/en/auto-mode-config) on its own approves tool calls within a single turn but doesn’t start a new one. Claude stops when it judges the work done. `/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work. The two are complementary: auto mode removes per-tool prompts, and `/goal` removes per-turn prompts.

The approaches above keep the current session running. You can also schedule work that runs independent of any open session, such as nightly tests or morning triage. See [scheduling options](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options) for cloud routines and desktop scheduled tasks.

## [​](https://code.claude.com/docs/en/goal\#use-/goal)  Use `/goal`

One goal can be active per session. The same command sets, checks, and clears it depending on the argument.

### [​](https://code.claude.com/docs/en/goal\#set-a-goal)  Set a goal

Run `/goal` followed by the condition you want satisfied. If a goal is already active, the new one replaces it.

```
/goal all tests in test/auth pass and the lint step is clean
```

Setting a goal starts a turn immediately, with the condition itself as the directive. You don’t need to send a separate prompt. While the goal is active, a `◎ /goal active` indicator shows how long the goal has been running.After each turn, the evaluator returns a short reason explaining why the condition is or isn’t met. The most recent reason appears in the status view and in the transcript so you can see what Claude is working toward next.

A goal keeps running until the condition is met or you run `/goal clear`. Run `/goal` with no argument to see turns and tokens spent so far.

### [​](https://code.claude.com/docs/en/goal\#write-an-effective-condition)  Write an effective condition

The [evaluator](https://code.claude.com/docs/en/goal#how-evaluation-works) judges your condition against what Claude has surfaced in the conversation. It doesn’t run commands or read files independently, so write the condition as something Claude’s own output can demonstrate. “All tests in `test/auth` pass” works because Claude runs the tests and the result lands in the transcript for the evaluator to read.A condition that holds up across many turns usually has:

- **One measurable end state**: a test result, a build exit code, a file count, an empty queue
- **A stated check**: how Claude should prove it, such as “`npm test` exits 0” or “`git status` is clean”
- **Constraints that matter**: anything that must not change on the way there, such as “no other test file is modified”

The condition can be up to 4,000 characters.To bound how long a goal runs, include a turn or time clause in the condition, such as `or stop after 20 turns`. Claude reports progress against that clause each turn and the evaluator judges it from the conversation.

### [​](https://code.claude.com/docs/en/goal\#check-status)  Check status

Run `/goal` with no arguments to see the current state.

```
/goal
```

If a goal is active, the status shows:

- The condition
- How long it has been running
- How many turns have been evaluated
- The current token spend
- The evaluator’s most recent reason

If no goal is active but one was achieved earlier in the session, the status shows the achieved condition along with its duration, turn count, and token spend.

### [​](https://code.claude.com/docs/en/goal\#clear-a-goal)  Clear a goal

Run `/goal clear` to remove an active goal before its condition is met.

```
/goal clear
```

`stop`, `off`, `reset`, `none`, and `cancel` are accepted as aliases for `clear`. Running `/clear` to start a new conversation also removes any active goal.

### [​](https://code.claude.com/docs/en/goal\#resume-with-an-active-goal)  Resume with an active goal

A goal that was still active when a session ended is restored when you resume that session with `--resume` or `--continue`. The condition carries over, but the turn count, timer, and token-spend baseline all reset on resume. A goal that was already achieved or cleared is not restored.

### [​](https://code.claude.com/docs/en/goal\#run-non-interactively)  Run non-interactively

`/goal` works in [non-interactive mode](https://code.claude.com/docs/en/headless), in the [desktop app](https://code.claude.com/docs/en/desktop), and through [Remote Control](https://code.claude.com/docs/en/remote-control). Setting a goal with `-p` runs the loop to completion in a single invocation:

```
claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"
```

Interrupt the process with Ctrl+C to stop a non-interactive goal before the condition is met.

## [​](https://code.claude.com/docs/en/goal\#how-evaluation-works)  How evaluation works

`/goal` is a wrapper around a session-scoped [prompt-based Stop hook](https://code.claude.com/docs/en/hooks#prompt-based-hooks). Each time Claude finishes a turn, the condition and the conversation so far are sent to your configured [small fast model](https://code.claude.com/docs/en/model-config), which defaults to Haiku. The model returns a yes-or-no decision and a short reason. A “no” tells Claude to keep working and includes the reason as guidance for the next turn. A “yes” clears the goal and records an achieved entry in the transcript.The evaluator runs on whichever provider your session is configured for. It does not call tools, so it can only judge what Claude has already surfaced in the conversation.

Evaluation tokens are billed on the small fast model configured for your provider and are typically negligible compared to main-turn spend.

## [​](https://code.claude.com/docs/en/goal\#requirements)  Requirements

`/goal` runs only in workspaces where you have accepted the trust dialog, because the evaluator is part of the hooks system. `/goal` is also unavailable when [`disableAllHooks`](https://code.claude.com/docs/en/hooks#disable-or-remove-hooks) is set at any settings level or when [`allowManagedHooksOnly`](https://code.claude.com/docs/en/settings#hook-configuration) is set in managed settings. In each case, the command tells you why instead of silently doing nothing.

## [​](https://code.claude.com/docs/en/goal\#see-also)  See also

- [Run a prompt repeatedly with `/loop`](https://code.claude.com/docs/en/scheduled-tasks#run-a-prompt-repeatedly-with-%2Floop): re-run on a time interval instead of until a condition holds
- [Prompt-based hooks](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks): write your own Stop hook when you need custom evaluation logic
- [Auto mode](https://code.claude.com/docs/en/auto-mode-config): approve tool calls automatically so each goal turn runs unattended
- [Scheduling comparison](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options): run work on a schedule independent of any open session

Was this page helpful?

YesNo

[Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks) [Programmatic usage](https://code.claude.com/docs/en/headless)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---
Metadata: {
  "charset": "utf-8",
  "ogImage": "https://claude-code.mintlify.app/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DAutomation%26appearance%3Dsystem%26title%3DKeep%2BClaude%2Bworking%2Btoward%2Ba%2Bgoal%26description%3DSet%2Ba%2Bcompletion%2Bcondition%2Bwith%2B%252Fgoal%2Band%2BClaude%2Bkeeps%2Bworking%2Bacross%2Bturns%2Buntil%2Bthe%2Bcondition%2Bis%2Bmet.%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Flight.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D78fd01ff4f4340295a4f66e2ea54903c%26logoDark%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Fdark.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D1298a0c3b3a1da603b190d0de0e31712%26primaryColor%3D%25230E0E0E%26lightColor%3D%2523D4A27F%26darkColor%3D%25230E0E0E%26backgroundLight%3D%2523FDFDF7%26backgroundDark%3D%252309090B&w=1200&q=100",
  "twitter:title": "Keep Claude working toward a goal - Claude Code Docs",
  "description": "Set a completion condition with /goal and Claude keeps working across turns until the condition is met.",
  "twitter:image:width": "1200",
  "ogTitle": "Keep Claude working toward a goal - Claude Code Docs",
  "viewport": "width=device-width, initial-scale=1, viewport-fit=cover",
  "twitter:description": "Set a completion condition with /goal and Claude keeps working across turns until the condition is met.",
  "application-name": "Claude Code Docs",
  "generator": "Mintlify",
  "og:url": "https://code.claude.com/docs/en/goal",
  "next-size-adjust": "",
  "og:title": "Keep Claude working toward a goal - Claude Code Docs",
  "og:site_name": "Claude Code Docs",
  "msapplication-TileColor": "#0E0E0E",
  "title": "Keep Claude working toward a goal - Claude Code Docs",
  "canonical": "https://code.claude.com/docs/en/goal",
  "twitter:card": "summary_large_image",
  "language": "en",
  "apple-mobile-web-app-title": "Claude Code Docs",
  "og:description": "Set a completion condition with /goal and Claude keeps working across turns until the condition is met.",
  "ogDescription": "Set a completion condition with /goal and Claude keeps working across turns until the condition is met.",
  "og:type": "website",
  "og:image:width": "1200",
  "og:image:height": "630",
  "ogUrl": "https://code.claude.com/docs/en/goal",
  "og:image": "https://claude-code.mintlify.app/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DAutomation%26appearance%3Dsystem%26title%3DKeep%2BClaude%2Bworking%2Btoward%2Ba%2Bgoal%26description%3DSet%2Ba%2Bcompletion%2Bcondition%2Bwith%2B%252Fgoal%2Band%2BClaude%2Bkeeps%2Bworking%2Bacross%2Bturns%2Buntil%2Bthe%2Bcondition%2Bis%2Bmet.%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Flight.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D78fd01ff4f4340295a4f66e2ea54903c%26logoDark%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Fdark.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D1298a0c3b3a1da603b190d0de0e31712%26primaryColor%3D%25230E0E0E%26lightColor%3D%2523D4A27F%26darkColor%3D%25230E0E0E%26backgroundLight%3D%2523FDFDF7%26backgroundDark%3D%252309090B&w=1200&q=100",
  "twitter:image": "https://claude-code.mintlify.app/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DAutomation%26appearance%3Dsystem%26title%3DKeep%2BClaude%2Bworking%2Btoward%2Ba%2Bgoal%26description%3DSet%2Ba%2Bcompletion%2Bcondition%2Bwith%2B%252Fgoal%2Band%2BClaude%2Bkeeps%2Bworking%2Bacross%2Bturns%2Buntil%2Bthe%2Bcondition%2Bis%2Bmet.%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Flight.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D78fd01ff4f4340295a4f66e2ea54903c%26logoDark%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Fdark.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D1298a0c3b3a1da603b190d0de0e31712%26primaryColor%3D%25230E0E0E%26lightColor%3D%2523D4A27F%26darkColor%3D%25230E0E0E%26backgroundLight%3D%2523FDFDF7%26backgroundDark%3D%252309090B&w=1200&q=100",
  "twitter:image:height": "630",
  "msapplication-config": "/docs/_mintlify/favicons/claude-code/pLsy-mRpNksna2sx/_generated/favicon/browserconfig.xml",
  "favicon": "https://code.claude.com/docs/_mintlify/favicons/claude-code/pLsy-mRpNksna2sx/_generated/favicon/favicon-16x16.png",
  "scrapeId": "019e4fdd-7744-74ea-9460-b4154eeb1929",
  "sourceURL": "https://code.claude.com/docs/en/goal",
  "url": "https://code.claude.com/docs/en/goal",
  "statusCode": 200,
  "contentType": "text/html; charset=utf-8",
  "proxyUsed": "basic",
  "cacheState": "hit",
  "cachedAt": "2026-05-22T09:50:32.273Z",
  "creditsUsed": 1,
  "concurrencyLimited": false
}
