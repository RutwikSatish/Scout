# InnoScout — Scouting Methodology

**Project:** North American Transport Technology Ecosystem Mapping
**Author:** Rutwik Satish
**Version:** 1.0 | May 2026
**Context:** Built to simulate the technology scouting workflow used by corporate innovation offices evaluating early-stage companies for strategic partnership, pilot programs, or investment.

---

## 1. Why this framework exists

Corporate innovation teams at large OEMs face a repeatable problem: thousands of startups exist across any given technology domain, but internal capacity to evaluate them is limited. Most scouting processes are ad hoc — driven by conference introductions, analyst reports, or individual relationships — producing no structured, auditable, or repeatable output.

This framework operationalizes the scouting process into five scoring dimensions derived from established technology readiness and partnership evaluation literature, applied across four strategic clusters and six US economic regions. The output is a ranked shortlist with defensible rationale — structured for senior leadership review.

---

## 2. Technology cluster definitions

Four clusters were selected based on Volvo Group's publicly stated strategic priorities in electrification, automation, and connected transport:

| Cluster | Definition | Strategic rationale |
|---------|-----------|-------------------|
| **Battery Management** | Companies developing battery hardware, software, thermal management, second-life, or charging infrastructure for commercial vehicle applications | Decarbonization of heavy transport requires breakthroughs in energy storage density, degradation prediction, and depot charging economics |
| **Autonomous Freight** | Companies building Level 3–5 autonomous systems, platooning stacks, driver assistance, or AV simulation/validation platforms for commercial trucks | Labor cost reduction and safety improvement in long-haul freight; regulatory readiness in 2025–2030 window |
| **Telematics** | Companies providing fleet connectivity, predictive maintenance, driver behavior, regulatory compliance, or data monetization platforms | Connected vehicle data is a strategic asset; OEMs who control fleet data streams gain aftermarket and service revenue |
| **Last-Mile Electrification** | Companies developing electric cargo vehicles, route optimization for EV fleets, depot charging, or carbon reporting for urban delivery | Final 20% of delivery journeys account for disproportionate emissions and cost; electrification here requires city-specific solutions |

---

## 3. Geographic scope — six US economic clusters

Regions were selected based on concentration of transport technology venture activity, academic research infrastructure, and proximity to manufacturing supply chains:

| Region | Rationale |
|--------|-----------|
| **Silicon Valley** | Highest concentration of AV, AI, and mobility startups; primary source of Series B+ freight technology companies |
| **Detroit Corridor** | Legacy automotive OEM ecosystem; strong talent pipeline for hardware-software integration and commercial vehicle applications |
| **Boston** | MIT, Harvard, Northeastern research commercialization; strong in battery chemistry, robotics, and software platforms |
| **Austin** | Emerging mobility hub with lower burn rates; active EV infrastructure and freight logistics startup activity post-2020 |
| **Research Triangle (NC)** | Proximity to Volvo's Greensboro manufacturing operations; growing logistics tech cluster; favorable regulatory environment |
| **Chicago** | Largest inland freight hub in North America; high density of last-mile, telematics, and fleet management companies |

---

## 4. Scoring dimensions and normalization

Each company is scored across five dimensions. All dimensions are normalized to a 0–1 scale before weighting to ensure comparability across different measurement units.

### 4.1 Technology Readiness Level (TRL)

**Source:** NASA TRL scale (adapted by EU Horizon program for commercial applications)

| TRL | Definition |
|-----|-----------|
| 1–2 | Basic principles observed; concept formulated |
| 3–4 | Proof of concept; laboratory validation |
| 5–6 | Technology validated in relevant environment; prototype demonstrated |
| 7–8 | System prototype demonstrated in operational environment; system complete and qualified |
| 9 | Actual system deployed in commercial operations |

**Normalization:** `TRL_norm = TRL / 10`

**Why it matters:** TRL below 5 indicates pre-commercial technology requiring significant development investment before deployment. OEM partnership candidates should generally be TRL 6+ unless the strategic priority justifies early-stage risk.

---

### 4.2 Strategic Alignment

**Definition:** Degree to which the company's core technology directly addresses one of the four cluster priorities AND is applicable to commercial vehicle (Class 5–8 truck) use cases specifically.

**Scoring rubric (1–10):**
- 9–10: Core product directly solves a priority problem for heavy commercial transport; no adaptation required
- 7–8: Strong fit with moderate adaptation for heavy vehicle context
- 5–6: Relevant technology but designed for passenger vehicle or light commercial vehicle market
- 3–4: Adjacent technology with indirect applicability
- 1–2: Peripheral relevance

**Normalization:** `SA_norm = Strategic_Alignment / 10`

---

### 4.3 Patent Activity

**Definition:** Volume and recency of patent filings as a proxy for proprietary technology depth and defensibility.

**Scoring rubric (1–10):**
- 9–10: 10+ active patents in core domain; recent filings in past 12 months; evidence of IP licensing revenue
- 7–8: 5–9 active patents; consistent filing cadence
- 5–6: 2–4 patents; technology partially protected
- 3–4: 1 patent or patent pending; limited IP moat
- 1–2: No patents filed; technology is largely process or software trade secret

**Normalization:** `PA_norm = Patent_Activity / 10`

**Note:** Patent activity is weighted lower than TRL and strategic alignment by default because software-native companies (telematics, fleet management) may have strong technology with limited patent strategy. Weight should be increased for hardware-intensive clusters (Battery Management, Autonomous Freight).

---

### 4.4 Partnership Track Record

**Definition:** Evidence of prior successful partnerships with Tier 1 automotive suppliers, OEMs, logistics operators, or government programs.

**Scoring rubric (1–10):**
- 9–10: Active commercial partnerships with named Tier 1 or OEM; publicly announced joint development agreements
- 7–8: Pilot program completed with enterprise customer; letter of intent or MOU in place
- 5–6: Paid proof-of-concept with at least one enterprise customer
- 3–4: Early customer conversations; no formal agreement
- 1–2: No enterprise engagement; direct-to-consumer or academic partnerships only

**Normalization:** `PTR_norm = Partnership_Track_Record / 10`

**Why it matters:** Startups with no prior OEM or Tier 1 partnership experience require significantly more onboarding investment. This dimension penalizes early-stage companies that have not yet demonstrated ability to navigate corporate procurement and compliance requirements.

---

### 4.5 Financial Runway

**Definition:** Estimated months of operating capital remaining based on last funding round, disclosed burn rate, and headcount.

**Normalization:** `FR_norm = min(Financial_Runway_Months / 36, 1.0)`

**Cap at 36 months:** Companies with runway beyond 3 years receive maximum score. The cap prevents very late-stage companies from receiving disproportionate advantage over well-funded Series B companies with 24 months of runway — both represent low near-term financial risk.

**Why it matters:** A company with less than 12 months of runway is unlikely to survive a typical OEM partnership evaluation cycle (6–18 months). Partnerships initiated with financially distressed startups carry reputational and supply chain continuity risk.

---

## 5. Composite scoring formula

```
Score = Σ (dimension_norm × weight) / Σ (weights) × 100
```

Where:
- `dimension_norm` is the normalized score (0–1) for each dimension
- `weight` is the user-defined importance weight (1–10) for each dimension
- Division by `Σ(weights)` ensures the final score is always on a 0–100 scale regardless of weight configuration

**Default weights (aligned to Volvo Group strategic priorities):**

| Dimension | Default weight | Rationale |
|-----------|---------------|-----------|
| Strategic Alignment | 9 | Highest priority — technology must solve a real Volvo problem |
| TRL | 8 | Commercial readiness is critical for OEM deployment timelines |
| Partnership Track Record | 7 | Proven enterprise execution reduces integration risk |
| Financial Runway | 6 | Must survive the partnership evaluation cycle |
| Patent Activity | 5 | Important but not determinative for software-heavy companies |

---

## 6. Shortlist threshold and partnership recommendation tiers

| Score range | Recommendation | Action |
|-------------|---------------|--------|
| 75–100 | Recommended for partnership | Initiate NDA and technical deep-dive; prepare partnership business case for leadership |
| 60–74 | Watch list | Monitor for 6 months; revisit at next funding round or product milestone |
| Below 60 | Pass | Insufficient strategic fit or financial/technical readiness at current stage |

---

## 7. Data sourcing protocol

For each company evaluated, data was sourced from:

1. **Crunchbase / PitchBook** — Funding stage, total funding raised, founding year, headcount
2. **USPTO Patent Database** — Patent filing volume and recency by company name
3. **Company website and press releases** — Product description, customer announcements, partnership disclosures
4. **LinkedIn** — Employee count verification and team composition
5. **SEC EDGAR** — For companies with public market activity or SPAC history
6. **Industry reports** — Frost and Sullivan, McKinsey, BloombergNEF transport technology market reports for TRL benchmarking

**Refresh cadence:** Scouting data degrades rapidly in early-stage markets. This dataset should be refreshed quarterly. Financial runway estimates should be recalculated at each new funding announcement.

---

## 8. Limitations and assumptions

- TRL scores are assessments based on publicly available product documentation and are not independently verified through technical due diligence. Full TRL verification requires direct engagement with the company's engineering team.
- Financial runway estimates are approximations based on disclosed funding and publicly available headcount data. Actual runway may differ materially if burn rate or revenue has changed since last public disclosure.
- Strategic alignment scores reflect Volvo Group's publicly stated priorities as of Q1 2026. Scores should be recalibrated if strategic focus shifts.
- Companies operating in stealth mode or with limited public disclosure are underrepresented in this dataset.
- This framework evaluates partnership readiness, not acquisition suitability. Valuation, financial performance, and IP ownership structure are outside this framework's scope.

---

## 9. How to extend this framework

To apply this framework to a new technology domain or geography:

1. Define 3–5 clusters aligned to the acquiring organization's strategic roadmap
2. Select regions based on startup density data from Crunchbase, NVCA, or regional economic development reports
3. Source 8–12 companies per cluster using the data sources listed in Section 7
4. Score each company against the five dimensions using the rubrics in Section 4
5. Adjust default weights in the sidebar to reflect the specific strategic context
6. Generate shortlist and export CSV for leadership review
7. Prepare partnership business case for top 3 recommended companies using the PowerPoint template in `/artifacts`
