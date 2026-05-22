# Scraped: https://code.claude.com/docs/en/agent-sdk/overview

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/overview#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Agent SDK

Agent SDK overview

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/agents) [Administration](https://code.claude.com/docs/en/admin-setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) [What's New](https://code.claude.com/docs/en/whats-new) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit, separate from your interactive usage limits. See [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) for details.

Build AI agents that autonomously read files, run commands, search the web, edit code, and more. The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript.

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Find and fix the bug in auth.py",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"]),
    ):
        print(message)  # Claude reads the file, finds the bug, edits it

asyncio.run(main())
```

The Agent SDK includes built-in tools for reading files, running commands, and editing code, so your agent can start working immediately without you implementing tool execution. Dive into the quickstart or explore real agents built with the SDK:

[**Quickstart** \\
\\
Build a bug-fixing agent in minutes](https://code.claude.com/docs/en/agent-sdk/quickstart)

[**Example agents** \\
\\
Email assistant, research agent, and more](https://github.com/anthropics/claude-agent-sdk-demos)

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#get-started)  Get started

1

[Navigate to header](https://code.claude.com/docs/en/agent-sdk/overview#)

Install the SDK

- TypeScript

- Python


```
npm install @anthropic-ai/claude-agent-sdk
```

```
pip install claude-agent-sdk
```

The TypeScript SDK bundles a native Claude Code binary for your platform as an optional dependency, so you don’t need to install Claude Code separately.

2

[Navigate to header](https://code.claude.com/docs/en/agent-sdk/overview#)

Set your API key

Get an API key from the [Console](https://platform.claude.com/), then set it as an environment variable:

```
export ANTHROPIC_API_KEY=your-api-key
```

The SDK also supports authentication via third-party API providers:

- **Amazon Bedrock**: set `CLAUDE_CODE_USE_BEDROCK=1` environment variable and configure AWS credentials
- **Claude Platform on AWS**: set `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` and `ANTHROPIC_AWS_WORKSPACE_ID`, then configure AWS credentials
- **Google Vertex AI**: set `CLAUDE_CODE_USE_VERTEX=1` environment variable and configure Google Cloud credentials
- **Microsoft Azure**: set `CLAUDE_CODE_USE_FOUNDRY=1` environment variable and configure Azure credentials

See the setup guides for [Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Claude Platform on AWS](https://code.claude.com/docs/en/claude-platform-on-aws), [Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), or [Azure AI Foundry](https://code.claude.com/docs/en/microsoft-foundry) for details.

Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead.

3

[Navigate to header](https://code.claude.com/docs/en/agent-sdk/overview#)

Run your first agent

This example creates an agent that lists files in your current directory using built-in tools.

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="What files are in this directory?",
        options=ClaudeAgentOptions(allowed_tools=["Bash", "Glob"]),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

**Ready to build?** Follow the [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart) to create an agent that finds and fixes bugs in minutes.

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#capabilities)  Capabilities

Everything that makes Claude Code powerful is available in the SDK:

- Built-in tools

- Hooks

- Subagents

- MCP

- Permissions

- Sessions


Your agent can read files, run commands, and search codebases out of the box. Key tools include:

| Tool | What it does |
| --- | --- |
| **Read** | Read any file in the working directory |
| **Write** | Create new files |
| **Edit** | Make precise edits to existing files |
| **Bash** | Run terminal commands, scripts, git operations |
| **Monitor** | Watch a background script and react to each output line as an event |
| **Glob** | Find files by pattern (`**/*.ts`, `src/**/*.py`) |
| **Grep** | Search file contents with regex |
| **WebSearch** | Search the web for current information |
| **WebFetch** | Fetch and parse web page content |
| **[AskUserQuestion](https://code.claude.com/docs/en/agent-sdk/user-input#handle-clarifying-questions)** | Ask the user clarifying questions with multiple choice options |

This example creates an agent that searches your codebase for TODO comments:

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Find all TODO comments and create a summary",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Glob", "Grep"]),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

Run custom code at key points in the agent lifecycle. SDK hooks use callback functions to validate, log, block, or transform agent behavior.**Available hooks:**`PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`, `SessionEnd`, `UserPromptSubmit`, and more.This example logs all file changes to an audit file:

Python

TypeScript

```
import asyncio
from datetime import datetime
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

async def log_file_change(input_data, tool_use_id, context):
    file_path = input_data.get("tool_input", {}).get("file_path", "unknown")
    with open("./audit.log", "a") as f:
        f.write(f"{datetime.now()}: modified {file_path}\n")
    return {}

async def main():
    async for message in query(
        prompt="Refactor utils.py to improve readability",
        options=ClaudeAgentOptions(
            permission_mode="acceptEdits",
            hooks={
                "PostToolUse": [\
                    HookMatcher(matcher="Edit|Write", hooks=[log_file_change])\
                ]
            },
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

[Learn more about hooks →](https://code.claude.com/docs/en/agent-sdk/hooks)

Spawn specialized agents to handle focused subtasks. Your main agent delegates work, and subagents report back with results.Define custom agents with specialized instructions. Include `Agent` in `allowedTools` since subagents are invoked via the Agent tool:

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def main():
    async for message in query(
        prompt="Use the code-reviewer agent to review this codebase",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Agent"],
            agents={
                "code-reviewer": AgentDefinition(
                    description="Expert code reviewer for quality and security reviews.",
                    prompt="Analyze code quality and suggest improvements.",
                    tools=["Read", "Glob", "Grep"],
                )
            },
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

Messages from within a subagent’s context include a `parent_tool_use_id` field, letting you track which messages belong to which subagent execution.[Learn more about subagents →](https://code.claude.com/docs/en/agent-sdk/subagents)

Connect to external systems via the Model Context Protocol: databases, browsers, APIs, and [hundreds more](https://github.com/modelcontextprotocol/servers).This example connects the [Playwright MCP server](https://github.com/microsoft/playwright-mcp) to give your agent browser automation capabilities:

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Open example.com and describe what you see",
        options=ClaudeAgentOptions(
            mcp_servers={
                "playwright": {"command": "npx", "args": ["@playwright/mcp@latest"]}
            }
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

[Learn more about MCP →](https://code.claude.com/docs/en/agent-sdk/mcp)

Control exactly which tools your agent can use. Allow safe operations, block dangerous ones, or require approval for sensitive actions.

For interactive approval prompts and the `AskUserQuestion` tool, see [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input).

This example creates a read-only agent that can analyze but not modify code. `allowed_tools` pre-approves `Read`, `Glob`, and `Grep`.

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Review this code for best practices",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep"],
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

[Learn more about permissions →](https://code.claude.com/docs/en/agent-sdk/permissions)

Maintain context across multiple exchanges. Claude remembers files read, analysis done, and conversation history. Resume sessions later, or fork them to explore different approaches.This example captures the session ID from the first query, then resumes to continue with full context:

Python

TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage, ResultMessage

async def main():
    session_id = None

    # First query: capture the session ID
    async for message in query(
        prompt="Read the authentication module",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Glob"]),
    ):
        if isinstance(message, SystemMessage) and message.subtype == "init":
            session_id = message.data["session_id"]

    # Resume with full context from the first query
    async for message in query(
        prompt="Now find all places that call it",  # "it" = auth module
        options=ClaudeAgentOptions(resume=session_id),
    ):
        if isinstance(message, ResultMessage):
            print(message.result)

asyncio.run(main())
```

[Learn more about sessions →](https://code.claude.com/docs/en/agent-sdk/sessions)

### [​](https://code.claude.com/docs/en/agent-sdk/overview\#claude-code-features)  Claude Code features

The SDK also supports Claude Code’s filesystem-based configuration. With default options the SDK loads these from `.claude/` in your working directory and `~/.claude/`. To restrict which sources load, set `setting_sources` (Python) or `settingSources` (TypeScript) in your options.

| Feature | Description | Location |
| --- | --- | --- |
| [Skills](https://code.claude.com/docs/en/agent-sdk/skills) | Specialized capabilities defined in Markdown | `.claude/skills/*/SKILL.md` |
| [Slash commands](https://code.claude.com/docs/en/agent-sdk/slash-commands) | Custom commands for common tasks | `.claude/commands/*.md` |
| [Memory](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) | Project context and instructions | `CLAUDE.md` or `.claude/CLAUDE.md` |
| [Plugins](https://code.claude.com/docs/en/agent-sdk/plugins) | Extend with custom commands, agents, and MCP servers | Programmatic via `plugins` option |

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#compare-the-agent-sdk-to-other-claude-tools)  Compare the Agent SDK to other Claude tools

The Claude Platform offers multiple ways to build with Claude. Here’s how the Agent SDK fits in:

- Agent SDK vs Client SDK

- Agent SDK vs Claude Code CLI

- Agent SDK vs Managed Agents


The [Anthropic Client SDK](https://platform.claude.com/docs/en/api/client-sdks) gives you direct API access: you send prompts and implement tool execution yourself. The **Agent SDK** gives you Claude with built-in tool execution.With the Client SDK, you implement a tool loop. With the Agent SDK, Claude handles it:

Python

TypeScript

```
# Client SDK: You implement the tool loop
response = client.messages.create(...)
while response.stop_reason == "tool_use":
    result = your_tool_executor(response.tool_use)
    response = client.messages.create(tool_result=result, **params)

# Agent SDK: Claude handles tools autonomously
async for message in query(prompt="Fix the bug in auth.py"):
    print(message)
```

Same capabilities, different interface:

| Use case | Best choice |
| --- | --- |
| Interactive development | CLI |
| CI/CD pipelines | SDK |
| Custom applications | SDK |
| One-off tasks | CLI |
| Production automation | SDK |

Many teams use both: CLI for daily development, SDK for production. Workflows translate directly between them.

[Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) is a hosted REST API: Anthropic runs the agent and the sandbox, and your application sends events and streams back results. The **Agent SDK** is a library that runs the agent loop inside your own process.

|  | Agent SDK | Managed Agents |
| --- | --- | --- |
| **Runs in** | Your process, your infrastructure | Anthropic-managed infrastructure |
| **Interface** | Python or TypeScript library | REST API |
| **Agent works on** | Files on your infrastructure | A managed sandbox per session |
| **Session state** | JSONL on your filesystem | Anthropic-hosted event log |
| **Custom tools** | In-process Python or TypeScript functions | Claude triggers the tool; you execute and return results |
| **Best for** | Local prototyping, agents that work directly on your filesystem and services | Production agents without operating sandbox or session infrastructure, long-running and asynchronous sessions |

A common path is to prototype with the Agent SDK locally, then move to Managed Agents for production.

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#changelog)  Changelog

View the full changelog for SDK updates, bug fixes, and new features:

- **TypeScript SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md)
- **Python SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md)

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#reporting-bugs)  Reporting bugs

If you encounter bugs or issues with the Agent SDK:

- **TypeScript SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-typescript/issues)
- **Python SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-python/issues)

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#branding-guidelines)  Branding guidelines

For partners integrating the Claude Agent SDK, use of Claude branding is optional. When referencing Claude in your product:**Allowed:**

- “Claude Agent” (preferred for dropdown menus)
- “Claude” (when within a menu already labeled “Agents”)
- ” Powered by Claude” (if you have an existing agent name)

**Not permitted:**

- “Claude Code” or “Claude Code Agent”
- Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code or any Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#license-and-terms)  License and terms

Use of the Claude Agent SDK is governed by [Anthropic’s Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), including when you use it to power products and services that you make available to your own customers and end users, except to the extent a specific component or dependency is covered by a different license as indicated in that component’s LICENSE file.

## [​](https://code.claude.com/docs/en/agent-sdk/overview\#next-steps)  Next steps

[**Quickstart** \\
\\
Build an agent that finds and fixes bugs in minutes](https://code.claude.com/docs/en/agent-sdk/quickstart)

[**Example agents** \\
\\
Email assistant, research agent, and more](https://github.com/anthropics/claude-agent-sdk-demos)

[**TypeScript SDK** \\
\\
Full TypeScript API reference and examples](https://code.claude.com/docs/en/agent-sdk/typescript)

[**Python SDK** \\
\\
Full Python API reference and examples](https://code.claude.com/docs/en/agent-sdk/python)

Was this page helpful?

YesNo

[Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

---
Metadata: {
  "twitter:description": "Build production AI agents with Claude Code as a library",
  "twitter:image": "https://claude-code.mintlify.app/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DAgent%2BSDK%26appearance%3Dsystem%26title%3DAgent%2BSDK%2Boverview%26description%3DBuild%2Bproduction%2BAI%2Bagents%2Bwith%2BClaude%2BCode%2Bas%2Ba%2Blibrary%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Flight.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D78fd01ff4f4340295a4f66e2ea54903c%26logoDark%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Fdark.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D1298a0c3b3a1da603b190d0de0e31712%26primaryColor%3D%25230E0E0E%26lightColor%3D%2523D4A27F%26darkColor%3D%25230E0E0E%26backgroundLight%3D%2523FDFDF7%26backgroundDark%3D%252309090B&w=1200&q=100",
  "generator": "Mintlify",
  "twitter:title": "Agent SDK overview - Claude Code Docs",
  "viewport": "width=device-width, initial-scale=1, viewport-fit=cover",
  "og:image": "https://claude-code.mintlify.app/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DAgent%2BSDK%26appearance%3Dsystem%26title%3DAgent%2BSDK%2Boverview%26description%3DBuild%2Bproduction%2BAI%2Bagents%2Bwith%2BClaude%2BCode%2Bas%2Ba%2Blibrary%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Flight.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D78fd01ff4f4340295a4f66e2ea54903c%26logoDark%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Fdark.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D1298a0c3b3a1da603b190d0de0e31712%26primaryColor%3D%25230E0E0E%26lightColor%3D%2523D4A27F%26darkColor%3D%25230E0E0E%26backgroundLight%3D%2523FDFDF7%26backgroundDark%3D%252309090B&w=1200&q=100",
  "ogTitle": "Agent SDK overview - Claude Code Docs",
  "apple-mobile-web-app-title": "Claude Code Docs",
  "og:type": "website",
  "canonical": "https://code.claude.com/docs/en/agent-sdk/overview",
  "language": "en",
  "twitter:card": "summary_large_image",
  "charset": "utf-8",
  "og:image:width": "1200",
  "ogImage": "https://claude-code.mintlify.app/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DAgent%2BSDK%26appearance%3Dsystem%26title%3DAgent%2BSDK%2Boverview%26description%3DBuild%2Bproduction%2BAI%2Bagents%2Bwith%2BClaude%2BCode%2Bas%2Ba%2Blibrary%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Flight.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D78fd01ff4f4340295a4f66e2ea54903c%26logoDark%3Dhttps%253A%252F%252Fmintcdn.com%252Fclaude-code%252Fc5r9_6tjPMzFdDDT%252Flogo%252Fdark.svg%253Ffit%253Dmax%2526auto%253Dformat%2526n%253Dc5r9_6tjPMzFdDDT%2526q%253D85%2526s%253D1298a0c3b3a1da603b190d0de0e31712%26primaryColor%3D%25230E0E0E%26lightColor%3D%2523D4A27F%26darkColor%3D%25230E0E0E%26backgroundLight%3D%2523FDFDF7%26backgroundDark%3D%252309090B&w=1200&q=100",
  "twitter:image:height": "630",
  "next-size-adjust": "",
  "twitter:image:width": "1200",
  "ogUrl": "https://code.claude.com/docs/en/agent-sdk/overview",
  "msapplication-TileColor": "#0E0E0E",
  "og:title": "Agent SDK overview - Claude Code Docs",
  "og:description": "Build production AI agents with Claude Code as a library",
  "ogDescription": "Build production AI agents with Claude Code as a library",
  "msapplication-config": "/docs/_mintlify/favicons/claude-code/pLsy-mRpNksna2sx/_generated/favicon/browserconfig.xml",
  "og:image:height": "630",
  "title": "Agent SDK overview - Claude Code Docs",
  "application-name": "Claude Code Docs",
  "og:site_name": "Claude Code Docs",
  "og:url": "https://code.claude.com/docs/en/agent-sdk/overview",
  "description": "Build production AI agents with Claude Code as a library",
  "favicon": "https://code.claude.com/docs/_mintlify/favicons/claude-code/pLsy-mRpNksna2sx/_generated/favicon/favicon-16x16.png",
  "scrapeId": "019e4fdd-7751-767f-a070-896176b2864e",
  "sourceURL": "https://code.claude.com/docs/en/agent-sdk/overview",
  "url": "https://code.claude.com/docs/en/agent-sdk/overview",
  "statusCode": 200,
  "contentType": "text/html; charset=utf-8",
  "proxyUsed": "basic",
  "cacheState": "hit",
  "cachedAt": "2026-05-22T13:04:38.224Z",
  "creditsUsed": 1,
  "concurrencyLimited": false
}
