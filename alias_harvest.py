#!/usr/bin/env python3
"""
Step 1 - Alias harvest (pure Python, zero tokens).

Frequency-counts every account string in the parsed corpus, clusters
near-duplicates, and PROPOSES a merge into account_aliases.csv.

Proposal only. Nothing is written to the pack unless run with --apply.

Usage:
    python3 alias_harvest.py                    # write the proposal
    python3 alias_harvest.py --apply            # merge into account_aliases.csv
"""

from paths import resolve
import argparse
import csv
import json
import os
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PACK = resolve("pack")
ALIASES = os.path.join(PACK, "account_aliases.csv")

# Wording the textbook treats as noise when matching an account name.
NOISE = re.compile(
    r"\b(to record|to accrue|being|entry|the|a|an|for|of|on|at|and)\b", re.I)
PUNCT = re.compile(r"[^a-z0-9 ]")
SUFFIX = re.compile(r"\s*[-–—]\s*(afs|ts|htm|oci|income|current|noncurrent|"
                    r"net|gross|trading|available for sale|held to maturity)\s*$", re.I)


DASHES = dict.fromkeys(map(ord, "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"), "-")


def canon_key(s):
    """
    Case / dash-family / spacing normaliser, used for SEED MEMBERSHIP only.
    The in-seed column was computed on raw strings, so "Accumulated
    Depreciation-Equipment" read as absent while the em-dash spelling sat in the
    chart. Membership is a different question from whether two spellings may be
    MERGED, which stays strict.
    """
    t = (s or "").translate(DASHES).lower()
    t = re.sub(r"&nbsp;|&#160;|&[a-z]+;|&#\d+;", " ", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def merge_key(s):
    """
    Two spellings may be merged ONLY if they normalise to the same string under
    case, punctuation and whitespace. No stopword removal and no fuzzy
    similarity: the corpus contains 'Patent', 'Patent A', 'Patent B', 'Patent X'
    and 'Patent Alpha' as genuinely different accounts, and folding those
    together would let an entry crediting the wrong patent pass as correct.
    """
    s = PUNCT.sub(" ", (s or "").lower())
    return re.sub(r"\s+", " ", s).strip()


def canon(s):
    s = PUNCT.sub(" ", (s or "").lower())
    s = NOISE.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def base(s):
    """Account family: drop the security/classification qualifier."""
    return SUFFIX.sub("", canon(s)).strip()


def load_seed():
    seed = set()
    p = os.path.join(PACK, "chart_of_accounts.txt")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                seed.add(line)
    return seed


def load_existing_aliases():
    rows = []
    if os.path.exists(ALIASES):
        with open(ALIASES, encoding="utf-8", newline="") as fh:
            rows = [r for r in csv.reader(fh) if r]
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--min-count", type=int, default=2)
    ap.add_argument("--similarity", type=float, default=0.86)
    args = ap.parse_args()

    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8")]

    counts = Counter()
    for q in qs:
        for l in q.get("answer_key") or []:
            a = re.sub(r"\s+", " ", (l.get("account") or "").strip())
            if a:
                counts[a] += 1

    seed = load_seed()
    seed_canon = {canon_key(s) for s in seed}

    # Cluster ONLY on exact normalised equality. Fuzzy similarity merged
    # 'Patent A' into 'Patent' at 0.86, which is a wrong-account error the
    # comparator would then be unable to see.
    groups = defaultdict(list)
    for name, n in counts.items():
        groups[merge_key(name)].append((name, n))
    clusters = list(groups.values())

    # canonical = most frequent spelling; only propose where it adds something
    proposals = []
    for grp in clusters:
        grp.sort(key=lambda x: (-x[1], x[0]))
        canonical, total = grp[0][0], sum(n for _, n in grp)
        variants = [g[0] for g in grp[1:]]
        if total < args.min_count and not variants:
            continue
        in_seed = canon_key(canonical) in seed_canon
        proposals.append({
            "canonical": canonical,
            "occurrences": total,
            "variants": variants,
            "already_in_chart": in_seed,
        })

    proposals.sort(key=lambda p: -p["occurrences"])
    new_names = [p for p in proposals if not p["already_in_chart"]]

    path = os.path.join(OUT, "reports", "alias_proposal.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = [
        "# Alias harvest — PROPOSAL (nothing applied)", "",
        f"- distinct account strings in corpus: **{len(counts)}**",
        f"- total parsed journal lines: **{sum(counts.values())}**",
        f"- seed chart entries: **{len(seed)}**",
        f"- clusters proposed: **{len(proposals)}**",
        f"- of those, NOT already in the seed chart: **{len(new_names)}**",
        "", "Clustering: canonical form = most frequent spelling in the cluster; "
        f"members joined when similarity >= {args.similarity} within an account family "
        "(family = name with its AFS/TS/HTM/OCI-style qualifier removed).", "",
        "## Top 40 proposed canonical accounts", "",
        "| occurrences | canonical | in seed chart | variants folded in |",
        "|---:|---|---|---|",
    ]
    for p in proposals[:40]:
        v = ", ".join(p["variants"][:3]) + (" …" if len(p["variants"]) > 3 else "")
        lines.append(f"| {p['occurrences']} | {p['canonical']} | "
                     f"{'yes' if p['already_in_chart'] else '**no**'} | {v or '—'} |")

    multi = [p for p in proposals if p["variants"]]
    lines += ["", f"## Clusters that actually merge spellings ({len(multi)})", ""]
    for p in multi[:30]:
        lines.append(f"- **{p['canonical']}** ({p['occurrences']})")
        for v in p["variants"][:6]:
            lines.append(f"  - {v}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    with open(os.path.join(OUT, "alias_proposal.json"), "w", encoding="utf-8") as fh:
        json.dump(proposals, fh, indent=1)

    print(f"distinct account strings : {len(counts)}")
    print(f"parsed journal lines     : {sum(counts.values())}")
    print(f"seed chart entries       : {len(seed)}")
    print(f"clusters proposed        : {len(proposals)}  ({len(new_names)} not in seed chart)")
    print(f"clusters merging >1 spelling: {len(multi)}")
    print(f"\nproposal: {path}")

    if args.apply:
        rows = load_existing_aliases()
        have = {r[0].strip().lower() for r in rows if r}
        added = 0
        with open(ALIASES, "a", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            for p in proposals:
                if p["canonical"].lower() in have:
                    continue
                w.writerow([p["canonical"]] + p["variants"])
                added += 1
        print(f"APPLIED: appended {added} rows to {ALIASES}")
    else:
        print("NOT applied. Re-run with --apply once the mapping is approved.")


if __name__ == "__main__":
    main()
