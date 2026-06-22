---
name: sub-improvement-roadmap
description: Convert validated findings into plain-language insights and concrete actions tied to each finding, with clear prioritization and measurement plans.
---

## Purpose
Transform analytical findings into actionable business intelligence that non-technical stakeholders can understand and execute.

## Inputs
- Validated findings from sub-quality-reviewer
- Validity log (method limitations, sample caveats)
- Original business question
- Analysis brief context

## Process

### Step 1: Translate Findings to Insights

**Insight formula:**
```
[Key Discovery] → [What it means] → [Why it matters]

Example: "Traffic dropped 15% in April → This explains the entire revenue decline → 
Focus on recovering traffic rather than optimizing conversion."
```

**Plain-language rules:**
1. Avoid jargon (say "customers" not "user acquisition")
2. Use active voice (not "was observed to have declined")
3. Lead with the "so what"
4. One message per insight
5. Tie back to the original question

**Chart recommendation framework:**

| Insight type | Best chart | Example |
|-------------|-----------|---------|
| Trend over time | Line chart | Revenue by month |
| Comparing values | Bar chart | Conversion by channel |
| Part-to-whole | Pie/donut chart | Revenue by category |
| Distribution | Histogram | Order value distribution |
| Relationship | Scatter plot | Ad spend vs. revenue |
| Change drivers | Waterfall | Revenue bridge from March to April |
| Concentration | Pareto | Top products by profit |
| Ranking | Horizontal bar | Top 10 SKUs |

**Insight structure:**
```
Insight: "Traffic dropped 15% in April, causing the entire revenue decline"
Chart: Line chart showing daily traffic March-April with April dip highlighted
Takeaway: "The decline isn't about conversion or pricing—it's about getting people to the site"
```

### Step 2: Develop Concrete Actions

**Action formula:**
```
[Verb] + [Specific target] + [To achieve] + [Expected outcome]

Example: "Launch retargeting campaign for visitors who viewed but didn't purchase 
to recover 5% of lost traffic, expecting ~$25,000 monthly revenue recovery."
```

**Action categories:**

1. **Immediate (0-30 days)**
   - Quick wins
   - Low effort, clear impact
   - Examples: Fix broken tracking, pause underperforming ads, send email campaign

2. **Short-term (1-3 months)**
   - Process improvements
   - Medium effort, moderate impact
   - Examples: A/B test landing page, optimize checkout flow, launch referral program

3. **Medium-term (3-6 months)**
   - Structural changes
   - Higher effort, sustained impact
   - Examples: Revamp pricing strategy, enter new market, rebuild customer journey

4. **Long-term (6+ months)**
   - Strategic initiatives
   - High effort, transformative impact
   - Examples: Platform migration, new product line, market expansion

**Action detail template:**
```
Action: [Clear description of what to do]
Owner: [Who should execute (role/team)]
Effort: [Low/Medium/High]
Timeframe: [Expected completion]
Impact: [Quantified expected outcome]
Cost: [Estimated cost if applicable]
Risk: [What could go wrong]
Finding: [Which validated finding this addresses]
```

### Step 3: Prioritize by Impact-to-Effort

**Impact/Effort Matrix:**

```
        │ Low Impact    │ High Impact
────────┼────────────────┼────────────────
High    │ Do last       │ Do first
Effort  │ (Quadrant 4)  │ (Quadrant 1)
────────┼────────────────┼────────────────
Low     │ Do next       │ Quick wins
Effort  │ (Quadrant 3)  │ (Quadrant 2)
```

**Prioritization criteria:**

**Impact score (1-5):**
- 5: Direct impact on primary KPI, >10% improvement
- 4: Clear impact on primary KPI, 5-10% improvement
- 3: Moderate impact, 2-5% improvement
- 2: Minor impact, <2% improvement
- 1: Indirect or uncertain impact

**Effort score (1-5):**
- 1: <1 day, minimal resources
- 2: 1-3 days, existing resources
- 3: 1-2 weeks, some coordination
- 4: 2-4 weeks, significant coordination
- 5: >1 month, major project

**Priority formula:**
```
Priority Score = Impact Score / Effort Score

Ranking:
  Score ≥ 3: High priority (Quadrants 1 & 2)
  Score 1-3: Medium priority (Quadrant 3)
  Score < 1: Low priority (Quadrant 4)
```

### Step 4: Define Success Metrics

**Measurement framework:**

For each action, define:
1. **Leading indicator:** What changes immediately (e.g., click rate, sign-ups)
2. **Lagging indicator:** What ultimately matters (e.g., revenue, profit)
3. **Target value:** What constitutes success
4. **Measurement frequency:** How often to check
5. **Time to result:** When to expect impact

**Example:**
```
Action: Launch email retargeting campaign
Leading indicator: Email open rate, click-through rate
Lagging indicator: Recovered traffic, recovered revenue
Target: 5% traffic recovery, $25,000 monthly revenue
Frequency: Weekly
Time to result: 4 weeks to see stabilized effect
```

## Outputs

**Structured output format:**

```
# Insights

## Insight 1
**Summary:** [One-sentence key takeaway]
**Chart:** [Chart type and what it shows]
**Detail:** [2-3 sentences explaining the finding and implications]
**Finding source:** [Links back to validated finding]

# Recommended Actions

## Priority 1 (Do First - High Impact, Low/Medium Effort)
### Action 1.1
**Description:** [What to do]
**Impact:** [Expected outcome]
**Effort:** [Time and resources]
**Owner:** [Who executes]
**Metrics:** [How to measure success]
**Timeline:** [When to expect results]
**Addresses:** [Finding 1]

## Priority 2 (Quick Wins - High Impact, Low Effort)
[... similar structure ...]

## Priority 3 (Do Next - Medium Impact/Effort)
[... similar structure ...]

## Priority 4 (Do Last - Low Impact, High Effort)
[... similar structure ...]

# Measurement Plan

| Action | Metric | Target | Frequency | Owner | Status |
|--------|--------|--------|-----------|-------|--------|
| Action 1.1 | Recovered traffic | +5% | Weekly | Marketing | Not started |
| Action 1.2 | Conversion rate | +0.5% | Monthly | Product | Not started |

# Risks & Considerations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Seasonality distorts comparison | Medium | High | Use YoY comparison |
| Data quality issues | Low | Medium | Validate with source |
| Competitor reaction | Medium | Medium | Monitor competitive intelligence
```

## Quality Gates

### Gate 1: Insight Quality
- [ ] Each insight derived from a validated finding
- [ ] Plain language without technical jargon
- [ ] Clear "so what" articulated
- [ ] Appropriate chart type recommended

### Gate 2: Action Specificity
- [ ] Each action tied to a specific finding
- [ ] Action described with concrete verb and target
- [ ] Expected outcome quantified
- [ ] Owner/role identified
- [ ] Effort level assessed

### Gate 3: Prioritization Logic
- [ ] Impact score justified (1-5)
- [ ] Effort score justified (1-5)
- [ ] Priority score calculated
- [ ] Actions ranked by priority
- [ ] Quick wins identified separately

### Gate 4: Measurement Defined
- [ ] Success metric specified for each action
- [ ] Target value defined
- [ ] Measurement frequency stated
- [ ] Owner assigned for tracking

## Example: Complete Output

```
# Insights

## Traffic Decline Drives Revenue Drop
**Summary:** April's 15% revenue decline is entirely explained by a 15% traffic drop—conversion and pricing remained flat.
**Chart:** Line chart showing daily traffic (March-April) with April dip highlighted; waterfall chart decomposing revenue change into traffic, conversion, and AOV components.
**Detail:** Traffic fell from 10,000 to 8,500 daily sessions in April while conversion held at 2.5% and AOV at $40. This means the solution lies in recovering traffic, not optimizing the funnel.
**Finding source:** Finding 1 (KPI tree driver decomposition)

## Profit Concentrated in Few Products
**Summary:** Just 20% of products generate 78% of gross profit, indicating strong Pareto effect.
**Chart:** Pareto chart with bars showing cumulative profit by SKU (sorted descending) and line showing cumulative percentage.
**Detail:** Of 500 SKUs, the top 100 drive $780K of profit while the bottom 250 contribute only $50K. This suggests opportunity to focus on high-margin products and rationalize the long tail.
**Finding source:** Finding 2 (Pareto analysis)

# Recommended Actions

## Priority 1: Do First (High Impact, Low-Medium Effort)

### Relaunch April-Underperforming Ads
**Description:** Restart the top 5 paid search campaigns that were paused in April with same budget and targeting.
**Impact:** Recover ~2,000 sessions (23% of lost traffic) → ~$20,000 monthly revenue
**Effort:** Low (4 hours setup)
**Owner:** Marketing Manager
**Metrics:** Campaign impressions, clicks, spend, traffic from paid channels
**Timeline:** 1 week to see initial impact
**Addresses:** Finding 1 (Traffic decline)
**Risk:** Low (reverting to previously successful configuration)

## Priority 2: Quick Wins (High Impact, Low Effort)

### Send Win-Back Email Campaign
**Description:** Email customers who purchased in Q1 but not in April with 15% discount code.
**Impact:** Recover 500 sessions (6% of lost traffic) → ~$5,000 monthly revenue
**Effort:** Low (6 hours including email design and segmentation)
**Owner:** Email Marketing Specialist
**Metrics:** Email sent, open rate, click rate, conversions, revenue attributed
**Timeline:** 3 days to send, 2 weeks to see conversions
**Addresses:** Finding 1 (Traffic decline)
**Risk:** Low (limited to one-time discount)

## Priority 3: Do Next (Medium Impact/Effort)

### Rationalize Bottom 100 SKUs
**Description:** Discontinue or merge the bottom 100 SKUs (contributing <2% of profit) to focus inventory and marketing on top performers.
**Impact:** Reduce inventory carrying costs, increase operational efficiency, potential 1-2% margin improvement
**Effort:** Medium (4 weeks including analysis, stakeholder alignment, execution)
**Owner:** Inventory Manager + Category Manager
**Metrics:** SKU count reduction, inventory cost savings, margin impact
**Timeline:** 8 weeks for full implementation
**Addresses:** Finding 2 (Profit concentration)
**Risk:** Medium (some customer dissatisfaction, need careful communication)

# Measurement Plan

| Action | Metric | Target | Frequency | Owner | Status |
|--------|--------|--------|-----------|-------|--------|
| Relaunch ads | Paid search traffic | +2,000 sessions/week | Weekly | Marketing Manager | Not started |
| Win-back email | Email conversion rate | 2% | Per campaign | Email Specialist | Not started |
| SKU rationalization | Gross margin % | +1.5% | Monthly | Inventory Manager | Not started |

# Risks & Considerations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| May seasonality affects comparison | High | High | Compare to April 2023, not March 2024 |
| Ad costs increased since April | Medium | Medium | Check current CPC before relaunch |
| Discount trains customers to wait | Low | Medium | Limit win-back to one-time, segment carefully |
| SKU discontinuation disappoints customers | Medium | Low | Identify alternatives before discontinuing |
```
