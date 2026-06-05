# Model Reframe

---

## Charging Is Not a Constraint

The original model treated charging infrastructure as a hard bottleneck (2 chargers per vehicle). This was a spreadsheet assumption masquerading as a physical law.

Fleet operations differ fundamentally from consumer EV ownership:

| Factor | Consumer EV | Robotaxi Fleet |
|--------|-------------|-----------------|
| Charging paradigm | Instant availability | Orchestrated, staggered, cost-optimized |
| Charger ratio | ~2 per vehicle | 1 per 12–20 vehicles |
| Utilization pattern | Evening peaks | 24/7 staggered + depot overnight |

**Annual cost per vehicle: $500 (capex amortization + maintenance) — 0.5% of fleet economics.**

Charging is solved with capital. If revenue justifies chargers, they are deployed. Regulatory approval is the actual binding constraint.

---

## Three Mutually Exclusive Worlds

| Aspect | **Regime A: Utility** | **Regime B: Infrastructure** | **Regime C: Platform** |
|--------|----------------------|------------------------------|------------------------|
| Competes with | Uber/Lyft | Transit + suburban cars | Car ownership (50%+) |
| TAM | $5–10B | $50–100B | $2–5T |
| Scaling model | Linear (capital) | Sigmoid (S-curve approval) | Exponential (software) |
| Fleet 2035 | 120–300k | 500k–2M | 10–50M |
| Terminal multiple | 9–18x | 25–50x | 50–150x |
| Waymo terminal value | $30–90B | $150–400B | $2–10T |
| Core assumption | Ownership <5% | Ownership 20–30% | Ownership 50%+ |

Regimes are internally coupled assumption packages, not points on a continuous scale. Cannot mix: if ownership truly replaces 50%+ of cars, the model cannot stay at a 9x transport multiple.

---

## Seven Hidden Variables That Lock the Regime

Each of these co-moves with the others. Observe one; the rest follow.

1. **Ownership Substitution %** — the hinge variable. Determines TAM, take-rate dynamics, and customer lock-in. If <10% by 2028, Regime A. If 15–30%, Regime B. If >30%, Regime C possible.

2. **Regulatory Approval Pace** — must match autonomy robustness. 3–6%/year = bureaucratic (A). S-curve inflection = infrastructure (B). Exponential post-inflection = platform (C).

3. **Non-Ride Revenue Mix** — reveals asset-layer formation. <5% = pure rideshare (A). 10–25% = infrastructure layer (B). >30% = platform exceeds core ride (C).

4. **Take-Rate Sustainability** — derivative of ownership + competition. <32% with Uber pressure (A). 25–40% with convenience premium (B). 40–65% with lock-in + network effects (C).

5. **Fleet Guidance** — reveals company's internal TAM model. <300k (A). 500k–2M (B). >5M (C).

6. **Software Scaling Rate** — marginal cost decline per year. <10%/year = hardware-gated (A). 15–25%/year = steady (B). 30%+/year = autonomy generalizing, cost toward zero (C).

7. **Competitive Consolidation** — coexistence requires software NOT scaling. Monopoly requires software scaling. Mutually exclusive. Both players surviving at similar pace = Regime A or B.

---

## The Original Model's Failure Mode

The model was locked into Regime A because every variable was set to A-compatible values:
- Fleet 120–300k → signals <5% ownership substitution
- Take-rate 18–32% → Uber/Lyft competitive pressure
- Approval 3–6%/year → bureaucratic, linear
- Terminal multiple 9–18x → transport commodity
- No asset-layer monetization

These are self-reinforcing. Ownership assumption drives fleet size, which drives utilization, which drives take-rate, which drives regulatory narrative. The architecture excluded 85–90% of potential upside by construction.

**Fix:** Ownership substitution is the primary input. All other variables derive from it. The model now takes ownership substitution as a scenario parameter and constrains the rest accordingly.

---

## Ownership Substitution Is the Hinge

All other variables are determined by this one:

- If <10% by Q4 2028 → accept Regime A, $30–90B Waymo value
- If 15–30% by Q4 2028 → model Regime B, $150–400B Waymo value  
- If >30% by Q4 2028 → price Regime C option, $2–10T range

**Data sources:** Insurance policy dropoffs · Car registrations per household · Waymo/Tesla ridership surveys · Public transit ridership · Census vehicle ownership
