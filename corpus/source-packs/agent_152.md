# Agent 152 — CORE DEMO — LO 17-12

**Chapter:** 17  
**LO title:** Describe the difference in accounting for a sale-leaseback versus a failed sale  
**Critical gap LO:** yes

## Concept list for this pack
- **Initial recognition JE (sale-leaseback):** when leaseback is **operating**, control transfers → **derecognize** asset, recognize **gain/loss** (sales price − carrying amount), and record **ROU asset** and **lease liability** at PV of lease payments
- **Initial recognition JE (failed sale):** when leaseback is **finance**, control does **not** transfer → **no sale**, **no gain/loss**, asset **remains** on books; cash proceeds recorded as a **note (finance) payable**
- **Subsequent measurement schedule (emphasis):** operating leaseback → **lease liability** and **ROU** amort schedules (interest on liability; single lease expense equal to payment pattern); failed sale → **note amortization** (interest + principal) plus continued **depreciation** of the retained asset
- **Period-end adjusting JE:** year-end lease expense / payment entries (sale-leaseback) or interest + principal payment and depreciation (failed sale)
- **Disposal / maturity / settlement JE:** at end of leaseback term, ROU and lease liability go to zero; at end of failed-sale loan term, final payment settles the note
- **Classification / presentation / disclosure:** finance leaseback = failed sale (financing); operating leaseback = true sale-leaseback; presentation of gain, ROU/liability vs note payable and owned PPE
- **Number-variant twin:** same sale-leaseback skill path with all amounts, rates, and terms changed

---

### Q1 — CORE — Sale-leaseback (operating leaseback): sale JE, ROU/liability, full subsequent schedules, year-end and maturity
**LO:** LO 17-12  
**Concept:** Classify leaseback as operating → true sale-leaseback; initial recognition of sale gain and ROU/lease liability; subsequent measurement schedules; period-end JEs; maturity zero-out of ROU and liability; presentation  
**Scenario:**  
**Riverton Logistics Co.** (calendar-year seller-lessee) needs cash but must keep using its distribution building. On **January 1, Year 1**, Riverton sells the building to **Summit Capital Leasing LLC** for **$300,000** cash (fair value) and **immediately leases it back**.

**Building data (immediately before sale):**
| Item | Amount |
|---|---:|
| Original cost | $525,000 |
| Accumulated depreciation | 285,000 |
| Carrying amount | 240,000 |
| Estimated remaining useful life | 16 years |
| Estimated residual value | $0 |

**Leaseback terms:**
- Noncancellable term: **5 years**
- Annual lease payment: **$62,000**, due each **December 31** (ordinary annuity)
- Implicit rate: **6%**, known to Riverton
- No transfer of ownership; no purchase option
- Building reverts to Summit at lease end and has **alternative uses** for the lessor
- Lessee does **not** guarantee residual value; residual is not included in Riverton’s lease payments for measurement

**Required:**  
a. **Classify** the leaseback for Riverton and conclude whether the transfer is a **sale-leaseback** or a **failed sale**. Support with the five lease classification criteria (including PV test).  
b. Prepare Riverton’s **January 1, Year 1 initial recognition JEs**.  
c. Prepare the **5-year subsequent measurement schedules** for the **lease liability** and **right-of-use asset** (columns: beginning balance, interest on liability, lease payment, liability/ROU reduction, ending balance; also show annual lease expense).  
d. Prepare the **December 31, Year 1** period-end JEs.  
e. Prepare the **December 31, Year 5** maturity-period JEs (final year) and confirm ending ROU and lease liability balances.  
f. **Presentation:** How is the Year 1 gain reported? How are the ROU asset and lease liability presented relative to a failed-sale financing?

**Answer key:**  

**a. Classification → operating leaseback → sale-leaseback (control transferred)**

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to lessor at end of 5 years | No |
| 2. Purchase option | None | No |
| 3. Lease term major part of economic life | 5/16 = **31.25%** (not major part; below 75% bright line) | No |
| 4. PV of lease payments substantially all of FV | PV = **$261,167** (below); 90% of FV $300,000 = **$270,000** | No |
| 5. Specialized asset / no alternative use | Building has alternative uses | No |

**PV of lease payments** (ordinary annuity):  
\[
PV = 62{,}000 \times \frac{1-(1.06)^{-5}}{0.06} = 62{,}000 \times 4.212364 = \$261{,}166.55 \approx \$261{,}167
\]

**None** of the finance-lease criteria are met → leaseback is an **operating lease**. Because the leaseback does **not** transfer control back to the seller-lessee in substance, the buyer obtains control → record a **sale** and account for an **operating leaseback** (**sale-leaseback**, not a failed sale).

**b. January 1, Year 1 — initial recognition**

*To record sale of building (derecognize asset; recognize gain)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 300,000 | |
| Accumulated Depreciation—Building | 285,000 | |
| Building | | 525,000 |
| Gain on Sale-Leaseback | | 60,000 |
| *Sell building at FV $300,000; CV $240,000; gain $60,000* | | |

**Check:** Dr 300,000 + 285,000 = 585,000; Cr 525,000 + 60,000 = 585,000. **Balanced.**  
Gain = $300,000 − $240,000 = **$60,000**.

*To record operating leaseback ROU asset and lease liability*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 261,167 | |
| Lease Liability | | 261,167 |
| *PV of 5 payments of $62,000 at 6%* | | |

**Check:** Dr 261,167 = Cr 261,167. **Balanced.**

**c. Subsequent measurement schedules (emphasis)**

Annual **lease expense** (operating lease, level payments, no prepaid/incentives) = cash payment = **$62,000** each year.  
Interest on liability = beginning liability × **6%** (rounded to nearest dollar).  
Liability reduction = payment − interest.  
ROU reduction = lease expense − interest (= same as liability reduction under this payment pattern).

**Lease liability schedule**

| Date / Year | Beg. liability | Interest (6%) | Lease payment | Liability reduction | End. liability |
|---|---:|---:|---:|---:|---:|
| Jan. 1, Y1 | | | | | **261,167** |
| Dec. 31, Y1 | 261,167 | 15,670 | 62,000 | 46,330 | 214,837 |
| Dec. 31, Y2 | 214,837 | 12,890 | 62,000 | 49,110 | 165,727 |
| Dec. 31, Y3 | 165,727 | 9,944 | 62,000 | 52,056 | 113,671 |
| Dec. 31, Y4 | 113,671 | 6,820 | 62,000 | 55,180 | 58,491 |
| Dec. 31, Y5 | 58,491 | 3,509 | 62,000 | 58,491 | **0** |
| **Totals** | | **48,833** | **310,000** | **261,167** | |

**Right-of-use asset schedule**

| Date / Year | Beg. ROU | Lease expense | Interest on liab. | ROU reduction | End. ROU |
|---|---:|---:|---:|---:|---:|
| Jan. 1, Y1 | | | | | **261,167** |
| Dec. 31, Y1 | 261,167 | 62,000 | 15,670 | 46,330 | 214,837 |
| Dec. 31, Y2 | 214,837 | 62,000 | 12,890 | 49,110 | 165,727 |
| Dec. 31, Y3 | 165,727 | 62,000 | 9,944 | 52,056 | 113,671 |
| Dec. 31, Y4 | 113,671 | 62,000 | 6,820 | 55,180 | 58,491 |
| Dec. 31, Y5 | 58,491 | 62,000 | 3,509 | 58,491 | **0** |
| **Totals** | | **310,000** | **48,833** | **261,167** | |

**Schedule checks:** liability and ROU both amortize from $261,167 to **$0**; total liability reductions = initial PV; total lease expense = 5 × $62,000 = $310,000.

**d. December 31, Year 1 — period-end JEs**

*Lease expense (operating pattern)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 62,000 | |
| Lease Liability | | 15,670 |
| Right-of-Use Asset | | 46,330 |
| *Single lease expense; accrete liability interest; reduce ROU* | | |

**Check:** Dr 62,000 = Cr 15,670 + 46,330. **Balanced.**

*Cash payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 62,000 | |
| Cash | | 62,000 |
| *Pay Year 1 lease installment* | | |

**Check:** Dr 62,000 = Cr 62,000. **Balanced.**  
**Net** liability change: +15,670 − 62,000 = **−46,330** → ending liability **$214,837**.

**e. December 31, Year 5 — maturity settlement of leaseback**

Beginning liability / ROU = **$58,491**; interest = round(58,491 × 0.06) = **$3,509**; ROU/liability reduction = **$58,491**.

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 62,000 | |
| Lease Liability | | 3,509 |
| Right-of-Use Asset | | 58,491 |
| *Final-year operating lease expense* | | |

**Check:** Dr 62,000 = Cr 3,509 + 58,491. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 62,000 | |
| Cash | | 62,000 |
| *Final lease payment* | | |

**Check:** Dr 62,000 = Cr 62,000. **Balanced.**  
After these entries: **Lease liability = $0**; **ROU asset = $0**. The leased-back building is no longer on Riverton’s books (sold in Year 1); possession ends under the contract.

**f. Presentation / disclosure**

- **Gain on Sale-Leaseback $60,000** is recognized **immediately** in income at the sale date (control transferred; operating leaseback).  
- **ROU asset** and **lease liability** are reported for the operating leaseback (lease liability split current/noncurrent as applicable).  
- Contrast with failed sale: no gain, PPE remains, and proceeds appear as **debt (note payable)** rather than as a completed sale plus lease.

**Key insight:** If the leaseback is **operating**, treat the transfer as a **sale**: remove the asset, book gain/loss, and account for a normal operating lease (ROU + liability + single lease expense). Subsequent measurement rolls the liability with interest and reduces ROU so both finish at zero at term end.

---

### Q2 — CORE number variant — Sale-leaseback (operating): full path with all numbers changed
**LO:** LO 17-12  
**Concept:** Number-variant twin of successful sale-leaseback — initial sale and ROU/liability JEs; subsequent measurement schedule; period-end JEs; classification confirmation  
**Scenario:**  
**Cedar Peak Manufacturing Inc.** sells specialized but re-deployable packaging equipment to **Prairie Asset Partners** on **January 1, Year 1** for **$140,000** cash (fair value) and leases the equipment back the same day.

**Equipment data:**
| Item | Amount |
|---|---:|
| Original cost | $200,000 |
| Accumulated depreciation | 95,000 |
| Carrying amount | 105,000 |
| Remaining useful life | 10 years |

**Leaseback terms:**
- Term: **3 years**
- Annual payment: **$42,000** each **December 31**
- Implicit rate known to lessee: **5%**
- No ownership transfer; no purchase option; equipment has alternative uses for the lessor at lease end
- No residual value guarantee by Cedar Peak

**Required:**  
a. Show that the leaseback is **operating** and the transfer is a **sale-leaseback** (brief criteria, including PV vs 90% of FV).  
b. January 1, Year 1 **sale JE** and **ROU/lease liability JE**.  
c. **Full 3-year** lease liability and ROU subsequent measurement schedules.  
d. **December 31, Year 1** and **December 31, Year 3** (final) period-end JEs.  
e. State the **total gain** recognized and the **total lease expense** over the 3-year term.

**Answer key:**  

**a. Classification**

| Criterion | Analysis | Met? |
|---|---|---|
| Ownership transfer | Reverts to lessor | No |
| Purchase option | None | No |
| Term / life | 3/10 = **30%** | No |
| PV substantially all of FV | PV **$114,376** vs 90% × $140,000 = **$126,000** | No |
| No alternative use | Has alternative uses | No |

\[
PV = 42{,}000 \times \frac{1-(1.05)^{-3}}{0.05} = 42{,}000 \times 2.723248 = \$114{,}376.42 \approx \$114{,}376
\]

**Operating leaseback** → **sale-leaseback** (control transferred to buyer-lessor).

**b. January 1, Year 1 — initial recognition**

Gain = $140,000 − $105,000 = **$35,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 140,000 | |
| Accumulated Depreciation—Equipment | 95,000 | |
| Equipment | | 200,000 |
| Gain on Sale-Leaseback | | 35,000 |
| *Sale at FV; derecognize equipment* | | |

**Check:** Dr 140,000 + 95,000 = 235,000; Cr 200,000 + 35,000 = 235,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 114,376 | |
| Lease Liability | | 114,376 |
| *PV of 3 × $42,000 at 5%* | | |

**Check:** Dr 114,376 = Cr 114,376. **Balanced.**

**c. Subsequent measurement schedules**

Lease expense each year = **$42,000**.

**Lease liability**

| Year | Beg. liability | Interest (5%) | Payment | Liability reduction | End. liability |
|---|---:|---:|---:|---:|---:|
| 1 | 114,376 | 5,719 | 42,000 | 36,281 | 78,095 |
| 2 | 78,095 | 3,905 | 42,000 | 38,095 | 40,000 |
| 3 | 40,000 | 2,000 | 42,000 | 40,000 | **0** |
| **Totals** | | **11,624** | **126,000** | **114,376** | |

**ROU asset** (same reductions as liability under this pattern)

| Year | Beg. ROU | Lease expense | Interest | ROU reduction | End. ROU |
|---|---:|---:|---:|---:|---:|
| 1 | 114,376 | 42,000 | 5,719 | 36,281 | 78,095 |
| 2 | 78,095 | 42,000 | 3,905 | 38,095 | 40,000 |
| 3 | 40,000 | 42,000 | 2,000 | 40,000 | **0** |
| **Totals** | | **126,000** | **11,624** | **114,376** | |

**Schedule checks:** both balances end at **$0**; total reductions = $114,376.

**d. Period-end JEs**

*December 31, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 42,000 | |
| Lease Liability | | 5,719 |
| Right-of-Use Asset | | 36,281 |

**Check:** Dr 42,000 = Cr 5,719 + 36,281. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,000 | |
| Cash | | 42,000 |

**Check:** Dr 42,000 = Cr 42,000. **Balanced.**

*December 31, Year 3 (maturity)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 42,000 | |
| Lease Liability | | 2,000 |
| Right-of-Use Asset | | 40,000 |

**Check:** Dr 42,000 = Cr 2,000 + 40,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,000 | |
| Cash | | 42,000 |

**Check:** Dr 42,000 = Cr 42,000. **Balanced.**  
Ending ROU and lease liability = **$0**.

**e. Totals**

- **Gain recognized (Year 1 only):** **$35,000**  
- **Total lease expense over 3 years:** 3 × $42,000 = **$126,000**

**Key insight:** Same core path as Q1 with every number changed: operating leaseback → sale + gain + ROU/liability; subsequent schedules drive period-end JEs until both ROU and liability mature to zero.

---

### Q3 — CORE alternate angle — Failed sale (finance leaseback): note payable, continued depreciation, amort schedule, settlement
**LO:** LO 17-12  
**Concept:** Finance leaseback precludes sale (failed sale); initial note payable only; subsequent note amortization schedule and continued depreciation; period-end payment and depreciation JEs; final settlement of note; classification contrast to sale-leaseback  
**Scenario:**  
**Harborcrest Industrial Corp.** “sells” a plant building to **Lakeside Funding Inc.** on **January 1, Year 1** for **$250,000** cash (stated fair value) and simultaneously leases the building back.

**Building data:**
| Item | Amount |
|---|---:|
| Original cost | $400,000 |
| Accumulated depreciation | 220,000 |
| Carrying amount | 180,000 |
| Remaining useful life | **6 years** |
| Residual value | $0 (straight-line depreciation continues if asset retained) |

**Leaseback terms:**
- Term: **5 years** (noncancellable)
- Annual payment: **$65,949.37**, due each **December 31**
- Implicit rate known to Harborcrest: **10%**
- No purchase option; legal title reverts to Lakeside at lease end
- Building would have alternative uses at lease end for the lessor  
- PV of the five lease payments equals **$250,000** (the cash “sales” proceeds / fair value)

**Required:**  
a. **Classify** the leaseback and conclude **sale-leaseback vs failed sale**. Explain the control conclusion.  
b. Prepare the **only** appropriate **January 1, Year 1** journal entry for Harborcrest. Explicitly state what is **not** recorded.  
c. Prepare a **5-year note payable subsequent measurement schedule** (beg. balance, interest, payment, principal, end. balance).  
d. Prepare **December 31, Year 1** period-end JEs (payment allocation + depreciation).  
e. Prepare the **December 31, Year 5** settlement (final payment) JE and the Year 5 depreciation JE.  
f. **Classification / presentation:** Compare balance-sheet presentation of this failed sale after Day 1 to Riverton’s sale-leaseback in Q1.

**Answer key:**  

**a. Classification → finance leaseback → failed sale (no sale)**

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Title reverts to lessor (not automatic transfer to lessee) | No |
| 2. Purchase option | None | No |
| 3. Lease term major part of economic life | 5/6 ≈ **83.3%** ≥ 75% bright line | **Yes** |
| 4. PV substantially all of FV | PV of payments = **$250,000** = 100% of FV (≥ 90%) | **Yes** |
| 5. No alternative use | Alternative uses exist | No |

Because the leaseback is a **finance lease**, Harborcrest has not surrendered control in substance — the arrangement is an **in-substance financing**. Treat as a **failed sale**: **do not** recognize a sale or gain.

**b. January 1, Year 1 — failed sale initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 250,000 | |
| Note Payable | | 250,000 |
| *Record financing proceeds on failed sale-leaseback* | | |

**Check:** Dr 250,000 = Cr 250,000. **Balanced.**

**Not recorded:**
- No removal of Building / Accumulated Depreciation  
- No Gain (or Loss) on sale  
- No ROU asset or Lease Liability for a “new” lease of an asset still controlled  

Carrying amount of building remains **$180,000**. Continue depreciating over remaining **6-year** useful life.

**c. Note payable subsequent measurement schedule (emphasis)**

Interest each year = beginning note balance × **10%** (rounded to cents).  
Principal = payment − interest.  
Payment = **$65,949.37** each December 31 (Year 5 principal clears remaining balance).

| Year | Beg. note | Interest (10%) | Payment | Principal | End. note |
|---|---:|---:|---:|---:|---:|
| 1 | 250,000.00 | 25,000.00 | 65,949.37 | 40,949.37 | 209,050.63 |
| 2 | 209,050.63 | 20,905.06 | 65,949.37 | 45,044.31 | 164,006.32 |
| 3 | 164,006.32 | 16,400.63 | 65,949.37 | 49,548.74 | 114,457.58 |
| 4 | 114,457.58 | 11,445.76 | 65,949.37 | 54,503.61 | 59,953.97 |
| 5 | 59,953.97 | 5,995.40 | 65,949.37 | 59,953.97 | **0.00** |
| **Totals** | | **79,746.85** | **329,746.85** | **250,000.00** | |

**Schedule checks:** total principal = initial note $250,000; ending balance **$0**; total interest = total payments − total principal = $329,746.85 − $250,000.00 = **$79,746.85**.

Annual depreciation (asset retained): $180,000 ÷ 6 = **$30,000** per year.

**d. December 31, Year 1 — period-end JEs**

*Allocate “lease” payment to interest and principal*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 25,000.00 | |
| Note Payable | 40,949.37 | |
| Cash | | 65,949.37 |
| *Failed-sale financing payment Year 1* | | |

**Check:** Dr 25,000.00 + 40,949.37 = 65,949.37 = Cr. **Balanced.**

*Continue depreciating owned building*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 30,000 | |
| Accumulated Depreciation—Building | | 30,000 |
| *SL depreciation on retained building ($180,000 / 6)* | | |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**  
Ending note = **$209,050.63**; book value of building after Year 1 dep = $180,000 − $30,000 = **$150,000**.

**e. December 31, Year 5 — maturity / settlement of note + depreciation**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 5,995.40 | |
| Note Payable | 59,953.97 | |
| Cash | | 65,949.37 |
| *Final payment settles failed-sale note* | | |

**Check:** Dr 5,995.40 + 59,953.97 = 65,949.37 = Cr. **Balanced.**  
Note payable balance after entry: **$0**.

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 30,000 | |
| Accumulated Depreciation—Building | | 30,000 |
| *Year 5 depreciation on building still on books* | | |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**  
(After 5 years of $30,000 dep, remaining book value = $180,000 − $150,000 = **$30,000**, which will be depreciated in Year 6 — the asset’s remaining economic life after the financing term.)

**f. Presentation contrast (failed sale vs sale-leaseback)**

| Item | Q1 Sale-leaseback (operating) | Q3 Failed sale (finance) |
|---|---|---|
| PPE building | **Derecognized** | **Remains** (continue to depreciate) |
| Day-1 income | **Gain $60,000** | **No gain** |
| Liability | **Lease liability** (PV of payments) | **Note payable** (= cash proceeds) |
| Asset side (use rights) | **ROU asset** | No new ROU; owned building stays |
| Subsequent expense | Single **lease expense** | **Interest expense** + **depreciation** |
| Cash proceeds | Sale proceeds (investing) + lease payments (operating for lessee operating lease presentation per SCF rules as applicable) | **Financing** inflow; repayments allocate to interest/principal |

**Key insight:** Finance leaseback = **failed sale**. Cash is a **loan**, the asset never leaves the books, there is **no sale gain**, and subsequent accounting is **debt service + depreciation** — not ROU amortization and single lease expense.

---

### Q4 — MC — Sale-leaseback vs failed sale classification
**LO:** LO 17-12  
**Concept:** Classification — operating leaseback yields sale-leaseback accounting; finance leaseback yields failed-sale (financing) accounting  
**Question:**  
On January 1, **Oakridge Bakeries** transfers a warehouse (carrying amount $420,000; fair value $500,000) to a buyer-lessor for $500,000 cash and leases it back for 12 years. The warehouse’s remaining economic life is 15 years. The PV of leaseback payments equals $500,000. There is no purchase option; title reverts to the lessor; the warehouse has alternative uses. Oakridge knows the 8% implicit rate.

Which statement is **correct**?

- A) Record a sale with $80,000 gain and an operating lease (ROU asset and lease liability).  
- B) Record a failed sale: debit Cash $500,000, credit Note Payable $500,000; keep the warehouse on the books and continue depreciation; do not recognize the $80,000 gain.  
- C) Record a sale with $80,000 gain and a finance lease ROU asset/liability equal to $500,000.  
- D) Record neither a sale nor a liability because possession of the warehouse never changed.

**Answer:** **B.**  
Lease term 12/15 = **80%** (major part of economic life) and PV of payments = **100%** of fair value → leaseback is a **finance lease**. A finance leaseback means control did **not** transfer → **failed sale**. Proceeds are a **loan**; PPE stays; **no gain**.  
A is the operating-leaseback (true sale) model, which fails here.  
C incorrectly combines a sale with finance-lease accounting for the same transfer (inconsistent under the LO 17-12 model).  
D ignores the cash financing that must be recognized.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PVs, interest, principal, depreciation, schedule roll-forwards to zero)
- [x] Core demo path (Demo 17-12 sale-leaseback vs failed sale) — not sidebar-only
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 1)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
