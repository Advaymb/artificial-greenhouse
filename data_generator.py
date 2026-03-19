import pandas as pd
import numpy as np
from datetime import datetime

#data bounds
START_DATE = datetime(2026, 1, 1, 0, 0)
END_DATE = datetime(2026, 1, 7, 23, 45)
FREQ_MINUTES = 15

BOUNDS = {
    "Cum_irr": (0, 1),           #Cumulative irrigation (L)
    "EC_drain_PC": (2.0, 4.0),   #Drainage EC (mS/cm)
    "Rhair": (70, 90),           #Relative humidity (%)
    "Tair": (14, 26),            #Air temperature (°C)
    "Tot_PAR": (0, 350),         #Total PAR (μmol/m2/s)
    "pH_drain_PC": (4.5, 6.7),   #Drainage pH
}


date_range = pd.date_range(start=START_DATE, end=END_DATE, freq=f"{FREQ_MINUTES}min")
n = len(date_range)

#generation loop
data = {
    "%time": [dt.toordinal() + dt.hour/24 + dt.minute/(24*60) for dt in date_range]
}
for col, (low, high) in BOUNDS.items():
    if col == "Cum_irr":
        continue
    if col == "Tair":
        tair_vals = []
        for dt in date_range:
            hour = dt.hour + dt.minute / 60
            amplitude = (high - low) / 2
            midpoint = (high + low) / 2
            radians = ((hour - 15) / 24) * 2 * np.pi
            base_temp = midpoint + amplitude * np.cos(radians)
            temp = np.clip(base_temp + np.random.normal(0, 1), low, high)
            tair_vals.append(round(temp, 2))
        data[col] = tair_vals
    if col == "Tot_PAR":
        tot_par_vals = []
        for dt in date_range:
            hour = dt.hour + dt.minute / 60
            amplitude = (high - low) / 4
            midpoint = (high + low) / 2
            radians = ((hour - 15) / 24) * 2 * np.pi
            base_temp = midpoint + amplitude * np.cos(radians)
            par = np.clip(base_temp + np.random.normal(0, (high - low) / 30), low, high)
            tot_par_vals.append(round(par, 2))
        data[col] = tot_par_vals
    else:
        vals = [np.random.uniform(low, high)]
        for _ in range(1, n):
            step = np.random.normal(0, (high-low)/40)
            next_val = np.clip(vals[-1] + step, low, high)
            vals.append(next_val)
        data[col] = np.round(vals, 2)

cum_irr_vals = []
first_date = date_range[0].date()
for dt in date_range:
    days_since_start = (dt.date() - first_date).days
    if (days_since_start % 2 == 0) and (dt.hour == 8) and (dt.minute == 0):
        set_irrigation = True
    # At midnight, reset irrigation flag
    if (dt.hour == 0) and (dt.minute == 0):
        set_irrigation = False
    if set_irrigation:
        cum_irr_vals.append(0.6)
    else:
        cum_irr_vals.append(0.0)
data["Cum_irr"] = cum_irr_vals

df = pd.DataFrame(data)
df = df[["%time"] + list(BOUNDS.keys())]

df.to_csv("generated_greenhouse_data.csv", index=False)
print(f"Generated {n} rows in generated_greenhouse_data.csv")