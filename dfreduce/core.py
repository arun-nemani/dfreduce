import pandas as pd
import numpy as np
from tqdm import tqdm


class DFReduce:
    """ Returns a memory efficient copy of an input dataframe """

    def __init__(self, df):
        tqdm.pandas()
        if isinstance(df, pd.DataFrame):
            self.df = df.copy()
        else:
            raise ValueError('Input must be a pandas dataframe')
        self.columns = self.df.columns
        self.int_columns = self.df.dtypes == np.int
        self.float_columns = self.df.dtypes == np.float
        self.obj_columns = self.df.loc[:, self.df.dtypes == object].columns
        self.orig_memory = self.df.memory_usage(deep=True).sum() / 1024 ** 2  # report in MBs
        self.new_memory = []
        return

    def reduce(self):
        # Reduce ints
        self.df.loc[:, self.int_columns] = self.df.loc[:, self.int_columns].progress_apply(
            pd.to_numeric, downcast='unsigned')

        # Reduce floats
        self.df.loc[:, self.float_columns] = self.df.loc[:, self.float_columns].progress_apply(
            pd.to_numeric, downcast='float')

        # Reduce objects to categoricals only when unique values is less than 50% of arr length
        for col in tqdm(self.obj_columns):
            num_unique_values = len(self.df[col].unique())
            num_total_values = len(self.df[col])
            if num_unique_values / num_total_values < 0.5:
                self.df.loc[:, col] = self.df[col].astype('category')
            else:
                self.df.loc[:, col] = self.df[col]

        self.new_memory = self.df.memory_usage(deep=True).sum() / 1024 ** 2
        print("Memory reduced from {:03.2f} MB to {:03.2f} MB".format(
            self.orig_memory, self.new_memory))
        print("Reduced by {:03.2f}% !!".format(
            100 * (self.orig_memory - self.new_memory) / self.orig_memory))

        return self.df
