#!/usr/bin/env python3
"""Compare the manuscript DOCX with the passage files in passages/<edition>/.

Read-only: it never changes a file. It writes a Markdown report.

Usage:
    python3 tools/compare_docx.py [--docx PATH] [--passages DIR] [--out REPORT.md]

What it checks, chapter by chapter:
  1. Wording   - word-by-word diff (exact characters: hyphen variants, quotes and
                 punctuation all count). Reports MISSING (in DOCX, not in the
                 passages), EXTRA (in the passages, not in the DOCX) and CHANGED.
  2. Structure - where block boundaries differ: DOCX paragraphs merged in the
                 Markdown, Markdown blocks that split a DOCX paragraph, soft line
                 breaks (Shift+Enter) lost, and block-kind differences (list item,
                 heading, boxed note / table cell vs. plain paragraph).
  3. Emphasis  - italic and bold runs in the DOCX that are missing in the Markdown.

How the DOCX is read: body paragraphs and tables in order. A paragraph with an
outline level whose text is entirely bold is a heading. A paragraph with
numbering is a list item (label computed from numbering.xml). Each table cell's
paragraphs are a "box" (the manuscript puts footnotes and notes in one-cell
tables). Soft line breaks are kept as line boundaries inside a block.
"""
import argparse
import difflib
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def q(tag):
    return "{%s}%s" % (W, tag)


# ---------------------------------------------------------------- DOCX reading

def _on(rpr, tag):
    if rpr is None:
        return False
    e = rpr.find("w:" + tag, NS)
    if e is None:
        return False
    return e.get(q("val")) not in ("0", "false", "none")


def _numbering(z):
    """numId -> (format, start) for level 0."""
    try:
        x = etree.fromstring(z.read("word/numbering.xml"))
    except KeyError:
        return {}
    absn = {}
    for a in x.findall("w:abstractNum", NS):
        lv = a.find("w:lvl[@w:ilvl='0']", NS)
        fmt = lv.find("w:numFmt", NS).get(q("val")) if lv is not None and lv.find("w:numFmt", NS) is not None else "decimal"
        st = lv.find("w:start", NS) if lv is not None else None
        absn[a.get(q("abstractNumId"))] = (fmt, int(st.get(q("val"))) if st is not None else 1, a.get(q("abstractNumId")))
    out = {}
    for n in x.findall("w:num", NS):
        a = n.find("w:abstractNumId", NS).get(q("val"))
        out[n.get(q("numId"))] = absn.get(a, ("decimal", 1, a))
    return out


def _runs(p):
    """List of (text, bold, italic); '\n' = soft line break."""
    out = []
    for r in p.iter(q("r")):
        rpr = r.find("w:rPr", NS)
        b, i = _on(rpr, "b"), _on(rpr, "i")
        for c in r:
            if c.tag == q("t"):
                out.append((c.text or "", b, i))
            elif c.tag in (q("br"), q("cr")):
                out.append(("\n", b, i))
            elif c.tag == q("tab"):
                out.append(("\t", b, i))
            elif c.tag in (q("footnoteReference"), q("endnoteReference")):
                out.append(("[^fn%s]" % c.get(q("id")), b, i))
    return out


def _spans(runs, flag):
    """Maximal runs of text with the given flag (1=bold, 2=italic), stripped."""
    spans, cur = [], ""
    for r in runs:
        if r[0] == "\n":
            if cur.strip():
                spans.append(cur.strip())
            cur = ""
            continue
        if r[flag]:
            cur += r[0]
        else:
            if cur.strip():
                spans.append(cur.strip())
            cur = ""
    if cur.strip():
        spans.append(cur.strip())
    return spans


def read_docx(path):
    z = zipfile.ZipFile(path)
    nums = _numbering(z)
    counters = {}
    body = etree.fromstring(z.read("word/document.xml")).find("w:body", NS)
    blocks = []  # dicts: kind, text, bold, italic, label, n (docx paragraph number)
    pno = 0

    def para_block(p, in_table=None):
        nonlocal pno
        pno += 1
        runs = _runs(p)
        text = "".join(r[0] for r in runs)
        if not text.strip():
            return None
        ppr = p.find("w:pPr", NS)
        ol = num = None
        if ppr is not None:
            o = ppr.find("w:outlineLvl", NS)
            ol = int(o.get(q("val"))) if o is not None else None
            n = ppr.find("w:numPr/w:numId", NS)
            num = n.get(q("val")) if n is not None else None
        visible = [r for r in runs if r[0].strip()]
        all_bold = bool(visible) and all(r[1] for r in visible)
        kind, label = "para", None
        if in_table is not None:
            kind = in_table
        elif num is not None and num in nums:
            fmt, start, key = nums[num]
            counters[key] = counters.get(key, start - 1) + 1
            kind = "item"
            label = "•" if fmt == "bullet" else "%d." % counters[key]
        elif ol is not None and all_bold:
            kind = "heading"
        return {
            "kind": kind, "ol": ol, "label": label, "text": text, "n": pno,
            "bold": _spans(runs, 1) if not (kind == "heading") else [], "all_bold": all_bold,
            "italic": _spans(runs, 2), "centered": ppr is not None and ppr.find("w:jc", NS) is not None,
        }

    for el in body:
        if el.tag == q("p"):
            b = para_block(el)
            if b:
                blocks.append(b)
        elif el.tag == q("tbl"):
            rows = el.findall("w:tr", NS)
            ncells = max(len(r.findall("w:tc", NS)) for r in rows)
            kind = "box" if ncells == 1 and len(rows) == 1 else "table"
            for ri, tr in enumerate(rows):
                for ci, tc in enumerate(tr.findall("w:tc", NS)):
                    for p in tc.findall("w:p", NS):
                        b = para_block(p, in_table=kind)
                        if b:
                            b["cell"] = (ri, ci)
                            blocks.append(b)
    return blocks


SECTION_RE = re.compile(r"^(Preface|Introduction|Chapter \d+)$")


def split_docx_sections(blocks):
    """-> (front_matter_blocks, {section_name: [blocks]}). Title lines of a
    chapter (centered bold lines right after 'Chapter N') become kind 'title'."""
    sections, order, cur, front = {}, [], None, []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        t = b["text"].strip()
        if SECTION_RE.match(t) and b["centered"]:
            cur = t
            order.append(cur)
            sections[cur] = []
            b = dict(b, kind="title")
            sections[cur].append(b)
            i += 1
            while i < len(blocks) and blocks[i]["centered"] and blocks[i]["kind"] in ("heading", "para") \
                    and not SECTION_RE.match(blocks[i]["text"].strip()):
                sections[cur].append(dict(blocks[i], kind="title"))
                i += 1
            continue
        (sections[cur] if cur else front).append(b)
        i += 1
    return front, sections, order


# ------------------------------------------------------------ Markdown reading

ID_RE = re.compile(r"\s*\^(PFP-\d{5})\s*$")


def md_inline(text):
    """-> (plain text, bold spans, italic spans)."""
    bold = [m.group(1).strip() for m in re.finditer(r"\*\*(.+?)\*\*", text)]
    t2 = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    ital = [m.group(2).strip() for m in re.finditer(r"(?<![\w*])([*_])(?!\s)(.+?)(?<!\s)\1(?![\w*])", t2)]
    plain = re.sub(r"(?<![\w*])([*_])(?!\s)(.+?)(?<!\s)\1(?![\w*])", r"\2", t2)
    plain = re.sub(r"\\([\\`*_{}\[\]()#+\-.!>])", r"\1", plain)
    plain = plain.replace("<br>", "\n")
    return plain, bold, ital


def read_md(path):
    """-> (frontmatter dict, blocks). Block: kind, text, ids, line, bold, italic.
    kinds: h1, heading, para, item, callout. A list's ID (on the line after the
    list) is attached to every item; an item's own ^ID wins."""
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    fm, i = {}, 0
    if lines and lines[0].strip() == "---":
        i = 1
        while lines[i].strip() != "---":
            m = re.match(r"(\w+):\s*(.*?)\s*(#.*)?$", lines[i])
            if m:
                fm[m.group(1)] = m.group(2).strip('"')
            i += 1
        i += 1
    blocks, pending_list = [], []

    def add(kind, raw, line, level=None):
        idm = ID_RE.search(raw)
        ids = [idm.group(1)] if idm else []
        raw = ID_RE.sub("", raw)
        plain, b, it = md_inline(raw)
        blk = {"kind": kind, "text": plain, "ids": ids, "line": line, "bold": b, "italic": it, "level": level}
        blocks.append(blk)
        return blk

    para_buf, para_line = [], 0
    callout_buf, callout_line = [], 0

    def flush_para():
        nonlocal para_buf
        if para_buf:
            add("para", "\n".join(para_buf), para_line)
            para_buf = []

    def flush_callout():
        nonlocal callout_buf
        if callout_buf:
            add("callout", "\n".join(callout_buf), callout_line)
            callout_buf = []

    while i < len(lines):
        ln, lno = lines[i], i + 1
        s = ln.strip()
        if not s:
            flush_para(); flush_callout()
            i += 1
            continue
        if s.startswith(">"):
            flush_para()
            body = s[1:].strip()
            if re.match(r"\[!\w+\]", body):
                flush_callout()
                callout_line = lno
                rest = re.sub(r"^\[!\w+\][-+]?\s*", "", body)
                callout_header = rest  # reference/translation header, not book text
                i += 1
                continue
            if not callout_buf:
                callout_line = lno
            callout_buf.append(body)
            i += 1
            continue
        flush_callout()
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush_para()
            lvl = len(m.group(1))
            add("h1" if lvl == 1 else "heading", m.group(2), lno, lvl)
            i += 1
            continue
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", ln)
        if m and not para_buf:
            blk = add("item", m.group(3), lno)
            blk["indent"] = len(m.group(1))
            blk["marker"] = "bullet" if m.group(2) in "-*+" else "number"
            pending_list.append(blk)
            i += 1
            continue
        m = re.match(r"^\^(PFP-\d{5})$", s)
        if m:
            flush_para()
            target = pending_list or ([blocks[-1]] if blocks else [])
            for b in target:
                if not b["ids"]:
                    b["ids"] = [m.group(1)]
                b.setdefault("list_id", m.group(1))
            pending_list = []
            i += 1
            continue
        if not para_buf:
            para_line = lno
            pending_list = [] if not pending_list or blocks[-1]["kind"] != "item" else pending_list
        para_buf.append(s)
        i += 1
    flush_para(); flush_callout()
    return fm, blocks


# ------------------------------------------------------------------ comparison

def tokens(blocks, side):
    """-> list of (word, block_index, boundary) where boundary is None or a tag
    marking the first word of a block ('block:<kind>') or of a soft line ('line')."""
    out = []
    for bi, b in enumerate(blocks):
        text = b["text"]
        if side == "md" and b["kind"] == "h1":
            text = re.sub(r"\s+—\s+", "\n", text, count=1)  # "Chapter 2 — Title" was built from 2 lines
        segs = text.split("\n")
        first = True
        for si, seg in enumerate(segs):
            words = seg.split()
            for wi, w in enumerate(words):
                if first:
                    tag = "block:" + b["kind"]
                    first = False
                elif wi == 0:
                    tag = "line"
                else:
                    tag = None
                out.append((w, bi, tag))
    return out


def short(s, n=110):
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def where_md(mb, path):
    ids = ",".join(mb["ids"]) if mb.get("ids") else "no ID: “%s”" % short(mb["text"], 40)
    return "%s (L%d)" % (ids, mb["line"])


KIND_NAME = {"para": "paragraph", "item": "list item", "heading": "heading", "title": "title",
             "box": "boxed note (1-cell table)", "table": "table cell", "h1": "title",
             "callout": "callout"}


def compare_section(name, dblocks, mfile, mblocks):
    R = {"wording": [], "structure": [], "emphasis": [], "stats": {}}
    dt, mt = tokens(dblocks, "docx"), tokens(mblocks, "md")
    A, B = [t[0] for t in dt], [t[0] for t in mt]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    ops = sm.get_opcodes()
    R["stats"] = {"docx_words": len(A), "md_words": len(B),
                  "matched": sum(i2 - i1 for tag, i1, i2, j1, j2 in ops if tag == "equal")}

    def ctx(tokens_, i, j):
        lo, hi = max(0, i - 6), min(len(tokens_), j + 6)
        return " ".join(t[0] for t in tokens_[lo:i]), " ".join(t[0] for t in tokens_[i:j]), " ".join(t[0] for t in tokens_[j:hi])

    def md_block_at(j):
        j = min(max(j, 0), len(mt) - 1)
        return mblocks[mt[j][1]] if mt else None

    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            continue
        mb = md_block_at(j1 if j1 < len(mt) else j1 - 1)
        db = dblocks[dt[min(i1, len(dt) - 1)][1]] if dt else None
        before, dtxt, after = ctx(dt, i1, i2)
        _, mtxt, _ = ctx(mt, j1, j2)
        R["wording"].append({
            "type": {"delete": "MISSING", "insert": "EXTRA", "replace": "CHANGED"}[tag],
            "md": where_md(mb, mfile) if mb else "-", "docx_n": db["n"] if db else None,
            "docx_kind": KIND_NAME.get(db["kind"], db["kind"]) if db else None,
            "docx": dtxt, "mdtext": mtxt, "before": before, "after": after,
            "nwords": max(i2 - i1, j2 - j1),
        })

    # structure: walk aligned word pairs
    pairs = []
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            pairs += list(zip(range(i1, i2), range(j1, j2)))
    struct = defaultdict(list)  # key: md block index -> messages
    seen_kind = set()
    for i, j in pairs:
        dw, dbi, dtag = dt[i]
        mw, mbi, mtag = mt[j]
        db, mb = dblocks[dbi], mblocks[mbi]
        dk = db["kind"]
        mk = mb["kind"]
        if dtag and dtag.startswith("block") and not mtag:
            struct[mbi].append(("MERGED", "DOCX %s starts here (“%s…”) but the Markdown runs it into the previous block"
                                % (KIND_NAME.get(dk, dk) + (" " + db["label"] if db.get("label") else ""), short(db["text"], 50))))
        elif dtag == "line" and not mtag:
            struct[mbi].append(("LINE", "soft line break lost before “%s”" % short(" ".join(t[0] for t in dt[i:i + 6]), 45)))
        elif mtag and mtag.startswith("block") and not dtag:
            struct[mbi].append(("SPLIT", "Markdown starts a new %s here, inside a DOCX %s"
                                % (KIND_NAME.get(mk, mk), KIND_NAME.get(dk, dk))))
        elif mtag and mtag.startswith("block") and dtag == "line":
            struct[mbi].append(("SPLIT-LINE", "Markdown starts a new %s at a DOCX soft line break (inside one DOCX %s)"
                                % (KIND_NAME.get(mk, mk), KIND_NAME.get(dk, dk))))
        if dtag and dtag.startswith("block") and mtag and mtag.startswith("block"):
            norm = {"title": "h1", "h1": "h1", "heading": "heading", "para": "para", "item": "item",
                    "box": "box", "table": "table", "callout": "para"}
            if norm.get(dk) != norm.get(mk) and not (dk == "title" and mk in ("h1", "heading")):
                if (dbi, mbi) not in seen_kind:
                    seen_kind.add((dbi, mbi))
                    extra = ""
                    if dk == "item":
                        extra = " (label %s)" % db["label"]
                    if dk == "heading":
                        extra = " (outline level %s)" % db["ol"]
                    elif db.get("all_bold"):
                        extra = " (entirely bold)"
                    struct[mbi].append(("KIND", "DOCX %s%s, Markdown %s" % (KIND_NAME.get(dk, dk), extra, KIND_NAME.get(mk, mk))))
            elif dk == "item" and mk == "item" and (db["label"] == "•") != (mb.get("marker") == "bullet") \
                    and ("lt", mb.get("list_id") or mbi) not in seen_kind:
                seen_kind.add(("lt", mb.get("list_id") or mbi))
                struct[mbi].append(("LIST-TYPE", "DOCX %s list, Markdown %s list"
                                    % ("bulleted" if db["label"] == "•" else "numbered", mb.get("marker"))))
    for mbi in sorted(struct):
        mb = mblocks[mbi]
        msgs = struct[mbi]
        R["structure"].append({"md": where_md(mb, mfile), "kind": mb["kind"], "text": short(mb["text"], 70), "msgs": msgs})

    # emphasis: DOCX italic/bold spans missing from the Markdown block holding them
    md_ital = defaultdict(set)
    md_bold = defaultdict(set)
    for bi, b in enumerate(mblocks):
        md_ital[bi] = set(" ".join(x.split()) for x in b["italic"])
        md_bold[bi] = set(" ".join(x.split()) for x in b["bold"])
    dpos = {}
    for i, j in pairs:
        dpos.setdefault(dt[i][1], mt[j][1])
    for dbi, db in enumerate(dblocks):
        if db["kind"] in ("title",):
            continue
        mbi = dpos.get(dbi)
        if mbi is None:
            continue
        for kind, spans, have in (("italic", db["italic"], md_ital[mbi]), ("bold", db["bold"], md_bold[mbi])):
            for s in spans:
                s = " ".join(s.split())
                if s and s not in have:
                    R["emphasis"].append({"md": where_md(mblocks[mbi], mfile), "kind": kind, "span": s})
    return R


# ---------------------------------------------------------------------- report

def md_file_for(name, files):
    if name == "Preface":
        return files.get("00a")
    if name == "Introduction":
        return files.get("00b")
    m = re.match(r"Chapter (\d+)$", name)
    return files.get("%02d" % int(m.group(1))) if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--docx", default=None)
    ap.add_argument("--passages", default=str(root / "passages" / "ed1"))
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    docx = Path(a.docx) if a.docx else next((root / "source").glob("*.docx"))
    dblocks = read_docx(docx)
    front, secs, order = split_docx_sections(dblocks)
    files = {p.name.split(" ")[0]: p for p in sorted(Path(a.passages).glob("*.md"))}

    out = []
    w = out.append
    w("# DOCX comparison report\n")
    w("- DOCX: `%s`" % docx.name)
    w("- Passages: `%s` (%d files)" % (Path(a.passages).name, len(files)))
    w("- Generated by `tools/compare_docx.py` (read-only). Wording is compared word by word with exact characters.\n")
    if front:
        w("**Front matter in the DOCX (title page, not in any passage file):** " +
          " / ".join("“%s”" % short(b["text"], 60) for b in front) + "\n")

    summary, bodies = [], []
    used = set()
    for name in order:
        mf = md_file_for(name, files)
        if not mf:
            summary.append((name, "-", "no passage file", "", "", ""))
            continue
        used.add(mf.name)
        fm, mblocks = read_md(mf)
        R = compare_section(name, secs[name], mf, mblocks)
        st = R["stats"]
        nmiss = sum(x["nwords"] for x in R["wording"] if x["type"] == "MISSING")
        nextra = sum(x["nwords"] for x in R["wording"] if x["type"] == "EXTRA")
        nch = sum(1 for x in R["wording"] if x["type"] == "CHANGED")
        summary.append((name, mf.name, "%d / %d" % (st["matched"], st["docx_words"]),
                        "%d chg, %d missing words, %d extra words" % (nch, nmiss, nextra),
                        str(sum(len(s["msgs"]) for s in R["structure"])), str(len(R["emphasis"]))))
        b = []
        b.append("\n## %s — `%s`\n" % (name, mf.name))
        b.append("DOCX words %d · Markdown words %d · matched %d\n" % (st["docx_words"], st["md_words"], st["matched"]))
        b.append("### Wording\n")
        if not R["wording"]:
            b.append("No wording differences.\n")
        for x in R["wording"]:
            if x["type"] == "MISSING":
                b.append("- **MISSING** before %s — DOCX %s ¶%s has: “%s” \n  context: …%s **[here]** %s…"
                         % (x["md"], x["docx_kind"], x["docx_n"], short(x["docx"], 400), short(x["before"], 60), short(x["after"], 60)))
            elif x["type"] == "EXTRA":
                b.append("- **EXTRA** at %s — Markdown has “%s”, not in the DOCX \n  context: …%s **[here]** %s…"
                         % (x["md"], short(x["mdtext"], 200), short(x["before"], 60), short(x["after"], 60)))
            else:
                b.append("- **CHANGED** at %s — DOCX “%s” → Markdown “%s” \n  context: …%s **[here]** %s…"
                         % (x["md"], short(x["docx"], 200), short(x["mdtext"], 200), short(x["before"], 60), short(x["after"], 60)))
        b.append("\n### Structure (paragraph / heading / list / line-break boundaries)\n")
        if not R["structure"]:
            b.append("No boundary differences.\n")
        for s in R["structure"]:
            counts = defaultdict(int)
            for tag, msg in s["msgs"]:
                counts[tag] += 1
            lines = []
            line_lost = [m for t, m in s["msgs"] if t == "LINE"]
            for t, m in s["msgs"]:
                if t != "LINE":
                    lines.append("%s: %s" % (t, m))
            if line_lost:
                lines.append("LINE: %d soft line break(s) lost — %s" % (len(line_lost), "; ".join(m.replace("soft line break lost before ", "") for m in line_lost[:4]) + (" …" if len(line_lost) > 4 else "")))
            b.append("- %s %s “%s”" % (s["md"], s["kind"], s["text"]))
            for l in lines:
                b.append("  - " + l)
        b.append("\n### Emphasis in the DOCX not in the Markdown\n")
        if not R["emphasis"]:
            b.append("None.\n")
        else:
            byid = defaultdict(list)
            for e in R["emphasis"]:
                byid[e["md"]].append("%s “%s”" % (e["kind"], short(e["span"], 70)))
            for k, v in byid.items():
                b.append("- %s: %s" % (k, "; ".join(v)))
        bodies.append("\n".join(b))

    w("## Summary\n")
    w("| Section | File | Words matched / DOCX words | Wording | Structure notes | Emphasis missing |")
    w("|---|---|---|---|---|---|")
    for r in summary:
        w("| " + " | ".join(r) + " |")
    unused = sorted(set(p.name for p in files.values()) - used)
    if unused:
        w("\nPassage files with no DOCX section: " + ", ".join(unused))
    w("\nLegend: **MERGED** = DOCX starts a new paragraph / list item / note here, Markdown doesn't. "
      "**SPLIT** = Markdown starts a new block inside one DOCX paragraph. **LINE** = DOCX soft line break "
      "(Shift+Enter) not kept. **KIND** = same text, different block type.\n")
    out += bodies
    text = "\n".join(out) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print("wrote", a.out)
    else:
        sys.stdout.write(text)
    for r in summary:
        print(" | ".join(r), file=sys.stderr)


if __name__ == "__main__":
    main()
