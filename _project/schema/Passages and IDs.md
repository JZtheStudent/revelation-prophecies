---
title: Passages and IDs
updated: 2026-11-22
---
# Passages and IDs

## IDs
- Format `PFP-00001` (5 digits), written as an Obsidian block ID at the end of the block: `^PFP-00127`.
- Opaque and permanent: **never renumbered, never reused.** IDs are unique within an edition; the same ID in two edition folders means the same passage (possibly reworded). Initial assignment follows reading order; later insertions take the next free number.
- Edition + ID is canonical. Links use vault-relative paths (`[[passages/ed1/01 Chapter 1#^PFP-00127]]`); the [[Validator]] repairs the path if a block moves between files. See [[Citations]].

## Location is derived, never stored by hand
Display location = file + heading path + block order, computed by a script. Moving a passage = cut/paste the block with its `^ID`.

## Granularity
One original paragraph = one passage, even if it contains several claims. Claims pinpoint a sentence with an exact quote ([[Citations]]).

## Chapter file frontmatter
```yaml
edition: ed1
part: preface | intro | chapter
chapter: 1
title: "..."
```

## Block types (inferred from Markdown syntax)

| Content | Written as | ID rule |
|---|---|---|
| Paragraph | plain text | one ID |
| List | `-` / `1.` items | one ID on the whole list; item IDs only when cited separately |
| Table | Markdown table | one ID on its own line after the table |
| Diagram / chart | `![[fig-01-02.png]]` + mandatory text description of what it asserts | ID on the description |
| Footnote | moved to a `## Notes` section at the end of the chapter | one ID each |
| Heading | `##` | no ID (structure only) |

## Quoted material (callouts)
- `> [!scripture] Rev.12.6 (KJV)`: Bible quotation, with reference and translation
- `> [!source] Author, *Work*, p. N`: historical or secondary source
- plain `>`: the author quoting informally

## Rules
Passage text is verbatim from the frozen edition. Edit it only to fix an extraction error against the DOCX, and note the fix in the commit message.
