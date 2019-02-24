from unittest import TestCase
from dfreduce import DFReduce
import numpy as np

try:
    import pandas as pd
except ImportError:
    pass


class BasicTest(TestCase):

    def basic_test(self):
        df = pd.DataFrame(np.random.randn(100000, 5),
                          columns=['a', 'b', 'c', 'd', 'e'])
        dfr = DFReduce()
        test_df = dfr.reduce(df)
        self.assertIsNotNone(test_df)
        self.assertTrue(isinstance(test_df, pd.DataFrame))