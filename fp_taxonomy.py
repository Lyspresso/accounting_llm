#!/usr/bin/env python3
"""
Five-way taxonomy for the false-positive floor.

A single FP rate is not actionable. 26.9% against a 10% ceiling could mean the
comparator is broken, or that the goldens are wrong, or that the rate is being
computed across two different versions of the truth. Those have opposite fixes,
and lumping them together is how a gate stays RED without telling you why.

    TRUE_FP         key correct, solver correct, comparator raised anyway.
                    Counts against the ceiling. This is the only class that does.
    GOLDEN_WRONG    the key is the defective party, so the finding was a TRUE
                    positive and the golden that called it clean is wrong.
                    Removing it from the numerator is a correction, not a
                    weakening - but the golden must be repaired, not deleted.
    MATCHER_ARTIFACT the finding traces to a comparator deficiency. Does not
                    count against the ceiling ONLY once the deficiency is fixed
                    and the detection floor is re-measured, because every
                    loosening trades against detection power.
    HASH_MIXING     the verdict was computed across two versions of the truth
                    (golden recorded against a content hash the item no longer
                    carries, or solver output whose provenance is inadmissible).
                    Not a rate at all - an invalid measurement.
    PENDING         not yet adjudicated. Reported, never silently dropped.

KEY-SILENT is the dominant mechanism found here and deserves its own note. The
comparator asks "does this value corroborate against the key's number pool" and,
failing that, "is it a small subset-sum of key figures". If both fail it emits
SOLVER_MISMATCH. But those two questions cannot distinguish

    (a) the key states a figure for this label and the solver's differs
    (b) the key never addresses this label at all

and only (a) is evidence of a wrong answer. Case (b) is a question about
COVERAGE - of the key, or of the solver - and routing it to a hard fail charges
the solver for the key's silence.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)

import canon                      # noqa: E402
import compare_stage1_v3 as C     # noqa: E402
import labelgrammar as G          # noqa: E402
import preflight as PF            # noqa: E402
import provenance as P            # noqa: E402

CLASSES = ("TRUE_FP", "GOLDEN_WRONG", "MATCHER_ARTIFACT", "HASH_MIXING", "PENDING")

# Label words too common to prove the key addresses a label. "value" appears in
# every lease key ever written; it distinguishes nothing.
UNDISTINGUISHING = {
    "total", "amount", "balance", "value", "net", "the", "of", "and", "as", "at",
    "for", "to", "in", "on", "per", "expense", "asset", "liability", "cash",
    "year", "end", "book", "carrying", "schedule", "entry", "after", "before",
    "beginning", "ending", "each", "annual", "amount", "recognized", "reported",
}


# Keys abbreviate. "NI: none." answers a Required part about net income, and a
# silence test that does not expand it reports the key as silent on a part the
# key plainly answers - manufacturing KEY_SILENT wherever the author was terse.
ABBREV = (
    (r"\bNI\b", "net income"), (r"\bOCI\b", "other comprehensive income"),
    (r"\bFVA?\b", "fair value"), (r"\bPV\b", "present value"),
    (r"\bAC\b", "amortized cost"), (r"\bROU\b", "right of use"),
    (r"\bLL\b", "lease liability"), (r"\bNBV\b", "net book value"),
    (r"\bAFS\b", "available for sale"), (r"\bHTM\b", "held to maturity"),
    (r"\bCFO\b", "operating"), (r"\bRE\b", "retained earnings"),
)


def distinguishing_terms(label):
    """
    The words in a label that could show the key is talking about IT.

    The label is expanded through the SAME abbreviation table as the key. It was
    not, and the asymmetry inverted the test: expanding "ROU" to "right of use"
    in the key alone made the label's own "rou" token unfindable, so a key that
    states the figure was reported as silent on it.
    """
    for pat, full in ABBREV:
        label = re.sub(pat, full, label)
    m = G.parse(label).get("measure") or ()
    return {w for w in m if w not in UNDISTINGUISHING and not w.isdigit()
            and len(w) > 2}



STOP_TOK = {"in", "of", "the", "and", "for", "on", "to", "a", "bonds", "bond"}


def _tok(s):
    return {w for w in re.findall(r"[a-z]+", (s or "").lower()) if w not in STOP_TOK}


def aggregation_equivalent(key_lines, solver_lines):
    """
    Is the solver's entry the KEY's entry with lines combined?

    Per side: totals must agree, and every solver amount must be a subset-sum of
    unconsumed key amounts whose accounts each share a token with the solver's.
    The token guard is what keeps this from certifying "Cash 150,000" as
    equivalent to "Investment 150,000" - equal money is not equal accounting.
    """
    import collections
    K, S = collections.defaultdict(list), collections.defaultdict(list)
    for l in key_lines:
        K[l["side"]].append((canon.norm_acct(l["account"]), round(abs(l["amount"]), 2)))
    for l in solver_lines:
        S[l["side"]].append((canon.norm_acct(l["account"]), round(abs(l["amount"]), 2)))
    if set(K) != set(S):
        return False, "sides differ"
    for side in K:
        if abs(sum(a for _, a in K[side]) - sum(a for _, a in S[side])) > 0.01:
            return False, f"{side} totals differ"
        pool = list(K[side])
        for acct, amt in sorted(S[side], key=lambda x: -x[1]):
            cand = [i for i, (ka, _) in enumerate(pool) if _tok(ka) & _tok(acct)]
            got, used = 0.0, []
            for i in sorted(cand, key=lambda i: -pool[i][1]):
                if got + pool[i][1] <= amt + 0.01:
                    got += pool[i][1]
                    used.append(i)
                if abs(got - amt) <= 0.01:
                    break
            if abs(got - amt) > 0.01:
                return False, f"{side} {acct} {amt} not a token-linked subset-sum"
            for i in sorted(used, reverse=True):
                pool.pop(i)
        if pool:
            return False, f"{side} key lines left over: {pool}"
    return True, "aggregation-equivalent: same sides, same totals, token-linked"


def ratio_derivable(value, pool):
    """
    Is the value a RATIO of two figures the key states?

    derivable_from_key does subset-SUMS only. A key that writes
    "PV = $81,911 < 90% x $140,000" states both inputs of a percentage without
    ever writing the percentage, so a solver reporting 58.51% is charged with a
    mismatch against a key that contains its own derivation. Percent, fraction
    and their reciprocals are all checked.
    """
    v = canon.as_number(value)
    if v is None or not pool:
        return None
    p = sorted({x for x in pool if x})
    if len(p) > 60:                      # keep the pair scan bounded
        p = p[:60]
    for a in p:
        for b in p:
            # A divisor of 1 (or of the value itself) "derives" anything. Keys
            # routinely contain a 1, so an unguarded scan certifies every figure
            # as key-derivable and the test stops testing.
            if a is b or not b or abs(b - 1.0) < 0.01 or abs(a - v) < 0.01:
                continue
            for cand, form in ((a / b * 100, "pct"), (a / b, "frac")):
                if abs(cand - a) < 0.01 or abs(cand - b) < 0.01:
                    continue              # degenerate: the "ratio" is an input
                if abs(cand - v) <= max(0.02, abs(v) * 1e-4):
                    return f"{a:,.2f} / {b:,.2f} = {cand:,.4f} ({form})"
    return None


PROSE_NULL = re.compile(
    r"(?:\bNI\b|net income|effect|impact|gain|loss)\s*[:\-]?\s*\*{0,2}"
    r"(none|no effect|nil|zero|\$?0)\b", re.I)


def key_states_null(key_text):
    """The key answered 'none'. A solver reporting 0 agrees with that."""
    return bool(PROSE_NULL.search(canon.delatex(key_text or "")))


def key_posts_account(q, account):
    """
    Does any of the KEY's journal-entry lines name this account?

    Scanning the whole key text instead answered the wrong question: an account
    can appear in a balance-sheet schedule and never be posted, which is exactly
    the gap worth finding.
    """
    want = _tok(canon.norm_acct(account))
    if not want:
        return True
    for l in C.key_lines_of(q):
        if want <= _tok(canon.norm_acct(l["account"])):
            return True
    return False


def key_addresses_label(label, key_text):
    """
    Does the key discuss this label at all?

    Requires EVERY distinguishing term to appear (synonyms allowed). A label
    with no distinguishing terms is treated as addressed - the conservative
    direction, since an unproven silence must not excuse a real mismatch.
    """
    terms = distinguishing_terms(label)
    if not terms:
        return True, "no distinguishing terms - treated as addressed"
    # G.SYN is a (pattern, canonical) tuple list: normalise the KEY through it,
    # so an abbreviation in the key satisfies the full word in the label.
    kt = canon.delatex(key_text or "")
    for pat, full in ABBREV:                 # expand BEFORE lowercasing: NI/OCI
        kt = re.sub(pat, full, kt)           # are case-bearing abbreviations
    kt = kt.lower()
    for pat, full in G.SYN:
        kt = re.sub(pat, full, kt, flags=re.I)
    missing = [t for t in terms if not re.search(rf"\b{re.escape(t)}", kt)]
    if missing:
        return False, f"key never mentions {sorted(missing)}"
    return True, "key discusses every distinguishing term"


def classify(qid, finding, q, golden, prov_ok, repaired_keys):
    """(class, reason). Evidence-driven; PENDING when nothing decides it."""
    key_text = q.get("solution", "") or ""
    label = str(finding.get("label") or "")

    if not prov_ok:
        return "HASH_MIXING", "solver output inadmissible (provenance)"
    if golden.get("truth_as_of_hash") and golden["truth_as_of_hash"] != q["content_hash"]:
        return "HASH_MIXING", "golden recorded against a superseded content hash"
    if qid in repaired_keys:
        return "GOLDEN_WRONG", f"key repaired at source: {repaired_keys[qid]}"

    if finding["kind"] == "SOLVER_MISMATCH":
        addressed, why = key_addresses_label(label, key_text)
        if not addressed:
            return "MATCHER_ARTIFACT", f"KEY_SILENT hard-failed - {why}"
        v = canon.as_number(finding.get("solver"))
        pool = canon.nums(canon.delatex(key_text))
        if v == 0 and key_states_null(key_text):
            return ("MATCHER_ARTIFACT",
                    "key answers 'none'; prose-null not recognised for this wording")
        near = sorted(pool, key=lambda x: abs(x - v))[:1] if (v and pool) else []
        if near and 0 < abs(near[0] - v) <= max(2.0, abs(v) * 1e-5):
            return ("MATCHER_ARTIFACT",
                    f"rounding: key {near[0]:,.2f} vs solver {v:,.2f} (delta "
                    f"{abs(near[0]-v):.2f}) inside compounded-rounding range")
        rd = ratio_derivable(v, pool)
        if rd:
            return ("MATCHER_ARTIFACT",
                    f"ratio-derivable from key figures: {rd}; "
                    f"derivable_from_key is sum-only")
        near = sorted(pool, key=lambda x: abs(x - v))[:1] if (v and pool) else []
        if near and 0 < abs(near[0] - v) <= max(2.0, abs(v) * 1e-5):
            return ("MATCHER_ARTIFACT",
                    f"rounding: key {near[0]} vs solver {v} (delta "
                    f"{abs(near[0]-v):.2f}) inside compounded-rounding range")
        return "PENDING", "key addresses the label and the figures differ"

    if finding["kind"] in ("JE_LINE_NOT_IN_KEY", "KEY_LINE_NOT_IN_SOLVER"):
        agg, why = aggregation_equivalent(C.key_lines_of(q), finding["_solver_lines"])
        if agg:
            return "MATCHER_ARTIFACT", f"{why} (needs an alias ruling to clear)"
        # the solver posted an entry the key has no counterpart for. If a
        # Required part demands that the entry exist, the KEY is the party at
        # fault - the pipeline found a gap, which is a true positive.
        acct = str(finding.get("solver") or "")
        req = re.search(r"\*\*Required.*", canon.delatex(q.get("stem", "")), re.S)
        demanded = bool(req) and bool(re.search(
            r"all balance sheet account changes|every .{0,24}account",
            req.group(0), re.I))
        if finding["kind"] == "JE_LINE_NOT_IN_KEY" and demanded and acct:
            if acct and not key_posts_account(q, acct):
                return ("GOLDEN_WRONG",
                        f"Required demands entries for every account change, but "
                        f"the key never posts '{acct[:40]}'")
        return "PENDING", f"JE line-level unresolved: {why}"
    return "PENDING", "unclassified kind"


def load_repairs():
    """Keys repaired at source. These make their goldens wrong, not the pipeline."""
    p = os.path.join(OUT, "key_repairs.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    return {}


def main():
    qs, known, amap = PF.load()
    dv = PF.dual_verified()
    repaired = load_repairs()
    par = {e["id"]: e["dir"] for e in
           json.load(open(os.path.join(OUT, "parity50.json"), encoding="utf-8"))}
    gold_dir = os.path.join(HERE, "goldens")

    rows, tally = [], {c: 0 for c in CLASSES}
    inadmissible = []
    item_class, clean = {}, 0
    for fn in sorted(os.listdir(gold_dir)):
        if not fn.endswith(".json") or fn == "INDEX.json":
            continue
        g = json.load(open(os.path.join(gold_dir, fn), encoding="utf-8"))
        qid = g["id"]
        q = qs.get(qid)
        if not q or g.get("expected_verdict") != "PASS":
            continue
        src, why_src = P.evidence_dir(qid, q)
        if src is None:
            inadmissible.append((qid, why_src))
            continue
        sp = os.path.join(src, "solver_output.json")
        pp = os.path.join(src, "provenance.json")
        prov = json.load(open(pp, encoding="utf-8")) if os.path.exists(pp) else None
        prov_ok = True
        clean += 1
        sol = json.load(open(sp, encoding="utf-8"))
        iss, _ = C.compare(sol, q, known, amap)
        hard = [i for i in iss if i["kind"] in C.HARD
                and (qid, str(i.get("label") or "").strip().lower()) not in dv]
        if not hard:
            continue
        cls_here = []
        slines = C.solver_lines(sol)
        for f in hard:
            f["_solver_lines"] = slines
            cls, why = classify(qid, f, q, g, prov_ok, repaired)
            tally[cls] += 1
            cls_here.append(cls)
            rows.append({"id": qid, "kind": f["kind"],
                         "label": str(f.get("label") or "")[:70],
                         "class": cls, "reason": why})
        # an item counts against the ceiling only if SOME finding is chargeable
        chargeable = [c for c in cls_here if c in ("TRUE_FP", "PENDING")]
        item_class[qid] = ("CHARGEABLE" if chargeable else
                           sorted(set(cls_here))[0])

    print("=== FALSE-POSITIVE FLOOR: FIVE-WAY TAXONOMY ===\n")
    print(f"clean goldens scored : {clean}")
    if inadmissible:
        print(f"EXCLUDED, no admissible evidence : {len(inadmissible)}")
        for qid, w in inadmissible:
            print(f"    {qid:14s} {w}")
    print(f"goldens with >=1 hard finding : {len(item_class)}\n")
    print("findings by class:")
    for c in CLASSES:
        print(f"  {c:18s} {tally[c]:>4}")
    print(f"  {'TOTAL':18s} {sum(tally.values()):>4}\n")

    charge = sum(1 for v in item_class.values() if v == "CHARGEABLE")
    lo, hi = PF.wilson(charge, clean)
    print(f"chargeable ITEMS (TRUE_FP or PENDING findings) : {charge}/{clean}")
    print(f"  chargeable rate {charge / max(1, clean):.1%}   "
          f"95% CI [{lo:.1%}, {hi:.1%}]   ceiling {PF.PROBE_FP_CEILING:.0%}")
    print(f"  -> floor #2 {'PASSES' if hi <= PF.PROBE_FP_CEILING else 'FAILS'} "
          f"on the upper bound\n")
    print("NOTE: MATCHER_ARTIFACT findings are EXCLUDED from the numerator above.")
    print("      That exclusion is only honest once each artifact is FIXED and")
    print("      the detection floor is re-measured - every loosening of the")
    print("      comparator trades against detection power. Until then the")
    print("      chargeable rate is a FORECAST, not a measurement.\n")

    print("per-finding detail:")
    for r in rows:
        print(f"  {r['id']:14s} {r['class']:17s} {r['kind']:22s} "
              f"{r['label'][:44]:44s} {r['reason'][:60]}")
    for qid, v in sorted(item_class.items()):
        print(f"    item {qid:14s} -> {v}")

    json.dump({"clean": clean, "findings": rows, "tally": tally,
               "item_class": item_class, "chargeable": charge,
               "chargeable_ci": [lo, hi],
               "caveat": "MATCHER_ARTIFACT excluded; forecast until fixed and "
                         "detection re-measured"},
              open(os.path.join(OUT, "fp_taxonomy.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(OUT, 'fp_taxonomy.json')}")


if __name__ == "__main__":
    main()
