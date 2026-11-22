---
title: Citations
updated: 2026-11-22
status: decided (D-022)
---
# Citations

Manuscript citations (where the book says it) live in the note **body**, under `## Cites`. Frontmatter stays flat. Evidence (scripture, sources) is separate; see [[Argument model]].

## Format
One top-level bullet per citation:
```markdown
## Cites
- [[passages/ed1/01 Chapter 1#^PFP-00127]] — "Exact quoted sentence."
- [[passages/ed2/01 Chapter 1#^PFP-00127]] @ed2 — "Revised sentence."
- [[passages/ed1/01 Chapter 1#^PFP-00130]]
```
Each line has:
1. a **vault-relative block wikilink** (`passages/<edition>/<file>#^<passage ID>`),
2. an optional **edition marker** `@edN`; an omitted marker always means `ed1`,
3. an optional **quote** after ` — ` (space, em dash, space).

## Identity
- **Edition marker + block ID** determine which passage is cited. The wikilink must open that same passage: its folder must be `passages/<that edition>/`, and the block must exist in that file.
- If a passage moves, repair the link path using the edition and passage ID together.

## Parsing rules
1. Parse the wikilink first, then the optional `@edN` marker.
2. Everything after the **first** ` — ` is quote text, so an em dash inside the quote is harmless.
3. Quote delimiters: straight `"…"` or curly `“…”` quotes, stripped before comparison.
4. A malformed line is reported with the note path and line number.
5. **The same parser serves both the [[Validator]] and the website export**, so the site generates links and per-passage backlinks from exactly what the validator checked.

## Quote matching
A quote must appear in the cited passage's **plain text**:
- Strip Markdown syntax (emphasis markers, link brackets, callout headers, the `^ID` marker).
- Normalize whitespace (collapse runs, trim).
- Preserve wording, punctuation and capitalization exactly.

## Rejected alternative
Nested objects in frontmatter (`cites: - {passage, edition, quote}`): the Obsidian Properties panel can't edit them, and links inside them aren't clickable or backlinked.
