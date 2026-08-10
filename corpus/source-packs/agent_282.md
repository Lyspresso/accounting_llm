# Agent 282 — CORE DEMO — LO 17-11

**Chapter:** 17  
**LO title:** Explain lease modifications and lease remeasurements  
**Critical gap LO:** yes  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Modification decision tree:** additional right of use at **standalone price** → **separate (new) lease**; otherwise → **single modified lease** (reassess classification + remeasure)
- **Remeasurement triggers (lessee):** (a) modification not a separate contract; (b) change in lease term; (c) change in assessment of purchase-option exercise; (d) contingency resolution making variable payments fixed; (e) change in amounts probable under a residual-value guarantee
- **Classification reassessment vs remeasure-only:** term / purchase-option assessment changes → **reassess + remeasure**; residual-guarantee probability / contingency resolution → **remeasure only** (no classification reassessment)
- **Remeasurement JE:** adjust **Lease Liability** to new PV of remaining lease payments; offset to **Right-of-Use Asset** (prospective, like a change in estimate)
- **Discount rate:** update to rate at remeasurement date **unless** residual-guarantee change, contingency resolution, or certain term/PO cases where the original rate already reflected the option (ASC 842-20-35-5)
- **Initial recognition JE:** finance lease at commencement — Dr ROU Asset / Cr Lease Liability for PV of unpaid lease payments (annuity-due or ordinary as stated)
- **Subsequent measurement schedule:** liability amortization (interest after payment for annuity-due); ROU amortization (finance: over lease term or useful life if ownership/PO reasonably certain)
- **Period-end adjusting JE (emphasis):** accrue **interest expense** on lease liability and **amortization expense** on ROU asset at reporting date
- **Disposal / maturity / settlement JE:** final payment(s); exercise purchase option (settle remaining liability; reclassify ROU → PPE)
- **Classification / presentation / disclosure:** finance vs operating after reassessment; current vs noncurrent lease liability; interest + amortization (finance) vs single lease cost (operating)
- **Number-variant twin:** same remeasurement path with all different amounts

---

### Q1 — CORE — Finance lease commencement, schedule, period-end JE (emphasis), purchase-option remeasurement, settlement

**LO:** LO 17-11  
**Concept:** Initial recognition of finance lease; liability/ROU schedules; **period-end interest and ROU amortization adjusting JEs**; remeasurement when purchase option becomes reasonably certain (update discount rate; Dr/Cr ROU ↔ LL); settlement by exercising PO  
**Scenario:**  
**Cedarline Logistics Inc.** (calendar-year) leases specialized sorting equipment from **North Pier Capital** on **January 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Lease term | 5 years (no renewal) |
| Economic life of equipment | 8 years |
| Annual lease payment (annuity-due) | **$72,000** due each **January 1**, beginning Year 1 |
| Purchase option at end of Year 5 | **$20,000** — **not** reasonably certain of exercise at commencement |
| Lessee incremental borrowing rate | **6%** (lessor implicit rate unknown) |
| Classification at commencement | **Finance lease** (PV of lease payments is substantial; other facts consistent with finance) |
| Residual value | None guaranteed |
| Initial direct costs | None |

On **January 1, Year 3** (before the Year 3 payment), Cedarline’s sales forecasts for products run on the equipment increase sharply. Management is now **reasonably certain** it will exercise the **$20,000** purchase option. After reassessing ASC 842 classification criteria, the lease **remains a finance lease**. Cedarline’s incremental borrowing rate on the remeasurement date is **5%**. The original 6% rate **did not** already reflect the purchase option.

Cedarline rounds PV factors and interest to the **nearest dollar**. ROU amortization before the PO reassessment is over the **5-year lease term**. After the PO is reasonably certain, ROU is amortized over the **remaining economic life** of the equipment (**6 years** from January 1, Year 3).

**Required:**  
a. Compute the **commencement PV** of lease payments (exclude the purchase option) and prepare the **January 1, Year 1 initial recognition JE** and the **Year 1 payment JE**.  
b. Prepare the **lease-liability amortization schedule** for Years 1–2 (through December 31, Year 2 / January 1, Year 3 balances before remeasurement).  
c. **(Emphasis)** Prepare the **December 31, Year 1 period-end adjusting JEs** (interest on LL; amortization of ROU).  
d. On **January 1, Year 3**, compute the **remeasured lease liability**, the **remeasurement adjustment**, and the **ROU carrying amount** immediately after remeasurement. Record the **remeasurement JE** (before the Year 3 payment).  
e. Record the **January 1, Year 3 lease payment**, then the **December 31, Year 3 period-end adjusting JEs** (interest at the **updated 5%** rate; ROU amort over remaining **6-year** economic life).  
f. Show the **liability roll-forward** after remeasurement through Year 5 (ending liability = purchase-option amount) and the **December 31, Year 5 / January 1, Year 6 settlement JEs** when Cedarline pays the **$20,000** purchase option and reclassifies the ROU asset to owned equipment.  
g. **Classification / presentation:** state how Year 3 lease-related expense appears on the income statement and how the lease liability is classified on the December 31, Year 3 balance sheet (current vs noncurrent components immediately after the January 1, Year 4 payment structure is known—use Year 4 payment + Year 4 interest pattern).

**Answer key:**  

**a. Commencement PV and January 1, Year 1 JEs**  
\[
\mathrm{PV} = \mathrm{PV}(6\%,\,5,\,-72{,}000,\,0,\,1) = \$321{,}488
\]  
(Excel: `=PV(0.06,5,-72000,0,1)`)

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset—Equipment | 321,488 | |
| Lease Liability | | 321,488 |
| *Commencement: finance lease at PV of unpaid lease payments (PO not included)* | | |

**Check:** Dr 321,488 = Cr 321,488. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 72,000 | |
| Cash | | 72,000 |
| *First annuity-due payment* | | |

**Check:** Dr 72,000 = Cr 72,000. **Balanced.**  
Liability after payment: \(321{,}488 - 72{,}000 = \$249{,}488\).

**b. Lease-liability schedule (Years 1–2) — interest = balance after payment × 6%**

| Date / period | Beg. LL | Payment (1/1) | LL after pmt | Interest (6%) | End. LL (12/31) |
|---|---:|---:|---:|---:|---:|
| 1/1/Y1 commencement | 321,488 | — | — | — | — |
| Year 1 | 321,488 | 72,000 | 249,488 | 14,969 | **264,457** |
| Year 2 | 264,457 | 72,000 | 192,457 | 11,547 | **204,004** |

Interest Y1: \(249{,}488 \times 0.06 = 14{,}969.28 \rightarrow \$14{,}969\).  
Interest Y2: \(192{,}457 \times 0.06 = 11{,}547.42 \rightarrow \$11{,}547\).  
**January 1, Year 3 LL before remeasurement / before payment = $204,004.**

**ROU before remeasurement:**  
Annual amort Y1–Y2: \(\mathrm{round}(321{,}488 / 5) = \$64{,}298\) per year.  
\[
\mathrm{ROU}_{1/1/\mathrm{Y3}} = 321{,}488 - 2\times 64{,}298 = \$192{,}892
\]

**c. December 31, Year 1 — Period-end adjusting JEs (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 14,969 | |
| Lease Liability | | 14,969 |
| *Period-end: accrete finance lease liability* | | |

**Check:** Dr 14,969 = Cr 14,969. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense—ROU Asset | 64,298 | |
| Accumulated Amortization—ROU Asset | | 64,298 |
| *Period-end: amortize ROU over 5-year lease term* | | |

**Check:** Dr 64,298 = Cr 64,298. **Balanced.**  
Year 1 finance-lease income-statement impact: interest **$14,969** + amortization **$64,298** = **$79,267**.

**d. January 1, Year 3 — Remeasurement (purchase option now reasonably certain)**  
Remeasured liability = PV of **3** remaining **$72,000** annuity-due payments + PV of **$20,000** PO, at **updated 5%**:  
\[
\mathrm{PV}(5\%,\,3,\,-72{,}000,\,-20{,}000,\,1) = \$223{,}154
\]  
(Excel: `=PV(0.05,3,-72000,-20000,1)`)

| Item | Amount |
|---|---:|
| Remeasured lease liability | $223,154 |
| Carrying amount of LL before remeasurement | 204,004 |
| **Increase in LL (adjustment to ROU)** | **$19,150** |
| ROU before remeasurement | 192,892 |
| **ROU after remeasurement** | **$212,042** |

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset—Equipment | 19,150 | |
| Lease Liability | | 19,150 |
| *Remeasure LL for PO now reasonably certain; update rate to 5%; offset to ROU* | | |

**Check:** Dr 19,150 = Cr 19,150. **Balanced.**  
**Why update the rate?** Change in assessment of whether the lessee will exercise a purchase option, and the original discount rate **did not** already reflect that option (ASC 842-20-35-5 exception does not apply).  
**Classification:** reassess → still finance lease.

**e. January 1, Year 3 payment + December 31, Year 3 period-end adjusting JEs (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 72,000 | |
| Cash | | 72,000 |

**Check:** Dr = Cr = 72,000. **Balanced.**  
LL after payment: \(223{,}154 - 72{,}000 = \$151{,}154\).

Interest Y3 at **5%**: \(151{,}154 \times 0.05 = 7{,}557.70 \rightarrow \$7{,}558\).

ROU amort Y3 over remaining **6-year** economic life:  
\[
212{,}042 / 6 = 35{,}340.333\ldots \rightarrow \$35{,}340
\]  
(use **$35,340** for Years 3–7 and plug residual in Year 8 if needed; for Y3 use **$35,340**).

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 7,558 | |
| Lease Liability | | 7,558 |
| *Period-end adjusting JE — interest on remeasured LL at 5%* | | |

**Check:** Dr 7,558 = Cr 7,558. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense—ROU Asset | 35,340 | |
| Accumulated Amortization—ROU Asset | | 35,340 |
| *Period-end adjusting JE — ROU over remaining economic life (PO reasonably certain)* | | |

**Check:** Dr 35,340 = Cr 35,340. **Balanced.**  
EOY Y3 LL: \(151{,}154 + 7{,}558 = \$158{,}712\).  
EOY Y3 ROU net: \(212{,}042 - 35{,}340 = \$176{,}702\).

**f. Post-remeasurement liability schedule through purchase-option settlement**

| Period | Beg. LL | Payment 1/1 | After pmt | Interest 5% | End. LL |
|---|---:|---:|---:|---:|---:|
| Y3 (after remeas) | 223,154 | 72,000 | 151,154 | 7,558 | 158,712 |
| Y4 | 158,712 | 72,000 | 86,712 | 4,336 | 91,048 |
| Y5 | 91,048 | 72,000 | 19,048 | 952 | **20,000** |

Interest Y4: \(86{,}712 \times 0.05 = 4{,}335.60 \rightarrow \$4{,}336\).  
Interest Y5: \(19{,}048 \times 0.05 = 952.40 \rightarrow \$952\) (plugs LL to PO amount **$20,000**).

**ROU net just before exercise (after 3 years of $35,340 amort, Y3–Y5):**  
\[
212{,}042 - 3\times 35{,}340 = 212{,}042 - 106{,}020 = \$106{,}022
\]

**Settlement when purchase option is paid (end of lease / early Year 6 as structured):**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 20,000 | |
| Cash | | 20,000 |
| *Exercise purchase option; settle remaining lease liability* | | |

**Check:** Dr 20,000 = Cr 20,000. **Balanced.**

**ROU gross / accum reconciliation at purchase:**  
- ROU gross (commencement + remeasurement debit): \(321{,}488 + 19{,}150 = \$340{,}638\)  
- Accumulated amortization: pre-remeas \(2\times 64{,}298 = 128{,}596\) + post-remeas \(3\times 35{,}340 = 106{,}020\) → **$234,616**  
- Net ROU: \(340{,}638 - 234{,}616 = \$106{,}022\) ✓

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 106,022 | |
| Accumulated Amortization—ROU Asset | 234,616 | |
| Right-of-Use Asset—Equipment | | 340,638 |
| *Transfer net ROU to PPE upon purchase* | | |

**Check:** Dr \(106{,}022 + 234{,}616 = 340{,}638\) = Cr 340,638. **Balanced.**

**g. Classification / presentation (Year 3)**  
- **Income statement (finance lease):** separate **Interest expense $7,558** and **Amortization expense $35,340** (not a single operating lease cost).  
- **Balance sheet Dec 31, Year 3:** ROU asset (net) **$176,702**; Lease liability total **$158,712**.  
  - **Current** lease liability (amounts due within one year): Year 4 payment **$72,000** less the portion of that payment that is effectively a reduction after considering that interest for Y4 accrues during Y4 — practical exam presentation: current portion ≈ **principal reduction in next year** = payment − next year’s interest = \(72{,}000 - 4{,}336 = \$67{,}664\), **or** simply disclose next cash lease payment **$72,000** as current with the residual noncurrent (course-dependent). Using principal-reduction approach:  
    - Current LL ≈ **$67,664**  
    - Noncurrent LL ≈ \(158{,}712 - 67{,}664 = \$91{,}048\) (equals EOY Y4 LL before Y5 dynamics — equals beg Y5 after Y4 interest… actually noncurrent after Y4 payment/interest path: EOY Y4 LL = 91,048 is the amount due beyond one year as of 12/31/Y3 after isolating next year’s principal reduction).

**Key insight:** A change in whether the lessee is **reasonably certain to exercise a purchase option** triggers **lease classification reassessment** and **liability remeasurement**. Remeasure at the **updated discount rate** (when the old rate did not already reflect the option), book the entire LL change to **ROU asset**, then continue **period-end adjusting JEs** for interest (new rate) and ROU amort (now over remaining **economic life**). Settlement of the PO extinguishes the residual liability and moves net ROU into owned PPE.

---

### Q2 — CORE number variant — Finance lease remeasurement when PO becomes reasonably certain

**LO:** LO 17-11  
**Concept:** Number-variant twin—initial finance lease JE; liability schedule; period-end adjusting JEs; remeasurement JE (updated rate) when purchase option assessment changes; post-remeasurement period-end JE  
**Scenario:**  
**Meridian Forge Co.** (calendar-year) leases a CNC cell on **January 1, Year 1**:

| Fact | Amount / term |
|---|---|
| Lease term | 5 years |
| Economic life | 7 years |
| Annual payment (annuity-due, each Jan 1) | **$95,000** |
| End-of-term purchase option | **$35,000** — not reasonably certain at commencement |
| Discount rate at commencement | **7%** |
| Classification | Finance lease |
| On Jan 1, Year 3 | PO becomes reasonably certain; lease remains finance; **new IBR 6%**; original rate did not reflect the PO |

Round to nearest dollar. ROU amort before remeasurement over **5-year term**; after remeasurement over remaining economic life **5 years** (7 − 2).

**Required:**  
a. Commencement PV, initial recognition JE, and first payment JE.  
b. Liability schedule through December 31, Year 2; ROU carrying amount January 1, Year 3 before remeasurement.  
c. **(Emphasis)** December 31, Year 1 period-end adjusting JEs.  
d. January 1, Year 3 remeasurement computation and JE; payment JE; December 31, Year 3 period-end adjusting JEs.  
e. Briefly state the **settlement** entry when the **$35,000** PO is paid at the end of Year 5 (assume LL has been accreted to exactly $35,000).

**Answer key:**  

**a. Commencement**  
\[
\mathrm{PV}(7\%,\,5,\,-95{,}000,\,0,\,1) = \$416{,}785
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset—Equipment | 416,785 | |
| Lease Liability | | 416,785 |

**Check:** Dr = Cr = 416,785. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 95,000 | |
| Cash | | 95,000 |

**Check:** Dr = Cr = 95,000. **Balanced.**

**b. Liability schedule (7%)**

| Period | Beg. LL | Payment | After pmt | Interest 7% | End. LL |
|---|---:|---:|---:|---:|---:|
| Y1 | 416,785 | 95,000 | 321,785 | 22,525 | 344,310 |
| Y2 | 344,310 | 95,000 | 249,310 | 17,452 | **266,762** |

Interest Y1: \(321{,}785 \times 0.07 = 22{,}524.95 \rightarrow \$22{,}525\).  
Interest Y2: \(249{,}310 \times 0.07 = 17{,}451.70 \rightarrow \$17{,}452\).

ROU amort/year pre-remeas: \(\mathrm{round}(416{,}785/5) = \$83{,}357\).  
\[
\mathrm{ROU}_{1/1/\mathrm{Y3}} = 416{,}785 - 2\times 83{,}357 = \$250{,}071
\]

**c. December 31, Year 1 period-end adjusting JEs (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 22,525 | |
| Lease Liability | | 22,525 |

**Check:** Dr = Cr = 22,525. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense—ROU Asset | 83,357 | |
| Accumulated Amortization—ROU Asset | | 83,357 |

**Check:** Dr = Cr = 83,357. **Balanced.**

**d. January 1, Year 3 remeasurement**  
\[
\mathrm{PV}(6\%,\,3,\,-95{,}000,\,-35{,}000,\,1) = \$298{,}559
\]

| Item | Amount |
|---|---:|
| Remeasured LL | $298,559 |
| LL before remeasurement | 266,762 |
| **Δ LL → ROU** | **$31,797** |
| ROU after remeasurement | \(250{,}071 + 31{,}797 = \$281{,}868\) |

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset—Equipment | 31,797 | |
| Lease Liability | | 31,797 |
| *PO now reasonably certain; remeasure at 6%; adjust ROU* | | |

**Check:** Dr = Cr = 31,797. **Balanced.**

Payment 1/1/Y3:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 95,000 | |
| Cash | | 95,000 |

LL after payment: \(298{,}559 - 95{,}000 = \$203{,}559\).  
Interest Y3: \(203{,}559 \times 0.06 = 12{,}213.54 \rightarrow \$12{,}214\).  
ROU amort Y3 (remaining life 5 years): \(281{,}868 / 5 = \$56{,}373.60 \rightarrow \$56{,}374\) (or $56,374 with later plug; use **$56,374**).

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 12,214 | |
| Lease Liability | | 12,214 |

**Check:** Dr = Cr = 12,214. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense—ROU Asset | 56,374 | |
| Accumulated Amortization—ROU Asset | | 56,374 |

**Check:** Dr = Cr = 56,374. **Balanced.**  
EOY Y3 LL: \(203{,}559 + 12{,}214 = \$215{,}773\).

**e. Settlement of purchase option (conceptual amounts)**  
When LL has accreted to **$35,000** at exercise date:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Cash | | 35,000 |

Then reclassify **net ROU** carrying amount to **Equipment** (same pattern as Q1-f).

**Key insight:** Same LO 17-11 mechanics as Q1 with all new numbers—remeasurement always **balances** (ROU ↔ LL) and subsequent **period-end adjusting JEs** use the **new discount rate** and the **revised ROU amort period**.

---

### Q3 — CORE alternate angle — Residual-guarantee remeasurement (rate not updated) + modification classification + period-end JE

**LO:** LO 17-11  
**Concept:** Remeasure-only for change in probable residual-guarantee payment (original discount rate retained); ROU/LL adjusting JE; period-end interest after remeasurement; classify separate lease vs modified lease vs reassess+remeasure events  
**Scenario — Part A (residual remeasurement):**  
**Harborlight Transit Co.** leases a fleet support vehicle on **January 1, Year 1** (finance lease):

| Fact | Amount / term |
|---|---|
| Term | 5 years; economic life 6 years |
| Annual payment (annuity-due, Jan 1) | **$88,000** |
| Guaranteed residual value (contractual) | **$15,000** |
| Amount **probable of being owed** at commencement | **$0** (expected residual ≥ guarantee) |
| Lessee discount rate | **6%** |
| On **January 1, Year 3** (before payment) | Technology shift lowers expected residual; Harborlight now expects to owe **$10,000** under the GRV at lease end |

**Required — Part A:**  
a. Does the change cause **classification reassessment**, **remeasurement only**, or both? Is the **discount rate updated**?  
b. Compute commencement LL/ROU (PV of rental payments only), the Y1–Y2 liability schedule, and LL/ROU on January 1, Year 3 **before** remeasurement.  
c. Remeasure the liability (include PV of expected **$10,000** residual payment); record the remeasurement JE.  
d. **(Emphasis)** After the January 1, Year 3 **$88,000** payment, record the **December 31, Year 3 period-end interest adjusting JE** (still at **6%**).

**Scenario — Part B (modification / event classification):**  
For each independent event, conclude **(1) new/separate lease**, **(2) remeasurement only**, or **(3) classification reassessment and remeasurement**. Briefly justify.

1. Lessee adds adjacent warehouse square footage for the remaining term; the **rent increase equals the standalone market price** for that space.  
2. Same expansion, but rent for the added space is **well below** standalone market.  
3. Parties **extend** the lease term by two years (single contract amendment; no new asset).  
4. Lessee now **reasonably certain** to exercise a purchase option that was not expected at commencement.  
5. Index-based variable payments change solely because the CPI index moved (no other change).  
6. A sales contingency resolves so that previously variable amounts become **fixed** for the remaining term.

**Answer key:**  

**Part A**  

**a.** Change in amounts probable under a **residual value guarantee** → **remeasurement only** (no classification reassessment).  
Discount rate: **do not update** — use the **original 6%** commencement rate (ASC 842-20-35-5(b)).

**b. Commencement PV (rentals only; $0 residual expected)**  
\[
\mathrm{PV}(6\%,\,5,\,-88{,}000,\,0,\,1) = \$392{,}929
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset—Vehicle | 392,929 | |
| Lease Liability | | 392,929 |

**Check:** Dr = Cr = 392,929. **Balanced.**

| Period | Beg. LL | Payment | After pmt | Interest 6% | End. LL |
|---|---:|---:|---:|---:|---:|
| Y1 | 392,929 | 88,000 | 304,929 | 18,296 | 323,225 |
| Y2 | 323,225 | 88,000 | 235,225 | 14,114 | **249,339** |

Interest Y1: \(304{,}929 \times 0.06 = 18{,}295.74 \rightarrow \$18{,}296\).  
Interest Y2: \(235{,}225 \times 0.06 = 14{,}113.50 \rightarrow \$14{,}114\).

ROU amort/year (over 5-year term; no ownership expected): \(\mathrm{round}(392{,}929/5) = \$78{,}586\).  
\[
\mathrm{ROU}_{1/1/\mathrm{Y3}} = 392{,}929 - 2\times 78{,}586 = \$235{,}757
\]  
LL before remeasurement = **$249,339**.

**c. Remeasurement at original 6%**  
Remaining: 3 annuity-due payments of $88,000 + $10,000 residual at end of Year 5:  
\[
\mathrm{PV}(6\%,\,3,\,-88{,}000,\,-10{,}000,\,1) = \$257{,}735
\]

| Item | Amount |
|---|---:|
| Remeasured LL | $257,735 |
| Prior LL | 249,339 |
| **Increase** | **$8,396** |
| ROU after | \(235{,}757 + 8{,}396 = \$244{,}153\) |

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset—Vehicle | 8,396 | |
| Lease Liability | | 8,396 |
| *Remeasure for probable residual payment; rate remains 6%* | | |

**Check:** Dr = Cr = 8,396. **Balanced.**

**d. Payment then period-end interest adjusting JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 88,000 | |
| Cash | | 88,000 |

LL after payment: \(257{,}735 - 88{,}000 = \$169{,}735\).  
Interest Y3: \(169{,}735 \times 0.06 = 10{,}184.10 \rightarrow \$10{,}184\).

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,184 | |
| Lease Liability | | 10,184 |
| *Period-end adjusting JE after residual remeasurement (original rate)* | | |

**Check:** Dr = Cr = 10,184. **Balanced.**  
EOY Y3 LL: \(169{,}735 + 10{,}184 = \$179{,}919\).

**Part B — Classification answers**

| # | Conclusion | Why |
|---|---|---|
| 1 | **(1) New/separate lease** | Additional ROU **and** payments increase commensurate with **standalone price** (ASC 842-10-25-8) |
| 2 | **(3) Reassess + remeasure** | Additional space **not** at standalone price → single modified lease |
| 3 | **(3) Reassess + remeasure** | Change in **lease term** |
| 4 | **(3) Reassess + remeasure** | Change in assessment of **purchase option** exercise |
| 5 | **Neither remeasurement nor new lease** for the index move alone | Change in reference index/rate is **not** resolution of a contingency for remeasurement of the liability under 842-10-35-4(b) (variable payments based on index are remeasured when remeasurement is otherwise required; a pure index tick is not itself a remeasurement trigger of the types tested here) |
| 6 | **(2) Remeasurement only** | Contingency resolved → variable payments become **fixed**; no classification reassessment |

**Key insight:** Not every mid-life change is a “new lease.” **Standalone-priced additional rights** create a **separate contract**. Term/PO changes force **reassessment + remeasurement** (often with a **new rate**). Residual-guarantee probability and contingency resolution are **remeasure-only** events that **keep the original discount rate**. In all remeasurement cases the JE is the same shape: **ROU ↔ Lease Liability**, then resume **period-end interest (and amort) adjusting entries**.

---

### Q4 — MC — Modification vs remeasurement classification

**LO:** LO 17-11  
**Concept:** Classify lease modification / event as separate lease, remeasure-only, or reassess+remeasure; identify correct discount-rate treatment  
**Question:**  
On January 1, Year 1, **Solstice Bakery LLC** entered a 6-year finance lease of an oven line. On January 1, Year 4, two independent facts arise in **separate** scenarios:

- **Scenario X:** Solstice and the lessor amend the contract to add a second oven line for the remaining three years. The payment increase **equals the market standalone rental** for a comparable oven line.  
- **Scenario Y:** Solstice’s estimate of the amount it will owe under a residual-value guarantee increases by $12,000; no other terms change.

Which statement is **correct**?

- A) Both X and Y are accounted for as **new separate leases**; both use a newly determined discount rate.  
- B) X is a **separate lease**; Y is a **remeasurement only** of the existing lease using the **original** discount rate.  
- C) X and Y both require **classification reassessment and remeasurement** with an **updated** discount rate.  
- D) Y is a **separate lease**; X is remeasurement only because no purchase option changed.

**Answer:** **B.**  
Scenario X grants an **additional right of use** at a **standalone price** → account for as a **separate contract** (new lease); original lease accounting continues unchanged.  
Scenario Y is a change in amounts **probable under a residual value guarantee** → **remeasure** the lease liability (offset to ROU) **without** classification reassessment and **without** updating the discount rate.

---

### Q5 — MC — Period-end adjusting effects after remeasurement

**LO:** LO 17-11  
**Concept:** Period-end adjusting JE after purchase-option remeasurement — which accounts and rate  
**Question:**  
After a January 1 remeasurement that increased both the lease liability and ROU asset because a purchase option became reasonably certain (discount rate updated from 8% to 7%), what is the **correct December 31 period-end adjusting pair** for a finance lease (ignore the cash lease payment already recorded on January 1)?

- A) Debit Lease expense (single amount); credit Cash — using straight-line rent only.  
- B) Debit Interest expense (beginning post-payment LL × **7%**); credit Lease liability; **and** debit Amortization expense; credit Accumulated amortization—ROU (over remaining **economic life** if ownership/PO reasonably certain).  
- C) Debit Interest expense (LL × **original 8%**); credit ROU asset only.  
- D) Debit ROU asset; credit Interest expense for the full remaining lease payments.

**Answer:** **B.**  
Finance-lease **period-end adjusting JEs** continue after remeasurement: **interest** uses the **updated** rate on the **post-payment** liability balance, and **ROU amortization** follows the revised pattern (remaining economic life when PO is reasonably certain). Remeasurement itself is **not** an income-statement “interest” entry—the ROU↔LL true-up is balance-sheet only.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV annuity-due formulas; interest = post-payment bal × rate; remeasurement deltas tie)
- [x] Core demo path from LO 17-11 / Demo 17-11 (modifications, remeasurement, rate exceptions) — not Expanding Your Knowledge sidebars
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
