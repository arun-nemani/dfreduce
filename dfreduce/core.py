import pandas as pd
import numpy as np
from tqdm import tqdm


class DFReduce():
    """ Returns a memory efficient copy of an input dataframe """

    def __init__(self, df, inplace=False):
        tqdm.pandas()
        if isinstance(df, pd.DataFrame):
            pass
        else:
            raise ValueError('Input must be a pandas dataframe')
        if isinstance(inplace, bool):
            self._inplace = inplace
        else:
            raise ValueError('Inplace must be either True or False (bool)')

        if self._inplace:
            self.df = df
        else:
            self.df = df.copy()
        self.columns = self.df.columns
        self.int_columns = self.df.dtypes == np.integer
        self.float_columns = self.df.dtypes == np.inexact
        self.obj_columns = self.df.loc[:, self.df.dtypes == object].columns
        self.orig_memory = self.df.memory_usage(deep=True).sum() / 1024 ** 2  # report in MBs # noqa: E501
        self.new_memory = []
        return

    def reduce(self):
        # Reduce ints
        self.df.loc[:, self.int_columns] = self.df.loc[:, self.int_columns].progress_apply(  # noqa: E501
            pd.to_numeric, downcast='signed')

        # Reduce floats
        self.df.loc[:, self.float_columns] = self.df.loc[:, self.float_columns].progress_apply(  # noqa: E501
            pd.to_numeric, downcast='float')

        # Reduce objects to categoricals only when unique values is less than 50% of arr length # noqa: E501
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
