# dfreduce

[![PyPI version](https://badge.fury.io/py/dfreduce.svg)](https://badge.fury.io/py/dfreduce)

Description: Automatically reduce the memory size of your pandas dataframe

## Installation
pip install dfreduce

## Usage
```
from dfreduce.core import DFReduce
import pandas as pd

df = pd.read_csv('https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv')
df_reduced = DFReduce(df).reduce()

# Alternatively, you can also use the inplace parameter to overwrite input dataframe
DFReduce(df, inplace=True).reduce()
```

## Uninstallation

```
pip uninstall dfreduce
```
