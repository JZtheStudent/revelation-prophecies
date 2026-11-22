---
title: Current
updated: 2026-11-22
---
# Current

## Phase
**v0** (D-027): convert the whole book into `passages/ed1/` Markdown with permanent passage IDs, then a reading website with good UX (every passage a linkable anchor). Audience: family (D-028). Claims/arguments/mind map = v1.

## In progress
- Nothing actively in progress.

## Blocked / waiting
- **GitHub access**: Josh links his GitHub account to Claude (claude.ai Settings → Connectors) so Claude can work in `MaterraX/revelation-prophecies` from the cloud.
- **First push**: Josh runs `git push -u origin main` once from the vault folder in Terminal (remote `origin` is already set).
- **Manuscript**: Josh adds the .docx to `source/`, possibly chapter by chapter (D-029).

## Next steps
- [x] ~~1. Settle P-001~~ → decided as D-022 ([[Citations]]).
- [ ] 2. Josh adds the manuscript .docx (or its first chapters) to `source/`.
- [ ] 3. Freeze the edition: create `editions/ed1.md` with the SHA-256; tag the commit `ed1` ([[Editions]]).
- [ ] 4. Pass 1 (mechanical): Preface, Introduction, Chapter 1 → `passages/ed1/` files with `^PFP-#####` IDs; images to `assets/`; spot-check tables, figures, captions and footnotes against the DOCX.
- [ ] 5. Pass 2 (interpretive): claims, arguments and objections, in reading order; include one real historical-source citation if the material has one.
- [ ] 6. Build the [[Validator]] (shared citation parser, usable by the website export).
- [ ] 7. Citation tests (D-024), using fixtures in `_test/`:
  - [ ] same passage ID in a synthetic ed2 with different wording; both links open the intended text
  - [ ] an `@ed2` citation deliberately pointed at the ed1 file → validator catches it
  - [ ] move a cited block → repaired link still opens the correct edition
  - [ ] backlinks and passage links work in Obsidian
- [ ] 8. v0 website: a static site in `site/` using the shared parser. Table of contents, chapter pages, per-passage anchors, footnotes, search, mobile-friendly.
- [ ] 9. Continue converting the remaining chapters in reading order.

### Deferred to v1
- Pass 2 (claims, arguments, objections), the reader-path demo ([[Success test]]) and the mind map. Steps 5 and 7 above can wait for v1 if v0 needs the time.

## Open questions (not yet up for decision)
- Website: Claude recommends a custom static site with the shared parser over Quartz; confirm when we start `site/`.
- Hosting and public/private: deferred until v0 is done (D-028).
- Off-machine backup: none yet (Time Machine as stopgap).

## Last session
[[2026-11-22 Citation format]]
