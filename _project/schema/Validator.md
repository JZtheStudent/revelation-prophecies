---
title: Validator
updated: 2026-11-22
status: to build in the pilot
---
# Validator

A script run before commits. It shares its citation parser with the website export (see [[Citations]]).

**Errors**
- duplicate passage IDs within one edition, or duplicate note IDs
- a malformed `## Cites` line (reported with note path + line number)
- a citation whose passage ID doesn't exist in the given edition
- a citation whose link folder doesn't match its edition marker (e.g. `@ed2` pointing into `passages/ed1/`)
- a quote that doesn't match the passage's plain text (whitespace-normalized; wording, punctuation and case exact)
- a `by: author` claim with no citation
- an argument that lists its own conclusion as a premise

**Warnings**
- unresolved forward references (allowed during extraction)
- a link whose file path doesn't match where the block now lives in that edition (auto-repairable using edition + ID)
