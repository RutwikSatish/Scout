# InnoScout — North American Transport Technology Scouting Dashboard

**Live app:** [innoscout.streamlit.app](https://innoscout.streamlit.app) &nbsp;|&nbsp; **Methodology:** [methodology.md](./methodology.md) &nbsp;|&nbsp; **Business case:** [artifacts/innoscout_business_case.pptx](./artifacts/innoscout_business_case.pptx)

---

## The problem

Corporate innovation teams at large OEMs evaluate hundreds of early-stage technology companies each year to identify strategic partnership candidates. Most scouting processes are ad hoc — driven by conference introductions and individual relationships — producing no structured, auditable, or repeatable output for leadership review. There is no standard way to compare a seed-stage battery startup against a Series B telematics platform using the same criteria.

**Result:** high-potential companies are missed, low-fit companies consume disproportionate evaluation time, and leadership decisions lack documented rationale.

---

## What this project does

InnoScout is a live technology scouting and partnership evaluation tool that maps 40 early-stage companies across four North American transport technology clusters — Battery Management, Autonomous Freight, Telematics, and Last-Mile Electrification — and scores each against five weighted dimensions drawn from NASA's Technology Readiness Level framework and corporate partnership evaluation practice.

The scoring model is fully configurable: sidebar sliders allow innovation analysts to adjust dimension weights in real time, instantly re-ranking the shortlist to reflect shifting strategic priorities. Output includes a ranked shortlist, bubble landscape map, dimension breakdown chart, radar-based company comparison, and automatic partnership recommendation tiers — all exportable to CSV.

---

## BA approach

- **Framed the business problem** as a requirements gap: innovation teams lack a structured evaluation framework, not a data source — so the tool needed to enforce a repeatable process, not just display information
- **Mapped 40 companies** across 4 technology clusters and 6 US economic regions (Silicon Valley, Detroit Corridor, Boston, Austin, Research Triangle, Chicago) using publicly available funding, patent, and partnership data
- **Designed a 5-dimension weighted scoring model** covering Technology Readiness Level, Strategic Alignment, Patent Activity, Partnership Track Record, and Financial Runway — each with a documented rubric and normalization methodology (see [methodology.md](./methodology.md))
- **Built a live Streamlit application** with adjustable weight sliders, multi-filter capability, side-by-side company comparison with radar charts, and color-coded partnership recommendations (Recommended / Watch List / Pass)
- **Produced a leadership-ready business case** in PowerPoint covering problem framing, methodology, top 3 recommended companies with rationale, and a phased engagement roadmap (see [artifacts/](./artifacts/))

---

## Outcome

- 12 of 40 companies scored above the 75-point shortlist threshold under default weights
- Top 3 recommended partnerships: ClearPath Freight (Autonomous Freight, 88.4), TruckIQ (Telematics, 86.1), CargoCycle (Last-Mile Electrification, 84.7)
- Framework is fully repeatable: refresh the dataset quarterly and re-run to track ecosystem evolution
- Methodology documented as an SOP so the scouting process can be handed off without rebuilding from scratch

---

## Tool stack

| Layer | Technology |
|-------|-----------|
| Application | Python 3.11, Streamlit 1.33 |
| Data processing | pandas 2.2 |
| Visualization | Plotly 5.22 (scatter, bar, radar, heatmap) |
| Scoring engine | Custom weighted normalization model (pure Python) |
| Deployment | Streamlit Community Cloud |

---

## Repo structure

```
innoscout/
├── app.py                          # Streamlit application
├── requirements.txt                # Dependency pinning
├── methodology.md                  # Scoring framework, rubrics, data sources, limitations
├── README.md                       # This file
└── artifacts/
    ├── innoscout_business_case.pptx  # 6-slide leadership presentation
    └── innoscout_ranked_results.csv  # Full scored dataset export
```

---

## How to run locally

```bash
git clone https://github.com/rutwiksatish/innoscout
cd innoscout
pip install -r requirements.txt
streamlit run app.py
```

---

## How to extend

To apply this framework to a different industry or geography, update the company dataset in `app.py` and recalibrate the scoring rubrics in `methodology.md` to reflect the new strategic context. The scoring engine, filters, and visualization layer require no changes.

---

## About the author

Rutwik Satish is a Master of Engineering Management candidate at Northeastern University (May 2026) with a background in Industrial Engineering and supply chain operations. This project was built to simulate the technology scouting workflow used by corporate innovation offices — specifically the process of mapping startup ecosystems, building weighted evaluation frameworks, and preparing structured business cases for senior leadership review.

[LinkedIn](https://linkedin.com/in/rutwiksatish) &nbsp;|&nbsp; [GitHub](https://github.com/rutwiksatish) &nbsp;|&nbsp; [FactorySync](https://factorysync.streamlit.app) &nbsp;|&nbsp; [TariffGuard](https://tariffguard.streamlit.app) &nbsp;|&nbsp; [PriceOps](https://priceops.streamlit.app)
