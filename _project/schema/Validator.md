---
title: Validator
updated: 2026-11-20
status: to build in the pilot
---
# Validator

A script (~100 lines) run before commits.

**Errors**
- duplicate passage or note IDs
- a citation to a passage ID that doesn't exist (in the given edition)
- a quote that isn't an exact substring of its passage
- a `by: author` claim with no citation
- an argument that lists its own conclusion as a premise

**Warnings**
- unresolved forward references (allowed during extraction)
- a link whose file name doesn't match where the block now lives (auto-repairable)
