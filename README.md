# timeseries_forecasting

## Installation
------------------------------------------New Method--------------------------------------------
1. Install conda-lock on your base environment: 
   > conda install --channel=conda-forge --name=base conda-lock
2. Activate conda: 
   > e.g, conda activate
3. Use the provided lock file to generate an exact replica of the target environment: 
   > conda-lock install --n env_name_here conda-lock.yml
4. To remove this environment use: 
   > conda remove -n env_name_here --all 
------------------------------------------Old Method--------------------------------------------
1. to create this venv run: conda env create -f environment.yml --solver=libmamba || mamba env create -f environment.yml
2. to destroy this venv run: conda remove -n env_name_here --all || mamba remove -n env_name_here --all