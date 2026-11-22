---
title: Current
updated: 2026-11-22
---
# Current

## Phase
Stage 1 pilot setup: schema complete; ready to convert Preface + Introduction + Chapter 1 once the manuscript is in.

## In progress
- Nothing actively in progress.

## Blocked / waiting
- **Manuscript**: Josh to add the .docx to `source/`.

## Next steps
- [x] ~~1. Settle P-001~~ → decided as D-022 ([[Citations]]).
- [ ] 2. Josh adds the manuscript .docx to `source/`.
- [ ] 3. Freeze the edition: create `editions/ed1.md` with the SHA-256; tag the commit `ed1` ([[Editions]]).
- [ ] 4. Pass 1 (mechanical): Preface, Introduction, Chapter 1 → `passages/ed1/` files with `^PFP-#####` IDs; images to `assets/`; spot-check tables, figures, captions and footnotes against the DOCX.
- [ ] 5. Pass 2 (interpretive): claims, arguments and objections, in reading order; include one real historical-source citation if the material has one.
- [ ] 6. Build the [[Validator]] (shared citation parser, usable by the website export).
- [ ] 7. Citation tests (D-024), using fixtures in `_test/`:
  - [ ] same passage ID in a synthetic ed2 with different wording; both links open the intended text
  - [ ] an `@ed2` citation deliberately pointed at the ed1 file → validator catches it
  - [ ] move a cited block → repaired link still opens the correct edition
  - [ ] backlinks and passage links work in Obsidian
- [ ] 8. Demo one complete reader path on real content ([[Success test]]).
- [ ] 9. Evaluate the pilot. If Ch. 1 has no substantial multi-premise argument, add the first chapter that does.

## Open questions (not yet up for decision)
- Website: Quartz vs. custom, after the pilot.
- Off-machine backup: none yet (Time Machine as stopgap).

## Last session
[[2026-11-22 Citation format]]
