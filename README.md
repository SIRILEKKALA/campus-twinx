# 🏫 CampusTwinX – AI-Powered Smart Campus Digital Twin

## 📌 Overview

CampusTwinX is an AI-driven Smart Campus Digital Twin prototype that models campus infrastructure as intelligent, predictive zones.

The system monitors energy consumption and footfall patterns, forecasts future demand, detects anomalies, and generates proactive optimization recommendations.

This prototype demonstrates how AI can transform traditional campuses into sustainable, data-driven smart environments.

---

## 🚀 Problem Statement

University campuses operate like micro-cities with:

* Fluctuating energy consumption
* Dynamic building occupancy
* Reactive infrastructure management
* Limited predictive planning

Inefficient monitoring can lead to:

* Energy waste
* Infrastructure overload
* Safety risks during peak occupancy
* Increased operational costs

CampusTwinX addresses this by enabling predictive and intelligent infrastructure decision-making.

---

## 🧠 Solution Architecture

Multi-Zone Data
↓
Feature Engineering (Time-based features: hour, weekday)
↓
Random Forest Forecasting Models (Energy & Footfall)
↓
Isolation Forest Anomaly Detection
↓
Simulation Engine (Event Load Multiplier)
↓
AI Optimization Recommendation System
↓
Interactive Streamlit Digital Twin UI

---

## 🤖 AI Models Used

### 1️⃣ RandomForestRegressor

* Predicts next 24-hour energy consumption
* Predicts next 24-hour building occupancy (footfall)
* Handles nonlinear time-based patterns efficiently
* Suitable for structured time-series forecasting in prototype environments

### 2️⃣ IsolationForest

* Detects abnormal energy spikes
* Identifies potential overload or unusual consumption behavior
* Enables proactive infrastructure monitoring

---

## 🏢 Smart Campus Zones Modeled

* Block A
* Block B
* Library
* Hostel

Each zone is independently modeled with its own predictive engine and infrastructure health metrics.

---

## ⚙️ Simulation Capability

The Event Load Multiplier allows simulation of:

* Campus fests
* Examination peaks
* High-occupancy events
* Infrastructure stress testing

This enables scenario-based predictive planning.

---

## 📊 Key Features

✔ Multi-zone digital twin architecture
✔ Energy forecasting (24-hour predictive model)
✔ Occupancy forecasting
✔ Real-time anomaly detection
✔ AI-generated infrastructure recommendations
✔ Interactive visual campus layout
✔ Scalable modular architecture

---

## 🔮 Future Scope (Full Proposal Vision)

This prototype interface represents a visualization layer.

The full-scale proposal includes:

* Real-time IoT sensor integration
* Smart meter data streaming
* Occupancy sensors
* Live environmental data feeds
* Fully interactive 3D campus digital twin rendering
* Edge-deployable AI inference for low-latency decisions

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* RandomForest & IsolationForest
* Matplotlib

---

## 🎯 Impact

CampusTwinX enables:

* Predictive infrastructure management
* Energy efficiency optimization
* Occupancy risk reduction
* Data-driven sustainability planning
* Scalable smart campus deployment

This prototype demonstrates how AI can serve as the foundation for intelligent campus ecosystems.

---

## 🧪 How to Run

1. Clone repository
2. Install dependencies

```
pip install -r requirements.txt
```

3. Generate dataset

```
python data_generator.py
```

4. Run application

```
streamlit run app.py
```

---

## 📌 Author

Siri Lekkala
B.Tech CSE – Smart Systems & AI Enthusiast

---

# 🚀 Final Advice

After adding this:

1. Save README
2. Run:

```
git add README.md
git commit -m "Updated professional README"
git push
```


