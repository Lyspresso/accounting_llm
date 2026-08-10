# Agent 355 — CORE DEMO — LO 14-11

**Chapter:** 14  
**LO title:** Describe and account for derivatives  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Initial recognition JE:** record derivative asset at cash premium paid (call/put); zero-value interest-rate swap or futures at inception → no entry
- **Subsequent measurement schedule:** fair-value rollforward of the derivative (and, for fair-value hedges, the hedged item); cumulative unrealized G/L through NI or OCI
- **Period-end adjusting JE (emphasis):** mark derivative to fair value each reporting date; speculative and fair-value hedges → Unrealized Gain or Loss—Income; cash-flow hedges (effective portion) → Gain or Loss—OCI; fair-value hedges also remeasure the hedged item through NI
- **Disposal / maturity / settlement JE:** sell or cash-settle the option (remove Call/Put Option at carrying amount); settle interest-rate-swap net cash; execute futures, clear the contract asset/liability, and reclassify AOCI when the hedged forecasted transaction affects earnings
- **Classification:** speculative → FV-NI; fair-value hedge → FV-NI on instrument **and** hedged item; cash-flow hedge → effective portion in OCI until reclassified
- **Number-variant twin:** same multi-period speculative call path with all companies and amounts changed

---

### Q1 — CORE — Speculative call option: initial recognition, multi-period period-end AJs (emphasis), FV schedule, and settlement

**LO:** LO 14-11  
**Concept:** Speculative call option — initial recognition at premium; **period-end fair-value adjusting JEs** (emphasis) through net income; subsequent measurement schedule; disposal/sale settlement  
**Scenario:**  
**Meridian Ridge Capital LLC** (calendar year-end) purchases a **call option** on **October 1, 20X1** from **Pinnacle Clearing Partners** for a cash premium of **$520**. The contract gives Meridian the right (not the obligation) to call **160 shares** of **Apex Dynamics Inc.** common stock at a strike (exercise) price of **$48 per share** at any time over the next **12 months**. The underlying is Apex Dynamics stock; the notional amount is **160 shares**. The option is held for **speculation** (not designated as a hedge).

Fair values of the call option (and cash sale proceeds on disposal):

| Date | Event | Fair value of call option |
|---|---|---:|
| Oct 1, 20X1 | Purchase (premium paid) | $520 |
| Dec 31, 20X1 | Year-end measurement | 1,780 |
| Mar 31, 20X2 | Quarter-end measurement | 2,140 |
| May 12, 20X2 | Sold (cash settlement) for **$2,460** | 2,460 |

Meridian marks the option to fair value at each reporting date and immediately before the May 12 sale, then removes the asset for cash.

**Required:**  
a. Prepare the **October 1, 20X1 initial recognition** journal entry for the call option premium. Prove the entry balances.  
b. Prepare the **December 31, 20X1 period-end adjusting JE** (emphasis) and the **March 31, 20X2 period-end adjusting JE**. Prove each balances.  
c. Prepare a **subsequent measurement schedule** for the Call Option asset from purchase through sale (date, fair value, change in FV, Unrealized Gain or Loss—Income, ending carrying amount). Prove cumulative NI impact equals cash proceeds − premium.  
d. Prepare the **May 12, 20X2** entries: (1) mark to sale-date fair value and (2) record the **sale/settlement** of the call option. Prove each balances.  
e. State the **net gain** on the call option reported in other revenues (expenses) for **20X1** and for **20X2**.

**Answer key:**

**(a) Initial recognition — Oct 1, 20X1**

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 520 | |
| Cash | | 520 |
| *Record speculative call option at premium paid* | | |

**Check:** Dr 520 = Cr 520. **Balanced.**

**(b) Period-end adjusting JEs (emphasis)**

*Dec 31, 20X1 — Mark to FV*  
Δ = \(1{,}780 - 520 = \mathbf{\$1{,}260}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 1,260 | |
| Unrealized Gain or Loss—Income | | 1,260 |
| *Period-end AJ: speculative derivative FV change in NI ($1,780 − $520)* | | |

**Check:** Dr 1,260 = Cr 1,260. **Balanced.**

*Mar 31, 20X2 — Mark to FV*  
Δ = \(2{,}140 - 1{,}780 = \mathbf{\$360}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 360 | |
| Unrealized Gain or Loss—Income | | 360 |
| *Period-end AJ: speculative derivative FV change in NI ($2,140 − $1,780)* | | |

**Check:** Dr 360 = Cr 360. **Balanced.**

**(c) Subsequent measurement schedule — Call Option rollforward**

| Date | Fair value | Change in FV (Δ) | Unrealized G/L—Income | Ending Call Option CV |
|---|---:|---:|---:|---:|
| Oct 1, 20X1 (purchase) | $520 | — | — | $520 |
| Dec 31, 20X1 | 1,780 | +1,260 | Gain $1,260 | 1,780 |
| Mar 31, 20X2 | 2,140 | +360 | Gain 360 | 2,140 |
| May 12, 20X2 (to sale FV) | 2,460 | +320 | Gain 320 | 2,460 |
| May 12, 20X2 (sale) | 0 | remove $(2,460) | — | 0 |

**Cumulative Unrealized G/L—Income:**  
\(1{,}260 + 360 + 320 = \mathbf{\$1{,}940}\) gain.

**Proof:** Cash proceeds on sale \(2{,}460\) − premium \(520\) = **$1,940** net gain. Schedule rolls forward: each ending CV = prior CV + Δ.

**(d) May 12, 20X2 — mark to sale FV and settlement**

(1) Mark to sale-date fair value:  
Δ = \(2{,}460 - 2{,}140 = \mathbf{\$320}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 320 | |
| Unrealized Gain or Loss—Income | | 320 |
| *Mark speculative call to sale-date FV before disposal* | | |

**Check:** Dr 320 = Cr 320. **Balanced.**

(2) Sale / settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,460 | |
| Call Option | | 2,460 |
| *Remove call option at carrying amount on cash settlement* | | |

**Check:** Dr 2,460 = Cr 2,460. **Balanced.**  
After settlement, Call Option balance = $0.

**(e) Income-statement impact**

| Period | Net gain on call option |
|---|---:|
| Year ended Dec 31, 20X1 | $1,260 |
| Year 20X2 (through May 12) | $360 + $320 = **$680** |
| **Total (life of option)** | **$1,940** |

**Key insight:** Speculative derivatives are recognized as assets at the premium paid, **remeasured to fair value at every period-end AJ through net income**, and removed at carrying amount on disposal. The multi-period schedule must roll forward so cumulative NI = cash in − cash out.

---

### Q2 — CORE number variant — Speculative call: period-end AJs, schedule, settlement

**LO:** LO 14-11  
**Concept:** Number-variant twin — speculative call option initial recognition, **period-end FV adjusting JEs** (emphasis), subsequent measurement schedule through NI, and disposal settlement  
**Scenario:**  
**Oakline Partners Inc.** (calendar year-end) purchases a **call option** on **November 15, 20X3** from **Silverfern Markets LLC** for a cash premium of **$360**. The contract allows Oakline to call **200 shares** of **Helix BioMed Corp.** at a strike of **$35 per share** anytime in the next **12 months**. Held for **speculation** (not a hedge).

Fair values:

| Date | Event | Fair value of call option |
|---|---|---:|
| Nov 15, 20X3 | Purchase (premium paid) | $360 |
| Dec 31, 20X3 | Year-end measurement | 1,140 |
| Jun 30, 20X4 | Mid-year measurement | 1,560 |
| Aug 8, 20X4 | Sold for cash **$1,890** | 1,890 |

**Required:**  
a. Nov 15, 20X3 **initial recognition** JE. Prove balances.  
b. **Dec 31, 20X3** and **Jun 30, 20X4 period-end adjusting JEs** (emphasis). Prove each balances.  
c. **Subsequent measurement schedule** purchase through sale; prove cumulative NI = proceeds − premium.  
d. **Aug 8, 20X4** mark-to-sale-FV and settlement JEs. Prove balances.  
e. Net gain in **20X3** and in **20X4**.

**Answer key:**

**(a) Initial recognition — Nov 15, 20X3**

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 360 | |
| Cash | | 360 |
| *Record speculative call option at premium paid* | | |

**Check:** Dr 360 = Cr 360. **Balanced.**

**(b) Period-end adjusting JEs (emphasis)**

*Dec 31, 20X3* — Δ = \(1{,}140 - 360 = \mathbf{\$780}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 780 | |
| Unrealized Gain or Loss—Income | | 780 |
| *Period-end AJ: FV change in NI ($1,140 − $360)* | | |

**Check:** Dr 780 = Cr 780. **Balanced.**

*Jun 30, 20X4* — Δ = \(1{,}560 - 1{,}140 = \mathbf{\$420}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 420 | |
| Unrealized Gain or Loss—Income | | 420 |
| *Period-end AJ: FV change in NI ($1,560 − $1,140)* | | |

**Check:** Dr 420 = Cr 420. **Balanced.**

**(c) Subsequent measurement schedule**

| Date | Fair value | Change in FV (Δ) | Unrealized G/L—Income | Ending Call Option CV |
|---|---:|---:|---:|---:|
| Nov 15, 20X3 (purchase) | $360 | — | — | $360 |
| Dec 31, 20X3 | 1,140 | +780 | Gain $780 | 1,140 |
| Jun 30, 20X4 | 1,560 | +420 | Gain 420 | 1,560 |
| Aug 8, 20X4 (to sale FV) | 1,890 | +330 | Gain 330 | 1,890 |
| Aug 8, 20X4 (sale) | 0 | remove $(1,890) | — | 0 |

**Cumulative G/L—Income:** \(780 + 420 + 330 = \mathbf{\$1{,}530}\).  
**Proof:** \(1{,}890 - 360 = \mathbf{\$1{,}530}\).

**(d) Aug 8, 20X4 — mark and settlement**

(1) Mark to sale FV: Δ = \(1{,}890 - 1{,}560 = \mathbf{\$330}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 330 | |
| Unrealized Gain or Loss—Income | | 330 |
| *Mark to sale-date FV before disposal* | | |

**Check:** Dr 330 = Cr 330. **Balanced.**

(2) Settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,890 | |
| Call Option | | 1,890 |
| *Remove call option on cash settlement* | | |

**Check:** Dr 1,890 = Cr 1,890. **Balanced.**

**(e) Income-statement impact**

| Period | Net gain |
|---|---:|
| 20X3 | **$780** |
| 20X4 | $420 + $330 = **$750** |
| **Life total** | **$1,530** |

**Key insight:** Same speculative path as Q1 with all numbers changed: every reporting date needs a **period-end AJ** through NI; disposal removes the asset only after it has been marked to sale-date FV.

---

### Q3 — CORE alternate angle — Fair value hedge (put on HTM) + interest rate swap: period-end dual AJs and settlement

**LO:** LO 14-11  
**Concept:** Fair value hedges — put option on HTM bonds (initial recognition; dual **period-end FV AJs** through NI on option and hedged item; settlement); interest rate swap on fixed-rate note (zero-value inception; cash settlement of net interest; period-end AJs on swap and note payable)  
**Scenario — Part A (put option fair value hedge):**  
**Crestwood Holdings Corp.** (calendar year-end) purchases **200** of **$50 par, 5%** bonds of **Lumen Forge Inc.** at par on **January 2, 20X5** for **$10,000 cash** and classifies them as **HTM** (measured at amortized cost). Ignore bond interest for simplicity.

On **July 1, 20X5**, to offset the risk of declines in the fair value of the Lumen Forge bonds, Crestwood enters a **2-year put option** with **Pinnacle Clearing Partners** allowing Crestwood to sell the **200 bonds at $50 each** (current FV). Cost of the put is **$280** cash, consisting only of **time value**. The put is designated as a **highly effective fair value hedge**.

On **December 31, 20X5**, Lumen Forge bonds trade at **$41 per bond**. Fair value of the put option increases to **$1,960**, consisting of intrinsic value **$1,800** \([($50 − $41) × 200]\) plus time value **$160**.

On **January 20, 20X6**, Crestwood **exercises** the put when bonds still trade at $41 and the put’s fair value equals its intrinsic value of **$1,800** (time value fully decayed). Counterparty pays **$10,000** cash for the bonds.

**Scenario — Part B (interest rate swap fair value hedge):**  
On **January 1, 20X5**, **Crestwood** also issues a **4-year note payable** for **$50,000 cash** at a **fixed 8%** annual rate (interest paid each December 31). The same day, Crestwood enters an **interest rate swap** with notional **$50,000**: Crestwood **receives fixed 8%** and **pays variable** benchmark interest; cash settlement each Dec 31 equals the difference between fixed and market interest on the notional. Swap FV at inception = **$0** (no entry). Hedge is **highly effective**; shortcut method permitted.

At **December 31, 20X5**, the benchmark market rate is **6.5%**. Estimated fair value of the swap asset is **$1,800**.

**Required:**  
**Part A**  
a. Record Jan 2 purchase of HTM bonds and July 1 purchase of the put option. Prove balances.  
b. Prepare **Dec 31, 20X5 period-end adjusting JEs** (emphasis) for (1) the HTM investment attributable to the hedged risk and (2) the put option. Compute net income-statement impact of the dual AJs.  
c. Prepare a brief **subsequent measurement schedule** for Put Option and for net HTM carrying amount (Investment − FVA) through Dec 31, 20X5.  
d. Record Jan 20, 20X6: (1) period-end-style mark of put from $1,960 to $1,800; (2) **exercise/settlement** removing bonds, FVA, and put for $10,000 cash. Prove balances.

**Part B**  
e. Record Jan 1 note issuance (swap = no entry).  
f. Record Dec 31: (1) interest payment to the bank; (2) cash settlement received on the swap; (3) **period-end AJs** (emphasis) for swap FV and note payable FV. Prove each balances.  
g. Present Dec 31, 20X5 balance-sheet amounts for the swap and the note, and the net interest expense and net unrealized G/L for 20X5 related to Part B.

**Answer key:**

**Part A**

**(a) Initial recognition**

*Jan 2, 20X5 — HTM purchase*

| Account | Debit | Credit |
|---|---:|---:|
| Investment in HTM Securities—Lumen Forge Bonds | 10,000 | |
| Cash ($50 × 200) | | 10,000 |
| *Purchase HTM bonds at par* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.**

*July 1, 20X5 — put option premium*

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 280 | |
| Cash | | 280 |
| *Record fair value hedge put option at premium paid* | | |

**Check:** Dr 280 = Cr 280. **Balanced.**

**(b) Dec 31, 20X5 period-end adjusting JEs (emphasis)**

Decline in bond FV attributable to hedged risk:  
\(($50 - $41) × 200 = \mathbf{\$1{,}800}\)

(1) Adjust hedged HTM investment:

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 1,800 | |
| Fair Value Adjustment—HTM | | 1,800 |
| *Period-end AJ: FV decline on hedged HTM item through NI* | | |

**Check:** Dr 1,800 = Cr 1,800. **Balanced.**  
*(FVA—HTM is a contra to the investment account.)*

(2) Adjust put option to FV:  
Δ put = \(1{,}960 - 280 = \mathbf{\$1{,}680}\)

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 1,680 | |
| Unrealized Gain or Loss—Income | | 1,680 |
| *Period-end AJ: FV increase on fair-value-hedge put through NI* | | |

**Check:** Dr 1,680 = Cr 1,680. **Balanced.**

**Net income-statement impact of dual AJs:**  
Loss \(1{,}800\) − Gain \(1{,}680\) = **net unrealized loss $120** (incomplete offset = residual time-value change).

**(c) Subsequent measurement schedule through Dec 31, 20X5**

| Item / date | Amount |
|---|---:|
| **Put Option** | |
| July 1, 20X5 — cost (time value) | $280 |
| Dec 31, 20X5 — FV increase | 1,680 |
| **Dec 31, 20X5 Put Option CV** | **$1,960** |
| **HTM bonds (net)** | |
| Jan 2 — amortized cost | $10,000 |
| Dec 31 — FVA (contra) | (1,800) |
| **Dec 31, 20X5 net carrying amount** | **$8,200** |

BS presentation check: Investment in debt securities **$8,200** + Put option **$1,960** = economic position near locked-in $10,000 less residual time value.

**(d) Jan 20, 20X6 — mark put and exercise settlement**

(1) Time value decay / mark put to intrinsic only:  
Δ = \(1{,}800 - 1{,}960 = \mathbf{\$(160)}\)

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 160 | |
| Put Option | | 160 |
| *Mark put to exercise-date FV (intrinsic only)* | | |

**Check:** Dr 160 = Cr 160. **Balanced.**  
Put Option CV after mark = **$1,800**.

(2) Exercise put — deliver bonds; receive $10,000:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 10,000 | |
| Fair Value Adjustment—HTM | 1,800 | |
| Investment in HTM Securities—Lumen Forge Bonds | | 10,000 |
| Put Option | | 1,800 |
| *Settle fair value hedge: sell bonds at put strike; clear FVA and put* | | |

**Check:** Dr \(10{,}000 + 1{,}800 = 11{,}800\) = Cr \(10{,}000 + 1{,}800 = 11{,}800\). **Balanced.**

**Part B**

**(e) Jan 1, 20X5 — note issuance; swap FV = 0 → no entry**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 50,000 | |
| Notes Payable | | 50,000 |
| *Issue fixed-rate note at par* | | |

**Check:** Dr 50,000 = Cr 50,000. **Balanced.**  
Swap inception FV $0 → **no journal entry**.

**(f) Dec 31, 20X5 — interest, swap settlement, period-end AJs**

Fixed interest to bank: \(8\% × $50{,}000 = \mathbf{\$4{,}000}\)

(1) Interest payment on note:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,000 | |
| Cash | | 4,000 |
| *Pay fixed interest on note (8% × $50,000)* | | |

**Check:** Dr 4,000 = Cr 4,000. **Balanced.**

Variable interest at market: \(6.5\% × $50{,}000 = \mathbf{\$3{,}250}\)  
Net receipt on swap: \(4{,}000 - 3{,}250 = \mathbf{\$750}\)

(2) Cash settlement on interest rate swap:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 750 | |
| Interest Expense | | 750 |
| *Receive net settlement on swap (fixed received − variable paid)* | | |

**Check:** Dr 750 = Cr 750. **Balanced.**  
Net interest expense after settlement = \(4{,}000 - 750 = \mathbf{\$3{,}250}\) (equals market-based interest).

(3) Period-end AJs (emphasis) — swap and hedged liability (shortcut: change in swap FV estimates change in liability FV):

| Account | Debit | Credit |
|---|---:|---:|
| Interest Rate Swap Contract | 1,800 | |
| Unrealized Gain or Loss—Income | | 1,800 |
| *Period-end AJ: mark interest rate swap to FV through NI* | | |

**Check:** Dr 1,800 = Cr 1,800. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 1,800 | |
| Notes Payable | | 1,800 |
| *Period-end AJ: adjust hedged fixed-rate note to FV through NI* | | |

**Check:** Dr 1,800 = Cr 1,800. **Balanced.**

**(g) Presentation — Part B Dec 31, 20X5**

| Balance sheet | Amount |
|---|---:|
| Interest rate swap contract (asset) | **$1,800** |
| Notes payable | **$51,800** |

| Income statement (Part B) | Amount |
|---|---:|
| Interest expense (\(4{,}000 - 750\)) | **$(3,250)** |
| Net unrealized holding gain or loss (\(1{,}800 - 1{,}800\)) | **$0** |

**Key insight:** For **fair value hedges**, period-end AJs hit **both** the derivative and the hedged item through **net income** so effective hedges largely offset. Speculative-style single-side marking is not enough when hedge accounting applies. Swap inception at zero FV needs no entry; settlement cash adjusts **interest expense** toward the variable (market) rate.

---

### Q4 — CORE alternate angle — Cash flow hedge (futures): period-end OCI AJ, settlement, and reclassification

**LO:** LO 14-11  
**Concept:** Cash flow hedge futures contract — zero-cost inception; **period-end adjusting JE** of futures to FV through **OCI**; multi-date subsequent measurement; settlement on purchase date; reclassification from AOCI into COGS when inventory is sold  
**Scenario:**  
**Cascade Roast Co.** (calendar year-end) forecasts a need to purchase **2,500 pounds** of Colombian coffee on **June 1, 20X2**. Spot price on **November 1, 20X1** is **$1.20 per pound**. On that date Cascade enters a **futures contract** with **ClearPath Exchange** to effectively lock in **$1.20/lb** for delivery **June 1, 20X2**. Under the contract, Cascade buys coffee at the then-market price when needed, but ClearPath pays Cascade for market increases above $1.20 and Cascade pays ClearPath for decreases below $1.20. Cost of the futures contract is **$0**. Designated as a **highly effective cash flow hedge** of the forecasted purchase.

| Date | Spot price of coffee | Futures contract FV (asset) |
|---|---:|---:|
| Nov 1, 20X1 | $1.20/lb | $0 |
| Dec 31, 20X1 | $1.32/lb | $300  [($1.32 − $1.20) × 2,500] |
| June 1, 20X2 (settlement) | $1.40/lb | $500  [($1.40 − $1.20) × 2,500] |

On **June 1, 20X2**, Cascade buys 2,500 lb at the spot market for cash and settles the futures (receives **$500** from ClearPath).  
On **August 15, 20X2**, Cascade sells the entire coffee inventory on account for **$2.10 per pound**.

**Required:**  
a. Nov 1, 20X1 entry for initiation of the futures contract (if any).  
b. **Dec 31, 20X1 period-end adjusting JE** (emphasis) for the cash flow hedge. Prove balances.  
c. Subsequent measurement / AOCI rollforward for the futures contract through June 1, 20X2 (before reclass).  
d. June 1, 20X2 entries: (1) purchase coffee inventory at spot; (2) settle futures (update OCI and clear Futures Contract). Prove balances.  
e. August 15, 20X2 entries for credit sale, COGS, and **reclassification of AOCI** into COGS. Prove balances.  
f. Year 20X2 income-statement excerpt for sales, COGS (net of hedge reclass), and gross profit on the coffee.

**Answer key:**

**(a) Nov 1, 20X1 — inception**  
Cost of futures = $0 → **no journal entry**.

**(b) Dec 31, 20X1 period-end AJ (emphasis) — cash flow hedge**

FV of futures = \(($1.32 - $1.20) × 2{,}500 = \mathbf{\$300}\)

| Account | Debit | Credit |
|---|---:|---:|
| Futures Contract | 300 | |
| Gain or Loss—OCI | | 300 |
| *Period-end AJ: cash flow hedge effective FV change in OCI (not NI)* | | |

**Check:** Dr 300 = Cr 300. **Balanced.**

**(c) Subsequent measurement / AOCI schedule**

| Date | Futures FV | Δ FV | Gain or Loss—OCI | Futures CV | AOCI (cumulative, credit = gain) |
|---|---:|---:|---:|---:|---:|
| Nov 1, 20X1 | $0 | — | — | $0 | $0 |
| Dec 31, 20X1 | 300 | +300 | Gain $300 (OCI) | 300 | 300 |
| June 1, 20X2 (to settlement FV) | 500 | +200 | Gain 200 (OCI) | 500 | 500 |
| June 1, 20X2 (settle contract) | 0 | remove | — | 0 | 500 (still in AOCI) |
| Aug 15, 20X2 (reclass to earnings) | — | — | Reclass $(500) | — | 0 |

**(d) June 1, 20X2 — purchase and futures settlement**

(1) Purchase coffee at spot:

| Account | Debit | Credit |
|---|---:|---:|
| Coffee Inventory | 3,500 | |
| Cash ($1.40 × 2,500) | | 3,500 |
| *Acquire coffee inventory at spot market price* | | |

**Check:** Dr 3,500 = Cr 3,500. **Balanced.**

(2) Settle futures — receive \(500\); clear asset \(300\); remaining Δ to OCI \(200\):

| Account | Debit | Credit |
|---|---:|---:|
| Cash [($1.40 − $1.20) × 2,500] | 500 | |
| Gain or Loss—OCI | | 200 |
| Futures Contract | | 300 |
| *Settle cash flow hedge futures; remaining FV change to OCI* | | |

**Check:** Dr 500 = Cr \(200 + 300 = 500\). **Balanced.**  
After settlement: Futures Contract = $0; cumulative AOCI gain = **$500**.

*(Alternative presentation if mark-to-$500 recorded first then cash settlement removing $500 Futures Contract and $500 cash also works and balances; net OCI credit remains $500.)*

**(e) August 15, 20X2 — sale and reclassification**

Sales = \(2.10 × 2{,}500 = \mathbf{\$5{,}250}\)

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 5,250 | |
| Sales | | 5,250 |
| *Credit sale of coffee inventory* | | |

**Check:** Dr 5,250 = Cr 5,250. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 3,500 | |
| Coffee Inventory | | 3,500 |
| *Remove inventory at cost* | | |

**Check:** Dr 3,500 = Cr 3,500. **Balanced.**

Reclassify AOCI when hedged transaction affects earnings (COGS):

| Account | Debit | Credit |
|---|---:|---:|
| Gain or Loss—OCI | 500 | |
| Cost of Goods Sold | | 500 |
| *Reclassify cash flow hedge gain from AOCI into COGS* | | |

**Check:** Dr 500 = Cr 500. **Balanced.**  
Net COGS = \(3{,}500 - 500 = \mathbf{\$3{,}000}\) (equals locked-in contract price \(1.20 × 2{,}500\)).

**(f) Year 20X2 income-statement excerpt (coffee)**

| Line | Amount |
|---|---:|
| Sales | $5,250 |
| Cost of goods sold on coffee (\(3{,}500 - 500\)) | (3,000) |
| **Gross profit** | **$2,250** |

**Key insight:** Cash flow hedges put the **period-end FV AJ in OCI**, not NI. Settlement clears the futures asset/liability; AOCI stays until the forecasted purchase **affects earnings** (sale of inventory → reclass into COGS), locking in the hedged price.

---

### Q5 — MC (classification / measurement path)

**LO:** LO 14-11  
**Concept:** Classification — where changes in fair value of derivatives are reported (net income vs OCI) by designation  

**Question 1:**  
On a reporting date, the fair value of a derivative increases. In which case is the **entire effective change** recorded in **other comprehensive income** rather than net income?

- A) Speculative call option on equity securities  
- B) Put option designated as a highly effective **fair value hedge** of HTM bonds  
- C) Futures contract designated as a highly effective **cash flow hedge** of a forecasted inventory purchase  
- D) Interest rate swap designated as a highly effective **fair value hedge** of a fixed-rate note payable  

**Answer:** **C.** Cash flow hedges record the effective portion of derivative FV changes in **OCI** until reclassified when the hedged forecasted transaction affects earnings. Speculative instruments (A) and fair value hedges (B, D) recognize derivative FV changes **currently in earnings** (and fair value hedges also remeasure the hedged item through earnings).

---

**LO:** LO 14-11  
**Concept:** Period-end adjusting JE for a fair value hedge of a fixed-rate liability  

**Question 2:**  
A company has a fixed-rate note payable and a highly effective receive-fixed / pay-variable interest rate swap designated as a fair value hedge (shortcut method). At year-end the swap’s fair value increases by **$900** (asset). Which pair of **period-end adjusting** effects is correct?

- A) Debit Interest Rate Swap $900; credit OCI $900 only — no entry to Notes Payable  
- B) Debit Interest Rate Swap $900; credit Unrealized Gain or Loss—Income $900; **and** debit Unrealized Gain or Loss—Income $900; credit Notes Payable $900  
- C) Debit Notes Payable $900; credit Interest Rate Swap $900  
- D) No adjusting entry until cash settlement of the swap  

**Answer:** **B.** Fair value hedge accounting marks the **swap through NI** and adjusts the **hedged note payable** by the same amount through NI (shortcut assumes perfect effectiveness). OCI is used for cash flow hedges, not this fair value hedge of a liability. Cash settlement is a separate cash entry that adjusts interest expense; it does not replace the FV period-end AJs.

---

### Self-check
- [x] Every JE balances (Dr = Cr checked on each entry)
- [x] Math recomputed (call Δs; put intrinsic/time; swap interest and FV; futures lb × price)
- [x] Core demo path (speculative call, FV put hedge, IRS FV hedge, CF futures) — not Expanding Your Knowledge sidebars only
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE
- [x] Original companies/numbers (not textbook Bold/Rivendell/SBC demo figures)
