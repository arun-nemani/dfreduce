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

    def test_int8_values_equality(self):
        df = pd.DataFrame(np.random.randint(-5, 5, size=[100, 5], dtype='int64'), columns=['a', 'b', 'c', 'd', 'e'])  # noqa: E501
        test_df = DFReduce(df).reduce()
        self.assertEqual(np.isclose(df, test_df, rtol=1e-7, atol=1e-7, equal_nan=False).all(), True)  # noqa: E501

    def test_int8_type_equality(self):
        df = pd.DataFrame(np.random.randint(-5, 5, size=[100, 5], dtype='int64'), columns=['a', 'b', 'c', 'd', 'e'])  # noqa: E501
        test_df = DFReduce(df).reduce()
        self.assertEqual(test_df.a.dtype.name, 'int8')

    def test_int16_type_equality(self):
        df = pd.DataFrame(np.random.randint(-12345, 12345, size=[1000, 5], dtype='int64'), columns=['a', 'b', 'c', 'd', 'e'])  # noqa: E501
        test_df = DFReduce(df).reduce()
        self.assertEqual(test_df.a.dtype.name, 'int16')

    def test_float_values_equality(self):
        df = pd.DataFrame(np.random.randn(100000, 5), columns=['a', 'b', 'c', 'd', 'e'])  # noqa: E501

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

    def test_inplace_param(self):
        df = pd.DataFrame(np.random.randint(-5, 5, size=[100, 5], dtype='int64'), columns=['a', 'b', 'c', 'd', 'e'])  # noqa: E501
        df_copy = df.copy()
        DFReduce(df_copy, inplace=True).reduce()
        self.assertEqual(np.isclose(df, df_copy, rtol=1e-7, atol=1e-7, equal_nan=False).all(), True)  # noqa: E501
