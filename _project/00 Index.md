---
title: Project Index
updated: 2026-11-20
---
# Perfectly Fulfilled Prophecies: Project Index

## Start here (for Claude or any AI assistant in a new session)
1. Read [[Current]]: what's in progress and the next step.
2. Skim the most recent note in `sessions/` for what happened last time.
3. Consult the other notes below as the task needs them: [[Schema overview]] before touching content, [[Decision log]] before reopening a question, [[Conventions overview]] for how we work.
4. Run `git status` and `git log --oneline -5` to confirm the vault matches [[Current]].
5. Resume from the first unchecked item in [[Current]] → Next steps.

This vault (local git repo) is the source of truth. The "Project Context" doc in the claude.ai Project is a compact mirror; if they disagree, the vault wins.

## Map

| Folder | What's in it | Changes |
|---|---|---|
| [[Current]] | Status, in-progress work, next steps, blockers | Every session |
| `vision/` | [[Goals]] and [[Success test]] | Rarely |
| `schema/` | How the book is modeled. Start at [[Schema overview]] | When we change the model |
| `decisions/` | [[Decision log]] (all decisions, append-only) + long-form notes for big decisions | When we decide something |
| `conventions/` | How we work. Start at [[Conventions overview]] | Rarely |
| `conversion/` | [[Verify against DOCX]] (formatting to check against the manuscript file) and [[Content notes]] (repetition and possible internal differences, for the author and v1) | As chapters are converted |
| `sessions/` | One dated note per working session: what we did and decided | Every session (new note) |

## Vault layout (outside `_project/`)
`source/` manuscript .docx · `editions/` frozen editions · `passages/ed1/` verbatim book text by edition · `_test/` labeled test fixtures · `claims/` · `arguments/` · `objections/` · `assets/` images. Details: [[Vault layout]].
