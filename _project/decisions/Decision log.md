---
title: Decision log
updated: 2026-11-22
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
| D-007 | 2026-11-20 | Freeze ed1 (SHA-256 + git tag); citations default to ed1; revision rules for revised/split/merged passages. *Storage of old wording superseded by D-023* | Preserve citations to original wording | Josh, Claude |
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
| D-018 | 2026-11-20 | Local git only (Option A), no GitHub. Claude works through the connected folder while the Mac is awake. *Superseded by D-026* | Keep it simple; no external account | Josh |
| D-019 | 2026-11-20 | Project memory lives in `_project/` in the vault, mirrored to a "Project Context" doc in the claude.ai Project | Context must outlive individual chats | Josh, Claude |
| D-020 | 2026-11-20 | Website (Quartz vs. custom) decided after the pilot | Test the reader flow first | Josh |
| D-021 | 2026-11-20 | `_project/` organized as folders + an index (`00 Index`, `Current`, vision/, schema/, decisions/, conventions/, sessions/) instead of 4 flat files; one decision log, with separate notes only for big decisions | Easier to navigate; each note has one job; volatile status separated from stable docs | Josh, Claude |
| D-022 | 2026-11-22 | Citations live in the body under `## Cites`: one bullet per citation = vault-relative block wikilink + optional `@edN` (omitted = ed1) + optional quote after the first ` — `. Frontmatter stays flat. Edition + block ID identify the passage; the link must open that same passage. Malformed lines reported with path + line; quotes matched against plain text with whitespace normalized; one shared parser for validator and website export. Resolves P-001 | Clickable, backlinked, per-citation quotes; nested frontmatter breaks Obsidian | Claude proposed; Josh decided |
| D-023 | 2026-11-22 | Each frozen edition has its own passage folder (`passages/ed1/`, `passages/ed2/`, ...); IDs unique within an edition, shared across editions for the same passage; earlier editions never edited. Supersedes the "old wording via git tag" part of D-007 | Every edition's wording stays openable and linkable in Obsidian | Josh |
| D-024 | 2026-11-22 | Pilot citation tests: same passage ID in two editions with different wording; both links open the intended text; an `@ed2` citation deliberately pointed at the ed1 file must be caught; move a block and confirm the repaired link opens the correct edition. Then one complete reader path on real content before scaling | Prove the citation scheme end to end | Josh |
| D-025 | 2026-11-22 | Test fixtures (e.g. the synthetic ed2) live only in `_test/`, mirroring the real layout; never in `passages/` | There is no real ed2; invented wording must never be mistakable for the author's | Claude |
| D-026 | 2026-11-22 | GitHub remote `JZtheStudent/revelation-prophecies` (private use for now); the vault's existing history is pushed to it. One repo for vault content + a future `site/` folder (excluded from Obsidian's index). Supersedes D-018 | Lets Claude work from the cloud when the Mac is asleep | Josh |
| D-027 | 2026-11-22 | **v0** = (1) convert the whole book into `passages/ed1/` Markdown with permanent passage IDs, (2) a reading website with good UX where every passage is a linkable anchor. Claims, arguments, objections and the mind map move to v1 | Gets something real in front of the family early; tests the conversion on the whole book; v1 links keep working | Josh; Claude agreed |
| D-028 | 2026-11-22 | v0 audience is Josh's family. Public/private and hosting are deferred until v0 is done (intended to go public later) | Focus on content and reading UX first | Josh |
| D-029 | 2026-11-22 | The manuscript may arrive chapter by chapter; conversion proceeds in reading order as chapters arrive | Matches how Josh will provide it | Josh |

## Pending

| ID | Opened | Question | Current proposal | Waiting on |
|---|---|---|---|---|
| ~~P-001~~ | 2026-11-20 | ~~Citation format~~ | Resolved 2026-11-22 by D-022 | — |
