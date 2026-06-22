# Test Scenarios — Business Data Analysis & Insights (Idea 67)

## Core Scenarios (Quality Gates)

### Scenario 1 — Revenue dip diagnosis
- **Input:** Monthly revenue table showing Q2 dip ($100K→$85K from March to April)
- **Context:** No known promotions; Easter in April
- **Expected outputs:**
  1. Requirements gatherer frames question measurably
  2. KPI tree built: Revenue = Traffic × Conversion × AOV
  3. Decomposition identifies which driver shifted
  4. Seasonality check applied (April vs March YoY)
  5. Method cited (driver decomposition, sequential comparison)
  6. Evidence shown (actual numbers, contribution %)
  7. Confidence stated (sample size, interval)
  8. Plain-language insight generated
  9. Action ties to specific driver identified
- **Pass criteria:** All above met; driver isolated; seasonal adjustment applied; method + evidence cited; action tied to finding

### Scenario 2 — Product profit Pareto
- **Input:** SKU-level sales & margin data (500 SKUs)
- **Expected outputs:**
  1. Pareto analysis performed
  2. Concentration calculated (what % of SKUs contribute what % of profit)
  3. Pareto index computed (>3 = strong concentration)
  4. ABC classification (A/B/C classes)
  5. Insight on concentration level
  6. Action to focus on top SKUs or rationalize long tail
  7. Chart recommendation (Pareto chart)
  8. Method cited (Pareto analysis)
  9. Sample size adequate (n=500)
- **Pass criteria:** Pareto analysis complete; concentration quantified; action ties to finding; method + evidence cited

### Scenario 3 — Churn cohort trend
- **Input:** Monthly cohort retention table (12 cohorts, 12 months each)
- **Expected outputs:**
  1. Cohort analysis method cited
  2. Retention rates calculated for each cohort
  3. Trend identified (improving/worsening/stable)
  4. Sample size noted (cohort sizes)
  5. Confidence intervals for retention estimates
  6. Churn rates calculated
  7. LTV estimation if applicable
  8. Insight on retention pattern
  9. Action recommendations (e.g., focus on early retention)
  10. Chart recommendation (cohort heatmap or line)
- **Pass criteria:** Cohort method used; sample noted; confidence stated; trend identified; action tied to finding

### Scenario 4 — Spurious correlation guard
- **Input:** Ice-cream sales correlate strongly (r=0.85) with website signups
- **Context:** Both rise in summer months
- **Expected outputs:**
  1. Correlation detected and quantified
  2. Quality reviewer invoked
  3. Temporal precedence tested (or flagged)
  4. Mechanism questioned (no plausible link)
  5. Seasonal confounder identified (summer drives both)
  6. Causal claim downgraded to correlation
  7. Finding adjusted to "associated with" not "causes"
  8. Caveat documented in validity log
  9. Recommendation not to act on causal assumption
- **Pass criteria:** Causal overreach prevented; downgraded to correlation; confounder identified; caveat documented

### Scenario 5 — Small-sample caution
- **Input:** 12 data points showing upward trend; claim of "strong growth"
- **Expected outputs:**
  1. Sample size flagged (n=12, below recommended 30)
  2. Confidence interval wide (reflecting uncertainty)
  3. Finding labeled low-confidence
  4. Trend acknowledged but qualified
  5. Recommendation to gather more data
  6. Caveat prominently stated
  7. No strong causal claims made
- **Pass criteria:** Sample-size flag prominent; cautious framing; wide CI shown; low confidence stated

### Scenario 6 — Offline / degraded mode
- **Input:** Dataset provided; WebSearch unavailable
- **Expected outputs:**
  1. Analysis proceeds using SECOND-KNOWLEDGE-BRAIN.md
  2. Internal benchmarks used (if applicable)
  3. Offline limitation flagged in output
  4. Currency of benchmarks not guaranteed (stated)
  5. All other analysis steps performed normally
  6. Methods applied correctly
  7. Findings still validated for statistical soundness
- **Pass criteria:** Offline limitation stated; internal knowledge used; analysis otherwise complete

## Edge Cases & Boundary Conditions

### Scenario 7 — Simpson's paradox detection
- **Input:** Aggregate conversion rate increased (2.0%→2.5%); but all segments declined
- **Context:** Mobile traffic share increased from 30%→60%; mobile has lower base conversion
- **Expected outputs:**
  1. Aggregate trend reported (2.0%→2.5%)
  2. Segment analysis shows contradictory trend
  3. Composition shift identified (mobile share increase)
  4. Simpson's paradox flagged
  5. Correct insight: Conversion down across segments; aggregate misleading
  6. Action tied to improving conversion, not celebrating aggregate
  7. Validity log documents paradox test
- **Pass criteria:** Paradox detected; segment-level reported; correct interpretation; aggregate flag

### Scenario 8 — Base effect exaggeration
- **Input:** New product showing "300% growth" (1→4 units)
- **Context:** Mature product showing "5% growth" (1000→1050 units)
- **Expected outputs:**
  1. Both growth rates calculated
  2. Absolute change reported (new: +3; mature: +50)
  3. Base effect flagged (small base exaggerates rate)
  4. Context provided (volume vs rate)
  5. Insight focuses on absolute impact, not just rate
  6. Action considers both rate and volume
- **Pass criteria:** Base effect flagged; absolute change shown; context provided; no over-interpretation of rate

### Scenario 9 — Multiple comparisons correction
- **Input:** Testing 10 traffic sources for conversion differences
- **Expected outputs:**
  1. Multiple tests identified (10 pairwise comparisons)
  2. Bonferroni correction applied (α = 0.05/10 = 0.005)
  3. Significance re-evaluated with corrected threshold
  4. Some findings may lose significance after correction
  5. Validity log documents correction
  6. Only corrected significant findings claimed
- **Pass criteria:** Multiple comparisons detected; correction applied; significance re-evaluated; findings adjusted

### Scenario 10 — Incomplete data handling
- **Input:** Revenue table with 20% missing days (randomly distributed)
- **Expected outputs:**
  1. Data completeness assessed (80% complete)
  2. Missingness pattern analyzed (random vs systematic)
  3. Impact on confidence noted (reduced precision)
  4. Analysis proceeds with caveats
  5. Confidence intervals widened
  6. Limitation documented
  7. Caution in interpretation
- **Pass criteria:** Completeness quantified; impact assessed; caveat documented; confidence adjusted

## Sector-Specific Scenarios

### Scenario 11 — E-commerce seasonal inventory
- **Sector:** E-commerce / Retail
- **Input:** Monthly inventory and sales data; Q4 spike
- **Context:** Holiday season准备
- **Expected outputs:**
  1. Seasonality adjustment applied
  2. YoY comparison used (Q4 vs Q4 prior year)
  3. Inventory turnover calculated
  4. Seasonal indices documented
  5. Stockout risk assessed
  6. Action on inventory timing
- **Pass criteria:** Seasonality handled; YoY used; inventory metrics calculated; seasonal insight

### Scenario 12 — SaaS churn analysis
- **Sector:** SaaS / Subscription
- **Input:** Monthly subscription data; churn fluctuating 5-12%
- **Context:** Competitive pricing changes during period
- **Expected outputs:**
  1. Cohort analysis by signup month
  2. Churn rate calculated and trended
  3. Correlation with pricing events tested
  4. LTV impact quantified
  5. Net revenue retention calculated
  6. Action on retention strategies
- **Pass criteria:** Cohort analysis; churn calculated; LTV estimated; pricing correlation tested

### Scenario 13 — Manufacturing yield optimization
- **Sector:** Manufacturing / B2B
- **Input:** Daily production yield data; 85-95% range
- **Context:** New equipment introduced mid-period
- **Expected outputs:**
  1. Before/after comparison (equipment change)
  2. Statistical significance tested (t-test)
  3. Yield improvement quantified
  4. Confidence intervals provided
  5. Causality assessment (equipment → yield?)
  6. Action on scaling or process refinement
- **Pass criteria:** Before/after analysis; significance tested; causality assessed; action tied

### Scenario 14 — Restaurant margin analysis
- **Sector:** Restaurant / Hospitality
- **Input:** Menu item sales and cost data
- **Context:** Some items high-volume/low-margin; others low-volume/high-margin
- **Expected outputs:**
  1. Margin calculated by item
  2. Volume vs margin matrix produced
  1. Stars (high vol/high margin) identified
  4. Plowhorses (high vol/low margin) flagged
  5. Puzzles (low vol/high margin) evaluated
  6. Dogs (low vol/low margin) considered for removal
  7. Action on menu optimization
- **Pass criteria:** Menu engineering performed; categories identified; action on optimization

## Statistical Validity Scenarios

### Scenario 15 — Non-normal distribution handling
- **Input:** Skewed order value distribution (median $25, mean $45)
- **Expected outputs:**
  1. Distribution characteristics identified (non-normal)
  2. Appropriate statistics selected (median vs mean)
  3. Non-parametric tests considered if needed
  4. Outliers handled appropriately
  5. Both median and mean reported for context
  6. Insight based on appropriate central tendency
- **Pass criteria:** Distribution assessed; appropriate stats used; outliers handled

### Scenario 16 — Outlier impact assessment
- **Input:** 100 data points; 1 extreme value (10× others)
- **Expected outputs:**
  1. Outlier detected (statistical test or visualization)
  2. Impact assessed (with vs without outlier)
  3. Sensitivity analysis performed
  4. Decision made (exclude/downgrade/report both)
  5. Justification documented
  6. Finding qualifies impact of outlier
- **Pass criteria:** Outlier detected; impact assessed; decision justified; finding qualified

### Scenario 17 — Trend vs noise discrimination
- **Input:** Metric fluctuating randomly; no real trend
- **Expected outputs:**
  1. Statistical trend test performed (Mann-Kendall or similar)
  2. Significance assessed (p-value reported)
  3. Variance decomposed (signal vs noise)
  4. If not significant: finding states "no clear trend"
  5. Confidence intervals shown overlap
  6. Action recommendation to monitor rather than intervene
- **Pass criteria:** Trend test performed; significance reported; no false trend claimed

## Integration Scenarios

### Scenario 18 — End-to-end revenue analysis
- **Input:** Complete business case: monthly revenue, traffic, orders, product mix
- **Context:** Multi-stage decline over 6 months
- **Expected outputs:**
  1. All sub-skills invoked in sequence
  2. Requirements: clear brief with KPI tree
  3. Research: benchmarks retrieved
  4. Analysis: comprehensive findings (trend, drivers, segments)
  5. Quality: all validity checks performed
  6. Roadmap: prioritized actions with measurement plan
  7. Output follows format specification
  8. All quality gates passed
- **Pass criteria:** Complete workflow; all skills used; all gates passed; output per spec

### Scenario 19 — Multi-metric dashboard request
- **Input:** "How's the business doing?" with access to full data warehouse
- **Expected outputs:**
  1. Clarifying questions asked (what to focus on?)
  2. If unclear: request prioritization or analyze key metrics
  3. KPI trees built for multiple metrics
  4. Synthesized view across metrics
  5. Prioritized insights
  6. Holistic action recommendations
- **Pass criteria:** Question refined; multiple KPIs analyzed; synthesis provided

### Scenario 20 — What-if analysis request
- **Input:** "What if we increase ad spend by 20%?"
- **Expected outputs:**
  1. Historical relationship analyzed (ad spend vs. revenue)
  2. Correlation quantified
  3. Causality carefully assessed (or flagged as uncertain)
  4. Scenario modeled with confidence intervals
  5. Limitations stated (past may not predict future)
  6. Recommendation qualified
- **Pass criteria:** Relationship analyzed; causality careful; scenario modeled; limitations stated

## Failure Mode Scenarios

### Scenario 21 — Ambiguous question
- **Input:** "Fix the sales problem"
- **Expected outputs:**
  1. Question recognized as ambiguous
  2. Clarifying questions asked:
      - What metric? (Revenue, volume, margin?)
      - What period? (Recent drop vs long-term decline?)
      - What baseline? (Target, last year, budget?)
  3. Examples provided of how question could be framed
  4. Analysis does not proceed without clarification
- **Pass criteria:** Ambiguity detected; clarifying questions asked; no guessing

### Scenario 22 — No data provided
- **Input:** "Why did revenue drop?" (no data)
- **Expected outputs:**
  1. Data absence identified
  2. Specific data requested (revenue by what period? what granularity?)
  3. Alternative approaches suggested (if some context available)
  4. Analysis blocked until data provided
- **Pass criteria:** Data absence flagged; specific request made; analysis blocked

### Scenario 23 — Contradictory data
- **Input:** Two data sources show opposite trends
- **Expected outputs:**
  1. Contradiction identified
  2. Sources compared (definitions, scope, collection methods)
  3. Reconciliation attempted
  4. If unreconcilable: both presented with caveats
  5. Finding states uncertainty
  6. Recommendation to verify sources
- **Pass criteria:** Contradiction detected; reconciliation attempted; both presented if needed

## Test Execution Guidelines

### Coverage Requirements
- All 23 scenarios must be documented
- Each scenario must specify inputs, expected outputs, and pass criteria
- Scenarios cover: core functionality, edge cases, sectors, statistics, integration, failures

### Execution Protocol
1. Run scenario through complete workflow
2. Collect actual outputs
3. Compare against expected outputs
4. Verify all pass criteria met
5. Document any deviations
6. Flag scenarios that fail for remediation

### Regression Testing
- Re-run all scenarios after any code changes
- Ensure no regression (previously passing scenarios now failing)
- Track scenario pass rate over time
- Target: 100% scenario pass rate

### Scenario Maintenance
- Add new scenarios as edge cases discovered
- Update scenarios as business requirements evolve
- Retire scenarios that no longer apply
- Document rationale for scenario changes
