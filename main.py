#%% Libs
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from statsforecast.utils import AirPassengersDF
import numpy as np
import pandas as pd

#%% Read in data
#https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_complete.html
df = pd.read_csv("three_months_energy_usage_data.csv")
df = df.rename(columns={"DateTime":"ds","EnergyUsage_MJ":"y"})
df["unique_id"] = "A1"

# %%
sf = StatsForecast(
    models = [AutoARIMA(season_length = 24)],
    freq = 'H'
)

#%%
sf.fit(df)
predictions = sf.predict(h=48, level=[90])

# %%
predictions.plot(x='ds',y='AutoARIMA')
# %%
