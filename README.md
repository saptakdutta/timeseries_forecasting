# timeseries_forecasting

## Getting started

The best way to get darts set up for me has been to create a new blank virtual environment

> conda create -n timeseries_forecasting

Then add in darts and let the conda-forge channel take care of the dependencies

> conda install -c conda-forge -c pytorch u8darts-all

This method is still hit or miss. On some older systems (e.g., GPUs that do not support CTK 12), WSL2 etc it seems to not install the correct pytorch and pytorch lightning with GPU accelerated libraries. It may also be that WSL2 messes up the conda-forge installer and causes it to incorrectly download pytorch lightning versions. For best results it's recommended to use a debian based bare metal linux system