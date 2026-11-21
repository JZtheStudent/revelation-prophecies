---
title: Project Overview
updated: 2026-11-20
---
# Perfectly Fulfilled Prophecies: Project Overview

## Start here (for Claude or any AI assistant joining a new session)
1. Read this file, then [[Schema]], [[Decisions]] and [[Conventions]], all in `_project/`.
2. **Current status** and **Next steps** below say exactly where we left off. Resume from the first unchecked next step.
3. This vault (a local git repo) is the source of truth. The "Project Context" doc in the claude.ai Project is a compact mirror; if the two disagree, this vault wins.
4. Before changing anything, run `git status` and `git log --oneline -5` to confirm the vault state matches this file.

## Goal
Turn the book *Perfectly Fulfilled Prophecies in the Book of Revelation* (by Josh's dad, 100+ page .docx) into:
- **Short videos**, each introducing one idea from the book.
- **An interactive website** where readers explore how the ideas connect (mind map + explicit "if P, then Q" relationships), trace every claim back to the book's exact text, examine its scriptural and historical support, and see what evidence or counterarguments could strengthen, weaken or overturn it.

Stage 1: organize the book's text into individually referenceable passages with stable IDs and clear links, then model its claims and arguments.

## Success test (for the pilot)
Starting at a conclusion, a reader can:
1. follow it to the argument that supports it,
2. see the premises that work together and the inference type (implies / supports),
3. see any objection and exactly what it challenges (a claim, or the inference),
4. click through to the original paragraph and the exact quoted sentence.

## Current status (as of 2026-11-20)
- [x] Vault created in Obsidian; local git initialized (Option A: no remote). First commit `2bd7080`.
- [x] Pilot folders created: editions, passages, claims, arguments, objections, assets, source.
- [x] Schema agreed in principle; see [[Schema]].
- [x] `_project/` memory files created.
- [ ] **Pending:** citation format. Claude proposed body-based citation lines; waiting on ChatGPT's response to that proposal (see Decisions, P-001).
- [ ] Manuscript .docx not yet added to `source/`.

## Next steps
1. Settle the citation format (P-001) and record it in [[Decisions]].
2. Josh adds the manuscript .docx to `source/`.
3. Freeze edition: create `editions/ed1.md` with the file's SHA-256; tag the commit `ed1`.
4. Pass 1 (mechanical): convert Preface, Introduction and Chapter 1 into passage files with `^PFP-#####` block IDs; extract images to `assets/`; spot-check tables, figures, captions and footnotes against the DOCX.
5. Pass 2 (interpretive): extract claims, arguments and objections in reading order. Include one real historical-source citation if the pilot material has one.
6. Write the validator script (see [[Schema]] § Validator).
7. Test in Obsidian: backlinks, passage links, and link repair after moving a cited block between files.
8. Demonstrate one complete reader path (conclusion → argument → objection → exact manuscript quote) for review.
9. Evaluate the pilot. If Chapter 1 has no substantial multi-premise argument, add the first chapter that does before scaling up.

## Open questions
- P-001 Citation format (body lines vs. nested frontmatter). Pending ChatGPT.
- Website: Quartz vs. custom. Decide after the pilot proves the reader flow.
- Off-machine backup: none yet (Time Machine or a non-GitHub remote suggested).
