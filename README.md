# dfreduce

[![PyPI version](https://badge.fury.io/py/dfreduce.svg)](https://badge.fury.io/py/dfreduce)

Description: Automatically reduce the memory size of your pandas dataframe

## Installation
pip install dfreduce

## Usage
```
import dfreduce.core as dfr
import pandas as pd

df = pd.read_csv('https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv')
df_reduced = dfr.DFReduce().reduce(df)
```

## Uninstallation

```
pip uninstall dfreduce
```
