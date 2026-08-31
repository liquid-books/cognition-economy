# Chapter 14 Companion — Build Your AI Security Posture

**cognitioneconomy.net/ch14-companion · Last verified: Fall 2026**

> This page is the perishable half of Chapter 14's exercise and its ZDR section. The printed book gives you the decisions — choose your surface, run the interview, pull the DPA, find the three phrases, verify ZDR in writing. This page gives you the buttons and the dated vendor comparison. When a vendor changes its terms, this page changes and the book does not.

**Changelog**
- *Fall 2026:* Initial version. Vendor ZDR comparison verified against current DPAs at press time.
- *(future entries go here — three lines max, dated)*

---

## Which tools these tracks map to (Fall 2026)

| Printed surface | Current product (Fall 2026) | Notes |
|---|---|---|
| Track A — chat assistant | Claude (claude.ai / Claude Desktop) | Any major chat assistant works. Desktop download: claude.ai/download |
| Track B — terminal agent | Claude Code | Quickstart: code.claude.com/docs/en/quickstart (~10 minutes to a working session) |
| Track C — agent-orchestration workspace | Antigravity IDE, Agent Manager view | Overview: antigravity.google/docs/ide-overview |

---

## Track A — Chat Assistant

The printed steps are complete; nothing here is required. For reference:

- **Step 1 (open your chat assistant):** claude.ai in a browser, or Claude Desktop from claude.ai/download.

## Track B — Terminal Agent (Claude Code, Fall 2026)

### Printed step 1 — "Set the interview dial"

- Open Claude Code in your terminal and paste the structured prompt exactly as printed. No slash commands are needed — the interview runs as a plain conversation inside the session.

### Printed step 3 — "Turn the unanswerables into the action list"

- Current DPA locations for the three major frontier vendors (Fall 2026):
  - **Anthropic:** anthropic.com → Legal → Data Processing Addendum (commercial terms page).
  - **OpenAI:** openai.com → Policies → Data Processing Addendum (business terms).
  - **Google:** cloud.google.com → Terms → Cloud Data Processing Addendum (covers Gemini API/Vertex; the consumer Gemini apps sit under separate terms — check which surface your team actually uses).
  - Vendors move these pages; if a link 404s, search "*[vendor] data processing addendum*" and confirm you are reading the live version, not a cached PDF.

### Printed step 5 — "Save the artifact as a file"

- `ai-security-posture.md` in your project folder. Terminal-agent sessions can re-open and update it next quarter — ask *"re-run my security audit against ai-security-posture.md and flag what changed."*

## Track C — Agent-Orchestration Workspace (Antigravity IDE, Fall 2026)

### Printed step 1 — "Open the orchestration view"

- Open Antigravity IDE. Press **CMD+E** (Mac) or **CTRL+E** (Windows) to switch to the **Agent Manager** — the no-code orchestration view. Orientation: antigravity.google/docs/ide-overview.

### Printed step 2 — "Run the least-privilege audit first"

- In the Agent Manager, each **Project** shows its connected data sources in Project Settings → Data Access. Walk the project list and note any project whose sources exceed its current work. This screen is the concrete Fall 2026 instance of the book's Practice One.

### Printed step 3 — "Start the audit task, scoped deliberately"

- **New Task**, paste the Track B interview prompt, and set the task's project to one with minimal data access before running — the project selector is at the top of the New Task dialog.

### Printed step 4 — "Review the deliverables"

- Artifacts (drafts, comparison tables, the final one-pager) appear in the task's right-hand panel as the agent works; feedback typed into the task thread redirects the next revision.

---

## The dated ZDR comparison (Fall 2026)

The book deliberately prints no vendor table — only the six-question checklist. This is the dated comparison the checklist produces when run against the major frontier vendors in Fall 2026. **Run the checklist yourself against the live documents before relying on any row.**

| Checklist question | Anthropic | OpenAI | Google |
|---|---|---|---|
| ZDR available, which tier? | Enterprise/API via addendum | Enterprise/API via addendum | Vertex AI via configuration + addendum |
| Default, setting, or addendum? | Negotiated addendum | Negotiated addendum | Setting + addendum (varies by product surface) |
| "No training" also "no retention"? | Separate commitments — confirm both in your signed agreement | Separate commitments — confirm both | Separate commitments — confirm both, per surface |
| Default retention without ZDR? | Weeks-scale; named in the DPA — verify the current number | Weeks-scale; named in the DPA — verify | Varies by product surface — verify per surface |
| Subprocessors bound? | Current list linked from the DPA — confirm flow-down | Current list linked from the DPA — confirm flow-down | Current list linked from the CDPA — confirm flow-down |
| Written evidence for an auditor? | Contractual language + attestation on request | Contractual language + attestation on request | Contractual language + attestation on request |

**Cells above are deliberately conservative.** Every "verify" is real work: the numbers and mechanics changed more than once between this book's drafting and its press date, which is exactly why the printed edition carries the checklist and not the table. Consumer-tier training defaults have also flipped since drafting — never assume last year's answer.

**Hosted-agent caveat (cross-ref Chapter 11):** hosted agent offerings (e.g., Managed Agents, beta 2026) did **not** inherit ZDR or HIPAA eligibility at launch. If your deployment depends on either, confirm the hosted tier is in scope of your addendum before using it.

---

## Verification lab answers (Fall 2026 baseline)

For the printed "Is This Still True?" checks:

1. *Pull the current DPA* — links above; confirm the document date is newer than this page's "Last verified" stamp.
2. *Find the three phrases* — "will not be used to train models," "retention period," "subprocessors." All three vendors addressed all three phrases in their Fall 2026 DPAs; where the language is vague, that is your negotiation agenda, not a reading failure.
3. *Get ZDR in writing* — a sales email is not writing. The commitment must appear in the signed agreement or its addendum, by name.

Log your own dated answers — where they differ from this page, the vendor has moved past press time, and your log is the newer truth.
