---
title: Current
updated: 2026-11-22
---
# Current

## Phase
**v0** (D-027): book → Markdown is **done (provisional)**; next is verification against the DOCX, then the reading website.

## In progress
- Nothing actively in progress. Last session ended after converting the whole book.

## Conversion status
- **Whole book converted** (pasted in chat, provisional): 17 files in `passages/ed1/` (Preface, Introduction, Chapters 1–15), **432 passage IDs, PFP-00001 to PFP-00432**, all unique and contiguous.
- Formatting items to check: [[Verify against DOCX]]. ⚠️ Highest priority: the missing Greek text of Rev 11:2 (Ch. 2), the truncated section 6 (Ch. 15), and the missing Isaiah 9:6 footnote (Intro).
- Content observations for the author: [[Content notes]] (repetition, possible internal differences, outdated chapter cross-references).

## Blocked / waiting
- **Manuscript .docx**: needed to verify the pasted text and freeze ed1. Josh will provide it next session.
- **P-002** (character normalization for search and quote matching): awaits Josh's decision.

## Next steps
- Next ID to assign: **PFP-00433**
- [x] ~~Settle P-001~~ → D-022.
- [x] ~~Convert the whole book to `passages/ed1/`~~ (provisional; pasted 2026-11-22).
- [ ] 1. Josh provides the manuscript .docx; put it in `source/`.
- [ ] 2. Verify every passage file against the DOCX with a script (text diff, ignoring formatting), then work through [[Verify against DOCX]]: missing text, merged lines, headings, lists, footnotes, italics/bold. Fix extraction errors; new blocks get new IDs (never renumber).
- [ ] 3. Freeze ed1: `editions/ed1.md` with the DOCX SHA-256; remove `status: provisional`; tag the commit `ed1`.
- [ ] 4. Decide P-002, then build the [[Validator]] (shared parser).
- [ ] 5. v0 website in `site/`: table of contents, chapter pages, per-passage anchors, footnotes, search, mobile-friendly. Confirm custom static site vs. Quartz first.
- [ ] 6. Share [[Content notes]] with the author.

### Deferred to v1
- Claims, arguments, objections, citation tests (D-024), the reader-path demo ([[Success test]]) and the mind map.

## Setup notes
- GitHub `JZtheStudent/revelation-prophecies` holds the full history (pushed 2026-11-22). Claude can push from the cloud. On the Mac, run `git pull` before editing so the vault picks up Claude's cloud commits.

## Open questions (not yet up for decision)
- Website: Claude recommends a custom static site with the shared parser over Quartz; confirm when we start `site/`.
- Hosting and public/private: deferred until v0 is done (D-028).
- Off-machine backup: none yet (Time Machine as stopgap).

## Last session
[[2026-11-22 Citation format]] (covers citation format, GitHub setup, v0 scope, and converting the whole book)
