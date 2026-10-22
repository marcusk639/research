#!/usr/bin/env python3
"""Merge per-angle ledgers into global JSONL ledgers and check quote fidelity.

Usage: python3 tools/consolidate.py [--no-fetch]
Writes: sources.jsonl, evidence.jsonl, claims.jsonl, id-map.json, quote-check.md
"""
import concurrent.futures as cf
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
CACHE = RUN / "tools" / ".cache"
ANGLES = sorted(RUN.glob("angle-*.md"))

SRC_RE = re.compile(r"^([AD]\d-S\d+)\s*\|\s*(.+)$")
EV_RE = re.compile(r'^([AD]\d-E\d+)\s*\|\s*([AD]\d-S\d+)\s*\|\s*"(.*)"\s*\|\s*(.*)$')
CL_RE = re.compile(
    r"^([AD]\d-C\d+)\s*\|\s*(.*?)\s*\|\s*support:\s*(.*?)\s*\|\s*independent_sources:\s*(.*?)\s*\|\s*confidence:\s*(.*)$"
)


def clean(line):
    line = line.strip()
    if line.startswith("- "):
        line = line[2:]
    if line.startswith("`") and line.endswith("`"):
        line = line[1:-1]
    if line.startswith("|") and line.endswith("|"):
        line = re.sub(r"\s*\|\s*", " | ", line[1:-1].strip())
    return line.strip()


def norm_url(u):
    u = u.split(" ")[0].strip().rstrip(").,")
    u = re.sub(r"^http://", "https://", u)
    u = u.replace("://www.", "://")
    u = re.sub(r"#.*$", "", u)
    u = re.sub(r"\?utm_[^&]*(&|$)", "", u)
    u = re.sub(r"arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(v\d+)?(\.pdf)?", r"arxiv.org/abs/\2", u)
    return u.rstrip("/")


def extra_urls(raw):
    """Secondary URLs written as '(+ /html/2402.09171)' or '+ https://...'."""
    out = []
    first = raw.split(" ")[0]
    for m in re.finditer(r"\+\s*(\S+)", raw):
        frag = m.group(1).rstrip(")")
        if frag.startswith("/"):
            base = re.match(r"https?://[^/]+", first)
            if base:
                out.append(base.group(0) + frag)
        elif frag.startswith("http"):
            out.append(frag)
    return out


def expand_support(raw, angle):
    """'A1-E3, A1-E5–E7, E25–E39, L4' -> explicit IDs, prefixing bare E-numbers with the angle."""
    out = []
    for m in re.finditer(r"(?:([AD]\d)-)?E(\d+)(?:\s*[–-]\s*(?:[AD]\d-)?E?(\d+))?|\b([LI]\d+)\b", raw):
        if m[4]:
            out.append(m[4])
            continue
        a = m[1] or angle
        lo, hi = int(m[2]), int(m[3] or m[2])
        out += [f"{a}-E{i}" for i in range(lo, hi + 1)]
    return out


def parse():
    sources, evidence, claims = [], [], []
    for f in ANGLES:
        angle = f.stem.split("-")[1]
        for raw in f.read_text().splitlines():
            line = clean(raw)
            m = re.match(r"^([AD]\d-E\d+)\s*\|\s*([AD]\d-S\d+)\s*\|\s*(.*)$", line)
            if m:
                body, _, locator = m[3].rpartition(" | ")
                if not body:
                    body, locator = m[3], ""
                frags = re.findall(r'"([^"]{12,})"', body)
                evidence.append(dict(aid=m[1], asrc=m[2], quote=body.strip(), fragments=frags,
                                     locator=locator.strip(), angle=angle))
                continue
            m = re.match(r"^([AD]\d-C\d+)\s*\|\s*(.*)$", line)
            if m:
                fields = [p.strip() for p in m[2].split(" | ")]
                sup_i = next((i for i, p in enumerate(fields) if p.lower().startswith("support")), None)
                ind_i = next((i for i, p in enumerate(fields) if p.lower().startswith("independent")), None)
                if sup_i is None and len(fields) >= 4:
                    # Unlabelled table row: claim | support | independent | confidence
                    sup_i, ind_i = len(fields) - 3, len(fields) - 2
                text = " | ".join(fields[:sup_i]) if sup_i else fields[0]
                sup_raw = fields[sup_i] if sup_i is not None else ""
                conf = fields[-1] if ind_i is not None and ind_i < len(fields) - 1 else ""
                claims.append(dict(aid=m[1], text=text, support_raw=sup_raw,
                                   support=expand_support(sup_raw, angle),
                                   indep_raw=fields[ind_i] if ind_i is not None else "",
                                   confidence_raw=re.sub(r"^confidence:\s*", "", conf), angle=angle))
                continue
            m = SRC_RE.match(line)
            if m:
                parts = [p.strip() for p in m[2].split(" | ")]
                if len(parts) < 2 or not parts[0].startswith("http"):
                    continue
                url_field = parts[0]
                sources.append(dict(
                    aid=m[1], url_raw=url_field, url=norm_url(url_field),
                    extra=extra_urls(url_field),
                    title=parts[1] if len(parts) > 1 else "",
                    publisher=parts[2] if len(parts) > 2 else "",
                    date=parts[3] if len(parts) > 3 else "",
                    quality=" | ".join(parts[4:]) if len(parts) > 4 else "", angle=angle))
    return sources, evidence, claims


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, a):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def fetch_text(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    key = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if key.exists():
        return key.read_text()
    fetch = url
    m = re.match(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
    if m:
        fetch = f"https://arxiv.org/pdf/{m[1]}"
    gh = re.match(r"https://github\.com/([^/]+/[^/]+)/blob/(.+)", url)
    if gh:
        fetch = f"https://raw.githubusercontent.com/{gh[1]}/{gh[2]}"
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "40", "-A",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36",
             "-o", path, "-w", "%{http_code} %{content_type}", fetch],
            capture_output=True, text=True, timeout=60)
        code, _, ctype = r.stdout.partition(" ")
        data = Path(path).read_bytes()
        if data[:4] == b"%PDF" or "pdf" in ctype:
            t = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True).stdout
        else:
            p = Text()
            p.feed(data.decode("utf-8", "replace"))
            t = html.unescape(" ".join(p.out))
        text = f"__HTTP {code}__\n{t}"
    except Exception as e:  # noqa: BLE001 - record any fetch failure as a gap
        text = f"__ERR {e}__"
    finally:
        os.unlink(path)
    key.write_text(text)
    return text


def norm_text(s):
    s = s.lower()
    s = re.sub(r"[‘’“”`*_]", "", s)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"[^a-z0-9%.]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def score(quote, text):
    q = norm_text(re.sub(r"\[[^\]]*\]|…|\.\.\.", " ", quote))
    t = norm_text(text)
    if not q:
        return 0.0
    if q in t:
        return 1.0
    w = q.split()
    n = 4 if len(w) >= 8 else 2
    grams = [" ".join(w[i:i + n]) for i in range(max(1, len(w) - n + 1))]
    hit = sum(1 for g in grams if g in t)
    return hit / len(grams)


def main():
    no_fetch = "--no-fetch" in sys.argv
    sources, evidence, claims = parse()

    # Global source IDs, deduplicated by normalized URL.
    gid_by_url, gsources, amap = {}, [], {}
    for s in sources:
        if s["url"] not in gid_by_url:
            gid = f"S{len(gsources) + 1}"
            gid_by_url[s["url"]] = gid
            gsources.append(dict(id=gid, url=s["url"], urls_extra=s["extra"], title=s["title"],
                                 publisher=s["publisher"], date=s["date"], quality=s["quality"],
                                 angle_ids=[s["aid"]]))
        else:
            g = next(x for x in gsources if x["id"] == gid_by_url[s["url"]])
            g["angle_ids"].append(s["aid"])
            g["urls_extra"] += [u for u in s["extra"] if u not in g["urls_extra"]]
        amap[s["aid"]] = gid_by_url[s["url"]]
    src_by_id = {g["id"]: g for g in gsources}

    texts = {}
    if not no_fetch:
        urls = {u for g in gsources for u in [g["url"], *g["urls_extra"]]}
        with cf.ThreadPoolExecutor(12) as ex:
            for u, t in zip(urls, ex.map(fetch_text, urls)):
                texts[u] = t

    gevidence = []
    for i, e in enumerate(evidence, 1):
        gid = f"E{i}"
        amap[e["aid"]] = gid
        sid = amap.get(e["asrc"])
        rec = dict(id=gid, source=sid, quote=e["quote"], fragments=e["fragments"],
                   locator=e["locator"], angle_id=e["aid"])
        if texts and sid:
            g = src_by_id[sid]
            bodies = []
            for u in [g["url"], *g["urls_extra"]]:
                t = texts.get(u, "")
                body = t.split("\n", 1)[1] if "\n" in t else ""
                if len(norm_text(body)) >= 400:
                    bodies.append(body)
            if not e["fragments"]:
                rec["fidelity"], rec["fidelity_status"] = None, "paraphrase-only"
            elif not bodies:
                rec["fidelity"], rec["fidelity_status"] = None, "unverifiable (page not machine-readable)"
            else:
                # Worst fragment decides: one invented fragment taints the row.
                best = min(max(score(fr, b) for b in bodies) for fr in e["fragments"])
                rec["fidelity"] = round(best, 2)
                rec["fidelity_status"] = (
                    "verbatim" if best >= 0.95 else "near-verbatim" if best >= 0.75 else
                    "partial" if best >= 0.4 else "not-found")
        gevidence.append(rec)
    ov_path = RUN / "tools" / "overrides.json"
    overrides = json.loads(ov_path.read_text()) if ov_path.exists() else {}
    for e in gevidence:
        o = overrides.get(e["id"])
        if o and e.get("angle_id"):
            e["fidelity_status"], e["fidelity_note"] = o["status"], o["how"]
            if "corrected_url" in o:
                e["corrected_url"] = o["corrected_url"]
    ev_by_id = {e["id"]: e for e in gevidence}

    gclaims = []
    for i, c in enumerate(claims, 1):
        gid = f"C{i}"
        amap[c["aid"]] = gid
        sup = [amap.get(x, x) for x in c["support"]]
        srcs = sorted({ev_by_id[x]["source"] for x in sup if x in ev_by_id})
        pubs = sorted({re.sub(r"\s*\(.*", "", src_by_id[s]["publisher"]).strip().lower() for s in srcs})
        gclaims.append(dict(id=gid, angle_id=c["aid"], text=c["text"], support=sup, sources=srcs,
                            independent_sources_recount=len(pubs), publishers=pubs,
                            independent_sources_worker=c["indep_raw"],
                            confidence_worker=c["confidence_raw"], verdict="unverified"))

    def dump(name, rows):
        with open(RUN / name, "w") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    dump("sources.jsonl", gsources)
    dump("evidence.jsonl", gevidence)
    dump("claims.jsonl", gclaims)
    (RUN / "id-map.json").write_text(json.dumps(amap, indent=1))

    if texts:
        from collections import Counter
        cnt = Counter(e["fidelity_status"] for e in gevidence)
        lines = ["# Quote-fidelity check", "",
                 "Each quote was matched against a raw curl (or pdftotext) fetch of its source,",
                 "independent of WebFetch. Score = share of the quote's word n-grams found in the page.", "",
                 "| status | count |", "| --- | --- |"]
        lines += [f"| {k} | {v} |" for k, v in cnt.most_common()]
        lines += ["", "## Not found or partial", "", "| E | src | angle id | score | quote |", "| - | - | - | - | - |"]
        for e in gevidence:
            if e.get("fidelity_status") in ("not-found", "partial", "paraphrase-only"):
                q = e["quote"][:110].replace("|", "/")
                lines.append(f"| {e['id']} | {e['source']} | {e['angle_id']} | {e['fidelity']} | {q} |")
        lines += ["", "## Unverifiable (page not machine-readable)", ""]
        bad = sorted({e["source"] for e in gevidence if e.get("fidelity_status", "").startswith("unverifiable")},
                     key=lambda s: int(s[1:]))
        lines += [f"- {s} {src_by_id[s]['url']}" for s in bad]
        (RUN / "quote-check.md").write_text("\n".join(lines) + "\n")
        print("\n".join(lines[:14]))
    print(f"sources {len(sources)} -> {len(gsources)} unique; evidence {len(gevidence)}; claims {len(gclaims)}")


if __name__ == "__main__":
    main()
