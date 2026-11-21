---
title: Schema overview
updated: 2026-11-20
status: agreed in principle; citation format pending (P-001)
---
# Schema overview

How the book is modeled. One note per topic:

| Note | Covers |
|---|---|
| [[Vault layout]] | Folders and file naming |
| [[Passages and IDs]] | Passage IDs, derived location, granularity, block types, callouts |
| [[Editions]] | Freezing editions and revision rules |
| [[Argument model]] | Claims, arguments, objections, repairs, and their fields |
| [[Citations]] | How notes cite the book (**pending P-001**) |
| [[Validator]] | Automated checks |

## The model in one paragraph
The book's text lives verbatim in `passages/`, one file per chapter, with a permanent ID on every citable block. **Claims** are single propositions that cite passages. **Arguments** are the only place relations live: premises (working together) + assumptions → a conclusion, with `inference: implies | supports`. **Objections** target a claim (its truth) or an argument (the inference). Everything carries `by: author | editor | external`, so the author's words are never confused with editorial reconstruction.
