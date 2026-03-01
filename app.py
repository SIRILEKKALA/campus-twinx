import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, IsolationForest
import matplotlib.pyplot as plt

st.set_page_config(page_title="CampusTwinX", layout="wide")

# ----------------------------
# LOAD DATA
# ----------------------------
data = pd.read_csv("campus_data.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

# ----------------------------
# ZONE SELECTION
# ----------------------------
st.markdown("## 🗺 Campus Digital Layout")
st.caption("Interactive Smart Campus Infrastructure Overview")
st.image(
    "https://storage.icograms.com/templates/thumbnails/campus-map.webp",
    use_container_width=True
)

st.markdown("### 🏢 Select Building / Zone")

colA, colB, colC, colD = st.columns(4)

if "selected_zone" not in st.session_state:
    st.session_state.selected_zone = "Block A"

if colA.button("Block A"):
    st.session_state.selected_zone = "Block A"
if colB.button("Block B"):
    st.session_state.selected_zone = "Block B"
if colC.button("Library"):
    st.session_state.selected_zone = "Library"
if colD.button("Hostel"):
    st.session_state.selected_zone = "Hostel"

zone_selected = st.session_state.selected_zone
st.markdown(f"### 🛰️ Currently Monitoring: **{zone_selected}**")

# Sidebar simulation
st.sidebar.header("Simulation Controls")
event_multiplier = st.sidebar.slider("Event Load Multiplier", 1.0, 2.0, 1.0)

zone_data = data[data["zone"] == zone_selected].copy()

# ----------------------------
# FEATURE ENGINEERING
# ----------------------------
zone_data["hour"] = zone_data["timestamp"].dt.hour
zone_data["day_of_week"] = zone_data["timestamp"].dt.dayofweek

features = ["hour", "day_of_week"]

# ----------------------------
# TRAIN MODELS
# ----------------------------
energy_model = RandomForestRegressor(n_estimators=100, random_state=42)
energy_model.fit(zone_data[features], zone_data["energy"])

footfall_model = RandomForestRegressor(n_estimators=100, random_state=42)
footfall_model.fit(zone_data[features], zone_data["footfall"])

future_hours = pd.date_range(
    zone_data["timestamp"].iloc[-1],
    periods=24,
    freq="H"
)

future_df = pd.DataFrame()
future_df["timestamp"] = future_hours
future_df["hour"] = future_df["timestamp"].dt.hour
future_df["day_of_week"] = future_df["timestamp"].dt.dayofweek

future_energy = energy_model.predict(future_df[features]) * event_multiplier
future_footfall = footfall_model.predict(future_df[features]) * event_multiplier

# ----------------------------
# ANOMALY DETECTION
# ----------------------------
iso = IsolationForest(contamination=0.02, random_state=42)
zone_data["anomaly"] = iso.fit_predict(zone_data[["energy"]])
anomalies = zone_data[zone_data["anomaly"] == -1]

# ----------------------------
# CALCULATE METRICS
# ----------------------------
avg_energy = zone_data["energy"].mean()
peak_energy = max(future_energy)

avg_footfall = zone_data["footfall"].mean()
peak_footfall = max(future_footfall)

status_color = "🟢"
if peak_energy > avg_energy * 1.3 or peak_footfall > avg_footfall * 1.4:
    status_color = "🔴"

# ----------------------------
# KPI SECTION
# ----------------------------
st.markdown(f"## {status_color} {zone_selected} – Live Infrastructure Status")

c1, c2, c3 = st.columns(3)
c1.metric("Avg Energy", round(avg_energy, 2))
c2.metric("Avg Footfall", round(avg_footfall, 2))
c3.metric("Anomalies Detected", len(anomalies))

# ----------------------------
# HISTORICAL ENERGY
# ----------------------------
st.markdown("### 📈 Historical Energy Usage (with Anomalies)")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(zone_data["timestamp"], zone_data["energy"], label="Energy")
ax.scatter(anomalies["timestamp"], anomalies["energy"], color="red", label="Anomaly")
ax.legend()
st.pyplot(fig)

# ----------------------------
# HISTORICAL FOOTFALL
# ----------------------------
st.markdown("### 📈 Historical Footfall")
st.line_chart(zone_data.set_index("timestamp")["footfall"])

# ----------------------------
# FORECAST SECTION
# ----------------------------
st.markdown("### 🔮 Next 24 Hours Energy Forecast")
st.line_chart(pd.DataFrame({
    "timestamp": future_df["timestamp"],
    "predicted_energy": future_energy
}).set_index("timestamp"))

st.markdown("### 🔮 Next 24 Hours Footfall Forecast")
st.line_chart(pd.DataFrame({
    "timestamp": future_df["timestamp"],
    "predicted_footfall": future_footfall
}).set_index("timestamp"))

# ----------------------------
# RECOMMENDATION ENGINE
# ----------------------------
st.markdown("### 🤖 AI Optimization Suggestion")

if peak_energy > avg_energy * 1.3:
    st.warning(
        f"⚠ Predicted energy surge in {zone_selected}. "
        "Recommend rescheduling high-load activities or redistributing power usage."
    )
elif peak_footfall > avg_footfall * 1.4:
    st.warning(
        f"⚠ High occupancy expected in {zone_selected}. "
        "Suggest alternate space allocation to reduce congestion."
    )
else:
    st.success(f"✅ {zone_selected} operating within optimal predicted range.")

st.caption("🧠 CampusTwinX – AI-driven Smart Campus Decision Support Prototype")