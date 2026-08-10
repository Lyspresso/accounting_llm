# Agent 5 — CORE DEMO — LO 14-4

**Chapter:** 14  
**LO title:** Account for equity securities measured at FV-NI with fair value adjustments at sale date and period-end  
**Critical gap LO:** yes

## Concept list for this pack
- Initial recognition of equity investment at cost (purchase price + brokerage/commissions) under ASC 321 / FV-NI
- Dividend revenue when investor has insignificant influence (not a reduction of investment)
- Fair value adjustment (FVA) valuation account and unrealized holding G/L through net income at period-end
- Sale-date FV-NI update then elimination of Investment + FVA (no residual “gain on sale” if already marked to sale-date FV)
- Balance sheet presentation (cost + FVA = fair value) and income statement components (dividends + unrealized G/L)
- Partial disposal cost allocation and period-end FVA on remaining shares
- Classification: FV-NI (insignificant influence / readily determinable FV) vs equity method

### Q1 — CORE — Full-cycle equity securities at FV-NI (purchase with commissions → dividend → year-end FVA → sale)
**LO:** LO 14-4  
**Concept:** initial_recognition_JE + period_end_adjusting_JE + disposal with sale-date FV-NI  
**Scenario:** Meridian Capital Corp. acquires a passive stake in Oakridge Industries, Inc. On **March 1, Year 1**, Meridian purchases **4,000** of Oakridge’s **50,000** outstanding common shares (**8%** ownership) for **$35** per share and pays **$1,200** in brokerage commissions. Meridian does **not** have significant influence over Oakridge; fair value is readily determinable. Meridian’s year-end is December 31.

Additional facts:
- **November 20, Year 1:** Oakridge declares and pays a cash dividend of **$1.50** per share.
- **December 31, Year 1:** Oakridge common stock fair value is **$38** per share.
- **February 12, Year 2:** Meridian sells the entire 4,000-share position for cash proceeds of **$154,800**.

**Required:**  
(a) Record the March 1, Year 1 purchase (include commissions in cost).  
(b) Record November 20, Year 1 dividend revenue.  
(c) Prepare the fair-value rollforward / FVA schedule at December 31, Year 1 and record the period-end adjusting entry (assume FVA begins at zero).  
(d) Show how the investment and related income items appear on Meridian’s December 31, Year 1 balance sheet and Year 1 income statement.  
(e) Record February 12, Year 2: (1) sale-date FV-NI adjustment, then (2) sale eliminating Investment and FVA. Reconcile total FV gains recognized over the holding period.

**Answer key:**

**(a) Purchase cost**  
Purchase price = \(4{,}000 \times \$35 = \$140{,}000\).  
Capitalized cost = \(140{,}000 + 1{,}200 = \mathbf{\$141{,}200}\).

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Mar 1, Y1 | Investment in Oakridge common stock | 141,200 | |
| | Cash | | 141,200 |

Dr = Cr = $141,200.

**(b) Dividend (insignificant influence → revenue, not return of capital)**  
Dividend = \(4{,}000 \times \$1.50 = \mathbf{\$6{,}000}\).

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Nov 20, Y1 | Cash | 6,000 | |
| | Dividend revenue | | 6,000 |

Dr = Cr = $6,000.

**(c) Period-end FVA schedule and JE**

| Item | Amount |
|---|---:|
| Cost (Investment account) | $141,200 |
| Fair value at Dec 31, Y1 (\(4{,}000 \times \$38\)) | 152,000 |
| Required FVA balance (debit / adjunct) | **10,800** |
| Existing FVA balance | 0 |
| Adjusting increase to FVA | **10,800** |

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec 31, Y1 | Fair value adjustment—equity securities | 10,800 | |
| | Unrealized gain or loss—income | | 10,800 |

Dr = Cr = $10,800.  
Carrying amount on BS = \(141{,}200 + 10{,}800 = \$152{,}000\).

**(d) Financial statement presentation — December 31, Year 1 / Year 1**

Balance sheet (assets excerpt):
- Investment in equity securities …………………… **$152,000**  
  (Investment $141,200 + FVA $10,800)

Income statement (other revenues/gains excerpt):
- Dividend revenue …………………………………… **$6,000**
- Unrealized holding gain on equity securities ……… **$10,800**

**(e) Sale-date FV-NI then disposal**

| Item | Amount |
|---|---:|
| Sale proceeds (sale-date FV) | $154,800 |
| Cost | 141,200 |
| Required FVA at sale date | **13,600** |
| Existing FVA (from Dec 31, Y1) | 10,800 |
| Additional FVA increase (sale-date unrealized gain) | **2,800** |

Sale-date adjust:

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Feb 12, Y2 | Fair value adjustment—equity securities | 2,800 | |
| | Unrealized gain or loss—income | | 2,800 |

Dr = Cr = $2,800.

Record sale (remove cost + full FVA; no separate residual gain):

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Feb 12, Y2 | Cash | 154,800 | |
| | Investment in Oakridge common stock | | 141,200 |
| | Fair value adjustment—equity securities | | 13,600 |

Dr $154,800 = Cr \(141{,}200 + 13{,}600 = \$154{,}800\).

Holding-period FV gain reconciliation:
- Year 1 unrealized gain (NI): **$10,800**
- Year 2 unrealized gain (NI): **$2,800**
- Total FV increase from cost to exit: **$13,600** (= \(154{,}800 - 141{,}200\))

**Key insight:** Under FV-NI (ASC 321), equity investments with insignificant influence are marked through **net income** at each reporting date and again at sale; brokerage is **capitalized** in cost; dividends are **revenue**; the sale entry clears Investment at cost and FVA so total earnings over the hold equal the economic price change (plus dividends).

---

### Q2 — CORE number variant twin (unrealized loss year-end → partial recovery on sale)
**LO:** LO 14-4  
**Concept:** number_variant_twin — same FV-NI cycle with loss FVA and sale-date recovery  
**Scenario:** Harbor Funds LLC buys **8,000** of Crestline Corp.’s **100,000** outstanding common shares (**8%**) on **June 15, Year 1** for **$22** per share plus **$800** brokerage commissions. Harbor has insignificant influence; FV is readily determinable. Year-end is December 31.

- **October 1, Year 1:** Crestline declares and pays **$0.75** per share cash dividend.
- **December 31, Year 1:** Fair value is **$20** per share.
- **April 3, Year 2:** Harbor sells all 8,000 shares for cash proceeds of **$165,600**.

**Required:**  
(a) Purchase JE.  
(b) Dividend JE.  
(c) Dec 31, Year 1 FVA schedule and adjusting JE (FVA begins at zero).  
(d) April 3, Year 2 sale-date FV-NI adjustment and sale JE (eliminate Investment + FVA).  
(e) Reconcile cumulative unrealized G/L recognized in Years 1–2 to the total price change from cost.

**Answer key:**

**(a) Cost** = \(8{,}000 \times \$22 + \$800 = \$176{,}000 + \$800 = \mathbf{\$176{,}800}\).

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jun 15, Y1 | Investment in Crestline common stock | 176,800 | |
| | Cash | | 176,800 |

Dr = Cr = $176,800.

**(b) Dividend** = \(8{,}000 \times \$0.75 = \mathbf{\$6{,}000}\).

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Oct 1, Y1 | Cash | 6,000 | |
| | Dividend revenue | | 6,000 |

Dr = Cr = $6,000.

**(c) Year-end FVA (loss)**

| Item | Amount |
|---|---:|
| Cost | $176,800 |
| Fair value Dec 31, Y1 (\(8{,}000 \times \$20\)) | 160,000 |
| Required FVA balance (credit / contra) | **16,800** |
| Existing FVA | 0 |
| Adjustment | **16,800** credit to FVA |

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec 31, Y1 | Unrealized gain or loss—income | 16,800 | |
| | Fair value adjustment—equity securities | | 16,800 |

Dr = Cr = $16,800.  
Carrying amount = \(176{,}800 - 16{,}800 = \$160{,}000\).

**(d) Sale-date update and disposal**

| Item | Amount |
|---|---:|
| Sale proceeds | $165,600 |
| Cost | 176,800 |
| Required FVA credit at sale | **11,200** (\(176{,}800 - 165{,}600\)) |
| Existing FVA credit | 16,800 |
| Decrease in FVA credit (recognize recovery in NI) | **5,600** |

Sale-date adjust (partial reversal of prior unrealized loss):

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Apr 3, Y2 | Fair value adjustment—equity securities | 5,600 | |
| | Unrealized gain or loss—income | | 5,600 |

Dr = Cr = $5,600.

Sale:

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Apr 3, Y2 | Cash | 165,600 | |
| | Fair value adjustment—equity securities | 11,200 | |
| | Investment in Crestline common stock | | 176,800 |

Dr \(165{,}600 + 11{,}200 = \$176{,}800\) = Cr $176,800.

**(e) Cumulative FV P&L reconciliation**
- Year 1 unrealized loss: **$(16,800)**
- Year 2 unrealized gain (recovery): **$5,600**
- Net FV loss over holding period: **$(11,200)** = \(165{,}600 - 176{,}800\)

**Key insight:** FVA can be a **debit (gain)** or **credit (loss)** adjunct/contra; sale-date FV-NI still updates FVA first so the disposal entry only reclassifies cash vs. cost/FVA with no leftover “realized gain” plug.

---

### Q3 — CORE alternate angle — Partial disposal + remaining-share period-end FVA + presentation
**LO:** LO 14-4  
**Concept:** disposal_maturity_or_settlement_JE (partial sale) + subsequent_measurement_schedule + classification_presentation_or_disclosure  
**Scenario:** Pinecrest Advisors Inc. purchases **5,000** shares of Helix Dynamics Corp. common stock on **January 10, Year 1** for **$75** per share and pays **$1,000** commissions (total cost **$376,000**). Helix has **80,000** shares outstanding (**6.25%** ownership). Pinecrest has insignificant influence and measures the investment at FV-NI. Year-end is December 31. FVA begins at zero.

- **August 20, Year 1:** Helix declares and pays **$2.00** per share cash dividend on shares outstanding (Pinecrest still holds all 5,000).
- **September 8, Year 1:** Pinecrest sells **2,000** shares for **$82** per share cash (**$164,000**). Allocate cost pro rata; use sale-date FV-NI on the sold tranche only, then eliminate related Investment and FVA.
- **December 31, Year 1:** Fair value of the **remaining 3,000** shares is **$78** per share.

**Required:**  
(a) January 10 purchase JE.  
(b) August 20 dividend JE.  
(c) September 8: cost of shares sold; sale-date FVA JE for the sold tranche; sale JE.  
(d) Remaining cost; Dec 31 FVA schedule and adjusting JE for remaining shares.  
(e) December 31, Year 1 BS carrying amount of the investment and Year 1 income statement amounts related to Helix (dividends + all unrealized G/L).

**Answer key:**

**(a) Cost** = \(5{,}000 \times \$75 + \$1{,}000 = \$375{,}000 + \$1{,}000 = \mathbf{\$376{,}000}\).

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 10, Y1 | Investment in Helix common stock | 376,000 | |
| | Cash | | 376,000 |

Dr = Cr = $376,000.

**(b) Dividend** = \(5{,}000 \times \$2 = \mathbf{\$10{,}000}\).

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Aug 20, Y1 | Cash | 10,000 | |
| | Dividend revenue | | 10,000 |

Dr = Cr = $10,000.

**(c) Partial sale — Sept 8**  
Cost allocated to sold shares = \(\dfrac{2{,}000}{5{,}000} \times \$376{,}000 = \mathbf{\$150{,}400}\).  
Proceeds = \(2{,}000 \times \$82 = \mathbf{\$164{,}000}\).  
Required FVA on sold tranche = \(164{,}000 - 150{,}400 = \mathbf{\$13{,}600}\).

Sale-date FV-NI (sold tranche):

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Sep 8, Y1 | Fair value adjustment—equity securities | 13,600 | |
| | Unrealized gain or loss—income | | 13,600 |

Dr = Cr = $13,600.

Sale (eliminate sold cost + related FVA):

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Sep 8, Y1 | Cash | 164,000 | |
| | Investment in Helix common stock | | 150,400 |
| | Fair value adjustment—equity securities | | 13,600 |

Dr $164,000 = Cr \(150{,}400 + 13{,}600 = \$164{,}000\).

**(d) Remaining position and year-end FVA**  
Remaining cost = \(376{,}000 - 150{,}400 = \mathbf{\$225{,}600}\) (3,000 shares).  
Remaining FVA after sale = **$0** (sold tranche FVA fully cleared).

| Item | Amount |
|---|---:|
| Remaining cost | $225,600 |
| Fair value Dec 31 (\(3{,}000 \times \$78\)) | 234,000 |
| Required FVA (debit) | **8,400** |
| Existing FVA | 0 |
| Adjustment | **8,400** |

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec 31, Y1 | Fair value adjustment—equity securities | 8,400 | |
| | Unrealized gain or loss—income | | 8,400 |

Dr = Cr = $8,400.  
Carrying amount = \(225{,}600 + 8{,}400 = \$234{,}000\).

**(e) Presentation / earnings related to Helix — Year 1**

Balance sheet Dec 31, Y1:
- Investment in equity securities ……………… **$234,000**

Income statement Year 1:
- Dividend revenue ……………………………… **$10,000**
- Unrealized holding gain (sale-date, sold shares) **$13,600**
- Unrealized holding gain (year-end, remaining) **$8,400**
- Total Helix-related income …………………… **$32,000**

**Key insight:** On a partial sale, allocate **cost pro rata**, mark **only the sold tranche** to sale-date FV through NI, clear that tranche’s FVA, then remeasure **remaining** shares at period-end with a fresh FVA rollforward.

---

### Q4 — MC — Method / presentation classification
**LO:** LO 14-4  
**Concept:** classification_presentation_or_disclosure — FV-NI vs equity method; unrealized G/L location  
**Question:** On January 1, Riverbend Holdings acquires **12%** of the voting common stock of Solara Tech Inc. for cash, including brokerage fees in the investment’s initial cost. Riverbend has **no** board representation, no participation in policy-making, and no other indicators of significant influence. Solara’s shares have a readily determinable fair value. At year-end the shares’ fair value exceeds cost. Under U.S. GAAP (ASC 321), how should Riverbend report the year-end fair value increase?

- A) As an unrealized holding gain in **other comprehensive income (OCI)**; investment remains at cost until sold  
- B) As an unrealized holding gain in **net income** (FV-NI), typically via a Fair Value Adjustment valuation account  
- C) As equity-method investment income equal to 12% of Solara’s net income for the year  
- D) As a direct credit to retained earnings, bypassing comprehensive income entirely  

**Answer:** **B.** With insignificant influence and readily determinable fair value, equity securities are measured at FV-NI (ASC 321-10-35-1): unrealized holding gains/losses are included in **earnings**. Option A describes AFS **debt** (FV-OCI), not equity under ASC 321. Option C is the **equity method** (generally presumed at 20–50% with significant influence—LO 14-5). Option D is not GAAP for this investment.

---

### Q5 — MC — Sale-date sequence under FV-NI
**LO:** LO 14-4  
**Concept:** disposal_maturity_or_settlement_JE — sale-date FV adjust then eliminate FVA  
**Question:** An equity security measured at FV-NI was purchased in Year 1 for $200,000 (including commissions). At December 31, Year 1, FVA was debited $14,000 (unrealized gain through NI). On March 10, Year 2, the investor sells the entire position for $218,000 cash when the existing FVA debit balance is still $14,000. Which sequence is correct under the textbook FV-NI sale approach?

- A) Debit Cash $218,000; credit Investment $200,000; credit Gain on sale $18,000; leave FVA untouched  
- B) First increase FVA by $4,000 through Unrealized G/L—Income; then debit Cash $218,000, credit Investment $200,000, credit FVA $18,000  
- C) Debit Cash $218,000 and debit FVA $14,000; credit Investment $200,000; credit Gain on sale $32,000  
- D) Reclassify the $14,000 Year 1 unrealized gain from AOCI to net income, then credit Investment $218,000  

**Answer:** **B.** Required FVA at sale = \(218{,}000 - 200{,}000 = \$18{,}000\). Existing FVA = $14,000 → additional **$4,000** through NI. Sale then removes Investment at **cost** and FVA at **$18,000** so Dr Cash = Cr Investment + Cr FVA with no residual gain plug. A double-counts economics vs prior FVA. C misuses FVA direction and invents an oversized gain. D confuses FV-NI with AFS FV-OCI reclassification.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (costs, pro rata partial sale, FVA required vs existing, sale clearings)
- [x] Core demo not sidebar-only (follows Demo 14-4 / Review 14-4 primary path; no “fair value not readily determinable” sidebar path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4–Q5 classification/method only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
