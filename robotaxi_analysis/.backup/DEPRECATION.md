# ⚠️ DEPRECATED: Old Robotaxi Model

**These files are SUPERSEDED and should NOT be used.**

## What Changed

The original robotaxi revenue model (May 2026) contained a fundamental error:

- **Incorrect assumption**: Charging infrastructure was modeled as a hard bottleneck (2 chargers per vehicle)
- **Impact**: Both Waymo and Tesla were capped at ~70k vehicles by 2035
- **Reality**: Charging is elastic capital ($500/vehicle/year, 0.5% of fleet capex), not a constraint

## What's Being Used Now

**New model**: `robotaxi_revenue_model_enhanced.py` (active)
**New analysis**: `REFRAME_ANALYSIS.md` (complete reframe)

### Key Changes in Reframed Model:
1. **Regulatory approval** is the primary binding constraint (not charging)
2. **Metro-tier framework** (Tier 1–4) replaces flat national assumptions
3. **Utilization efficiency** depends on operational maturity, not just network effects
4. **Terminal outcomes** by metro type (Waymo 17.3x premium, Tesla 9.8x suburban)
5. **Charging cost model** ($500/vehicle/year, not a constraint)

## Files Archived

- `robotaxi_revenue_model.py.old` — Old model with charging bottleneck ❌
- `run_all_scenarios.py.old` — Runner for old model ❌

## Why This Matters

Using the old model will:
- Incorrectly cap fleets at 70k vehicles
- Miss the real constraint (regulatory approval by metro)
- Misunderstand Waymo's advantage (premium markets, not chargers)
- Misevaluate Tesla's risk (autonomy maturity, not infrastructure)

**Do not use these files for new analysis.**

---

**Archived**: May 20, 2026  
**Replaced by**: `robotaxi_revenue_model_enhanced.py`  
**Full reframe doc**: `REFRAME_ANALYSIS.md`
