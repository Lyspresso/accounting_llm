#!/usr/bin/env python3
"""
canon — the single canonicalization library.

Every canonicalization rule lives here exactly once, and the comparator, the
dual scorer and the probe generator all import it. No scorer reimplements
comparison: the dual scorer drifted from the comparator on two rules within an
hour of being written (it hard-coded 2-decimal precision, and it had no
period-factor rule at all), and each drift showed up as a fabricated finding.

Rules, each traceable to the ruling that forced it:
  precision inheritance   - corroborate at the key's DISPLAYED precision
  rounding context        - round-then-carry equivalence inside rollforwards
  percent <-> fraction    - 0.72 and 72 are one answer when framed as a rate
  prose null              - "no entry" corroborates a reported 0
  aggregation equivalence - a pooled leg equals the key's split legs
  period/unit             - figures related by a whole period factor are the
                            same rate, not a disagreement
  latex normalisation     - keys write money as \\mathbf{\\$18{,}000}
"""

import re

# ---------------------------------------------------------------- constants

MONEY_FLOOR = 100.0     # at/above this a figure is treated as money
RATIO_REL = 0.005       # +/-0.5% on ratios and percentages
MONEY_ABS = 1.0         # per-period rounding allowance inside schedules
PERIOD_FACTORS = (2, 3, 4, 6, 12)

NUM = re.compile(r"-?\$?\s*\d[\d,]*(?:\.\d+)?")

LATEX = (("{,}", ","), ("{.}", "."), ("\\$", "$"), ("\\,", ""),
         ("\\ ", " "), ("~", " "))
LATEX_WRAP = re.compile(r"\\(?:mathbf|mathrm|text|bf|textbf)\{([^{}]*)\}")

# LOOSENING 1 of 4 (ORDER-002 item 5). A key answers a "what was the effect"
# part by naming the measure and saying none of it: "NI: none.", "Effect on net
# income: $0", "no gain or loss". A solver reporting 0 AGREES with that, and the
# pattern below previously only recognised the entry-level phrasings, so the
# agreement was scored as a mismatch.
#
# Deliberately NOT a bare "none": the word must be bound to a MEASURE (an
# effect/impact/gain/loss, or an explicit abbreviation the keys use) or to an
# entry phrase. An unbound "none" appears in prose that has nothing to do with
# the figure being checked, and matching it would let any zero pass anywhere.
_NULL_WORD = r"(?:none|nil|zero|no effect|no impact|\$?0(?:\.00)?)"
_MEASURE = (r"(?:\bNI\b|\bOCI\b|net income|comprehensive income|effect|impact|"
            r"gain(?: or loss)?|loss|adjustment|change)")
PROSE_NULL = re.compile(
    r"\b(no entry|no journal entry|none required|not required|"
    r"no adjusting entry|no entry is (?:made|required))\b"
    rf"|{_MEASURE}\s*(?:on [\w\s]{{0,24}})?[:\-—]?\s*\*{{0,2}}{_NULL_WORD}\b"
    rf"|\bno\s+{_MEASURE}\b", re.I)

# Deepest chain of independently-rounded components the edition actually builds
# inside one rollforward line: a remeasured ROU asset is (opening PV, less k
# rounded amortisation postings, plus a rounded remeasurement), which bottoms
# out at three rounding points in the observed corpus. Three is the measured
# depth, not a comfort margin - raising it without a worked example is how a
# tolerance becomes a blindfold.
ROUND_CHAIN_MAX = 3

PCT_LABEL = re.compile(r"percent|percentage|\bratio\b|\brate\b|%", re.I)

# Scoped by CONTEXT, not chapter: the edition rounds to whole dollars in journal
# entries while running PVs at full precision, and says so, inside any
# period-by-period rollforward.
SCHEDULE_CTX = re.compile(
    r"amorti[sz]ation schedule|amorti[sz]ation table|effective[- ]interest|"
    r"net investment schedule|discount amorti[sz]ation|premium amorti[sz]ation|"
    r"lease liability|right[- ]of[- ]use|\bROU\b|sale[- ]leaseback|"
    r"carrying amount .{0,40}(schedule|rollforward|roll[- ]forward)|"
    r"(schedule|rollforward|roll[- ]forward) .{0,40}carrying amount",
    re.I)

ACCT_PUNCT = re.compile(r"[^a-z0-9 ]")


# ---------------------------------------------------------------- primitives

def delatex(text):
    t = text or ""
    for a, b in LATEX:
        t = t.replace(a, b)
    return LATEX_WRAP.sub(r"\1", t)


def as_number(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip()
    if NUM.fullmatch(s):
        try:
            return float(s.replace("$", "").replace(",", ""))
        except ValueError:
            return None
    return None


def nums(text):
    out = set()
    for m in NUM.finditer(delatex(text)):
        try:
            out.add(round(abs(float(m.group(0).replace("$", "").replace(",", ""))), 2))
        except ValueError:
            pass
    return out


def num_precision(text):
    """value -> decimals the key DISPLAYS it with."""
    prec = {}
    for m in NUM.finditer(delatex(text)):
        raw = m.group(0).replace("$", "").replace(",", "").strip()
        try:
            v = round(abs(float(raw)), 2)
        except ValueError:
            continue
        d = len(raw.split(".")[1]) if "." in raw else 0
        prec[v] = max(prec.get(v, 0), d)
    return prec


def is_schedule_context(*texts):
    return bool(SCHEDULE_CTX.search(" ".join(t or "" for t in texts)))


def precision_tol(key_value, decimals, schedule, label=""):
    if re.search(r"per[- ]share|per[- ]unit|eps\b", label or "", re.I):
        return 0.005
    if abs(key_value) < MONEY_FLOOR:
        return max(0.005, abs(key_value) * RATIO_REL)
    if schedule:
        # LOOSENING 2 of 4 (ORDER-002 item 5), scoped by D7.
        #
        # Inside a rollforward the edition rounds each posted figure to whole
        # dollars while the underlying PV runs at full precision, so a key
        # figure assembled from k independently-rounded components can sit up to
        # 0.5*k away from a full-precision solver. A flat sub-dollar tolerance
        # calls that a mismatch, which is how a blessed convention pair (D7)
        # came to be charged against the false-positive floor.
        #
        # The bound is DERIVED, not chosen: 0.5 per rounding point, and the
        # chain depth is capped at ROUND_CHAIN_MAX so this can never become a
        # general-purpose "money is approximate" rule. Outside a schedule
        # context nothing changes at all.
        return max(MONEY_ABS, 0.5 * ROUND_CHAIN_MAX)
    if decimals == 0:
        return 0.5
    return 10 ** (-decimals) / 2 + 1e-9


def tol_for(value, prec, schedule, label=""):
    """Tolerance for a solver figure against the nearest key figure."""
    v = abs(value)
    near = min(prec, key=lambda k: abs(k - v)) if prec else None
    dec = prec.get(near, 2) if near is not None else 2
    return precision_tol(v, dec, schedule, label)


PERIOD_WORD = re.compile(r"month|quarter|semi[- ]?annual|annual|year|week|day", re.I)


def period_factor_pair(v1, v2, label_a="", label_b=""):
    """
    True when two figures are the same rate stated over different periods.

    Guarded: cumulative-vs-first-year ratios inside a schedule are 2, 3, 4 -
    indistinguishable from semiannual/quarterly factors - so an unguarded
    version EXEMPTED genuine mis-pairings as "unit differences" and hid the one
    real signal on a 5-year schedule (ratio 5, not a period factor, never
    raised). The exemption now requires the two labels to actually disagree
    about period granularity.
    """
    if not v1 or not v2:
        return False
    r = abs(v2) / abs(v1)
    if not any(abs(r - f) < 1e-6 or abs(r - 1 / f) < 1e-6 for f in PERIOD_FACTORS):
        return False
    if label_a or label_b:
        pa = {m.group(0).lower() for m in PERIOD_WORD.finditer(label_a or "")}
        pb = {m.group(0).lower() for m in PERIOD_WORD.finditer(label_b or "")}
        if pa == pb:
            return False        # same granularity -> this is a mis-pairing
    return True


def corroborates(value, pool, key_text="", label="", schedule=False, prec=None):
    """
    The single corroboration test. Every caller uses this - a second
    implementation is how the dual scorer invented findings.
    """
    n = as_number(value)
    if n is None:
        return True
    n = round(abs(n), 2)
    prec = prec if prec is not None else num_precision(key_text)
    for k in pool:
        if abs(k - n) <= precision_tol(k, prec.get(k, 2), schedule, label):
            return True
    if n == 0 and PROSE_NULL.search(delatex(key_text)):
        return True
    if 0 < n <= 1 and PCT_LABEL.search(f"{label} {key_text[:400]}"):
        scaled = n * 100
        for k in pool:
            if abs(k - scaled) <= precision_tol(k, prec.get(k, 2), schedule, label):
                return True
    # NO cross-magnitude corroboration. A thousands/millions rescale block was
    # carried over from an early draft and it falsely corroborated a solver's
    # 900 against a key figure of 0.9 - three orders of magnitude apart - which
    # silently turned three failing items into passes. This corpus states full
    # dollar amounts; a figure that only matches after rescaling does not match.
    return False


def derivable_from_key(value, pool, max_terms=3, schedule=False, label=""):
    """Small-subset sum over figures the key itself states. Bounded, no free-form."""
    v = as_number(value)
    if v is None:
        return None
    v = round(abs(v), 2)
    # Quotients are tried FIRST and independently of the subset-sum candidate
    # filter. That filter keeps only pool values <= v, which is right for sums
    # and exactly wrong for ratios: the inputs of a percentage are almost always
    # LARGER than the percentage, so the early return below made the quotient
    # branch unreachable for every case it was written to catch.
    r = ratio_derivable(v, pool)
    if r:
        return [r]

    cand = sorted(x for x in pool if 0 < x <= v + 1)
    if not cand:
        return None
    t = precision_tol(v, 2, schedule, label)
    for i in range(len(cand)):
        if abs(cand[i] - v) <= t:
            continue
        for j in range(i + 1, len(cand)):
            s2 = cand[i] + cand[j]
            if abs(s2 - v) <= t:
                return [cand[i], cand[j]]
            if max_terms >= 3 and s2 < v:
                for k in range(j + 1, len(cand)):
                    if abs(s2 + cand[k] - v) <= t:
                        return [cand[i], cand[j], cand[k]]

    # LOOSENING 4 of 4 (ORDER-002 item 5): QUOTIENTS of key-stated inputs.
    #
    # This function was sums-only, so a key that writes both inputs of a ratio -
    # a present value and the fair value it is tested against - and never writes
    # the quotient charged the solver with a mismatch against a key containing
    # its own derivation.
    #
    # Guarded exactly like the subset-sum, and the guards are the whole point: a
    # divisor of 1 "derives" anything, keys routinely contain a 1, and an
    # unguarded quotient scan would certify every figure as key-derivable and
    # stop testing. Divisors within 0.01 of 1 are skipped, and a "ratio" equal
    # to one of its own inputs is rejected as degenerate.
    return None


# Security-unqualified paid-in-capital forms. These name no security, so the
# account is context-dependent: the same string is a Common Stock APIC in one
# entry and a Preferred Stock APIC in another. Folding them unconditionally to
# —Common Stock is right by dominance but wrong in a preferred context.
UNQUALIFIED_APIC = re.compile(
    r"^\s*(paid.?in capital in excess of par|additional paid.?in capital|"
    r"share premium)\s*$", re.I)
PREFERRED_SIGNAL = re.compile(r"preferred", re.I)
APIC_DEFAULT = "Paid-in Capital in Excess of Par—Common Stock"


def resolve_contextual(account, entry_accounts=(), part_text=""):
    """
    (resolved_name, suspended, why) for context-dependent account forms.

    Applied UNIFORMLY to every unqualified form, not just the bare one - a rule
    that covered only some of them would leave the others silently mis-folded.
    Default is the dominant form; a preferred-stock signal in the same entry or
    in the part text SUSPENDS the fold and flags for adjudication rather than
    guessing.
    """
    if not UNQUALIFIED_APIC.match(account or ""):
        return (account, False, "")
    ctx = " ".join(list(entry_accounts) + [part_text or ""])
    if PREFERRED_SIGNAL.search(ctx):
        return (account, True,
                "unqualified paid-in-capital form in a preferred context - "
                "fold suspended, needs adjudication")
    return (APIC_DEFAULT, False, "unqualified form folded to the dominant security")


def net_per_account(lines, scope_key=lambda l: l.get("date")):
    """
    Within ONE entry/date, an account appearing on both dr and cr collapses to
    its net line. Demo 17-3 presents the same year-end operating entry two ways
    and prefers neither: the compound form credits ROU 31,721 while the two-part
    form debits ROU 3,251 and credits 34,972. Identical ledgers; only netting
    makes them compare equal.

    SCOPED: netting spans one entry/date only. Netting across an item would
    collapse genuinely separate entries and hide a real error.
    """
    from collections import defaultdict
    buckets = defaultdict(lambda: defaultdict(float))
    order = {}
    for l in lines:
        k = scope_key(l)
        a = norm_acct(l.get("account"))
        buckets[k][a] += (abs(l["amount"]) if l["side"] == "dr" else -abs(l["amount"]))
        order.setdefault((k, a), l)
    out = []
    for k, accts in buckets.items():
        for a, net in accts.items():
            if abs(net) < 0.005:
                continue                 # fully offsetting: no net line
            src = order[(k, a)]
            out.append({"date": k, "account": src.get("account"),
                        "side": "dr" if net > 0 else "cr",
                        "amount": round(abs(net), 2), "part": src.get("part")})
    return out


def norm_acct(a):
    return re.sub(r"\s+", " ", ACCT_PUNCT.sub(" ", (a or "").lower())).strip()


import labelgrammar as G  # noqa: E402  (structured label parser; stdlib-only)


# ---------------------------------------------------------------------------
# KEY-SILENCE TEST (shared)
# ---------------------------------------------------------------------------
# Lives here, not in the taxonomy, because the COMPARATOR needs it too: it must
# distinguish "the key states a figure for this label and the solver's differs"
# (a mismatch) from "the key never addresses this label at all" (a coverage
# question). Charging the second to the solver is charging it for the key's
# silence. Two copies of this rule would drift, and this project has already
# paid that bill twice.

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


def ratio_derivable(value, pool):
    """
    Is the value a RATIO of two figures the key states?

    derivable_from_key does subset-SUMS only. A key that writes
    "PV = $81,911 < 90% x $140,000" states both inputs of a percentage without
    ever writing the percentage, so a solver reporting 58.51% is charged with a
    mismatch against a key that contains its own derivation. Percent, fraction
    and their reciprocals are all checked.
    """
    v = as_number(value)
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


# NOTE: the taxonomy used to carry its own narrower PROSE_NULL here. Two
# definitions of one pattern in one module is not a near-miss - the later one
# silently replaced the loosening-1 pattern above and a canon fixture caught it
# within the minute. One definition, at the top.


def key_states_null(key_text):
    """The key answered 'none'. A solver reporting 0 agrees with that."""
    return bool(PROSE_NULL.search(delatex(key_text or "")))


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
    kt = delatex(key_text or "")
    for pat, full in ABBREV:                 # expand BEFORE lowercasing: NI/OCI
        kt = re.sub(pat, full, kt)           # are case-bearing abbreviations
    kt = kt.lower()
    for pat, full in G.SYN:
        kt = re.sub(pat, full, kt, flags=re.I)
    missing = [t for t in terms if not re.search(rf"\b{re.escape(t)}", kt)]
    if missing:
        return False, f"key never mentions {sorted(missing)}"
    return True, "key discusses every distinguishing term"


