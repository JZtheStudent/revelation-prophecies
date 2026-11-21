---
title: Decision log
updated: 2026-11-20
---
# Decision log

Append new decisions at the bottom; never delete. To change a decision, add a new entry that supersedes it and mark the old one `superseded by D-0xx`.
**Source** = who proposed it (Josh / Claude / ChatGPT). Everything here is agreed by Josh unless marked pending.

## Agreed

| ID | Date | Decision | Why | Source |
|---|---|---|---|---|
| D-001 | 2026-11-20 | Git repo = source of truth; Obsidian = editing interface | Plain text, versioned, portable across AIs and tools | Josh |
| D-002 | 2026-11-20 | One Markdown file per chapter for passages | Reads like the book; avoids hundreds of tiny files | Claude → Josh |
| D-003 | 2026-11-20 | Pilot = Preface + Introduction + Chapter 1; add the first chapter with a substantial multi-premise argument if Ch. 1 lacks one | Intro holds method/premises reused later; argument records must get tested | Josh, Claude |
| D-004 | 2026-11-20 | Convert in reading order, in two passes: (1) passages + IDs, (2) claims/arguments/objections | Later arguments depend on earlier claims | Josh, Claude |
| D-005 | 2026-11-20 | Opaque permanent passage IDs `PFP-00001` as Obsidian block IDs; never renumbered or reused | Identity must survive moves and edits | Josh |
| D-006 | 2026-11-20 | Chapter/section/order derived from file + heading path + block order, not stored by hand | Hand-stored fields go stale; block IDs can't carry metadata | Claude; ChatGPT agreed |
| D-007 | 2026-11-20 | Freeze ed1 (SHA-256 + git tag); citations default to ed1; revision rules for revised/split/merged passages | Preserve citations to original wording | Josh, Claude |
| D-008 | 2026-11-20 | One paragraph = one passage, even with multiple claims; exact quotes pinpoint sentences | Keeps the original structure; quotes are verifiable | Josh |
| D-009 | 2026-11-20 | Block types inferred from Markdown syntax; `[!scripture]` / `[!source]` callouts for quoted material; diagrams need a text description; footnotes move to `## Notes` | Distinguishes the author's words from quotations without extra fields | Claude |
| D-010 | 2026-11-20 | Argument records are the single mechanism for inference, including one-premise cases; `inference: implies \| supports` | One place to maintain relations | Josh, Claude; ChatGPT agreed |
| D-011 | 2026-11-20 | Premises + assumptions in one record work together; independent lines of reasoning = separate records | Lets readers challenge each line separately | ChatGPT |
| D-012 | 2026-11-20 | Assumptions are ordinary claims (usually `by: editor`); every claim/argument/objection has `by: author \| editor \| external` | Readers must see what's the author's words vs. editorial reconstruction | Claude |
| D-013 | 2026-11-20 | Manuscript citations (`cites`) are distinct from evidence (`scripture`, sources). Evidence stays a claim property in the pilot; separate evidence notes only when reused | Where the author says it ≠ what supports it | Josh, Claude |
| D-014 | 2026-11-20 | Objections target a claim (truth) or an argument (inference) | Covers claim, assumption and inference without an extra field | Josh, Claude |
| D-015 | 2026-11-20 | Repairs are linked editorial reconstructions (`repairs`, `responds_to`); the original argument and its objection stay untouched | Preserves the author's argument as stated | ChatGPT |
| D-016 | 2026-11-20 | Forward references allowed during extraction; the validator warns, not fails | Extraction in order will hit not-yet-created claims | ChatGPT |
| D-017 | 2026-11-20 | Pilot checks: spot-check tables/figures/captions/footnotes against the DOCX; test link repair after moving a cited block; show one complete reader path before scaling | Verify the success test end to end | ChatGPT |
| D-018 | 2026-11-20 | Local git only (Option A), no GitHub. Claude works through the connected folder while the Mac is awake | Keep it simple; no external account | Josh |
| D-019 | 2026-11-20 | Project memory lives in `_project/` in the vault, mirrored to a "Project Context" doc in the claude.ai Project | Context must outlive individual chats | Josh, Claude |
| D-020 | 2026-11-20 | Website (Quartz vs. custom) decided after the pilot | Test the reader flow first | Josh |
| D-021 | 2026-11-20 | `_project/` organized as folders + an index (`00 Index`, `Current`, vision/, schema/, decisions/, conventions/, sessions/) instead of 4 flat files; one decision log, with separate notes only for big decisions | Easier to navigate; each note has one job; volatile status separated from stable docs | Josh, Claude |

## Pending

| ID | Opened | Question | Current proposal | Waiting on |
|---|---|---|---|---|
| P-001 | 2026-11-20 | Citation format: how to attach edition + passage ID + per-citation quote | Body `## Cites` lines instead of nested frontmatter objects (see [[Citations]]) | ChatGPT's response, then Josh |
