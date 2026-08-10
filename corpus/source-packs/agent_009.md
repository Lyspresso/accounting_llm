# Agent 9 — CORE DEMO — LO 14-8

**Chapter:** 14  
**LO title:** Account for debt securities measured at FV-OCI with fair value adjustments only at period-end  
**Critical gap LO:** yes

## Concept list for this pack
- Initial recognition of AFS debt at acquisition cost (par path)
- Interest revenue in net income (coupon / amortized cost)
- Period-end-only Fair Value Adjustment through OCI (no sale-date FV adjust)
- Sale: realized G/L = cash proceeds − amortized cost (NI); FVA left until year-end
- Year-end FVA cleanup after disposal and AOCI reclassification disclosure
- Multi-security AFS portfolio period-end FVA after partial sale
- Classification / presentation: BS at FV; unrealized in AOCI; reclass out of AOCI on sale

---

### Q1 — CORE — Cascade Peaks full AFS life cycle (period-end-only FV-OCI)
**LO:** LO 14-8  
**Concept:** Initial recognition, interest, period-end FVA through OCI, sale without mid-period FV adjust, year-end FVA elimination, AOCI reclass disclosure  
**Scenario:** On July 1 of Year 1, Cascade Peaks Investments LLC purchased for par **$40,000** face of Meridian 7% bonds that mature on June 30 of Year 6. Cash interest is paid semiannually on June 30 and December 31. Cascade classifies the investment as **available-for-sale (AFS)** and applies the **Appendix 14B / LO 14-8 method**: fair value is adjusted **only at period-end** (not at the sale date). Cascade’s annual reporting period ends December 31. Beginning FVA—AFS and AOCI related to these bonds are zero.

Additional facts:
- December 31, Year 1 fair value of Meridian bonds = **$37,600**
- No purchases or sales of AFS in Year 2; December 31, Year 2 fair value = **$41,200**
- January 1, Year 3: Cascade sells the entire Meridian holding for **$42,000** cash (no accrued interest—sale on an interest date)
- No other AFS holdings remain after the sale; December 31, Year 3 required FVA ending balance = **$0**

**Required:**  
(a) Record the July 1, Year 1 purchase.  
(b) Record receipt of cash interest on December 31, Year 1.  
(c) Record the December 31, Year 1 period-end fair value adjusting entry (FV-OCI).  
(d) Show December 31, Year 1 balance sheet carrying amount of the AFS investment and AOCI, and list Year 1 interest revenue and the OCI unrealized holding amount.  
(e) Record the December 31, Year 2 period-end fair value adjusting entry (show the FVA bridge: required vs existing).  
(f) Record the January 1, Year 3 sale (**period-end-only method**: do **not** adjust FVA at the sale date).  
(g) Record the December 31, Year 3 entry to eliminate the Fair Value Adjustment account.  
(h) Prepare the Year 3 Accumulated OCI reconciliation / reclassification disclosure (beginning AOCI, current-period unrealized, reclassification to NI, ending AOCI).

**Answer key:**

**(a) July 1, Year 1 — Purchase at par**
```
Investment in AFS Securities—Meridian Bonds ....... 40,000
    Cash .................................................... 40,000
```
Dr = Cr = $40,000

**(b) December 31, Year 1 — Interest (semiannual)**  
Cash interest = $40,000 × 0.07 × 6/12 = **$1,400**
```
Cash .............................................. 1,400
    Interest Revenue ........................................ 1,400
```
Dr = Cr = $1,400  
*(Interest revenue is recognized in **net income**; amortized cost remains $40,000 because purchased at par.)*

**(c) December 31, Year 1 — Period-end FV-OCI**  
Unrealized holding loss = amortized cost $40,000 − FV $37,600 = **$2,400**
```
Unrealized Gain or Loss—OCI ....................... 2,400
    Fair Value Adjustment—AFS ............................... 2,400
```
Dr = Cr = $2,400  
Required FVA balance = **$2,400 credit**; AOCI related = **$(2,400)**

**(d) Year 1 reporting**
| Item | Amount |
|---|---:|
| BS: Investment in AFS (at FV) | **$37,600** |
| BS: AOCI (loss) | **$(2,400)** |
| IS: Interest revenue | **$1,400** |
| OCI: Unrealized holding loss on AFS | **$(2,400)** |

**(e) December 31, Year 2 — Period-end FV-OCI bridge**

| | Amount |
|---|---:|
| Amortized cost | $40,000 |
| Fair value 12/31/Y2 | $41,200 |
| Required FVA (debit = unrealized gain) | **$1,200** |
| Existing FVA balance | **$(2,400)** credit |
| Increase (debit) needed to FVA | **$3,600** |

```
Fair Value Adjustment—AFS ......................... 3,600
    Unrealized Gain or Loss—OCI ............................. 3,600
```
Dr = Cr = $3,600  
After entry: FVA = $1,200 debit; AOCI = **$1,200** credit (net of prior-year $(2,400) + Year 2 $3,600)

**(f) January 1, Year 3 — Sale (no sale-date FV adjust)**  
Realized gain = cash $42,000 − amortized cost $40,000 = **$2,000**
```
Cash .............................................. 42,000
    Investment in AFS—Meridian Bonds ........................ 40,000
    Gain on Sale of Investment .............................. 2,000
```
Dr = Cr = $42,000  
**Key LO 14-8 distinction:** FVA is **not** adjusted or eliminated at the sale date; the realized gain hits **net income** now; FVA is cleaned up only at **period-end**.

**(g) December 31, Year 3 — Eliminate FVA (no remaining AFS)**

| | Amount |
|---|---:|
| Required FVA ending balance | $0 |
| Existing FVA balance | $1,200 debit |
| Decrease (credit) needed | **$(1,200)** |

```
Unrealized Gain or Loss—OCI ....................... 1,200
    Fair Value Adjustment—AFS ............................... 1,200
```
Dr = Cr = $1,200

**(h) Year 3 AOCI reclassification disclosure**

Components of Year 3 OCI of **$(1,200)**:
1. Current-period fair value increase from 12/31/Y2 FV $41,200 to sale proceeds $42,000 = **$800** unrealized gain in Y3 before sale  
2. Reclassification adjustment for **gain included in net income** = **$(2,000)**  

| Reconciliation of AOCI | Amount |
|---|---:|
| Accumulated OCI, January 1, Year 3 | $1,200 |
| Current period unrealized gain on AFS | 800 |
| Reclassification adjustment for gain included in NI | (2,000) |
| Net OCI for Year 3 | (1,200) |
| Accumulated OCI, December 31, Year 3 | **$0** |

AOCI life-cycle check (volatility in OCI, not NI, until sale):  
Year 1 OCI $(2,400) + Year 2 OCI $3,600 + Year 3 OCI $(1,200) = **$0**.  
Total NI gain over holding period = **$2,000** (recognized only in Year 3 at sale).

**Key insight:** Under LO 14-8, unrealized AFS fair-value changes hit **OCI only at period-end**. At sale, compute realized G/L as **cash − amortized cost** in NI and leave FVA alone until year-end, when FVA is reset for remaining holdings (here, fully eliminated).

---

### Q2 — CORE number variant — Harborline full AFS life cycle (period-end-only)
**LO:** LO 14-8  
**Concept:** Number-variant twin of Q1 — same period-end-only FV-OCI path with fully changed facts  
**Scenario:** On January 1 of Year 1, Harborline Mutual Fund Corp. purchased for par **$75,000** face of Solstice 4% bonds that mature on December 31 of Year 5. Cash interest is paid **annually** on December 31. Harborline classifies the bonds as **AFS** and uses **fair value adjustments only at period-end**. Fiscal year-end is December 31. Beginning FVA and related AOCI = $0.

Additional facts:
- December 31, Year 1 fair value = **$72,000**
- No AFS activity in Year 2; December 31, Year 2 fair value = **$76,500**
- February 1, Year 3: sells entire holding for **$77,250** cash (ignore accrued interest for this problem; focus on amortized cost vs cash for the gain/loss)
- No other AFS securities; December 31, Year 3 required FVA = **$0**

**Required:**  
(a) Purchase entry on January 1, Year 1.  
(b) Interest revenue entry on December 31, Year 1.  
(c) Period-end FV-OCI entry on December 31, Year 1.  
(d) Period-end FV-OCI entry on December 31, Year 2 (show required vs existing FVA).  
(e) Sale entry on February 1, Year 3 (period-end-only: no FVA at sale).  
(f) December 31, Year 3 FVA elimination.  
(g) Year 3 AOCI reconciliation (beg AOCI, current-period unrealized from last YE FV to sale price, reclass of realized gain, ending AOCI).

**Answer key:**

**(a) January 1, Year 1**
```
Investment in AFS Securities—Solstice Bonds ....... 75,000
    Cash .................................................... 75,000
```
Dr = Cr = $75,000

**(b) December 31, Year 1 — Interest**  
$75,000 × 0.04 × 12/12 = **$3,000**
```
Cash .............................................. 3,000
    Interest Revenue ........................................ 3,000
```
Dr = Cr = $3,000

**(c) December 31, Year 1 — FV-OCI**  
Unrealized loss = $75,000 − $72,000 = **$3,000**
```
Unrealized Gain or Loss—OCI ....................... 3,000
    Fair Value Adjustment—AFS ............................... 3,000
```
Dr = Cr = $3,000  
BS carrying amount = **$72,000**; AOCI = **$(3,000)**

**(d) December 31, Year 2 — FVA bridge**

| | Amount |
|---|---:|
| Required FVA (FV $76,500 − AC $75,000) | **$1,500** debit |
| Existing FVA | **$(3,000)** credit |
| Debit to FVA needed | **$4,500** |

```
Fair Value Adjustment—AFS ......................... 4,500
    Unrealized Gain or Loss—OCI ............................. 4,500
```
Dr = Cr = $4,500  
Ending FVA = $1,500 debit; AOCI = **$1,500**

**(e) February 1, Year 3 — Sale**  
Gain = $77,250 − $75,000 = **$2,250**
```
Cash .............................................. 77,250
    Investment in AFS—Solstice Bonds ........................ 75,000
    Gain on Sale of Investment .............................. 2,250
```
Dr = Cr = $77,250  
No FVA entry at sale date.

**(f) December 31, Year 3 — Eliminate FVA**
```
Unrealized Gain or Loss—OCI ....................... 1,500
    Fair Value Adjustment—AFS ............................... 1,500
```
Dr = Cr = $1,500

**(g) Year 3 AOCI reconciliation**  
Current-period unrealized from 12/31/Y2 FV $76,500 → sale $77,250 = **$750**  
Reclass of realized gain in NI = **$(2,250)**  
Net Year 3 OCI = $750 − $2,250 = **$(1,500)**

| AOCI | Amount |
|---|---:|
| Beginning, 1/1/Y3 | $1,500 |
| Current period unrealized gain | 750 |
| Reclassification adjustment for gain in NI | (2,250) |
| Ending, 12/31/Y3 | **$0** |

Life-cycle OCI: Y1 $(3,000) + Y2 $4,500 + Y3 $(1,500) = **$0**; total NI gain over hold = **$2,250**.

**Key insight:** Changing all amounts does not change the LO 14-8 sequence: **purchase → interest in NI → period-end FVA↔OCI → sale at AC vs cash in NI → year-end FVA cleanup + AOCI reclass**.

---

### Q3 — CORE alternate angle — Multi-security AFS portfolio, partial sale, period-end-only FVA
**LO:** LO 14-8  
**Concept:** Portfolio period-end FVA after disposing of one AFS holding; reclassification disclosure when remaining securities continue  
**Scenario:** At December 31 of Year 2, Lumen Treasury Co. holds the following **AFS** debt portfolio (all purchased at par; amortized cost = face). Lumen uses **period-end-only** fair value adjustments (LO 14-8). Accounting year ends December 31.

| AFS investment | Amortized cost | Fair value 12/31/Y2 | Unrealized holding G/(L) |
|---|---:|---:|---:|
| Orion 5% bonds | $60,000 | $58,200 | $(1,800) |
| Pinnacle 6% bonds | 90,000 | 94,500 | 4,500 |
| **Totals** | **$150,000** | **$152,700** | **$2,700** |

The $2,700 unrealized net gain equals the December 31, Year 2 balances in **FVA—AFS** (debit) and **AOCI** (credit).

On **January 1 of Year 3**, Lumen sells the entire Orion holding for **$59,400** cash. No other AFS purchases or sales occur in Year 3. On December 31 of Year 3, remaining Pinnacle bonds have fair value **$93,000** (amortized cost still $90,000).

**Required:**  
(a) Record the January 1, Year 3 sale of Orion (period-end-only method).  
(b) Compute the required December 31, Year 3 FVA balance for remaining AFS and the adjusting entry amount (required − existing). Record the year-end FVA entry.  
(c) Prepare the Year 3 AOCI reconciliation, including: (i) current-period unrealized G/L on Orion from last YE FV to sale price and on Pinnacle from last YE FV to YE3 FV; (ii) reclassification adjustment for the realized loss; (iii) ending AOCI.  
(d) State the December 31, Year 3 balance sheet carrying amount of the remaining AFS investment.

**Answer key:**

**(a) January 1, Year 3 — Sale of Orion**  
Realized **loss** = cash $59,400 − amortized cost $60,000 = **$600**
```
Cash .............................................. 59,400
Loss on Sale of Investment ........................ 600
    Investment in AFS—Orion Bonds ........................... 60,000
```
Dr = Cr = $60,000  
No FVA entry at sale.

**(b) December 31, Year 3 — Portfolio FVA**

| | Amount |
|---|---:|
| Required FVA (Pinnacle FV $93,000 − AC $90,000) | **$3,000** debit |
| Existing FVA (12/31/Y2 portfolio) | **$2,700** debit |
| Increase (debit) needed | **$300** |

```
Fair Value Adjustment—AFS ......................... 300
    Unrealized Gain or Loss—OCI ............................. 300
```
Dr = Cr = $300

**(c) Year 3 AOCI components and reconciliation**

Current-period fair value changes:
| Security | FV at sale or 12/31/Y3 | FV 12/31/Y2 | Difference |
|---|---:|---:|---:|
| Orion (sold) | $59,400 | $58,200 | **$1,200** |
| Pinnacle (held) | 93,000 | 94,500 | **$(1,500)** |
| **Total current-period unrealized** | | | **$(300)** |

Reclassification adjustment for **loss** included in net income = **+$600** (removes cumulative unrealized loss effect from AOCI as the $600 loss is now in NI).

Net Year 3 OCI = $(300) + $600 = **+$300** (matches credit to Unrealized G/L—OCI in part b).

| Reconciliation of AOCI | Amount |
|---|---:|
| AOCI, January 1, Year 3 | $2,700 |
| Current period unrealized loss on AFS | (300) |
| Reclassification adjustment for loss included in NI | 600 |
| Net OCI Year 3 | 300 |
| AOCI, December 31, Year 3 | **$3,000** |

*(Ending AOCI $3,000 = remaining Pinnacle unrealized gain $93,000 − $90,000.)*

**(d)** BS carrying amount of AFS (Pinnacle) at 12/31/Y3 = fair value **$93,000** (= AC $90,000 + FVA debit $3,000).

**Key insight:** After a partial portfolio sale under period-end-only FV-OCI, the year-end FVA entry is a **single portfolio plug** (required FVA for securities still held − existing FVA). That plug automatically embeds current-year FV moves on sold and held securities **and** the reclassification of the realized G/L out of AOCI.

---

### Q4 — MC (classification / method)
**LO:** LO 14-8  
**Concept:** Distinguishing period-end-only FV-OCI (Appendix 14B) from sale-date-and-period-end FV-OCI; routing of unrealized vs realized  
**Question:** Northwind Advisors holds AFS debt securities and elects the accounting policy under which fair value is updated **only at period-end** (LO 14-8 / Appendix 14B). On March 20 of Year 4, Northwind sells an AFS bond that had amortized cost of $25,000. Cash proceeds are $26,400. Immediately before the sale, Fair Value Adjustment—AFS related to this bond still reflected the **prior year-end** fair value (no entry has been made since December 31, Year 3). Which combination is correct for the **sale-date** entry and the **year-end** treatment of FVA?

- A) At sale: adjust FVA to current FV through OCI, then remove the investment and FVA with no separate gain/loss; year-end: no further FVA work related to this bond.  
- B) At sale: debit Cash $26,400, credit Investment $25,000, credit Gain on Sale $1,400; leave FVA unchanged at sale; at year-end, adjust FVA for remaining AFS (including elimination of FVA that related to the sold bond).  
- C) At sale: debit Cash $26,400, credit Investment $26,400; recognize no gain because AFS unrealized amounts never affect net income; year-end FVA only for remaining bonds.  
- D) At sale: debit Cash $26,400, credit Investment $25,000, credit Unrealized Gain or Loss—OCI $1,400; year-end: reclassify the same $1,400 from AOCI to NI.

**Answer:** **B.** Under LO 14-8, realized gain = cash − amortized cost is recorded in **net income** at sale; **FVA is not adjusted at the sale date**. Period-end FVA then resets the valuation account for securities still held and clears amounts related to securities sold during the period.  
A describes the LO 14-3 “adjust at sale date and period-end” approach. C is wrong because realized G/L **does** affect NI. D misroutes the realized gain to OCI at sale instead of NI.

---

### Q5 — MC (presentation)
**LO:** LO 14-8  
**Concept:** Balance-sheet classification and comprehensive-income presentation of AFS debt under FV-OCI  
**Question:** At December 31, Year 2, Riverton Holdings reports an AFS corporate bond portfolio with amortized cost $200,000 and fair value $195,500. There were no sales of AFS during Year 2. Beginning FVA—AFS was $0. Under LO 14-8 period-end-only measurement, which statement is correct?

- A) Investment is reported at amortized cost $200,000 on the balance sheet; the $4,500 decline is disclosed only in the notes.  
- B) Investment is reported at fair value $195,500; Unrealized Gain or Loss—Income is debited $4,500 so net income is reduced.  
- C) Investment is reported at fair value $195,500 (via FVA); Unrealized Gain or Loss—OCI is debited $4,500; AOCI is reduced (or shows an accumulated loss); net income is **not** reduced by the $4,500 unrealized loss.  
- D) Investment is reported at fair value $195,500; the entire $4,500 is reclassified from AOCI into net income at year-end even though no sale occurred.

**Answer:** **C.** AFS debt is measured at **fair value** on the BS; period-end unrealized holding losses go to **OCI → AOCI**, not net income, until realized (sale) or certain impairment exceptions. Interest revenue still flows through NI on the amortized-cost basis. A confuses HTM. B is the FV-NI / trading treatment. D incorrectly forces reclassification without a realizing event.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (Q1: 1,400; 2,400; 3,600; 2,000; 800/1,200 AOCI; Q2: 3,000; 4,500; 2,250; 750; Q3: 600 loss; FVA +300; AOCI end 3,000)
- [x] Core demo not sidebar-only (Demo 14-8A / 14-8B primary path: period-end-only FV-OCI)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method items)
- [x] Original company names and numbers (not textbook Bold/Rush/Blue/Cait)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (FVA bridges), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
