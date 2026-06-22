# CLAUDE.md — Business Data Analysis & Insights Skill (Idea 67)

**Skill name:** `business-data-insights`
**Tagline:** Non-tech-friendly insights from sales/revenue/KPI data with validated, actionable findings.
**Current phase:** Scaffold complete (Phases 0–5).
**Source idea:** 67 — *Analyze business data (sales reports, revenue, KPIs) to surface insights and trends for non-technical users, grounded in world-renowned data-analysis methods, with improvement recommendations; continuously crawl papers/docs to stay current.*
**Cluster:** `business-operations`

## Problem This Skill Solves
Non-technical owners can't extract reliable insights from their data and chase noise. This skill structures the question, analyzes with sound methods (KPI trees, trend/variance/cohort analysis, statistical validity), validates findings against spurious correlation, and emits plain-language insights + actions.

## Harness Flow Summary
1. **Requirements** (`sub-requirements-gatherer`) — business question, data, KPIs, period.
2. **Research** (main) — verify benchmark/method norms vs SECOND-KNOWLEDGE-BRAIN.md.
3. **Analysis** (`sub-scoring-engine`) — trend/variance/cohort/segmentation findings.
4. **Challenge** (`sub-quality-reviewer`) — guard against spurious/overfit conclusions.
5. **Roadmap** (`sub-improvement-roadmap`) — plain-language insights + actions.

## Sub-skills
- `sub-requirements-gatherer.md` · `sub-scoring-engine.md` · `sub-quality-reviewer.md` · `sub-improvement-roadmap.md`

## Tools Required
WebSearch, WebFetch, Read, Write, Bash.

## Knowledge Sources
Statistics/analytics literature, industry KPI benchmarks, data-storytelling (Knaflic), SSRN business analytics.

## Supporting Python Tools
`tools/knowledge_updater.py` — crawl → SECOND-KNOWLEDGE-BRAIN.md.

## Active Development Tasks
- [x] Scaffold deliverables.
- [ ] Add sector KPI benchmark tables.

## Reference Docs
PROJECT-detail.md · PROJECT-DEVELOPMENT-PHASE-TRACKING.md · SECOND-KNOWLEDGE-BRAIN.md
