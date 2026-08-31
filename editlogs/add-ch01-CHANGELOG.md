# Additions Changelog — Chapter 1 (ch01.md)

**Date:** 2026-08-31
**Spec:** ADDITIONS-SPEC-2026-08.md (Chapter 1 topics)
**Mode:** Additive only — no existing paragraphs, exercise steps, or case-study text edited. All new material inserted as new sections / `### Try It:` blocks.

## Insertions in `chapters/ch01.md`

1. **"When the Model Picks the Model: Routing"** — new section inserted in the model-roster material (after the Grok section, before "Open-Weight Models"). Covers routed flagship systems (ChatGPT's real-time router across fast/thinking/mini variants; Gemini and Claude defaults moving the same way), why providers route, and the two decisions routing does not make for you (provider choice; when to override).
   - **Activity:** `### Try It: Routed vs. Pinned — Same Prompt, Two Paths` — run one arithmetic-reasoning prompt on chatgpt.com under the routed default, then pin a specific reasoning model via the top-left model picker, compare thinking indicator/latency/answers; optional third run on a fast/mini model; Claude fallback path included. Deliverable: comparison table + two sentences.

2. **"When a Business Actually Chooses Open-Weight"** — new subsection appended inside the existing "Open-Weight Models" section (existing text untouched). Three decision drivers (data residency/compliance, cost at scale, offline/edge), the operational trade-off, and Ollama as the reference tool.
   - **Optional activity:** `### Try It (Optional): See Local AI Without Installing Anything` — observation-only walkthrough of ollama.com/Models (no installation), per spec. Deliverable: two sentences.

3. **"The Models You Cannot Have: Restricted Frontier Tiers"** — new short section after the open-weight material, before "Where to Compare Models Side by Side". Honest treatment of gated enterprise/government model tiers, pre-release evaluation by government AI-safety institutes, release timing as partly a regulatory event. No activity (per spec).

4. **"Beyond Text: Multimodal Work as a Daily Workflow"** — new full section inserted after the "Meeting the Models" section's closing Try This, before "Tokens". Table mapping PDF/image/video/voice inputs to the workflows they replace; product-support notes (Gemini native video/audio); "extraction is reading, not measuring" caveat; The Multimodal Reflex admonition.
   - **Activity:** `### Try It: Extract Tables from a PDF and a Chart Photo — Then Verify by Hand` — Part A: upload a PDF (Berkshire letter fallback) to claude.ai via paperclip/+ and extract the main table; Part B: photograph a chart, upload (desktop or Claude mobile app camera), extract values with ~ estimate marks; Part C: mandatory hand-verification of one number from each. Deliverable: both tables + three-sentence note.
   - New figure referenced: `../images/ch01-multimodal-infographic.png`.

5. **"Past the Meter: Caching, Schemas, and Token Budgets"** — new full section inserted after "The Token Economy" section's closing Try This, before "Context: The Working Memory of the AI". Subsections: Prompt Caching (mechanics, ~10× cheaper cached reads, why Projects/Gems economics depend on it, cache-friendly = stable prefix), Structured Output (JSON schema as contract; forcing commitment), Token Budgeting (four budgets: output, context, model tier, reasoning effort) + One-Line Budget Habit admonition.
   - **Activity:** `### Try It: Schema vs. Freeform — Same Analysis, Two Shapes` — same document analyzed twice on claude.ai (fresh chats), free-form vs. explicit JSON schema; compare scanability/commitment/reusability; optional paste-into-spreadsheet step. Deliverable: both outputs + three sentences.

6. **"Hallucination and the Verification Discipline"** — new full named section inserted after "Context Rot" section's closing Try This, before "Voice Changes Everything". Covers: why models fabricate (compression not database; training rewarded answering; the dark-room gap), where risk concentrates (specific checkable claims vs. reasoning over supplied context), and the three verification habits — citation checking (Google Scholar; "a citation you have not opened is a hypothesis"), confidence probing (exact self-audit prompt; fresh-chat stability probe), and the Verify-Before-Forward Rule (warning admonition).
   - **Activity:** `### Try It: Elicit a Hallucination, Then Audit It` — deliberately elicit citations on an obscure topic (exact prompt + recipe for substituting your own field), disable web-search toggle, audit all five citations on scholar.google.com, log REAL/FABRICATED/DISTORTED, then run the confidence probe and compare against the audit; re-run-narrower fallback if everything checks out. Deliverable: five-row audit table + three-sentence reflection.
   - New figure referenced: `../images/ch01-hallucination-infographic.png`.

7. **`<!-- NEW IMAGES NEEDED -->` comment** appended at end of ch01.md describing the two new infographics (multimodal, hallucination/verification).

## Cross-references added in subfiles (one `:::{seealso}` block each, appended at end; no content duplicated)

- `chapters/ch01-3-meeting-the-models.md` → points to routing, multimodal, open-weight decision drivers, restricted tiers in full Chapter 1.
- `chapters/ch01-5-token-economy.md` → points to caching/structured-output/token-budgeting section.
- `chapters/ch01-9-context-rot.md` → points to Hallucination and the Verification Discipline section.

## Not changed

- All existing ch01.md sections, admonitions, figures, case study, discussion guidelines, and the six-step Applied Exercise: byte-identical except for the insertions above.
- Quizzes / case-studies / canvas-pages: untouched (existing ones remain valid; new sections have in-place activities).
