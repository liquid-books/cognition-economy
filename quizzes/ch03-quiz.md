# Chapter 3 Quiz: Tools and the MCP Revolution

**Instructions:** Choose the best answer for each question.

---

## Question 1

What does MCP stand for, and who published the open standard?

A. Machine Command Protocol, published by OpenAI  
B. Model Context Protocol, published by Anthropic  
C. Managed Cloud Platform, published by Google  
D. Multi-Channel Pipeline, published by Microsoft  

---

## Question 2

The chapter uses an analogy to describe what MCP does for AI. Which analogy best captures it?

A. MCP is like giving your AI a new brain with more memory  
B. MCP is like USB — a standard connector so any tool following it works with any AI that supports it  
C. MCP is like a firewall that protects your data from the AI  
D. MCP is like a search engine that pre-loads results before you ask  

---

## Question 3

Before MCP existed, what was the main problem with connecting an AI to external tools?

A. AI models were not intelligent enough to use external data  
B. Every integration required custom code, API wrappers, and significant engineering effort  
C. External tools were too slow for real-time AI processing  
D. Privacy laws prevented AI from accessing any external data  

---

## Question 4

Which of the following best describes what an MCP server does from a practical standpoint?

A. It replaces Claude Desktop with a more capable AI model  
B. It stores your conversation history permanently in the cloud  
C. It runs alongside Claude Desktop, translating Claude's requests into calls to actual tools and returning results  
D. It encrypts all data before sending it to Anthropic's servers  

---

## Question 5

When you connect Google Workspace to Claude Desktop, which three services become accessible?

A. Google Photos, Google Maps, and Google Pay  
B. Gmail, Google Drive, and Google Calendar  
C. Google Docs, Google Sheets, and Google Slides  
D. YouTube, Google Search, and Google Translate  

---

## Question 6

Regarding Gmail permissions after connecting Google Workspace, which statement is accurate?

A. Claude can read, draft, and automatically send emails on your behalf without confirmation  
B. Claude can only read emails — it cannot create drafts or interact with Gmail in any other way  
C. Claude can read emails and create drafts, but cannot send — anything drafted must be sent manually by you  
D. Claude has no access to email content, only subject lines and sender names  

---

## Question 7

Firecrawl's free account provides 500 lifetime credits. According to the chapter, what does one credit roughly equal?

A. One keyword search across the entire web  
B. One page scrape — extracting the content of a single URL  
C. One hour of continuous web monitoring  
D. One AI-generated summary of a topic  

---

## Question 8

What is described as the highest-value use case for Firecrawl in a business context?

A. Downloading files from public file-sharing sites  
B. Translating foreign-language websites into English  
C. Competitive intelligence — reading competitor pages and synthesizing them into a brief  
D. Archiving your own website for backup purposes  

---

## Question 9

Why does Supabase matter specifically for AI workflows, according to the chapter?

A. It provides a faster AI model than Claude for number-crunching tasks  
B. It gives AI a persistent storage layer — data that survives between conversations, unlike Claude's context window  
C. It connects directly to social media platforms so AI can post updates automatically  
D. It replaces Google Drive as a document storage system  

---

## Question 10

What is the "universal pattern" for connecting any MCP server to Claude Desktop?

A. Download an installer, run it as administrator, restart your computer, and re-open Claude  
B. Find the tool's MCP documentation, copy the configuration snippet, open Claude Desktop and ask it to install the snippet, then follow Claude's guidance  
C. Write a Python script, host it on a server, generate an API key, and paste the key into Claude's settings  
D. Submit a request to Anthropic's support team, wait for approval, then receive a setup link by email  

---

## Answer Key

1. **B** — MCP stands for Model Context Protocol, and it was published as an open standard by Anthropic. It defines a common handshake so any compliant tool can plug into any supporting AI.

2. **B** — The chapter explicitly uses the USB analogy: before USB every peripheral had its own connector; after USB, anything following the standard worked together. MCP does the same for AI tools.

3. **B** — Before MCP, every external tool connection required custom code, API wrappers, and significant engineering effort — each integration was a one-off project. MCP standardizes the handshake.

4. **C** — An MCP server is a small piece of software running alongside Claude Desktop that translates Claude's requests into calls to the actual tool (Gmail, a database, a website) and returns the results back to Claude.

5. **B** — The Google Workspace connectors built into Claude Desktop give access to Gmail, Google Drive, and Google Calendar — the three services the chapter walks through in detail.

6. **C** — The chapter is explicit: Google's OAuth screen mentions email sending, but Claude only reads emails and creates drafts. Anything drafted must be sent manually. The inbox is read-only from Claude's perspective unless you approve a specific action.

7. **B** — One Firecrawl credit equals roughly one page scrape. The chapter notes that 500 deliberate scrapes — competitor pages, pricing pages, news articles — represents meaningful research capability at no cost.

8. **C** — The chapter calls competitive intelligence "the highest-value use case for most professionals" — reading competitor pricing, about pages, and blog posts, then synthesizing them into a competitive brief that would take hours manually.

9. **B** — Claude's context window clears between sessions and is not persistent storage. Supabase provides the persistent layer: a free cloud database that AI can read from, write to, and query in plain English, with data that survives indefinitely.

10. **B** — The universal four-step pattern is: find the tool's MCP documentation (search "[tool name] MCP Claude Desktop"), copy the configuration snippet, open Claude Desktop and say "Install this for me and walk me through it," then paste the snippet and follow Claude's guidance.
