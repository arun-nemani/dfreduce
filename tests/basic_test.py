from unittest import TestCase
from dfreduce.core import DFReduce

try:
    import pandas as pd
    import numpy as np
except ImportError:
    pass


class TestBasic(TestCase):

    def test_check_dataframe_type(self):
        df = 'test'
        with self.assertRaises(ValueError):
            DFReduce(df).reduce()

    def test_numerical_values_equality(self):
        df = pd.DataFrame(np.random.randn(100000, 5), columns=['a', 'b', 'c', 'd', 'e'])

        test_df = DFReduce(df).reduce()
        self.assertEqual(np.isclose(df, test_df, rtol=1e-7, atol=1e-7, equal_nan=False).all(), True)  # noqa: E501

    def test_string_values_equality(self):
        df = pd.DataFrame(np.random.randn(100000, 1), columns=['a'])
        df.a = df.a.astype(np.str)
        test_df = DFReduce(df).reduce()
        self.assertEqual((test_df.a == df.a).all(), True)

    def test_string_type(self):
        df = pd.DataFrame(np.random.randn(100000, 1), columns=['a'])
        df.a = df.a.astype(np.str)
        test_df = DFReduce(df).reduce()
        self.assertEqual(test_df.a.dtype.name, 'object')

    def test_cat_type(self):
        df = pd.DataFrame(['test'] * 100, columns=['a'])
        test_df = DFReduce(df).reduce()
        self.assertEqual(test_df.a.dtype.name, 'category')
