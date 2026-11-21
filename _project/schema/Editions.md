---
title: Editions
updated: 2026-11-20
---
# Editions

## Freezing
The pilot freezes **ed1**: `editions/ed1.md` records the source and its hash, and the git commit is tagged `ed1`. Citations default to ed1.

```yaml
edition: ed1
source_file: source/<name>.docx
sha256: <hash>
frozen: 2026-MM-DD
```

## Revision rules (not built yet)
- **Revised passage:** keeps its ID; old wording preserved via the edition tag.
- **Split passage:** original ID stays on the first part; the rest gets a new ID.
- **Merged passages:** one ID survives; the other is marked retired.
- If a revision breaks a citation's exact quote, the [[Validator]] flags it for review.
