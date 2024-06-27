# %% Libs
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# %% Read in data
# https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_complete.html
# df = pd.read_csv("three_months_energy_usage_data.csv").rename(columns={"DateTime": "ds", "EnergyUsage_MJ": "y"})
df = pd.read_csv("pjm_hourly_est.csv").rename(
    columns={"Datetime": "ds", "PJM_Load": "y"}
)
df["unique_id"] = "A1"
df = df.sort_values(by="ds", ascending=True)
df

# %% Set parameters
sf = StatsForecast(models=[AutoARIMA(season_length=24)], freq="H")

# split dataset into train and test
train_df, test_df = train_test_split(df, test_size=0.1, shuffle=False, stratify=None)

# %% predictions
sf.fit(train_df.tail(1000))
predictions = sf.predict(h=100, level=[75])

# %% Plot predictions
predictions.plot(x="ds", y="AutoARIMA")

# %% Examine with sample data
test_df[0:100].plot(x="ds", y="y")

# %%
