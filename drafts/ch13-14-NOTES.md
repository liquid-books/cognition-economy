# Chapters 13–14 Revision Notes — drafts/ (August 2026 audit pass)

Scope: `chapters/ch13.md`, `chapters/ch14.md`, plus the eight numbered subfiles (all empty scaffolds — see bottom). Originals untouched. Companion URL convention: `drlee.io/ch13`, `drlee.io/ch14`.

---

## ch13.md — what changed

### Channels enumeration replaced (highest-rot line)
- "The currently supported channels in the research preview are Telegram, Discord, and iMessage" → audit's replacement text verbatim: "The first channels to ship were consumer messaging apps; the set grows with every release, and which ones your tool supports today is a companion-page question, not a book question. The model is what matters."
- Added present-tense Slack-style team-channels sentence ("Team channels in particular are now a first-class surface… an agent can post into the channel your team already reads — and be addressed there by name").
- "Claude Code calls this concept…" → "Agent tools call this concept…". The iMessage two-way example de-branded ("A phone-messaging channel lets you text your AI…"). "a partner reads only their iPhone Messages" → "the messages app on their phone."
- "For the first two years of consumer AI" → "In the first years of consumer AI."

### Hook events → evergreen lifecycle phrasing
- "Claude Code documents over twenty different hook events… [current list]" → audit's phrasing: "Agent tools expose dozens of lifecycle moments you can attach a rule to — when a session starts, before or after a tool runs, when the AI needs your input, when a sub-agent finishes, when a file changes. The catalogue grows with every release; the shape is always 'when this happens, also do this.'" (Dropped "when a notification is sent" and "when the working directory changes" from the enumerated list — release-specific.)

### Track B wrong-primitive bug FIXED (audit bug 10)
- Old Track B had the reader ask Claude Code for "a hook configuration that fires this briefing at the scheduled time" — a time trigger is a scheduled task by the chapter's own taxonomy. The collapsed exercise (see below) now frames the automated version as "a **scheduled-task configuration plus a delivery channel**," with a hook reserved for the event example: "notify me when the briefing has been delivered." This framing lives in the "Three Surfaces, One Exercise" admonition and in Part 2 step 5 ("That alarm IS your schedule — a scheduled task with you as the delivery mechanism").

### Briefing time standardized to 8:00 AM (audit bug 10, second half)
- All occurrences unified: worked example ("Every weekday at 8:00 AM… By 8:15"), Northwind case (7:30 → 8:00), Crestmoor case (6:00 → 8:00), automation-stack recap ("The 8:00 AM briefing"), exercise spec + phone alarm. Non-briefing times (4:00 PM Friday review, fifteen-minutes-before-meeting) left as-is. The "8 AM Briefing Pattern" admonition title now matches its own advice.

### 1980/2024 factory analogy → relative time (Move 3)
- "a factory floor in 1980" → "a factory floor forty years ago"; "the same factory in 2024" → "the same factory today"; "1980 mode" → "old-factory mode"; "the 2024 factory" → "the modern factory."

### Unsourced consulting study → illustration
- "A 2025 internal study by a global consulting firm tracked…" → "Picture the internal usage data at a large consulting firm that tracks…" (present-tense hypothetical). Invented precision removed: 4.1 hrs → "a few hours"; 6.8 hrs → "somewhat more"; 61% → "well over half." Paragraph's argumentative shape (top quartile's AI work is push-not-pull) preserved. Verb tenses in the two follow-on paragraphs shifted to match the hypothetical framing.

### "Arvin Ash" dropped
- "Here is the analogy Arvin Ash might use" → "Here is an analogy worth holding onto."

### Native scheduled tasks in the agentic workspace
- New short paragraph at top of Scheduled Tasks section: "This pattern used to require an engineer and a server. It no longer does. The agentic workspace you configured back in Chapter 2 runs scheduled tasks natively — you describe the schedule and the work in plain English, and no terminal is involved." (No product name — consistent with ch02 draft's teach-the-shape approach.)
- "The tools you already use — Claude Code, the Antigravity 2.0 IDE, the major workflow platforms —" → "the chat assistant, the terminal agent, the agentic workspace, the major workflow platforms."

### Case study date/number scrub (Move 3)
- "Founded in 1983" → "Now in its fifth decade" (preserves the ~40-year-old-firm fact relatively).
- "fiscal year 2024 reached $42.6 million" → "the firm's most recent fiscal year reached the low forties of millions" (per audit).
- "Director of Operations since 2019" → "Director of Operations" (date dropped).
- "In January 2025, Ostrowski launched" → "Eighteen months into that modernization effort, Ostrowski launched" (sequence, not calendar).
- All other case content (metrics like 42 minutes/14 inquiries/one-in-eight, the team, the debate, the Discussion Prompt, Discussion Guidelines) preserved verbatim.

### Tracks collapsed (Move 1, drlee.io/ch13)
- "Choose Your Track" admonition + Tracks A/B/C + all code.claude.com and antigravity.google URLs + CMD+E + Agent Manager mechanics deleted. Replaced with "Three Surfaces, One Exercise" admonition (three surface types + companion pointer + the corrected scheduled-task-plus-channel framing + the hook event example), matching the pattern established in drafts/ch02.md.
- Exercise restructured as Part 1 (write the spec — kept old Track B step 1's concrete guidance) + Part 2 (the former Track A manual version, de-branded). Old Track A step 5's confused "difference between Track C and Tracks A and B" line rewritten as the manual/automated contrast without track letters.
- Reflection rewritten for single-path (was: "how the two tools handled the same specification" — reader only used one). New reflection keeps the contract-vs-delegation question and adds a trigger–work–channel spotting question.
- Track B/C submission blocks removed; Track A submission block kept as the single submission.

### Optional exercise variant added (Ch 3 connection ladder)
- New admonition "Optional Variant: The Desktop-Bound Task": desktop app no connector reaches → Chapter 3's connection ladder, last rung (computer use), with human-approval gate while the tool earns trust.

### Leave-alone items preserved verbatim
- Reactive vs. proactive framing; "you are the customer of the output"; trigger/work/channel decomposition; "Hooks are the steel rails. AI is the train"; regulator test; "the right channel is the one that gets read" (Sapient Bio story intact); "the schedule is the discipline" paragraph; automation stack as a department; Compose-Don't-Centralize; full Bradford & Wynne walkthrough and guardrails section; Renee Ostrowski opening; all admonitions except the track chooser; closing italic paragraph.

---

## ch14.md — what changed (LEGAL/TRUST-SENSITIVE ITEMS)

### Opening vignette rewritten (the unknowable-outcome assertion)
- "Under the terms of the firm's consumer-tier ChatGPT usage, that data became part of the training corpus. It is now, in effect, in the model." → audit's exact replacement: "Under the consumer terms nobody at the firm had read, that data left the firm's control the moment it was pasted — with no data-processing agreement, no retention commitment, and no contractual mechanism to get it back. Whether or how the vendor used it is, from the auditor's chair, beside the point: the firm cannot say, and cannot prove otherwise."
- "the free consumer version of ChatGPT" → "the free tier of a popular chatbot" (vignette + the later "would have pasted the portfolio data into ChatGPT" → "into a consumer chat tool").
- Crowder callback paragraph in Data Usage updated to match: "On the consumer tier, that data fed the model" → "the firm had no agreement, no retention commitment, and no way to prove what happened to the data."

### Halcyon case — same reframe
- "that information was now in a consumer vendor's training corpus, with no contractual mechanism for retrieval or deletion" → "under the consumer terms, that information had left the firm's control the moment it was pasted — with no data-processing agreement, no retention commitment, and no contractual mechanism for retrieval or deletion. Whether or how the vendor used it was, from the audit committee's chair, beside the point: the firm could not say, and could not prove otherwise."
- "a free, consumer-tier AI tool" → "the free tier of a popular consumer AI tool."
- Date/number scrub: "$3.1-billion… thirty-one branches… approximately 410,000 members" → "$3-billion… about thirty branches… roughly four hundred thousand members" (per Move 3's exact example). "joined the firm in 2021 after eleven years" → "joined the firm after eleven years." "In the spring of 2024" → "Early in the firm's AI adoption." Everything else in the case (near-miss framing, three board questions, thirty-day deadline — a deadline, not a retention window) preserved.

### ZDR section restructured
- **Promoted to lead:** "The detail to internalize in this section is not any specific vendor's offering — those will evolve. The detail to internalize is that Zero Data Retention is a thing you can ask for, by name…" now opens the section (was buried after the table).
- **Vendor table DELETED**, replaced with the six-row vendor-neutral checklist per the audit (availability/tier; default-setting-or-addendum; no-training vs. no-retention; default retention window; subprocessors bound; written evidence for an auditor), formatted as a two-column list-table (question / what a good answer looks like).
- **Added verbatim:** "As of this writing every major frontier vendor has a path to ZDR for enterprise customers; the mechanics differ and change often. The companion page at drlee.io/ch14 keeps a dated comparison." (Note: audit Move 6 says cut "as of this writing" hedges, but the Ch 14 section mandates this exact sentence — mandate wins.)
- "The three major frontier vendors all offer ZDR as a contractual option… though the specifics differ in ways that matter" → deleted (superseded by the sentence above).
- "commonly thirty days" → "typically measured in weeks, not hours, long enough that a regulator will ask about it." Downstream "even thirty days of retention" → "even a few weeks of retention"; "for thirty days" → "for weeks."
- **Verify sidebar added** ("Is This Still True?", end of ZDR section): pull the current DPA; find the three phrases; get ZDR in writing; companion pointer.
- Figure `ch14-zdr-comparison.png` reference kept but caption/alt rewritten to describe a six-row checklist rather than a three-vendor comparison → **FIGURES-TODO** below.

### Four Questions section
- "Thirty days?" in question 2 → "Weeks?" (consistency with the retention reframe).
- "In 2024 alone, multiple Fortune 500 firms…" → "Multiple Fortune 500 firms have quietly issued…" (date-scrubbed).
- **Samsung 2023 sentence kept dated and real** per audit; citation placeholder added: `[CITATION NEEDED: contemporaneous reporting on Samsung's 2023 ChatGPT restriction, e.g., Bloomberg, May 2023]`.
- Added the one evergreen regulatory sentence at the end of that paragraph: "release schedules have entered the regulatory conversation, with supervisors in several industries now asking not just what tools a firm uses but how it evaluates each new version before turning it on."

### Least-privilege section additions (Practice One)
- **Browser-agent permission ladder** added as a durable example: approve-each-action → standing trust for a specific site → autonomous within hard vendor safeguards; "match the rung to the stakes… default to the lowest rung that gets the work done." No product names (cross-consistent with drafts/ch03-12-browser.md).
- **Per-app consent / screenshot caution:** "grant access per application, not to the whole desktop… screenshots capture everything visible — close the sensitive windows before you start."
- **Hosted-agent convenience-vs-compliance note** (cross-ref Ch 11): "Before you assume a hosted option inherits your ZDR or regulated-industry commitments, check; at launch, hosted tiers often do not."

### Data Usage section
- Added one sentence acknowledging consumer opt-outs / shifting defaults (supports the vignette reframe and the audit's landscape note that consumer training defaults have flipped): "Some vendors let consumers opt out; the defaults shift between releases; and the setting your team is actually running under, right now, is something you almost certainly do not know."

### Cultural layer
- "in the last three years" → "in recent years"; Pearlman & Strauss "ran exactly this briefing in early 2024" → "ran exactly this briefing" (the near-miss context carries the sequence).

### Exercise bugs fixed (audit bug 11) + tracks collapsed (Move 1, drlee.io/ch14)
The three bugs:
1. Track A said "the same artifacts Tracks A and B produce" (meant B and C) — moot after collapse; the "Three Surfaces" admonition now says all three surfaces produce the same three artifacts.
2. Track A's steps produced two artifacts (risks + briefing) while its submission demanded three — fixed: step 3 now explicitly requests all three artifacts (approved-tools list with four questions, ranked risk gaps, fifteen-minute briefing), matching the submission block.
3. Track C referenced "the same structured prompt from Track A's step 1" (the structured prompt lived in Track B) — moot after collapse.
- Tracks A/B/C, the Choose Your Track admonition, code.claude.com quickstart URLs, antigravity.google URL, CMD+E, and Agent Manager mechanics removed. Replaced with "Three Surfaces, One Exercise" admonition; Track C's genuinely useful step 2 (auditing project data-permission scopes as a least-privilege exercise) preserved as a companion-page teaser inside the admonition ("including how to scope the task to a project with appropriate data permissions, itself a useful least-privilege audit").
- Single exercise merges Track A's conversational flow with Track B's stronger steps (the "cannot answer → vendor action list" step, now pointed at pulling the current DPA; the "edit the briefing for your firm's voice" step). Submission = former Track A submission (now consistent at three artifacts). Reflection kept verbatim (already track-agnostic).

### Leave-alone items preserved verbatim
- New-hire analogy; four questions framework; "you have a guess, not a posture"; consumer-vs-enterprise same-model-different-contract core; Free Tool Trap; screenshot test; approved-tools list; ZDR as concept + "ask for it by name" (closing "Ask for it. Get it in writing. Move on."); three SLA phrases admonition; four operational practices (additions appended to Practice One only); cultural layer + five-point briefing; trust compound section; Halcyon tension and discussion prompt; Wellfront story; Discussion Guidelines; closing italic paragraph.

---

## Scaffold subfiles (ch13-1 … ch14-4)
All eight numbered subfiles are empty scaffolds ("Chapter coming soon"). Titles and descriptions checked for perishables — **all clean and evergreen** (e.g., "The doorbell," "The alarm clock for your AI," "The Mission Impossible message," "Race cars have roll cages to go faster"). Copied to drafts/ unchanged.

---

## Flags / ambiguities
- **Move-6 vs. Ch-14 mandate:** the audit's book-wide move says cut "as of this writing," but the Ch 14 section mandates a sentence beginning with it. Kept the mandated sentence exactly; no other hedges introduced.
- **"90/10 Rule" figures:** the 90/10 admonition's numbers are rhetorical, not sourced-claim-shaped; audit is silent → preserved.
- **Sapient Bio / Northwind / Crestmoor / Lattice / Wellfront / Pearlman:** invented illustrative firms with no calendar dates; specific-but-plausible numbers (94% adoption, 340 records, ninety-two clinics) preserved — they read as composite-case texture, covered by the front-matter composite disclaimer (fm draft).
- **Meridian dedupe (audit bug 5):** no Meridian appears in ch13/ch14 — nothing to flag.
- **Samsung citation:** placeholder inserted; needs a real reference entry (Bloomberg, May 2023, "Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak" or equivalent) at final pass.
- **ch14 exercise structured prompt:** the collapsed exercise absorbs Track B's interview-style prompt as a direct three-artifact request (step 3). If Dr. Lee prefers the one-question-at-a-time interview flow in print, it can be restored verbatim — both were in the original.

## FIGURES-TODO
- **ch14-zdr-comparison.png (REQUIRED):** current image is a three-vendor (Anthropic/OpenAI/Google) ZDR comparison — several cells inaccurate and all perishable. Regenerate as the six-row vendor-neutral **ZDR Checklist** (availability/tier · default-setting-or-addendum · no-training≠no-retention · default retention window · subprocessors bound · written evidence). Draft caption/alt already describe the checklist version.
- **ch13-channels.png (OPTIONAL):** image alt text bakes in "Slack, email, Discord, iMessage, Telegram" — channel names in the art will date. If regenerated, use generic surfaces (team chat, email, phone messages, dashboard). Not required by the audit; body text no longer depends on the named set.
- **ch13-infographic.png (OK):** "delivered to Slack, email, and calendar" — Slack survives in body text as a present-tense example; no change needed.

---

## Retrofit pass (per HANDS-ON-STRATEGY, August 2026)

Second pass on `drafts/ch13.md` and `drafts/ch14.md` only. Reason: HANDS-ON-STRATEGY found the COLLAPSE pattern (applied in the first pass above) cost ch13 its automation build entirely — "the chapter titled 'Make Your AI Work While You Sleep' no longer has the student make anything work while they sleep" — and standardized the book on the **DIAL pattern** (ch09/ch10 as exemplars): full three-track structure in print, de-branded, each step named for the evergreen decision it sets, only literal click-paths/menu names/config syntax on the companion page. Originals in `chapters/` untouched.

### ch13.md — Tracks B/C restored, DIAL-style

- **Structure now:** shared Part 1 (write the specification — unchanged) → Track A (the former manual version, unchanged content, now labeled as a track with its submission block) → Track B (terminal agent, scheduled task) → Track C (orchestration workspace, recurring background task) → optional computer-use variant (moved after Track C) → reflection → NEW verification lab.
- **Track chooser admonition** retitled "One Exercise, Three Surfaces" to match ch09/ch10 phrasing ("You only need to complete one track…"); retains the first pass's corrected framing verbatim: automated path = **scheduled-task configuration plus a delivery channel**, hook reserved for the event example ("notify me when the briefing has been delivered").
- **Track B rebuilt from the original — with the wrong-primitive bug NOT regressed.** Original Track B asked Claude Code for "a hook configuration that fires this briefing at the scheduled time" (audit bug 10). Restored track instead has the student *speak the delegation*: "Every weekday at 8:00 AM, assemble my briefing from the specification I am about to paste, and deliver it to [the channel where you actually read things]. Confirm what you've scheduled and show me how to inspect or cancel it." (Per HANDS-ON-STRATEGY §3.3 item 1, near-verbatim.) Step names = decisions: trigger dial (schedule-not-event, with an explicit "notice what you did NOT ask for: a hook" teaching beat), channel dial (the place that gets read; original's Telegram/iMessage/Slack channel-doc step → in-session "which channels can you reach today?" question + companion pointer), read-back-the-contract (Ch 6 cross-ref, from original's "read it, ask to adjust" step), add-the-hook (the event-driven notify step — the two primitives contrasted back to back), let-it-fire-once (`briefing-spec.md` artifact kept from original step 5; plus the HANDS-ON-STRATEGY fallback: "if your tool can't schedule tasks yet, that's a logged verification answer"). The printed track now has the student SET UP a working automation and wake up to a briefing they did not ask for that morning — the chapter's restored promise.
- **Track C rebuilt from the original**, de-branded (Antigravity/CMD+E/Agent Manager → "orchestration view"/"manager view," click-path to companion). Original's 7:00 AM recurrence sentence → **8:00 AM** (kept the first pass's standardization; original Track C was one of the four inconsistent times). Steps named for decisions: open the view, set the recurrence decision (trigger/work/channel identified inside one task description), watch the first run, review as the customer of the output (chapter's own phrase), save as recurring. "Artifacts" (branded noun) → "structured deliverables"/"deliverable."
- **Submissions:** Track A block unchanged; Track B and C submission blocks restored from the originals, lightly de-branded ("first briefing it delivered without you asking" / "first deliverable"; "Artifact" → "deliverable"). Track B keeps the original's one-sentence pull-vs-push question.
- **Reflection** extended for multi-track: keeps the first pass's contract-vs-delegation + trigger–work–channel questions, adds "if you ran Track B or C: what changed in you when the first briefing arrived without being asked for?" Single-track-safe (each question gated).
- **NEW "Is this still true?" verification lab** — HANDS-ON-STRATEGY flagged ch13 as the most tool-heavy chapter in the book with no verify sidebar (Move 5 gap) and specified this lab as mandatory: (1) can it schedule + how to inspect/cancel, (2) which delivery channels today, (3) where scheduled tasks live (chat assistant vs terminal agent). Active checks, dated log, appended to submission, companion pointer last.
- **Not regressed:** 8:00 AM everywhere; scheduled-task-not-hook framing; all first-pass body edits (channels line, lifecycle phrasing, factory relative time, illustration reframe, case scrub) untouched; optional computer-use variant kept.

### ch14.md — Tracks B/C restored, DIAL-style, three exercise-bug fixes carried over

- **Structure now:** "One Exercise, Three Surfaces" chooser (ch09/ch10 phrasing) → Track A (the first pass's merged single exercise, verbatim, relabeled) → Track B (terminal agent) → Track C (orchestration workspace) → reflection (unchanged — already track-agnostic).
- **Bug fixes carried over, not regressed:**
  1. *Track-letter references:* chooser admonition states "all three tracks produce the same three artifacts" — no track refers to another track's letter for its artifact list. Track C's prompt reference now correctly points at **Track B, step 1** (original said "Track A's step 1" while the prompt lived in Track B).
  2. *Three-artifacts mismatch:* Track A step 3 (from the first pass) requests all three artifacts explicitly; the restored Track B prompt was reordered to name them in the same order and count (tools list / ranked gaps / briefing); all three submission blocks demand exactly the three artifacts their steps produce.
  3. *Track C dependency:* Track C step 3 explicitly says "the structured interview prompt printed in Track B, step 1" — the printed dependency now names the right track and the prompt actually exists there.
- **Track B rebuilt from the original**, steps named for decisions: interview dial (one-question-at-a-time — with the *why*: an interview surfaces what you'd forget to volunteer), answer honestly, unanswerables→action list (upgraded from the original's vague "contact the vendors" to the chapter's verify-sidebar actions: **pull the DPA, find the three phrases, get ZDR in writing** — vendor-neutral, decision-based), edit for your firm's voice, save as a file (`ai-security-posture.md` kept; framed as the file-you-own advantage of the surface). Original Track B submission (three artifacts + 30-day personal action plan) restored verbatim in substance.
- **Track C rebuilt from the original**, de-branded. The genuinely distinct pedagogy — original step 2's project-permission review — restored in print as "run the least-privilege audit first" and tied explicitly to Practice One ("observed live in your own tooling"); the first pass had reduced it to a teaser clause in the admonition, now removed from the admonition since it is a printed step again. Step 3 frames scope selection as the exercise ("applying least privilege to the audit of your least-privilege posture"). Original Track C submission (three artifacts + 100–150-word honest-posture paragraph) restored.
- **Not regressed:** ZDR checklist framing, promoted lead sentence, "Is This Still True?" DPA sidebar, vignette/Halcyon reframes, retention-window phrasing, least-privilege additions — all first-pass body work untouched. Reflection kept verbatim.

### companion/ pages created (the perishable layer)

- New `companion/ch13-companion.md` and `companion/ch14-companion.md` (companion/ dir created). Header "Last verified: Fall 2026" + 3-line changelog stub, per HANDS-ON-STRATEGY §3.5. Organized **per printed exercise step**, so instructor and student can say "step 2 on your sheet."
- ch13 page: surface→product mapping table (Claude/Claude Code/Antigravity/Claude Cowork), Claude Code scheduled-task inspect/cancel syntax, Fall 2026 channel list (Slack-style, email, Telegram, Discord, iMessage) with the in-session question flagged as authoritative, the why-not-a-hook explanation, CMD+E/CTRL+E + Agent Manager click-paths, Artifacts panel, computer-use preview caveats, and baseline answers for the new verification lab.
- ch14 page: same mapping table, Fall 2026 DPA locations for the three majors, Antigravity Project Settings→Data Access path, and the **dated ZDR comparison table** the printed checklist deliberately does not contain (conservative cells, every row marked verify; consumer-default-flip warning; Managed Agents not-ZDR/HIPAA-at-launch caveat cross-ref'd to Ch 11), plus baseline answers for the printed verify sidebar.
- Doc URLs from the originals (code.claude.com quickstart, antigravity.google/docs/ide-overview) live only on these pages, per audit bug 13.

### Flags

- **Submission-block instruction "append your verification log" (HANDS-ON-STRATEGY §3.2):** the new ch13 lab tells students to append dated answers to their submission; the three per-track submission blocks were not each amended to repeat it (kept blocks aligned with ch09/ch10 exemplars, which also carry the instruction only in the lab). If Dr. Lee wants it inside every submission block book-wide, that is a one-line global pass.
- **ch14 has no NEW verification lab** — it already had one from the first pass (the DPA/three-phrases/ZDR sidebar), which HANDS-ON-STRATEGY rated adequate; left as-is.
- **Companion ZDR table cells are placeholders shaped as conservative truths** ("weeks-scale — verify"). Before the page goes live, someone must run the six checks against the actual Fall 2026 DPAs and harden the cells — the page says so, but flagging here too.
- No FIGURES-TODO changes from this pass (first-pass list stands).
