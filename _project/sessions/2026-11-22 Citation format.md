---
title: 2026-11-22 Citation format
date: 2026-11-22
participants: Josh, Claude
---
# 2026-11-22: Citation format

## What we did
- Settled P-001: body-based citations under `## Cites`, with a vault-relative block wikilink, an optional `@edN` and an optional quote.
- Moved passages into per-edition folders (`passages/ed1/`).
- Updated the schema notes: Citations, Vault layout, Passages and IDs, Editions, Validator.

## What we decided
- D-022 citation format and parsing rules (resolves P-001)
- D-023 per-edition passage folders (supersedes part of D-007)
- D-024 pilot citation tests
- D-025 test fixtures only in `_test/`
- D-026 GitHub remote `JZtheStudent/revelation-prophecies` (supersedes local-only)
- D-027 v0 = book → Markdown + reading website; argument model moves to v1
- D-028 family audience; hosting deferred
- D-029 manuscript may arrive chapter by chapter
- D-030 pasted chapters are provisional until checked against the DOCX

## Converted
- Preface → `passages/ed1/00a Preface.md`, 12 paragraphs, PFP-00001 to PFP-00012 (provisional).
- Introduction → `passages/ed1/00b Introduction.md`, 59 blocks (55 paragraphs + 4 lists), PFP-00013 to PFP-00071 (provisional). Started [[Verify against DOCX]] for formatting the paste may have lost (one footnote is missing).
- Chapter 1 → `passages/ed1/01 Chapter 1.md`, 26 blocks, PFP-00072 to PFP-00097 (provisional). Pilot pass 1 complete.
- Chapter 2 → `passages/ed1/02 Chapter 2.md`, 37 blocks, PFP-00098 to PFP-00134 (provisional; Greek verse missing from the paste).

## Next
Josh links GitHub to Claude, pushes once, and adds the first chapters. See [[Current]].
