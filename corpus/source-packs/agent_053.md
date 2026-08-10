# Agent 53 — CORE DEMO — LO 9-6

**Chapter:** 9  
**LO title:** Explain and compute a LIFO reserve  
**Critical gap LO:** no

## Concept list for this pack
- LIFO reserve = inventory at internal method (FIFO/avg/standard) − inventory at LIFO
- **Initial recognition JE** (first year): create Allowance to Reduce Inventory to LIFO Basis; Dr COGS for full reserve
- **Subsequent measurement schedule**: multi-year rollforward of FIFO, LIFO, reserve, and Δ reserve
- **Period-end adjusting JE**: adjust allowance only for the *change* in the reserve
- **Settlement / reverse adjustment** when reserve decreases (Dr Allowance, Cr COGS)
- **Classification / presentation**: Inventory net of contra allowance on the balance sheet; note disclosure of LIFO reserve for comparability
- Outside-the-books conversion: compute reserve for external reporting without formal JE

---

### Q1 — CORE — Cedarvale Hardware: create LIFO reserve, multi-year schedule, period-end adjust, reverse when reserve falls
**LO:** LO 9-6  
**Concept:** Initial recognition of LIFO reserve (Allowance to Reduce Inventory to LIFO Basis); subsequent period-end adjustments for Δ reserve; BS presentation  
**Scenario:**  
**Cedarvale Hardware Co.** maintains **FIFO** inventory records for internal control and uses **LIFO** for external financial reporting and income tax. Year 1 is the company’s first year of operations. Year-end is **December 31**. Conversion to LIFO is **recognized in the accounts** via an allowance (contra-inventory) account.

Inventory valuations at each year-end:

| Date | Ending inventory at FIFO | Ending inventory at LIFO |
|---|---:|---:|
| Dec 31, Year 1 | $45,000 | $32,000 |
| Dec 31, Year 2 | 52,000 | 36,000 |
| Dec 31, Year 3 | 48,000 | 38,000 |

**Required:**  
a. Compute the **LIFO reserve** at each year-end and the **change in LIFO reserve** for Years 1–3. Prepare a **subsequent measurement schedule** (FIFO EI, LIFO EI, LIFO reserve, Δ reserve, effect on COGS).  
b. Prepare the **December 31, Year 1** journal entry to **create** the LIFO allowance (**initial recognition emphasis**).  
c. Prepare the **period-end adjusting entries** on December 31, Year 2 and December 31, Year 3 to adjust the LIFO reserve.  
d. Illustrate how **Inventory** is presented on the comparative balance sheets at December 31, Year 2 and Year 3 (show FIFO, allowance, and net LIFO).  
e. For Year 3 only, state the income-statement effect of the LIFO reserve adjustment (increase or decrease COGS, amount).

**Answer key:**  

**a. LIFO reserve computation and subsequent measurement schedule**

Formula: **LIFO reserve = FIFO inventory − LIFO inventory**

| Date | FIFO EI | LIFO EI | LIFO reserve | Δ reserve (current − prior) | Effect on COGS |
|---|---:|---:|---:|---:|---|
| Dec 31, Y1 | $45,000 | $32,000 | **$13,000** | +13,000 (create) | Increase COGS $13,000 |
| Dec 31, Y2 | 52,000 | 36,000 | **16,000** | +3,000 | Increase COGS $3,000 |
| Dec 31, Y3 | 48,000 | 38,000 | **10,000** | −6,000 | Decrease COGS $6,000 |

Checks:  
- Y1: 45,000 − 32,000 = **13,000**  
- Y2: 52,000 − 36,000 = **16,000**; Δ = 16,000 − 13,000 = **+3,000**  
- Y3: 48,000 − 38,000 = **10,000**; Δ = 10,000 − 16,000 = **−6,000**

**Allowance T-account (credit balance):**

| | Allowance to Reduce Inventory to LIFO Basis | |
|---:|---|---:|
| | | 13,000 (Y1 create) |
| | | 3,000 (Y2 increase) |
| Y3 decrease 6,000 | | |
| | **Bal. after Y3: 10,000 Cr** | |

**b. December 31, Year 1 — Initial recognition (create LIFO allowance)**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 13,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 13,000 |
| *Create year-end LIFO reserve: FIFO $45,000 − LIFO $32,000* | | |

**Check:** Dr = Cr = **13,000**. Balanced.

**c. Period-end adjusting entries — Years 2 and 3**

*December 31, Year 2 — Increase in LIFO reserve*

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 3,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 3,000 |
| *Adjust allowance for Δ reserve: $16,000 − $13,000 = $3,000* | | |

**Check:** Dr = Cr = **3,000**. Balanced. Allowance balance after entry = 13,000 + 3,000 = **$16,000**.

*December 31, Year 3 — Decrease in LIFO reserve (partial reverse / settlement of prior build-up)*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to LIFO Basis | 6,000 | |
| Cost of Goods Sold | | 6,000 |
| *Adjust allowance for Δ reserve: $10,000 − $16,000 = $(6,000)* | | |

**Check:** Dr = Cr = **6,000**. Balanced. Allowance balance after entry = 16,000 − 6,000 = **$10,000**.

**d. Comparative balance-sheet presentation (inventory section)**

| | Dec 31, Year 2 | Dec 31, Year 3 |
|---|---:|---:|
| Inventory (at FIFO) | $52,000 | $48,000 |
| Less: Allowance to Reduce Inventory to LIFO Basis | (16,000) | (10,000) |
| **Inventory, net (at LIFO)** | **$36,000** | **$38,000** |

(Alternatively, companies may report a single line “Inventory (LIFO)” of $36,000 / $38,000 and disclose the LIFO reserve in the notes.)

**e. Year 3 income-statement effect**  
The Year 3 adjustment **decreases Cost of Goods Sold by $6,000** (credit to COGS), increasing pretax income by $6,000 relative to leaving the allowance unadjusted.

**Key insight:** The LIFO reserve is the **full** FIFO−LIFO gap; the **journal entry each year books only the change** in that gap (except Year 1, when the full reserve is first recognized). An increase in the reserve raises COGS; a decrease lowers COGS. Net inventory on the balance sheet always equals LIFO cost when the allowance is kept current.

---

### Q2 — CORE number variant — Northfork Merchandising: LIFO reserve twin
**LO:** LO 9-6  
**Concept:** Number-variant twin — create LIFO reserve, multi-year Δ-reserve schedule, period-end JEs, and BS net presentation  
**Scenario:**  
**Northfork Merchandising LLC** uses **average cost** for internal records and converts to **LIFO** at year-end for external reporting. Year 1 is the first year of operations. Adjustments are recognized **in the accounts**.

| Date | Ending inventory at average cost | Ending inventory at LIFO |
|---|---:|---:|
| Dec 31, Year 1 | $90,000 | $55,000 |
| Dec 31, Year 2 | 105,000 | 62,000 |
| Dec 31, Year 3 | 98,000 | 70,000 |

**Required:**  
a. Compute LIFO reserve each year and Δ reserve; prepare the measurement schedule.  
b. Journal entry December 31, Year 1 (create allowance).  
c. Journal entries December 31, Year 2 and Year 3.  
d. Show Inventory on the Dec 31, Year 3 balance sheet (gross internal method, allowance, net LIFO).  
e. Compute cumulative effect on COGS over Years 1–3 from LIFO reserve entries (net Dr or Cr to COGS).

**Answer key:**  

**a. Schedule**

LIFO reserve = internal (average) inventory − LIFO inventory

| Date | Avg-cost EI | LIFO EI | LIFO reserve | Δ reserve | Effect on COGS |
|---|---:|---:|---:|---:|---|
| Dec 31, Y1 | $90,000 | $55,000 | **$35,000** | +35,000 | +COGS $35,000 |
| Dec 31, Y2 | 105,000 | 62,000 | **43,000** | +8,000 | +COGS $8,000 |
| Dec 31, Y3 | 98,000 | 70,000 | **28,000** | −15,000 | −COGS $15,000 |

Checks:  
- Y1: 90,000 − 55,000 = **35,000**  
- Y2: 105,000 − 62,000 = **43,000**; Δ = 43,000 − 35,000 = **+8,000**  
- Y3: 98,000 − 70,000 = **28,000**; Δ = 28,000 − 43,000 = **−15,000**

**b. December 31, Year 1 — Create allowance**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 35,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 35,000 |
| *Initial LIFO reserve: $90,000 − $55,000* | | |

**Check:** Dr = Cr = **35,000**.

**c. Subsequent period-end adjustments**

*December 31, Year 2*

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 8,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 8,000 |
| *Δ reserve +$8,000* | | |

**Check:** Dr = Cr = **8,000**. Allowance bal. = 35,000 + 8,000 = **$43,000**.

*December 31, Year 3*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to LIFO Basis | 15,000 | |
| Cost of Goods Sold | | 15,000 |
| *Δ reserve −$15,000* | | |

**Check:** Dr = Cr = **15,000**. Allowance bal. = 43,000 − 15,000 = **$28,000**.

**d. Balance sheet — December 31, Year 3**

| | Amount |
|---|---:|
| Inventory (at average cost) | $98,000 |
| Less: Allowance to Reduce Inventory to LIFO Basis | (28,000) |
| **Inventory, net (at LIFO)** | **$70,000** |

**e. Cumulative COGS effect (Years 1–3)**  
Net debit to COGS = 35,000 + 8,000 − 15,000 = **$28,000**  
(Equals ending LIFO reserve of $28,000 — the cumulative amount by which COGS has been increased relative to the internal method.)

**Key insight:** Regardless of whether the internal method is FIFO or average cost, the mechanics are the same: **reserve = internal EI − LIFO EI**; book **only Δ reserve** after Year 1. Ending allowance always equals the current-year reserve, and cumulative COGS charges equal the ending reserve balance.

---

### Q3 — CORE alternate angle — Ridgeway Industrial: period-end only + disclosure vs in-accounts conversion
**LO:** LO 9-6  
**Concept:** Period-end LIFO reserve adjustment from given beginning allowance; classification/presentation; outside-the-books disclosure alternative  
**Scenario:**  
**Ridgeway Industrial Supply Inc.** uses FIFO internally and LIFO externally. At **January 1, Year 5**, the balance in **Allowance to Reduce Inventory to LIFO Basis** is a credit of **$72,000** (equal to the LIFO reserve at the end of Year 4).

At **December 31, Year 5**, inventory is:

| Valuation basis | Amount |
|---|---:|
| FIFO | $410,000 |
| LIFO | 325,000 |

Management is evaluating two reporting approaches for Year 5:  
**(1) In the accounts** — adjust the allowance at year-end.  
**(2) Outside the accounts** — leave books on FIFO; compute LIFO amounts only for external statements and notes (no formal JE).

**Required:**  
a. Compute the **LIFO reserve at December 31, Year 5** and the **required adjustment** to the allowance (Δ reserve).  
b. Prepare the **December 31, Year 5 period-end adjusting JE** under approach (1).  
c. Under approach (1), show the **balance-sheet classification** of inventory at December 31, Year 5.  
d. Under approach (2), state: (i) whether a formal JE is made; (ii) the inventory amount reported on the LIFO-basis balance sheet; (iii) the **LIFO reserve amount disclosed** in the notes for comparability with FIFO peers; (iv) FIFO inventory that analysts would reconstruct.  
e. Assume that in **Year 6** LIFO inventory rises to **$360,000** while FIFO inventory is **$400,000**. Prepare the Year 6 period-end JE under approach (1) (beginning allowance = ending Year 5 reserve).

**Answer key:**  

**a. Reserve and Δ**  
LIFO reserve, Dec 31, Y5 = 410,000 − 325,000 = **$85,000**  
Beginning allowance (Y4 ending reserve) = **$72,000**  
Δ reserve = 85,000 − 72,000 = **+$13,000** (increase → debit COGS)

**b. December 31, Year 5 — Period-end adjusting JE (in the accounts)**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 13,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 13,000 |
| *Increase LIFO reserve from $72,000 to $85,000* | | |

**Check:** Dr = Cr = **13,000**. Ending allowance = 72,000 + 13,000 = **$85,000**.

**c. Balance-sheet classification (approach 1)**

| Current assets | Amount |
|---|---:|
| Inventory (FIFO) | $410,000 |
| Less: Allowance to Reduce Inventory to LIFO Basis | (85,000) |
| **Inventory (LIFO basis)** | **$325,000** |

The allowance is a **contra-inventory** (valuation) account — not a liability.

**d. Outside-the-accounts conversion (approach 2)**  
(i) **No formal journal entry** is recorded for the LIFO reserve.  
(ii) External balance sheet reports inventory at LIFO: **$325,000**.  
(iii) Note disclosure of LIFO reserve: **$85,000** (so users can add it back for FIFO comparability).  
(iv) Reconstructed FIFO inventory = LIFO inventory + disclosed reserve = 325,000 + 85,000 = **$410,000**.

**e. December 31, Year 6 — Period-end JE**

LIFO reserve Y6 = 400,000 − 360,000 = **$40,000**  
Beginning allowance = **$85,000**  
Δ reserve = 40,000 − 85,000 = **−$45,000**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to LIFO Basis | 45,000 | |
| Cost of Goods Sold | | 45,000 |
| *Decrease LIFO reserve from $85,000 to $40,000* | | |

**Check:** Dr = Cr = **45,000**. Ending allowance = 85,000 − 45,000 = **$40,000**.

**Key insight:** Whether conversion is booked or done off-books, users need the **LIFO reserve** for cross-company comparability. When booked, only the **change** hits COGS; the balance sheet always nets to LIFO. A shrinking reserve (as in Y6) **credits** COGS — the reverse of the initial recognition entry.

---

### Q4 — MC — Classification and measurement of the LIFO reserve
**LO:** LO 9-6  
**Concept:** Classification of the LIFO allowance and which amount adjusts COGS each period  

**Question:**  
Sable Creek Co. keeps inventory on FIFO for internal purposes and reports LIFO externally. At the end of Year 4 the LIFO reserve (credit balance in Allowance to Reduce Inventory to LIFO Basis) is **$40,000**. At the end of Year 5, FIFO ending inventory is **$210,000** and LIFO ending inventory is **$165,000**. Sable Creek records the conversion **in the accounts**. Which statement is **correct**?

- A) Year 5 LIFO reserve is $45,000; the Year 5 adjusting entry debits Allowance $5,000 and credits COGS $5,000.  
- B) Year 5 LIFO reserve is $45,000; the Year 5 adjusting entry debits COGS $45,000 and credits Allowance $45,000.  
- C) Year 5 LIFO reserve is $45,000; the Year 5 adjusting entry debits COGS $5,000 and credits Allowance $5,000; the allowance is a contra-inventory account.  
- D) Year 5 LIFO reserve is $165,000; Inventory is reported at $210,000 with no allowance because LIFO is used only for tax.

**Answer:** **C.**  
Year 5 LIFO reserve = 210,000 − 165,000 = **$45,000**.  
Δ reserve = 45,000 − 40,000 = **+$5,000** → Dr COGS $5,000 / Cr Allowance $5,000 (only the change, not the full reserve).  
The allowance is a **contra account to inventory**, not a liability.  
A reverses the direction of the entry. B incorrectly books the full ending reserve instead of the change. D misstates the reserve amount and the reporting presentation.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (all reserves, Δ reserves, allowance rollforwards, cumulative COGS)
- [x] Core demo not sidebar-only (Demo 9-6 / Review 9-6 path: compute reserve, create/adjust allowance, present inventory)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC on classification/method)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (reserve decrease reverse), classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not Erie/Boynton textbook figures)
