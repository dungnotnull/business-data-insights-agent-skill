# SECOND-KNOWLEDGE-BRAIN.md — Business Data Analysis & Insights (Idea 67)

Grown weekly by `tools/knowledge_updater.py`.

## Core Concepts & Frameworks

### KPI Tree / Driver Tree
Decompose a top metric into drivers to localize change.

**Structure:** Revenue = Traffic × Conversion Rate × AOV (Average Order Value)
- Traffic = Sessions or unique visitors
- Conversion Rate = Orders / Traffic
- AOV = Revenue / Orders

**Three-level breakdown:**
1. Level 1: Revenue, Profit, Customer Count
2. Level 2: Drivers that directly affect Level 1
3. Level 3: Underlying levers (e.g., Traffic = Organic + Paid + Direct)

**Use case:** When revenue drops 15%, identify which driver shifted.

**Formula:** Contribution % = (Driver change × Driver weight) / Total change

### Descriptive → Diagnostic → Predictive Ladder
- **Descriptive:** What happened? (Revenue dropped 15% in Q2)
- **Diagnostic:** Why did it happen? (Traffic fell 22%; conversion stayed flat)
- **Predictive:** What will happen? (If trend continues, Q3 will be 12% lower)

### Variance / Contribution Analysis
Attribute changes to specific segments, products, or periods.

**Two-way decomposition:**
- Volume effect: (New quantity - Old quantity) × Old price
- Price effect: (New price - Old price) × New quantity
- Interaction effect: (New quantity - Old quantity) × (New price - Old price)

**Formula:** Variance = Actual - Budget = Price variance + Volume variance + Mix variance

### Cohort Analysis
Track groups over time to understand retention, churn, and lifetime value.

**Metrics:**
- Retention rate: % of cohort still active after N periods
- Churn rate: % of cohort that left
- Lifetime value (LTV): Average revenue per customer over their lifetime

**Period types:** Calendar month, Fiscal quarter, Customer tenure month

**Formula:** Retention = (Active at end / Active at start) × 100%

### Pareto Analysis (80/20 Rule)
Identify concentration of value in few items or customers.

**Calculation:**
1. Sort items by value descending
2. Calculate cumulative % of items and % of total value
3. Identify Pareto frontier (typically top 20% of items contribute 80% of value)

**Use case:** Focus optimization on top 20% of SKUs that generate 80% of margin.

### Statistical Validity
**Sample size rules:**
- Minimum n ≥ 30 for parametric tests
- Minimum n ≥ 100 for stable trend analysis
- Confidence interval: Mean ± (Z × SD / √n)
  - Z = 1.96 for 95% confidence
  - SD = standard deviation
  - n = sample size

**Correlation ≠ Causation:**
- Correlation coefficient (r): -1 to +1
- R² = proportion of variance explained
- Causation requires: temporal precedence, strength, consistency, mechanism, ruling out confounders

**Simpson's Paradox:** A trend appears in groups but disappears or reverses when groups are combined. Always check segment-level trends.

**Seasonality & Base Effects:**
- Year-over-year (YoY): Compare same period across years
- Sequential vs. seasonal: Is the pattern due to time or season?
- Base effect: Growth from a small base appears exaggerated

**Statistical tests:**
- t-test: Compare means of two groups
- Chi-square: Test association between categorical variables
- ANOVA: Compare means across three+ groups
- Regression: Quantify relationships between variables

### Data Storytelling (Knaflic)
**Principles:**
1. One message per chart
2. Use plain language, avoid jargon
3. Lead with the key takeaway
4. Use color strategically (highlight the insight, not everything)
5. Remove chart clutter (gridlines, borders, unnecessary labels)

**Chart selection:**
- Trends over time: Line chart
- Comparisons: Bar chart
- Parts of whole: Pie chart (if ≤5 categories)
- Distribution: Histogram
- Relationships: Scatter plot
- Geospatial: Map

## Analysis Dimensions (this skill)
| Dimension | Weight | Method | Key Output |
|-----------|--------|--------|-------------|
| Trend & seasonality | 25% | time-series, base effects, YoY | Trend direction, seasonal pattern |
| Driver decomposition | 25% | KPI tree, variance | Which driver caused change |
| Segmentation & concentration | 20% | cohort, Pareto | High-value segments |
| Statistical validity | 20% | sample/confidence, causation | Confidence level, causation strength |
| Communication clarity | 10% | data storytelling | Plain-language insights |

## Sector-Specific KPI Benchmarks

### E-commerce & Retail
| Metric | Typical Range | Source | Context |
|--------|--------------|--------|---------|
| Conversion rate | 2-4% | Industry standard | Varies by traffic source |
| Average order value | $45-150 | Segment dependent | Fashion lower, electronics higher |
| Customer acquisition cost | $15-150 | Channel dependent | Email lower, Paid search higher |
| Customer lifetime value | $100-500 | Segment dependent | Repeat purchasers higher |
| Return rate | 10-30% | Category dependent | Apparel higher, electronics lower |
| Gross margin | 25-50% | Category dependent | Luxury higher, commodity lower |
| Inventory turnover | 4-12×/year | Category dependent | Fast fashion higher |

### SaaS / Subscription
| Metric | Typical Range | Source | Context |
|--------|--------------|--------|---------|
| Monthly recurring revenue growth | 10-30% YoY | Industry standard | Early-stage higher |
| Churn rate | 5-10% monthly | Industry standard | Enterprise lower, SMB higher |
| Customer lifetime value | $500-5000 | Segment dependent | Enterprise higher |
| Customer acquisition cost | $200-2000 | Segment dependent | Self-serve lower, enterprise higher |
| Free to paid conversion | 3-8% | Industry standard | Depends on trial quality |
| Net revenue retention | 90-120% | Industry standard | >100% = expansion exceeds churn |
| Average revenue per user | $50-500 | Segment dependent | Enterprise higher |

### Manufacturing / B2B
| Metric | Typical Range | Source | Context |
|--------|--------------|--------|---------|
| Gross margin | 20-40% | Industry standard | Varies by commoditization |
| Inventory turnover | 4-8×/year | Industry standard | Just-in-time higher |
| Days sales outstanding | 30-60 days | Industry standard | Net-30 terms typical |
| On-time delivery rate | 85-95% | Industry standard | Varies by complexity |
| Production yield | 85-98% | Industry standard | Varies by process complexity |

### Restaurants / Hospitality
| Metric | Typical Range | Source | Context |
|--------|--------------|--------|---------|
| Food cost percentage | 28-35% | Industry standard | Fine dining lower |
| Labor cost percentage | 25-35% | Industry standard | Full-service higher |
| Table turnover rate | 1.5-3×/meal | Concept dependent | Quick-service higher |
| Average ticket size | $15-60 | Concept dependent | Fine dining higher |
| Customer retention | 40-70% | Industry standard | Varies by loyalty program |

## Key Research / Sources
| Title | Source | Year | Link | Relevance |
|-------|--------|------|------|-----------|
| Storytelling with Data | Knaflic | 2015 | — | Communication |
| Business analytics methods | SSRN | 2022 | ssrn.com | Method rigor |
| Lean Analytics | Croll & Yoskovitz | 2013 | — | Startup metrics |
| Advanced Analytics Methodologies | HBR | 2024 | hbr.org | Current methods |

## Authoritative Data Sources
Statistics/analytics literature, industry KPI benchmark reports, SSRN business analytics, HBR Analytics, McKinsey Insights, Gartner Metrics.

## Analytical Frameworks
KPI/driver tree · Variance analysis · Cohort · Pareto · Statistical validity · Data storytelling · Seasonality adjustment · Confidence intervals.

## Self-Update Protocol
- Queries: "business analytics method 2026", "KPI benchmark report", "data storytelling", "cohort analysis business", "statistical significance small sample", "Simpson's paradox business"
- Sources: SSRN, analytics literature, benchmarks, HBR, McKinsey. Frequency: weekly.
- Append: `- [DATE] Title — Source — finding — URL <!--h:hash-->`. Dedupe by hash.

## Knowledge Update Log
- [2026-06-18] Seed entry — methods documented.
- [2026-06-22] Enhanced with calculation formulas, sector KPI benchmarks, statistical tests, and detailed method explanations.
