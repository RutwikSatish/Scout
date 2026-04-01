import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="InnoScout | CampX Technology Scouting",
    page_icon="🔍",
    layout="wide"
)

# ── DATA ──────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    companies = [
        # Battery Management
        {"Company": "VoltCore Systems", "Cluster": "Battery Management", "Region": "Silicon Valley", "Stage": "Series B", "Founded": 2019, "Employees": 85, "TRL": 7, "Strategic Alignment": 9, "Patent Activity": 8, "Partnership Track Record": 6, "Financial Runway (mo)": 18, "Funding ($M)": 42, "Website": "voltcore.io", "Description": "AI-driven battery degradation prediction for commercial EV fleets"},
        {"Company": "CellMatrix Inc.", "Cluster": "Battery Management", "Region": "Detroit Corridor", "Stage": "Series A", "Founded": 2020, "Employees": 34, "TRL": 6, "Strategic Alignment": 8, "Patent Activity": 7, "Partnership Track Record": 4, "Financial Runway (mo)": 14, "Funding ($M)": 18, "Website": "cellmatrix.com", "Description": "Solid-state battery modules for heavy-duty transport applications"},
        {"Company": "ThermaGuard", "Cluster": "Battery Management", "Region": "Boston", "Stage": "Seed", "Founded": 2022, "Employees": 12, "TRL": 4, "Strategic Alignment": 7, "Patent Activity": 5, "Partnership Track Record": 2, "Financial Runway (mo)": 10, "Funding ($M)": 4, "Website": "thermaguard.ai", "Description": "Thermal management software for lithium-ion pack safety in extreme climates"},
        {"Company": "Electra Pack", "Cluster": "Battery Management", "Region": "Austin", "Stage": "Series C", "Founded": 2017, "Employees": 210, "TRL": 8, "Strategic Alignment": 9, "Patent Activity": 9, "Partnership Track Record": 8, "Financial Runway (mo)": 30, "Funding ($M)": 120, "Website": "electrapack.com", "Description": "Modular battery pack architecture for rapid swapping in logistics fleets"},
        {"Company": "IonBridge", "Cluster": "Battery Management", "Region": "Chicago", "Stage": "Series A", "Founded": 2021, "Employees": 45, "TRL": 6, "Strategic Alignment": 7, "Patent Activity": 6, "Partnership Track Record": 3, "Financial Runway (mo)": 16, "Funding ($M)": 22, "Website": "ionbridge.io", "Description": "Fast-charge infrastructure firmware for depot-based commercial vehicle charging"},
        {"Company": "NovCell", "Cluster": "Battery Management", "Region": "Research Triangle", "Stage": "Series B", "Founded": 2018, "Employees": 90, "TRL": 7, "Strategic Alignment": 8, "Patent Activity": 8, "Partnership Track Record": 5, "Financial Runway (mo)": 20, "Funding ($M)": 55, "Website": "novcell.com", "Description": "Second-life battery repurposing platform with OEM integration APIs"},
        {"Company": "AmpLogic", "Cluster": "Battery Management", "Region": "Silicon Valley", "Stage": "Series A", "Founded": 2020, "Employees": 28, "TRL": 5, "Strategic Alignment": 6, "Patent Activity": 4, "Partnership Track Record": 3, "Financial Runway (mo)": 12, "Funding ($M)": 15, "Website": "amplogic.ai", "Description": "Edge-based battery state-of-health monitoring for remote fleet operators"},
        {"Company": "GridSync", "Cluster": "Battery Management", "Region": "Detroit Corridor", "Stage": "Series B", "Founded": 2019, "Employees": 72, "TRL": 7, "Strategic Alignment": 7, "Patent Activity": 6, "Partnership Track Record": 6, "Financial Runway (mo)": 22, "Funding ($M)": 38, "Website": "gridsync.io", "Description": "V2G (vehicle-to-grid) energy management for commercial depot operators"},

        # Autonomous Freight
        {"Company": "PathwayAI", "Cluster": "Autonomous Freight", "Region": "Silicon Valley", "Stage": "Series C", "Founded": 2016, "Employees": 320, "TRL": 8, "Strategic Alignment": 9, "Patent Activity": 9, "Partnership Track Record": 9, "Financial Runway (mo)": 36, "Funding ($M)": 210, "Website": "pathwayai.com", "Description": "Level 4 autonomous highway freight with active OEM pilot programs"},
        {"Company": "FreightMind", "Cluster": "Autonomous Freight", "Region": "Austin", "Stage": "Series B", "Founded": 2018, "Employees": 140, "TRL": 7, "Strategic Alignment": 8, "Patent Activity": 7, "Partnership Track Record": 7, "Financial Runway (mo)": 24, "Funding ($M)": 88, "Website": "freightmind.io", "Description": "Platooning software stack for long-haul commercial trucks"},
        {"Company": "SentinelDrive", "Cluster": "Autonomous Freight", "Region": "Detroit Corridor", "Stage": "Series A", "Founded": 2020, "Employees": 55, "TRL": 6, "Strategic Alignment": 7, "Patent Activity": 6, "Partnership Track Record": 4, "Financial Runway (mo)": 18, "Funding ($M)": 30, "Website": "sentineldrive.ai", "Description": "Driver assistance and fatigue detection for commercial long-haul operators"},
        {"Company": "LaneLogix", "Cluster": "Autonomous Freight", "Region": "Chicago", "Stage": "Series A", "Founded": 2021, "Employees": 38, "TRL": 5, "Strategic Alignment": 7, "Patent Activity": 5, "Partnership Track Record": 3, "Financial Runway (mo)": 14, "Funding ($M)": 20, "Website": "lanelogix.com", "Description": "HD mapping and lane prediction for urban freight corridors"},
        {"Company": "AutonomIQ", "Cluster": "Autonomous Freight", "Region": "Boston", "Stage": "Seed", "Founded": 2022, "Employees": 16, "TRL": 4, "Strategic Alignment": 6, "Patent Activity": 4, "Partnership Track Record": 1, "Financial Runway (mo)": 9, "Funding ($M)": 6, "Website": "autonomiq.ai", "Description": "Simulation-based validation platform for AV freight certification"},
        {"Company": "HaulBot", "Cluster": "Autonomous Freight", "Region": "Research Triangle", "Stage": "Series B", "Founded": 2017, "Employees": 175, "TRL": 8, "Strategic Alignment": 8, "Patent Activity": 8, "Partnership Track Record": 7, "Financial Runway (mo)": 28, "Funding ($M)": 95, "Website": "haulbot.com", "Description": "Short-haul autonomous yard truck for distribution center operations"},
        {"Company": "ClearPath Freight", "Cluster": "Autonomous Freight", "Region": "Silicon Valley", "Stage": "Series C", "Founded": 2015, "Employees": 410, "TRL": 9, "Strategic Alignment": 9, "Patent Activity": 10, "Partnership Track Record": 9, "Financial Runway (mo)": 40, "Funding ($M)": 340, "Website": "clearpathfreight.com", "Description": "Full-stack AV freight platform with deployed commercial routes in 3 US states"},

        # Telematics
        {"Company": "FleetSense", "Cluster": "Telematics", "Region": "Chicago", "Stage": "Series B", "Founded": 2018, "Employees": 130, "TRL": 8, "Strategic Alignment": 8, "Patent Activity": 7, "Partnership Track Record": 7, "Financial Runway (mo)": 26, "Funding ($M)": 70, "Website": "fleetsense.io", "Description": "Real-time fleet health monitoring with predictive maintenance alerts via OBD integration"},
        {"Company": "OmniTrack", "Cluster": "Telematics", "Region": "Detroit Corridor", "Stage": "Series A", "Founded": 2020, "Employees": 42, "TRL": 6, "Strategic Alignment": 7, "Patent Activity": 5, "Partnership Track Record": 4, "Financial Runway (mo)": 15, "Funding ($M)": 24, "Website": "omnitrack.io", "Description": "Multi-modal freight tracking combining GPS, RFID, and computer vision"},
        {"Company": "NexDrive Analytics", "Cluster": "Telematics", "Region": "Austin", "Stage": "Series B", "Founded": 2017, "Employees": 160, "TRL": 8, "Strategic Alignment": 9, "Patent Activity": 8, "Partnership Track Record": 8, "Financial Runway (mo)": 30, "Funding ($M)": 85, "Website": "nexdrive.com", "Description": "Driver behavior scoring and route optimization for commercial fleets over 50 vehicles"},
        {"Company": "PulseFleet", "Cluster": "Telematics", "Region": "Boston", "Stage": "Series A", "Founded": 2021, "Employees": 35, "TRL": 6, "Strategic Alignment": 7, "Patent Activity": 4, "Partnership Track Record": 3, "Financial Runway (mo)": 13, "Funding ($M)": 18, "Website": "pulsefleet.ai", "Description": "IoT sensor fusion platform for trailer condition monitoring and cargo integrity"},
        {"Company": "SignalPath", "Cluster": "Telematics", "Region": "Research Triangle", "Stage": "Seed", "Founded": 2023, "Employees": 9, "TRL": 3, "Strategic Alignment": 6, "Patent Activity": 3, "Partnership Track Record": 1, "Financial Runway (mo)": 8, "Funding ($M)": 3, "Website": "signalpath.io", "Description": "5G-native edge computing modules for real-time vehicle-to-infrastructure data exchange"},
        {"Company": "TruckIQ", "Cluster": "Telematics", "Region": "Silicon Valley", "Stage": "Series C", "Founded": 2016, "Employees": 285, "TRL": 9, "Strategic Alignment": 9, "Patent Activity": 9, "Partnership Track Record": 9, "Financial Runway (mo)": 36, "Funding ($M)": 180, "Website": "truckiq.com", "Description": "End-to-end fleet management SaaS with ERP and TMS integrations for enterprise fleets"},
        {"Company": "RouteGuard", "Cluster": "Telematics", "Region": "Chicago", "Stage": "Series A", "Founded": 2020, "Employees": 50, "TRL": 6, "Strategic Alignment": 7, "Patent Activity": 5, "Partnership Track Record": 4, "Financial Runway (mo)": 16, "Funding ($M)": 26, "Website": "routeguard.ai", "Description": "Regulatory compliance monitoring for HOS, weight limits, and hazmat routing"},
        {"Company": "DataRig", "Cluster": "Telematics", "Region": "Detroit Corridor", "Stage": "Series B", "Founded": 2019, "Employees": 95, "TRL": 7, "Strategic Alignment": 8, "Patent Activity": 7, "Partnership Track Record": 6, "Financial Runway (mo)": 22, "Funding ($M)": 52, "Website": "datarig.io", "Description": "Connected vehicle data monetization platform for OEMs and fleet operators"},

        # Last-Mile Electrification
        {"Company": "UrbanVolt", "Cluster": "Last-Mile Electrification", "Region": "Boston", "Stage": "Series A", "Founded": 2020, "Employees": 48, "TRL": 6, "Strategic Alignment": 8, "Patent Activity": 6, "Partnership Track Record": 5, "Financial Runway (mo)": 17, "Funding ($M)": 28, "Website": "urbanvolt.io", "Description": "Light electric cargo vehicle platform designed for dense urban last-mile delivery"},
        {"Company": "ChargeRoute", "Cluster": "Last-Mile Electrification", "Region": "Silicon Valley", "Stage": "Series B", "Founded": 2018, "Employees": 110, "TRL": 8, "Strategic Alignment": 9, "Patent Activity": 7, "Partnership Track Record": 7, "Financial Runway (mo)": 25, "Funding ($M)": 65, "Website": "chargeroute.com", "Description": "Dynamic charging route optimization for urban EV delivery fleets"},
        {"Company": "MicroFreight", "Cluster": "Last-Mile Electrification", "Region": "Austin", "Stage": "Seed", "Founded": 2022, "Employees": 14, "TRL": 4, "Strategic Alignment": 7, "Patent Activity": 4, "Partnership Track Record": 2, "Financial Runway (mo)": 11, "Funding ($M)": 5, "Website": "microfreight.ai", "Description": "Autonomous micro-mobility freight pods for pedestrian zone last-mile delivery"},
        {"Company": "GreenDock", "Cluster": "Last-Mile Electrification", "Region": "Chicago", "Stage": "Series A", "Founded": 2021, "Employees": 32, "TRL": 5, "Strategic Alignment": 7, "Patent Activity": 5, "Partnership Track Record": 3, "Financial Runway (mo)": 14, "Funding ($M)": 16, "Website": "greendock.io", "Description": "Modular electric cargo bike fleet management with depot charging infrastructure"},
        {"Company": "LastMileOS", "Cluster": "Last-Mile Electrification", "Region": "Research Triangle", "Stage": "Series B", "Founded": 2017, "Employees": 145, "TRL": 8, "Strategic Alignment": 9, "Patent Activity": 8, "Partnership Track Record": 8, "Financial Runway (mo)": 28, "Funding ($M)": 90, "Website": "lastmileos.com", "Description": "Operating system for electric last-mile fleets including routing, charging, and driver dispatch"},
        {"Company": "SwiftCharge", "Cluster": "Last-Mile Electrification", "Region": "Detroit Corridor", "Stage": "Series A", "Founded": 2020, "Employees": 60, "TRL": 6, "Strategic Alignment": 8, "Patent Activity": 6, "Partnership Track Record": 5, "Financial Runway (mo)": 19, "Funding ($M)": 32, "Website": "swiftcharge.io", "Description": "Mobile on-demand EV charging for last-mile delivery vehicles stranded mid-route"},
        {"Company": "CargoCycle", "Cluster": "Last-Mile Electrification", "Region": "Boston", "Stage": "Series C", "Founded": 2016, "Employees": 230, "TRL": 9, "Strategic Alignment": 9, "Patent Activity": 9, "Partnership Track Record": 9, "Financial Runway (mo)": 38, "Funding ($M)": 155, "Website": "cargocycle.com", "Description": "Heavy-payload electric cargo bikes with autonomous return-to-depot for city logistics"},
        {"Company": "VoltMile", "Cluster": "Last-Mile Electrification", "Region": "Austin", "Stage": "Series B", "Founded": 2019, "Employees": 88, "TRL": 7, "Strategic Alignment": 8, "Patent Activity": 7, "Partnership Track Record": 6, "Financial Runway (mo)": 21, "Funding ($M)": 48, "Website": "voltmile.io", "Description": "EV fleet leasing and charging-as-a-service platform for SME delivery operators"},
        {"Company": "CleanHaul", "Cluster": "Last-Mile Electrification", "Region": "Chicago", "Stage": "Seed", "Founded": 2023, "Employees": 8, "TRL": 3, "Strategic Alignment": 6, "Patent Activity": 2, "Partnership Track Record": 1, "Financial Runway (mo)": 7, "Funding ($M)": 2, "Website": "cleanhaul.io", "Description": "Carbon credit tracking and reporting platform for electrified delivery fleets"},
        {"Company": "NordCharge", "Cluster": "Last-Mile Electrification", "Region": "Research Triangle", "Stage": "Series A", "Founded": 2021, "Employees": 41, "TRL": 6, "Strategic Alignment": 7, "Patent Activity": 5, "Partnership Track Record": 4, "Financial Runway (mo)": 15, "Funding ($M)": 21, "Website": "nordcharge.io", "Description": "Cold-weather optimized charging solutions for EV fleets in northern US logistics hubs"},
        {"Company": "PortalEV", "Cluster": "Last-Mile Electrification", "Region": "Silicon Valley", "Stage": "Series B", "Founded": 2018, "Employees": 102, "TRL": 8, "Strategic Alignment": 8, "Patent Activity": 7, "Partnership Track Record": 7, "Financial Runway (mo)": 24, "Funding ($M)": 72, "Website": "portalev.com", "Description": "Bidirectional EV charging integration for commercial fleet depots with grid balancing"},
    ]
    return pd.DataFrame(companies)

df = load_data()

STAGE_ORDER = ["Seed", "Series A", "Series B", "Series C"]
CLUSTER_COLORS = {
    "Battery Management": "#1D9E75",
    "Autonomous Freight": "#378ADD",
    "Telematics": "#BA7517",
    "Last-Mile Electrification": "#D85A30",
}

def compute_score(row, weights):
    dims = ["TRL", "Strategic Alignment", "Patent Activity",
            "Partnership Track Record", "Financial Runway (mo)"]
    norms = {
        "TRL": row["TRL"] / 10,
        "Strategic Alignment": row["Strategic Alignment"] / 10,
        "Patent Activity": row["Patent Activity"] / 10,
        "Partnership Track Record": row["Partnership Track Record"] / 10,
        "Financial Runway (mo)": min(row["Financial Runway (mo)"] / 36, 1.0),
    }
    total_w = sum(weights.values())
    score = sum(norms[d] * weights[d] for d in dims) / total_w
    return round(score * 100, 1)

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Filters")
    clusters = st.multiselect(
        "Technology cluster",
        options=df["Cluster"].unique().tolist(),
        default=df["Cluster"].unique().tolist()
    )
    stages = st.multiselect(
        "Funding stage",
        options=STAGE_ORDER,
        default=STAGE_ORDER
    )
    regions = st.multiselect(
        "Region",
        options=sorted(df["Region"].unique().tolist()),
        default=sorted(df["Region"].unique().tolist())
    )
    min_runway = st.slider("Min financial runway (months)", 0, 40, 0)

    st.markdown("---")
    st.markdown("### Scoring weights")
    st.caption("Adjust to reflect strategic priorities")
    w_trl = st.slider("Technology readiness (TRL)", 1, 10, 8)
    w_sa  = st.slider("Strategic alignment", 1, 10, 9)
    w_pa  = st.slider("Patent activity", 1, 10, 5)
    w_ptr = st.slider("Partnership track record", 1, 10, 7)
    w_fr  = st.slider("Financial runway", 1, 10, 6)

weights = {
    "TRL": w_trl,
    "Strategic Alignment": w_sa,
    "Patent Activity": w_pa,
    "Partnership Track Record": w_ptr,
    "Financial Runway (mo)": w_fr,
}

filtered = df[
    df["Cluster"].isin(clusters) &
    df["Stage"].isin(stages) &
    df["Region"].isin(regions) &
    (df["Financial Runway (mo)"] >= min_runway)
].copy()

filtered["Score"] = filtered.apply(lambda r: compute_score(r, weights), axis=1)
filtered = filtered.sort_values("Score", ascending=False).reset_index(drop=True)
filtered["Rank"] = filtered.index + 1

# ── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("## InnoScout — Technology Scouting Dashboard")
st.caption("CampX Innovation | North American Transport Technology Ecosystem | 4 Clusters · 6 Regions · 40 Companies")

# ── METRICS ───────────────────────────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Companies in view", len(filtered))
c2.metric("Avg score", f"{filtered['Score'].mean():.1f}" if len(filtered) else "—")
c3.metric("Top scorer", filtered.iloc[0]["Company"] if len(filtered) else "—")
c4.metric("Total funding ($M)", f"${filtered['Funding ($M)'].sum():.0f}M")
c5.metric("Shortlist (score ≥ 75)", len(filtered[filtered["Score"] >= 75]))

st.markdown("---")

# ── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Ranked shortlist", "Landscape map", "Scoring breakdown", "Compare companies", "Data preview"
])

# TAB 1 — RANKED TABLE
with tab1:
    st.markdown("#### Ranked company shortlist")
    st.caption("Scores recalculate live when sidebar weights change.")

    display_cols = ["Rank", "Company", "Cluster", "Region", "Stage",
                    "Funding ($M)", "Employees", "Score", "Description"]
    styled = filtered[display_cols].copy()

    def color_score(val):
        if val >= 75: return "background-color: #E1F5EE; color: #085041"
        if val >= 60: return "background-color: #FAEEDA; color: #633806"
        return "background-color: #FCEBEB; color: #501313"

    st.dataframe(
        styled.style.map(color_score, subset=["Score"]),
        use_container_width=True,
        hide_index=True,
        height=480
    )

    csv = filtered.to_csv(index=False).encode()
    st.download_button("Download full list as CSV", csv, "innoscout_results.csv", "text/csv")

# TAB 2 — BUBBLE MAP
with tab2:
    st.markdown("#### Ecosystem landscape — funding vs. score")
    st.caption("Bubble size = number of employees. Color = technology cluster.")

    if len(filtered) == 0:
        st.info("No companies match current filters.")
    else:
        fig = px.scatter(
            filtered,
            x="Funding ($M)",
            y="Score",
            size="Employees",
            color="Cluster",
            color_discrete_map=CLUSTER_COLORS,
            hover_name="Company",
            hover_data={"Region": True, "Stage": True, "Description": True,
                        "Employees": True, "Score": True},
            size_max=40,
            template="simple_white",
        )
        fig.add_hline(y=75, line_dash="dash", line_color="#888",
                      annotation_text="Shortlist threshold (75)", annotation_position="right")
        fig.update_layout(
            height=480,
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
            margin=dict(t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Regional cluster density")
    if len(filtered) > 0:
        heat = filtered.groupby(["Region", "Cluster"]).size().reset_index(name="Count")
        fig2 = px.density_heatmap(
            heat, x="Region", y="Cluster", z="Count",
            color_continuous_scale="Teal",
            template="simple_white"
        )
        fig2.update_layout(height=300, margin=dict(t=20, b=40))
        st.plotly_chart(fig2, use_container_width=True)

# TAB 3 — SCORING BREAKDOWN
with tab3:
    st.markdown("#### Dimension scoring breakdown — top 15 companies")
    if len(filtered) == 0:
        st.info("No companies match current filters.")
    else:
        top15 = filtered.head(15)
        dims = ["TRL", "Strategic Alignment", "Patent Activity",
                "Partnership Track Record", "Financial Runway (mo)"]
        norm_top = top15[["Company"] + dims].copy()
        norm_top["TRL"] = norm_top["TRL"] / 10 * 100
        norm_top["Strategic Alignment"] = norm_top["Strategic Alignment"] / 10 * 100
        norm_top["Patent Activity"] = norm_top["Patent Activity"] / 10 * 100
        norm_top["Partnership Track Record"] = norm_top["Partnership Track Record"] / 10 * 100
        norm_top["Financial Runway (mo)"] = (norm_top["Financial Runway (mo)"] / 36).clip(upper=1) * 100

        melted = norm_top.melt(id_vars="Company", var_name="Dimension", value_name="Score (normalized)")
        fig3 = px.bar(
            melted,
            x="Score (normalized)",
            y="Company",
            color="Dimension",
            orientation="h",
            template="simple_white",
            barmode="group",
            color_discrete_sequence=["#1D9E75","#378ADD","#BA7517","#D85A30","#7F77DD"],
        )
        fig3.update_layout(height=520, margin=dict(t=20, b=40),
                           legend=dict(orientation="h", yanchor="bottom", y=1.02))
        st.plotly_chart(fig3, use_container_width=True)

# TAB 4 — COMPARE
with tab4:
    st.markdown("#### Side-by-side company comparison")
    all_names = filtered["Company"].tolist()
    if len(all_names) < 2:
        st.info("Filter results must include at least 2 companies to compare.")
    else:
        defaults = all_names[:3] if len(all_names) >= 3 else all_names[:2]
        selected = st.multiselect(
            "Select 2–4 companies to compare",
            options=all_names,
            default=defaults,
            max_selections=4
        )
        if len(selected) >= 2:
            comp = filtered[filtered["Company"].isin(selected)].set_index("Company")
            dims = ["TRL", "Strategic Alignment", "Patent Activity",
                    "Partnership Track Record", "Financial Runway (mo)", "Score",
                    "Funding ($M)", "Employees", "Stage", "Region", "Cluster"]
            st.dataframe(comp[dims].T, use_container_width=True)

            st.markdown("##### Radar comparison")
            radar_dims = ["TRL", "Strategic Alignment", "Patent Activity",
                          "Partnership Track Record"]
            fig4 = go.Figure()
            for name in selected:
                row = comp.loc[name]
                vals = [row[d] for d in radar_dims]
                vals.append(vals[0])
                fig4.add_trace(go.Scatterpolar(
                    r=vals,
                    theta=radar_dims + [radar_dims[0]],
                    fill="toself",
                    name=name,
                    opacity=0.6
                ))
            fig4.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                template="simple_white",
                height=420,
                legend=dict(orientation="h", yanchor="bottom", y=1.05)
            )
            st.plotly_chart(fig4, use_container_width=True)

            st.markdown("##### Partnership recommendation")
            for name in selected:
                row = comp.loc[name]
                score = row["Score"]
                if score >= 75:
                    rec = "Recommended for Partnership — strong strategic fit and execution readiness"
                    color = "#E1F5EE"
                elif score >= 60:
                    rec = "Watch List — monitor for 6 months, revisit at next funding round"
                    color = "#FAEEDA"
                else:
                    rec = "Pass — insufficient strategic alignment or financial runway at this stage"
                    color = "#FCEBEB"
                st.markdown(
                    f"<div style='background:{color};padding:10px 14px;border-radius:8px;"
                    f"margin-bottom:6px;font-size:13px'>"
                    f"<b>{name}</b> ({score}/100) — {rec}</div>",
                    unsafe_allow_html=True
                )

# TAB 5 — DATA PREVIEW
with tab5:
    st.markdown("#### Raw dataset preview")
    st.caption("Full underlying dataset used by the scoring model. All 40 companies across 4 clusters and 6 regions.")

    col1, col2, col3 = st.columns(3)
    preview_cluster = col1.selectbox(
        "Filter by cluster",
        options=["All"] + sorted(df["Cluster"].unique().tolist())
    )
    preview_stage = col2.selectbox(
        "Filter by stage",
        options=["All"] + STAGE_ORDER
    )
    preview_region = col3.selectbox(
        "Filter by region",
        options=["All"] + sorted(df["Region"].unique().tolist())
    )

    preview_df = df.copy()
    if preview_cluster != "All":
        preview_df = preview_df[preview_df["Cluster"] == preview_cluster]
    if preview_stage != "All":
        preview_df = preview_df[preview_df["Stage"] == preview_stage]
    if preview_region != "All":
        preview_df = preview_df[preview_df["Region"] == preview_region]

    st.markdown(f"Showing **{len(preview_df)}** of **{len(df)}** companies")

    raw_cols = ["Company", "Cluster", "Region", "Stage", "Founded",
                "Employees", "Funding ($M)", "TRL", "Strategic Alignment",
                "Patent Activity", "Partnership Track Record",
                "Financial Runway (mo)", "Website", "Description"]
    st.dataframe(preview_df[raw_cols].reset_index(drop=True),
                 use_container_width=True, hide_index=True, height=420)

    st.markdown("#### Dimension distributions")
    dist_dim = st.selectbox(
        "Select dimension to visualize",
        options=["TRL", "Strategic Alignment", "Patent Activity",
                 "Partnership Track Record", "Financial Runway (mo)", "Funding ($M)"]
    )
    fig5 = px.histogram(
        preview_df,
        x=dist_dim,
        color="Cluster",
        color_discrete_map=CLUSTER_COLORS,
        nbins=10,
        template="simple_white",
        barmode="overlay",
        opacity=0.75
    )
    fig5.update_layout(height=300, margin=dict(t=20, b=40),
                       legend=dict(orientation="h", yanchor="bottom", y=1.02))
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("#### Summary statistics")
    stat_cols = ["TRL", "Strategic Alignment", "Patent Activity",
                 "Partnership Track Record", "Financial Runway (mo)", "Funding ($M)", "Employees"]
    st.dataframe(
        preview_df[stat_cols].describe().round(2),
        use_container_width=True
    )
