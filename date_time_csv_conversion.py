import pandas as pd

# read CSV
csv_path = "example_greenhouse_data.csv"
df = pd.read_csv(csv_path)

# convert to readable datetime
df["Time_readable"] = pd.to_datetime(df["%time"], origin='1899-12-30', unit='D')
df["Time_readable"] = df["Time_readable"].dt.strftime("%m/%d/%Y %H:%M")

# replace with readable
df_new = df.copy()
df_new = df_new.drop(columns=["%time"])
df_new.insert(0, "%time", df["Time_readable"])

# Save
df_new.to_csv("example_greenhouse_data_readable.csv", index=False)
print("Saved example_greenhouse_data_readable.csv")