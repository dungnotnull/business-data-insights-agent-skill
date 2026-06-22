---
name: sub-scoring-engine
description: Analyze business data with trend/variance/cohort/Pareto methods, producing method-anchored findings.
---

## Purpose
Produce reliable, statistically-sound findings tied to specific analytical methods and evidence, with confidence intervals clearly stated.

## Inputs
Analysis brief from sub-requirements-gatherer, including:
- Measurable question
- KPI tree structure
- Data inventory
- Period and context

## Dimensions & Weights
| Dimension | Weight | Method | Output |
|-----------|--------|--------|--------|
| Trend & seasonality | 25% | time-series, YoY, moving average | Trend direction, seasonal pattern |
| Driver decomposition | 25% | KPI tree, variance analysis | Which driver caused change |
| Segmentation & concentration | 20% | cohort, Pareto, ABC analysis | High-value segments |
| Statistical validity | 20% | confidence intervals, significance | Confidence level, p-value |
| Communication clarity | 10% | data storytelling | Plain-language framing |

## Process

### Step 1: Trend & Seasonality Analysis

**Time-series decomposition:**
```
Value = Trend + Seasonality + Residual
```

**Methods:**

1. **Year-over-Year (YoY) Comparison**
   - Formula: YoY % = (Current period - Same period last year) / Same period last year × 100
   - Use when: Comparing same seasonal period across years
   - Example: April 2024 vs. April 2023

2. **Sequential Growth**
   - Formula: Growth % = (Current period - Previous period) / Previous period × 100
   - Use when: Assessing immediate momentum
   - Example: April 2024 vs. March 2024

3. **Moving Average**
   - Simple Moving Average (SMA): Average of last N periods
   - Formula: SMA = (X₁ + X₂ + ... + Xₙ) / n
   - Use when: Smoothing noisy data

4. **Seasonal Adjustment**
   - Identify seasonal pattern (calculate seasonal indices)
   - Formula: Seasonally adjusted = Actual / Seasonal index
   - Example: If December sales are typically 1.5× average, divide December actual by 1.5

**Output structure:**
```
Finding: "Revenue declined 15% in April vs. March"
Method: Sequential comparison
Evidence: April: $85,000; March: $100,000; Change: -$15,000 (-15%)
Confidence: High (n=62 days, SD=$8,000, CI ±$2,200 at 95%)
Seasonality: Noted (April typically 3% lower than March historically)
```

### Step 2: Driver Decomposition (KPI Tree Analysis)

**Multiplicative decomposition:**
```
Revenue = Traffic × Conversion Rate × AOV
```

**Decomposition formulas:**
- Traffic contribution: ΔTraffic × Base ConvRate × Base AOV
- Conversion contribution: Base Traffic × ΔConvRate × Base AOV
- AOV contribution: Base Traffic × Base ConvRate × ΔAOV

**Example calculation:**
```
Period 1 (March): Traffic=10,000; Conv=2.5%; AOV=$40 → Revenue=$10,000
Period 2 (April): Traffic=8,500; Conv=2.5%; AOV=$40 → Revenue=$8,500

Change: -$1,500 (-15%)

Driver analysis:
- Traffic effect: (8,500-10,000) × 0.025 × $40 = -$1,500
- Conversion effect: 10,000 × (0.025-0.025) × $40 = $0
- AOV effect: 10,000 × 0.025 × ($40-$40) = $0

Conclusion: Entire 15% decline driven by traffic drop; conversion and AOV flat.
```

**Variance analysis (for budget vs. actual):**
```
Total Variance = Actual Revenue - Budgeted Revenue
Price Variance = (Actual Price - Budget Price) × Actual Quantity
Volume Variance = (Actual Quantity - Budget Quantity) × Budget Price
Mix Variance = Interaction effect (when product mix shifts)
```

**Output structure:**
```
Finding: "Revenue decline entirely driven by traffic decrease"
Method: KPI tree driver decomposition
Evidence: 
  - Traffic dropped 15% (10,000→8,500 sessions)
  - Conversion flat at 2.5%
  - AOV flat at $40
  - Traffic contribution: -$1,500 (100% of variance)
Confidence: High (complete data, n=62 days, SD traffic=$1,200)
```

### Step 3: Segmentation & Concentration Analysis

**Cohort Analysis:**

**Retention calculation:**
```
Retention Rate = (Customers active in month N / Customers in cohort) × 100
Churn Rate = 100 - Retention Rate
```

**Cohort table structure:**
```
          Month 0   Month 1   Month 2   Month 3   Month 4
Jan '24   1,000      700       550       480       450
Feb '24   1,200      850       680       590       —
Retention            70%       70%       71%       87%
```

**Lifetime Value (LTV) calculation:**
```
LTV = Average Revenue per Customer × Average Customer Lifespan
LTV = ARPU × (1 / Churn Rate)  (for subscription)
```

**Pareto / ABC Analysis:**

1. Sort items by value descending
2. Calculate cumulative value % and cumulative item %
3. Classify:
   - A class: Top 20% of items contributing ~80% of value
   - B class: Next 30% of items contributing ~15% of value
   - C class: Remaining 50% of items contributing ~5% of value

**Pareto index:**
```
Pareto Index = (Cumulative Value % / Cumulative Item %)
If Index > 4: Strong Pareto effect (80/20 or stronger)
If Index = 4: Perfect 80/20 distribution
If Index < 4: Weaker concentration
```

**Output structure:**
```
Finding: "Top 20% of SKUs generate 78% of gross profit (strong Pareto effect)"
Method: Pareto analysis (ABC classification)
Evidence:
  - Total SKUs: 500
  - Top 100 SKUs (A class): 78% of GP, $780,000
  - Next 150 SKUs (B class): 17% of GP, $170,000
  - Bottom 250 SKUs (C class): 5% of GP, $50,000
  - Pareto Index: 3.9 (strong concentration)
Confidence: High (complete SKU-level data, n=500)
```

### Step 4: Statistical Validity Assessment

**Confidence Interval calculation:**
```
CI = Mean ± (Z × (SD / √n))

Where:
  Z = 1.96 for 95% confidence
  SD = Standard deviation
  n = Sample size
```

**Sample size adequacy:**
- n ≥ 500: Excellent precision
- n ≥ 100: Good precision
- n ≥ 50: Adequate for most analyses
- n ≥ 30: Minimum for parametric tests
- n < 30: Limited; flag as low-confidence

**Statistical significance tests:**

1. **t-test (comparing two means)**
   - Use when: Comparing average values between two groups
   - Output: t-statistic, p-value
   - Interpretation: p < 0.05 = statistically significant

2. **Chi-square test (categorical associations)**
   - Use when: Testing if two categorical variables are related
   - Output: χ² statistic, p-value
   - Example: Is conversion rate different between traffic sources?

3. **ANOVA (comparing multiple means)**
   - Use when: Comparing averages across three or more groups
   - Output: F-statistic, p-value
   - Example: Do AOVs differ across regions?

**Correlation analysis:**
```
Pearson correlation (r) for continuous variables:
  r = covariance(X,Y) / (SD_X × SD_Y)
  Range: -1 to +1
  
Coefficient of determination (R²):
  R² = r² (proportion of variance explained)
```

**Output structure:**
```
Finding: "Email traffic shows significantly higher conversion than paid search (p<0.01)"
Method: Statistical significance test (two-sample t-test)
Evidence:
  - Email: 4.2% conversion (n=5,000 sessions)
  - Paid search: 2.8% conversion (n=8,000 sessions)
  - Difference: 1.4 percentage points
  - t-statistic: 8.3, p-value: <0.001
  - 95% CI for difference: [1.1%, 1.7%]
Confidence: Very high (large sample, statistically significant)
```

### Step 5: Communication & Storytelling

**Findings framing:**
1. Lead with the key insight
2. Support with evidence
3. State confidence level
4. Note limitations or caveats

**Chart recommendations:**
- Trend over time: Line chart
- Comparing categories: Bar chart
- Part-to-whole: Pie or donut chart
- Distribution: Histogram
- Relationship: Scatter plot
- Geographic: Map

## Outputs

**Findings list structure:**
```
[
  {
    "finding": "Plain-language statement of what was discovered",
    "method": "Specific analytical method used",
    "evidence": {
      "key_metrics": ["Value 1", "Value 2", ...],
      "calculations": "Brief description of calculation",
      "supporting_numbers": {"label": "value"}
    },
    "confidence": {
      "level": "High/Medium/Low",
      "sample_size": n,
      "interval": "Confidence interval if applicable",
      "notes": "Any limitations affecting confidence"
    },
    "chart_recommendation": "Type of chart that best visualizes this finding",
    "actionability": "How this finding could inform a decision"
  }
]
```

## Quality Gates

### Gate 1: Method Citation
- [ ] Each finding names the specific analytical method
- [ ] Method is appropriate for the data type
- [ ] Formula or calculation logic documented

### Gate 2: Evidence Support
- [ ] Key metrics stated with actual values
- [ ] Sample size or data volume specified
- [ ] Comparison baseline identified

### Gate 3: Confidence Stated
- [ ] Confidence level (High/Medium/Low) specified
- [ ] Sample size adequate for method used
- [ ] Statistical test performed if comparing groups
- [ ] Confidence interval provided for estimates

### Gate 4: Communication
- [ ] Finding stated in plain language
- [ ] Technical jargon explained
- [ ] Chart type recommended

## Block Conditions

**Flag findings as low-confidence when:**
- Sample size < 30 observations
- Data completeness < 80%
- Time period < 4 weeks for trend analysis
- High variability (coefficient of variation > 50%)
- Multiple comparisons without correction

**Do not claim statistical significance when:**
- p-value ≥ 0.05
- Sample size insufficient
- Test assumptions violated

## Example: Complete Finding Set

```
Finding 1: "Revenue declined 15% in April due entirely to 15% traffic drop"
  Method: KPI tree driver decomposition
  Evidence: Traffic 10,000→8,500; Conversion 2.5%→2.5%; AOV $40→$40
  Confidence: High (complete data, n=62 days)
  Chart: Stacked waterfall chart showing revenue components

Finding 2: "Top 20% of products (100 SKUs) generate 78% of gross profit"
  Method: Pareto analysis
  Evidence: A class $780K GP; B class $170K GP; C class $50K GP
  Confidence: High (complete SKU data, n=500)
  Chart: Pareto chart with cumulative line

Finding 3: "Email converts 50% better than paid search (4.2% vs 2.8%, p<0.001)"
  Method: Two-sample t-test
  Evidence: Email n=5K, Paid n=8K, t=8.3, p<0.001
  Confidence: Very high (large sample, highly significant)
  Chart: Bar chart comparing conversion rates with confidence intervals
```
