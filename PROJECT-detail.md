# PROJECT-detail.md — Business Data Analysis & Insights (Idea 67)

## Executive Summary
A harness that turns a business question + data into validated, plain-language insights and actions, using sound analytical methods and guarding against spurious conclusions.

## Problem Statement
Non-technical users misread charts, confuse correlation with causation, and react to noise. This skill applies rigorous methods and communicates clearly.

## Target Users & Use Cases
- **Shop owner:** "Why did revenue dip in Q2?" → diagnostic breakdown.
- **Manager:** "Which products drive profit?" → segmentation + Pareto.
- **Founder:** "Is churn getting worse?" → cohort trend with significance.

## Harness Architecture
```
/business-data-insights
  → sub-requirements-gatherer  (question, data, KPIs)    [gate: question + data defined]
  → [main] research            (benchmarks/methods)      [gate: benchmarks dated]
  → sub-scoring-engine         (analysis + findings)     [gate: each finding method + evidence]
  → sub-quality-reviewer       (spurious-conclusion guard)[gate: causation/sample checked]
  → sub-improvement-roadmap    (insights + actions)      [gate: each action tied to a finding]
  → [main] synthesize
```

## Full Sub-Skill Catalog
| Sub-skill | Purpose | Inputs | Outputs | Tools | Gate |
|-----------|---------|--------|---------|-------|------|
| sub-requirements-gatherer | Frame question | question, data | analysis brief | Read | Question + data defined |
| sub-scoring-engine | Analyze | data | findings | Read | Each finding method + evidence |
| sub-quality-reviewer | Validity guard | findings | validated findings | Read | Causation/sample checked |
| sub-improvement-roadmap | Insights + actions | findings | actions | Write | Each action tied to a finding |

## Skill File Format Specification
Per Claude skill standard; see skills/main.md.

## E2E Execution Flow
1. Frame the business question into an analyzable form; build a KPI tree. 2. Research relevant benchmarks. 3. Analyze: trend, variance/contribution, segmentation, Pareto, cohort; note sample size and confidence. 4. Quality reviewer guards against spurious correlation, Simpson's paradox, small-sample noise, and causal overreach. 5. Roadmap: plain-language insights with one chart-idea each and concrete actions. 6. Render.
Error handling: insufficient data → state limits; no clear question → ask; offline → use brain + flag.

## SECOND-KNOWLEDGE-BRAIN Integration
Sources: statistics/analytics literature, KPI benchmarks, data-storytelling. Weekly append.

## Supporting Tools Spec
`knowledge_updater.py`: queries on analytics methods & KPI benchmarks; weekly cron; dedupe by hash.

## Quality Gates
- Each finding states the method and the supporting evidence.
- Causation claims justified or downgraded to correlation.
- Sample-size/confidence noted; actions tied to findings; offline flagged.

## Test Scenarios (summary)
1. Revenue dip diagnosis. 2. Product profit Pareto. 3. Churn cohort trend. 4. Spurious correlation guard. 5. Small-sample caution. (Full set in tests/.)

## Key Design Decisions
1. KPI-tree framing. 2. Correlation ≠ causation guard. 3. Plain-language output. 4. Each insight has a chart-idea. 5. Sample/confidence always noted.
