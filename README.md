# dfreduce

Description: Automatically reduce the size of your pandas dataframe

## Installation
pip install dfreduce

## Usage
```
import dfreduce
import pandas as pd

df = pd.read_csv('https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv')
dfr = DFreduce()
df_reduced = dfr.reduce(df)
```

## Uninstallation

```
pip uninstall dfreduce
```