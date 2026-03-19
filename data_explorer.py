import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
csv_path = "generated_greenhouse_data.csv"
df = pd.read_csv(csv_path)

# Create a graph
factors = [col for col in df.columns if col != "%time"]

for factor in factors:
    plt.figure(figsize=(10, 5))
    plt.plot(df["%time"], df[factor], marker='o')
    plt.title(f"{factor} over Time")
    plt.xlabel("Time")
    plt.ylabel(factor)
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    img_filename = f"./graphs/{factor}_over_time.png"
    plt.savefig(img_filename)
    plt.close()
    print(f"Saved {img_filename}")
