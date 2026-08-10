# Agent 232 — CORE DEMO — LO 16-11

**Chapter:** 16  
**LO title:** Accounting for Bonds with Stock Warrants  
**Critical gap LO:** no

## Concept list for this pack
- **Nondetachable warrants:** entire proceeds allocated to debt (straight-debt issue); no separate equity for warrants
- **Detachable warrants — incremental method:** when FV of only one security is known, assign known FV to that security; residual proceeds to the other
- **Detachable warrants — proportional method:** when FV of both debt without warrants and warrants are known, allocate package proceeds by relative fair values
- **Initial recognition JE:** Cash (+ Discount) / Bonds Payable, Premium (if any), Paid-In Capital—Stock Warrants (detachable only)
- **Subsequent measurement schedule (emphasis):** amortize the **debt-only** discount or premium over the bond term; equity warrant balance is not amortized
- **Period-end adjusting JE:** interest expense using cash coupon ± discount/premium amortization
- **Exercise of warrants:** Cash + remove PIC—Stock Warrants → Common Stock + PIC in Excess of Par
- **Expiration of warrants:** reclassify remaining PIC—Stock Warrants → PIC in Excess of Par—Common Stock (no P&L)
- **Maturity / settlement JE:** retire Bonds Payable at face for cash after final interest; premium/discount should be fully amortized

---

### Q1 — CORE — Detachable warrants (proportional), debt amort schedule, interest, exercise, expiration, maturity
**LO:** LO 16-11  
**Concept:** Proportional allocation of detachable bond-with-warrants proceeds; subsequent straight-line premium amortization schedule; period-end interest JE; warrant exercise and expiration; bond maturity  
**Scenario:**  
**Northwind Fabricators** (calendar-year company) issues bonds with **detachable** stock purchase warrants on **January 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Face amount | **$200,000** of 6%, 4-year nonconvertible bonds |
| Interest | Payable **annually each December 31** |
| Bond unit | Each **$1,000** bond carries **10** detachable warrants |
| Total warrants | \(200 \times 10 = \mathbf{2{,}000}\) warrants |
| Exercise terms | Each warrant: one share of **$1** par common for **$25** cash |
| Package issue price | **105** (bonds + warrants) → cash proceeds **$210,000** |
| Fair value shortly after issuance | Bonds **without** warrants quoted at **103**; warrants trade at **$2** each |
| Debt amortization | **Straight-line** amortization of premium/discount over **4 years** |

On **March 1, Year 3**, holders exercise **1,600** warrants. The remaining **400** warrants expire unexercised on **January 31, Year 4**. Bonds are held to maturity and settled on **December 31, Year 4** (after the Year-4 interest payment).

**Required:**  
a. Allocate the **$210,000** package proceeds to bonds and warrants using the **proportional method**. Compute the initial bond carrying amount and premium (or discount).  
b. Record the **January 1, Year 1** initial recognition journal entry.  
c. Prepare a complete **subsequent measurement amortization schedule** for Years 1–4 (beginning carrying amount, cash interest, premium amortization, interest expense, ending carrying amount).  
d. Record the **December 31, Year 1** period-end interest journal entry.  
e. Record the **March 1, Year 3** exercise of 1,600 warrants.  
f. Record the **January 31, Year 4** expiration of the remaining 400 warrants.  
g. Record the **December 31, Year 4** maturity (settlement) entry for the bonds (interest already recorded separately).  
h. In one or two sentences, explain why Paid-In Capital—Stock Warrants is **not** amortized over the bond term.

**Answer key:**  

**a. Proportional allocation**

| Component | Fair value | Weight |
|---|---:|---|
| Bonds without warrants (\(200{,}000 \times 1.03\)) | **$206,000** | \(206{,}000 / 210{,}000\) |
| Warrants (\(2{,}000 \times \$2\)) | **$4,000** | \(4{,}000 / 210{,}000\) |
| **Total fair value** | **$210,000** | |

Package proceeds = **$210,000** (same as total FV in this case).

- Allocation to bonds = \(210{,}000 \times 206/210 = \mathbf{\$206{,}000}\)  
- Allocation to warrants = \(210{,}000 \times 4/210 = \mathbf{\$4{,}000}\)  
- Premium on bonds = \(206{,}000 - 200{,}000 = \mathbf{\$6{,}000}\)  
- Initial bond carrying amount = **$206,000**

**b. Initial recognition**

*January 1, Year 1 — Issue bonds with detachable warrants (proportional method)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 210,000 | |
| Bonds Payable | | 200,000 |
| Premium on Bonds Payable | | 6,000 |
| Paid-In Capital—Stock Warrants | | 4,000 |
| *Allocate package proceeds by relative FV; warrants recorded in equity* | | |

**Check:** Dr 210,000 = Cr 200,000 + 6,000 + 4,000. **Balanced.**

**c. Subsequent measurement schedule (emphasis) — straight-line premium amortization**

Annual cash interest = \(200{,}000 \times 6\% = \mathbf{\$12{,}000}\).  
Annual premium amortization = \(6{,}000 / 4 = \mathbf{\$1{,}500}\).  
Annual interest expense = \(12{,}000 - 1{,}500 = \mathbf{\$10{,}500}\).

| Year | Beginning CA | Cash interest | Premium amort. | Interest expense | Ending CA |
|---:|---:|---:|---:|---:|---:|
| 1 | 206,000 | 12,000 | 1,500 | 10,500 | **204,500** |
| 2 | 204,500 | 12,000 | 1,500 | 10,500 | **203,000** |
| 3 | 203,000 | 12,000 | 1,500 | 10,500 | **201,500** |
| 4 | 201,500 | 12,000 | 1,500 | 10,500 | **200,000** |
| **Totals** | | **48,000** | **6,000** | **42,000** | |

**Roll-forward check:** Premium fully amortized \(4 \times 1{,}500 = 6{,}000\); ending CA = face **$200,000**. Equity warrant balance is **outside** this debt schedule.

**d. Period-end adjusting / interest entry — Year 1**

*December 31, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,500 | |
| Premium on Bonds Payable | 1,500 | |
| Cash | | 12,000 |
| *Cash coupon less SL premium amortization* | | |

**Check:** Dr 10,500 + 1,500 = Cr 12,000. **Balanced.**

**e. Exercise of 1,600 warrants**

PIC—Stock Warrants removed = \(4{,}000 \times 1{,}600/2{,}000 = \mathbf{\$3{,}200}\).  
Cash received = \(1{,}600 \times 25 = \mathbf{\$40{,}000}\).  
Common stock (par) = \(1{,}600 \times 1 = \mathbf{\$1{,}600}\).  
PIC in excess of par (plug) = \(40{,}000 + 3{,}200 - 1{,}600 = \mathbf{\$41{,}600}\).

*March 1, Year 3 — Exercise warrants*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 40,000 | |
| Paid-In Capital—Stock Warrants | 3,200 | |
| Common Stock | | 1,600 |
| Paid-In Capital in Excess of Par—Common Stock | | 41,600 |

**Check:** Dr 40,000 + 3,200 = Cr 1,600 + 41,600. **Balanced.**

**f. Expiration of remaining 400 warrants**

PIC—Stock Warrants remaining = \(4{,}000 \times 400/2{,}000 = \mathbf{\$800}\).

*January 31, Year 4 — Expire unexercised warrants*

| Account | Debit | Credit |
|---|---:|---:|
| Paid-In Capital—Stock Warrants | 800 | |
| Paid-In Capital in Excess of Par—Common Stock | | 800 |
| *Reclassify expired warrant equity within equity; no gain or loss* | | |

**Check:** Dr = Cr = 800. **Balanced.**  
**Check:** PIC—Stock Warrants balance after e–f = \(4{,}000 - 3{,}200 - 800 = \mathbf{\$0}\).

**g. Maturity / settlement**

After Year-4 interest and full premium amortization, carrying amount = face **$200,000**.

*December 31, Year 4 — Retire bonds at maturity*

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 200,000 | |
| Cash | | 200,000 |

**Check:** Dr = Cr = 200,000. **Balanced.**

**h. Why warrants equity is not amortized**  
Detachable warrant proceeds are **paid-in capital**, not a valuation adjustment of the debt. Only the amount allocated to the **bonds** (premium or discount) is amortized as part of interest; the warrant equity remains until **exercise** or **expiration**.

**Key insight:** For detachable warrants with both FVs known, use the **proportional method** to split the package price. The **subsequent measurement schedule** applies only to the **debt carrying amount**; equity stays put until exercise/expiration, and maturity simply clears face Bonds Payable once the premium/discount is gone.

---

### Q2 — CORE number variant — Detachable warrants (incremental), discount schedule, interest, full exercise, maturity
**LO:** LO 16-11  
**Concept:** Number-variant twin: incremental allocation when only warrant FV is known; subsequent straight-line **discount** amortization schedule; period-end interest; exercise of all warrants; bond maturity  
**Scenario:**  
**Pinnacle Harbor Marine** (calendar year) issues bonds with **detachable** stock purchase warrants on **January 1, Year 1**.

| Fact | Amount / term |
|---|---|
| Face amount | **$300,000** of 5%, 3-year nonconvertible bonds |
| Interest | Payable **annually each December 31** |
| Bond unit | Each **$1,000** bond carries **15** detachable warrants |
| Total warrants | \(300 \times 15 = \mathbf{4{,}500}\) warrants |
| Exercise terms | Each warrant: one share of **$5** par common for **$18** cash |
| Package issue price | **102** → cash proceeds **$306,000** |
| Fair values | Warrants trade at **$4** each immediately after issuance; **FV of bonds without warrants is not determinable** |
| Debt amortization | **Straight-line** over **3 years** |

On **July 1, Year 2**, all **4,500** warrants are exercised. Bonds are held to maturity and retired for cash on **December 31, Year 3** (after Year-3 interest).

**Required:**  
a. Allocate proceeds using the **incremental method**. Compute discount and initial bond carrying amount.  
b. Record the **January 1, Year 1** issuance entry.  
c. Prepare the **3-year subsequent measurement amortization schedule**.  
d. Record the **December 31, Year 1** interest entry.  
e. Record the **July 1, Year 2** exercise of all warrants.  
f. Record the **December 31, Year 3** bond maturity settlement.  
g. Compute **total interest expense** over the three-year life and reconcile to cash interest + total discount amortized.

**Answer key:**  

**a. Incremental allocation**

| Step | Amount |
|---|---:|
| Selling price of bonds with warrants (\(300{,}000 \times 1.02\)) | **$306,000** |
| Fair value of warrants (\(4{,}500 \times \$4\)) | **18,000** |
| **Allocation to bonds (residual)** | **$288,000** |
| Discount on bonds (\(300{,}000 - 288{,}000\)) | **$12,000** |

Because only the warrant FV is known, the **incremental method** assigns **$18,000** to equity and the **remainder** of package proceeds to debt.

**b. Initial recognition**

*January 1, Year 1 — Issue bonds with detachable warrants (incremental method)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 306,000 | |
| Discount on Bonds Payable | 12,000 | |
| Bonds Payable | | 300,000 |
| Paid-In Capital—Stock Warrants | | 18,000 |

**Check:** Dr 306,000 + 12,000 = Cr 300,000 + 18,000. **Balanced.**

**c. Subsequent measurement schedule (emphasis) — straight-line discount amortization**

Annual cash interest = \(300{,}000 \times 5\% = \mathbf{\$15{,}000}\).  
Annual discount amortization = \(12{,}000 / 3 = \mathbf{\$4{,}000}\).  
Annual interest expense = \(15{,}000 + 4{,}000 = \mathbf{\$19{,}000}\).

| Year | Beginning CA | Cash interest | Discount amort. | Interest expense | Ending CA |
|---:|---:|---:|---:|---:|---:|
| 1 | 288,000 | 15,000 | 4,000 | 19,000 | **292,000** |
| 2 | 292,000 | 15,000 | 4,000 | 19,000 | **296,000** |
| 3 | 296,000 | 15,000 | 4,000 | 19,000 | **300,000** |
| **Totals** | | **45,000** | **12,000** | **57,000** | |

**Roll-forward check:** Discount fully amortized; ending CA = face **$300,000**.

**d. Period-end interest — Year 1**

*December 31, Year 1*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 19,000 | |
| Discount on Bonds Payable | | 4,000 |
| Cash | | 15,000 |

**Check:** Dr 19,000 = Cr 4,000 + 15,000. **Balanced.**

**e. Exercise of all warrants**

Cash = \(4{,}500 \times 18 = \mathbf{\$81{,}000}\).  
PIC—Stock Warrants removed = **$18,000**.  
Common stock (par) = \(4{,}500 \times 5 = \mathbf{\$22{,}500}\).  
PIC in excess of par = \(81{,}000 + 18{,}000 - 22{,}500 = \mathbf{\$76{,}500}\).

*July 1, Year 2 — Exercise all warrants*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 81,000 | |
| Paid-In Capital—Stock Warrants | 18,000 | |
| Common Stock | | 22,500 |
| Paid-In Capital in Excess of Par—Common Stock | | 76,500 |

**Check:** Dr 81,000 + 18,000 = Cr 22,500 + 76,500. **Balanced.**  
**Note:** Exercising warrants does **not** affect Bonds Payable or the remaining discount amortization schedule.

**f. Maturity settlement**

*December 31, Year 3 — Retire bonds at maturity*

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 300,000 | |
| Cash | | 300,000 |

**Check:** Dr = Cr = 300,000. **Balanced.**

**g. Total interest expense reconciliation**

Total interest expense = \(3 \times 19{,}000 = \mathbf{\$57{,}000}\).  
Reconciliation: cash interest \(45{,}000\) + discount amortized \(12{,}000\) = **$57,000**.

**Key insight:** Under the **incremental method**, the known warrant FV is pulled out of package proceeds first, usually creating (or enlarging) a **discount** on the bonds. The **amortization schedule** then measures subsequent interest; warrant exercise is a pure equity exchange that leaves the debt schedule untouched.

---

### Q3 — CORE alternate angle — Nondetachable vs detachable; nondetachable amort schedule; maturity
**LO:** LO 16-11  
**Concept:** Nondetachable warrants treated as straight debt (no equity split); contrast issuance if warrants were detachable (incremental); subsequent premium amortization schedule; period-end interest; maturity settlement  
**Scenario:**  
**Summit Trail Beverages** issues **$150,000** of 7%, **5-year** nonconvertible bonds on **January 1, Year 1**. Interest is payable annually each **December 31**. Each **$1,000** bond carries **10** stock purchase warrants; each warrant allows purchase of one share of **$2** par common for **$30**. The bonds (including warrants) sell at **104** (cash proceeds **$156,000**). No separate market price for the bonds without warrants is available. Management amortizes any premium or discount **straight-line** over 5 years.

**Part A — Warrants are nondetachable** (cannot be traded separately).  
**Part B — Alternative:** Assume instead the warrants are **detachable** and, immediately after issuance, trade at **$3** each (FV of bonds without warrants still unknown).

Bonds in Part A are held to maturity.

**Required:**  
a. **(Part A)** Record the January 1, Year 1 issuance entry for **nondetachable** warrants.  
b. **(Part A)** Prepare the **5-year subsequent measurement amortization schedule** and record the **December 31, Year 1** interest entry.  
c. **(Part A)** Record the **December 31, Year 5** maturity settlement (after final interest).  
d. **(Part B)** Record the issuance entry if the warrants are **detachable** (incremental method).  
e. Explain in 2–3 sentences why accounting differs for nondetachable versus detachable warrants, and compute how much **less** premium is recorded on the bonds under Part B than under Part A.

**Answer key:**  

**a. Nondetachable — initial recognition (entire package to debt)**

Cash proceeds = \(150{,}000 \times 1.04 = \mathbf{\$156{,}000}\).  
Premium = \(156{,}000 - 150{,}000 = \mathbf{\$6{,}000}\).  
No Paid-In Capital—Stock Warrants (no separate market / nondetachable).

*January 1, Year 1 — Nondetachable warrants (straight-debt treatment)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 156,000 | |
| Bonds Payable | | 150,000 |
| Premium on Bonds Payable | | 6,000 |

**Check:** Dr 156,000 = Cr 150,000 + 6,000. **Balanced.**

**b. Subsequent measurement schedule (Part A) and Year-1 interest**

Annual cash interest = \(150{,}000 \times 7\% = \mathbf{\$10{,}500}\).  
Annual premium amortization = \(6{,}000 / 5 = \mathbf{\$1{,}200}\).  
Annual interest expense = \(10{,}500 - 1{,}200 = \mathbf{\$9{,}300}\).

| Year | Beginning CA | Cash interest | Premium amort. | Interest expense | Ending CA |
|---:|---:|---:|---:|---:|---:|
| 1 | 156,000 | 10,500 | 1,200 | 9,300 | **154,800** |
| 2 | 154,800 | 10,500 | 1,200 | 9,300 | **153,600** |
| 3 | 153,600 | 10,500 | 1,200 | 9,300 | **152,400** |
| 4 | 152,400 | 10,500 | 1,200 | 9,300 | **151,200** |
| 5 | 151,200 | 10,500 | 1,200 | 9,300 | **150,000** |
| **Totals** | | **52,500** | **6,000** | **46,500** | |

*December 31, Year 1 — Interest*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 9,300 | |
| Premium on Bonds Payable | 1,200 | |
| Cash | | 10,500 |

**Check:** Dr 9,300 + 1,200 = Cr 10,500. **Balanced.**

**c. Maturity settlement (Part A)**

*December 31, Year 5 — Retire bonds*

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 150,000 | |
| Cash | | 150,000 |

**Check:** Dr = Cr = 150,000. **Balanced.**

**d. Detachable alternative — incremental issuance**

Number of warrants = \(150 \times 10 = \mathbf{1{,}500}\).  
FV of warrants = \(1{,}500 \times \$3 = \mathbf{\$4{,}500}\).  
Allocation to bonds = \(156{,}000 - 4{,}500 = \mathbf{\$151{,}500}\).  
Premium on bonds = \(151{,}500 - 150{,}000 = \mathbf{\$1{,}500}\).

*January 1, Year 1 — Detachable warrants (incremental method)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 156,000 | |
| Bonds Payable | | 150,000 |
| Premium on Bonds Payable | | 1,500 |
| Paid-In Capital—Stock Warrants | | 4,500 |

**Check:** Dr 156,000 = Cr 150,000 + 1,500 + 4,500. **Balanced.**

**e. Why different; premium comparison**

Nondetachable warrants cannot be sold separately, so there is **no separate fair value** for the equity feature and **100% of proceeds** stay with the bonds. Detachable warrants **do** have a separate market, so ASC 470-20 requires allocation of a portion of proceeds to **Paid-In Capital—Stock Warrants**, reducing the amount (and premium) assigned to debt.

Premium Part A **$6,000** − premium Part B **$1,500** = **$4,500** less premium under detachable accounting (exactly the equity allocation).

**Key insight:** Detachability is the switch. **Nondetachable** = straight debt (full package price on the bond, full amort schedule on that carrying amount). **Detachable** = split package price to debt + equity; only the debt residual is amortized; equity is cleared later by exercise or expiration.

---

### Q4 — MC — Method selection for detachable warrants
**LO:** LO 16-11  
**Concept:** Classification of allocation method (incremental vs proportional) for bonds with detachable stock warrants  
**Question:**  
On January 1, **Lumen Ridge Tools** issues nonconvertible bonds with **detachable** stock purchase warrants for a single package price. Immediately after issuance, the warrants trade in an active market. The fair value of identical bonds **without** warrants **cannot** be determined. Which measurement approach should Lumen Ridge use to allocate the package proceeds?

- A) Allocate the entire package price to Bonds Payable (and premium/discount); record nothing for warrants because the bonds are nonconvertible  
- B) Use the **proportional method**, estimating a bond FV so both relative FVs can be applied  
- C) Use the **incremental method**: measure warrants at known FV and assign the residual package proceeds to the bonds  
- D) Record the full package price as Paid-In Capital—Stock Warrants and accrete Bonds Payable from zero to face  

**Answer:** **C.** When warrants are detachable and only one security’s fair value is known, the **incremental method** assigns known FV to that security (here, the warrants) and the remaining proceeds to the bonds. A is correct only for **nondetachable** warrants. B requires known FV of **both** instruments. D reverses the economics and violates debt face recognition.

---

### Q5 — MC — Nondetachable warrants presentation
**LO:** LO 16-11  
**Concept:** Classification of proceeds when bonds are issued with nondetachable stock warrants  
**Question:**  
**Copperline Logistics** issues bonds with **nondetachable** stock purchase warrants at a package price above face. No separate market exists for the warrants. At issuance, Copperline should:

- A) Credit Paid-In Capital—Stock Warrants for the excess of package price over face and credit Bonds Payable for face  
- B) Allocate package proceeds between debt and equity using relative fair values even though warrants are nondetachable  
- C) Credit Bonds Payable for face and Premium on Bonds Payable for the entire excess of package price over face (straight-debt treatment)  
- D) Debit a deferred charge for the warrant feature and amortize it separately from bond interest  

**Answer:** **C.** Nondetachable warrants have no separate market, so the issuer treats the package as a **straight-debt issue**: all proceeds go to the bonds (face + premium or − discount). No Paid-In Capital—Stock Warrants is recognized at issuance for nondetachable warrants.

---

### Self-check
- [x] Every JE balances
- [x] Math recomputed (allocations, SL amort schedules, exercise plugs, maturity)
- [x] Core demo not sidebar-only (Demo 16-11 / Review 16-11 path: nondetachable, incremental, proportional, exercise, expiration)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE (maturity + warrant exercise/expiration)
- [x] Original companies and numbers (not textbook Embassy/CostKo figures)
