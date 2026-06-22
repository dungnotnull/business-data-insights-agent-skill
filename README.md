# Business Data Insights Agent Skill

> Turn business questions and data into validated, plain-language insights and actions using sound analytical methods with guards against spurious conclusions.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-purple.svg)](https://claude.ai/code)
[![Production Ready](https://img.shields.io/badge/Status-Production--ready-brightgreen.svg)](https://github.com/dungnotnull/business-data-insights-agent-skill)

## 🎯 Overview

Business Data Insights is a production-grade AI agent skill that transforms raw business data into actionable intelligence. Designed for non-technical business owners, it applies rigorous analytical methods—including KPI trees, trend analysis, cohort segmentation, Pareto analysis, and statistical validity checks—to surface reliable insights while guarding against common analytical pitfalls like spurious correlation and Simpson's paradox.

### The Problem It Solves

Non-technical users struggle to extract reliable insights from their data because they:
- Misinterpret charts and confuse correlation with causation
- React to noise rather than genuine signals
- Lack statistical rigor in their analysis
- Chase false patterns that don't hold up under scrutiny
- Need plain-language explanations, not technical jargon

### The Solution

This skill structures the analytical question, applies proven methods with statistical validity, validates findings against common fallacies, and outputs clear insights with concrete actions tied directly to evidence.

## ✨ Key Features

### 🔍 Rigorous Analysis Methods

- **KPI Tree Decomposition**: Break down metrics into drivers (e.g., Revenue = Traffic × Conversion × AOV)
- **Trend & Variance Analysis**: Time-series decomposition with seasonal adjustment
- **Cohort Analysis**: Track customer groups over time for retention and churn insights
- **Pareto/ABC Analysis**: Identify concentration of value (80/20 rule) in products or customers
- **Statistical Testing**: t-tests, chi-square, ANOVA, correlation with confidence intervals

### 🛡️ Quality Gates

- **Correlation ≠ Causation Guard**: Systematically challenges causal claims
- **Simpson's Paradox Detection**: Identifies when segment trends contradict aggregates
- **Sample Size Validation**: Flags findings based on insufficient data
- **Seasonality Adjustment**: Separates genuine change from seasonal patterns
- **Multiple Comparison Correction**: Prevents false positives from repeated testing

### 📊 Sector-Specific Benchmarks

Built-in KPI benchmarks for:
- **E-commerce & Retail**: Conversion rates, AOV, margins, returns
- **SaaS & Subscription**: Churn, LTV, CAC, net revenue retention
- **Manufacturing / B2B**: Margins, inventory turnover, delivery rates
- **Restaurants / Hospitality**: Food/labor costs, turnover rates

### 🎯 Actionable Outputs

- Plain-language insights with chart recommendations
- Prioritized action list by impact-to-effort matrix
- Measurement plans with success metrics
- Risk assessment and mitigation strategies

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Business Question                        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│         Phase 1: Requirements Gatherer                        │
│  • Frame question measurably                                 │
│  • Build KPI tree                                            │
│  • Inventory data                                             │
│  • Capture context                                           │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│         Phase 2: Research Benchmarks                         │
│  • Search industry KPIs                                       │
│  • Verify analytical methods                                  │
│  • Date all sources                                          │
│  • Offline mode support                                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│         Phase 3: Scoring Engine                               │
│  • Trend & seasonality analysis                              │
│  • Driver decomposition                                      │
│  • Segmentation & Pareto                                     │
│  • Statistical validity                                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│         Phase 4: Quality Reviewer                            │
│  • Causation vs correlation check                             │
│  • Simpson's paradox test                                    │
│  • Sample size validation                                    │
│  • Seasonality effects                                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│         Phase 5: Improvement Roadmap                          │
│  • Plain-language insights                                   │
│  • Concrete actions                                          │
│  • Impact/effort prioritization                              │
│  • Success metrics                                           │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    Final Report                               │
│  • Key findings with evidence & confidence                   │
│  • Validity notes & caveats                                  │
│  • Insights with chart recommendations                       │
│  • Prioritized actions & measurement plan                    │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
business-data-insights/
├── README.md                              # This file
├── CLAUDE.md                              # Skill instructions
├── PROJECT-detail.md                      # Detailed project documentation
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md # Development tracking
├── SECOND-KNOWLEDGE-BRAIN.md              # Knowledge base & benchmarks
├── skills/
│   ├── main.md                            # Main harness orchestration
│   ├── sub-requirements-gatherer.md       # Phase 1: Question framing
│   ├── sub-scoring-engine.md              # Phase 3: Analysis methods
│   ├── sub-quality-reviewer.md           # Phase 4: Validity gates
│   └── sub-improvement-roadmap.md        # Phase 5: Actions & insights
├── tools/
│   └── knowledge_updater.py              # Automated knowledge updates
└── tests/
    └── test-scenarios.md                  # 23 comprehensive test scenarios
```

## 🚀 Installation

### As a Claude Skill

1. Clone this repository:
```bash
git clone https://github.com/dungnotnull/business-data-insights-agent-skill.git
cd business-data-insights-agent-skill
```

2. Copy to your Claude skills directory:
```bash
# Windows
copy business-data-insights-agent-skill C:\Users\YourUsername\.claude\skills\

# macOS/Linux
cp -r business-data-insights-agent-skill ~/.claude/skills/
```

3. Restart Claude Code or Claude desktop app

4. Invoke the skill:
```
/business-data-insights "Why did revenue drop in April?"
```

### Knowledge Updater (Optional)

The knowledge updater automatically crawls analytics literature and KPI benchmarks to keep SECOND-KNOWLEDGE-BRAIN.md current.

```bash
# Install dependencies
pip install crawl4ai

# Run manual update
python tools/knowledge_updater.py

# Run with dry-run (preview only)
python tools/knowledge_updater.py --dry-run

# Schedule weekly updates (cron)
0 2 * * 0 /usr/bin/python3 /path/to/knowledge_updater.py
```

## 📖 Usage Examples

### Example 1: Revenue Decline Diagnosis

**Input:**
```
"Why did revenue drop 15% in April compared to March?"
Data: Daily revenue, traffic, orders, AOV for March-April 2024
```

**Output:**
```markdown
# Business Data Insights — Revenue Decline Analysis

## 1. Question & Data
- **Question framed:** Why did total revenue decrease from $100,000 (March) to $85,000 (April)?
- **Period:** March 1-31 vs April 1-30, 2024
- **Target metric:** Total revenue (USD)

## 2. Key Findings

### Finding 1: Traffic Drop Explains Entire Decline
**Finding:** Revenue declined 15% entirely due to 15% traffic decrease; conversion and AOV remained flat.
**Method:** KPI tree driver decomposition
**Evidence:** 
- Traffic: 10,000 → 8,500 sessions (-15%)
- Conversion: 2.5% → 2.5% (flat)
- AOV: $40 → $40 (flat)
- Traffic contribution: -$15,000 (100% of variance)
**Confidence:** High (n=62 days, complete data, SD traffic=$1,200)

## 3. Validity Notes
- **Causation:** Traffic decline caused revenue decline (mechanism clear)
- **Seasonality:** April typically 3% lower than March; this is 15% (beyond seasonal)
- **Sample:** Adequate (n=62)

## 4. Insights

### Insight 1: Fix Traffic, Not Funnel
**Summary:** The entire revenue decline comes from fewer visitors, not from conversion issues.
**Chart:** Line chart showing daily traffic with April dip highlighted
**Detail:** With conversion flat at 2.5% and AOV stable at $40, recovering 1,500 daily sessions would restore the $15,000 loss. Optimization efforts should focus on traffic acquisition, not funnel optimization.

## 5. Recommended Actions

### Priority 1: Do First (High Impact, Low Effort)

**Action 1.1: Restart Top Performing Ad Campaigns**
- Description: Relaunch the 5 paid search campaigns paused in April with same budget
- Impact: Recover ~2,000 sessions (23% of loss) → ~$20,000 monthly revenue
- Effort: Low (4 hours setup)
- Owner: Marketing Manager
- Metrics: Campaign impressions, clicks, traffic from paid channels
- Timeline: 1 week to see initial impact
- Addresses: Finding 1

### Priority 2: Quick Wins

**Action 2.1: Win-Back Email Campaign**
- Description: Email Q1 customers who didn't purchase in April with 15% discount
- Impact: Recover 500 sessions (6% of loss) → ~$5,000 monthly revenue
- Effort: Low (6 hours)
- Timeline: 3 days to send, 2 weeks to see conversions
```

### Example 2: Product Profit Pareto

**Input:**
```
"Which products should we focus on?"
Data: SKU-level sales and margin (500 SKUs)
```

**Output:**
```markdown
# Business Data Insights — Product Concentration Analysis

## 2. Key Findings

### Finding 1: Strong Pareto Effect
**Finding:** Top 20% of SKUs (100 items) generate 78% of gross profit
**Method:** Pareto analysis with ABC classification
**Evidence:**
- A class (top 100 SKUs): $780,000 GP (78%)
- B class (next 150 SKUs): $170,000 GP (17%)
- C class (bottom 250 SKUs): $50,000 GP (5%)
- Pareto Index: 3.9 (strong concentration)
**Confidence:** High (complete SKU data, n=500)

## 4. Insights

### Insight 1: Focus on Top 20%
**Summary:** Just 100 products drive nearly 80% of profit.
**Chart:** Pareto chart with cumulative line showing 80/20 concentration
**Detail:** Concentration is strong enough that inventory and marketing focus should prioritize the A-class SKUs. The long tail (C-class) contributes minimal profit while likely tying up resources.

## 5. Recommended Actions

### Priority 1: Do First

**Action 1.1: Ensure Stock of Top 100 SKUs**
- Description: Implement safety stock monitoring for A-class SKUs to prevent stockouts
- Impact: Protect 78% of GP from stockout risk
- Effort: Medium (2 weeks)
- Timeline: Immediate implementation

**Action 1.2: Rationalize Bottom 100 SKUs**
- Description: Discontinue or merge bottom 100 SKUs contributing <2% of GP
- Impact: Reduce inventory costs, simplify operations
- Effort: Medium (4 weeks including stakeholder alignment)
- Timeline: Q3 2024
```

## 🧪 Testing

The skill includes 23 comprehensive test scenarios covering:

- Core functionality (revenue diagnosis, Pareto analysis, cohort trends)
- Edge cases (Simpson's paradox, base effects, multiple comparisons)
- Sector-specific cases (e-commerce, SaaS, manufacturing, restaurant)
- Statistical validity (non-normal distributions, outliers, trend vs noise)
- Integration tests (end-to-end workflows)
- Failure modes (ambiguous questions, missing data, contradictory sources)

Run tests:
```bash
# Manual walkthrough
cat tests/test-scenarios.md

# Automated testing (coming soon)
npm test
```

## 📚 Documentation

- **[PROJECT-detail.md](PROJECT-detail.md)**: Complete technical specification
- **[PROJECT-DEVELOPMENT-PHASE-TRACKING.md](PROJECT-DEVELOPMENT-PHASE-TRACKING.md)**: Development phase tracking
- **[SECOND-KNOWLEDGE-BRAIN.md](SECOND-KNOWLEDGE-BRAIN.md)**: Knowledge base with methods and benchmarks

### Core Concepts

| Concept | Description |
|---------|-------------|
| **KPI Tree** | Decompose metrics into multiplicative drivers (Revenue = Traffic × Conv × AOV) |
| **Variance Analysis** | Attribute changes to specific factors (price, volume, mix) |
| **Cohort Analysis** | Track customer groups over time for retention insights |
| **Pareto Principle** | 80/20 concentration analysis (top 20% drive 80% of value) |
| **Statistical Validity** | Sample size, confidence intervals, significance testing |

## 🔧 Development

### Sub-Skill Architecture

Each phase is implemented as a modular sub-skill:

1. **sub-requirements-gatherer**: Frame questions, build KPI trees, inventory data
2. **sub-scoring-engine**: Apply analytical methods with statistical rigor
3. **sub-quality-reviewer**: Validate findings against common fallacies
4. **sub-improvement-roadmap**: Generate insights and prioritized actions

### Cross-Skill Reuse

The `sub-requirements-gatherer` and `sub-scoring-engine` sub-skills are designed for reuse across related business-operation skills:
- Idea 57: Sales Performance Analysis
- Idea 63: Customer Journey Optimization
- Idea 78: Marketing Attribution
- Idea 80: Pricing Intelligence
- Idea 106: Inventory Optimization
- Idea 178: Financial Health Monitor

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

- [ ] Additional sector benchmarks (healthcare, education, finance)
- [ ] More statistical methods (regression, clustering, forecasting)
- [ ] Automated test suite with assertion framework
- [ ] Visualization generation (chart images)
- [ ] Multi-language support

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update tests if applicable
5. Submit a pull request

## 📊 Benchmarks & Standards

### E-commerce Benchmarks

| Metric | Typical Range |
|--------|--------------|
| Conversion Rate | 2-4% |
| Average Order Value | $45-150 |
| Customer LTV | $100-500 |
| Gross Margin | 25-50% |
| Return Rate | 10-30% |

### SaaS Benchmarks

| Metric | Typical Range |
|--------|--------------|
| Monthly Churn | 5-10% |
| Net Revenue Retention | 90-120% |
| CAC | $200-2000 |
| Free-to-Paid Conversion | 3-8% |

## ⚠️ Limitations & Best Practices

### What This Skill Does Well

- Analyzing historical data to identify patterns and trends
- Decomposing metrics to localize change
- Validating insights against statistical fallacies
- Communicating findings in plain language

### What This Skill Doesn't Do

- Real-time monitoring or alerting
- Predictive forecasting (use specialized tools)
- Data collection or ETL
- Accounting or financial reporting

### Best Practices

1. **Provide sufficient data**: At least 30 data points for trend analysis
2. **Define clear questions**: Vague questions lead to vague insights
3. **Context matters**: Share information about promotions, seasonality, market changes
4. **Verify causality**: Don't act on correlational findings without confirming mechanism
5. **Monitor over time**: Establish baseline before making major decisions

## 🔐 Privacy & Data Handling

- This skill processes data within your local Claude environment
- No data is transmitted to external services (except optional WebSearch for benchmarks)
- Knowledge updater fetches public sources only
- Your business data never leaves your control

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built on proven analytical frameworks:
- **Cole Naflic** — Storytelling with Data
- **Thomas H. Davenport** — Competing on Analytics
- **Eric Ries** — Lean Analytics
- **Industry standards** — SSRN, HBR, McKinsey Analytics

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/dungnotnull/business-data-insights-agent-skill/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dungnotnull/business-data-insights-agent-skill/discussions)
- **Documentation**: See project `.md` files

## 🌟 Star History

If you find this skill useful, please consider giving it a ⭐ star on GitHub!

---

**Built with ❤️ for the business community that deserves better data insights.**
