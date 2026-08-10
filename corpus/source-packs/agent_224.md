# Agent 224 — CORE DEMO — LO 14-11

**Chapter:** 14  
**LO title:** Describe and account for derivatives  
**Critical gap LO:** no

## Concept list for this pack
- **Initial recognition JE:** record derivative at premium paid (call/put option asset); zero-value interest rate swap / futures at inception → no entry
- **Subsequent measurement schedule (emphasis):** multi-period fair-value rollforward of the derivative carrying amount; cumulative unrealized G/L through NI (speculative and fair-value hedges) or OCI (cash-flow hedges)
- **Period-end adjusting JE:** mark derivative to fair value; for fair-value hedges, also adjust the hedged item (HTM bonds or fixed-rate note payable) through net income
- **Disposal / maturity / settlement JE:** sell or cash-settle the option (remove Call/Put Option at carrying amount); settle interest-rate-swap net cash; execute futures and reclassify AOCI when the hedged item affects earnings
- **Classification:** speculative → FV-NI; fair-value hedge → FV-NI on both instrument and hedged item; cash-flow hedge → effective portion in OCI until reclassified to earnings
- **Number-variant twin:** same multi-period speculative call path with all amounts changed

---

### Q1 — CORE — Speculative call option: multi-period subsequent measurement schedule, period-end FV adj, and settlement
**LO:** LO 14-11  
**Concept:** Speculative call option — initial recognition at premium; multi-period subsequent measurement (FV) schedule through net income; period-end adjusting JEs; disposal/sale settlement  
**Scenario:**  
**Harborline Analytics Corp.** purchases a **call option** on **January 5, Year 1** from **Northbridge Capital Markets** for a cash premium of **$480**. The contract gives Harborline the right (not the obligation) to call **120 shares** of **Quorom Robotics** common stock at a strike (exercise) price of **$55 per share** at any time over the next **12 months**. The option is held for **speculation** (not designated as a hedge). Harborline reports fair-value adjustments **quarterly**.

Fair values of the call option (and cash sale proceeds on disposal):

| Date | Event | Fair value of call option |
|---|---|---:|
| Jan 5, Y1 | Purchase (premium paid) | $480 |
| Mar 31, Y1 | Period-end measurement | 920 |
| Jun 30, Y1 | Period-end measurement | 1,760 |
| Sep 30, Y1 | Period-end measurement | 1,340 |
| Dec 20, Y1 | Sold (cash settlement) for **$1,580** | 1,580 |

Harborline marks the option to fair value immediately before the Dec 20 sale (if not already at sale-date FV), then removes the asset for cash.

**Required:**  
a. Prepare the **January 5 initial recognition** journal entry for the call option premium.  
b. Prepare a **subsequent measurement schedule** for the Call Option asset for Year 1 (date, fair value, change in FV, Unrealized Gain or Loss—Income, ending carrying amount). Total the Year 1 income-statement impact and prove it equals cash proceeds − premium.  
c. Prepare the **period-end adjusting journal entries** at Mar 31, Jun 30, and Sep 30.  
d. Prepare the **December 20** entries: (1) mark to sale-date fair value and (2) record the **sale/settlement** of the call option.  
e. State the **single-line net gain** on the call option that appears in other revenues (expenses) for Year 1.

**Answer key:**

**(a) Initial recognition — Jan 5, Year 1**

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 480 | |
| Cash | | 480 |
| *Record speculative call option at premium paid* | | |

**Check:** Dr 480 = Cr 480. **Balanced.**

**(b) Subsequent measurement schedule (emphasis) — Call Option rollforward**

| Date | Fair value | Change in FV (Δ) | Unrealized G/L—Income | Ending Call Option CV |
|---|---:|---:|---:|---:|
| Jan 5, Y1 (purchase) | $480 | — | — | $480 |
| Mar 31, Y1 | 920 | +440 | Gain $440 | 920 |
| Jun 30, Y1 | 1,760 | +840 | Gain 840 | 1,760 |
| Sep 30, Y1 | 1,340 | (420) | Loss 420 | 1,340 |
| Dec 20, Y1 (to sale FV) | 1,580 | +240 | Gain 240 | 1,580 |
| Dec 20, Y1 (sale) | 0 | remove $(1,580) | — | 0 |

**Cumulative Unrealized G/L—Income Year 1:**  
\(440 + 840 - 420 + 240 = \mathbf{\$1{,}100}\) gain.

**Proof:** Cash proceeds on sale \(1{,}580\) − premium \(480\) = **$1,100** net gain. Schedule rolls forward: each ending CV = prior CV + Δ.

**(c) Period-end adjusting JEs**

*Mar 31 — Mark to FV*  
Δ = \(920 - 480 = \mathbf{\$440}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 440 | |
| Unrealized Gain or Loss—Income | | 440 |
| *Speculative derivative: FV change in net income* | | |

**Check:** Dr 440 = Cr 440. **Balanced.**

*Jun 30 — Mark to FV*  
Δ = \(1{,}760 - 920 = \mathbf{\$840}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 840 | |
| Unrealized Gain or Loss—Income | | 840 |

**Check:** Dr 840 = Cr 840. **Balanced.**

*Sep 30 — Mark to FV*  
Δ = \(1{,}340 - 1{,}760 = \mathbf{\$(420)}\)

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 420 | |
| Call Option | | 420 |

**Check:** Dr 420 = Cr 420. **Balanced.**  
Call Option CV after Sep 30 = \(1{,}760 - 420 = \mathbf{\$1{,}340}\).

**(d) Disposal / settlement — Dec 20, Year 1**

*Mark to sale-date FV*  
Δ = \(1{,}580 - 1{,}340 = \mathbf{\$240}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 240 | |
| Unrealized Gain or Loss—Income | | 240 |

**Check:** Dr 240 = Cr 240. **Balanced.**  
Call Option CV = **$1,580**.

*Sale of call option (cash settlement)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,580 | |
| Call Option | | 1,580 |
| *Remove derivative asset at carrying amount equal to proceeds* | | |

**Check:** Dr 1,580 = Cr 1,580. **Balanced.** Call Option ending balance = **$0**.

**(e) Income statement — Year 1**

Other revenues (expenses):  
**Net gain on call option — $1,100**  
(\(440 + 840 - 420 + 240\); equals cash received on sale − premium paid.)

**Key insight:** Speculative derivatives are recognized as assets/liabilities and measured at **fair value each period**, with **all** FV changes in **net income**. A subsequent measurement schedule links premium → period-end FVs → disposal proceeds; cumulative NI gain/loss always equals total cash inflows (settlement) minus cash outflows (premium), when the instrument is fully settled.

---

### Q2 — CORE number variant — Speculative call option multi-period schedule and settlement
**LO:** LO 14-11  
**Concept:** Number-variant twin — speculative call option initial recognition, multi-period subsequent measurement schedule through NI, period-end adjusting JEs, and disposal settlement  
**Scenario:**  
**Westmoor Portfolio Partners** purchases a **call option** on **February 1, Year 1** from **Helix Securities LLC** for a cash premium of **$750**. The option covers **200 shares** of **Helix Biometrics** at a strike of **$35 per share** and is held for **speculation**. Westmoor adjusts the option to fair value at each interim reporting date below and sells the option for cash on **November 15, Year 1**.

| Date | Event | Fair value of call option |
|---|---|---:|
| Feb 1, Y1 | Purchase (premium) | $750 |
| Apr 30, Y1 | Period-end measurement | 1,450 |
| Jul 31, Y1 | Period-end measurement | 2,900 |
| Oct 31, Y1 | Period-end measurement | 2,200 |
| Nov 15, Y1 | Sold for cash **$2,550** | 2,550 |

**Required:**  
a. Journal entry for the **Feb 1** purchase.  
b. **Subsequent measurement schedule** of the Call Option (FV, Δ, G/L—Income, ending CV); prove total NI impact = sale proceeds − premium.  
c. Period-end adjusting JEs at **Apr 30, Jul 31, and Oct 31**.  
d. **Nov 15** mark-to-sale FV and **settlement** JEs.  
e. Year 1 net gain (loss) on the call option for the income statement.

**Answer key:**

**(a) Feb 1 — Initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 750 | |
| Cash | | 750 |

**Check:** Dr 750 = Cr 750. **Balanced.**

**(b) Subsequent measurement schedule**

| Date | Fair value | Δ FV | Unrealized G/L—Income | Ending Call Option CV |
|---|---:|---:|---:|---:|
| Feb 1, Y1 | $750 | — | — | $750 |
| Apr 30, Y1 | 1,450 | +700 | Gain $700 | 1,450 |
| Jul 31, Y1 | 2,900 | +1,450 | Gain 1,450 | 2,900 |
| Oct 31, Y1 | 2,200 | (700) | Loss 700 | 2,200 |
| Nov 15, Y1 (to sale) | 2,550 | +350 | Gain 350 | 2,550 |
| Nov 15, Y1 (sale) | 0 | remove | — | 0 |

**Cumulative NI:** \(700 + 1{,}450 - 700 + 350 = \mathbf{\$1{,}800}\) gain.  
**Proof:** \(2{,}550 - 750 = \mathbf{\$1{,}800}\).

**(c) Period-end adjusting JEs**

*Apr 30* — Δ = \(1{,}450 - 750 = \mathbf{\$700}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 700 | |
| Unrealized Gain or Loss—Income | | 700 |

**Check:** 700 = 700.

*Jul 31* — Δ = \(2{,}900 - 1{,}450 = \mathbf{\$1{,}450}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 1,450 | |
| Unrealized Gain or Loss—Income | | 1,450 |

**Check:** 1,450 = 1,450.

*Oct 31* — Δ = \(2{,}200 - 2{,}900 = \mathbf{\$(700)}\)

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 700 | |
| Call Option | | 700 |

**Check:** 700 = 700. CV = **$2,200**.

**(d) Nov 15 — Mark and settlement**

*Mark to sale FV* — Δ = \(2{,}550 - 2{,}200 = \mathbf{\$350}\)

| Account | Debit | Credit |
|---|---:|---:|
| Call Option | 350 | |
| Unrealized Gain or Loss—Income | | 350 |

**Check:** 350 = 350.

*Sale / cash settlement*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,550 | |
| Call Option | | 2,550 |

**Check:** 2,550 = 2,550. Call Option = **$0**.

**(e) Income statement**  
**Net gain on call option — $1,800.**

**Key insight:** Same core path as Q1 with every amount changed. The subsequent measurement schedule is the control document: each period’s adjusting entry is exactly the schedule’s Δ FV column, and disposal removes the schedule’s final carrying amount for cash.

---

### Q3 — CORE alternate angle — Fair value hedge (put on HTM) and interest rate swap: period-end adj, settlement, multi-period swap schedule
**LO:** LO 14-11  
**Concept:** Fair value hedges — put option on HTM bonds (initial recognition, dual period-end FV adjustments through NI); interest rate swap on fixed-rate note (zero-value inception, cash settlement of net interest, multi-period subsequent measurement of swap and note payable)  
**Scenario (two independent cases):**

#### Case A — Put option as a fair value hedge (underlying = HTM asset)
**Summit Peak Holdings Co.** acquires **200** of **$100** par, **6%** bonds of **Larkspur Corp.** on **January 1, Year 1** at **par ($20,000)** and classifies them as **held-to-maturity (HTM)** (amortized cost). For simplicity, **ignore bond interest**.

On **March 1, Year 1**, to offset fair-value decline risk, Summit Peak purchases a **2-year put option** from **Granite Counterparty Inc.** that allows Summit Peak to sell the **200** Larkspur bonds at **$100** each. The put premium is **$500** (time value only at inception). The put is designated as a **highly effective fair value hedge**.

On **December 31, Year 1**, Larkspur bonds trade at **$88** per bond. The put’s fair value is **$2,800** (intrinsic value \([(100 - 88) \times 200 = \$2{,}400]\) plus time value **$400**).

On **January 15, Year 2**, Summit Peak **exercises** the put when bonds trade at **$85**. It delivers the bonds to Granite for **$20,000** cash under the put. Immediately before exercise, the put’s fair value equals its intrinsic value of **$3,000** \([(100 - 85) \times 200]\) (time value has decayed to zero). The HTM investment’s amortized cost remains **$20,000**; the Fair Value Adjustment—HTM balance from Dec 31 still reflects the **$2,400** decline. Update both the put and the FVA to the exercise-date values before settlement.

**Required (Case A):**  
a. Jan 1 JE for purchase of HTM bonds.  
b. Mar 1 JE for purchase of the put option.  
c. Dec 31 period-end adjusting JEs for (1) the HTM bonds and (2) the put option. Compute net income effect.  
d. **Subsequent measurement schedule** for Put Option and for Fair Value Adjustment—HTM from Mar 1 through Dec 31.  
e. Jan 15, Year 2: entries to (1) update put and FVA to exercise-date amounts, (2) settle/exercise the put and dispose of the bonds for $20,000 cash under the contract. Show that cash received and removal of net bond carrying amount and put are consistent.

#### Case B — Interest rate swap as a fair value hedge (underlying = fixed-rate liability)
**Glacier Ridge Manufacturing Co.** issues a **4-year, 6%**, **$80,000** note payable to a bank on **January 1, Year 1** (interest paid annually each Dec 31). The same day, Glacier Ridge enters an **interest rate swap** with **Oakmont Derivatives** that is **highly effective** as a fair value hedge of interest-rate risk on the note. Under the swap, Glacier Ridge **receives fixed 6%** on a notional **$80,000** and **pays the variable benchmark rate**. At inception the swap has **zero fair value** (no entry). Cash settlement of the swap coincides with the note’s interest payment date each Dec 31 (net cash = fixed interest − variable interest on the notional). Glacier Ridge uses the **shortcut method** (assume perfect effectiveness): the change in note fair value attributable to interest rates equals the change in swap fair value.

| Date | Benchmark (variable) rate for the year just ended | Fair value of swap (asset) |
|---|---:|---:|
| Jan 1, Y1 (inception) | 6.0% (at-market) | $0 |
| Dec 31, Y1 | 5.0% | 2,400 |
| Dec 31, Y2 | 5.5% | 900 |

**Required (Case B):**  
f. Jan 1 JE for issuance of the note (and state the swap entry, if any).  
g. Dec 31, Y1: (1) interest payment to the bank, (2) cash settlement of the swap, (3) FV adjustment of the swap, (4) FV adjustment of the note payable.  
h. Dec 31, Y2: same four-step sequence.  
i. **Multi-period subsequent measurement schedule** for the Interest Rate Swap Contract and Note Payable carrying amount (and net unrealized G/L each year).  
j. Effective interest expense each year (bank payment ± swap settlement).

**Answer key:**

#### Case A

**(a) Jan 1 — Purchase HTM bonds**

| Account | Debit | Credit |
|---|---:|---:|
| Investment in HTM Securities—Larkspur Bonds | 20,000 | |
| Cash (\(200 \times \$100\)) | | 20,000 |

**Check:** 20,000 = 20,000.

**(b) Mar 1 — Initial recognition of put (fair value hedge)**

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 500 | |
| Cash | | 500 |

**Check:** 500 = 500.

**(c) Dec 31, Y1 — Period-end adjusting JEs**

Decline in bond FV attributable to hedged risk:  
\((\$100 - \$88) \times 200 = \mathbf{\$2{,}400}\)

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 2,400 | |
| Fair Value Adjustment—HTM | | 2,400 |
| *Adjust hedged HTM item for change in FV of hedged risk* | | |

**Check:** 2,400 = 2,400.  
(Fair Value Adjustment—HTM is a **contra** to the investment.)

Put FV increase: \(2{,}800 - 500 = \mathbf{\$2{,}300}\)

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 2,300 | |
| Unrealized Gain or Loss—Income | | 2,300 |
| *Mark hedging put to fair value through NI* | | |

**Check:** 2,300 = 2,300.

**Net income effect (Year 1):** Unrealized loss \(2{,}400\) − Unrealized gain \(2{,}300\) = **net loss $100** (imperfect offset due to time-value decline of $100: time value fell from $500 to $400).

Carrying amounts at Dec 31, Y1:  
- HTM investment net = \(20{,}000 - 2{,}400 = \mathbf{\$17{,}600}\)  
- Put option = **$2,800**

**(d) Subsequent measurement schedule — Case A (through Dec 31, Y1)**

| Date | Put Option FV/CV | Δ Put (→ NI) | Bond unit FV | FVA—HTM (credit bal.) | Δ FVA (→ NI) | Net NI impact |
|---|---:|---:|---:|---:|---:|---:|
| Mar 1, Y1 | $500 | — | $100 | $0 | — | — |
| Dec 31, Y1 | 2,800 | +2,300 gain | 88 | 2,400 | (2,400) loss | **$(100)** |

**(e) Jan 15, Y2 — Update to exercise-date FV, then settle**

*Update put to exercise-date FV*  
New put FV = \( (100 - 85) \times 200 = \mathbf{\$3{,}000}\).  
Δ put = \(3{,}000 - 2{,}800 = \mathbf{\$200}\)

| Account | Debit | Credit |
|---|---:|---:|
| Put Option | 200 | |
| Unrealized Gain or Loss—Income | | 200 |

**Check:** 200 = 200. Put CV = **$3,000**.

*Update FVA—HTM for further decline from $88 to $85*  
Additional decline = \((88 - 85) \times 200 = \mathbf{\$600}\)

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 600 | |
| Fair Value Adjustment—HTM | | 600 |

**Check:** 600 = 600.  
FVA—HTM credit balance = \(2{,}400 + 600 = \mathbf{\$3{,}000}\).  
Net bond CV = \(20{,}000 - 3{,}000 = \mathbf{\$17{,}000}\).

*Exercise put / dispose of bonds — receive $20,000 under put; remove investment, FVA, and put*

Net assets removed: Investment 20,000 − FVA 3,000 + Put 3,000 = **$20,000**, equal to cash received.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 20,000 | |
| Fair Value Adjustment—HTM | 3,000 | |
| Investment in HTM Securities—Larkspur Bonds | | 20,000 |
| Put Option | | 3,000 |
| *Exercise fair-value-hedge put; settle bonds at strike; clear FVA and put* | | |

**Check:** Dr \(20{,}000 + 3{,}000 = \mathbf{23{,}000}\); Cr \(20{,}000 + 3{,}000 = \mathbf{23{,}000}\). **Balanced.**  
All related balances zero. Y2 NI from final FV updates: gain 200 − loss 600 = **net loss $400** (time value of put fully expired and last bond decline not fully offset in the same instant before exercise—here the put’s intrinsic captured the full $15 decline while the final period’s put FV change only +$200 after Dec 31).

*Simpler presentation of settlement economics (proof):*  
Cash under put $20,000 vs original bond cost $20,000 → economic break-even on principal via the put; remaining net losses over the life equal the put premium $500 (time value), which never recovers: Y1 net loss $100 + Y2 net loss $400 = **$500**.

#### Case B

**(f) Jan 1, Y1 — Issue note; swap at zero value**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 80,000 | |
| Note Payable | | 80,000 |

**Check:** 80,000 = 80,000.  
**Swap at inception:** FV = $0 → **no journal entry**.

**(g) Dec 31, Year 1**

Fixed interest to bank: \(80{,}000 \times 6\% = \mathbf{\$4{,}800}\).  
Variable interest on notional: \(80{,}000 \times 5\% = \mathbf{\$4{,}000}\).  
Net cash **received** on swap: \(4{,}800 - 4{,}000 = \mathbf{\$800}\).

*(1) Interest payment to bank*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,800 | |
| Cash | | 4,800 |

**Check:** 4,800 = 4,800.

*(2) Cash settlement of interest rate swap*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 800 | |
| Interest Expense | | 800 |
| *Net settlement reduces effective interest expense* | | |

**Check:** 800 = 800.  
**Effective interest expense Y1** = \(4{,}800 - 800 = \mathbf{\$4{,}000}\) (= variable rate × notional).

*(3) FV adjustment of swap* — FV asset $2,400

| Account | Debit | Credit |
|---|---:|---:|
| Interest Rate Swap Contract | 2,400 | |
| Unrealized Gain or Loss—Income | | 2,400 |

**Check:** 2,400 = 2,400.

*(4) FV adjustment of note payable (shortcut: same amount)*

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 2,400 | |
| Note Payable | | 2,400 |

**Check:** 2,400 = 2,400.  
Note payable CV = \(80{,}000 + 2{,}400 = \mathbf{\$82{,}400}\).  
**Net unrealized G/L Y1 = $0** (perfect offset under shortcut method).

**(h) Dec 31, Year 2**

Variable interest: \(80{,}000 \times 5.5\% = \mathbf{\$4{,}400}\).  
Net cash **received** on swap: \(4{,}800 - 4{,}400 = \mathbf{\$400}\).  
Swap FV falls from $2,400 to $900 → Δ = **$(1,500)**.

*(1) Interest to bank*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 4,800 | |
| Cash | | 4,800 |

**Check:** 4,800 = 4,800.

*(2) Swap cash settlement*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 400 | |
| Interest Expense | | 400 |

**Check:** 400 = 400.  
**Effective interest expense Y2** = \(4{,}800 - 400 = \mathbf{\$4{,}400}\).

*(3) FV adjustment of swap*

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—Income | 1,500 | |
| Interest Rate Swap Contract | | 1,500 |

**Check:** 1,500 = 1,500. Swap CV = \(2{,}400 - 1{,}500 = \mathbf{\$900}\).

*(4) FV adjustment of note payable*

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 1,500 | |
| Unrealized Gain or Loss—Income | | 1,500 |

**Check:** 1,500 = 1,500.  
Note CV = \(82{,}400 - 1{,}500 = \mathbf{\$80{,}900}\).  
**Net unrealized G/L Y2 = $0**.

**(i) Multi-period subsequent measurement schedule — swap and note**

| Date | Swap FV (asset) | Δ Swap → NI | Note Payable CV | Δ Note → NI | Net unrealized G/L | Swap cash settlement | Effective interest exp. |
|---|---:|---:|---:|---:|---:|---:|---:|
| Jan 1, Y1 | $0 | — | $80,000 | — | — | — | — |
| Dec 31, Y1 | 2,400 | +2,400 gain | 82,400 | +2,400 loss | **$0** | +$800 receive | **$4,000** |
| Dec 31, Y2 | 900 | (1,500) loss | 80,900 | (1,500) gain | **$0** | +$400 receive | **$4,400** |

Schedule check: Note CV always = \(80{,}000 +\) Swap FV (asset) under shortcut perfect effectiveness when rates fall and the fixed-rate liability’s FV rises.

**(j) Effective interest expense summary**

| Year | Bank cash interest | Swap settlement (receipt) | Effective interest expense |
|---|---:|---:|---:|
| Y1 | $4,800 | $800 | **$4,000** (= 5.0% × $80,000) |
| Y2 | 4,800 | 400 | **$4,400** (= 5.5% × $80,000) |

**Key insight:** Fair-value hedges mark **both** the derivative and the hedged item through **net income** so offsetting risks net near zero (Case A residual = time-value decay of the put; Case B residual = $0 under the shortcut method). Interest rate swaps also involve **periodic cash settlement** that converts fixed interest to effective variable interest. The multi-period schedule ties swap FV, note CV, net unrealized G/L, and effective interest together.

---

### Q4 — MC — Classification of derivative G/L (speculative vs cash-flow hedge)
**LO:** LO 14-11  
**Concept:** Classification — where changes in fair value of derivatives are reported (net income vs OCI) by designation  

**Question 1:**  
**Cedarvale Trading LLC** holds a call option that is **not** designated as a hedging instrument. At year-end the option’s fair value increased by $3,200. Where is the $3,200 reported?

- A) Other comprehensive income (OCI) until the option is sold, then reclassified to net income  
- B) Net income (earnings) in the period of the fair-value change  
- C) As a direct adjustment to retained earnings, never through comprehensive income  
- D) Deferred as a liability until exercise, with no income-statement effect until settlement  

**Answer:** **B.**  
Under ASC 815, the gain or loss on a derivative **not designated** as a hedging instrument is recognized **currently in earnings**. OCI treatment applies to the effective portion of **cash flow hedges** (and certain foreign-currency hedges), not to speculative derivatives.  
(A describes cash-flow-hedge deferral; C is incorrect; D ignores FV measurement of derivatives.)

**Question 2:**  
**Pinecroft Roasters Inc.** designates a **futures contract** as a **highly effective cash flow hedge** of a forecasted purchase of coffee inventory. At December 31, Year 1, the futures contract has increased in value by $500 (no excluded components). The forecasted purchase and inventory sale will occur in Year 2. How should Pinecroft report the $500 Year 1 fair-value increase?

- A) Unrealized gain in net income in Year 1  
- B) Gain in OCI in Year 1; reclassify to earnings (e.g., reduce COGS) in Year 2 when the hedged transaction affects earnings  
- C) Increase inventory cost in Year 1 before the coffee is purchased  
- D) Memo only until settlement; no balance-sheet recognition of the futures contract  

**Answer:** **B.**  
For a qualifying **cash flow hedge**, the effective change in fair value of the hedging derivative is recorded in **OCI** and later **reclassified into earnings** in the period(s) the hedged forecasted transaction affects earnings (e.g., when inventory is sold and COGS is recognized). Derivatives are still recognized on the balance sheet at fair value (not memo only). Inventory is not adjusted in Year 1 before purchase.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (schedules roll forward; Q1 NI $1,100 = 1,580 − 480; Q2 NI $1,800 = 2,550 − 750; Case A put premium $500 = cumulative net losses; Case B effective interest = variable × notional; swap Δ = note Δ under shortcut)
- [x] Core demo not sidebar-only (Demo 14-11A speculative call; Demo 14-11B put FV hedge; Demo 14-11C interest rate swap; cash-flow hedge classification per Demo 14-11D / ASC 815 — not Expanding Your Knowledge foreign-currency or effectiveness-testing sidebars)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification items)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Bold/SBC demo figures)
