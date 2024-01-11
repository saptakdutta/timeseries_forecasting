#%% Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from darts import TimeSeries
from darts.datasets import AirPassengersDataset
import torch

#%% Load data
series = AirPassengersDataset().load()
print(series.pd_dataframe().head(5))
series.plot()

# %%
