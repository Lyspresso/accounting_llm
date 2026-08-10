# Agent 156 — CORE DEMO — LO 17-5

**Chapter:** 17  
**LO title:** Account for complex operating leases for a lessee  
**Critical gap LO:** yes  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- Operating classification when none of the five finance criteria are met
- Initial measurement of **lease liability** = PV of lease payments (same base as finance)
- **Right-of-use asset** = lease liability − lease incentives + initial direct costs
- Pre-commencement JEs for cash incentive and incremental legal (IDC) costs
- Commencement JE that records ROU/liability and clears IDC and incentive balances
- **Lease liability amortization schedule** (effective interest; annuity-due payments) — emphasis input
- **ROU subsequent measurement schedule**: straight-line single lease expense − period “interest” = ROU reduction
- Period-end adjusting JE: Dr Lease expense / Cr Lease liability / Cr ROU (not separate interest + amortization on the IS)
- Prepaid first payment: reduce liability after measuring gross PV; ROU still reflects liability − incentive + IDC
- Maturity / settlement: liability and ROU both to zero after final year
- Presentation: single lease expense in income from continuing operations; SCF classifies full operating-lease payment as operating outflow
- Number-variant twin (all facts/numbers changed)

---

### Q1 — CORE — Dual subsequent schedules for complex operating lease (IDC + incentive)
**LO:** LO 17-5  
**Concept:** Subsequent measurement schedules (liability + ROU); single SL lease expense plug; initial recognition; period-end JE; maturity settlement  
**Scenario:** On **January 1, Year 1** (commencement), **Harborline Logistics Inc.** (lessee) leases specialized warehouse sorting equipment from **Northspan Equipment Leasing LLC**. Facts:

1. Noncancellable **3-year** lease; equipment reverts to Northspan at end of term.  
2. Remaining economic life of the equipment is **10 years**.  
3. Fair value at commencement is **$350,000**.  
4. Three annual lease payments of **$42,841** due **January 1** of Year 1, Year 2, and Year 3 (payments in advance).  
5. No purchase or renewal option that is reasonably certain to be exercised.  
6. Residual value is **unguaranteed**; Northspan routinely re-leases this class of equipment to other logistics firms.  
7. Lessor’s implicit rate is **5%** and is known to Harborline.  
8. Before commencement, Harborline paid **$1,800** of incremental legal fees to execute the lease (initial direct costs).  
9. Before commencement, Northspan paid Harborline a **$4,500** cash lease incentive; Harborline recorded Cash and Lease Incentive Liability.  
10. Harborline’s fiscal year ends **December 31**.

**Required:**  
(a) Journal entries for the initial direct cost and the lease incentive **prior to** commencement.  
(b) Classify the lease for Harborline (apply all five criteria; show PV for criterion 4).  
(c) Compute the **lease liability** and **right-of-use asset** at commencement.  
(d) Prepare the commencement journal entry that records ROU and lease liability (and clears IDC and incentive balances), and the January 1, Year 1 cash lease payment.  
(e) Prepare the **lease liability amortization schedule** and the **right-of-use asset subsequent measurement schedule** for the full term (emphasis).  
(f) Prepare the **December 31, Year 1** period-end lease-expense adjusting entry.  
(g) Show Year 1 income-statement lease expense and Dec 31 Year 1 balance-sheet amounts (ROU net; current and noncurrent lease liability).  
(h) Prepare Year 2 journal entries and **Year 3 (maturity)** journal entries; confirm ROU and liability are zero after maturity.

**Answer key:**

**(a) Prior to commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Initial Direct Cost | 1,800 | |
| Cash | | 1,800 |
| *Incremental legal fees to execute the lease (IDC)* | | |

**Check:** Dr 1,800 = Cr 1,800. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 4,500 | |
| Lease Incentive Liability | | 4,500 |
| *Cash lease incentive received before commencement* | | |

**Check:** Dr 4,500 = Cr 4,500. **Balanced.**

**(b) Classification — operating lease** (no finance criterion met)

| Criterion | Analysis | Met? |
|---|---|---|
| 1 Ownership transfer | Asset reverts to lessor | No |
| 2 Purchase option | None | No |
| 3 Lease term | 3 / 10 = **30%** < 75% | No |
| 4 PV of lease payments | PV of 3 payments in advance at 5% = **$122,500** < 90% × $350,000 = $315,000 (and even net of the $4,500 incentive for classification analysis, PV remains well below 90% of FV) | No |
| 5 No alternative use | Lessor routinely re-leases equipment of this class | No |

Excel: `=PV(0.05,3,−42841,0,1)` → **$122,500** (rounded).  
→ **Operating lease.**

**(c) Measurement**  
- **Lease liability** = PV of lease payments at commencement = **$122,500**.  
- **Right-of-use asset** = lease liability − lease incentive + initial direct costs  
  \(= 122{,}500 - 4{,}500 + 1{,}800 = \mathbf{\$119{,}800}\).

**(d) January 1, Year 1 — commencement and first payment**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 119,800 | |
| Lease Incentive Liability | 4,500 | |
| Initial Direct Cost | | 1,800 |
| Lease Liability | | 122,500 |
| *Record ROU and liability; clear IDC asset and incentive liability* | | |

**Check:** Dr 124,300 = Cr 124,300. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,841 | |
| Cash | | 42,841 |
| *First annuity-due lease payment* | | |

**Check:** Dr 42,841 = Cr 42,841. **Balanced.**  
Liability after payment: \(122{,}500 - 42{,}841 = \mathbf{\$79{,}659}\).

**(e) Subsequent measurement schedules (emphasis)**

**Lease liability schedule** (rate 5%; amounts to nearest cent)

| Date | Lease payment | Interest (5%) | Principal reduction | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 122,500.00 |
| Jan 1, Y1 | 42,841.00 | 0.00 | 42,841.00 | 79,659.00 |
| Jan 1, Y2 | 42,841.00 | 3,982.95 | 38,858.05 | 40,800.95 |
| Jan 1, Y3 | 42,841.00 | 2,040.05 | 40,800.95 | 0.00 |
| **Totals** | **128,523.00** | **6,023.00** | **122,500.00** | |

Interest checks: \(79{,}659.00 \times 0.05 = 3{,}982.95\); \(40{,}800.95 \times 0.05 = 2{,}040.05\).

**Right-of-use asset schedule**  
Total cost of the lease = undiscounted payments + IDC − incentive  
\(= 128{,}523 + 1{,}800 - 4{,}500 = \mathbf{\$125{,}823}\).  
Straight-line lease expense = \(125{,}823 / 3 = \mathbf{\$41{,}941}\) per year.  
ROU reduction each period = SL lease expense − that period’s “interest” from the liability schedule (interest shown on the *next* payment date; zero in the final year after the last payment).

| Date | Lease expense (SL) | Interest on liability | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commence) | | | | 119,800.00 |
| Dec 31, Y1 | 41,941.00 | 3,982.95 | 37,958.05 | 81,841.95 |
| Dec 31, Y2 | 41,941.00 | 2,040.05 | 39,900.95 | 41,941.00 |
| Dec 31, Y3 | 41,941.00 | 0.00 | 41,941.00 | 0.00 |
| **Totals** | **125,823.00** | **6,023.00** | **119,800.00** | |

**Schedule rollforward checks:**  
- Liability ends at **$0**; principal reductions sum to **$122,500**.  
- ROU ends at **$0**; ROU reductions sum to **$119,800**.  
- Total lease expense = total interest-component + total ROU reduction = \(6{,}023 + 119{,}800 = 125{,}823\).

**(f) December 31, Year 1 — period-end single lease expense**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 41,941.00 | |
| Lease Liability | | 3,982.95 |
| Right-of-Use Asset | | 37,958.05 |
| *SL operating lease expense; accrete liability; reduce ROU (plug)* | | |

**Check:** Dr 41,941.00 = Cr 3,982.95 + 37,958.05. **Balanced.**

**(g) Year 1 financial statement impact**

**Income statement (Year 1):**  
- Lease expense (single amount in income from continuing operations): **$41,941**  
- *Not* separate interest expense + ROU amortization (finance-lease presentation).

**Balance sheet (Dec 31, Year 1):**  
- ROU asset (net): \(119{,}800 - 37{,}958.05 = \mathbf{\$81{,}841.95}\)  
- Total lease liability: \(79{,}659 + 3{,}982.95 = \mathbf{\$83{,}641.95}\)  
- **Current** lease liability = next payment **$42,841**  
- **Noncurrent** lease liability: \(83{,}641.95 - 42{,}841 = \mathbf{\$40{,}800.95}\)

**Statement of cash flows (Year 1):** full cash lease payment **$42,841** is an **operating** cash outflow (operating lease).

**(h) Year 2 and Year 3 (maturity)**

**Year 2**  
January 1, Year 2 — payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,841.00 | |
| Cash | | 42,841.00 |

**Check:** Dr = Cr = 42,841. **Balanced.**

December 31, Year 2 — lease expense:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 41,941.00 | |
| Lease Liability | | 2,040.05 |
| Right-of-Use Asset | | 39,900.95 |

**Check:** Dr 41,941.00 = Cr 2,040.05 + 39,900.95. **Balanced.**

**Year 3 — maturity / settlement**  
January 1, Year 3 — final payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,841.00 | |
| Cash | | 42,841.00 |

**Check:** Dr = Cr = 42,841. **Balanced.**  
After this payment, lease liability = **$0**.

December 31, Year 3 — final ROU reduction (no remaining “interest”):

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 41,941.00 | |
| Right-of-Use Asset | | 41,941.00 |

**Check:** Dr = Cr = 41,941. **Balanced.**

After Year 3 entries: **ROU = $0** and **lease liability = $0**. Asset returned to lessor; no residual settlement (unguaranteed).

**Key insight:** Complex operating leases use the **same initial measurement** as finance leases (liability = PV of payments; ROU adjusted for incentives and IDC), but **subsequent** measurement produces a **single straight-line lease expense**. The liability schedule’s “interest” is **not** reported as interest expense; it is an **input** to the ROU reduction plug so that Expense = Interest-component + ROU-reduction each period.

---

### Q2 — CORE number variant — Dual schedules twin (all numbers changed)
**LO:** LO 17-5  
**Concept:** Complex operating lease — IDC + incentive; subsequent measurement schedules (all numbers changed)  
**Scenario:** On **January 1, Year 1**, **Redcedar Bottling Co.** leases refrigerated warehouse racking under a **4-year** noncancellable lease from **Glacier Capital Leasing**. Facts:

1. Economic life **15 years**; equipment reverts to lessor; no PO reasonably certain to exercise; residual unguaranteed; lessor re-leases this class of racking.  
2. Annual payments of **$49,959** due **January 1** each year for 4 years (in advance).  
3. Fair value at commencement **$520,000**.  
4. Implicit rate known to lessee: **6%**.  
5. Pre-commencement initial direct costs (execution legal fees): **$2,100**.  
6. Pre-commencement cash lease incentive from lessor: **$5,500** (recorded as Lease Incentive Liability).  
7. Year-end December 31.

**Required:**  
(a) Classify the lease (brief support).  
(b) Compute lease liability and ROU asset at commencement.  
(c) Prepare the commencement JE (including clearing IDC and incentive) and the first cash payment.  
(d) Prepare the full **lease liability schedule** and **ROU asset schedule** (emphasis).  
(e) Record Year 1 Dec 31 lease-expense adjusting entry.  
(f) State Year 1 lease expense and Dec 31 current vs noncurrent lease liability.  
(g) Record Year 4 (maturity) payment and final lease-expense entry; confirm zero balances.

**Answer key:**

**(a) Operating lease** — 4/15 = 26.7% < 75%; PV of payments \(=\mathbf{\$183{,}500}\) < 90% × $520,000 = $468,000; no transfer, no PO, alternative use exists.

Excel: `=PV(0.06,4,−49959,0,1)` → **$183,500** (rounded).

**(b) Measurement**  
- Lease liability = **$183,500**  
- ROU asset = \(183{,}500 - 5{,}500 + 2{,}100 = \mathbf{\$180{,}100}\)

**(c) January 1, Year 1 — commencement and first payment**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 180,100 | |
| Lease Incentive Liability | 5,500 | |
| Initial Direct Cost | | 2,100 |
| Lease Liability | | 183,500 |

**Check:** Dr 185,600 = Cr 185,600. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 49,959 | |
| Cash | | 49,959 |

**Check:** Dr = Cr = 49,959. **Balanced.**  
Liability after payment: \(183{,}500 - 49{,}959 = \mathbf{\$133{,}541}\).

**(d) Lease liability schedule** (6%)

| Date | Lease payment | Interest (6%) | Principal | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 183,500.00 |
| Jan 1, Y1 | 49,959.00 | 0.00 | 49,959.00 | 133,541.00 |
| Jan 1, Y2 | 49,959.00 | 8,012.46 | 41,946.54 | 91,594.46 |
| Jan 1, Y3 | 49,959.00 | 5,495.67 | 44,463.33 | 47,131.13 |
| Jan 1, Y4 | 49,959.00 | 2,827.87 | 47,131.13 | 0.00 |
| **Totals** | **199,836.00** | **16,336.00** | **183,500.00** | |

Interest checks: \(133{,}541 \times 0.06 = 8{,}012.46\); \(91{,}594.46 \times 0.06 = 5{,}495.67\); \(47{,}131.13 \times 0.06 = 2{,}827.87\).

**ROU schedule**  
Total cost = \(199{,}836 + 2{,}100 - 5{,}500 = \mathbf{\$196{,}436}\)  
SL lease expense = \(196{,}436 / 4 = \mathbf{\$49{,}109}\)

| Date | Lease expense (SL) | Interest on liability | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | | | | 180,100.00 |
| Dec 31, Y1 | 49,109.00 | 8,012.46 | 41,096.54 | 139,003.46 |
| Dec 31, Y2 | 49,109.00 | 5,495.67 | 43,613.33 | 95,390.13 |
| Dec 31, Y3 | 49,109.00 | 2,827.87 | 46,281.13 | 49,109.00 |
| Dec 31, Y4 | 49,109.00 | 0.00 | 49,109.00 | 0.00 |
| **Totals** | **196,436.00** | **16,336.00** | **180,100.00** | |

**(e) December 31, Year 1 — lease expense**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 49,109.00 | |
| Lease Liability | | 8,012.46 |
| Right-of-Use Asset | | 41,096.54 |

**Check:** Dr 49,109.00 = Cr 8,012.46 + 41,096.54. **Balanced.**

**(f) Year 1 reporting**  
- Lease expense: **$49,109** (single amount in income from continuing operations).  
- Total liability at Dec 31, Y1: \(133{,}541 + 8{,}012.46 = \mathbf{\$141{,}553.46}\)  
- **Current** lease liability: **$49,959**  
- **Noncurrent** lease liability: \(141{,}553.46 - 49{,}959 = \mathbf{\$91{,}594.46}\)  
- ROU net: \(180{,}100 - 41{,}096.54 = \mathbf{\$139{,}003.46}\)

**(g) Year 4 maturity**

January 1, Year 4 — final payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 49,959.00 | |
| Cash | | 49,959.00 |

**Check:** Dr = Cr = 49,959. **Balanced.** Liability → **$0**.

December 31, Year 4 — final expense (no interest component):

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 49,109.00 | |
| Right-of-Use Asset | | 49,109.00 |

**Check:** Dr = Cr = 49,109. **Balanced.** ROU → **$0**.

**Key insight:** Changing term, rate, payments, IDC, and incentive changes every schedule cell, but the **structure** is identical: SL expense from total lease cost ÷ periods; ROU reduction = expense − liability interest component.

---

### Q3 — CORE alternate angle — Prepaid first payment; period-end expense; maturity
**LO:** LO 17-5  
**Concept:** Complex operating lease with prepayment of first payment; initial recognition bridge; subsequent schedules; maturity  
**Scenario:** On **December 28, Year 0**, **Pinecrest Specialty Clinics** prepaid the first annual lease payment on a lease that **commences January 1, Year 1**. Pinecrest recorded:

| Account | Debit | Credit |
|---|---:|---:|
| Prepaid Lease Payment | 41,582 | |
| Cash | | 41,582 |

**Lease facts at commencement (January 1, Year 1):**  
1. Noncancellable **3-year** lease of clinical imaging support equipment from **Oakridge Property Partners**; asset reverts to lessor.  
2. Economic life **12 years**; FV **$300,000**; residual unguaranteed; lessor has alternative uses.  
3. Three annual payments of **$41,582** due **January 1** each year (in advance); first payment already prepaid on Dec 28, Year 0.  
4. Implicit rate **5%** known to Pinecrest.  
5. Before commencement, Pinecrest also paid **$900** IDC (legal fees) and received a **$3,000** cash lease incentive (already on books as Initial Direct Cost and Lease Incentive Liability, respectively).  
6. Year-end December 31.

**Required:**  
(a) Classify the lease and compute gross lease liability and ROU at commencement.  
(b) Prepare the January 1, Year 1 commencement entry (clear IDC and incentive) **and** the entry to apply the prepaid payment against the lease liability.  
(c) Prepare the liability schedule and ROU schedule for the full term.  
(d) Record Dec 31, Year 1 period-end lease expense.  
(e) Record Year 3 maturity payment and final expense; confirm zero balances.

**Answer key:**

**(a) Classification and measurement**  
**Operating lease:** 3/12 = 25% < 75%; PV = **$118,900** < 90% × $300,000 = $270,000; no transfer/PO; alternative use exists.  
Excel: `=PV(0.05,3,−41582,0,1)` → **$118,900**.

- Gross lease liability (PV of payments) = **$118,900**  
- ROU asset = \(118{,}900 - 3{,}000 + 900 = \mathbf{\$116{,}800}\)

**(b) January 1, Year 1 — commencement and apply prepayment**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 116,800 | |
| Lease Incentive Liability | 3,000 | |
| Initial Direct Cost | | 900 |
| Lease Liability | | 118,900 |

**Check:** Dr 119,800 = Cr 119,800. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 41,582 | |
| Prepaid Lease Payment | | 41,582 |
| *Apply prepayment to reduce lease liability (no cash at commencement)* | | |

**Check:** Dr = Cr = 41,582. **Balanced.**  
Net lease liability after prepayment application: \(118{,}900 - 41{,}582 = \mathbf{\$77{,}318}\).  
ROU remains **$116,800** (prepayment reduces liability, not ROU).

**(c) Schedules**

**Lease liability schedule** (5%)

| Date | Lease payment | Interest (5%) | Principal | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial gross) | | | | 118,900.00 |
| Jan 1, Y1 (apply prepaid) | 41,582.00 | 0.00 | 41,582.00 | 77,318.00 |
| Jan 1, Y2 | 41,582.00 | 3,865.90 | 37,716.10 | 39,601.90 |
| Jan 1, Y3 | 41,582.00 | 1,980.10 | 39,601.90 | 0.00 |
| **Totals** | **124,746.00** | **5,846.00** | **118,900.00** | |

Interest checks: \(77{,}318 \times 0.05 = 3{,}865.90\); \(39{,}601.90 \times 0.05 = 1{,}980.10\).

**ROU schedule**  
Total cost = \(124{,}746 + 900 - 3{,}000 = \mathbf{\$122{,}646}\)  
SL lease expense = \(122{,}646 / 3 = \mathbf{\$40{,}882}\)

| Date | Lease expense (SL) | Interest on liability | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | | | | 116,800.00 |
| Dec 31, Y1 | 40,882.00 | 3,865.90 | 37,016.10 | 79,783.90 |
| Dec 31, Y2 | 40,882.00 | 1,980.10 | 38,901.90 | 40,882.00 |
| Dec 31, Y3 | 40,882.00 | 0.00 | 40,882.00 | 0.00 |
| **Totals** | **122,646.00** | **5,846.00** | **116,800.00** | |

**(d) December 31, Year 1 — period-end**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 40,882.00 | |
| Lease Liability | | 3,865.90 |
| Right-of-Use Asset | | 37,016.10 |

**Check:** Dr 40,882.00 = Cr 3,865.90 + 37,016.10. **Balanced.**

Dec 31, Y1 BS: ROU **$79,783.90**; total liability \(77{,}318 + 3{,}865.90 = \mathbf{\$81{,}183.90}\); current **$41,582**; noncurrent **$39,601.90**.

**(e) Year 3 maturity**

January 1, Year 3 — final payment (cash):

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 41,582.00 | |
| Cash | | 41,582.00 |

**Check:** Dr = Cr = 41,582. **Balanced.** Liability → **$0**.

December 31, Year 3 — final expense:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 40,882.00 | |
| Right-of-Use Asset | | 40,882.00 |

**Check:** Dr = Cr = 40,882. **Balanced.** ROU → **$0**.

**Key insight:** Prepaying the first payment **before commencement** does not change the PV used for the **gross** liability or the ROU (still liability − incentive + IDC). The prepayment is applied by reducing the liability (and clearing Prepaid Lease Payment) so the **net** liability at commencement equals PV of remaining payments.

---

### Q4 — MC — Classification: guaranteed residual can flip operating vs finance
**LO:** LO 17-5  
**Concept:** Guaranteed residual — criterion 4 classification PV vs operating-lease classification context  
**Question:** Lessee enters a 3-year equipment lease with no ownership transfer, no purchase option, lease term 30% of economic life, and alternative uses for the lessor. Annual payments in advance have a present value of **$122,500**. Fair value of the equipment is **$150,000**. The lessee also receives a **$5,000** lease incentive at commencement. Which statement is **correct**?

- A) The lease is always a finance lease because a ROU asset and lease liability are recognized.  
- B) If the residual is **unguaranteed**, criterion 4 is **not** met (\(122{,}500 < 90\% \times 150{,}000 = 135{,}000\)), so the lease is **operating** for the lessee; if the lessee instead **guarantees** a residual whose PV brings total PV of lease payments to **$150,000**, then after subtracting the incentive the classification PV can **exceed** 90% of FV and the lease becomes **finance**.  
- C) Lease incentives are ignored entirely when applying the 90% test.  
- D) Guaranteeing residual value never affects classification; it affects only subsequent interest expense presentation.

**Answer:** B.  
Recognition of ROU/liability occurs for **both** operating and finance leases (except short-term election). Criterion 4 compares PV of lease payments **and** residual amounts guaranteed by the lessee to substantially all (90%) of FV; incentives reduce the amount compared for classification in the Demo 17-5 analysis. An unguaranteed residual is **not** a lessee payment for this test. Guaranteeing residual can push the lease over the 90% threshold and flip classification to finance.

---

### Q5 — MC — Presentation and SCF for complex operating lease
**LO:** LO 17-5  
**Concept:** Presentation of complex operating lease expense vs finance lease; SCF classification of cash payments  
**Question:** For a lessee’s **complex operating lease** (with IDC and a lease incentive), which presentation is correct under ASC 842?

- A) Report interest expense on the liability and separate amortization of the ROU asset on the income statement; classify the principal portion of cash payments as a financing outflow.  
- B) Report a **single straight-line lease expense** in income from continuing operations; classify the **full** cash lease payment as an **operating** cash outflow.  
- C) Capitalize IDC as a separate prepaid and expense incentives immediately; no ROU asset is recorded for operating leases.  
- D) Accrete the lease liability with a debit to Interest Expense each period even though the lease is operating.

**Answer:** B.  
Complex operating leases still recognize ROU and liability (adjusted for IDC and incentives), but subsequent measurement produces **one** SL lease expense amount in operations. On the SCF, the entire cash payment is an operating outflow (contrast finance leases, which split interest vs principal). The “interest” in the liability schedule is only a computational input to the ROU reduction plug—not a separate IS line for operating leases.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV, interest, SL expense, ROU plug, BS current/noncurrent)
- [x] Core demo path (Demo 17-5: complex operating with IDC/incentive/prepayment) — not sidebar-only
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Emphasis angle covered: subsequent_measurement_schedule (Q1/Q2 dual schedules)
- [x] Angles: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook Demo 17-5 figures)
