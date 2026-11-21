---
title: Vault layout
updated: 2026-11-20
---
# Vault layout

```
_project/     project memory (start at 00 Index)
source/       original manuscript .docx (read-only reference)
editions/     one note per frozen edition (ed1.md, ...)
passages/     verbatim book text, one file per chapter
claims/       C-0001.md ...
arguments/    A-0001.md ...
objections/   O-0001.md ...
assets/       images extracted from the .docx
```

## Naming
- Passage files: `00a Preface.md`, `00b Introduction.md`, `01 Chapter 1.md`, `02 Chapter 2.md`, ...
- Claim, argument and objection notes are named **by ID only** (`C-0001.md`); the display name lives in a `title` property, so renaming a title never breaks a link.
