import pandas as pd
import numpy as np

np.random.seed(42)

zones = ["Block A", "Block B", "Library", "Hostel"]
hours = 30 * 24
date_range = pd.date_range(start="2026-01-01", periods=hours, freq="H")

rows = []

for zone in zones:
    for timestamp in date_range:
        hour = timestamp.hour
        day = timestamp.dayofweek
        
        base_energy = 100
        base_footfall = 200
        
        if zone == "Library":
            base_energy += 20
            base_footfall += 40
        elif zone == "Hostel":
            base_energy += 10
        
        energy = (
            base_energy +
            40 * (9 <= hour <= 18) +
            20 * (day < 5) +
            np.random.normal(0, 10)
        )
        
        footfall = (
            base_footfall +
            80 * (10 <= hour <= 16) +
            50 * (day < 5) +
            np.random.normal(0, 20)
        )
        
        rows.append([timestamp, zone, energy, footfall])

data = pd.DataFrame(rows, columns=["timestamp", "zone", "energy", "footfall"])
data.to_csv("campus_data.csv", index=False)

print("Multi-zone campus dataset generated!")