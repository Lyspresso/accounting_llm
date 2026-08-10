# Agent 93 — CORE DEMO — LO 14-11

**Chapter:** 14  
**LO title:** Describe and account for derivatives  
**Critical gap LO:** no

## Concept list for this pack
- **Initial recognition JE:** record derivative assets (call/put options) at premium paid; zero-cost futures/swaps need no entry at inception
- **All derivatives** recognized as assets or liabilities and **measured at fair value**
- **Speculative derivative (call option):** subsequent FV changes through **net income**; disposal/settlement clears the derivative account
- **Fair value hedge (put option on HTM bonds):** FV changes on **both** the hedging instrument and the hedged item through **net income** (same line item); net residual = imperfect offset
- **Fair value hedge (interest rate swap):** zero value at inception; cash settlement adjusts interest expense; FV of swap and offsetting FV of note payable through NI (shortcut method assumes perfect effectiveness)
- **Cash flow hedge (futures):** FV changes in **OCI**; reclassify from AOCI to earnings when the forecasted transaction affects earnings (e.g., COGS)
- **Subsequent measurement schedule** of derivative FV over reporting dates
- **Period-end adjusting JE** to fair value
- **Disposal / maturity / settlement JE** (sale of option; cash settlement of swap; settlement of futures with purchase of inventory)
- **Classification / presentation / disclosure:** NI vs OCI for FV changes; BS line items for derivative assets/liabilities and adjusted hedged items

---

### Q1 — CORE — Speculative call option: initial recognition, period-end FV, disposal
**LO:** LO 14-11  
**Concept:** Initial recognition of a speculative call option at premium; period-end fair value adjustment through NI; disposal (sale) of the option; income statement presentation  
**Scenario:**  
**Mariner Forge Inc.** purchases a **call option** for speculative purposes (not designated as a hedge) from Apex Markets LLC on **March 1**.

| Item | Fact |
|---|---|
| Option premium paid | $480 |
| Notional | Right to call **200 shares** of Helix Dynamics common stock |
| Strike (exercise) price | **$35** per share |
| Total strike if exercised | $35 × 200 = **$7,000** |
| Settlement form | Net cash settlement equal to (market price − strike) × shares, if market > strike |
| Fair value of call option, December 31 | **$2,280** |
| Disposition | Mariner **sells** the option on December 31 for **$2,280** (after the year-end FV adjustment is recorded) |
| Fiscal year-end | December 31 |

**Required:**  
a. Prepare the **initial recognition journal entry** on March 1 for the purchase of the call option.  
b. Prepare the **December 31 period-end adjusting entry** to measure the call option at fair value.  
c. Prepare the **disposal journal entry** for the sale of the call option on December 31.  
d. Present the **current-year income statement impact** of the derivative transactions.  
e. State the **balance sheet** carrying amount of the Call Option immediately after the sale.

**Answer key:**  

**a. March 1 — initial recognition (option premium)**  

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 480 | |
| Cash | | 480 |
| *Recognize speculative derivative asset at cost (premium paid)* | | |

**Check:** Dr = Cr = 480.

**b. December 31 — period-end fair value adjustment**  
Unrealized gain = FV − carrying amount = $2,280 − $480 = **$1,800**

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 1,800 | |
| Unrealized Gain or Loss—Income | | 1,800 |
| *Speculative derivative: entire change in FV through net income* | | |

**Check:** Dr = Cr = 1,800.  
Carrying amount of Call Option after adj = $480 + $1,800 = **$2,280**.

**c. December 31 — disposal (sale) of call option**  

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,280 | |
| Call Option | | 2,280 |
| *Clear derivative asset at carrying amount equal to cash proceeds (no additional G/L)* | | |

**Check:** Dr = Cr = 2,280.

**d. Income statement excerpt — Year ended December 31**  

| Line | Amount |
|---|---:|
| Other revenues (expenses) | |
| Net gain on call option | **$1,800** |

(Only the FV mark-to-market hits NI; sale at already-adjusted FV adds no further gain.)

**e. Balance sheet after sale**  
Call Option = **$0** (asset fully disposed).

**Key insight:** Speculative derivatives are assets (or liabilities) measured at fair value with changes recognized **currently in earnings**. Initial recognition is at the premium paid; subsequent measurement and disposal clear through the derivative account with G/L already in NI.

---

### Q2 — CORE number variant — Speculative call option twin
**LO:** LO 14-11  
**Concept:** Number-variant twin — initial recognition of speculative call; period-end FV through NI; settlement/sale; NI impact  
**Scenario:**  
**Cedar Ridge Holdings** purchases a **call option** for speculation from Northline Capital Markets on **October 1**.

| Item | Fact |
|---|---|
| Option premium paid | $360 |
| Notional | Right to call **150 shares** of Meridian Labs common stock |
| Strike price | **$40** per share |
| Total strike if exercised | $40 × 150 = **$6,000** |
| Fair value of call option, December 31 | **$1,560** |
| Disposition | Cedar Ridge **settles/sells** the option on December 31 for **$1,560** (after year-end FV adjustment) |
| Fiscal year-end | December 31 |

**Required:**  
a. Prepare the **initial recognition JE** on October 1.  
b. Prepare the **December 31 period-end adjusting JE**.  
c. Prepare the **settlement/sale JE** on December 31.  
d. State the **total impact on net income** for the year from the call option.  
e. Brief **subsequent measurement rollforward** of the Call Option account (beginning → purchase → FV adj → disposal → ending).

**Answer key:**  

**a. October 1 — initial recognition**  

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 360 | |
| Cash | | 360 |

**Check:** Dr = Cr = 360.

**b. December 31 — period-end FV adjustment**  
Unrealized gain = $1,560 − $360 = **$1,200**

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 1,200 | |
| Unrealized Gain or Loss—Income | | 1,200 |

**Check:** Dr = Cr = 1,200.

**c. December 31 — settlement/sale**  

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,560 | |
| Call Option | | 1,560 |

**Check:** Dr = Cr = 1,560.

**d. Total NI impact**  
Net gain on call option = **$1,200**.

**e. Subsequent measurement schedule (Call Option rollforward)**  

| Date | Event | Debit (Cr) | Balance |
|---|---|---:|---:|
| Oct 1 | Beginning | — | $0 |
| Oct 1 | Purchase (initial recognition) | 360 | 360 |
| Dec 31 | FV adjustment (to $1,560) | 1,200 | 1,560 |
| Dec 31 | Sale / settlement | (1,560) | **0** |

**Key insight:** Same core path as Q1 with all amounts changed: premium → mark to FV through NI → dispose at carrying amount. The NI impact equals the cumulative change in fair value while held.

---

### Q3 — CORE — Put option as fair value hedge of HTM bonds
**LO:** LO 14-11  
**Concept:** Initial recognition of put option fair value hedge; period-end adjusting JEs for hedged HTM item and put; subsequent measurement schedule; net NI residual; BS/IS presentation  
**Scenario:**  
**Northline Capital Co.** holds HTM debt and hedges fair value risk with a put option. Ignore bond interest for simplicity. The hedge is **highly effective**.

| Date | Event |
|---|---|
| January 5 | Purchases **250** bonds of Harborline Corp. (**$40** face each) at **par**. Classifies as **HTM** (amortized cost). Total cost = 250 × $40 = **$10,000**. |
| July 1 | Enters a **2-year put option** with Apex Markets LLC allowing Northline to sell the **250 bonds at $40** each (current FV). Premium paid = **$350** (time value only). Designated as a **fair value hedge**. |
| December 31 | Harborline bonds trade at **$32** per bond. Fair value of put option = **$2,250**, consisting of intrinsic value **$2,000** [($40 − $32) × 250] + time value **$250**. |

**Required:**  
a. Prepare the **January 5** JE to acquire the HTM bonds (underlying asset).  
b. Prepare the **July 1 initial recognition JE** for the put option.  
c. Prepare the **December 31 period-end adjusting entries** for (1) the HTM investment fair value change attributable to the hedged risk and (2) the put option fair value change.  
d. Prepare a **subsequent measurement schedule** for the Put Option and for the investment’s net carrying amount (Investment − Fair Value Adjustment).  
e. Present **December 31 balance sheet** and **income statement** excerpts for the derivative/hedge relationships.

**Answer key:**  

**a. January 5 — purchase of underlying HTM bonds**  

| Account | Debit | Credit |
|---|---:|---:|
| Investment in HTM Securities—Harborline Bonds | 10,000 | |
| Cash (250 × $40) | | 10,000 |

**Check:** Dr = Cr = 10,000.

**b. July 1 — initial recognition of put option (fair value hedge)**  

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 350 | |
| Cash | | 350 |
| *Recognize hedging derivative at premium paid* | | |

**Check:** Dr = Cr = 350.

**c. December 31 — period-end adjustments**  

Decline in bond FV attributable to hedged risk = ($40 − $32) × 250 = **$2,000**

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 2,000 | |
| Fair Value Adjustment—HTM | | 2,000 |
| *FV hedge: adjust hedged item’s carrying amount for change in FV of hedged risk through NI* | | |

**Check:** Dr = Cr = 2,000.

Increase in put FV = $2,250 − $350 = **$1,900**

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 1,900 | |
| Unrealized Gain or Loss—Income | | 1,900 |
| *FV hedge: mark hedging instrument to FV through NI* | | |

**Check:** Dr = Cr = 1,900.

**Net unrealized holding loss** = $2,000 − $1,900 = **$100** (imperfect offset; time-value residual).

**d. Subsequent measurement schedules**

*Put Option rollforward*

| Date | Event | Debit (Cr) | Balance |
|---|---|---:|---:|
| July 1 | Purchase | 350 | 350 |
| Dec 31 | FV adjustment | 1,900 | **2,250** |

*Harborline HTM investment — net carrying amount*

| Component | Amount |
|---|---:|
| Investment in HTM Securities (amortized cost) | $10,000 |
| Less: Fair Value Adjustment—HTM (contra) | (2,000) |
| **Net investment carrying amount** | **$8,000** |
| Put Option asset | **$2,250** |
| Combined economic position (net of residual) | $10,250* |

\*Combined = $8,000 + $2,250 = $10,250; compared with original $10,000 investment + $350 premium = $10,350, the $100 NI loss is the residual cost of the hedge for the period.

**e. Financial statement presentation**

*Balance sheet excerpt — December 31*

| Assets | Amount |
|---|---:|
| Investment in debt securities (HTM, net) | $8,000 |
| Put option | 2,250 |

*Income statement excerpt — Year ended December 31*

| Other revenues (expenses) | Amount |
|---|---:|
| Net unrealized holding gain or loss ($2,000 − $1,900) | **$(100)** |

**Key insight:** For a **fair value hedge**, both the derivative and the hedged item’s FV change (for the hedged risk) hit **net income** in the same line item. HTM bonds that would not otherwise be marked to market are adjusted while the hedge is in effect. Residual NI impact reflects imperfect offset (here, decline in option time value).

---

### Q4 — CORE — Interest rate swap as fair value hedge of fixed-rate note
**LO:** LO 14-11  
**Concept:** Zero-cost swap inception (no JE); interest payment; cash settlement of swap; period-end FV adjustment of swap and note (shortcut method); presentation  
**Scenario:**  
**Summit Bridge Manufacturing** wants to convert fixed-rate debt to effectively variable using an interest rate swap designated as a **fair value hedge**. The hedge is **highly effective**; use the **shortcut method** (change in FV of swap estimates the offsetting change in the note’s FV).

| Item | Fact |
|---|---|
| January 1 | Issues a **4-year note payable** to a bank for **$80,000** cash at a **fixed 6%** interest rate |
| January 1 | Enters interest rate swap with Apex Markets LLC: **receive fixed 6%** on notional **$80,000**; **pay variable** based on a designated benchmark rate. Swap **fair value = $0** at inception. Cash settlement each December 31 equals difference between fixed and variable interest on the notional. |
| December 31 | Benchmark / market rate = **5%** |
| December 31 | Estimated fair value of the interest rate swap (asset) = **$2,400** |
| Fiscal year-end | December 31 |

**Required:**  
a. Record issuance of the note and the swap agreement on **January 1**.  
b. Record the **interest payment** to the bank on December 31.  
c. Record the **cash settlement** on the interest rate swap on December 31 (market rate 5%).  
d. Record **period-end adjusting entries** for the fair value of the swap and the note payable.  
e. Present **December 31 balance sheet** and **income statement** excerpts. Show a brief **net interest expense** computation.

**Answer key:**  

**a. January 1 — note issuance; swap at zero value**  

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 80,000 | |
| Note Payable | | 80,000 |
| *Issue fixed-rate note at par* | | |

**Check:** Dr = Cr = 80,000.

Swap fair value = $0 → **no journal entry** for the swap at inception.

**b. December 31 — interest on note payable**  
Interest = 6% × $80,000 = **$4,800**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,800 | |
| Cash | | 4,800 |

**Check:** Dr = Cr = 4,800.

**c. December 31 — cash settlement received on swap**  
Variable interest at market = 5% × $80,000 = **$4,000**  
Settlement due to Summit = fixed − variable = $4,800 − $4,000 = **$800** (rates fell → Summit receives cash)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 800 | |
| Interest Expense | | 800 |
| *Net cash settlement reduces interest expense to effective variable rate* | | |

**Check:** Dr = Cr = 800.

**d. December 31 — fair value adjustments (shortcut method)**  

| Account | Debit | Credit |
|---|---:|---:|
| Interest Rate Swap Contract | 2,400 | |
| Unrealized Gain or Loss—Income | | 2,400 |
| *Mark swap asset to FV through NI* | | |

**Check:** Dr = Cr = 2,400.

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 2,400 | |
| Note Payable | | 2,400 |
| *Adjust hedged liability to FV; offsetting loss through NI* | | |

**Check:** Dr = Cr = 2,400.

**e. Financial statement presentation**

*Net interest expense computation*

| Component | Amount |
|---|---:|
| Gross interest paid to bank | $4,800 |
| Less: cash received on swap settlement | (800) |
| **Net interest expense** | **$4,000** |

(Equals variable market interest 5% × $80,000 — the economic goal of the swap.)

*Balance sheet excerpt — December 31*

| | Amount |
|---|---:|
| **Assets** | |
| Interest rate swap contract | $2,400 |
| **Liabilities** | |
| Note payable ($80,000 + $2,400) | $82,400 |

*Income statement excerpt — Year ended December 31*

| Other revenues (expenses) | Amount |
|---|---:|
| Interest expense ($4,800 − $800) | $(4,000) |
| Net unrealized holding gain or loss ($2,400 − $2,400) | **0** |

**Key insight:** An interest rate swap used as a **fair value hedge** of fixed-rate debt converts interest cost economically to variable. Under the shortcut method, FV changes of the swap and the note **perfectly offset** in NI. Cash settlements adjust **interest expense**; the swap is an asset when rates fall (receive-fixed is valuable).

---

### Q5 — CORE — Futures contract as cash flow hedge of forecasted purchase
**LO:** LO 14-11  
**Concept:** Zero-cost futures inception; period-end FV through OCI; settlement at purchase; reclassification of AOCI into COGS when inventory is sold; presentation  
**Scenario:**  
**Rivertown Roasters Co.** projects a need for green coffee beans and hedges purchase-price risk with a futures contract designated as a **cash flow hedge**. The hedge is **highly effective**. Contract cost is **zero**.

| Date | Event |
|---|---|
| November 1, Year 1 | Projects need to purchase **2,000 pounds** of Brazilian coffee on **June 1, Year 2**. Spot price = **$1.50**/lb. Enters futures with Clearing House Inc. to effectively lock **$1.50**/lb for 2,000 lb delivery on June 1, Year 2. Under the contract, Rivertown buys coffee at then-current market on June 1; Clearing House pays Rivertown for price increases above $1.50 and Rivertown pays Clearing House for decreases below $1.50. |
| December 31, Year 1 | Spot price of coffee = **$1.70**/lb. |
| June 1, Year 2 | Spot price = **$1.80**/lb. Rivertown purchases 2,000 lb at market and settles the futures. |
| August 15, Year 2 | Sells the entire coffee inventory on account at **$2.40**/lb. |

**Required:**  
a. Record the **November 1, Year 1** entry for initiation of the futures contract (if any).  
b. Record the **December 31, Year 1 period-end adjusting entry** for the futures contract.  
c. Record the **June 1, Year 2** entries for (1) purchase of coffee inventory at market and (2) settlement of the futures contract (including any additional OCI to bring cumulative OCI to the full settlement amount).  
d. Record the **August 15, Year 2** sale and the **reclassification** of AOCI into cost of goods sold.  
e. Present the **Year 2 income statement** impact related to the sale of coffee (sales, COGS net of reclassification, gross profit).  
f. Prepare a **brief OCI / Futures Contract subsequent measurement schedule** from inception through settlement and reclassification.

**Answer key:**  

**a. November 1, Year 1 — initiation**  
Cost of futures = $0 → **no journal entry**.

**b. December 31, Year 1 — period-end FV through OCI**  
FV of futures asset = ($1.70 − $1.50) × 2,000 = **$400**

| Account | Debit | Credit |
|---|---:|---:|
| Futures Contract | 400 | |
| Gain or Loss—OCI | | 400 |
| *Cash flow hedge: effective portion of FV change in OCI, not NI* | | |

**Check:** Dr = Cr = 400.

**c. June 1, Year 2 — purchase and settlement**  

Purchase at market: 2,000 × $1.80 = **$3,600**

| Account | Debit | Credit |
|---|---:|---:|
| Coffee Inventory | 3,600 | |
| Cash | | 3,600 |

**Check:** Dr = Cr = 3,600.

Settlement from Clearing House: ($1.80 − $1.50) × 2,000 = **$600**  
Additional OCI gain since Dec 31: $600 − $400 = **$200**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 600 | |
| Gain or Loss—OCI | | 200 |
| Futures Contract | | 400 |
| *Collect settlement; update OCI for remaining FV change; clear futures asset* | | |

**Check:** Dr = Cr = 600.

Cumulative Gain or Loss—OCI credit balance (AOCI) related to hedge = $400 + $200 = **$600**.

**d. August 15, Year 2 — sale and reclassification into earnings**  
Sales = 2,000 × $2.40 = **$4,800**

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 4,800 | |
| Sales | | 4,800 |

**Check:** Dr = Cr = 4,800.

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 3,600 | |
| Coffee Inventory | | 3,600 |
| *Remove inventory at purchase cost* | | |

**Check:** Dr = Cr = 3,600.

Reclassify AOCI into COGS (reduces COGS; inventory “locked-in” cost = contract price $1.50 × 2,000 = $3,000):

| Account | Debit | Credit |
|---|---:|---:|
| Gain or Loss—OCI | 600 | |
| Cost of Goods Sold | | 600 |
| *Reclassify cash flow hedge gain from AOCI when forecasted transaction affects earnings* | | |

**Check:** Dr = Cr = 600.

**e. Year 2 income statement excerpt (coffee sale)**  

| Line | Amount |
|---|---:|
| Sales | $4,800 |
| Cost of goods sold on coffee ($3,600 − $600) | (3,000) |
| **Gross profit** | **$1,800** |

Net COGS equals locked-in contract price: 2,000 × $1.50 = **$3,000**.

**f. Subsequent measurement schedule — Futures Contract and related OCI**

| Date | Event | Futures bal. | Cumulative OCI gain (AOCI) |
|---|---|---:|---:|
| Nov 1, Y1 | Inception (zero cost) | $0 | $0 |
| Dec 31, Y1 | FV adj ($0.20 × 2,000) | 400 | 400 |
| June 1, Y2 | Additional FV to settlement ($0.10 × 2,000); clear contract | 0 | 600 |
| Aug 15, Y2 | Reclass AOCI → COGS | 0 | **0** |

**Key insight:** **Cash flow hedges** park effective FV changes in **OCI** until the hedged forecasted transaction hits earnings. At purchase, inventory is recorded at market; the settlement gain lives in AOCI until sale, when it is reclassified to **reduce COGS** so earnings reflect the **hedged (locked-in) cost**.

---

### Q6 — MC — Classification of derivative FV changes and hedge type
**LO:** LO 14-11  
**Concept:** Classification — where fair value changes of derivatives are reported (NI vs OCI) by designation  
**Question:**  
Which of the following correctly describes the **primary financial statement location** of unrealized gains and losses from marking a derivative to fair value under U.S. GAAP (assuming the hedge is highly effective where designated)?

- A) Speculative call option → OCI; cash flow hedge futures → net income; fair value hedge put → OCI  
- B) Speculative call option → net income; cash flow hedge futures → OCI (until reclassification); fair value hedge put → net income  
- C) All derivatives always report FV changes only in OCI until settlement  
- D) Speculative call option → AOCI permanently; fair value hedge interest rate swap → OCI; cash flow hedge → net income immediately  

**Answer:** **B.**  
Speculative derivatives: FV changes through **earnings**. Cash flow hedges: effective portion through **OCI**, reclassified into earnings when the hedged transaction affects earnings. Fair value hedges: FV changes on the derivative (and the hedged item for the hedged risk) through **earnings**. A, C, and D reverse or misstate these paths.

---

### Q6b — MC — Classification of interest rate swap presentation
**LO:** LO 14-11  
**Concept:** Classification — economic effect and presentation of a receive-fixed / pay-variable interest rate swap designated as a fair value hedge of fixed-rate debt  
**Question:**  
Summit Bridge issues fixed-rate debt and enters a receive-fixed, pay-variable interest rate swap that qualifies as a **fair value hedge** of the note (highly effective; shortcut method). During the year, market rates fall, Summit receives a net cash settlement on the swap, and the swap has a positive fair value at year-end. Which presentation is correct?

- A) Cash settlement increases interest expense; swap FV gain and note FV loss both go to OCI and do not offset in NI  
- B) Cash settlement reduces interest expense toward the variable rate; swap is reported as an asset; unrealized gain on the swap and unrealized loss on the note both go through NI and offset  
- C) No entry is made for the cash settlement; the entire swap FV is capitalized as a reduction of the note payable only  
- D) The note remains at amortized cost with no FV adjustment because HTM-style amortized cost always applies to notes payable  

**Answer:** **B.**  
Cash settlement on a receive-fixed swap when rates fall **reduces interest expense** (economic variable rate). The swap is an **asset** when valuable. Under a fair value hedge of the liability, both the swap gain and the increase in the note’s fair value flow through **NI** and offset (perfectly under the shortcut method). The hedged note is adjusted away from pure amortized-cost presentation while the hedge is designated. A misplaces amounts to OCI; C and D omit required FV accounting for a designated fair value hedge.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (call gains 1,800 / 1,200; put residual loss 100; swap interest 4,000 and FV 2,400 offset; futures OCI 400→600, COGS net 3,000)
- [x] Core demo not sidebar-only (Demo 14-11A/B/C/D primary path: speculative call, FV put hedge, interest rate swap FV hedge, cash flow futures)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q6, Q6b)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
