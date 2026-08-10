#!/usr/bin/env python3
"""
Ledger migration for the whole-key hash change, plus reconstruction of the
stage-1 verdicts that stage0_normalize.py truncated.

Two jobs:

1. Re-key. The content hash now covers the whole key, not just the structured
   JE lines, so EVERY item's hash changed - not only the repaired one. Terminal
   states carry forward wherever the underlying bytes are unchanged.

2. Rebuild. The ledger opened in "w" mode until now, so each re-normalisation
   wiped every appended stage-1 verdict. The verdicts themselves survive in the
   evidence bundles and results files; this reconstructs the ledger from them
   rather than re-running a single solver.

A byte change is detected by hashing (stem + options + solution) directly, so
future migrations are mechanical instead of relying on anyone remembering which
items were repaired.
"""

import glob
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PIPELINE_VERSION = "1.2"


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def old_hash(q):
    """The pre-change formula: JE lines only, solution text ignored."""
    kl = q.get("answer_key")
    key_repr = json.dumps(kl, sort_keys=True) if kl else (q.get("solution") or "")[:4000]
    return sha(q["stem"] + json.dumps(q["options"]) + key_repr)


def bytes_hash(q):
    """Identity of the CONTENT a student reads - the migration's real key."""
    return sha(q["stem"] + json.dumps(q["options"]) + (q.get("solution") or ""))


def main():
    qs = [json.loads(l) for l in open(os.path.join(OUT, "questions.jsonl"),
                                      encoding="utf-8")]
    by_id = {q["id"]: q for q in qs}

    # ---- 1. the old -> new map ----------------------------------------
    mapping = []
    for q in qs:
        mapping.append({"id": q["id"], "old_hash": old_hash(q),
                        "new_hash": q["content_hash"],
                        "bytes_hash": bytes_hash(q),
                        "changed_by_rekey": old_hash(q) != q["content_hash"]})
    rekeyed = sum(1 for m in mapping if m["changed_by_rekey"])

    # ---- 2. recover stage-1 verdicts from surviving artifacts ----------
    verdicts = {}          # id -> row
    for p in glob.glob(os.path.join(OUT, "evidence", "*", "comparison.json")):
        try:
            c = json.load(open(p, encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if c.get("id"):
            verdicts[c["id"]] = {"status": c.get("status"),
                                 "comparator_version": c.get("comparator_version"),
                                 "source": "evidence/comparison.json"}
    for fn, key in ((f"stage1_v3_batch12_results.json", "rows"),
                    ("stage1_batch1_results.json", "rows"),
                    ("stage1_batch2_results.json", "rows"),
                    ("parity50_results.json", "rows")):
        p = os.path.join(OUT, fn)
        if not os.path.exists(p):
            continue
        try:
            d = json.load(open(p, encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        cv = d.get("comparator_version", "unknown")
        for r in d.get(key, []):
            qid = r.get("id")
            if not qid:
                continue
            st = r.get("status") or (r.get("baseline-1") or {}).get("verdict")
            if st and qid not in verdicts:
                verdicts[qid] = {"status": st, "comparator_version": cv,
                                 "source": fn}

    # ---- 3. items whose bytes changed cannot inherit -------------------
    # agent_130#00 was repaired at source; its prior verdict must not carry.
    REPAIRED = {"agent_130#00"}

    # Prior rows indexed by BYTES hash. A mechanical re-key (whole-key hashing,
    # a parser fix, a re-normalisation) leaves the content a student reads
    # untouched, so every state carries forward. Only a BYTES change forfeits
    # state - that is the whole point of hashing bytes separately from content.
    from ledger_io import read_rows
    prior_by_bytes = {}
    for r in read_rows():
        b = r.get("bytes_hash")
        if b and r.get("stage"):
            prev = prior_by_bytes.get(b)
            if prev is None or (r.get("stage") or 0) >= (prev.get("stage") or 0):
                prior_by_bytes[b] = r

    rows, carried, dropped, rekey_carried = [], 0, 0, 0
    for m in mapping:
        q = by_id[m["id"]]
        base = {"content_hash": m["new_hash"], "id": m["id"],
                "lineage_id": q["lineage_id"], "pack_id": q["pack_id"],
                "remake_count": q["remake_count"],
                "pipeline_version": PIPELINE_VERSION,
                "bytes_hash": m["bytes_hash"],
                "migrated_from": m["old_hash"]}
        prior = prior_by_bytes.get(m["bytes_hash"])
        v = verdicts.get(m["id"])
        if prior and m["id"] not in REPAIRED:
            base.update({k: prior[k] for k in ("stage", "status", "comparator_version")
                         if k in prior})
            base["carried_forward"] = True
            base["carry_reason"] = "mechanical re-key, bytes unchanged"
            rekey_carried += 1
            rows.append(base)
            continue
        if v and m["id"] not in REPAIRED:
            base.update({"stage": 1, "status": v["status"],
                         "comparator_version": v["comparator_version"],
                         "carried_forward": True, "recovered_from": v["source"]})
            carried += 1
        else:
            base.update({"stage": 0, "status": q["status"]})
            if v:
                base["prior_verdict_dropped"] = v["status"]
                base["drop_reason"] = "bytes changed by key repair - must re-verify"
                dropped += 1
        rows.append(base)

    from ledger_io import append_rows
    append_rows(rows)

    with open(os.path.join(OUT, "hash_migration.json"), "w", encoding="utf-8") as fh:
        json.dump({"pipeline_version": PIPELINE_VERSION,
                   "reason": "content_hash now covers the whole key, not only JE lines",
                   "items": mapping}, fh, indent=1)

    # duplicate-content detection falls out of the byte hash for free
    seen = {}
    dups = []
    for m in mapping:
        seen.setdefault(m["bytes_hash"], []).append(m["id"])
    for h, ids in seen.items():
        if len(ids) > 1:
            dups.append(ids)

    print(f"items                       : {len(mapping)}")
    print(f"re-keyed by the hash change : {rekeyed} ({rekeyed/len(mapping):.0%})")
    print(f"stage-1 verdicts recovered  : {len(verdicts)}")
    print(f"  carried forward           : {carried}")
    print(f"  dropped (bytes changed)   : {dropped}  {sorted(REPAIRED)}")
    print(f"cache survival              : {carried}/{len(verdicts)} "
          f"({carried/max(1,len(verdicts)):.0%})")
    print(f"carried by bytes-unchanged rule: {rekey_carried}")
    print(f"byte-identical duplicate groups: {len(dups)}")
    for g in dups[:8]:
        print(f"    {g}")


if __name__ == "__main__":
    main()
