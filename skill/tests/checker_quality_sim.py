#!/usr/bin/env python3
"""Checker-quality defenses for the v1.1 loop protocol.

The loop protocol sim proved STRUCTURE (termination, conservation, budgets).
This companion proves the three structural defenses against a weak checker:

  D1 SEEDED PROBES   Known-wrong mutants + known-good goldens injected
                     unlabeled into the check stream measure detection
                     live and HALT a garbage checker before labels ship.
  D2 INDEPENDENCE    Unanimity across 3 *independent* checkers cubes the
                     miss rate; 3 *correlated* checkers ~= 1 checker at 3x
                     cost. Shared-miss rate on probes exposes correlation.
  D3 TARGETED AUDIT  Risk-weighted audit slices catch several times more
                     escapes than uniform slices at identical spend.

What this CANNOT prove: that derivation-compare framing beats grading
framing for real LLMs. That is an empirical claim — test it on the golden
set by running both framings against known mutants and comparing measured
detection. The sim would otherwise just assume its own conclusion.
"""

import random

# ---------------------------------------------------------------- D1 ----

def run_with_probe_monitor(det, fp, n_checks=6000, probe_rate=0.05,
                           min_evidence=25, det_floor=0.85, fp_ceiling=0.10,
                           p_wrong=0.30, seed=11):
    """A verification stream with an unlabeled probe monitor.

    Returns (status, checks_done, measured_det, measured_fp,
             garbage_labels_shipped_without_monitor).
    """
    random.seed(seed)
    wrong_probes = wrong_caught = good_probes = good_flagged = 0
    silent_garbage = 0  # wrong real items a monitor-less run would verify
    for i in range(1, n_checks + 1):
        if random.random() < probe_rate:
            if random.random() < 0.5:          # known-wrong mutant
                wrong_probes += 1
                if random.random() < det:
                    wrong_caught += 1
            else:                               # known-good golden
                good_probes += 1
                if random.random() < fp:
                    good_flagged += 1
        else:                                   # real item
            if random.random() < p_wrong and random.random() > det:
                silent_garbage += 1             # escape (wrong -> verified)
        if wrong_probes >= min_evidence and good_probes >= min_evidence:
            mdet = wrong_caught / wrong_probes
            mfp = good_flagged / good_probes
            if mdet < det_floor or mfp > fp_ceiling:
                return ("HALT", i, mdet, mfp, silent_garbage)
    mdet = wrong_caught / max(wrong_probes, 1)
    mfp = good_flagged / max(good_probes, 1)
    return ("COMPLETED", n_checks, mdet, mfp, silent_garbage)


# ---------------------------------------------------------------- D2 ----

def ensemble_escape_rates(marginal_miss=0.10, shared=0.07, trials=200_000,
                          seed=22):
    """Escape rate of a wrong item under three checker configurations.

    Correlated model: with prob `shared` all three share a blind spot and
    miss together; otherwise they miss independently at a residual rate
    chosen so each checker's marginal miss stays `marginal_miss`.
    """
    random.seed(seed)
    resid = (marginal_miss - shared) / (1 - shared)
    single = triple_ind = triple_corr = 0
    shared_miss_ind = shared_miss_corr = 0   # all-three-miss rate on probes
    for _ in range(trials):
        # single checker
        if random.random() < marginal_miss:
            single += 1
        # three independent, unanimity to pass (escape iff all miss)
        ind_all_miss = all(random.random() < marginal_miss for _ in range(3))
        if ind_all_miss:
            triple_ind += 1
            shared_miss_ind += 1
        # three correlated
        if random.random() < shared:
            corr_all_miss = True
        else:
            corr_all_miss = all(random.random() < resid for _ in range(3))
        if corr_all_miss:
            triple_corr += 1
            shared_miss_corr += 1
    t = trials
    return (single / t, triple_ind / t, triple_corr / t,
            shared_miss_ind / t, shared_miss_corr / t)


# ---------------------------------------------------------------- D3 ----

def audit_catch_rates(n_verified=4000, escape_rate=0.012, hi_risk_frac=0.20,
                      escapes_in_hi=0.80, audit_budget=0.10, det_audit=0.97,
                      trials=400, seed=33):
    """Fraction of escapes caught by uniform vs targeted vs split audits,
    at identical audit spend (audit_budget * n_verified checks)."""
    random.seed(seed)
    n_esc = int(n_verified * escape_rate)
    n_hi = int(n_verified * hi_risk_frac)
    budget = int(n_verified * audit_budget)
    catches = {"uniform": 0, "targeted": 0, "split 25/75": 0}
    for _ in range(trials):
        # place escapes: 80% inside the high-risk 20% pool
        esc = set()
        for _ in range(n_esc):
            if random.random() < escapes_in_hi:
                esc.add(random.randrange(0, n_hi))
            else:
                esc.add(random.randrange(n_hi, n_verified))
        def caught(sample):
            return sum(1 for i in sample
                       if i in esc and random.random() < det_audit)
        pop, hi = range(n_verified), range(n_hi)
        catches["uniform"] += caught(random.sample(pop, budget))
        catches["targeted"] += caught(random.sample(hi, min(budget, n_hi)))
        u = budget // 4
        catches["split 25/75"] += caught(random.sample(pop, u)) + \
            caught(random.sample(hi, min(budget - u, n_hi)))
    return {k: v / (trials * n_esc) for k, v in catches.items()}


# -------------------------------------------------------------- main ----

def main():
    print("D1 — Seeded-probe monitor (floor: det>=0.85, fp<=0.10)")
    print(f"  {'true det':>9} {'status':>10} {'decided at':>11} "
          f"{'measured det':>13} {'measured fp':>12} {'garbage w/o monitor':>20}")
    for det, fp in ((0.50, 0.50), (0.70, 0.12), (0.95, 0.03), (0.999, 0.01)):
        status, at, mdet, mfp, garbage = run_with_probe_monitor(det, fp)
        print(f"  {det:>9.3f} {status:>10} {at:>11} {mdet:>12.0%} "
              f"{mfp:>11.0%} {garbage:>20}")
    print("  -> garbage checkers HALT with measured numbers; without the")
    print("     monitor the same runs silently ship the garbage column.\n")

    print("D2 — Ensemble independence (marginal miss 10% per checker)")
    s, ti, tc, smi, smc = ensemble_escape_rates()
    print(f"  single checker escape rate:            {s:6.2%}")
    print(f"  3 independent, unanimity:              {ti:6.2%}")
    print(f"  3 correlated (7% shared blind spot):   {tc:6.2%}")
    print(f"  detectable: all-three-miss rate on wrong probes is "
          f"{smi:.2%} (independent) vs {smc:.2%} (correlated)")
    print("  -> independence cubes detection; clones don't. Correlation")
    print("     shows up directly in shared-miss stats on probes.\n")

    print("D3 — Audit targeting at identical spend "
          "(10% coverage, 80% of escapes in the top-risk 20%)")
    for k, v in audit_catch_rates().items():
        print(f"  {k:>12}: catches {v:6.1%} of escapes")
    print("  -> same budget, several-fold more escapes caught; keep the")
    print("     uniform slice for unbiased measurement, target the rest.\n")

    print("VERDICT: probes convert checker quality from assumed to measured")
    print("and halt garbage runs; independence requirements multiply")
    print("detection; targeted audits multiply escape-catching. The one")
    print("claim left to empirics: derivation-vs-grading framing — run the")
    print("bake-off on your golden set.")


if __name__ == "__main__":
    main()
