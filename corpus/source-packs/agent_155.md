# Agent 155 — CORE DEMO — LO 17-4

**Chapter:** 17  
**LO title:** Account for complex finance leases for a lessee  
**Critical gap LO:** yes

## Concept list for this pack
- **Initial recognition JE:** measure finance lease liability at PV of lease payments (fixed payments + purchase option if reasonably certain + **only probable amount owed** under residual value guarantee); measure ROU = liability − incentives + initial direct costs + prepaid lease payments
- **Subsequent measurement schedule (emphasis):** multi-period lease liability amortization table (effective interest) and ROU straight-line amortization roll-forward
- **Period-end adjusting JE:** accrue interest expense on lease liability; record amortization expense on ROU asset
- **Disposal / maturity / settlement JE:** final residual-guarantee cash settlement; exercise of purchase option and reclass ROU residual basis to equipment
- **Classification / presentation / disclosure:** finance vs operating criteria; current vs noncurrent lease liability; interest + amortization (not single lease expense) for finance leases
- **Number-variant twin:** same GRV finance-lease skill path with all facts and amounts changed
- **Complex payment components:** residual guarantee (classification = 100% GRV; liability = probable excess only); purchase option reasonably certain; initial direct costs

---

### Q1 — CORE — Northline finance lease with residual guarantee, IDC, and full liability schedule
**LO:** LO 17-4  
**Concept:** Complex finance lease for lessee — initial recognition (IDC + residual guarantee), subsequent measurement schedule (emphasis), period-end interest and ROU amortization, residual settlement, current/noncurrent presentation  
**Scenario:**  
On **January 1, Year 1** (commencement), **Northline Precision LLC** leases specialized cutting equipment under a **3-year noncancellable** contract. Northline’s reporting year ends **December 31**. Facts:

| Item | Amount / term |
|---|---|
| Fair value of equipment at commencement | **$95,000** |
| Estimated economic life | **3 years** |
| Annual lease payment (due **January 1** each year, beginning Year 1) | **$30,000** |
| Guaranteed residual value (due if residual is short at end of Year 3 / Jan 1 Year 4) | **$12,000** |
| Expected residual value at lease end (Northline’s estimate) | **$8,000** |
| Rate implicit in the lease (known to Northline) | **6%** |
| Incremental borrowing rate | 7% (not used — implicit rate known) |
| Purchase / renewal options | None; asset reverts to lessor |
| Initial direct costs (legal fees for **execution** of the lease), paid **December 28, Year 0** | **$1,500** |
| Lease incentives | None |

Northline uses the **75% / 90%** bright lines for classification when judgment is required. Round interest in the liability schedule to the **nearest dollar** (consistent effective-interest roll-forward).

**Required:**  
a. Record the **December 28, Year 0** entry for initial direct costs.  
b. **Classify** the lease for Northline; support with the applicable criterion(ia). For criterion 4, compute PV of lease payments using **100% of the guaranteed residual**.  
c. Compute the **lease liability** and **right-of-use asset** at January 1, Year 1 (liability uses only the **probable** residual amount owed).  
d. Prepare the full **lease liability subsequent measurement schedule** (emphasis): dates through residual settlement; columns for payment, interest, principal (liability reduction), and ending liability.  
e. Record **all Year 1 journal entries** (commencement ROU/liability, first payment, Dec 31 interest, Dec 31 ROU amortization).  
f. Show **December 31, Year 1** balance sheet presentation of the ROU asset and lease liability (**current** vs **noncurrent**) and Year 1 income statement amounts.  
g. Record **Year 2** payment and period-end adjusting entries.  
h. Record **Year 3** payment, period-end interest and amortization, and the **settlement** of the residual guarantee on December 31, Year 3 / January 1, Year 4 when the equipment’s actual fair value is **$8,000** as expected.

**Answer key:**  

**a. December 28, Year 0 — Initial direct cost**

| Account | Debit | Credit |
|---|---:|---:|
| Initial Direct Cost | 1,500 | |
| Cash | | 1,500 |
| *Legal fees incremental to obtaining the lease (execution)* | | |

**Check:** Dr 1,500 = Cr 1,500. **Balanced.**

**b. Classification — finance lease**  
At least one classification criterion is met:

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to lessor | No |
| 2. Purchase option | None | No |
| 3. Lease term length | 3-year term ÷ 3-year life = **100% ≥ 75%** | **Yes** |
| 4. PV of lease payments | PV including **100% of $12,000 GRV** (below) vs 90% × $95,000 = **$85,500** | **Yes** |
| 5. No alternative use | Not indicated (routinely leasable class of equipment) | No |

**Criterion 4 computation** (annuity-due TYPE=1; residual as FV at end of term):  
PV = PV(0.06, 3, −30000, −12000, 1) ≈ **$95,077**  
$95,077 > $85,500 → criterion 4 also met.  
*(IDC does not affect classification. Implicit rate 6% is used.)*

**Finance lease.**

**c. Lease liability and ROU asset**

Probable amount owed under residual guarantee = $12,000 − $8,000 = **$4,000**.

Lease liability = PV(0.06, 3, −30000, −4000, 1) ≈ **$88,360** (rounded).

| Component | Amount |
|---|---:|
| Initial measurement of lease liability | $88,360 |
| − Lease incentives | 0 |
| + Initial direct costs | 1,500 |
| + Prepaid lease payments at commencement (before reclass of first payment) | 0 |
| **Right-of-use asset** | **$89,860** |

**d. Subsequent measurement schedule — lease liability (emphasis)**

| Date | Lease payment | Interest (6%) | Principal reduction | Lease liability ending |
|---|---:|---:|---:|---:|
| Jan 1, Year 1 (initial) | — | — | — | **88,360** |
| Jan 1, Year 1 | 30,000 | 0 | 30,000 | 58,360 |
| Jan 1, Year 2 | 30,000 | 3,502 | 26,498 | 31,862 |
| Jan 1, Year 3 | 30,000 | 1,912 | 28,088 | 3,774 |
| Jan 1, Year 4 (residual) | 4,000 | 226 | 3,774 | **0** |
| **Totals** | **94,000** | **5,640** | **88,360** | |

**Schedule checks:**  
- Interest Y1: $58,360 × 0.06 = $3,501.60 → **$3,502**  
- Interest Y2: $31,862 × 0.06 = $1,911.72 → **$1,912**  
- Interest Y3: $3,774 × 0.06 = $226.44 → **$226**  
- Ending balance after residual settlement = **$0**  
- Total payments $94,000 − total interest $5,640 = principal $88,360 ✓

**e. Year 1 journal entries**

**January 1, Year 1 — Recognize ROU and lease liability; reclass IDC**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 89,860 | |
| Lease Liability | | 88,360 |
| Initial Direct Cost | | 1,500 |
| *Commencement: ROU = liability + IDC* | | |

**Check:** Dr 89,860 = Cr 88,360 + 1,500. **Balanced.**

**January 1, Year 1 — First lease payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 30,000 | |
| Cash | | 30,000 |
| *Annuity-due payment; all principal (no interest yet accrued)* | | |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**

**December 31, Year 1 — Accrue interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 3,502 | |
| Lease Liability | | 3,502 |
| *Effective interest on $58,360 carrying amount* | | |

**Check:** Dr 3,502 = Cr 3,502. **Balanced.**

**December 31, Year 1 — Amortize ROU (straight-line over lease term = economic life)**  
$89,860 ÷ 3 = **$29,953** (Years 1–2); Year 3 = **$29,954** (plug for rounding).

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 29,953 | |
| Right-of-Use Asset | | 29,953 |
| *Finance lease: separate amortization of ROU* | | |

**Check:** Dr 29,953 = Cr 29,953. **Balanced.**

**f. December 31, Year 1 financial statement impact**

| Balance sheet | Amount |
|---|---:|
| ROU asset, net ($89,860 − $29,953) | **$59,907** |
| Lease liability — **current** (next payment due Jan 1 Y2) | **$30,000** |
| Lease liability — **noncurrent** ($61,862 total − $30,000) | **$31,862** |
| *Total liability after Y1 interest = $58,360 + $3,502 = $61,862* | |

| Income statement — Year 1 | Amount |
|---|---:|
| Interest expense | **$3,502** |
| Amortization expense — ROU | **$29,953** |
| *Not a single straight-line “lease expense” (that is operating-lease presentation)* | |

**g. Year 2 entries**

**January 1, Year 2 — Lease payment** (clears accrued interest + principal)

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 30,000 | |
| Cash | | 30,000 |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**  
*(Liability after payment = $31,862.)*

**December 31, Year 2 — Interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 1,912 | |
| Lease Liability | | 1,912 |

**Check:** Dr 1,912 = Cr 1,912. **Balanced.**

**December 31, Year 2 — ROU amortization**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 29,953 | |
| Right-of-Use Asset | | 29,953 |

**Check:** Dr 29,953 = Cr 29,953. **Balanced.**  
ROU net after Y2 = $59,907 − $29,953 = **$29,954**.  
Total liability after Y2 interest = $31,862 + $1,912 = **$33,774** (current $30,000; noncurrent residual strip $3,774).

**h. Year 3 and residual settlement**

**January 1, Year 3 — Lease payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 30,000 | |
| Cash | | 30,000 |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**  
*(Liability after payment = $3,774.)*

**December 31, Year 3 — Interest on residual strip**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 226 | |
| Lease Liability | | 226 |

**Check:** Dr 226 = Cr 226. **Balanced.**  
*(Liability = $4,000 = probable residual payment.)*

**December 31, Year 3 — Final ROU amortization (rounding)**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 29,954 | |
| Right-of-Use Asset | | 29,954 |

**Check:** Dr 29,954 = Cr 29,954. **Balanced.**  
ROU balance = **$0**.

**December 31, Year 3 / January 1, Year 4 — Settle residual guarantee**  
Actual residual $8,000; shortfall vs $12,000 guarantee = **$4,000** cash (matches amount already in liability).

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 4,000 | |
| Cash | | 4,000 |
| *Payment of probable amount under residual value guarantee* | | |

**Check:** Dr 4,000 = Cr 4,000. **Balanced.**  
Lease liability and ROU both **$0** after settlement.

**Key insight:** For a **lessee**, residual guarantees enter the **classification PV test at 100%**, but the **lease liability includes only the amount probable of being owed** (guarantee − expected residual). IDC increases the ROU asset only (not the liability). Finance-lease subsequent measurement separates **effective-interest** expense from **straight-line ROU amortization**.

---

### Q2 — CORE number variant — Cedar & Brass residual-guarantee finance lease
**LO:** LO 17-4  
**Concept:** Number-variant twin — complex finance lease with residual guarantee; liability schedule; period-end interest and amortization; settlement  
**Scenario:**  
On **January 1, Year 1**, **Cedar & Brass Fabricators** enters a **3-year noncancellable** finance lease for a CNC press. Year-end is **December 31**. All amounts differ from Q1.

| Item | Amount / term |
|---|---|
| Fair value of press at commencement | **$110,000** |
| Estimated economic life | **3 years** |
| Annual lease payment (due **January 1**, beginning Year 1) | **$35,000** |
| Guaranteed residual value | **$15,000** |
| Expected residual value at lease end | **$10,000** |
| Rate implicit in the lease (known) | **8%** |
| Purchase / renewal options | None; asset reverts |
| Initial direct costs / incentives | None |

Round interest to the nearest dollar.

**Required:**  
a. Classify the lease and compute PV for criterion 4 using **100% of GRV**.  
b. Compute lease liability and ROU at commencement (probable residual only).  
c. Prepare the **full lease liability subsequent measurement schedule**.  
d. Record commencement JE, first payment, and **December 31, Year 1** adjusting entries.  
e. Compute Year 1 interest expense, amortization expense, ROU carrying amount, and current vs noncurrent lease liability at December 31, Year 1.  
f. Record the **residual settlement** entry when actual residual equals the $10,000 expectation (liability should equal the shortfall).

**Answer key:**  

**a. Classification**  
Lease term 3 ÷ life 3 = **100% ≥ 75%** → **finance** (criterion 3).  
Also criterion 4: PV(0.08, 3, −35000, −15000, 1) ≈ **$109,322** > 90% × $110,000 = **$99,000**.

**b. Liability and ROU**  
Probable residual payment = $15,000 − $10,000 = **$5,000**.  
Lease liability = PV(0.08, 3, −35000, −5000, 1) ≈ **$101,383**.  
ROU asset = **$101,383** (no IDC/incentives).

**c. Subsequent measurement schedule**

| Date | Lease payment | Interest (8%) | Principal | Liability ending |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | — | — | — | **101,383** |
| Jan 1, Y1 | 35,000 | 0 | 35,000 | 66,383 |
| Jan 1, Y2 | 35,000 | 5,311 | 29,689 | 36,694 |
| Jan 1, Y3 | 35,000 | 2,936 | 32,064 | 4,630 |
| Residual settlement | 5,000 | 370 | 4,630 | **0** |
| **Totals** | **110,000** | **8,617** | **101,383** | |

**Checks:** $66,383 × 0.08 = $5,310.64 → **$5,311**; $36,694 × 0.08 = $2,935.52 → **$2,936**; $4,630 × 0.08 = $370.40 → **$370**. Totals: payments − interest = principal ✓; end bal $0 ✓.

**d. Journal entries — Year 1**

**January 1, Year 1 — Commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 101,383 | |
| Lease Liability | | 101,383 |

**Check:** Dr 101,383 = Cr 101,383. **Balanced.**

**January 1, Year 1 — Payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Cash | | 35,000 |

**Check:** Dr 35,000 = Cr 35,000. **Balanced.**

**December 31, Year 1 — Interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,311 | |
| Lease Liability | | 5,311 |

**Check:** Dr 5,311 = Cr 5,311. **Balanced.**

**December 31, Year 1 — ROU amortization**  
$101,383 ÷ 3: Years 1–2 **$33,794**; Year 3 **$33,795**.

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 33,794 | |
| Right-of-Use Asset | | 33,794 |

**Check:** Dr 33,794 = Cr 33,794. **Balanced.**

**e. Year 1 amounts**

| Item | Amount |
|---|---:|
| Interest expense | **$5,311** |
| Amortization expense | **$33,794** |
| ROU asset, net | **$67,589** ($101,383 − $33,794) |
| Total lease liability (after interest) | **$71,694** ($66,383 + $5,311) |
| Current lease liability | **$35,000** |
| Noncurrent lease liability | **$36,694** |

**f. Residual settlement** (when residual is $10,000 as expected)

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 5,000 | |
| Cash | | 5,000 |
| *Shortfall $15,000 − $10,000 already embedded in liability schedule* | | |

**Check:** Dr 5,000 = Cr 5,000. **Balanced.**

**Key insight:** Changing rates, payments, and residual estimates changes every schedule row, but the measurement rules are identical: **probable residual only in the liability**, **100% GRV in the classification PV test**, and finance-lease P&L still shows **interest + amortization** separately.

---

### Q3 — CORE alternate angle — Purchase option reasonably certain; amortize over useful life; exercise
**LO:** LO 17-4  
**Concept:** Finance lease with purchase option expected to be exercised — include option price in liability; amortize ROU over **useful life** (not lease term); period-end entries; exercise/settlement and reclass to equipment  
**Scenario:**  
On **January 1, Year 1**, **Harborline Labs Inc.** leases laboratory imaging equipment:

| Item | Amount / term |
|---|---|
| Fair value at commencement | **$96,000** |
| Economic / useful life | **5 years** (straight-line; zero salvage for ROU amortization policy) |
| Lease term (noncancellable) | **3 years** |
| Annual payment due **January 1** each year | **$32,000** |
| Purchase option at end of Year 3 | **$8,000** — **reasonably certain** to be exercised |
| Residual value guarantee | None |
| Implicit rate (known) | **8%** |
| IDC / incentives | None |

Harborline’s year-end is December 31. Because exercise of the purchase option is reasonably certain, the **lease term for measurement ends at the option date**, and the option price is a **lease payment**. Round interest to nearest dollar.

**Required:**  
a. Classify the lease; identify which criteria are met.  
b. Compute the lease liability / ROU at commencement.  
c. Prepare the **lease liability schedule** through exercise of the purchase option.  
d. Compute **annual ROU amortization** and explain why the period is 5 years, not 3.  
e. Record Year 1 commencement, first payment, and December 31 adjusting entries.  
f. At **December 31, Year 3** (after Year 3 interest and amortization), record (1) exercise of the purchase option for cash and (2) reclassification of the remaining ROU carrying amount to **Equipment**. State the equipment’s remaining depreciable life.

**Answer key:**  

**a. Classification — finance**  
- **Purchase option reasonably certain** → criterion 2 met.  
- PV of payments including $8,000 option: PV(0.08, 3, −32000, −8000, 1) ≈ **$95,415** > 90% × $96,000 = **$86,400** → criterion 4 also met.  
- Term 3/5 = 60% < 75% → criterion 3 **not** met on term alone; finance still holds via criteria 2 and 4.

**b. Liability and ROU**  
Lease liability = ROU = **$95,415** (full purchase option included; no “probable residual” haircut).

**c. Liability schedule**

| Date | Payment | Interest (8%) | Principal | Liability ending |
|---|---:|---:|---:|---:|
| Jan 1, Y1 initial | — | — | — | **95,415** |
| Jan 1, Y1 | 32,000 | 0 | 32,000 | 63,415 |
| Jan 1, Y2 | 32,000 | 5,073 | 26,927 | 36,488 |
| Jan 1, Y3 | 32,000 | 2,919 | 29,081 | 7,407 |
| Dec 31 Y3 / exercise | 8,000 | 593 | 7,407 | **0** |

**Checks:** $63,415 × 0.08 = $5,073.20 → **$5,073**; $36,488 × 0.08 = $2,919.04 → **$2,919**; $7,407 × 0.08 = $592.56 → **$593**. End bal $0 ✓.

**d. ROU amortization period**  
Because Harborline is **reasonably certain to purchase**, economic benefits extend over the asset’s **useful life (5 years)**, not merely the 3-year contractual term.  
Annual amortization = $95,415 ÷ 5 = **$19,083**.

*(If there were initial direct costs, IDC would still be amortized over the **lease term to the purchase date**, not the full useful life — none here.)*

**e. Year 1 journal entries**

**January 1, Year 1 — Commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 95,415 | |
| Lease Liability | | 95,415 |

**Check:** Dr 95,415 = Cr 95,415. **Balanced.**

**January 1, Year 1 — Payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 32,000 | |
| Cash | | 32,000 |

**Check:** Dr 32,000 = Cr 32,000. **Balanced.**

**December 31, Year 1 — Interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,073 | |
| Lease Liability | | 5,073 |

**Check:** Dr 5,073 = Cr 5,073. **Balanced.**

**December 31, Year 1 — ROU amortization (over useful life)**

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 19,083 | |
| Right-of-Use Asset | | 19,083 |

**Check:** Dr 19,083 = Cr 19,083. **Balanced.**

**f. Exercise and reclass at end of Year 3**

After three years of amortization: ROU remaining = $95,415 − 3 × $19,083 = $95,415 − $57,249 = **$38,166**.  
After Year 3 interest accrual, lease liability = **$8,000**.

**(1) Exercise purchase option**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 8,000 | |
| Cash | | 8,000 |
| *Pay option price; clear remaining liability* | | |

**Check:** Dr 8,000 = Cr 8,000. **Balanced.**

**(2) Reclassify remaining ROU basis to owned equipment**

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 38,166 | |
| Right-of-Use Asset | | 38,166 |
| *Transfer unamortized ROU to PPE upon ownership* | | |

**Check:** Dr 38,166 = Cr 38,166. **Balanced.**  
Remaining depreciable life = **2 years** (5 − 3). Year 4–5 depreciation = $38,166 ÷ 2 = **$19,083** per year (continues same pattern).

**Key insight:** A **reasonably certain purchase option** is included **in full** in lease payments (unlike residual guarantees, which use only the probable shortfall for the liability). ROU amortization switches from lease-term to **useful life** when ownership transfer or a reasonably certain purchase option is present. At exercise, cash settles the liability and any remaining ROU basis becomes **owned equipment**.

---

### Q4 — MC — Residual guarantee: classification vs liability measurement
**LO:** LO 17-4  
**Concept:** Classification presentation of residual guarantee (100% in PV test) versus liability measurement (probable amount only)  
**Question:**  
On commencement of a finance lease, the lessee guarantees a residual value of **$20,000** and expects the asset’s residual value to be **$14,000**. Which statement is correct under ASC 842 for the **lessee**?

- A) Include **$20,000** in both the classification PV test and the initial lease liability.  
- B) Include **$20,000** in the classification PV test, but include only **$6,000** (the amount probable of being owed) when measuring the lease liability.  
- C) Include only **$6,000** in both the classification PV test and the lease liability.  
- D) Exclude residual guarantees entirely from the lessee’s PV test and liability because the asset will be returned.

**Answer:** **B.**  
For **lease classification criterion 4**, the lessee includes **100% of the guaranteed residual** in lease payments. For **measurement of the lease liability**, the lessee includes only amounts **probable of being owed** under the guarantee — here $20,000 − $14,000 = **$6,000**. Unguaranteed residual is never a lessee lease payment. (If a purchase option is reasonably certain, residual guarantees are ignored because the asset is expected to remain with the lessee.)

---

### Q5 — MC — Amortization period with purchase option
**LO:** LO 17-4  
**Concept:** ROU amortization period when purchase option is reasonably certain  
**Question:**  
A lessee classifies a lease as finance solely because it is reasonably certain to exercise a purchase option at the end of a **4-year** lease term. The underlying asset’s remaining economic life is **7 years**. Ignoring salvage, over which period should the lessee amortize the right-of-use asset?

- A) 4 years (the contractual lease term only)  
- B) 7 years (the useful life of the underlying asset)  
- C) The shorter of 4 years and 7 years, which is always the lease term for finance leases  
- D) 7 years only if ownership automatically transfers; otherwise 4 years even with a reasonably certain purchase option  

**Answer:** **B.**  
If the lease **transfers ownership** or the lessee is **reasonably certain to exercise a purchase option**, the ROU asset is amortized over the **useful life of the underlying asset**, not the lease term. Here that is **7 years**.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV annuity-due, effective-interest schedule rolls to zero, ROU amortization sums to cost)
- [x] Core demo not sidebar-only (Demo 17-4A IDC, 17-4B residual guarantee, 17-4C purchase option)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 classification/method only)
- [x] Emphasis angle covered: subsequent_measurement_schedule (Q1 full table; Q2 twin; Q3 PO schedule)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
