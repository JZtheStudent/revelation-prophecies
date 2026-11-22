---
title: Editions
updated: 2026-11-22
---
# Editions

## Freezing
The pilot freezes **ed1**: `editions/ed1.md` records the source and its hash, its text lives in `passages/ed1/`, and the git commit is tagged `ed1`. A citation with no edition marker means ed1.

```yaml
edition: ed1
source_file: source/<name>.docx
sha256: <hash>
frozen: 2026-MM-DD
```

## Revision rules (not built yet)
Each frozen edition gets its own folder (`passages/ed2/`, ...), so every edition's wording stays openable in Obsidian side by side. Earlier editions are never edited.
- **Revised passage:** keeps its ID; the new wording lives in the new edition's folder, the old wording stays in the old one.
- **Split passage:** original ID stays on the first part; the rest gets a new ID.
- **Merged passages:** one ID survives; the other is marked retired.
- If a revision breaks a citation's exact quote, the [[Validator]] flags it for review.
