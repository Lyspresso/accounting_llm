# Applied alias rows — for the record

Applied to `/Users/lyspressopro/Downloads/question-verifier/pack/account_aliases.csv`.

## A. Case/punctuation merge clusters (36)

| canonical | variants folded in | occurrences |
|---|---|---:|
| Interest Expense | Interest expense | 409 |
| Cost of Goods Sold | Cost of goods sold | 324 |
| Income Tax Expense | Income tax expense | 248 |
| Lease Liability | Lease liability | 227 |
| Bonds Payable | Bonds payable | 215 |
| Depreciation Expense | Depreciation expense | 192 |
| Retained Earnings | Retained earnings | 180 |
| Discount on Bonds Payable | Discount on bonds payable | 168 |
| Paid-In Capital in Excess of Par—Common Stock | Paid-in Capital in Excess of Par—Common Stock | 139 |
| Right-of-Use Asset | Right-of-use asset | 131 |
| Deferred Tax Asset | Deferred tax asset | 129 |
| Interest Payable | Interest payable | 128 |
| Deferred Tax Liability | Deferred tax liability | 128 |
| Fair Value Adjustment—AFS | Fair value adjustment—AFS | 106 |
| Premium on Bonds Payable | Premium on bonds payable | 101 |
| Inventory (beginning) | Inventory (Beginning) | 56 |
| Lease Expense | Lease expense | 49 |
| Treasury Stock | Treasury stock | 49 |
| Inventory (ending) | Inventory (Ending) | 43 |
| Salaries Expense | Salaries expense | 35 |
| Dividends Payable | Dividends payable | 28 |
| Freight-In | Freight-in | 24 |
| Paid-In Capital—Stock Warrants | Paid-in Capital—Stock Warrants | 24 |
| Loss on Sale of Equipment | Loss on sale of equipment | 20 |
| Accumulated Other Comprehensive Income | Accumulated other comprehensive income | 19 |
| Loss on bond retirement | Loss on Bond Retirement | 13 |
| Common Stock ($5 par) | Common stock, $5 par | 11 |
| Paid-in Capital in Excess of Par—Common | Paid-In Capital in Excess of Par—Common | 8 |
| Retained Earnings (or Dividends) | Retained earnings (or Dividends) | 7 |
| Common Stock ($10 par) | Common stock, $10 par | 6 |
| Available-for-Sale Debt Securities | Available-for-sale debt securities | 4 |
| Notes Payable (long-term) | Notes Payable—Long-term | 4 |
| Loss / Expense — Abnormal Spoilage | Loss / Expense—Abnormal Spoilage | 3 |
| Retained Earnings (or Cash Dividends—Preferred) | Retained Earnings (or Cash Dividends — Preferred) | 3 |
| Paid-in Capital in Excess of Par | Paid-In Capital in Excess of Par | 3 |
| Equipment (Improvements) | Equipment Improvements | 2 |

## B. Approved new canonical accounts (6)

| canonical | occurrences |
|---|---:|
| Patent | 128 |
| Purchases | 102 |
| Compensation Expense | 85 |
| Discount on Note Payable | 76 |
| Fair Value Adjustment—TS | 67 |
| Retained Earnings—Prior Period Adjustment | 59 |

## C. Pair rulings (3 rows)

### note_payable_singular_plural

- ruling: **ALIAS_TO_CANONICAL**
- canonical: Note Payable
- why: The book uses BOTH but is not balanced: 612 vs 82 overall, 154 vs 36 in journal-entry position - roughly 4:1 for the singular in both views. That is a dominant house form, not two equally sanctioned spellings, so the singular is canonical and the plural aliases to it. An equivalence pair would be the right call only if the counts were comparable.

### unrealized_holding_token

- ruling: **EQUIVALENCE_PAIR_FAMILY_LEVEL**
- canonical: — (family-level equivalence)
- why: Neither bare string occurs. The corpus writes 27 distinct spellings, all carrying a destination suffix (--Income / --OCI) that is semantically load-bearing: --Income and --OCI are DIFFERENT accounts and must never merge. The token 'Holding' is the only difference within a destination (e.g. 'Unrealized Gain or Loss--OCI' 114 vs 'Unrealized Holding Gain--OCI' 9), so equivalence is declared FAMILY-LEVEL: same destination suffix and differing only by 'Holding' -> equivalent; different suffix -> distinct.

### rd_expense

- ruling: **CANONICAL_AS_HARVESTED**
- canonical: Research and Development Expense
- why: 'R&D Expense' was order-block shorthand and does not occur in the corpus; disregarded.

## D. Not applied

- `R&D Expense` — order-block shorthand; does not occur. Canonical is **Research and Development Expense** as harvested.
- `Buildings` — does not occur in the corpus; `Building` (55) stands alone.
- 28 notation strings (`Cash (or Salaries Payable)`, `Retained Earnings (or Dividends)`, …) routed to acceptable-form handling; they are notations, not accounts.
