---
title: Vault layout
updated: 2026-11-22
---
# Vault layout

```
_project/          project memory (start at 00 Index)
source/            original manuscript .docx files (read-only reference)
editions/          one note per frozen edition (ed1.md, ...)
passages/
  ed1/             verbatim text of edition 1, one file per chapter
  ed2/             (only if a revised edition is ever frozen)
claims/            C-0001.md ...
arguments/         A-0001.md ...
objections/        O-0001.md ...
assets/            images extracted from the .docx
_test/             labeled test fixtures, mirroring the real layout
                   (_test/passages/ed1/, _test/passages/ed2/, _test/claims/, ...);
                   never real book content. The validator runs on any root.
```

## Naming
- Passage files: `passages/ed1/00a Preface.md`, `00b Introduction.md`, `01 Chapter 1.md`, `02 Chapter 2.md`, ...
- The same file names are used in every edition folder.
- Claim, argument and objection notes are named **by ID only** (`C-0001.md`); the display name lives in a `title` property, so renaming a title never breaks a link.
