---
title: Argument model
updated: 2026-11-20
---
# Argument model

## Claim (`claims/C-0001.md`)
One proposition.
```yaml
title: "..."
by: author | editor | external     # author ⇒ must cite the book
scripture: [Rev.12.6]               # OSIS-style refs; evidence for readers
```
Body: the proposition in one sentence, then `## Cites` ([[Citations]]).
An **assumption** is just a claim listed in an argument's `assumptions` field, usually `by: editor`.

Evidence stays a claim property for the pilot; separate evidence notes come only once sources are reused.

## Argument (`arguments/A-0001.md`)
The **only** place relations live; claims carry no implies/supports fields.
```yaml
title: "..."
by: author | editor
premises: ["[[C-0001]]", "[[C-0002]]"]   # work TOGETHER
assumptions: []                          # unstated premises (claims)
conclusion: "[[C-0003]]"
inference: implies | supports
repairs: "[[A-0001]]"                    # editorial reconstructions only
responds_to: "[[O-0001]]"                # editorial reconstructions only
```
Body: how the premises lead to the conclusion, then `## Cites`.
- `implies`: the conclusion follows from the stated premises. `supports`: the premises make it more plausible.
- One-premise support still gets an argument record (single mechanism).
- Independent lines of reasoning for the same conclusion = separate records.

## Objection (`objections/O-0001.md`)
```yaml
title: "..."
by: author | editor | external
targets: "[[C-0003]]"     # claim → challenges its truth; argument → challenges the inference
```
Body: `**Challenges:**` exactly what is challenged, and why. Add `## Cites` if the objection is raised in the book itself.

## Repairs
An accepted objection never edits the original argument. A repair is a new argument (`by: editor`) with `repairs` and `responds_to` links, usually adding the missing premise as an editor assumption. The author's argument stays exactly as stated, with its objection still attached.
