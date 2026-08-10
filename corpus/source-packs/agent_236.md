# Agent 236 — CORE DEMO — LO 18-9

**Chapter:** 18  
**LO title:** Apply intraperiod tax allocation  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Intraperiod tax allocation:** allocate total income tax expense (benefit) to continuing operations, discontinued operations, and OCI (not interperiod deferred taxes)
- **Subsequent measurement schedule (emphasis):** component-by-component pretax → tax @ enacted rate → net-of-tax roll schedule that ties to payable / DTA / DTL
- **Continuing operations:** pretax × tax rate = **Income tax expense** (gross presentation)
- **Discontinued operations:** presented **net of tax** on the income statement (tax benefit or tax expense allocated to the component)
- **OCI items** (e.g., unrealized AFS debt-security gains/losses): presented **net of tax**; related deferred tax asset or liability recognized when the pretax amount is not yet taxable/deductible
- **Initial / period-end tax JE:** Dr Income tax expense (and OCI tax effect if any); Cr tax benefit—disc. ops (or Dr tax expense—disc. ops for gains); Cr Income taxes payable; Cr/Dr deferred tax for OCI
- **Disposal JE:** record sale of discontinued segment (remove net assets; recognize pretax gain/loss), then allocate tax to the discontinued component
- Simple structure assumption when stated: no permanent/temporary differences outside the facts given; taxable income = pretax GAAP income for continuing + discontinued operations

---

### Q1 — CORE — Full intraperiod allocation: schedule, statements, and period-end tax JE
**LO:** LO 18-9  
**Concept:** Subsequent measurement tax-allocation schedule by financial-statement component; income statement and SCI with net-of-tax disc. ops and OCI; period-end intraperiod tax JE  
**Scenario:**  
**Cedarline Outfitters** (calendar year-end) has a simple tax structure for Year 5: no permanent differences, no temporary differences other than those implied by the AFS unrealized holding gain (not yet recognized in taxable income), no state/foreign taxes, and no tax credits. The enacted tax rate is **25%** for all years. Taxable income equals pretax GAAP income for continuing operations plus discontinued operations.

Pretax account balances for the year ended December 31, Year 5:

| Item | Amount |
|---|---:|
| Revenues | $420,000 |
| Cost of goods sold | 210,000 |
| Operating expenses | 54,000 |
| Loss from discontinued operations (fully tax-deductible this year) | (48,000) |
| Unrealized **gain** on available-for-sale debt securities (pretax; not yet taxable) | 16,000 |

**Required:**  
a. Compute pretax income from **continuing operations**.  
b. Prepare the **intraperiod tax allocation schedule** (emphasis) showing pretax amount, tax expense (benefit) at 25%, and net-of-tax amount for continuing operations, discontinued operations, net income, OCI, and comprehensive income. Prove that current **Income taxes payable** equals tax on (continuing + discontinued) pretax.  
c. Prepare the **income statement** (through net income) and the **statement of comprehensive income** using intraperiod tax allocation.  
d. Record the **December 31, Year 5 period-end journal entry** to record income taxes with intraperiod allocation (including deferred tax on the AFS unrealized gain).  
e. In one or two sentences, explain **why** tax on continuing operations is shown gross while discontinued operations and OCI are shown net of tax.

**Answer key:**  

**a. Pretax income from continuing operations**

\[
\$420{,}000 - \$210{,}000 - \$54{,}000 = \$156{,}000
\]

**b. Intraperiod tax allocation schedule (emphasis — subsequent measurement)**

Tax rate = 25%.  
Taxable income (continuing + discontinued) = \(156{,}000 - 48{,}000 = 108{,}000\).  
Income taxes payable = \(108{,}000 \times 25\% = \$27{,}000\).  
Deferred tax liability on AFS unrealized gain = \(16{,}000 \times 25\% = \$4{,}000\).

| Component | Pretax amount | Tax exp. (benefit) @ 25% | Net of tax |
|---|---:|---:|---:|
| Income from continuing operations | 156,000 | 39,000 | 117,000 |
| Loss from discontinued operations | (48,000) | (12,000) | (36,000) |
| **Net income** | **108,000** | **27,000** | **81,000** |
| OCI — unrealized gain on AFS debt securities | 16,000 | 4,000 | 12,000 |
| **Comprehensive income** | **124,000** | **31,000** | **93,000** |

**Schedule checks:**  
- Tax on continuing: \(156{,}000 \times 0.25 = 39{,}000\).  
- Tax benefit on disc. ops: \(48{,}000 \times 0.25 = 12{,}000\).  
- Net current tax on NI components: \(39{,}000 - 12{,}000 = 27{,}000\) = payable.  
- OCI tax: \(16{,}000 \times 0.25 = 4{,}000\) → DTL (gain not yet taxable).  
- Net income: \(117{,}000 - 36{,}000 = 81{,}000\).  
- Comprehensive income: \(81{,}000 + 12{,}000 = 93{,}000\).

**c. Income statement and statement of comprehensive income**

**Cedarline Outfitters**  
**Income Statement**  
**For the Year Ended December 31, Year 5**

| | Amount |
|---|---:|
| Revenues | $420,000 |
| Cost of goods sold | 210,000 |
| Gross margin | 210,000 |
| Operating expenses | 54,000 |
| Income from continuing operations before income tax | 156,000 |
| Income tax expense (\(156{,}000 \times 25\%\)) | 39,000 |
| Income from continuing operations | 117,000 |
| Discontinued operations | |
| Loss from discontinued operations, net of tax (\(48{,}000 \times 75\%\)) | (36,000) |
| **Net income** | **$81,000** |

**Cedarline Outfitters**  
**Statement of Comprehensive Income**  
**For the Year Ended December 31, Year 5**

| | Amount |
|---|---:|
| Net income | $81,000 |
| Other comprehensive income | |
| Unrealized gain on AFS debt securities, net of tax (\(16{,}000 \times 75\%\)) | 12,000 |
| **Comprehensive income** | **$93,000** |

**d. Period-end adjusting JE — intraperiod tax allocation**

*December 31, Year 5 — Record income taxes with intraperiod allocation*

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 39,000 | |
| Income Tax Expense—OCI (unrealized AFS gain) | 4,000 | |
| Income Tax Benefit—Discontinued Operations | | 12,000 |
| Income Taxes Payable | | 27,000 |
| Deferred Tax Liability | | 4,000 |
| *Allocate tax to continuing ops, disc. ops, and OCI; record current payable and DTL on AFS gain* | | |

**Check:** Dr \(39{,}000 + 4{,}000 = 43{,}000\); Cr \(12{,}000 + 27{,}000 + 4{,}000 = 43{,}000\). **Balanced.**

(Equivalently, the $4,000 OCI tax effect may be closed/presented as a reduction of pretax OCI so OCI is reported net of tax; the deferred tax liability still equals $4,000.)

**e. Presentation rationale**  
Intraperiod tax allocation matches the tax consequence with the financial-statement component that generated it. Continuing operations show tax expense **gross** as a separate line; discontinued operations and OCI are reported **net of tax** so users see after-tax performance of those components.

**Key insight:** Build the **allocation schedule first** (pretax × rate by component). Payable is tax only on components that enter **taxable income** this period (continuing + disc. ops). OCI tax typically hits **deferred tax** (AFS holding gains/losses), not current payable.

---

### Q2 — CORE number variant — Different company, rate, and signs
**LO:** LO 18-9  
**Concept:** Number-variant twin: intraperiod tax allocation schedule; IS/SCI; period-end JE with disc. ops **gain** and OCI **loss**  
**Scenario:**  
**Northfork Analytics** (calendar year) reports the following pretax amounts for Year 3. Enacted tax rate is **21%**. Taxable income equals pretax GAAP income for continuing operations plus discontinued operations. The unrealized AFS loss is not yet deductible for tax (creates a deferred tax asset). No other temporary or permanent differences.

| Item | Amount |
|---|---:|
| Income from continuing operations before tax | $520,000 |
| Gain from discontinued operations (pretax; fully taxable this year) | 80,000 |
| Unrealized **loss** on available-for-sale debt securities (pretax) | (30,000) |

**Required:**  
a. Prepare the **intraperiod tax allocation schedule** (emphasis) for continuing operations, discontinued operations, net income, OCI, and comprehensive income.  
b. Prepare the income statement (from pretax continuing through net income) and the statement of comprehensive income.  
c. Record the December 31, Year 3 journal entry for income taxes with intraperiod allocation.  
d. Prove: Income taxes payable + deferred tax asset (from OCI) reconciles to net tax related to all components.

**Answer key:**  

**a. Allocation schedule (emphasis)**

Taxable income = \(520{,}000 + 80{,}000 = 600{,}000\).  
Income taxes payable = \(600{,}000 \times 21\% = \$126{,}000\).  
DTA on unrealized AFS loss = \(30{,}000 \times 21\% = \$6{,}300\).

| Component | Pretax amount | Tax exp. (benefit) @ 21% | Net of tax |
|---|---:|---:|---:|
| Income from continuing operations | 520,000 | 109,200 | 410,800 |
| Gain from discontinued operations | 80,000 | 16,800 | 63,200 |
| **Net income** | **600,000** | **126,000** | **474,000** |
| OCI — unrealized loss on AFS debt securities | (30,000) | (6,300) | (23,700) |
| **Comprehensive income** | **570,000** | **119,700** | **450,300** |

**Checks:**  
- Cont. tax: \(520{,}000 \times 0.21 = 109{,}200\).  
- Disc. tax: \(80{,}000 \times 0.21 = 16{,}800\).  
- NI tax total: \(109{,}200 + 16{,}800 = 126{,}000\) = payable.  
- OCI tax benefit: \(30{,}000 \times 0.21 = 6{,}300\).  
- Net income: \(410{,}800 + 63{,}200 = 474{,}000\).  
- Comprehensive income: \(474{,}000 - 23{,}700 = 450{,}300\).

**b. Statements**

**Northfork Analytics — Income Statement (partial), Year 3**

| | Amount |
|---|---:|
| Income from continuing operations before income tax | $520,000 |
| Income tax expense | 109,200 |
| Income from continuing operations | 410,800 |
| Discontinued operations | |
| Gain from discontinued operations, net of tax (\(80{,}000 \times 79\%\)) | 63,200 |
| **Net income** | **$474,000** |

**Northfork Analytics — Statement of Comprehensive Income, Year 3**

| | Amount |
|---|---:|
| Net income | $474,000 |
| Other comprehensive income (loss) | |
| Unrealized loss on AFS debt securities, net of tax (\(30{,}000 \times 79\%\)) | (23,700) |
| **Comprehensive income** | **$450,300** |

**c. Period-end JE**

*December 31, Year 3*

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 109,200 | |
| Income Tax Expense—Discontinued Operations | 16,800 | |
| Deferred Tax Asset | 6,300 | |
| Income Taxes Payable | | 126,000 |
| Income Tax Benefit—OCI (unrealized AFS loss) | | 6,300 |
| *Allocate tax to continuing, disc. ops gain, and OCI loss; record payable and DTA* | | |

**Check:** Dr \(109{,}200 + 16{,}800 + 6{,}300 = 132{,}300\); Cr \(126{,}000 + 6{,}300 = 132{,}300\). **Balanced.**

**d. Payable / deferred reconciliation**

| Item | Amount |
|---|---:|
| Income taxes payable (current) | 126,000 |
| Less: Deferred tax asset (OCI loss) | (6,300) |
| Net tax related to NI + OCI components | **119,700** |

Matches schedule total tax on comprehensive income components: \(109{,}200 + 16{,}800 - 6{,}300 = 119{,}700\).

**Key insight:** A **gain** on discontinued operations **increases** tax allocated to that component (expense, not benefit). An OCI **loss** creates a **DTA** and a tax **benefit** netted in OCI—not a reduction of current taxes payable when the loss is not yet deductible.

---

### Q3 — CORE alternate angle — Disposal of discontinued segment + tax allocation JE
**LO:** LO 18-9  
**Concept:** Disposal (settlement) JE for discontinued operations; intraperiod tax allocation schedule; period-end tax JE when disc. ops is a net pretax gain  
**Scenario:**  
**Harborstone Media** (calendar year) decides in Year 2 to exit its print-catalog product line, which qualifies as a **discontinued operation**. On **October 1, Year 2**, it sells the product line’s net assets for cash.

| Fact | Amount |
|---|---:|
| Carrying amount of net assets sold (Oct 1) | $85,000 |
| Cash proceeds | 110,000 |
| Operating loss of the discontinued product line, Jan 1–Oct 1 (pretax; tax-deductible) | (10,000) |
| Pretax income from **continuing** operations for Year 2 | 200,000 |
| Enacted tax rate | 25% |
| Other comprehensive income | none |
| Temporary/permanent differences | none (taxable income = pretax GAAP income for continuing + discontinued) |

The company has already recorded the Year 2 operating results of the discontinued line in a “Loss from discontinued operations” account. Record the disposal and year-end tax allocation.

**Required:**  
a. Record the **October 1, Year 2 disposal journal entry** for the sale of the discontinued product line.  
b. Compute total pretax income (loss) from **discontinued operations** for Year 2 (operations + disposal).  
c. Prepare the **intraperiod tax allocation schedule** for continuing operations, discontinued operations, and net income.  
d. Record the **December 31, Year 2 period-end tax journal entry** with intraperiod allocation.  
e. Show the discontinued operations section of the income statement (net of tax) and net income.

**Answer key:**  

**a. Disposal JE (settlement of discontinued segment)**

Pretax gain on disposal = \(110{,}000 - 85{,}000 = \$25{,}000\).

*October 1, Year 2 — Sell discontinued product line*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 110,000 | |
| Net Assets of Discontinued Operation (or detail: AR, Inv, PPE, etc.) | | 85,000 |
| Gain on Disposal of Discontinued Operation | | 25,000 |
| *Record sale of discontinued product line* | | |

**Check:** Dr 110,000 = Cr \(85{,}000 + 25{,}000\). **Balanced.**

**b. Pretax discontinued operations total**

| Component | Pretax |
|---|---:|
| Operating loss through disposal date | (10,000) |
| Gain on disposal | 25,000 |
| **Total pretax income from discontinued operations** | **15,000** |

**c. Intraperiod tax allocation schedule (emphasis)**

Taxable income = \(200{,}000 + 15{,}000 = 215{,}000\).  
Income taxes payable = \(215{,}000 \times 25\% = \$53{,}750\).

| Component | Pretax amount | Tax exp. (benefit) @ 25% | Net of tax |
|---|---:|---:|---:|
| Income from continuing operations | 200,000 | 50,000 | 150,000 |
| Income from discontinued operations | 15,000 | 3,750 | 11,250 |
| **Net income** | **215,000** | **53,750** | **161,250** |

**Checks:** \(200{,}000 \times 0.25 = 50{,}000\); \(15{,}000 \times 0.25 = 3{,}750\); \(50{,}000 + 3{,}750 = 53{,}750\).

**d. Period-end tax JE**

*December 31, Year 2*

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 50,000 | |
| Income Tax Expense—Discontinued Operations | 3,750 | |
| Income Taxes Payable | | 53,750 |
| *Allocate tax between continuing and discontinued operations* | | |

**Check:** Dr \(50{,}000 + 3{,}750 = 53{,}750\) = Cr. **Balanced.**

**e. Income statement presentation (partial)**

| | Amount |
|---|---:|
| Income from continuing operations before income tax | $200,000 |
| Income tax expense | 50,000 |
| Income from continuing operations | 150,000 |
| Discontinued operations | |
| Income from discontinued operations, net of tax (\(15{,}000 \times 75\%\)) | 11,250 |
| **Net income** | **$161,250** |

(Optional detail disclosure: pretax disc. ops $15,000 less tax $3,750.)

**Key insight:** **Disposal** of a discontinued component creates a pretax gain/loss that is **combined** with the segment’s operating results for the period; intraperiod allocation taxes the **combined** disc. ops pretax amount and reports the **net-of-tax** total in the discontinued operations section—not inside continuing operations.

---

### Q4 — MC — Scope of intraperiod tax allocation
**LO:** LO 18-9  
**Concept:** Classification — which financial-statement components require intraperiod tax allocation  
**Question:**  
Under U.S. GAAP (as illustrated for LO 18-9), **intraperiod tax allocation** primarily requires allocation of income tax expense (benefit) among which of the following?

- A) Current tax payable versus deferred tax asset/liability only  
- B) Federal tax versus state tax jurisdictions only  
- C) Income (loss) from continuing operations, income (loss) from discontinued operations, and items of other comprehensive income  
- D) Temporary differences originating this year versus temporary differences reversing this year  

**Answer:** **C.**  
Intraperiod tax allocation assigns tax expense (benefit) to different **within-period** financial-statement components—continuing operations, discontinued operations, and OCI (net of tax). Choice A describes the **current vs. deferred** split of the tax provision (related to interperiod allocation / temporary differences). Choice B is jurisdictional, not intraperiod. Choice D is the temporary-difference rollforward, not component allocation.

---

### Q5 — MC — Compute net-of-tax discontinued operations
**LO:** LO 18-9  
**Concept:** Measurement of discontinued operations presented net of tax  
**Question:**  
Pinevault Corp. reports pretax income from continuing operations of $300,000 and a pretax **loss** from discontinued operations of $40,000. The tax rate is 25%. Taxable income equals pretax GAAP income. What amount of **loss from discontinued operations** is reported on the income statement (net of tax), and what is **net income**?

- A) Disc. ops loss $40,000; net income $195,000  
- B) Disc. ops loss $30,000; net income $195,000  
- C) Disc. ops loss $30,000; net income $220,000  
- D) Disc. ops loss $10,000; net income $260,000  

**Answer:** **B.**  
Tax benefit on disc. ops = \(40{,}000 \times 25\% = 10{,}000\); net disc. ops loss = \(40{,}000 - 10{,}000 = \$30{,}000\) (or \(40{,}000 \times 75\%\)).  
Tax on continuing = \(300{,}000 \times 25\% = 75{,}000\); income from continuing = \(300{,}000 - 75{,}000 = 225{,}000\).  
Net income = \(225{,}000 - 30{,}000 = \$195{,}000\).  
(Alternatively: pretax total \(260{,}000 \times 75\% = 195{,}000\).)  
A fails to net tax on disc. ops. C miscomputes NI. D confuses the tax benefit with the net loss.

---

### Self-check
- [x] Every JE balances (Q1 tax JE; Q2 tax JE; Q3 disposal + tax JE)
- [x] Math recomputed (all pretax × rates; payable = tax on taxable components; NI and CI roll)
- [x] Core demo not sidebar-only (Demo 18-9 / Review 18-9 / AppBE18 path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition / period-end tax JE; subsequent measurement allocation schedule (emphasis); disposal/settlement of discontinued ops; presentation classification MC
