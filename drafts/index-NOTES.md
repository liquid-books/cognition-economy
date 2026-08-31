# Notes — Appendix K Index + Copyright Page (drafts)

Files produced (originals untouched):

- `drafts/appendix-k-index.md` — complete index, replaces the scaffolded stub
- `drafts/fm-copyright.md` — new copyright page (no original existed; suggested position: immediately after the title page, before the foreword)
- `drafts/index-NOTES.md` — this file

## Design decisions

1. **Concepts own the entries.** Per the audit's index design, no product name has a locator of its own in the main alphabet. Products appear only as *see* cross-references pointing at the concept ("Antigravity, *see* agent-orchestration workspace") and in the single dated sub-index at the end, headed by the required line: "Names current as of this edition; the companion site (cognitioneconomy.net) tracks changes." This keeps the main index evergreen — when a product renames, only the dated sub-index and the companion site change.

2. **No page numbers.** This is a MyST/Jupyter Book build, so locators are chapter references ("ch 15", "fm", "appendix G") with "(case study)" appended where the locator is the chapter-ending case. First/primary locators for major frameworks are MyST links to the chapter labels that exist in the source (`#ch00`–`#ch16`, `#fm-two-mental-models`). I linked only the primary locator per entry to keep the index readable; secondary locators are plain text. Section-level labels exist for the split files (e.g. `ch15-1`) but those files are scaffolds — the real content lives in the chapter-level `chNN.md` files — so I anchored to chapter labels only. If the book is later split into per-section files, locators can be tightened without restructuring.

3. **Renamed/new frameworks indexed under their post-audit names.** Architect-and-builder pattern (not Opus-Plus-Sonnet), completion-condition loop (with "setting a finish line" as a subentry, not "/goal command"), control-vs-convenience spectrum (ch 8's replacement for the plugin/MCP/skill taxonomy), connection ladder and agentic browsing (ch 3's new sections, present in `drafts/ch03.md` per ch03-NOTES), programming by demonstration / skills-by-demonstration (ch 4's new subsection), three surfaces (the audit's replacement for the three-track blocks). Where the original chapter still uses the old name, the index points at the concept the drafts establish — the index is built against the *audited* book, not the pre-audit text.

4. **Five strands implemented:**
   - Frameworks and coined terms: indexed most densely, each with subentries (four moats gets all four moats plus collapse order; role vulnerability scorecard gets the six questions note + 0.65 threshold; all six engineering disciplines have their own headword entries via cross-reference from the "six engineering disciplines" hub).
   - Concepts and practices: skills carries the five required subentries (anatomy / by demonstration / by description / compounding library / open standard); sub-agents carries scout/planner/generalist, five dials, two-cost cross-ref; memory file, system prompt, meta-prompting, agent teams, hooks, channels, scheduled tasks, ZDR, least privilege, agentic browsing, tokens/context window/context engineering all present.
   - Cases: every fictional firm has a headword with protagonist(s) and the dilemma as a subentry. Non-Meridian firms: Coastal Regional Medical Center (ch 0), Cascade Strategy Partners (ch 9), Lumenax Health (ch 10), Cypress Coastal Insurance (ch 11), Astoria CloudWorks (ch 12), Bradford & Wynne LLP (ch 13), Halcyon Federal Credit Union (ch 14), Halverson Strathmore (ch 15), Calder Industries (ch 16). Fictional vendors CogniCare, ClaimsLogic AI, and RelayWorks are indexed under their case firms (CogniCare also as its own line since it spans the ch 0 comparison). Crestmoor Logistics (ch 13 in-body example, not a case study) indexed as "example firm."
   - Exercises and instruments: engineering brief template, 15-minute security briefing (with "fifteen-minute" as the alphabetized form and a Numbers-section cross-ref), weekly review, skim checklist, role scorecard — all present with their exercise locators.
   - Products-and-Tools dated sub-index: all thirteen required names plus Record a Skill and Claude Desktop, every one a cross-reference.

5. **Numbers section.** "0.65 threshold" and "15-minute" get a small Numbers section at the top (standard index practice) cross-referencing the spelled-out entries.

6. **Copyright page contents:** edition stamp exactly as specified ("Tool references current as of Fall 2026"), composite-case disclaimer (expanded slightly from the audit's one-liner to cover figures and dates, since the audit's Move 3 asks for exactly this in front matter), ISM 6427C (the audit says "Course number → copyright page" — this satisfies that front-matter fix), CC-BY-4.0 with the standard freedoms/obligations sentence, and the companion-site note with the cognitioneconomy.net/chNN-companion convention already used across the other drafts.

## Entry count

- Main headwords: 182 (including cross-reference-only headwords and the 17 dated sub-index lines)
- Subentries: 239
- Total indexable lines: ~420

The 250–350 target is met or exceeded depending on the counting convention: counting each headword and each subentry that introduces a distinct term (excluding pure locator-repeat subentries like "taste, ch 15"), the index lands near 320. If Dr. Lee wants it thinner, the easiest cuts are the quotation-style subentries (e.g., "steel rails," "a brilliant generalist is a bottleneck") — I kept them because the book's coinages are half its voice and readers will look them up verbatim.

## ⚠ Meridian flag (audit bug #5, extended)

The audit flags **three** fictional Meridians (ch 6 Capital Advisors / ch 7 Strategy Group / ch 8 Capital Group, all Atlanta, two CCOs surnamed Park). Building the case index surfaced the full extent: there are **nine distinct Meridian firms** across chapters 0–8:

| Ch | Firm | Location | Key people |
|----|------|----------|-----------|
| 0 | Meridian Health System | Fort Lauderdale FL | Dr. Sandra Okafor (CMIO) |
| 1 | Meridian Advisory Group | Atlanta GA | Dr. Camille Vance, Jordan Elias |
| 2 | Meridian Strategy Group (34 employees) | Atlanta GA | Diane Okafor, Marcus Trent |
| 3 | Meridian Health Partners | Fort Lauderdale FL | Diana Ruiz, James Okafor, Veronica Sánchez |
| 4 | Meridian Capital Partners | Miami FL | Rachel Osei |
| 5 | Meridian Wealth Partners | Charlotte NC | Sandra Reyes, Marcus Webb |
| 6 | Meridian Capital Advisors | Atlanta GA | Dana Whitfield, Marcus Reyes, Sandra Park (CCO) |
| 7 | Meridian Strategy Group (~340 consultants) | Atlanta GA | Renata Voss, Darius Okafor |
| 8 | Meridian Capital Group | Atlanta GA | Diana Forsythe, Rafael Mendez, Sylvia Park (CCO) |

Additional collisions worth the dedupe pass:
- **Two different Meridian Strategy Groups** (ch 2: boutique, 34 people; ch 7: mid-sized, 340 consultants) — same name, incompatible facts. Worst collision in the set.
- **Four Okafors** (ch 0 Sandra, ch 2 Diane, ch 3 James, ch 7 Darius), **two Parks as CCO** (ch 6 Sandra, ch 8 Sylvia), **three case-protagonist Reyeses** (ch 0 James at Coastal, ch 5 Sandra, ch 6 Marcus — plus ch 11 Daniel), **three named Priyas** (ch 4 associate, ch 9 Raman, ch 10 Shankar — plus ch 11 Priya Doshi), **two Marcus Reyes-adjacent Marcuses everywhere** (Trent, Webb, Reyes, Liang, Tellman, Holloway, Vance — seven Marcuses book-wide).
- Ch 10 names an AI teammate "Marc" in a book with seven human Marcuses.

Per the audit, the dedupe decision is Dr. Lee's; the index lists all Meridians **as written**, grouped under one "Meridian" headword with a publisher's-note line so a reader who notices the repetition sees it was deliberate at index level. If firms are renamed in the dedupe, only the Meridian block and the affected case-firm headwords need re-alphabetizing.

## Open questions for Dr. Lee

1. Should the index include the appendices (A–J) as locators? Currently only appendix G (two mental models) is referenced, because the other appendices are scaffolds with no content to index yet.
2. Copyright page: I wrote "© 2026 Dr. Ernesto Lee" — confirm the rights-holder line and whether a publisher imprint should appear.
3. The fm-NOTES draft flags the `cognitioneconomy.net/setup-companion` vs `cognitioneconomy.net/chNN-companion` slug question; the copyright page uses bare `cognitioneconomy.net` as the umbrella, which sidesteps it.
