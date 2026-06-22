---
name: sub-requirements-gatherer
description: Frame the business question, capture the data and KPIs, and build a KPI tree before analysis.
---

## Purpose
Turn a vague ask into an analyzable question with clear metrics, available data, and a structured approach.

## Inputs
- Business question (the ask)
- Data source (tables, figures, file paths, or description)
- Relevant KPIs (if known)
- Time period (if specified)
- Known context (promotions, seasonality, special events)

## Process

### Step 1: Question Framing
Transform vague questions into measurable ones.

**Patterns:**

| Vague | Measurable |
|-------|------------|
| "Why did sales drop?" | "Why did total revenue decrease from $X to $Y between Month A and Month B?" |
| "Which products are best?" | "Which products contributed the most to gross profit in Period X?" |
| "Is churn bad?" | "What is the monthly churn rate for customer cohort acquired in Month X, and how does it compare to benchmark?" |
| "Should I invest in marketing?" | "What is the customer acquisition cost by channel, and which channel yields the highest LTV:CAC ratio?" |

**Question elements to capture:**
- Metric: What exactly is being measured?
- Comparison: What baseline or target exists?
- Period: What time frame?
- Segmentation: By product, channel, region, customer type?

### Step 2: Build KPI/Driver Tree
Decompose the target metric into drivers.

**Template:**
```
Target Metric (Level 0)
├── Driver 1 (Level 1)
│   ├── Sub-driver A (Level 2)
│   └── Sub-driver B (Level 2)
├── Driver 2 (Level 1)
│   ├── Sub-driver C (Level 2)
│   └── Sub-driver D (Level 2)
└── Driver 3 (Level 1)
    └── Sub-driver E (Level 2)
```

**Example: Revenue Decomposition**
```
Revenue
├── Traffic (Sessions)
│   ├── Organic search
│   ├── Paid advertising
│   ├── Direct
│   └── Referral
├── Conversion Rate
│   ├── Add-to-cart rate
│   └── Checkout completion rate
└── Average Order Value (AOV)
    ├── Units per transaction
    └── Price per unit
```

**Validation questions:**
- Do the drivers multiply to the target?
- Is each driver measurable with available data?
- Are there missing drivers that could explain variance?

### Step 3: Data Inventory
Catalog available data sources and quality.

**Inventory Template:**

| Data Element | Granularity | Period | Completeness | Source | Notes |
|--------------|-------------|--------|--------------|--------|-------|
| Revenue | Daily | 2024-01-01 to 2024-06-15 | 100% | SQL table revenue | No missing dates |
| Orders | Transactional | 2024-01-01 to present | 99.8% | SQL table orders | 0.2% failed status |
| Website Traffic | Daily | 2024-01-01 to present | 95% | Google Analytics | Some days missing |
| Product Catalog | SKU-level | Current | 100% | Product DB | Updated weekly |

**Completeness assessment:**
- 100%: Complete for analysis
- 80-99%: Usable with caveats
- <80%: Limited reliability; flag in findings
- Unknown: Requires investigation

### Step 4: Context Capture
Document factors that could affect interpretation.

**Context checklist:**
- Promotions or campaigns during period
- Seasonality patterns (holiday, quarterly)
- Pricing changes
- Product launches or discontinuations
- Market events (competitor actions, economic shifts)
- Data collection changes (GA4 migration, tracking updates)

## Outputs

**Analysis Brief Structure:**
```
{
  "question": "Measurable restatement of the business question",
  "target_metric": "The primary KPI to analyze",
  "kpi_tree": {
    "level_0": "Target metric",
    "level_1": ["Driver 1", "Driver 2", "Driver 3"],
    "level_2": ["Sub-driver 1a", "Sub-driver 1b", ...]
  },
  "data_inventory": {
    "available": ["Data element 1", "Data element 2", ...],
    "missing": ["Data element X", "Data element Y"],
    "quality_assessment": "Overall data quality rating"
  },
  "period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD",
    "type": "comparison/continuous/snapshot"
  },
  "context": {
    "known_factors": ["Factor 1", "Factor 2"],
    "seasonality": "Expected seasonal pattern",
    "promotions": ["Campaign A: dates, expected impact"]
  },
  "blocking_issues": ["Issue preventing analysis", ...] or []
}
```

## Quality Gates

### Gate 1: Question Definition
- [ ] Question stated in measurable terms
- [ ] Target metric identified
- [ ] Comparison baseline defined
- [ ] Time period specified

### Gate 2: Data Availability
- [ ] Primary data sources identified
- [ ] Data completeness assessed
- [ ] Missing data documented
- [ ] Data quality flagged if concerning

### Gate 3: KPI Tree Validity
- [ ] Target metric decomposed into drivers
- [ ] Driver relationships mathematically sound
- [ ] Each driver traceable to available data
- [ ] Tree depth sufficient for diagnosis (≥2 levels)

## Block Conditions

**Block analysis and ask user for clarification when:**
- Question is ambiguous (multiple interpretations)
- No data source provided or specified
- Target metric not defined
- Time period unclear
- Data completeness <50% without acknowledgment

**Proceed with caution (flag in output) when:**
- Data completeness 50-80%
- Granularity mismatch (daily data vs. monthly question)
- Period <4 weeks for trend analysis
- Sample size <30 observations

## Example: Complete Analysis Brief

```
Question: "Why did e-commerce revenue decrease 15% in April 2024 compared to March 2024?"
Target metric: Total revenue (USD)
KPI tree: Revenue = Traffic × Conversion Rate × AOV
Data inventory: 
  - Revenue: Daily, 100% complete, SQL source
  - Traffic: Daily, 95% complete, Google Analytics
  - Orders: Transactional, 99% complete, SQL source
Period: March 1-31, 2024 vs. April 1-30, 2024
Context: 
  - Easter fell in April 2024 vs. March 2023
  - No major promotions in either month
  - No pricing changes
  - No new product launches
Blocking issues: []
```
