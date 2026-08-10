# Agent 24 — CORE DEMO — LO 17-4

**Chapter:** 17  
**LO title:** Account for complex finance leases for a lessee  
**Critical gap LO:** yes

## Concept list for this pack
- Initial recognition of finance lease liability and right-of-use asset with **initial direct costs** and **lease incentives**
- Lease liability amortization schedule (annuity-due payments; effective interest)
- Period-end adjusting entries: interest on lease liability + ROU amortization
- Guaranteed residual: **100%** in classification PV test vs **only probable amount owed** in liability measurement
- Residual-value guarantee **settlement** at lease end
- Purchase option reasonably certain: include exercise price in liability; amortize ROU over **economic life**; reclass/settle at exercise
- Current vs noncurrent lease liability presentation
- Classification criterion #4 with complex payment components

---

### Q1 — CORE — Finance lease with initial direct costs and lease incentive (initial recognition emphasis)
**LO:** LO 17-4  
**Concept:** Complex finance lease — IDC + lease incentive; measure liability and ROU; initial JEs  
**Scenario:** On **January 1, Year 1** (commencement), **Riverton Packaging Co.** (lessee) enters a **4-year** noncancellable lease for a packaging line. Facts:

1. Economic life of the equipment is **4 years**; asset reverts to the lessor at lease end.  
2. Four annual lease payments of **$42,973.23** are due **January 1** of Year 1 through Year 4 (payments in advance).  
3. Fair value of the equipment at commencement is **$160,000**.  
4. No renewal or purchase option; residual value is **$0** (unguaranteed).  
5. Lessor’s implicit rate is **5%** and is known to Riverton; Riverton’s incremental borrowing rate is also 5%.  
6. Before commencement, Riverton paid **$2,400** of incremental legal fees to execute the lease (initial direct costs).  
7. Before commencement, the lessor paid Riverton a **$3,600** cash lease incentive; Riverton recorded Cash and Lease Incentive Liability.  
8. Riverton’s fiscal year ends **December 31**. Riverton amortizes right-of-use assets straight-line.

**Required:**  
(a) Journal entry for the initial direct cost paid prior to commencement.  
(b) Journal entry for receipt of the lease incentive prior to commencement.  
(c) Classify the lease (apply the five criteria; show the PV of lease payments for criterion 4).  
(d) Compute the **lease liability** and the **right-of-use asset** at commencement.  
(e) Prepare the commencement journal entry that records the ROU asset and lease liability (and clears IDC and incentive balances).  
(f) Prepare the **lease liability amortization schedule** (all four payments).  
(g) Prepare all lessee journal entries for **Year 1** (commencement payment, Dec 31 interest, Dec 31 ROU amortization).  
(h) Show Year 1 income-statement lease-related expenses and the Dec 31 Year 1 balance-sheet amounts for ROU (net) and lease liability (current and noncurrent).

**Answer key:**

**(a) Prior to commencement — initial direct cost**  
```
Dr Initial Direct Cost ...................... 2,400
   Cr Cash ........................................... 2,400
```
(Dr = Cr = 2,400)

**(b) Prior to commencement — lease incentive**  
```
Dr Cash ..................................... 3,600
   Cr Lease Incentive Liability ...................... 3,600
```
(Dr = Cr = 3,600)

**(c) Classification — finance lease**  
At least one criterion is met:

| Criterion | Analysis | Met? |
|---|---|---|
| 1 Ownership transfer | Asset reverts to lessor | No |
| 2 Purchase option | None | No |
| 3 Lease term | 4 years / 4-year life = **100%** ≥ 75% | **Yes** |
| 4 PV of lease payments | PV of 4 payments in advance at 5% = **$160,000** > 90% × $160,000 = $144,000 | **Yes** |
| 5 No alternative use | Not indicated | No |

Excel check (annuity due): `=PV(0.05,4,−42973.23,0,1)` → **$160,000** (rounded).  
IDC and the incentive liability do **not** change the liability PV used in measurement; for criterion 4, fixed payments are considered **net of incentives** when assessing classification, but even after reducing the first payment by $3,600 the PV remains well above 90% of FV, and criterion 3 alone is sufficient.

**(d) Measurement**  
- **Lease liability** = PV of unpaid lease payments at commencement (before the Jan 1 Year 1 payment is applied in the payment entry) = **$160,000**.  
  (Only fixed payments here; no residual probable amount; no PO.)  
- **Right-of-use asset** = lease liability − lease incentive + initial direct costs  
  \(= 160{,}000 - 3{,}600 + 2{,}400 = \mathbf{\$158{,}800}\).

**(e) January 1, Year 1 — record ROU and liability; clear IDC and incentive**  
```
Dr Right-of-Use Asset ..................... 158,800
Dr Lease Incentive Liability ................ 3,600
   Cr Initial Direct Cost ............................ 2,400
   Cr Lease Liability .............................. 160,000
```
(Dr 162,400 = Cr 162,400)

**(f) Lease liability schedule** (amounts to nearest cent; rate 5%)

| Date | Lease payment | Interest (5%) | Principal | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 160,000.00 |
| Jan 1, Y1 | 42,973.23 | 0.00 | 42,973.23 | 117,026.77 |
| Jan 1, Y2 | 42,973.23 | 5,851.34 | 37,121.89 | 79,904.88 |
| Jan 1, Y3 | 42,973.23 | 3,995.24 | 38,977.99 | 40,926.89 |
| Jan 1, Y4 | 42,973.23 | 2,046.34 | 40,926.89 | 0.00 |
| **Totals** | **171,892.92** | **11,892.92** | **160,000.00** | |

Interest checks: \(117{,}026.77 \times 0.05 = 5{,}851.34\); \(79{,}904.88 \times 0.05 = 3{,}995.24\); \(40{,}926.89 \times 0.05 = 2{,}046.34\).

**(g) Year 1 journal entries**  
January 1, Year 1 — first lease payment:  
```
Dr Lease Liability ......................... 42,973.23
   Cr Cash ....................................... 42,973.23
```

December 31, Year 1 — interest (effective interest on $117,026.77):  
```
Dr Interest Expense ......................... 5,851.34
   Cr Lease Liability ............................. 5,851.34
```

December 31, Year 1 — ROU amortization (\(158{,}800 / 4\)):  
```
Dr Amortization Expense .................... 39,700.00
   Cr Right-of-Use Asset ......................... 39,700.00
```

**(h) Year 1 financial statement impact**  
**Income statement (Year 1):**  
- Interest expense — lease liability: **$5,851.34**  
- Amortization expense — ROU: **$39,700.00**  
- Total finance-lease cost: **$45,551.34**

**Balance sheet (Dec 31, Year 1):**  
- ROU asset (net): \(158{,}800 - 39{,}700 = \mathbf{\$119{,}100}\)  
- Total lease liability: \(117{,}026.77 + 5{,}851.34 = \mathbf{\$122{,}878.11}\)  
- **Current** lease liability = next payment **$42,973.23** (accrued interest $5,851.34 + principal reduction on next payment $37,121.89)  
- **Noncurrent** lease liability: \(122{,}878.11 - 42{,}973.23 = \mathbf{\$79{,}904.88}\)

**Key insight:** For a complex finance lease, the **liability** is the PV of lease payments only; the **ROU asset** starts from that liability and is reduced by incentives and increased by initial direct costs. Subsequent measurement splits expense into **interest** (effective interest on the liability) and **straight-line ROU amortization**.

---

### Q2 — CORE number variant — IDC + incentive twin
**LO:** LO 17-4  
**Concept:** Complex finance lease — IDC + incentive (all numbers changed)  
**Scenario:** On **January 1, Year 1**, **Harborline Logistics LLC** leases specialized sorting equipment under a **4-year** noncancellable finance lease. Facts:

1. Economic life **4 years**; equipment reverts to lessor; no PO or residual guarantee.  
2. Annual payments of **$68,978.53** due **January 1** each year for 4 years (in advance).  
3. Fair value at commencement **$250,000**.  
4. Implicit rate known to lessee: **7%**.  
5. Pre-commencement initial direct costs (document preparation / execution legal fees): **$1,800**.  
6. Pre-commencement cash lease incentive from lessor: **$5,000** (recorded as Lease Incentive Liability).  
7. Year-end December 31; straight-line ROU amortization over the lease term.

**Required:**  
(a) Compute lease liability and ROU asset at commencement.  
(b) Commencement JE (record ROU/liability; clear IDC and incentive).  
(c) Full lease liability schedule.  
(d) All Year 1 lessee JEs (payment, interest, amortization).  
(e) Dec 31 Year 1 ROU net and current/noncurrent lease liability.

**Answer key:**

**(a)**  
- Lease liability = PV of 4 payments in advance at 7% = **$250,000**.  
  Check: `=PV(0.07,4,−68978.53,0,1)` → $250,000.  
- ROU = \(250{,}000 - 5{,}000 + 1{,}800 = \mathbf{\$246{,}800}\).

**(b) January 1, Year 1 — commencement**  
```
Dr Right-of-Use Asset ..................... 246,800
Dr Lease Incentive Liability ................ 5,000
   Cr Initial Direct Cost ............................ 1,800
   Cr Lease Liability .............................. 250,000
```
(Dr 251,800 = Cr 251,800)

(Prior entries implied: Dr IDC 1,800 / Cr Cash 1,800; Dr Cash 5,000 / Cr Lease Incentive Liability 5,000.)

**(c) Lease liability schedule (7%)**

| Date | Lease payment | Interest (7%) | Principal | Liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 250,000.00 |
| Jan 1, Y1 | 68,978.53 | 0.00 | 68,978.53 | 181,021.47 |
| Jan 1, Y2 | 68,978.53 | 12,671.50 | 56,307.03 | 124,714.44 |
| Jan 1, Y3 | 68,978.53 | 8,730.01 | 60,248.52 | 64,465.92 |
| Jan 1, Y4 | 68,978.53 | 4,512.61 | 64,465.92 | 0.00 |
| **Totals** | **275,914.12** | **25,914.12** | **250,000.00** | |

Interest checks: \(181{,}021.47 \times 0.07 = 12{,}671.50\); \(124{,}714.44 \times 0.07 = 8{,}730.01\); \(64{,}465.92 \times 0.07 = 4{,}512.61\).

**(d) Year 1 JEs**  
```
Jan 1  Dr Lease Liability ............... 68,978.53
          Cr Cash ............................... 68,978.53

Dec 31 Dr Interest Expense .............. 12,671.50
          Cr Lease Liability .................... 12,671.50

Dec 31 Dr Amortization Expense .......... 61,700.00
          Cr Right-of-Use Asset ................. 61,700.00
```
(\(246{,}800 / 4 = 61{,}700\); each JE balances.)

**(e) Dec 31, Year 1 presentation**  
- ROU net: \(246{,}800 - 61{,}700 = \mathbf{\$185{,}100}\)  
- Total liability: \(181{,}021.47 + 12{,}671.50 = \mathbf{\$193{,}692.97}\)  
- Current liability: **$68,978.53**  
- Noncurrent: \(193{,}692.97 - 68{,}978.53 = \mathbf{\$124{,}714.44}\)

**Key insight:** Same measurement model as Q1 with a new rate, payment, liability, IDC, and incentive — ROU still equals liability − incentive + IDC, and finance-lease expense remains interest + amortization (not a single straight-line lease expense).

---

### Q3 — CORE — Guaranteed residual value (classification vs measurement + settlement)
**LO:** LO 17-4  
**Concept:** Finance lease with residual value guarantee — 100% in class test, probable amount in liability; end-of-term settlement  
**Scenario:** On **January 1, Year 1**, **Northwind Meats Inc.** (lessee) leases a refrigeration system for **3 years**. Facts:

1. Economic life of the system is **3 years**; asset reverts to the lessor.  
2. Three annual payments of **$49,384.11** due **January 1** of Year 1–Year 3 (in advance).  
3. Fair value at commencement: **$150,000**.  
4. No purchase option.  
5. Lessee **guarantees residual value of $12,000** at lease end. Northwind estimates expected residual value at end of term will be **$8,000**, so the amount **probable of being owed** is **$4,000** (\(12{,}000 - 8{,}000\)).  
6. Implicit rate **6%**, known to the lessee.  
7. No initial direct costs or incentives.  
8. Year-end December 31. At lease end, actual residual fair value is **$8,000** as expected.

**Required:**  
(a) Classify the lease; show the PV used for criterion 4 (include **100%** of the residual guarantee).  
(b) Compute the lease liability and ROU asset (include only the **probable** residual payment).  
(c) Prepare the complete lease liability schedule, including the residual payment.  
(d) Year 1 journal entries (commencement, first payment, Dec 31 interest and amortization).  
(e) Dec 31 Year 1 current vs noncurrent lease liability and ROU net.  
(f) Year 3 year-end interest accrual on the residual strip and the journal entry to **settle** the residual guarantee when residual FV is $8,000 as expected.

**Answer key:**

**(a) Classification — finance lease**  

| Criterion | Analysis | Met? |
|---|---|---|
| 1 Ownership transfer | Reverts to lessor | No |
| 2 Purchase option | None | No |
| 3 Lease term | 3/3 = **100%** of economic life | **Yes** |
| 4 PV of lease payments | PV of 3 payments due + **full $12,000** GRV at 6% ≈ **$150,000** > 90% × $150,000 = $135,000 | **Yes** |
| 5 Specialized asset | Not indicated | No |

Classification PV check: `=PV(0.06,3,−49384.11,−12000,1)` → **$150,000** (rounded).  
**Important:** Criterion 4 includes **100%** of the guaranteed residual, not merely the probable shortfall.

**(b) Liability and ROU**  
Liability PV uses only probable residual **$4,000**:  
`=PV(0.06,3,−49384.11,−4000,1)` → **$143,283.05**.  
ROU (no IDC/incentive) = **$143,283.05**.

**(c) Lease liability schedule**

| Date | Payment | Interest (6%) | Principal | Balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 143,283.05 |
| Jan 1, Y1 | 49,384.11 | 0.00 | 49,384.11 | 93,898.94 |
| Jan 1, Y2 | 49,384.11 | 5,633.94 | 43,750.17 | 50,148.77 |
| Jan 1, Y3 | 49,384.11 | 3,008.93 | 46,375.18 | 3,773.59 |
| Dec 31, Y3 / residual | 4,000.00 | 226.41* | 3,773.59 | 0.00 |

\*Final interest plugged by **$0.01** for rounding (\(3{,}773.59 \times 0.06 = 226.4154 \rightarrow\) raw 226.42 would leave $0.01; textbook-style round to clear the liability).

**(d) Year 1 JEs**  
```
Jan 1  Dr Right-of-Use Asset ............ 143,283.05
          Cr Lease Liability .................. 143,283.05

Jan 1  Dr Lease Liability ............... 49,384.11
          Cr Cash ............................. 49,384.11

Dec 31 Dr Interest Expense ............... 5,633.94
          Cr Lease Liability .................... 5,633.94

Dec 31 Dr Amortization Expense .......... 47,761.02
          Cr Right-of-Use Asset ................. 47,761.02
```
ROU amortization: \(143{,}283.05 / 3 = 47{,}761.0166\ldots\); use **$47,761.02** in Years 1–2 and **$47,761.01** in Year 3 (sum = $143,283.05).

**(e) Dec 31, Year 1 presentation**  
- ROU net: \(143{,}283.05 - 47{,}761.02 = \mathbf{\$95{,}522.03}\)  
- Total liability: \(93{,}898.94 + 5{,}633.94 = \mathbf{\$99{,}532.88}\)  
- Current: next payment **$49,384.11**  
- Noncurrent: \(99{,}532.88 - 49{,}384.11 = \mathbf{\$50{,}148.77}\)

**(f) End of lease — residual settlement (expected outcome)**  
After the Jan 1, Year 3 payment, liability balance is $3,773.59. During Year 3, accrue interest on that strip:

```
Dec 31, Y3  Dr Interest Expense ............. 226.41
               Cr Lease Liability ................... 226.41
```
Liability is now **$4,000**. Actual residual FV $8,000 vs guarantee $12,000 → cash shortfall **$4,000** (equals amount already in the liability):

```
Dec 31, Y3  Dr Lease Liability .............. 4,000.00
               Cr Cash .............................. 4,000.00
```
(Dr = Cr = 4,000). ROU is fully amortized to $0 by end of Year 3. No gain/loss because the outcome matched the probable estimate.

*(If actual residual had been only $7,500, cash paid would be $4,500; entry: Dr Lease Liability 4,000, Dr Loss on residual guarantee 500, Cr Cash 4,500.)*

**Key insight:** **Classification** PV includes **100% of the GRV**; **measurement** of the lessee’s liability includes only the **probable amount owed** under the guarantee. Settlement zeros the remaining liability strip when residual is as expected.

---

### Q4 — CORE — Purchase option reasonably certain (amortize over useful life + exercise)
**LO:** LO 17-4  
**Concept:** Finance lease with purchase option expected to be exercised; ROU over economic life; maturity settlement/reclass  
**Scenario:** On **January 1, Year 1**, **Copperfield Dental Group** leases a 3-D imaging unit:

1. Lease term **4 years**; payments **$58,935.76** each **January 1**, Year 1–Year 4 (in advance).  
2. Fair value at commencement **$240,000**.  
3. Economic life of the unit is **6 years** (straight-line; no salvage for lessee cost allocation).  
4. Lease includes a **$25,000** purchase option at the end of Year 4 that Copperfield is **reasonably certain** to exercise.  
5. No residual value guarantee (ignored when PO exercise is reasonably certain).  
6. Implicit rate **5%**, known to lessee.  
7. No IDC or incentives.  
8. Fiscal year-end December 31.

**Required:**  
(a) Why is this a finance lease? What cash flows enter the lease liability?  
(b) Compute lease liability / ROU at commencement.  
(c) Lease liability schedule including the purchase-option payment.  
(d) Over what period is the ROU amortized, and what is annual amortization?  
(e) Year 1 adjusting entries (interest + amortization).  
(f) At **December 31, Year 4**, after accruing final interest: entries to **pay the purchase option** and to **reclassify** the remaining ROU carrying amount to Equipment.

**Answer key:**

**(a)** Finance lease because criterion **2** is met (PO reasonably certain to be exercised). Also, PV of lease payments including the $25,000 exercise price equals substantially all of FV (criterion 4).  
Lease payments in the liability: four fixed payments of $58,935.76 **plus** the $25,000 purchase option. Residual guarantees are **not** layered on when exercise of the PO is reasonably certain.

**(b)**  
Lease liability = ROU = `=PV(0.05,4,−58935.76,−25000,1)` → **$240,000**.

**(c) Schedule (5%)**

| Date | Payment | Interest (5%) | Principal | Balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (initial) | | | | 240,000.00 |
| Jan 1, Y1 | 58,935.76 | 0.00 | 58,935.76 | 181,064.24 |
| Jan 1, Y2 | 58,935.76 | 9,053.21 | 49,882.55 | 131,181.69 |
| Jan 1, Y3 | 58,935.76 | 6,559.08 | 52,376.68 | 78,805.01 |
| Jan 1, Y4 | 58,935.76 | 3,940.25 | 54,995.51 | 23,809.50 |
| Dec 31, Y4 (exercise PO) | 25,000.00 | 1,190.50* | 23,809.50 | 0.00 |

\*Interest on $23,809.50 for Year 4: \(23{,}809.50 \times 0.05 = 1{,}190.475 \rightarrow\) **$1,190.50** (rounded to clear liability when combined with $25,000 payment).

**(d) ROU amortization period**  
Because ownership will transfer via the reasonably certain PO, amortize ROU over the **economic life (6 years)**, not the 4-year lease term:  
\(240{,}000 / 6 = \mathbf{\$40{,}000}\) per year.

**(e) Year 1 adjusting entries**  
```
Dec 31  Dr Interest Expense ............... 9,053.21
           Cr Lease Liability ..................... 9,053.21

Dec 31  Dr Amortization Expense .......... 40,000.00
           Cr Right-of-Use Asset .................. 40,000.00
```

**(f) December 31, Year 4 — exercise and reclass**  
Accrue final interest (if not already recorded):  
```
Dr Interest Expense ......................... 1,190.50
   Cr Lease Liability ............................. 1,190.50
```
Pay purchase option:  
```
Dr Lease Liability ......................... 25,000.00
   Cr Cash ....................................... 25,000.00
```
ROU carrying amount after 4 years of $40,000 amortization:  
\(240{,}000 - 4 \times 40{,}000 = \mathbf{\$80{,}000}\).  
Reclassify to owned equipment:  
```
Dr Equipment ............................... 80,000.00
   Cr Right-of-Use Asset ......................... 80,000.00
```
Thereafter, depreciate the $80,000 equipment over the **remaining 2-year** life ($40,000 per year), consistent with the original economic-life pattern.

**Key insight:** A reasonably certain purchase option is a **lease payment** for both classification and liability measurement; the ROU is amortized over **useful life**, and at exercise the remaining ROU becomes **Equipment** while cash settles the liability strip equal to the option price (plus final interest).

---

### Q5 — MC — Residual guarantee: classification vs liability measurement
**LO:** LO 17-4  
**Concept:** Lessee residual value guarantee — amounts in classification PV vs lease liability  
**Question:** At lease commencement, a lessee’s contract guarantees a residual value of **$20,000**. The lessee expects the asset’s residual fair value at the end of the lease to be **$17,500**. For a lessee, which statement is correct under ASC 842?

- A) Include **$20,000** in both the classification PV test and the initial lease liability.  
- B) Include **$20,000** in the classification PV test, but include only **$2,500** (the amount probable of being owed) when measuring the lease liability.  
- C) Include only **$2,500** in both the classification PV test and the lease liability.  
- D) Exclude residual guarantees entirely from lessee classification and measurement; only lessors include them.

**Answer:** **B.** For criterion 4 (PV of lease payments), the lessee includes **100% of the residual value guarantee**. For **measurement** of the lease liability (and ROU before other adjustments), the lessee includes only amounts **probable of being owed** under the guarantee — here \(20{,}000 - 17{,}500 = 2{,}500\). Unguaranteed residual is excluded from the lessee’s payments entirely.

---

### Q6 — MC — ROU amortization period with purchase option
**LO:** LO 17-4  
**Concept:** Finance lease ROU amortization — lease term vs useful life when PO is reasonably certain  
**Question:** A lessee classifies a lease as a finance lease solely because it is reasonably certain to exercise a purchase option at the end of a **5-year** lease term. The underlying asset’s remaining economic life is **8 years**. There are no impairment indicators. Over which period should the lessee amortize the right-of-use asset?

- A) 5 years (the lease term only).  
- B) 8 years (the useful life of the underlying asset).  
- C) 3 years (useful life minus lease term).  
- D) Do not amortize ROU; reclassify immediately to PPE at commencement.

**Answer:** **B.** If the lease transfers ownership or the lessee is reasonably certain to exercise a purchase option, the ROU asset is amortized to the end of the **useful life** of the underlying asset, not merely over the contractual lease term. (Initial direct costs, if any, are still amortized over the **lease term** so their balance is zero by exercise date.)

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV annuity-due, effective interest, ROU = liab − incentive + IDC)
- [x] Core demo path (Demo 17-4A/B/C style) — not Expanding Your Knowledge sidebars
- [x] LO + Concept on every item
- [x] MC = 2 (classification / method only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook $100,000 / $34,972.24 demo figures)
