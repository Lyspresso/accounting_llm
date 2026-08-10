# Agent 283 — CORE DEMO — LO 17-12

**Chapter:** 17  
**LO title:** Describe the difference in accounting for a sale-leaseback versus a failed sale  
**Critical gap LO:** yes  
**Emphasis:** period_end_adjusting_JE

## Concept list for this pack
- **Control test:** sale-leaseback is recognized only if the buyer-lessor obtains control; leaseback classified as **operating** → sale; leaseback classified as **finance** → **failed sale** (financing)
- **Recognized sale-leaseback (seller-lessee):** derecognize asset at carrying amount, record cash at fair value, recognize **gain/loss**, then record **ROU asset and lease liability** for the operating leaseback
- **Failed sale (seller-lessee):** do **not** derecognize the asset; record cash proceeds as a **note/finance liability**; continue **depreciation** over remaining useful life; allocate payments to **interest** and **principal**
- **Initial recognition JE:** sale + operating lease capitalization vs loan only
- **Subsequent measurement / schedules:** operating lease liability & ROU roll-forward vs note amortization table
- **Period-end adjusting JE (emphasis):** Dec 31 lease expense / interest-and-ROU reduction (and cash payment if ordinary annuity); failed-sale interest/principal split + depreciation; annuity-due year-end accrual with no cash
- **Disposal / maturity / settlement:** end-of-term ROU and lease liability to zero; final note principal payment on failed sale
- **Classification / presentation / disclosure:** operating lease liabilities (current/noncurrent) and gain on sale vs note payable and PPE remaining on BS

---

### Q1 — CORE — Sale-leaseback vs failed sale: classification, initial JEs, schedules, period-end JEs, presentation, maturity
**LO:** LO 17-12  
**Concept:** Contrast recognized sale-leaseback (operating leaseback) with failed sale (finance leaseback): control/classification, initial recognition, liability schedules, **period-end adjusting JEs**, BS presentation, and end-of-term settlement  
**Scenario:**  
**Cascade Forge Co.** (calendar-year) owns a warehouse used in operations. On **January 1, Year 1**, Cascade negotiates a sale-leaseback with **Northline Capital LLC**.

| Item | Amount / term |
|---|---|
| Cash selling price (= fair value) | $240,000 |
| Warehouse cost | $500,000 |
| Accumulated depreciation at sale | $320,000 |
| Carrying amount | $180,000 |
| Remaining useful life | 20 years (straight-line, no salvage) |
| Lessee’s known implicit rate | 7% |
| Residual value estimate (not guaranteed by Cascade) | immaterial for lessee PV test |
| Title / purchase option | none; asset reverts to Northline |
| Alternative use at lease end | yes |

**Case A — Recognized sale-leaseback:** lease term **6 years**; annual lease payments **$42,000** due each **December 31** (ordinary annuity), first payment Dec 31, Year 1.

**Case B — Failed sale (same asset and price; only lease terms change):** lease term **16 years**; annual payments **$25,405.84** due each **December 31** (payment sized so PV of payments ≈ fair value $240,000 at 7%).

Round present values and schedule amounts to the **nearest dollar** for Case A (final period plugs residual). Keep **cents** for Case B note amortization as shown.

**Required:**  
a. For **each** case, determine lease classification for Cascade and whether the transfer is a **sale-leaseback** or a **failed sale**. Support with the five classification criteria (ownership transfer, purchase option, term/economic life, PV of payments vs 90% of FV, no alternative use).  
b. Prepare Cascade’s **January 1, Year 1 initial recognition JEs** for Case A and Case B.  
c. Prepare the **lease liability / ROU schedule** for Case A (all 6 years) and the **note payable amortization schedule** for Case B for **Years 1–3** (show formula for later years).  
d. **(Emphasis)** Prepare **December 31, Year 1 period-end JEs** for Case A and Case B.  
e. Prepare a **December 31, Year 1 balance sheet excerpt** for each case (relevant PPE, lease/note liabilities current vs noncurrent, and note any gain recognized in Year 1).  
f. **(Settlement)** For Case A only, prepare the **December 31, Year 6** entries that settle the lease (final payment and expense allocation). Briefly state how Case B is settled at the end of Year 16.

**Answer key:**  

**Setup — carrying amount and gain**  
Carrying amount \(= 500{,}000 - 320{,}000 = \mathbf{\$180{,}000}\).  
Potential gain if sale recognized \(= 240{,}000 - 180{,}000 = \mathbf{\$60{,}000}\).  
90% of fair value \(= 0.90 \times 240{,}000 = \mathbf{\$216{,}000}\).

**a. Classification**

| Criterion | Case A (6-year) | Met? | Case B (16-year) | Met? |
|---|---|:---:|---|:---:|
| 1. Ownership transfer to lessee | Reverts to lessor | No | Reverts to lessor | No |
| 2. Purchase option | None | No | None | No |
| 3. Lease term ≥ major part of economic life (~75%) | \(6/20 = 30\%\) | No | \(16/20 = 80\%\) | **Yes** |
| 4. PV of payments ≥ substantially all of FV (~90%) | See below | No | See below | **Yes** |
| 5. No alternative use | Alternative uses exist | No | Alternative uses exist | No |

**Case A — PV of lease payments (ordinary annuity):**  
\[
\mathrm{PV} = 42{,}000 \times \frac{1-(1.07)^{-6}}{0.07} = \mathbf{\$200{,}195}
\]  
\(200{,}195 < 216{,}000\) → Criterion 4 not met.  
**None of the criteria met → operating leaseback → control transferred to buyer-lessor → recognized sale-leaseback.**

**Case B — PV of lease payments:**  
\[
\mathrm{PV} = 25{,}405.84 \times \frac{1-(1.07)^{-16}}{0.07} \approx \mathbf{\$240{,}000}
\]  
\(240{,}000 > 216{,}000\) → Criterion 4 met; Criterion 3 also met.  
**Finance leaseback → control not transferred → failed sale (accounted for as a loan).**

**b. January 1, Year 1 — Initial recognition**

**Case A — Recognized sale-leaseback**

*Record sale of warehouse*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 240,000 | |
| Accumulated Depreciation—Warehouse | 320,000 | |
| Warehouse | | 500,000 |
| Gain on Sale-Leaseback | | 60,000 |
| *Derecognize warehouse; recognize gain (control transferred)* | | |

**Check:** Dr \(240{,}000 + 320{,}000 = 560{,}000\) = Cr \(500{,}000 + 60{,}000\). **Balanced.**

*Record operating leaseback (ROU and liability at PV of lease payments)*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 200,195 | |
| Lease Liability | | 200,195 |
| *Capitalize operating leaseback at PV of payments* | | |

**Check:** Dr 200,195 = Cr 200,195. **Balanced.**

**Case B — Failed sale**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 240,000 | |
| Note Payable | | 240,000 |
| *Proceeds recorded as financing; warehouse remains on books* | | |

**Check:** Dr 240,000 = Cr 240,000. **Balanced.**  
**No** gain, **no** asset derecognition, **no** ROU asset.

**c. Schedules**

**Case A — Lease liability and ROU asset (operating; payment Dec 31)**  
Interest \(=\) beginning balance \(\times 7\%\) (rounded). Liability/ROU reduction \(=\) payment \(-\) interest. Year 6 plugs residual.

| Date | Payment | Interest (7%) | Liab / ROU reduction | Lease liability (end) | ROU asset (end) |
|---|---:|---:|---:|---:|---:|
| Jan 1, Y1 | — | — | — | 200,195 | 200,195 |
| Dec 31, Y1 | 42,000 | 14,014 | 27,986 | 172,209 | 172,209 |
| Dec 31, Y2 | 42,000 | 12,055 | 29,945 | 142,264 | 142,264 |
| Dec 31, Y3 | 42,000 | 9,958 | 32,042 | 110,222 | 110,222 |
| Dec 31, Y4 | 42,000 | 7,716 | 34,284 | 75,938 | 75,938 |
| Dec 31, Y5 | 42,000 | 5,316 | 36,684 | 39,254 | 39,254 |
| Dec 31, Y6 | 42,000 | 2,746 | 39,254 | 0 | 0 |
| **Totals** | **252,000** | **51,805** | **200,195** | | |

**Roll-forward checks:** sum of reductions \(= 200{,}195\) initial PV; both ROU and liability end at zero.

**Case B — Note payable amortization (partial)**  
Interest \(=\) beginning note balance \(\times 7\%\). Principal \(=\) payment \(-\) interest.

| Date | Payment | Interest (7%) | Principal | Note balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | — | — | — | 240,000.00 |
| Dec 31, Y1 | 25,405.84 | 16,800.00 | 8,605.84 | 231,394.16 |
| Dec 31, Y2 | 25,405.84 | 16,197.59 | 9,208.25 | 222,185.91 |
| Dec 31, Y3 | 25,405.84 | 15,553.01 | 9,852.83 | 212,333.08 |

Years 4–16 continue the same pattern; Year 16 payment plugs residual principal so the note reaches zero (final cash outlay ≈ $25,405.69 with residual interest).

**d. Period-end adjusting / year-end JEs — December 31, Year 1 (emphasis)**

**Case A — Operating leaseback (two entries, Hanlon Demo 17-12 style)**

*Lease expense allocation (interest accretion + ROU reduction)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 42,000 | |
| Lease Liability | | 14,014 |
| Right-of-Use Asset | | 27,986 |
| *Recognize single lease expense; accrete liability; reduce ROU* | | |

**Check:** Dr 42,000 = Cr \(14{,}014 + 27{,}986\). **Balanced.**

*Cash lease payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,000 | |
| Cash | | 42,000 |
| *Pay Year 1 lease installment* | | |

**Check:** Dr 42,000 = Cr 42,000. **Balanced.**  
**Net** liability change: \(+14{,}014 - 42{,}000 = -27{,}986\) → balance **$172,209**.

**Case B — Failed sale (financing + continued depreciation)**

*Loan payment (interest + principal)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 16,800.00 | |
| Note Payable | 8,605.84 | |
| Cash | | 25,405.84 |
| *Allocate payment: 7% interest on $240,000; remainder principal* | | |

**Check:** Dr \(16{,}800.00 + 8{,}605.84 = 25{,}405.84\) = Cr 25,405.84. **Balanced.**

*Continue depreciating warehouse (still owned for accounting)*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 9,000 | |
| Accumulated Depreciation—Warehouse | | 9,000 |
| *\(180{,}000 / 20 = 9{,}000\)* | | |

**Check:** Dr 9,000 = Cr 9,000. **Balanced.**

**e. December 31, Year 1 presentation**

**Case A (sale-leaseback)**  
- Warehouse: **derecognized** (not on BS).  
- Year 1 income includes **Gain on sale-leaseback $60,000** and **Lease expense $42,000**.  
- ROU asset: **$172,209**.  
- Lease liability: **$172,209**, of which **current** = next year’s principal reduction **$29,945**; **noncurrent** = \(172{,}209 - 29{,}945 = \mathbf{\$142{,}264}\).

**Case B (failed sale)**  
- Warehouse remains: cost $500,000; accum. dep. \(320{,}000 + 9{,}000 = 329{,}000\); **carrying amount $171,000**.  
- **No** sale gain. Year 1 expenses: interest **$16,800** + depreciation **$9,000**.  
- Note payable: **$231,394.16**, of which **current** ≈ next principal **$9,208.25**; **noncurrent** ≈ **$222,185.91**.

**f. Settlement**

**Case A — December 31, Year 6 (final period)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 42,000 | |
| Lease Liability | | 2,746 |
| Right-of-Use Asset | | 39,254 |
| *Final operating lease expense allocation* | | |

**Check:** Dr 42,000 = Cr \(2{,}746 + 39{,}254\). **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 42,000 | |
| Cash | | 42,000 |
| *Final lease payment; liability and ROU now zero* | | |

**Check:** Dr 42,000 = Cr 42,000. **Balanced.**

**Case B — end of Year 16:** final payment clears remaining note principal and residual interest; warehouse continues to be depreciated only until fully depreciated over its 20-year remaining life at sale (independent of the 16-year financing term if lives differ—here dep. ends after 20 years from Jan 1, Y1).

**Key insight:** If the leaseback is **operating**, the seller records a real **sale** (gain/loss, asset off books) plus an **operating lease**. If the leaseback is **finance**, the “sale” **fails**—cash is a **loan**, the asset **stays**, and payments are **debt service** plus continued **depreciation**.

---

### Q2 — CORE number variant — Sale-leaseback vs failed sale (all numbers changed)
**LO:** LO 17-12  
**Concept:** Number-variant twin of Q1: recompute classification, gain, PV, initial JEs, first-year schedules, and **period-end JEs** for sale-leaseback vs failed sale  
**Scenario:**  
**Northwind Storage Inc.** (calendar-year) sells a distribution building to **Palisade Equipment Finance** on **January 1, Year 1** and leases it back.

| Item | Amount / term |
|---|---|
| Cash selling price (= fair value) | $165,000 |
| Building cost | $380,000 |
| Accumulated depreciation at sale | $245,000 |
| Carrying amount | $135,000 |
| Remaining useful life | 15 years (SL, no salvage) |
| Implicit rate known to lessee | 6% |
| Title transfer / purchase option | none; reverts to lessor |
| Alternative use | yes |

**Case A — Sale-leaseback:** term **5 years**; annual payments **$35,000** each **December 31**.  
**Case B — Failed sale:** term **12 years** (\(12/15 = 80\%\)); annual payments **$19,680.71** each **December 31** (PV ≈ $165,000 at 6%).

Round Case A PV and schedule amounts to the nearest dollar (final-year plug).

**Required:**  
a. Classify each case (sale-leaseback vs failed sale) with key quantitative tests.  
b. January 1, Year 1 JEs for both cases.  
c. Case A full 5-year liability/ROU schedule; Case B note schedule for Years 1–2.  
d. **(Emphasis)** December 31, Year 1 period-end JEs for both cases.  
e. Compute Year 1 **gain (if any)**, **lease or interest expense**, and **depreciation (if any)** for each case.

**Answer key:**  

**Setup**  
Carrying amount \(= 380{,}000 - 245{,}000 = \mathbf{\$135{,}000}\).  
Gain if sale recognized \(= 165{,}000 - 135{,}000 = \mathbf{\$30{,}000}\).  
90% of FV \(= 0.90 \times 165{,}000 = \mathbf{\$148{,}500}\).

**a. Classification**  
**Case A:** term \(5/15 \approx 33\% < 75\%\).  
\[
\mathrm{PV} = 35{,}000 \times \frac{1-(1.06)^{-5}}{0.06} = \mathbf{\$147{,}433} < 148{,}500
\]  
No title, no PO, alternative use → **operating → sale-leaseback**.

**Case B:** term \(12/15 = 80\% \geq 75\%\) (Criterion 3). PV of payments ≈ **$165,000** > $148,500 (Criterion 4) → **finance → failed sale**.

**b. January 1, Year 1**

**Case A — Sale**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 165,000 | |
| Accumulated Depreciation—Building | 245,000 | |
| Building | | 380,000 |
| Gain on Sale-Leaseback | | 30,000 |

**Check:** Dr \(165{,}000 + 245{,}000 = 410{,}000\) = Cr \(380{,}000 + 30{,}000\). **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 147,433 | |
| Lease Liability | | 147,433 |

**Check:** Dr 147,433 = Cr 147,433. **Balanced.**

**Case B — Failed sale**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 165,000 | |
| Note Payable | | 165,000 |

**Check:** Dr 165,000 = Cr 165,000. **Balanced.** Building remains at carrying amount $135,000.

**c. Schedules**

**Case A — Liability / ROU**

| Date | Payment | Interest (6%) | Reduction | Balance (liab = ROU) |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | — | — | — | 147,433 |
| Dec 31, Y1 | 35,000 | 8,846 | 26,154 | 121,279 |
| Dec 31, Y2 | 35,000 | 7,277 | 27,723 | 93,556 |
| Dec 31, Y3 | 35,000 | 5,613 | 29,387 | 64,169 |
| Dec 31, Y4 | 35,000 | 3,850 | 31,150 | 33,019 |
| Dec 31, Y5 | 35,000 | 1,981 | 33,019 | 0 |
| **Totals** | **175,000** | **27,567** | **147,433** | |

**Case B — Note (partial)**

| Date | Payment | Interest (6%) | Principal | Note balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 | — | — | — | 165,000.00 |
| Dec 31, Y1 | 19,680.71 | 9,900.00 | 9,780.71 | 155,219.29 |
| Dec 31, Y2 | 19,680.71 | 9,313.16 | 10,367.55 | 144,851.74 |

**d. December 31, Year 1 period-end JEs (emphasis)**

**Case A**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 35,000 | |
| Lease Liability | | 8,846 |
| Right-of-Use Asset | | 26,154 |

**Check:** Dr 35,000 = Cr \(8{,}846 + 26{,}154\). **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Cash | | 35,000 |

**Check:** Dr 35,000 = Cr 35,000. **Balanced.**

**Case B**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 9,900.00 | |
| Note Payable | 9,780.71 | |
| Cash | | 19,680.71 |

**Check:** Dr \(9{,}900.00 + 9{,}780.71 = 19{,}680.71\). **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 9,000 | |
| Accumulated Depreciation—Building | | 9,000 |
| *\(135{,}000 / 15 = 9{,}000\)* | | |

**Check:** Dr 9,000 = Cr 9,000. **Balanced.**

**e. Year 1 P&L contrast**

| Item | Case A (sale-leaseback) | Case B (failed sale) |
|---|---:|---:|
| Gain on sale | 30,000 | 0 |
| Lease expense | 35,000 | 0 |
| Interest expense | 0 (embedded in lease exp model) | 9,900 |
| Depreciation expense | 0 (asset sold) | 9,000 |
| Asset on BS at year-end? | ROU 121,279 (no building) | Building CA 126,000 |

**Key insight:** Same economic “sell and still use the building,” but finance-lease classification flips the accounting from **sale + operating lease** to **loan + continued ownership accounting**.

---

### Q3 — CORE alternate angle — Annuity-due sale-leaseback period-end adjusting JEs (emphasis) and end-of-term settlement
**LO:** LO 17-12  
**Concept:** Recognized sale-leaseback with **payments in advance**: initial sale + ROU/liability + first payment; pure **period-end adjusting JE** (no cash) each December 31; settlement when ROU/liability reach zero  
**Scenario:**  
**Ironclad Components Corp.** (calendar-year) sells specialty manufacturing space to **Harbor Trust Leasing** on **January 1, Year 1** and immediately leases it back under an **operating** leaseback (recognized sale-leaseback).

| Item | Amount / term |
|---|---|
| Cash selling price (= fair value) | $320,000 |
| Building cost | $700,000 |
| Accumulated depreciation | $430,000 |
| Carrying amount | $270,000 |
| Remaining useful life | 25 years |
| Lease term | 8 years (\(8/25 = 32\%\)) |
| Annual lease payment (due **January 1**, annuity due) | $45,000 |
| Implicit rate known to lessee | 8% |
| Title / PO / guaranteed residual | none |
| Alternative use at end | yes |

First payment is made **at commencement (January 1, Year 1)**. Subsequent payments each January 1. Ironclad’s year-end is **December 31**.

**Required:**  
a. Show that the leaseback is **operating** and the transfer is a **recognized sale-leaseback** (include PV test).  
b. Compute the **commencement PV** of the annuity-due lease payments (ROU and lease liability before the first payment).  
c. Prepare **January 1, Year 1** JEs: (1) sale, (2) ROU/liability, (3) first lease payment.  
d. **(Emphasis)** Prepare the **December 31, Year 1 period-end adjusting JE** only (no cash). Explain why this entry differs from Q1’s year-end package.  
e. Provide the **Years 1–3** rows of the ROU/liability roll-forward (after each Dec 31 adjusting entry).  
f. **(Settlement)** Prepare the **January 1, Year 8** final payment and the **December 31, Year 8** final adjusting entry that clear ROU and liability.  
g. Briefly contrast what would change if the lease term were **20 years** (80% of life) with payments re-set so PV ≈ $320,000 (failed sale).

**Answer key:**  

**a. Classification — operating → sale-leaseback**  
- Term \(32\% < 75\%\).  
- No ownership transfer, no PO, alternative use exists.  
- PV (part b) \(= \mathbf{\$279{,}287} < 90\% \times 320{,}000 = \mathbf{\$288{,}000}\).  
→ **Operating leaseback → recognized sale.**

**b. PV of annuity-due payments**  
Ordinary factor for 8 periods at 8%, then × \((1.08)\), or equivalently \(45{,}000 + \mathrm{PV}\) of 7 ordinary payments:  
\[
\mathrm{PV}_{\mathrm{due}} = 45{,}000 \times \frac{1-(1.08)^{-8}}{0.08} \times 1.08 = \mathbf{\$279{,}287}
\]  
(rounded to nearest dollar).

**c. January 1, Year 1**

*Sale*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 320,000 | |
| Accumulated Depreciation—Building | 430,000 | |
| Building | | 700,000 |
| Gain on Sale-Leaseback | | 50,000 |
| *Gain \(= 320{,}000 - 270{,}000 = 50{,}000\)* | | |

**Check:** Dr \(320{,}000 + 430{,}000 = 750{,}000\) = Cr \(700{,}000 + 50{,}000\). **Balanced.**

*ROU and lease liability at full annuity-due PV*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 279,287 | |
| Lease Liability | | 279,287 |

**Check:** Dr 279,287 = Cr 279,287. **Balanced.**

*First payment in advance*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 45,000 | |
| Cash | | 45,000 |
| *Commencement payment reduces liability immediately* | | |

**Check:** Dr 45,000 = Cr 45,000. **Balanced.**  
Liability after payment: \(279{,}287 - 45{,}000 = \mathbf{\$234{,}287}\). ROU remains **$279,287** until year-end adjusting.

**d. December 31, Year 1 — period-end adjusting JE only (emphasis)**  
Interest on liability after the Jan 1 payment: \(\mathrm{round}(234{,}287 \times 0.08) = \mathbf{\$18{,}743}\).  
ROU reduction \(= 45{,}000 - 18{,}743 = \mathbf{\$26{,}257}\).  
Lease expense (operating, constant payments) \(= \mathbf{\$45{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 45,000 | |
| Lease Liability | | 18,743 |
| Right-of-Use Asset | | 26,257 |
| *Year-end adjusting: accrete liability; amortize ROU; no cash* | | |

**Check:** Dr 45,000 = Cr \(18{,}743 + 26{,}257\). **Balanced.**  
Ending balances: liability \(234{,}287 + 18{,}743 = \mathbf{\$253{,}030}\); ROU \(279{,}287 - 26{,}257 = \mathbf{\$253{,}030}\).

**Why different from Q1:** In Q1 payments fall on **Dec 31**, so year-end includes **both** the expense allocation **and** the cash payment. Here the cash payment already occurred on **Jan 1**, so Dec 31 is a **pure adjusting entry** (exam trap: do not credit Cash at year-end).

**e. Partial subsequent measurement schedule (balances after each Dec 31 adjusting entry)**

| Year | Jan 1 payment | Dec 31 interest | Dec 31 ROU red. | Lease exp. | Liab end | ROU end |
|---:|---:|---:|---:|---:|---:|---:|
| 0 (commence, before pmt) | — | — | — | — | 279,287 | 279,287 |
| 1 | 45,000 | 18,743 | 26,257 | 45,000 | 253,030 | 253,030 |
| 2 | 45,000 | 16,642 | 28,358 | 45,000 | 224,672 | 224,672 |
| 3 | 45,000 | 14,374 | 30,626 | 45,000 | 194,046 | 194,046 |

(Pattern continues; after Dec 31, Year 7 balances are each **$45,000**.)

**f. Settlement — Year 8**

*January 1, Year 8 — final payment (liability was $45,000 after Dec 31, Y7)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 45,000 | |
| Cash | | 45,000 |

**Check:** Dr 45,000 = Cr 45,000. **Balanced.** Liability → **$0**.

*December 31, Year 8 — final adjusting (clear remaining ROU; interest = 0)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 45,000 | |
| Right-of-Use Asset | | 45,000 |
| *Final ROU reduction; no liability remains to accrete* | | |

**Check:** Dr 45,000 = Cr 45,000. **Balanced.** ROU → **$0**.

**g. Failed-sale contrast (if term were finance)**  
If term/PV tests made the leaseback a **finance** lease, Ironclad would **not** record the sale or gain, would **not** record ROU, would credit **Note Payable $320,000** for cash, would **keep depreciating** the $270,000 carrying amount over 25 years ($10,800/year), and would treat each $ payment as **interest + principal**—including period-end accruals if payment dates and year-end differ.

**Key insight:** Payment timing does not change the sale-vs-failed-sale **classification** test, but it changes which period-end entry is pure **adjusting** vs cash. Annuity-due sale-leasebacks are prime exam material for **period-end adjusting JEs**.

---

### Q4 — MC — Sale-leaseback vs failed sale classification
**LO:** LO 17-12  
**Concept:** Classification of transfer as sale-leaseback vs failed sale based on leaseback type (operating vs finance)  
**Question:**  
On January 1, **Summit Parcel Co.** sells equipment (FV = carrying amount = $90,000) to a finance company and leases it back for its remaining **9-year** economic life. The leaseback has **no** title transfer and **no** purchase option, but the present value of lease payments equals **$90,000** (100% of FV). Summit’s incremental borrowing rate is 5%. How should Summit account for the January 1 transfer?

- A) Recognized sale-leaseback: remove equipment, record gain/loss if any, and capitalize an operating lease ROU asset and liability  
- B) Failed sale: keep equipment on the books, record cash and a finance/note liability, and continue depreciation  
- C) Recognized sale only (no lease accounting) because legal title transferred to the finance company  
- D) Operating lease with no cash entry because the sale and leaseback offset  

**Answer:** **B.**  
PV of payments = 100% of FV and term = 100% of remaining economic life → leaseback is a **finance** lease. Finance leaseback means the buyer-lessor did **not** obtain control for sale accounting → **failed sale**. Summit records a **loan**, retains the asset, and continues depreciation. A would apply only if the leaseback were **operating**. C ignores required lease/financing analysis. D is incorrect: cash is received and either a sale+lease or a loan must be recorded.

---

### Q5 — MC — Period-end accounts in a failed sale vs sale-leaseback
**LO:** LO 17-12  
**Concept:** Identify which period-end accounts appear under failed sale versus recognized sale-leaseback  
**Question:**  
At December 31 of the first year after a January 1 transfer structured as a **failed sale** (finance leaseback, annual payment on Dec 31), which set of year-end entries is appropriate for the seller-lessee?

- A) Debit Lease Expense; credit ROU Asset and Lease Liability; no depreciation on the underlying asset  
- B) Debit Interest Expense and Note Payable; credit Cash; **and** debit Depreciation Expense; credit Accumulated Depreciation  
- C) Debit Cash and Accumulated Depreciation; credit Asset and Gain — repeated each year-end  
- D) Debit ROU Asset; credit Note Payable only (no interest or depreciation)  

**Answer:** **B.**  
Failed sale = **debt service** (interest + principal against the note) **plus continued depreciation** of the asset that was never derecognized. A describes **operating leaseback** period-end allocation after a **recognized sale**. C is the initial sale entry, not annual period-end. D misstates both initial and subsequent measurement.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PVs, 7%/6%/8% interest, principal plugs, dep = CA / life)
- [x] Core demo path (Demo 17-12 sale-leaseback vs failed sale) — not sidebar-only
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
