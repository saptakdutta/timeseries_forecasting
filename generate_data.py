# %% Libs
import pandas as pd
import numpy as np

# %% Define the time range (3 months)
hours = pd.date_range(start="2023-01-01", periods=2160, freq="H")

# Initialize the energy usage array
energy_usage = np.zeros(2160)

# %% Populate the energy usage data
# Populate the energy usage data
for i in range(2160):
    hour_of_day = i % 24
    if 0 <= hour_of_day < 12:
        # Energy increases from 10 MJ to 100 MJ
        energy_usage[i] = 10 + (90 / 11) * hour_of_day
    elif 12 <= hour_of_day < 17:
        # Energy decreases from 100 MJ to 50 MJ
        energy_usage[i] = 100 - (50 / 5) * (hour_of_day - 12)
    else:
        # Energy decreases from 50 MJ to 10 MJ
        energy_usage[i] = 50 - (40 / 7) * (hour_of_day - 17)

# Create a DataFrame
df = pd.DataFrame({"DateTime": hours, "EnergyUsage_MJ": energy_usage})

# %% Print the DataFrame
print(df.head(24))  # Print the first day as a sample
df.to_csv("three_months_energy_usage_data.csv", index=False)

# %%
