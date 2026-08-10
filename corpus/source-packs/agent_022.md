# Agent 22 — CORE DEMO — LO 17-2

**Chapter:** 17  
**LO title:** Accounting for a Basic Finance Lease by a Lessee  
**Critical gap LO:** yes  
**Emphasis:** initial_recognition_JE

## Concept list for this pack
- Initial recognition of ROU asset and lease liability at commencement (annuity-due PV)
- Lease liability amortization schedule (effective interest method)
- Period-end adjusting entries: interest on lease liability + straight-line ROU amortization
- Maturity / final settlement when ROU and liability reach zero
- Balance sheet classification (current vs noncurrent lease liability) and dual IS expenses
- Discount rate hierarchy: lessor’s implicit rate when known vs incremental borrowing rate
- Number-variant twin of the full life-cycle demo

---

### Q1 — CORE — Basic finance lease: initial recognition through maturity (Cedar Ridge)

**LO:** LO 17-2  
**Concept:** Initial recognition JE + full liability schedule + period-end and maturity JEs  
**Scenario:**  
On **January 1 of Year 1** (commencement), **Cedar Ridge Fabricators** leases a CNC milling system from **Summit Equipment Leasing**. Facts:

1. Noncancellable **3-year** lease of equipment that Summit routinely leases to other customers (nonspecialized; alternative uses exist).  
2. **Three** annual lease payments of **$63,528.08**, payable **January 1** of Year 1, Year 2, and Year 3 (**annuity due**).  
3. Fair value of the equipment at commencement = **$180,000**.  
4. Estimated economic life = **3 years**. Estimated residual value = **$0**; no residual value guarantee.  
5. No renewal or purchase option; asset reverts to Summit at end of term.  
6. Lessor’s **implicit rate = 6%**, known by Cedar Ridge. Cedar Ridge’s incremental borrowing rate = **7%**.  
7. Cedar Ridge’s fiscal year ends **December 31**. For the basic case, there are **no** initial direct costs, prepaid rent, or lease incentives (ROU = lease liability at commencement).  
8. Round interest and schedule amounts to the **nearest cent**. Credit the ROU asset directly for amortization (textbook chapter convention).

**Required:**  
(a) Classify the lease for the **lessee** and identify which classification criterion(s) are met.  
(b) Measure the lease liability and ROU asset at commencement; identify the discount rate used.  
(c) Prepare the **lease liability schedule** (effective interest method).  
(d) Prepare **all lessee journal entries for Year 1** (commencement, payment, and December 31 adjusting entries).  
(e) Show **Year 1** balance sheet (ROU; current and noncurrent lease liability) and income statement lease-related expenses.  
(f) Prepare lessee journal entries for **Year 2** and **Year 3** (through maturity / asset return with zero residual).  
(g) How would measurement change if only the **7%** incremental borrowing rate were known (implicit rate not readily determinable)? Briefly.

**Answer key:**

**(a) Classification — finance lease**  
At least one of the five criteria is met:

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to lessor | No |
| 2. Purchase option reasonably certain | None | No |
| 3. Lease term major part of economic life | 3 / 3 = **100%** (≥ 75% bright line often used) | **Yes** |
| 4. PV of lease payments substantially all of FV | PV = $180,000 ≥ 90% × $180,000 | **Yes** |
| 5. Specialized asset / no alternative use | Routinely leased to others | No |

→ **Finance lease** to the lessee.

**(b) Measurement**  
Discount rate = **6%** (rate implicit in the lease, known by lessee — preferred over IBR).  

Excel: `=PV(0.06,3,-63528.08,0,1)` → **$180,000.00**  

Lease liability (commencement) = **$180,000**  
ROU asset (basic case, no adjustments) = **$180,000**

**(c) Lease liability schedule**

| Date | Lease payment | Interest on liability (6%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | $180,000.00 |
| Jan 1, Y1 | $63,528.08 | $0.00 | $63,528.08 | 116,471.92 |
| Jan 1, Y2 | 63,528.08 | 6,988.32 | 56,539.76 | 59,932.16 |
| Jan 1, Y3 | 63,528.08 | 3,595.92* | 59,932.16 | 0.00 |
| **Totals** | **$190,584.24** | **$10,584.24** | **$180,000.00** | |

\*Final-period interest plugged **$0.01** so liability clears ($59,932.16 × 0.06 = $3,595.9296 → schedule uses **$3,595.92** so payment − interest = remaining principal).  
Interest after commencement: rate × beginning liability for the period (first payment is 100% principal — no time has elapsed).  
Check: total cash $190,584.24 − PV $180,000.00 = total interest **$10,584.24**.

**(d) Year 1 journal entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y1 | Right-of-Use Asset | 180,000.00 | |
| | Lease Liability | | 180,000.00 |
| | *Record ROU asset and lease liability at commencement* | | |
| Jan 1, Y1 | Lease Liability | 63,528.08 | |
| | Cash | | 63,528.08 |
| | *First lease payment (all principal)* | | |
| Dec 31, Y1 | Interest Expense | 6,988.32 | |
| | Lease Liability | | 6,988.32 |
| | *Accrue interest: $116,471.92 × 6%* | | |
| Dec 31, Y1 | Amortization Expense | 60,000.00 | |
| | Right-of-Use Asset | | 60,000.00 |
| | *Straight-line ROU amort over lease term: $180,000 / 3* | | |

**Balance checks:** Dr = Cr on every entry ($180,000; $63,528.08; $6,988.32; $60,000).

**(e) Year 1 financial statement impact**

**Income statement — Year 1**  
- Interest expense—lease liability: **$6,988.32**  
- Amortization expense—ROU asset: **$60,000.00**  
- Total lease-related expense: **$66,988.32** (two lines — finance lease pattern)

**Balance sheet — Dec 31, Year 1**  
- ROU asset: $180,000 − $60,000 = **$120,000**  
- Lease liability total: $116,471.92 + $6,988.32 = **$123,460.24**  
  - Current lease liability = next payment **$63,528.08** (= accrued interest $6,988.32 + principal reduction $56,539.76)  
  - Noncurrent lease liability = $123,460.24 − $63,528.08 = **$59,932.16**

**(f) Year 2 and Year 3 journal entries (through maturity)**

**Year 2**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y2 | Lease Liability | 63,528.08 | |
| | Cash | | 63,528.08 |
| | *Pays accrued interest $6,988.32 + principal $56,539.76* | | |
| Dec 31, Y2 | Interest Expense | 3,595.92 | |
| | Lease Liability | | 3,595.92 |
| | *$59,932.16 × 6% (schedule / plug)* | | |
| Dec 31, Y2 | Amortization Expense | 60,000.00 | |
| | Right-of-Use Asset | | 60,000.00 |

After Dec 31, Y2: ROU = $60,000; lease liability = $59,932.16 + $3,595.92 = **$63,528.08** (all current).

**Year 3 (maturity / settlement)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y3 | Lease Liability | 63,528.08 | |
| | Cash | | 63,528.08 |
| | *Final payment extinguishes liability* | | |
| Dec 31, Y3 | Amortization Expense | 60,000.00 | |
| | Right-of-Use Asset | | 60,000.00 |
| | *Final ROU amortization; no interest after final payment* | | |

After Year 3 entries: **ROU = $0**, **Lease liability = $0**. Asset returns to lessor; no residual guarantee JE.

**(g) Rate change**  
If the **implicit rate were not readily determinable**, Cedar Ridge would discount at its **7% IBR**, producing a **lower** PV (and lower initial ROU/liability) than $180,000. Here the implicit rate **is known**, so measurement stays at **6% / $180,000** even though IBR is 7%.

**Key insight:** A basic finance lease is recognized like financed PPE: ROU + liability at PV of lease payments; subsequent accounting splits **interest** (effective interest on the liability) from **amortization** (straight-line on the ROU over the lease term when there is no ownership transfer/BPO).

---

### Q2 — CORE number variant — Full basic finance lease (Northwind Packaging)

**LO:** LO 17-2  
**Concept:** Number-variant twin — initial recognition, 4-year schedule, period-end and maturity JEs  
**Scenario:**  
On **January 1 of Year 1**, **Northwind Packaging Co.** leases a high-speed carton former from **Lakeside Capital Leasing**.

1. Noncancellable **4-year** lease; equipment is nonspecialized and reverts to Lakeside.  
2. **Four** annual payments of **$85,946.46** due **each January 1** beginning Year 1 (annuity due).  
3. Fair value at commencement = **$320,000**; economic life = **4 years**; residual estimate **$0**; no residual guarantee; no purchase/renewal option.  
4. Implicit rate **5%**, known by Northwind. Northwind’s IBR = **5.5%**.  
5. Fiscal year-end **December 31**. No ROU adjustments at commencement. Round to nearest cent; credit ROU directly for amortization.

**Required:**  
(a) Classify the lease and state the discount rate.  
(b) Measure commencement ROU asset and lease liability.  
(c) Prepare the full lease liability schedule.  
(d) Journal entries for **Year 1** (all four types: commencement, payment, interest, amortization).  
(e) Dec 31, Year 1: ROU carrying amount; current vs noncurrent lease liability.  
(f) Journal entries for **Year 4** only (final payment on Jan 1 and final amortization on Dec 31), and confirm zero balances.

**Answer key:**

**(a)** **Finance lease** — lease term is **100%** of economic life; PV of payments = **100%** of FV. Discount rate = **5%** (implicit rate known).

**(b)** `=PV(0.05,4,-85946.46,0,1)` → **$320,000.00**  
ROU asset = Lease liability = **$320,000** at commencement.

**(c) Lease liability schedule**

| Date | Lease payment | Interest (5%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | $320,000.00 |
| Jan 1, Y1 | $85,946.46 | $0.00 | $85,946.46 | 234,053.54 |
| Jan 1, Y2 | 85,946.46 | 11,702.68 | 74,243.78 | 159,809.76 |
| Jan 1, Y3 | 85,946.46 | 7,990.49 | 77,955.97 | 81,853.79 |
| Jan 1, Y4 | 85,946.46 | 4,092.67* | 81,853.79 | 0.00 |
| **Totals** | **$343,785.84** | **$23,785.84** | **$320,000.00** | |

\*Final interest plugged **$0.02** ($81,853.79 × 0.05 = $4,092.6895) so ending liability is exactly zero.  
Check: $343,785.84 − $320,000.00 = **$23,785.84** total interest.

**(d) Year 1 journal entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y1 | Right-of-Use Asset | 320,000.00 | |
| | Lease Liability | | 320,000.00 |
| Jan 1, Y1 | Lease Liability | 85,946.46 | |
| | Cash | | 85,946.46 |
| Dec 31, Y1 | Interest Expense | 11,702.68 | |
| | Lease Liability | | 11,702.68 |
| | *$234,053.54 × 5%* | | |
| Dec 31, Y1 | Amortization Expense | 80,000.00 | |
| | Right-of-Use Asset | | 80,000.00 |
| | *$320,000 / 4 years* | | |

All entries balance.

**(e) Dec 31, Year 1 presentation**  
- ROU asset: $320,000 − $80,000 = **$240,000**  
- Total lease liability: $234,053.54 + $11,702.68 = **$245,756.22**  
  - Current: **$85,946.46**  
  - Noncurrent: $245,756.22 − $85,946.46 = **$159,809.76**

**(f) Year 4 maturity entries**  
(After Jan 1, Y3 payment and Dec 31, Y3 accruals, liability before final payment = **$85,946.46**; ROU before final amort = **$80,000**.)

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y4 | Lease Liability | 85,946.46 | |
| | Cash | | 85,946.46 |
| Dec 31, Y4 | Amortization Expense | 80,000.00 | |
| | Right-of-Use Asset | | 80,000.00 |

**ROU = $0; Lease liability = $0** after maturity.

**Key insight:** Changing term, rate, and PV does not change the pattern—recognize PV, amortize liability with effective interest, amortize ROU straight-line over the lease term, and clear both accounts at final payment/period-end.

---

### Q3 — CORE — Period-end adjusting entries, interim measurement, and presentation (Harborline)

**LO:** LO 17-2  
**Concept:** Period-end interest/amortization adjusting JEs + interim liability measurement + BS classification  
**Scenario:**  
**Harborline Diagnostics** entered a **3-year finance lease** of laboratory imaging equipment on **January 1, Year 1** with **Pinnacle MedLease**. Commencement measurement (already recorded correctly):

- ROU asset and lease liability at commencement: **$96,000**  
- Annual payment (annuity due, each January 1): **$33,262.94**  
- Implicit rate known: **4%**  
- Economic life = lease term = 3 years; residual $0; asset reverts to lessor  
- First payment on January 1, Year 1 **was recorded** (Dr Lease Liability / Cr Cash $33,262.94)  
- No Year 1 adjusting entries have been made yet  

**Required:**  
(a) Complete the remaining two rows of the lease liability schedule (payments on Jan 1, Y2 and Jan 1, Y3).  
(b) Prepare the **December 31, Year 1** adjusting entries only.  
(c) Compute the lease liability that would be reported if Harborline prepared **interim statements on October 31, Year 1** (10 months of interest accrued; no payment between Jan 1 and Oct 31).  
(d) Prepare the **January 1, Year 2** payment entry and the **December 31, Year 2** adjusting entries.  
(e) At **December 31, Year 2**, classify the lease liability (current vs noncurrent) and state Year 2 interest and amortization expense.  
(f) Prepare the **January 1, Year 3** final payment and **December 31, Year 3** final amortization entry.

**Answer key:**

**(a) Schedule (liability after Jan 1, Y1 payment = $96,000 − $33,262.94 = $62,737.06)**

| Date | Lease payment | Interest (4%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (after payment) | $33,262.94 | $0.00 | $33,262.94 | $62,737.06 |
| Jan 1, Y2 | 33,262.94 | 2,509.48 | 30,753.46 | 31,983.60 |
| Jan 1, Y3 | 33,262.94 | 1,279.34 | 31,983.60 | 0.00 |

Interest Y1 period: $62,737.06 × 4% = **$2,509.4824 → $2,509.48**  
Interest Y2 period: $31,983.60 × 4% = **$1,279.344 → $1,279.34**  
Totals check: cash $99,788.82 − PV $96,000 = interest **$3,788.82** (= $2,509.48 + $1,279.34).

**(b) December 31, Year 1 adjusting entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec 31, Y1 | Interest Expense | 2,509.48 | |
| | Lease Liability | | 2,509.48 |
| Dec 31, Y1 | Amortization Expense | 32,000.00 | |
| | Right-of-Use Asset | | 32,000.00 |
| | *$96,000 / 3* | | |

Both balance. YE1 liability = $62,737.06 + $2,509.48 = **$65,246.54**; ROU = **$64,000**.

**(c) October 31, Year 1 interim liability**  
Interest for 10/12 of year: $2,509.48 × 10/12 = **$2,091.2333 → $2,091.23**  
Lease liability at Oct 31, Y1 = $62,737.06 + $2,091.23 = **$64,828.29**  
(If books use months × annual interest without separate monthly compounding — consistent with textbook Demo 17-2 interim illustration.)

**(d) Year 2 entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y2 | Lease Liability | 33,262.94 | |
| | Cash | | 33,262.94 |
| Dec 31, Y2 | Interest Expense | 1,279.34 | |
| | Lease Liability | | 1,279.34 |
| Dec 31, Y2 | Amortization Expense | 32,000.00 | |
| | Right-of-Use Asset | | 32,000.00 |

**(e) December 31, Year 2 presentation / expenses**  
- Interest expense Y2: **$1,279.34**  
- Amortization expense Y2: **$32,000.00**  
- ROU carrying amount: $64,000 − $32,000 = **$32,000**  
- Lease liability: $31,983.60 + $1,279.34 = **$33,262.94** — **all current**; noncurrent = **$0**

**(f) Year 3 maturity**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y3 | Lease Liability | 33,262.94 | |
| | Cash | | 33,262.94 |
| Dec 31, Y3 | Amortization Expense | 32,000.00 | |
| | Right-of-Use Asset | | 32,000.00 |

Balances after maturity: **ROU $0; Lease liability $0**.

**Key insight:** Payment-date schedules may not match reporting dates — accrue interest from the last payment date to the balance-sheet date, then classify the next cash payment as current; ROU amortization runs on the reporting calendar independently of the payment date.

---

### Q4 — MC — Discount rate for lessee measurement

**LO:** LO 17-2  
**Concept:** Implicit rate vs incremental borrowing rate for initial measurement  
**Question:**  
On commencement of a finance lease, the lessee knows the lessor’s **implicit rate is 6%**. The lessee’s **incremental borrowing rate is 8%**. There are no initial direct costs, prepayments, or incentives. Which statement is correct?

- A) Measure the lease liability using 8%, because the lessee’s own borrowing rate always controls.  
- B) Measure the lease liability using 6%, the rate implicit in the lease, because that rate is known.  
- C) Measure the lease liability using the average of 6% and 8%.  
- D) Measure the ROU asset at fair value of the underlying asset and the liability at 8%.

**Answer:** **B.** ASC 842 requires the lessee to discount lease payments using the **rate implicit in the lease when that rate is readily determinable**; only if it is not readily determinable does the lessee use its incremental borrowing rate. Here 6% is known, so both liability and (basic) ROU use the 6% PV.

---

### Q5 — MC — Finance lease income-statement presentation

**LO:** LO 17-2  
**Concept:** Dual expense presentation (interest + amortization) vs single lease expense  
**Question:**  
For a **basic finance lease**, which income-statement presentation is correct for the lessee in periods after commencement?

- A) A single “lease expense” equal to the cash payment each period.  
- B) A single “lease expense” equal to straight-line total cash rents over the term (operating-lease pattern).  
- C) Separate **interest expense** on the lease liability (effective interest) and **amortization expense** on the ROU asset (typically straight-line).  
- D) Only amortization expense; interest is capitalized into the ROU asset each period.

**Answer:** **C.** Finance leases present **two** expenses—interest (effective interest method on the liability) and ROU amortization (usually straight-line over the lease term when ownership does not transfer). Single straight-line lease expense is the **operating** lease pattern (LO 17-3), not the basic finance lease pattern.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV, interest, principal, ROU amort, current/noncurrent split)
- [x] Schedules roll to zero at maturity; total interest = total cash − PV
- [x] Core demo path (Demo 17-2 / Review 17-2 style) — not Expanding Your Knowledge sidebars
- [x] LO + Concept on every item
- [x] MC = 2 (classification/method/presentation only)
- [x] Original company names and amounts (not textbook $100,000 / $34,972 demo)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
