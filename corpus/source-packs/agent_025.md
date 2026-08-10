# Agent 25 — CORE DEMO — LO 17-5

**Chapter:** 17  
**LO title:** Account for complex operating leases for a lessee  
**Critical gap LO:** yes  
**Emphasis angle:** initial_recognition_JE

## Concept list for this pack
- Operating classification when none of the five finance criteria are met (including residual-guarantee alternate that can flip criterion 4)
- Initial measurement of **lease liability** = PV of lease payments (same base as finance)
- **Right-of-use asset** = lease liability − lease incentives + initial direct costs
- Pre-commencement JEs for cash incentive and incremental legal (IDC) costs
- Commencement JE that records ROU/liability and clears IDC and incentive balances
- Lease liability amortization schedule (effective interest; annuity-due payments)
- ROU schedule: straight-line **single lease expense** − period “interest” = ROU reduction
- Period-end adjusting JE: Dr Lease expense / Cr Lease liability / Cr ROU (not separate interest + amortization on the IS)
- Prepaid first payment: reduce liability; ROU still includes full PV before prepayment application
- Maturity / settlement: liability and ROU both to zero after final year
- Presentation: single lease expense in income from continuing operations; SCF classifies full operating-lease payment as operating outflow
- Number-variant twin (all facts/numbers changed)

---

### Q1 — CORE — Complex operating lease with IDC and lease incentive (initial recognition emphasis)
**LO:** LO 17-5  
**Concept:** Complex operating lease — IDC + incentive; measure liability and ROU; initial JEs; liability/ROU schedules; subsequent and maturity  
**Scenario:** On **January 1, Year 1** (commencement), **Summit Trail Retail Co.** (lessee) leases modular store fixtures from **Crestline Equipment Partners**. Facts:

1. Noncancellable **4-year** lease; fixtures revert to lessor at end of term.  
2. Remaining economic life of the fixtures is **12 years**.  
3. Fair value at commencement is **$400,000**.  
4. Four annual lease payments of **$41,387.12** due **January 1** of Year 1 through Year 4 (payments in advance).  
5. No purchase or renewal option that is reasonably certain to be exercised.  
6. Residual value is **unguaranteed**; equipment is routinely re-leased by Crestline to other retailers.  
7. Lessor’s implicit rate is **7%** and is known to Summit; Summit’s incremental borrowing rate is also 7%.  
8. Before commencement, Summit paid **$2,000** of incremental legal fees to execute the lease (initial direct costs).  
9. Before commencement, Crestline paid Summit a **$7,500** cash lease incentive; Summit recorded Cash and Lease Incentive Liability.  
10. Summit’s fiscal year ends **December 31**.

**Required:**  
(a) Journal entries for the initial direct cost and the lease incentive **prior to** commencement.  
(b) Classify the lease for Summit (apply all five criteria; show PV for criterion 4).  
(c) Compute the **lease liability** and **right-of-use asset** at commencement.  
(d) Prepare the commencement journal entry that records ROU and lease liability (and clears IDC and incentive balances).  
(e) Prepare the **lease liability amortization schedule** and the **right-of-use asset schedule** for the full term.  
(f) Prepare all lessee journal entries for **Year 1** (first payment; Dec 31 single lease expense).  
(g) Show Year 1 income-statement lease expense and Dec 31 Year 1 balance-sheet amounts (ROU net; current and noncurrent lease liability).  
(h) Prepare Year 2 journal entries and **Year 4 (maturity)** journal entries; confirm ROU and liability are zero after maturity.

**Answer key:**

**(a) Prior to commencement**  
```
Dr Initial Direct Cost ...................... 2,000
   Cr Cash ........................................... 2,000
```
(Dr = Cr = 2,000)

```
Dr Cash ..................................... 7,500
   Cr Lease Incentive Liability ...................... 7,500
```
(Dr = Cr = 7,500)

**(b) Classification — operating lease** (no finance criterion met)

| Criterion | Analysis | Met? |
|---|---|---|
| 1 Ownership transfer | Asset reverts to lessor | No |
| 2 Purchase option | None | No |
| 3 Lease term | 4 / 12 = **33.3%** < 75% | No |
| 4 PV of lease payments | PV of 4 payments in advance at 7% = **$150,000** < 90% × $400,000 = $360,000 (and even net of $7,500 incentive for classification, PV remains well below 90% of FV) | No |
| 5 No alternative use | Lessor routinely re-leases fixtures | No |

Excel: `=PV(0.07,4,−41387.12,0,1)` → **$150,000** (rounded).  
→ **Operating lease.**

**(c) Measurement**  
- **Lease liability** = PV of unpaid lease payments at commencement = **$150,000**.  
- **Right-of-use asset** = lease liability − lease incentive + initial direct costs  
  \(= 150{,}000 - 7{,}500 + 2{,}000 = \mathbf{\$144{,}500}\).

**(d) January 1, Year 1 — record ROU and liability; clear IDC and incentive**  
```
Dr Right-of-Use Asset ..................... 144,500
Dr Lease Incentive Liability ................ 7,500
   Cr Initial Direct Cost ............................ 2,000
   Cr Lease Liability .............................. 150,000
```
(Dr 152,000 = Cr 152,000)

**(e) Lease liability schedule** (rate 7%; amounts to nearest cent)

| Date | Lease payment | Interest (7%) | Principal | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 150,000.00 |
| Jan 1, Y1 | 41,387.12 | 0.00 | 41,387.12 | 108,612.88 |
| Jan 1, Y2 | 41,387.12 | 7,602.90 | 33,784.22 | 74,828.66 |
| Jan 1, Y3 | 41,387.12 | 5,238.01 | 36,149.11 | 38,679.55 |
| Jan 1, Y4 | 41,387.12 | 2,707.57 | 38,679.55 | 0.00 |
| **Totals** | **165,548.48** | **15,548.48** | **150,000.00** | |

Interest checks: \(108{,}612.88 \times 0.07 = 7{,}602.90\); \(74{,}828.66 \times 0.07 = 5{,}238.01\); \(38{,}679.55 \times 0.07 = 2{,}707.57\).

**Right-of-use asset schedule**  
Total cost of the lease = undiscounted payments + IDC − incentive  
\(= 165{,}548.48 + 2{,}000 - 7{,}500 = \mathbf{\$160{,}048.48}\).  
Straight-line lease expense = \(160{,}048.48 / 4 = \mathbf{\$40{,}012.12}\) per year.  
ROU reduction each period = SL lease expense − period “interest” from the liability schedule.

| Date | Lease expense (SL) | Interest on liability | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commence) | | | | 144,500.00 |
| Dec 31, Y1 | 40,012.12 | 7,602.90 | 32,409.22 | 112,090.78 |
| Dec 31, Y2 | 40,012.12 | 5,238.01 | 34,774.11 | 77,316.67 |
| Dec 31, Y3 | 40,012.12 | 2,707.57 | 37,304.55 | 40,012.12 |
| Dec 31, Y4 | 40,012.12 | 0.00 | 40,012.12 | 0.00 |
| **Totals** | **160,048.48** | **15,548.48** | **144,500.00** | |

**(f) Year 1 journal entries**

January 1, Year 1 — first lease payment:  
```
Dr Lease Liability ......................... 41,387.12
   Cr Cash ....................................... 41,387.12
```
(Dr = Cr = 41,387.12)

December 31, Year 1 — single lease expense (period-end adjusting):  
```
Dr Lease Expense ........................... 40,012.12
   Cr Lease Liability ............................. 7,602.90
   Cr Right-of-Use Asset ......................... 32,409.22
```
(Dr 40,012.12 = Cr 7,602.90 + 32,409.22)

**(g) Year 1 financial statement impact**

**Income statement (Year 1):**  
- Lease expense (single amount in income from continuing operations): **$40,012.12**  
- *Not* separate interest expense + ROU amortization (finance-lease presentation).

**Balance sheet (Dec 31, Year 1):**  
- ROU asset (net): \(144{,}500 - 32{,}409.22 = \mathbf{\$112{,}090.78}\)  
- Total lease liability: \(108{,}612.88 + 7{,}602.90 = \mathbf{\$116{,}215.78}\)  
- **Current** lease liability = next payment **$41,387.12**  
- **Noncurrent** lease liability: \(116{,}215.78 - 41{,}387.12 = \mathbf{\$74{,}828.66}\)

**Statement of cash flows (Year 1):** full cash lease payment **$41,387.12** is an **operating** cash outflow (operating lease).

**(h) Year 2 and Year 4 (maturity)**

**Year 2**  
January 1, Year 2 — payment:  
```
Dr Lease Liability ......................... 41,387.12
   Cr Cash ....................................... 41,387.12
```

December 31, Year 2 — lease expense:  
```
Dr Lease Expense ........................... 40,012.12
   Cr Lease Liability ............................. 5,238.01
   Cr Right-of-Use Asset ......................... 34,774.11
```
(Dr 40,012.12 = Cr 5,238.01 + 34,774.11)

**Year 4 — maturity / settlement**  
January 1, Year 4 — final payment:  
```
Dr Lease Liability ......................... 41,387.12
   Cr Cash ....................................... 41,387.12
```
After this payment, lease liability = **$0**.

December 31, Year 4 — final ROU reduction (no remaining “interest”):  
```
Dr Lease Expense ........................... 40,012.12
   Cr Right-of-Use Asset ......................... 40,012.12
```
(Dr = Cr = 40,012.12)

After Year 4 entries: **ROU = $0** and **lease liability = $0**. Asset returned to lessor; no residual settlement (unguaranteed).

**Key insight:** Complex operating leases use the **same initial measurement** as finance leases (liability = PV of payments; ROU adjusted for incentives and IDC), but **subsequent** measurement produces a **single straight-line lease expense**. “Interest” on the liability is an input to the ROU reduction plug so that Expense = Interest-component + ROU-reduction each period.

---

### Q2 — CORE number variant — IDC + incentive twin
**LO:** LO 17-5  
**Concept:** Complex operating lease — IDC + incentive (all numbers changed)  
**Scenario:** On **January 1, Year 1**, **Copper Basin Foods LLC** leases refrigerated display cases under a **4-year** noncancellable operating lease. Facts:

1. Economic life **15 years**; equipment reverts to lessor; no PO; residual unguaranteed; lessor re-leases this class of equipment.  
2. Annual payments of **$43,560.98** due **January 1** each year for 4 years (in advance).  
3. Fair value at commencement **$450,000**.  
4. Implicit rate known to lessee: **6%**.  
5. Pre-commencement initial direct costs (execution legal fees): **$2,400**.  
6. Pre-commencement cash lease incentive from lessor: **$6,000** (recorded as Lease Incentive Liability).  
7. Year-end December 31.

**Required:**  
(a) Classify the lease (brief support).  
(b) Compute lease liability and ROU asset at commencement.  
(c) Prepare the commencement JE (including clearing IDC and incentive).  
(d) Prepare the full lease liability schedule and ROU asset schedule.  
(e) Record Year 1 payment and Dec 31 lease-expense adjusting entry.  
(f) State Year 1 lease expense and Dec 31 current vs noncurrent lease liability.

**Answer key:**

**(a) Operating lease** — 4/15 = 26.7% < 75%; PV of payments \(=\mathbf{\$160{,}000}\) < 90% × $450,000 = $405,000; no transfer, no PO, alternative use exists.

Excel: `=PV(0.06,4,−43560.98,0,1)` → **$160,000** (rounded).

**(b) Measurement**  
- Lease liability = **$160,000**  
- ROU asset = \(160{,}000 - 6{,}000 + 2{,}400 = \mathbf{\$156{,}400}\)

**(c) January 1, Year 1 — commencement**  
```
Dr Right-of-Use Asset ..................... 156,400
Dr Lease Incentive Liability ................ 6,000
   Cr Initial Direct Cost ............................ 2,400
   Cr Lease Liability .............................. 160,000
```
(Dr 162,400 = Cr 162,400)

**(d) Lease liability schedule** (6%)

| Date | Lease payment | Interest (6%) | Principal | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 160,000.00 |
| Jan 1, Y1 | 43,560.98 | 0.00 | 43,560.98 | 116,439.02 |
| Jan 1, Y2 | 43,560.98 | 6,986.34 | 36,574.64 | 79,864.38 |
| Jan 1, Y3 | 43,560.98 | 4,791.86 | 38,769.12 | 41,095.26 |
| Jan 1, Y4 | 43,560.98 | 2,465.72 | 41,095.26 | 0.00 |
| **Totals** | **174,243.92** | **14,243.92** | **160,000.00** | |

Interest checks: \(116{,}439.02 \times 0.06 = 6{,}986.34\); \(79{,}864.38 \times 0.06 = 4{,}791.86\); \(41{,}095.26 \times 0.06 = 2{,}465.72\).

**ROU schedule**  
Total cost = \(174{,}243.92 + 2{,}400 - 6{,}000 = \mathbf{\$170{,}643.92}\)  
SL lease expense = \(170{,}643.92 / 4 = \mathbf{\$42{,}660.98}\)

| Date | Lease expense (SL) | Interest on liability | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | | | | 156,400.00 |
| Dec 31, Y1 | 42,660.98 | 6,986.34 | 35,674.64 | 120,725.36 |
| Dec 31, Y2 | 42,660.98 | 4,791.86 | 37,869.12 | 82,856.24 |
| Dec 31, Y3 | 42,660.98 | 2,465.72 | 40,195.26 | 42,660.98 |
| Dec 31, Y4 | 42,660.98 | 0.00 | 42,660.98 | 0.00 |
| **Totals** | **170,643.92** | **14,243.92** | **156,400.00** | |

**(e) Year 1 entries**  
January 1, Year 1 — payment:  
```
Dr Lease Liability ......................... 43,560.98
   Cr Cash ....................................... 43,560.98
```

December 31, Year 1 — lease expense:  
```
Dr Lease Expense ........................... 42,660.98
   Cr Lease Liability ............................. 6,986.34
   Cr Right-of-Use Asset ......................... 35,674.64
```
(Dr 42,660.98 = Cr 6,986.34 + 35,674.64)

**(f) Year 1 reporting**  
- Lease expense: **$42,660.98**  
- ROU (net): **$120,725.36**  
- Total lease liability Dec 31 Y1: \(116{,}439.02 + 6{,}986.34 = \mathbf{\$123{,}425.36}\)  
- Current: **$43,560.98**; noncurrent: \(123{,}425.36 - 43{,}560.98 = \mathbf{\$79{,}864.38}\)

**Key insight:** Changing the rate, payment, term context, IDC, and incentive changes every dollar amount, but the **structure** is identical: liability at PV, ROU = PV − incentive + IDC, then single SL lease expense each period.

---

### Q3 — CORE alternate angle — Prepaid first payment + full-term settlement
**LO:** LO 17-5  
**Concept:** Complex operating lease with prepayment of first payment; initial recognition; period-end expense; maturity  
**Scenario:** On **December 28, Year 0** (before commencement), **Ironwood Studio LLC** (lessee) arranges a **4-year** noncancellable lease of sound-stage equipment that will commence **January 1, Year 1**. Facts:

1. Economic life **12 years**; FV **$380,000**; asset reverts to lessor; no PO; residual unguaranteed; lessor has alternative use.  
2. Four annual payments of **$41,387.12** due each **January 1** (Years 1–4).  
3. Implicit rate known to lessee: **7%**.  
4. On **December 28, Year 0**, Ironwood:  
   - Paid the **first** lease payment of **$41,387.12** in advance (recorded as Prepaid Lease Payment).  
   - Paid incremental legal fees (IDC) of **$2,000**.  
   - Received a cash lease incentive of **$7,500** (Lease Incentive Liability).  
5. Fiscal year-end December 31.

**Required:**  
(a) Classify the lease.  
(b) Record the three pre-commencement entries on December 28, Year 0.  
(c) Compute gross lease liability and ROU at commencement **before** applying the prepayment; then compute **net** lease liability after applying the prepaid payment.  
(d) Prepare the January 1, Year 1 commencement entries (record ROU/liability; apply prepaid to liability).  
(e) Prepare the Dec 31, Year 1 lease-expense adjusting entry (use the same liability/ROU mechanics as a non-prepaid lease after the first payment has been applied).  
(f) Prepare Year 4 maturity entries and confirm zero balances.

**Answer key:**

**(a) Operating lease** — same analysis as Q1: term 4/12 < 75%; PV of four payments at 7% = **$150,000** < 90% × $380,000 = $342,000; no transfer/PO; alternative use.  

**(b) December 28, Year 0 — pre-commencement**  
```
Dr Prepaid Lease Payment .................. 41,387.12
   Cr Cash ....................................... 41,387.12
```
```
Dr Initial Direct Cost ...................... 2,000.00
   Cr Cash ........................................ 2,000.00
```
```
Dr Cash ..................................... 7,500.00
   Cr Lease Incentive Liability ................... 7,500.00
```
(Each entry balances.)

**(c) Measurement at commencement**  
- Gross lease liability (PV of lease payments) = **$150,000**  
- ROU asset = \(150{,}000 - 7{,}500 + 2{,}000 = \mathbf{\$144{,}500}\)  
  (Prepayment is **not** added again to ROU when it is applied by reducing the liability; textbook Demo 17-5 pattern: ROU reflects PV ± incentive/IDC; prepaid reduces liability.)  
- Net lease liability after applying prepaid first payment = \(150{,}000 - 41{,}387.12 = \mathbf{\$108{,}612.88}\)

**(d) January 1, Year 1 — commencement**  
```
Dr Right-of-Use Asset ..................... 144,500.00
Dr Lease Incentive Liability ................ 7,500.00
   Cr Initial Direct Cost ......................... 2,000.00
   Cr Lease Liability ........................... 150,000.00
```
(Dr 152,000 = Cr 152,000)

```
Dr Lease Liability ......................... 41,387.12
   Cr Prepaid Lease Payment ...................... 41,387.12
```
(Dr = Cr = 41,387.12)

Liability balance after these entries: **$108,612.88** (matches post–first-payment balance on the Q1 liability schedule).

**(e) December 31, Year 1 — lease expense**  
Same SL expense and interest as Q1 (total cost still \(165{,}548.48 + 2{,}000 - 7{,}500 = 160{,}048.48\); SL = **$40,012.12**):  
```
Dr Lease Expense ........................... 40,012.12
   Cr Lease Liability ............................. 7,602.90
   Cr Right-of-Use Asset ......................... 32,409.22
```
(Dr 40,012.12 = Cr 40,012.12)

Dec 31, Y1: ROU = **$112,090.78**; total liability = **$116,215.78** (current $41,387.12; noncurrent $74,828.66).

**(f) Year 4 maturity** (after Y2–Y3 payments and accruals as in the Q1 schedules)  
January 1, Year 4 — final cash payment:  
```
Dr Lease Liability ......................... 41,387.12
   Cr Cash ....................................... 41,387.12
```
Liability → **$0**.

December 31, Year 4:  
```
Dr Lease Expense ........................... 40,012.12
   Cr Right-of-Use Asset ......................... 40,012.12
```
ROU → **$0**. Settlement complete; no residual cash payment (unguaranteed residual).

**Key insight:** A **prepaid** first payment is applied against the lease liability at commencement (or reduces the liability measurement for unpaid payments). ROU is still based on full PV adjusted for incentives and IDC. Subsequent operating-lease accounting (single SL expense) is unchanged once the prepayment has been applied.

---

### Q4 — MC — Residual guarantee and operating vs finance classification
**LO:** LO 17-5  
**Concept:** Guaranteed residual — criterion 4 classification PV vs measurement of lease liability (complex operating context)  
**Question:** **LumenPath Clinics** enters a 3-year equipment lease. Annual payments of $34,972.24 are due at the **beginning** of each year. Fair value of the equipment is $150,000; lessor’s implicit rate (known to lessee) is 5%. The asset reverts to the lessor; economic life is 6 years; lessor has alternative use. There is **no** purchase option. Estimated residual at lease end is $57,882.

If the residual is **unguaranteed**, the PV of lease payments for classification is $100,000 and the lease is **operating**.  

If instead LumenPath **guarantees** the full residual of $57,882, and for criterion 4 the lessee includes the PV of the guaranteed residual in “lease payments,” which statement is **correct**?

- A) Classification remains operating because the lease term is still only 50% of economic life.  
- B) Classification becomes **finance** because PV of lease payments (including the guaranteed residual) equals about $150,000, which exceeds 90% of fair value ($135,000).  
- C) The lease liability always includes 100% of any residual guarantee even if the lessee expects residual fair value to fully cover the guarantee.  
- D) Operating-lease subsequent measurement splits expense into interest expense and amortization expense on the income statement.

**Answer:** **B.**  
With a full residual guarantee, criterion 4 uses PV of the three annuity-due payments **plus** PV of the $57,882 residual: Excel `=PV(0.05,3,−34972.24,−57882,1)` ≈ **$150,000** > 90% × $150,000 = $135,000 → **finance lease**. Meeting **any one** criterion is enough; the term-length criterion need not also be met.  
(A is wrong because criterion 4 alone can force finance classification. C is wrong for **measurement**: liability includes only the **probable amount owed** under the residual guarantee, which may be less than 100% of the guarantee. D describes **finance** subsequent presentation, not operating.)

---

### Q5 — MC — Income statement / SCF presentation (operating vs finance)
**LO:** LO 17-5  
**Concept:** Presentation of complex operating lease expense vs finance lease; SCF classification of cash payments  
**Question:** For a lessee’s **operating** lease (with ROU asset and lease liability recognized), which presentation is correct under ASC 842?

- A) Interest expense on the lease liability and amortization of the ROU asset are reported as two separate amounts (interest often in other expense; amortization in operating income).  
- B) A single lease expense is recognized, typically on a straight-line basis, in income from continuing operations; the full cash lease payment is classified as an **operating** cash outflow.  
- C) No ROU asset or lease liability appears on the balance sheet after ASC 842.  
- D) Only the principal portion of each cash payment is an operating outflow; the interest portion is a financing outflow.

**Answer:** **B.**  
Operating leases: single lease cost in continuing operations; SCF treats the entire payment as an operating outflow.  
(A and the split SCF treatment in D are **finance** lease patterns. C is pre-ASC 842 operating off-balance-sheet treatment and is incorrect under current GAAP.)

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (liability schedules, SL expense, ROU rollforwards to zero)
- [x] Core demo (Demo 17-5 path: complex operating with IDC/incentive/prepayment) — not sidebar-only
- [x] LO + Concept on every item
- [x] MC = 2 (classification + presentation only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
