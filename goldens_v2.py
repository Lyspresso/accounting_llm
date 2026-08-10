#!/usr/bin/env python3
"""
Goldens v2 — truth-versioned, provenance-tiered, regression-wired.

Three changes:

1. truth_as_of_hash. A golden records the content hash it was verified against.
   Scoring a golden whose content has since moved is what produced the phantom
   false-negative on agent_130#00: its truth was recorded pre-repair and scored
   post-repair. A hash mismatch now downgrades the golden to `stale` instead of
   reporting a defect that no longer exists.

2. Provenance tiers: human_confirmed > ai_cross_checked > adjudicated. Only
   countersigned=true items reach the top tier, and only the top tier certifies
   floor #2.

3. Regression wiring. Every ruling to date names the comparator rule it forced
   into existence, so probe suite v2 can assert the rule still holds. A rule
   with no golden guarding it is a rule that can silently regress.
"""

from paths import resolve
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
GOLD = os.path.join(HERE, "goldens")
VERDICTS = resolve("verdicts")

# id -> (tier, expected_verdict, guards_rule, rationale)
# expected_verdict is what a CORRECT comparator must return for this content.
RULINGS = {
    # ---- ch17 lease cohort: zero genuine accounting disagreements ----
    "agent_022#01": ("adjudicated", "PASS", None, "clean; NON_NUMERIC_ANSWER only"),
    "agent_019#00": ("adjudicated", "PASS", "latex_number_extraction",
                     "key states figures in LaTeX prose"),
    "agent_285#00": ("adjudicated", "PASS", "header_driven_je_extraction",
                     "parser lifted a 4-line optional-form table as the whole key"),
    "agent_151#01": ("adjudicated", "PASS", "rounding_context_scope",
                     "$0.86/$1.35 round-then-carry in an ROU rollforward"),
    "agent_283#02": ("adjudicated", "PASS", "rounding_context_scope",
                     "$0.65 same convention pair"),
    "agent_150#02": ("adjudicated", "PASS", "key_silent_derived",
                     "key declines to state Option 3 PV; solver correct"),
    # ---- parity flips ----
    "agent_002#03": ("adjudicated", "PASS", "je_aggregation_equivalence",
                     "pooled 150,000 vs key's 90,000+60,000 split"),
    "agent_032#01": ("ai_cross_checked", "PASS", "latex_number_extraction",
                     "key states 18,000 in LaTeX the old extractor split"),
    "agent_303#02": ("ai_cross_checked", "FAIL", "stem_ambiguity",
                     "stem underdetermines the refund-liability identity"),
    "agent_043#00": ("ai_cross_checked", "PASS", "rounding_context_scope",
                     "round-then-carry vs carry-then-plug, both close to face"),
    "agent_053#01": ("ai_cross_checked", "PASS", "reporting_volume_invariance",
                     "order-dependent downgrade manufactured the flip"),
    "agent_107#02": ("ai_cross_checked", "PASS", "percent_fraction_units",
                     "0.72/0.28 vs key's 72/28"),
    # CORRECTED. This was recorded as a solver treatment error. It was not: the
    # trim harness carried no LO 11-8 rule at all while the dual harness did, so
    # the two solvers were answering under different instructions and the split
    # was manufactured by the instrument. Re-derived symmetrically (both prompts
    # from build_solver_prompt, note present in both): 12/12 shared figures
    # agree, and the comparator returns ZERO findings against 13 key lines for
    # BOTH derivations. The item is clean and always was.
    "agent_204#02": ("ai_cross_checked", "PASS", "solver_context_symmetry",
                     "asymmetric prompts manufactured the split; symmetric "
                     "re-derivation agrees and matches the key exactly"),
    "agent_333#02": ("ai_cross_checked", "PASS", "prose_null_zero",
                     "solver 0 IS the key's 'No journal entry'"),
    "agent_268#00": ("ai_cross_checked", "PASS", "prose_null_zero",
                     "solver 0 IS the key's 'No entry'"),
    # ---- key repair, re-goldened POST-repair ----
    # CORRECTED to FAIL. The T-account repair fixed one defect and the golden was
    # rewritten as clean, but a SECOND defect survives in the same key: Required
    # (b) demands entries explaining "all balance sheet account changes", the
    # key's own schedule shows Restricted cash rising 15,000 -> 25,000, and none
    # of the key's 26 entry lines posts Restricted Cash. A comparator that flags
    # this is right, so a golden calling it clean makes the pipeline look wrong
    # for being correct. Repair is PROPOSED, not applied - see
    # out/key_repair_proposals.json.
    # REPAIRED and re-pinned post-repair, per ORDER-002 item 3 (per-item approval
    # for THIS item only). Entry (k) - Dr Restricted Cash / Cr Cash and Cash
    # Equivalents - was added to the source pack, so the key now answers its own
    # Required (b). The hash moved; this golden pins the REPAIRED content. The
    # defect was real: `key_completeness_vs_required` upgrades D10 from
    # KEY_SILENT to key incompleteness.
    "agent_130#00": ("ai_cross_checked", "PASS", "key_completeness_vs_required",
                     "restricted-cash reclass entry added; key now answers its "
                     "own Required (b)"),
    # ---- trim A/B ----
    "agent_052#01": ("adjudicated", "PASS", "key_silent_derived",
                     "FIFO/LIFO running balances correct from the key's own layers"),
}


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    os.makedirs(GOLD, exist_ok=True)
    qs = {q["id"]: q for q in (json.loads(l) for l in
          open(os.path.join(OUT, "questions.jsonl"), encoding="utf-8"))}

    cross = {}
    if os.path.exists(VERDICTS):
        v = json.load(open(VERDICTS, encoding="utf-8"))
        for it in v["items"]:
            cross[it["id"]] = it

    # add the 10 clean machine_passed items from the cross-check as goldens too:
    # a false-positive floor needs confirmed-clean items, not just contested ones
    for qid, it in cross.items():
        if qid not in RULINGS and it["cross_check_verdict"] == "pass":
            RULINGS[qid] = ("ai_cross_checked", "PASS", "corroboration_not_waving_through",
                            it.get("evidence", "")[:160])

    written, by_tier, by_rule = 0, {}, {}
    for qid, (tier, expected, rule, why) in RULINGS.items():
        q = qs.get(qid)
        if not q:
            continue
        x = cross.get(qid, {})
        countersigned = bool(x.get("countersigned"))
        eff_tier = "human_confirmed" if countersigned else tier
        g = {
            "id": qid,
            "pack_id": q["pack_id"],
            "provenance_tier": eff_tier,
            "countersigned": countersigned,
            "countersign_priority": x.get("countersign_priority"),
            "expected_verdict": expected,
            "guards_rule": rule,
            "rationale": why,
            # truth-versioning: this golden is only valid for THIS content
            "truth_as_of_hash": q["content_hash"],
            "truth_as_of_bytes": sha(q["stem"] + json.dumps(q["options"])
                                     + (q.get("solution") or "")),
            "adjudicated_on": "2026-08-07",
            "comparator_version_at_truth": "3.6",
            "cross_check_finding_class": x.get("finding_class"),
            "cross_check_evidence": x.get("evidence"),
        }
        with open(os.path.join(GOLD, f"{qid.replace('#', '_')}.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(g, fh, indent=1)
        written += 1
        by_tier[eff_tier] = by_tier.get(eff_tier, 0) + 1
        if rule:
            by_rule.setdefault(rule, []).append(qid)

    with open(os.path.join(GOLD, "INDEX.json"), "w", encoding="utf-8") as fh:
        json.dump({"count": written, "by_tier": by_tier,
                   "rules_guarded": {k: v for k, v in by_rule.items()}}, fh, indent=1)

    print(f"goldens written : {written}")
    for t, n in sorted(by_tier.items(), key=lambda kv: -kv[1]):
        print(f"   {t:20s} {n}")
    print(f"\nexpected PASS   : {sum(1 for r in RULINGS.values() if r[1]=='PASS')}")
    print(f"expected FAIL   : {sum(1 for r in RULINGS.values() if r[1]=='FAIL')}")
    print(f"\nrules guarded by at least one regression golden: {len(by_rule)}")
    for rule, ids in sorted(by_rule.items()):
        print(f"   {rule:34s} {len(ids)}  {ids[:3]}")
    unguarded = {"prose_null_zero", "percent_fraction_units", "rounding_context_scope",
                 "latex_number_extraction", "je_aggregation_equivalence",
                 "header_driven_je_extraction", "key_silent_derived",
                 "reporting_volume_invariance", "whole_key_content_hash"} - set(by_rule)
    print(f"\nrules with NO golden guarding them: {sorted(unguarded) or 'none'}")


if __name__ == "__main__":
    main()
