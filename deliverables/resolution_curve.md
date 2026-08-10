# Unresolved-line resolution curve

**5036 unresolved LINES** across **1208 distinct account strings** (notation lines excluded).

Admitting the next *N* most frequent harvest strings covers:

| next N strings admitted | lines covered | % of unresolved |
|---:|---:|---:|
| 10 | 831 | 16.5% |
| 25 | 1346 | 26.7% |
| 50 | 1903 | 37.8% |
| 100 | 2541 | 50.5% |
| 150 | 2952 | 58.6% |
| 200 | 3253 | 64.6% |
| 300 | 3681 | 73.1% |
| 400 | 3983 | 79.1% |
| 500 | 4183 | 83.1% |
| 1208 | 5036 | 100.0% |

The curve is steep: the head is a small number of very common accounts, so a short approval batch retires most of the volume.

## Proposed next approval batch — top 25

| # | account string | lines |
|---:|---|---:|
| 1 | `Income Tax Payable` | 173 |
| 2 | `Unrealized Gain or Loss—Income` | 156 |
| 3 | `Unrealized Gain or Loss—OCI` | 114 |
| 4 | `Research and Development Expense` | 74 |
| 5 | `Accumulated Depreciation—Building` | 61 |
| 6 | `Construction in Process` | 61 |
| 7 | `Building` | 55 |
| 8 | `Fair Value Adjustment—Equity Securities` | 47 |
| 9 | `Discount on Note Receivable` | 45 |
| 10 | `Customer List` | 45 |
| 11 | `Asset Retirement Obligation` | 41 |
| 12 | `Paid-In Capital in Excess of Par—Preferred Stock` | 39 |
| 13 | `Paid-in Capital—Stock Options` | 39 |
| 14 | `Income Summary` | 38 |
| 15 | `Depreciation Expense—Equipment` | 36 |
| 16 | `Liability for Unrecognized Tax Benefits` | 36 |
| 17 | `Valuation Allowance for Deferred Tax Asset` | 35 |
| 18 | `Gain on Sale of Investment` | 33 |
| 19 | `Mandatorily Redeemable Preferred Stock Liability` | 33 |
| 20 | `Additional Paid-in Capital—Common` | 33 |
| 21 | `Investment Income` | 32 |
| 22 | `Loss on Impairment` | 32 |
| 23 | `License` | 30 |
| 24 | `Software Intangible Asset` | 29 |
| 25 | `Allowance to Reduce Inventory to Market` | 29 |

Operator review: approve as canonical chart entries, or mark any that are notation/context-dependent so they route to the acceptable-form handler instead.

Non-blocking; runs parallel to the sequence. Apply before tranche 1 if approved in time.

