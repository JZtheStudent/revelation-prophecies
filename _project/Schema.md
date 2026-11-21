---
title: Pilot Schema
updated: 2026-11-20
status: agreed in principle; citation format pending (P-001)
---
# Pilot Schema

## 1. Folders
```
_project/     project memory: Overview, Schema, Decisions, Conventions
source/       original manuscript .docx (read-only reference)
editions/     one note per frozen edition (ed1.md, ...)
passages/     verbatim book text, one file per chapter
claims/       C-0001.md ...   one proposition each (includes assumptions)
arguments/    A-0001.md ...   premises → conclusion
objections/   O-0001.md ...   challenges to a claim or an argument
assets/       images extracted from the .docx
```
- Note files are named by ID only (`C-0001.md`); the display name lives in a `title` property. Renaming a title never breaks a link.
- Passage files: `00a Preface.md`, `00b Introduction.md`, `01 Chapter 1.md`, `02 Chapter 2.md`, ...

## 2. Passage IDs
- Format `PFP-00001` (5 digits, zero-padded), written as an Obsidian block ID at the end of the block: `^PFP-00127`.
- Opaque and permanent: never renumbered, never reused. Initial assignment follows reading order; later insertions take the next free number.
- The **bare ID (plus edition) is canonical.** The file name inside a link (`[[01 Chapter 1#^PFP-00127]]`) exists only to make it clickable, and the validator repairs it if a block moves between files.

## 3. Location (derived, never stored by hand)
Display location = file + heading path + block order, computed by a script. Moving a passage = cut/paste the block with its `^ID`.

## 4. Editions
- The pilot freezes **ed1**: `editions/ed1.md` records the source file and its SHA-256, and the git commit is tagged `ed1`.
- Citations default to ed1.
- Revision rules (not built yet):
  - Revised passage: keeps its ID; old wording preserved via the edition tag.
  - Split passage: original ID stays on the first part; the rest gets a new ID.
  - Merged passages: one ID survives; the other is marked retired.
- If a revision breaks a citation's exact quote, the validator flags it for review.

## 5. Passages and block types
- Default: one original paragraph = one passage, even if it contains several claims. Claims pinpoint a sentence with an exact quote.
- Block type is inferred from Markdown syntax:

| Content | Written as | ID rule |
|---|---|---|
| Paragraph | plain text | one ID |
| List | `-` / `1.` items | one ID on the whole list; item IDs only when cited separately |
| Table | Markdown table | one ID on its own line after the table |
| Diagram / chart | `![[fig-01-02.png]]` + mandatory text description of what it asserts | ID on the description |
| Footnote | moved to a `## Notes` section at the end of the chapter | one ID each |
| Heading | `##` | no ID (structure only) |

- Block quotes distinguish the author's words from quoted material with callouts:
  - `> [!scripture] Rev.12.6 (KJV)`: Bible quotation, with reference and translation
  - `> [!source] Author, *Work*, p. N`: historical or secondary source
  - plain `>`: the author quoting informally

## 6. Note types and fields

**Chapter file (passages/)**
```yaml
edition: ed1
part: preface | intro | chapter
chapter: 1
title: "..."
```

**Edition (editions/)**
```yaml
edition: ed1
source_file: source/<name>.docx
sha256: <hash>
frozen: 2026-MM-DD
```

**Claim (claims/)**: one proposition.
```yaml
title: "..."
by: author | editor | external     # author ⇒ must cite the book
scripture: [Rev.12.6]               # OSIS-style refs, evidence for readers
```
Body: the proposition in one sentence, then `## Cites` (see §7).
An **assumption** is just a claim listed in an argument's `assumptions` field, usually `by: editor`.

**Argument (arguments/)**: the only place relations live. Claims have no implies/supports fields.
```yaml
title: "..."
by: author | editor
premises: ["[[C-0001]]", "[[C-0002]]"]   # these work TOGETHER
assumptions: []                          # unstated premises (claims)
conclusion: "[[C-0003]]"
inference: implies | supports            # implies = follows from stated premises; supports = makes more plausible
repairs: "[[A-0001]]"                    # only on editorial reconstructions
responds_to: "[[O-0001]]"                # only on editorial reconstructions
```
Body: how the premises lead to the conclusion, then `## Cites`.
- One-premise support still gets an argument record (single mechanism).
- Independent lines of reasoning for the same conclusion = separate argument records.

**Objection (objections/)**
```yaml
title: "..."
by: author | editor | external
targets: "[[C-0003]]" | "[[A-0001]]"    # claim → challenges its truth; argument → challenges the inference
```
Body: `**Challenges:**` exactly what is challenged, and why. Add `## Cites` if the objection is raised in the book.

**Repairs:** an accepted objection never edits the original argument. A repair is a new argument `by: editor` with `repairs` and `responds_to` links, usually adding the missing premise as an editor assumption. The author's argument stays exactly as stated, and the objection stays attached to it.

## 7. Citations (PENDING, P-001)
Proposed: citations live in the note body so they're clickable, appear as backlinks, and each carries its own quote:
```markdown
## Cites
- [[01 Chapter 1#^PFP-00127]] — "exact quoted sentence"
- [[01 Chapter 1#^PFP-00128]] @ed2 — "quote from a later edition"
```
- Edition defaults to ed1; write `@edN` only when it differs.
- The quote is optional, but when present it must be an exact substring of that passage in that edition.
- Rejected alternative: nested objects in frontmatter (the Obsidian Properties panel can't edit them, and links inside them aren't clickable or backlinked).

## 8. Validator (to build in the pilot)
Errors:
- duplicate passage or note IDs
- a citation to a passage ID that doesn't exist (in the given edition)
- a quote that isn't an exact substring of its passage
- a `by: author` claim with no citation
- an argument that lists its own conclusion as a premise
Warnings:
- unresolved forward references (allowed during extraction)
- a link whose file name doesn't match where the block now lives (auto-repairable)
