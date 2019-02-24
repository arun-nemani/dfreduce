import pandas as pd
import numpy as np


class DFReduce:
    """ Returns a memory efficient copy of an input dataframe """

    def __init__(self):
        self.data = []
        self.new_memory = []
        return

    def reduce(self, df):
        if isinstance(df, pd.DataFrame):
            self.data = df.copy()
        else:
            raise ValueError('Input must be a pandas dataframe')

        self.columns = df.columns
        self.int_columns = df.dtypes == np.int
        self.float_columns = df.dtypes == np.float
        self.obj_columns = df.loc[:, df.dtypes == object].columns
        self.orig_memory = df.memory_usage(
            deep=True).sum() / 1024 ** 2  # report in MBs

        # Reduce ints
        self.data.loc[:, self.int_columns] = self.data.loc[:, self.int_columns].apply(
            pd.to_numeric, downcast='unsigned')

        # Reduce floats
        self.data.loc[:, self.float_columns] = self.data.loc[:, self.float_columns].apply(
            pd.to_numeric, downcast='float')

        # Reduce objects to categoricals
        for col in self.obj_columns:
            num_unique_values = len(self.data[col].unique())
            num_total_values = len(self.data[col])
            if num_unique_values / num_total_values < 0.5:
                self.data.loc[:, col] = self.data[col].astype('category')
            else:
                self.data.loc[:, col] = self.data[col]

        self.new_memory = self.data.memory_usage(deep=True).sum() / 1024 ** 2
        print("Memory reduced from {:03.2f} MB to {:03.2f} MB".format(
            self.orig_memory, self.new_memory))
        print("Reduced by {:03.2f}% !!".format(
            100 * (self.orig_memory - self.new_memory) / self.orig_memory))

        return self.data
