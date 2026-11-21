---
title: Citations
updated: 2026-11-20
status: PENDING (P-001)
---
# Citations (pending P-001)

**Agreed:** a citation resolves by edition + passage ID; an exact quote attaches to that specific citation; edition defaults to ed1. Manuscript citations (where the book says it) are distinct from evidence (scripture and sources that help readers evaluate it).

**Proposed format (awaiting ChatGPT, then Josh):** citations live in the note body:
```markdown
## Cites
- [[01 Chapter 1#^PFP-00127]] — "exact quoted sentence"
- [[01 Chapter 1#^PFP-00128]] @ed2 — "quote from a later edition"
```
- Clickable, shows up in backlinks, one quote per citation.
- Write `@edN` only when the edition isn't ed1.
- The quote is optional but, when present, must be an exact substring of that passage in that edition.

**Rejected alternative:** nested objects in frontmatter (`cites: - {passage, edition, quote}`). The Obsidian Properties panel can't edit them, and links inside them aren't clickable or backlinked, which breaks the [[Success test]].
