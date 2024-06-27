# %% Libs
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from statsforecast.utils import AirPassengersDF
import numpy as np
import pandas as pd

# %% Read in data
# https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_complete.html
# df = pd.read_csv("three_months_energy_usage_data.csv").rename(columns={"DateTime": "ds", "EnergyUsage_MJ": "y"})
df = pd.read_csv("pjm_hourly_est.csv").rename(
    columns={"Datetime": "ds", "PJM_Load": "y"}
)
df["unique_id"] = "A1"
df = df[0:32895]
df

# %% Set parameters
sf = StatsForecast(models=[AutoARIMA(season_length=24)], freq="H")

# %% predictions
sf.fit(df)
predictions = sf.predict(h=96, level=[75])

# %% Plot predictions
predictions.plot(x="ds", y="AutoARIMA")

# %% Examine with sample data
df[0:152].plot(x="ds", y="y")

# %%
