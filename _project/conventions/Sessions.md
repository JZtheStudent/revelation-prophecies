---
title: Sessions
updated: 2026-11-20
---
# Sessions

## Starting
1. Josh connects this vault folder to the chat ("Add folder" in the Claude desktop app). Uploading a folder is a one-time snapshot, not a live connection.
2. Claude reads [[00 Index]] → [[Current]] → the latest note in `sessions/`, and checks `git status` / `git log`.
3. Resume from the first unchecked item in [[Current]] → Next steps.

## Ending (or finishing a unit of work)
1. Update [[Current]]: status, next steps, blockers, last-session link.
2. Write a short session note: `sessions/YYYY-MM-DD <topic>.md` (what we did, what we decided, what's next).
3. Add new decisions to the [[Decision log]] (new rows only; never rewrite old ones).
4. Update the `schema/` notes if the model changed.
5. Re-sync the "Project Context" doc in the claude.ai Project.
6. Commit.

## Where things go
- Something we **decided** → [[Decision log]]
- Something we **did** → the session note
- Something we're **doing next** → [[Current]]
- How the model **works** → `schema/`
