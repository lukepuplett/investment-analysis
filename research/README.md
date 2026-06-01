# Investment Analysis Research Repository

**Purpose:** Centralized library of cross-cutting industry research, thematic analyses, and methodological documentation that informs company-specific investment analysis. This repository enables analysts to reference validated research when evaluating companies operating within specific market verticals or facing common structural headwinds.

---

## Repository Structure

### `themes/` — Thematic Research by Industry/Market Driver

Organized by major structural themes that cut across multiple companies. Each theme contains:
- **Pipeline & landscape analysis** (capacity, geography, timing)
- **Supply/demand dynamics** (constraints, growth projections)
- **Competitive/technical shifts** (technology transitions, obsolescence)
- **Financial implications** (capex cycles, margin pressure, TAM expansion)

#### `data-center-buildout/` — Global Data Center Development Dynamics (Q2 2026)

**Scope:** Global capital expenditure, construction pipelines by region, facility design evolution, fit-out methodology, commissioning framework.

**Key Files:**
- `2026_Q2_GEMINI_global_data_center_research.md` — Comprehensive landscape analysis from Google Gemini (June 1, 2026)
- Topics covered:
  - Global capex projections ($640B current, $3T through 2030)
  - Regional operational & under-construction capacity (US, Europe, APAC, LatAm, ME/Africa)
  - 40+ mega-project index with investment/capacity/timeline
  - Fleet age analysis & technological obsolescence (legacy 5-10 kW vs. AI 40-140 kW)
  - 11-step data center fit-out process (utility → commissioning → handoff)
  - 6-level commissioning framework (design through operations)

**How to Use:**
- **For TT analysis:** Data center cooling TAM, fleet lifecycle drivers (older facilities needing retrofits), Stella modular systems applicability
- **For other companies:** Hyperscaler capex timing, grid interconnection lead times (8-10 years in Europe), power density evolution, liquid cooling adoption (40% of new builds)
- **For valuation:** Supports 30%+ data center cooling TAM growth assumptions; validates multi-year visibility into infrastructure projects

**Refresh Cadence:** Semi-annual (H1, H2 reports from Synergy Research, JLL, or fresh Gemini pulls)

---

## Research Methodology & Cost-Saving Documentation

This section documents how to conduct cost-effective industry research and where to find methodology references.

### Recommended Research Sources (Free/Low-Cost)
1. **Google Gemini / OpenAI** — Large-context LLMs for synthesizing public data into structured landscape analyses
2. **Public Industry Reports** — Synergy Research, JLL, Gartner, IDC (often available as executive summaries or free tiers)
3. **Company Presentations** — Earnings calls, investor days reveal forward-looking strategy and TAM estimates
4. **Regulatory Filings** — SEC 10-Ks contain industry context, competitive analysis, risk disclosures
5. **News Aggregation** — DataBox, News API, or manual Reuters/Bloomberg screening for deal flow and trend signals

### Cost Optimization Approach
- **Batch research by theme, not by company** — Analyze "global data center buildout" once, reference it across 10+ companies (energy, cooling, infrastructure, cloud, semiconductors)
- **Use LLMs for synthesis** — Feed 20-30 public sources into a single prompt to generate a structured landscape analysis (vs. buying $3K research reports)
- **Update semi-annually** — Refresh thematic research on a regular cadence; drill down to company specifics only quarterly

### Documentation Best Practices
- Include **source dates** and **data refresh timing** (e.g., "as of June 1, 2026 via Google Gemini")
- Cite **primary sources** where possible (JLL reports, SEC filings, news articles)
- Structure as **referenceable tables and sections** so analysts can quickly pull data for their own company analysis
- Cross-link to **company-specific analysis** that depends on the research (e.g., TT README → data center research)

---

## Company Cross-References to Thematic Research

### Trane Technologies (TT)
- **Data Center Buildout Research** → Supports TAM expansion thesis, Stella modular systems applicability, fleet retrofit opportunity
- Location: `/tt/README.md` → Search "data center" → Cross-reference `/research/themes/data-center-buildout/`

### [Future Companies]
- [To be populated as new companies enter coverage]

---

## Research Update Log

| Theme | Last Updated | Data Date | Source | Key Metrics |
|-------|--------------|-----------|--------|-----------|
| **Data Center Buildout** | 2026-06-01 | 2026-06-01 | Google Gemini | 14% CAGR, 103→200 GW, $640B capex, 8-10 yr grid queues |

---

## Next Steps

1. ✅ Global data center research documented and indexed
2. ⏳ Cross-link TT README to data center research
3. ⏳ Create additional thematic research directories (e.g., labor scarcity, AI capex cycles, tariff impact)
4. ⏳ Establish research refresh schedule and ownership
5. ⏳ Document additional research methodologies and cost-saving techniques

---

*Last Updated: June 1, 2026 | Curator: Investment Analysis Team*
