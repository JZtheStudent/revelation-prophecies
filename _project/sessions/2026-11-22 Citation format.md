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
- Chapter 3 → `passages/ed1/03 Chapter 3.md`, 15 blocks (6 scripture callouts + 9 paragraphs), PFP-00135 to PFP-00149 (provisional).
- Chapter 4 → `passages/ed1/04 Chapter 4.md`, 54 blocks, PFP-00150 to PFP-00203 (provisional). Started [[Content notes]] for content observations.
- Chapter 5 → `passages/ed1/05 Chapter 5.md`, 22 blocks, PFP-00204 to PFP-00225 (provisional).
- Chapter 6 → `passages/ed1/06 Chapter 6.md`, 29 blocks, PFP-00226 to PFP-00254 (provisional).
- Chapter 7 → `passages/ed1/07 Chapter 7.md`, 13 paragraphs, PFP-00255 to PFP-00267 (provisional).
- Chapter 8 → `passages/ed1/08 Chapter 8.md`, 21 blocks (12 scripture callouts + 9 paragraphs), PFP-00268 to PFP-00288 (provisional).
- Chapter 9 → `passages/ed1/09 Chapter 9.md`, 13 paragraphs, PFP-00289 to PFP-00301 (provisional).
- Chapter 10 → `passages/ed1/10 Chapter 10.md`, 12 paragraphs, PFP-00302 to PFP-00313 (provisional).
- Chapter 11 → `passages/ed1/11 Chapter 11.md`, 22 blocks (3 scripture callouts), PFP-00314 to PFP-00335 (provisional).
- Chapter 12 → `passages/ed1/12 Chapter 12.md`, 12 paragraphs, PFP-00336 to PFP-00347 (provisional).
- Chapter 13 → `passages/ed1/13 Chapter 13.md`, 35 blocks (8 lists), PFP-00348 to PFP-00382 (provisional).

## Next
Josh links GitHub to Claude, pushes once, and adds the first chapters. See [[Current]].
