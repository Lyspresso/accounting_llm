# Agent 153 — CORE DEMO — LO 17-2

**Chapter:** 17  
**LO title:** Accounting for a Basic Finance Lease by a Lessee  
**Critical gap LO:** yes  
**Emphasis:** subsequent_measurement_schedule

## Concept list for this pack
- Classification of a basic lease as **finance** when at least one of the five ASC 842 criteria is met
- Initial recognition: ROU asset and lease liability at PV of lease payments (annuity-due)
- Discount rate hierarchy: rate implicit in the lease when known; otherwise incremental borrowing rate
- **Subsequent measurement schedule:** lease liability roll-forward under the effective interest method
- Period-end adjusting entries: interest accrual on the liability + straight-line ROU amortization
- Maturity / final settlement: final payment clears liability; final amort clears ROU (zero residual basic case)
- Presentation: dual IS expenses (interest + amortization); current vs noncurrent lease liability
- Number-variant twin of the full basic finance-lease life cycle

---

### Q1 — CORE — Subsequent measurement schedule + full basic finance lease (Ironvale)

**LO:** LO 17-2  
**Concept:** Subsequent measurement — complete lease liability schedule (effective interest) with initial recognition, period-end, and maturity JEs  
**Scenario:**  
On **January 1 of Year 1** (commencement), **Ironvale Machinery Co.** leases a precision stamping line from **Crestline Capital Partners**. Facts:

1. Noncancellable **4-year** lease of equipment that Crestline routinely leases to other customers (nonspecialized; alternative uses exist).  
2. **Four** annual lease payments of **$40,838.42**, payable **January 1** of Year 1, Year 2, Year 3, and Year 4 (**annuity due**).  
3. Fair value of the equipment at commencement = **$150,000**.  
4. Estimated economic life = **4 years**. Estimated residual value = **$0**; no residual value guarantee.  
5. No renewal or purchase option; asset reverts to Crestline at end of term.  
6. Lessor’s **implicit rate = 6%**, known by Ironvale. Ironvale’s incremental borrowing rate = **6.5%**.  
7. Ironvale’s fiscal year ends **December 31**. No initial direct costs, prepaid rent, or lease incentives (basic case: ROU = lease liability at commencement).  
8. Round interest and schedule amounts to the **nearest cent**. Credit the ROU asset **directly** for amortization (chapter convention). Amortize ROU **straight-line over the lease term** (no ownership transfer / no reasonably certain purchase option).

**Required:**  
(a) Classify the lease for the **lessee** and identify which classification criterion(s) are met.  
(b) Measure the lease liability and ROU asset at commencement; identify the discount rate used.  
(c) Prepare the **complete lease liability schedule** (effective interest method) — emphasize roll-forward of the liability balance each period.  
(d) Prepare **all lessee journal entries for Year 1** (commencement, payment, and December 31 adjusting entries).  
(e) Show **Year 1** balance sheet (ROU; current and noncurrent lease liability) and income statement lease-related expenses.  
(f) Prepare lessee journal entries for **Year 2**, **Year 3**, and **Year 4** (through maturity / asset return with zero residual).  
(g) How would measurement change if only the **6.5%** incremental borrowing rate were known (implicit rate not readily determinable)? Briefly.

**Answer key:**

**(a) Classification — finance lease**  
At least one of the five criteria is met:

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to lessor | No |
| 2. Purchase option reasonably certain | None | No |
| 3. Lease term major part of economic life | 4 / 4 = **100%** (≥ 75% bright line often used) | **Yes** |
| 4. PV of lease payments substantially all of FV | PV = $150,000 ≥ 90% × $150,000 | **Yes** |
| 5. Specialized asset / no alternative use | Routinely leased to others | No |

→ **Finance lease** to the lessee.

**(b) Measurement**  
Discount rate = **6%** (rate implicit in the lease, known by lessee — preferred over IBR).  

Excel: `=PV(0.06,4,-40838.42,0,1)` → **$150,000.00**  

Lease liability (commencement) = **$150,000.00**  
ROU asset (basic case, no adjustments) = **$150,000.00**

**(c) Lease liability schedule — subsequent measurement (emphasis)**  
Effective interest method. First payment on commencement day is **100% principal** (no time has elapsed). Each later payment = interest on beginning liability + principal reduction. Final-period interest is plugged **$0.01** so the liability clears exactly.

| Date | Lease payment | Interest on liability (6%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | $150,000.00 |
| Jan 1, Y1 | $40,838.42 | $0.00 | $40,838.42 | 109,161.58 |
| Jan 1, Y2 | 40,838.42 | 6,549.69 | 34,288.73 | 74,872.85 |
| Jan 1, Y3 | 40,838.42 | 4,492.37 | 36,346.05 | 38,526.80 |
| Jan 1, Y4 | 40,838.42 | 2,311.62* | 38,526.80 | 0.00 |
| **Totals** | **$163,353.68** | **$13,353.68** | **$150,000.00** | |

\*Raw interest $38,526.80 × 6% = $2,311.608 → schedule uses **$2,311.62** so payment − interest = remaining principal $38,526.80.  

*Computation notes:*  
- After Jan 1, Y1 payment: $150,000.00 − $40,838.42 = **$109,161.58**  
- Interest Y1 period (accrued Dec 31, Y1 / paid as part of Jan 1, Y2): $109,161.58 × 6% = **$6,549.6948 → $6,549.69**  
- Principal reduction on Jan 1, Y2: $40,838.42 − $6,549.69 = **$34,288.73**  
- Interest Y2 period: $74,872.85 × 6% = **$4,492.371 → $4,492.37**  
- Interest Y3 period (plug): **$2,311.62**  
- Check: total cash $163,353.68 − PV $150,000.00 = total interest **$13,353.68**.

**Period-end liability measurement (from schedule):**  
Add accrued interest from the most recent payment date to the reporting date.  
- Dec 31, Y1 liability = $109,161.58 + $6,549.69 = **$115,711.27**  
- Dec 31, Y2 liability = $74,872.85 + $4,492.37 = **$79,365.22**  
- Dec 31, Y3 liability = $38,526.80 + $2,311.62 = **$40,838.42** (all current)  
- After Jan 1, Y4 payment: **$0**

**(d) Year 1 journal entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y1 | Right-of-Use Asset | 150,000.00 | |
| | Lease Liability | | 150,000.00 |
| | *Record ROU asset and lease liability at commencement* | | |
| Jan 1, Y1 | Lease Liability | 40,838.42 | |
| | Cash | | 40,838.42 |
| | *First lease payment (all principal)* | | |
| Dec 31, Y1 | Interest Expense | 6,549.69 | |
| | Lease Liability | | 6,549.69 |
| | *Accrue interest: $109,161.58 × 6%* | | |
| Dec 31, Y1 | Amortization Expense | 37,500.00 | |
| | Right-of-Use Asset | | 37,500.00 |
| | *Straight-line ROU amort over lease term: $150,000 / 4* | | |

**Balance checks:** Dr = Cr on every entry ($150,000.00; $40,838.42; $6,549.69; $37,500.00).

**(e) Year 1 financial statement impact**

**Income statement — Year 1**  
- Interest expense—lease liability: **$6,549.69**  
- Amortization expense—ROU asset: **$37,500.00**  
- Total lease-related expense: **$44,049.69** (two lines — finance lease pattern)

**Balance sheet — Dec 31, Year 1**  
- ROU asset: $150,000.00 − $37,500.00 = **$112,500.00**  
- Lease liability total: $109,161.58 + $6,549.69 = **$115,711.27**  
  - Current lease liability = next payment **$40,838.42** (= accrued interest $6,549.69 + principal reduction $34,288.73)  
  - Noncurrent lease liability = $115,711.27 − $40,838.42 = **$74,872.85**

**(f) Year 2–Year 4 journal entries (through maturity)**

**Year 2**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y2 | Lease Liability | 40,838.42 | |
| | Cash | | 40,838.42 |
| | *Pays accrued interest $6,549.69 + principal $34,288.73* | | |
| Dec 31, Y2 | Interest Expense | 4,492.37 | |
| | Lease Liability | | 4,492.37 |
| | *$74,872.85 × 6%* | | |
| Dec 31, Y2 | Amortization Expense | 37,500.00 | |
| | Right-of-Use Asset | | 37,500.00 |

After Dec 31, Y2: ROU = **$75,000.00**; lease liability = $74,872.85 + $4,492.37 = **$79,365.22** (current $40,838.42; noncurrent $38,526.80).

**Year 3**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y3 | Lease Liability | 40,838.42 | |
| | Cash | | 40,838.42 |
| Dec 31, Y3 | Interest Expense | 2,311.62 | |
| | Lease Liability | | 2,311.62 |
| | *Schedule / plug interest on $38,526.80* | | |
| Dec 31, Y3 | Amortization Expense | 37,500.00 | |
| | Right-of-Use Asset | | 37,500.00 |

After Dec 31, Y3: ROU = **$37,500.00**; lease liability = **$40,838.42** (all current).

**Year 4 (maturity / settlement)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y4 | Lease Liability | 40,838.42 | |
| | Cash | | 40,838.42 |
| | *Final payment extinguishes liability* | | |
| Dec 31, Y4 | Amortization Expense | 37,500.00 | |
| | Right-of-Use Asset | | 37,500.00 |
| | *Final ROU amortization; no interest after final payment* | | |

After Year 4 entries: **ROU = $0**, **Lease liability = $0**. Asset returns to lessor; no residual guarantee JE.

**(g) Rate change**  
If the **implicit rate were not readily determinable**, Ironvale would discount at its **6.5% IBR**, producing a **lower** PV (and lower initial ROU/liability) than $150,000. Here the implicit rate **is known**, so measurement stays at **6% / $150,000** even though IBR is 6.5%.

**Key insight:** Subsequent measurement of a basic finance lease is driven by the **lease liability schedule**: each period’s interest is beginning liability × discount rate (except the day-one payment), payments reduce the liability, and ROU amortization runs **separately** on a straight-line path over the lease term until both accounts hit zero at maturity.

---

### Q2 — CORE number variant — Full basic finance lease schedule (Solstice)

**LO:** LO 17-2  
**Concept:** Number-variant twin — recompute PV, full subsequent-measurement liability schedule, period-end and maturity JEs  
**Scenario:**  
On **January 1 of Year 1**, **Solstice Beverage Group** leases a high-speed bottling system from **Atlas Equipment Finance**.

1. Noncancellable **5-year** lease; equipment is nonspecialized and reverts to Atlas.  
2. **Five** annual payments of **$60,493.40** due **each January 1** beginning Year 1 (annuity due).  
3. Fair value at commencement = **$275,000**; economic life = **5 years**; residual estimate **$0**; no residual guarantee; no purchase/renewal option.  
4. Implicit rate **5%**, known by Solstice. Solstice’s IBR = **5.75%**.  
5. Fiscal year-end **December 31**. No ROU adjustments at commencement. Round to nearest cent; credit ROU directly for amortization.

**Required:**  
(a) Classify the lease and state the discount rate.  
(b) Measure commencement ROU asset and lease liability.  
(c) Prepare the **full lease liability schedule** (subsequent measurement).  
(d) Journal entries for **Year 1** (commencement, payment, interest, amortization).  
(e) Dec 31, Year 1: ROU carrying amount; current vs noncurrent lease liability.  
(f) Journal entries for **Year 5** only (final payment on Jan 1 and final amortization on Dec 31), and confirm zero balances.  
(g) State total interest over the lease term from the schedule.

**Answer key:**

**(a)** **Finance lease** — lease term is **100%** of economic life; PV of payments = **100%** of FV. Discount rate = **5%** (implicit rate known).

**(b)** `=PV(0.05,5,-60493.40,0,1)` → **$275,000.00**  
ROU asset = Lease liability = **$275,000.00** at commencement.

**(c) Lease liability schedule — subsequent measurement**

| Date | Lease payment | Interest (5%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | $275,000.00 |
| Jan 1, Y1 | $60,493.40 | $0.00 | $60,493.40 | 214,506.60 |
| Jan 1, Y2 | 60,493.40 | 10,725.33 | 49,768.07 | 164,738.53 |
| Jan 1, Y3 | 60,493.40 | 8,236.93 | 52,256.47 | 112,482.06 |
| Jan 1, Y4 | 60,493.40 | 5,624.10 | 54,869.30 | 57,612.76 |
| Jan 1, Y5 | 60,493.40 | 2,880.64 | 57,612.76 | 0.00 |
| **Totals** | **$302,467.00** | **$27,467.00** | **$275,000.00** | |

*Computation notes:*  
- $214,506.60 × 5% = **$10,725.33**  
- $164,738.53 × 5% = **$8,236.9265 → $8,236.93**  
- $112,482.06 × 5% = **$5,624.103 → $5,624.10**  
- $57,612.76 × 5% = **$2,880.638 → $2,880.64** (equals $60,493.40 − $57,612.76)  
- Check: $302,467.00 − $275,000.00 = **$27,467.00** total interest.

**(d) Year 1 journal entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y1 | Right-of-Use Asset | 275,000.00 | |
| | Lease Liability | | 275,000.00 |
| Jan 1, Y1 | Lease Liability | 60,493.40 | |
| | Cash | | 60,493.40 |
| Dec 31, Y1 | Interest Expense | 10,725.33 | |
| | Lease Liability | | 10,725.33 |
| | *$214,506.60 × 5%* | | |
| Dec 31, Y1 | Amortization Expense | 55,000.00 | |
| | Right-of-Use Asset | | 55,000.00 |
| | *$275,000 / 5 years* | | |

All entries balance.

**(e) Dec 31, Year 1 presentation**  
- ROU asset: $275,000.00 − $55,000.00 = **$220,000.00**  
- Total lease liability: $214,506.60 + $10,725.33 = **$225,231.93**  
  - Current: **$60,493.40**  
  - Noncurrent: $225,231.93 − $60,493.40 = **$164,738.53**

**(f) Year 5 maturity entries**  
(After Jan 1, Y4 payment and Dec 31, Y4 accrual, liability before final payment = **$60,493.40**; ROU before final amort = **$55,000.00**.)

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y5 | Lease Liability | 60,493.40 | |
| | Cash | | 60,493.40 |
| Dec 31, Y5 | Amortization Expense | 55,000.00 | |
| | Right-of-Use Asset | | 55,000.00 |

**ROU = $0; Lease liability = $0** after maturity.

**(g)** Total interest over the lease = **$27,467.00** (from schedule totals).

**Key insight:** Changing term, rate, payment, and PV does not change the **subsequent measurement pattern**—build the effective-interest liability schedule, accrue interest at each reporting date, amortize ROU straight-line over the lease term, and clear both accounts at final payment / final period-end.

---

### Q3 — CORE — Period-end adjusting entries, interim liability, and maturity (Clearbrook)

**LO:** LO 17-2  
**Concept:** Period-end interest/amortization adjusting JEs + interim liability from the schedule + maturity settlement  
**Scenario:**  
**Clearbrook Diagnostics** entered a **3-year finance lease** of laboratory analyzers on **January 1, Year 1** with **Meridian Lab Leasing**. Commencement measurement (already recorded correctly):

- ROU asset and lease liability at commencement: **$105,000**  
- Annual payment (annuity due, each January 1): **$37,392.92**  
- Implicit rate known: **7%**  
- Economic life = lease term = 3 years; residual $0; asset reverts to lessor  
- First payment on January 1, Year 1 **was recorded** (Dr Lease Liability / Cr Cash $37,392.92)  
- No Year 1 adjusting entries have been made yet  

**Required:**  
(a) Complete the remaining rows of the **lease liability schedule** (payments on Jan 1, Y2 and Jan 1, Y3) after the post–Jan 1, Y1 balance.  
(b) Prepare the **December 31, Year 1** adjusting entries only.  
(c) Compute the lease liability that would be reported if Clearbrook prepared **interim statements on October 31, Year 1** (10 months of interest accrued; no payment between Jan 1 and Oct 31).  
(d) Prepare the **January 1, Year 2** payment entry and the **December 31, Year 2** adjusting entries.  
(e) At **December 31, Year 2**, classify the lease liability (current vs noncurrent) and state Year 2 interest and amortization expense.  
(f) Prepare the **January 1, Year 3** final payment and **December 31, Year 3** final amortization entry.

**Answer key:**

**(a) Schedule (liability after Jan 1, Y1 payment = $105,000.00 − $37,392.92 = $67,607.08)**

| Date | Lease payment | Interest (7%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (after payment) | $37,392.92 | $0.00 | $37,392.92 | $67,607.08 |
| Jan 1, Y2 | 37,392.92 | 4,732.50 | 32,660.42 | 34,946.66 |
| Jan 1, Y3 | 37,392.92 | 2,446.26 | 34,946.66 | 0.00 |

Interest Y1 period: $67,607.08 × 7% = **$4,732.4956 → $4,732.50**  
Interest Y2 period: $34,946.66 × 7% = $2,446.2662; schedule uses **$2,446.26** so payment clears the remaining principal ($37,392.92 − $34,946.66).  
Totals check: cash $112,178.76 − PV $105,000.00 = interest **$7,178.76** (= $4,732.50 + $2,446.26).

**(b) December 31, Year 1 adjusting entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec 31, Y1 | Interest Expense | 4,732.50 | |
| | Lease Liability | | 4,732.50 |
| Dec 31, Y1 | Amortization Expense | 35,000.00 | |
| | Right-of-Use Asset | | 35,000.00 |
| | *$105,000 / 3* | | |

Both balance. YE1 liability = $67,607.08 + $4,732.50 = **$72,339.58**; ROU = **$70,000.00**.

**(c) October 31, Year 1 interim liability**  
Interest for 10/12 of year: $4,732.50 × 10/12 = **$3,943.75**  
Lease liability at Oct 31, Y1 = $67,607.08 + $3,943.75 = **$71,550.83**  
(Consistent with textbook Demo 17-2 interim illustration: accrue a fraction of the annual effective interest from the last payment date; no separate monthly compounding.)

**(d) Year 2 entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y2 | Lease Liability | 37,392.92 | |
| | Cash | | 37,392.92 |
| Dec 31, Y2 | Interest Expense | 2,446.26 | |
| | Lease Liability | | 2,446.26 |
| Dec 31, Y2 | Amortization Expense | 35,000.00 | |
| | Right-of-Use Asset | | 35,000.00 |

**(e) December 31, Year 2 presentation / expenses**  
- Interest expense Y2: **$2,446.26**  
- Amortization expense Y2: **$35,000.00**  
- ROU carrying amount: $70,000.00 − $35,000.00 = **$35,000.00**  
- Lease liability: $34,946.66 + $2,446.26 = **$37,392.92** — **all current**; noncurrent = **$0**

**(f) Year 3 maturity**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y3 | Lease Liability | 37,392.92 | |
| | Cash | | 37,392.92 |
| Dec 31, Y3 | Amortization Expense | 35,000.00 | |
| | Right-of-Use Asset | | 35,000.00 |

Balances after maturity: **ROU $0; Lease liability $0**.

**Key insight:** The **subsequent measurement schedule** is the control document—payment-date rows may not match reporting dates, so accrue interest from the last payment date to the balance-sheet (or interim) date, classify the next cash payment as current, and run ROU amortization on the reporting calendar until maturity clears both accounts.

---

### Q4 — MC — Finance lease income-statement and balance-sheet presentation

**LO:** LO 17-2  
**Concept:** Classification/presentation — dual expense pattern and current vs noncurrent liability  
**Question:**  
**Thornridge Logistics** is the lessee in a basic **finance** lease (annuity-due payments each January 1; fiscal year ends December 31). At December 31 of Year 1, after period-end adjusting entries, the lease liability schedule shows: accrued interest for Year 1 of **$5,200**, principal reduction that will occur with the January 1, Year 2 payment of **$28,800**, and remaining liability after that Year 2 payment of **$62,000**. ROU amortization for Year 1 was **$30,000**. Which presentation is correct?

- A) Income statement: single lease expense of $34,000; balance sheet: all $96,000 lease liability as noncurrent.  
- B) Income statement: interest expense $5,200 and amortization expense $30,000; balance sheet: current lease liability $34,000 and noncurrent lease liability $62,000.  
- C) Income statement: interest expense $5,200 only; ROU amortization is not recognized for finance leases.  
- D) Income statement: interest $5,200 and amortization $30,000; balance sheet: current lease liability $5,200 and noncurrent $90,800.

**Answer:** **B.** Basic finance leases present **two** expenses—interest (effective interest on the liability) and ROU amortization (typically straight-line over the lease term). At year-end, the **current** portion equals the **next cash payment** ($5,200 accrued interest + $28,800 principal = **$34,000**); the **noncurrent** portion is the liability remaining after that next payment (**$62,000**). Single straight-line “lease expense” is the **operating** lease pattern (LO 17-3), not the finance pattern.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV, interest, principal, ROU amort, current/noncurrent split, interim accrual)
- [x] Schedules roll to zero at maturity; total interest = total cash − PV
- [x] Core demo path (Demo 17-2 / Review 17-2 style) — not Expanding Your Knowledge sidebars
- [x] LO + Concept on every item
- [x] MC = 1 (classification/presentation only)
- [x] Original company names and amounts (not textbook $100,000 / $34,972 demo; not agent_022 amounts)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Emphasis on subsequent_measurement_schedule (Q1 schedule-first; Q2 full schedule twin; Q3 schedule-driven period-end/interim)
