# Agent 284 — CORE DEMO — LO 17-2

**Chapter:** 17  
**LO title:** Accounting for a Basic Finance Lease by a Lessee  
**Critical gap LO:** yes

## Concept list for this pack
- Classify a lease as a **finance lease** when at least one of the five ASC 842 criteria is met (ownership transfer, reasonably certain purchase option, major part of economic life, substantially all of fair value, specialized asset)
- **Initial recognition JE:** debit Right-of-use (ROU) asset and credit Lease liability for the PV of lease payments (annuity-due / payments in advance)
- Discount rate: use the **rate implicit in the lease if known**; otherwise the lessee’s incremental borrowing rate
- **Lease liability schedule** under the **effective interest method** (first payment all principal when paid on commencement day)
- **Period-end adjusting JEs (emphasis):** accrue interest expense (increase lease liability) and record straight-line ROU amortization expense
- Subsequent measurement: payments reduce lease liability (principal + previously accrued interest); interest declines as liability declines
- **Maturity/settlement:** final payment clears remaining lease liability; final period amortization brings ROU carrying amount to zero when asset reverts to lessor with zero residual
- **Classification/presentation:** finance lease reports **interest expense** and **amortization expense** separately; split lease liability into **current** and **noncurrent** (current ≈ next payment)

---

### Q1 — CORE — Basic finance lease full cycle (initial recognition, schedule, period-end adjusting JEs, maturity)
**LO:** LO 17-2  
**Concept:** Lessee basic finance lease—initial ROU/liability recognition, effective-interest liability schedule, period-end interest & ROU amortization adjusting JEs, BS/IS presentation, runoff to maturity  
**Scenario:**  
On **January 1, Year 1** (commencement), **Meridian Forge LLC** (lessee, calendar year-end) enters a **4-year noncancellable** lease for specialized production equipment with **Lumen Capital Leasing**. Facts:

1. Annual lease payments of **$55,000** are due **January 1 of Year 1, Year 2, Year 3, and Year 4** (payments in advance / annuity due).  
2. Fair value of the equipment at commencement equals the present value of the lease payments.  
3. Estimated economic life of the equipment is **4 years**.  
4. The asset reverts to the lessor at the end of the lease; **no** renewal or purchase option; estimated residual value **$0**; no residual value guarantee.  
5. Lessor’s **implicit rate is 7%** and is **known** by Meridian. Meridian’s incremental borrowing rate is **8%**.  
6. No initial direct costs, prepaid rent, or lease incentives. ROU asset equals the initial lease liability.  
7. Meridian credits the ROU asset directly for amortization (no accumulated amortization contra), consistent with the chapter’s demo style. Amortize the ROU asset **straight-line over the lease term**.

**Required:**  
a. Determine the proper **lease classification** for Meridian and identify which criterion (or criteria) is met. State the discount rate Meridian should use.  
b. Compute the **lease liability** and **right-of-use asset** at commencement.  
c. Prepare the complete **lease liability schedule** (payment, interest, liability change, ending balance) for all four payment dates.  
d. Prepare **all Year 1 journal entries**, including **period-end adjusting entries**.  
e. Show Year 1 **balance sheet** (ROU asset; current and noncurrent lease liability) and **income statement** lease-related expenses.  
f. Prepare **Year 2 journal entries** (payment + period-end adjusting).  
g. Prepare **Year 4 (final year) journal entries** through **maturity/settlement** (final payment and final amortization). Confirm ending ROU and lease liability balances.

**Answer key:**  

**a. Classification and rate**  
Finance lease — **at least one** criterion is met:

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to lessor | No |
| 2. Purchase option reasonably certain | None | No |
| 3. Lease term = major part of economic life | 4 / 4 = **100%** (≥ 75% bright-line guidance) | **Yes** |
| 4. PV of payments ≈ substantially all of FV | PV = FV by construction (≥ 90% guidance) | **Yes** |
| 5. Specialized / no alternative use | Not needed once another criterion is met (equipment is routinely leasable in other demos; here term/PV already suffice) | — |

**Discount rate:** use the **7% implicit rate** (known). Incremental borrowing rate of 8% is **not** used when the implicit rate is known.

**b. Initial measurement**  
Present value of an annuity due of $55,000 for 4 periods at 7%:

\[
PV = 55{,}000 + 55{,}000 \times \frac{1-(1.07)^{-3}}{0.07} = \mathbf{\$199{,}337.38}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 199,337.38 | |
| Lease Liability | | 199,337.38 |
| *Commencement — basic finance lease; ROU = LL (no adjustments)* | | |

**Check:** Dr = Cr = 199,337.38.

**c. Lease liability schedule (effective interest, 7%)**

| Date | Lease payment | Interest on liability (7%) | Liability change (payment − interest) | Lease liability balance |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 (commencement) | — | — | — | 199,337.38 |
| Jan. 1, Y1 | 55,000.00 | 0.00 | 55,000.00 | 144,337.38 |
| Jan. 1, Y2 | 55,000.00 | 10,103.62 | 44,896.38 | 99,441.00 |
| Jan. 1, Y3 | 55,000.00 | 6,960.87 | 48,039.13 | 51,401.87 |
| Jan. 1, Y4 | 55,000.00 | 3,598.13 | 51,401.87 | 0.00 |
| **Totals** | **220,000.00** | **20,662.62** | **199,337.38** | |

Interest computations:  
- Y1 accrual base: \(144{,}337.38 \times 0.07 = 10{,}103.62\)  
- Y2 accrual base: \(99{,}441.00 \times 0.07 = 6{,}960.87\)  
- Y3 accrual base: \(51{,}401.87 \times 0.07 = 3{,}598.13\)  

(First payment on day one carries **zero** interest because no time has elapsed.)

**d. Year 1 journal entries**

*January 1, Year 1 — initial recognition*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 199,337.38 | |
| Lease Liability | | 199,337.38 |

**Check:** Dr = Cr = 199,337.38.

*January 1, Year 1 — lease payment (all principal)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 55,000.00 | |
| Cash | | 55,000.00 |

**Check:** Dr = Cr = 55,000.00.

*December 31, Year 1 — **period-end adjusting JE** — interest on lease liability*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,103.62 | |
| Lease Liability | | 10,103.62 |
| *Accrue full-year interest: 7% × $144,337.38* | | |

**Check:** Dr = Cr = 10,103.62.  
Liability after accrual: \(144{,}337.38 + 10{,}103.62 = \mathbf{\$154{,}441.00}\).

*December 31, Year 1 — **period-end adjusting JE** — ROU amortization*

Annual SL amortization = \(199{,}337.38 / 4 = 49{,}834.345\) → record **$49,834.35** (round; last year absorbs $0.02).

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 49,834.35 | |
| Right-of-Use Asset | | 49,834.35 |
| *Straight-line over 4-year lease term* | | |

**Check:** Dr = Cr = 49,834.35.  
ROU carrying amount Dec. 31, Y1: \(199{,}337.38 - 49{,}834.35 = \mathbf{\$149{,}503.03}\).

**e. Year 1 financial statement impact**

**Income statement — Year 1**

| Expense | Amount |
|---|---:|
| Interest expense—lease liability | $10,103.62 |
| Amortization expense—right-of-use asset | 49,834.35 |
| **Total lease-related expense (finance lease pattern)** | **$59,937.97** |

**Balance sheet — December 31, Year 1**

| Item | Amount |
|---|---:|
| **Assets — noncurrent** | |
| Right-of-use asset (net) | $149,503.03 |
| **Liabilities — current** | |
| Lease liability (next payment = $10,103.62 interest + $44,896.38 principal) | $55,000.00 |
| **Liabilities — noncurrent** | |
| Lease liability ($154,441.00 total − $55,000.00 current) | $99,441.00 |

**f. Year 2 journal entries**

*January 1, Year 2 — lease payment* (pays accrued interest + principal reduction)

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 55,000.00 | |
| Cash | | 55,000.00 |

**Check:** Dr = Cr = 55,000.00.  
Balance after payment: \(154{,}441.00 - 55{,}000.00 = 99{,}441.00\).

*December 31, Year 2 — period-end interest*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,960.87 | |
| Lease Liability | | 6,960.87 |

**Check:** Dr = Cr = 6,960.87. Total LL = \(99{,}441.00 + 6{,}960.87 = 106{,}401.87\).

*December 31, Year 2 — period-end ROU amortization*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 49,834.35 | |
| Right-of-Use Asset | | 49,834.35 |

**Check:** Dr = Cr = 49,834.35. End ROU CV = \(149{,}503.03 - 49{,}834.35 = 99{,}668.68\).

**g. Year 4 maturity / settlement**

After Dec. 31, Year 3 adjusting entries:  
- Interest accrued for Y3: **$3,598.13**; principal before that accrual was **$51,401.87**; total LL Dec. 31 Y3 = **$55,000.00**.  
- ROU CV at Jan. 1 Y4 after three amortizations of $49,834.35: \(199{,}337.38 - 3\times 49{,}834.35 = 49{,}834.33\).

*January 1, Year 4 — final lease payment (settles liability)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 55,000.00 | |
| Cash | | 55,000.00 |

**Check:** Dr = Cr = 55,000.00. **Lease liability = $0**.

*December 31, Year 4 — final ROU amortization (no interest; liability already settled)*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 49,834.33 | |
| Right-of-Use Asset | | 49,834.33 |
| *Rounding plug so ROU reaches zero* | | |

**Check:** Dr = Cr = 49,834.33. **ROU asset = $0**.

At lease end (asset reverts; zero residual), both ROU asset and lease liability are fully run off — **maturity/settlement** without a separate third-party disposal gain or loss.

**Key insight:** A basic finance lease puts a ROU asset and lease liability on the books at PV. Subsequent accounting is **two period-end adjusting engines**: (1) effective-interest **interest expense** that **increases** the lease liability, and (2) straight-line **amortization expense** that **decreases** the ROU asset. Cash payments hit the liability (not “rent expense”). Front-loaded total expense vs an operating lease’s single straight-line lease cost.

---

### Q2 — CORE number variant — Basic finance lease (different term, rate, and payments)
**LO:** LO 17-2  
**Concept:** Number-variant twin—lessee finance lease initial recognition, full liability schedule, period-end adjusting JEs, and Year-1 presentation  
**Scenario:**  
On **January 1, Year 1**, **CedarPoint Packaging Inc.** leases a packaging line under a **5-year noncancellable** finance lease. Payments of **$40,000** are due **each January 1 beginning Year 1** (annuity due). Economic life of the asset is **5 years**; asset reverts to the lessor; residual **$0**; no purchase option. Lessor’s implicit rate **5%** is known to CedarPoint (IBR 6.5% is therefore irrelevant). No ROU adjustments. Calendar year-end. Credit ROU directly for amortization; amortize SL over the **lease term**.

**Required:**  
a. Compute commencement **lease liability / ROU asset**.  
b. Prepare the **lease liability schedule** for all five payments.  
c. Prepare **all Year 1 journal entries** (initial recognition, payment, and both period-end adjusting entries).  
d. State December 31, Year 1 **ROU carrying amount**, **total lease liability**, and the **current / noncurrent** split.  
e. Compute **Year 1 total** finance-lease expense (interest + amortization).

**Answer key:**  

**a. Initial PV**  
\[
PV = 40{,}000 + 40{,}000 \times \frac{1-(1.05)^{-4}}{0.05} = \mathbf{\$181{,}838.02}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 181,838.02 | |
| Lease Liability | | 181,838.02 |

**Check:** Dr = Cr = 181,838.02.

**b. Lease liability schedule (5%, effective interest)**

| Date | Payment | Interest (5%) | Change | Balance |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 commence | — | — | — | 181,838.02 |
| Jan. 1, Y1 | 40,000.00 | 0.00 | 40,000.00 | 141,838.02 |
| Jan. 1, Y2 | 40,000.00 | 7,091.90 | 32,908.10 | 108,929.92 |
| Jan. 1, Y3 | 40,000.00 | 5,446.50 | 34,553.50 | 74,376.42 |
| Jan. 1, Y4 | 40,000.00 | 3,718.82 | 36,281.18 | 38,095.24 |
| Jan. 1, Y5 | 40,000.00 | 1,904.76 | 38,095.24 | 0.00 |
| **Totals** | **200,000.00** | **18,161.98** | **181,838.02** | |

Interest checks:  
\(141{,}838.02\times0.05=7{,}091.90\); \(108{,}929.92\times0.05=5{,}446.496\to5{,}446.50\);  
\(74{,}376.42\times0.05=3{,}718.821\to3{,}718.82\); \(38{,}095.24\times0.05=1{,}904.762\to1{,}904.76\).

**c. Year 1 journal entries**

*Jan. 1 — recognition*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 181,838.02 | |
| Lease Liability | | 181,838.02 |

**Check:** 181,838.02 = 181,838.02.

*Jan. 1 — payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 40,000.00 | |
| Cash | | 40,000.00 |

**Check:** 40,000 = 40,000.

*Dec. 31 — period-end interest adjusting JE*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 7,091.90 | |
| Lease Liability | | 7,091.90 |

**Check:** 7,091.90 = 7,091.90.  
Total LL Dec. 31 Y1: \(141{,}838.02 + 7{,}091.90 = \mathbf{\$148{,}929.92}\).

*Dec. 31 — period-end ROU amortization adjusting JE*  
Annual amort = \(181{,}838.02 / 5 = 36{,}367.604\) → **$36,367.60** (years 1–4); year 5 **$36,367.62**.

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 36,367.60 | |
| Right-of-Use Asset | | 36,367.60 |

**Check:** 36,367.60 = 36,367.60.

**d. December 31, Year 1 balances**

| Item | Amount |
|---|---:|
| ROU asset CV | \(181{,}838.02 - 36{,}367.60 = \mathbf{\$145{,}470.42}\) |
| Total lease liability | **$148,929.92** |
| Current lease liability | **$40,000.00** (next payment) |
| Noncurrent lease liability | \(148{,}929.92 - 40{,}000.00 = \mathbf{\$108{,}929.92}\) |

**e. Year 1 total finance-lease expense**  
Interest \(7{,}091.90\) + Amortization \(36{,}367.60\) = **$43,459.50**.

**Key insight:** Changing n, r, and PMT only rescales the same **Demo 17-2 engine**: PV at commencement, zero-interest first payment, period-end interest accretion + SL ROU amortization, current liability ≈ next cash payment.

---

### Q3 — CORE alternate angle — Period-end adjusting JEs, interim liability measurement, and maturity runoff
**LO:** LO 17-2  
**Concept:** Period-end adjusting JE emphasis—full-year and interim (month-fraction) interest accrual; ROU amortization; current/noncurrent presentation; final-year settlement  
**Scenario:**  
**Harborline Logistics Co.** commenced a **3-year finance lease** on **January 1, Year 1** for a delivery truck fleet unit. Annual payments of **$72,000** are due **January 1 of Year 1, Year 2, and Year 3**. Implicit rate **4%** (known). Economic life **3 years**; reverts to lessor; residual $0; no purchase option. Initial ROU = LL = PV of payments. No other adjustments. Year-end is December 31. Management prepares **monthly internal reports** and needs the lease liability at **October 31, Year 1** as well as the formal December 31 entries.

Commencement PV (given / computed): **$207,798.82**.  
After the January 1, Year 1 payment, unpaid principal is **$135,798.82**.

**Required:**  
a. Prepare the **lease liability schedule** (three payments).  
b. Compute the **lease liability at October 31, Year 1** (after 10/12 of the Year-1 interest has accrued) and the **formal December 31, Year 1 period-end adjusting entries** (interest and ROU amortization).  
c. Prepare **Year 2** payment entry and **December 31, Year 2** period-end adjusting entries.  
d. Prepare **Year 3 maturity** entries (final payment + final amortization) and show that ROU and LL end at zero.  
e. For December 31, Year 1, state **current vs noncurrent** lease liability and the **income-statement presentation** labels (not a single “lease expense”).

**Answer key:**  

**a. Lease liability schedule (4%)**

| Date | Payment | Interest (4%) | Change | Balance |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 commence | — | — | — | 207,798.82 |
| Jan. 1, Y1 | 72,000.00 | 0.00 | 72,000.00 | 135,798.82 |
| Jan. 1, Y2 | 72,000.00 | 5,431.95 | 66,568.05 | 69,230.77 |
| Jan. 1, Y3 | 72,000.00 | 2,769.23 | 69,230.77 | 0.00 |

Interest: \(135{,}798.82 \times 0.04 = 5{,}431.9528 \to 5{,}431.95\);  
\(69{,}230.77 \times 0.04 = 2{,}769.2308 \to 2{,}769.23\).

**b. Interim measurement and Year 1 period-end adjusting JEs**

Full-year interest to accrue during Year 1 = **$5,431.95**.

**October 31, Year 1 lease liability** (measurement date between payments):  
\[
135{,}798.82 + \left(\frac{10}{12}\times 5{,}431.95\right) = 135{,}798.82 + 4{,}526.625 \approx \mathbf{\$140{,}325.45}
\]  
(textbook style: add month-fraction of the next scheduled interest to the post-payment principal balance).

*December 31, Year 1 — interest adjusting JE (full year)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,431.95 | |
| Lease Liability | | 5,431.95 |

**Check:** Dr = Cr = 5,431.95.  
Total LL Dec. 31 Y1: \(135{,}798.82 + 5{,}431.95 = \mathbf{\$141{,}230.77}\).

*December 31, Year 1 — ROU amortization adjusting JE*  
\(207{,}798.82 / 3 = 69{,}266.273\ldots\) → **$69,266.27** in Y1 and Y2; **$69,266.28** in Y3.

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 69,266.27 | |
| Right-of-Use Asset | | 69,266.27 |

**Check:** Dr = Cr = 69,266.27.  
ROU CV Dec. 31 Y1: \(207{,}798.82 - 69{,}266.27 = \mathbf{\$138{,}532.55}\).

**c. Year 2**

*January 1, Year 2 — payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 72,000.00 | |
| Cash | | 72,000.00 |

**Check:** 72,000 = 72,000. Post-payment principal = \(141{,}230.77 - 72{,}000.00 = 69{,}230.77\).

*December 31, Year 2 — interest*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 2,769.23 | |
| Lease Liability | | 2,769.23 |

**Check:** 2,769.23 = 2,769.23. Total LL = \(69{,}230.77 + 2{,}769.23 = 72{,}000.00\).

*December 31, Year 2 — ROU amortization*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 69,266.27 | |
| Right-of-Use Asset | | 69,266.27 |

**Check:** 69,266.27 = 69,266.27.  
ROU CV = \(138{,}532.55 - 69{,}266.27 = 69{,}266.28\).

**d. Year 3 maturity / settlement**

*January 1, Year 3 — final payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 72,000.00 | |
| Cash | | 72,000.00 |

**Check:** 72,000 = 72,000. **LL = $0**.

*December 31, Year 3 — final amortization (no interest)*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 69,266.28 | |
| Right-of-Use Asset | | 69,266.28 |

**Check:** 69,266.28 = 69,266.28. **ROU = $0**.

**e. Presentation — December 31, Year 1**

| Classification | Amount / label |
|---|---|
| Current lease liability | **$72,000.00** (= next payment = $5,431.95 interest + $66,568.05 principal) |
| Noncurrent lease liability | \(141{,}230.77 - 72{,}000.00 = \mathbf{\$69{,}230.77}\) |
| Income statement | **Interest expense** $5,431.95 **and** **Amortization expense** $69,266.27 **separately** (finance lease — **not** a single straight-line lease cost) |

**Key insight (emphasis):** The liability schedule is built on **payment dates**, but reporting dates require **period-end adjusting entries**. Accrue interest for the elapsed fraction of the interest period (e.g., 10/12 at October 31; 12/12 at December 31) by **increasing the lease liability**; amortize ROU for the same reporting period by **decreasing the ROU asset**. At maturity the final cash payment zeros the liability; the final amortization zeros the ROU asset.

---

### Q4 — MC — Discount rate selection for lessee measurement
**LO:** LO 17-2  
**Concept:** Classification/method—rate used to measure the lease liability when the implicit rate is known  
**Question:**  
At commencement of a finance lease, the lessor’s implicit interest rate is **6%** and is **readily determinable** by the lessee. The lessee’s incremental borrowing rate for a similar loan is **7.5%**. Which rate should the lessee use to measure the lease liability and ROU asset?

- A) 7.5%, because the incremental borrowing rate always better reflects the lessee’s credit risk  
- B) 6%, the rate implicit in the lease, because it is known / readily determinable  
- C) The average of 6% and 7.5%  
- D) 0%, because the first payment is entirely principal under an annuity-due lease  

**Answer:** **B.** ASC 842 requires the lessee to discount lease payments using the **rate implicit in the lease when that rate can be readily determined**; only if the implicit rate is not readily determinable does the lessee use its incremental borrowing rate. (The first payment being all principal affects the **interest schedule**, not the choice of discount rate.)

---

### Q5 — MC — Finance lease income-statement presentation
**LO:** LO 17-2  
**Concept:** Classification/presentation—finance lease expense pattern vs operating lease single lease cost  
**Question:**  
For a **basic finance lease**, how does the lessee present lease-related amounts on the **income statement** after commencement?

- A) A single straight-line “lease expense” equal to the cash payment each period  
- B) A single straight-line “lease expense” equal to the total undiscounted payments divided by the lease term  
- C) **Interest expense** on the lease liability (effective interest method) **and** **amortization expense** on the ROU asset (typically straight-line), reported separately  
- D) Only amortization expense; interest is capitalized into the ROU asset each period  

**Answer:** **C.** Finance leases recognize **interest expense** (effective interest on the liability) and **amortization expense** (typically SL on the ROU asset) as **separate** income statement items. A single straight-line lease cost is the **operating lease** pattern (LO 17-3), not the basic finance lease pattern in LO 17-2.

---

### Self-check
- [x] Every JE balances (Dr = Cr on each entry)
- [x] Math recomputed (PV annuity-due formulas; interest = rate × beginning liability after payment; schedules roll to zero)
- [x] Core demo not sidebar-only (Demo 17-2 / Review 17-2 path: basic finance lease, zero residual)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4 rate selection; Q5 presentation)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
