# test for convert.py
# use pytest

import pytest

import numpy as np
from convert import *


def test_convert_str_to_list():
    assert convert_str_to_list("1,2,3", "int") == [1, 2, 3]
    assert convert_str_to_list("1.0,2.0,3.0", "float") == [1.0, 2.0, 3.0]
    assert convert_str_to_list("a,b,c", "str") == ["a", "b", "c"]

def test_convert_list_to_numpy():
    # listがnumpy配列に変換できるか
    assert convert_list_to_numpy([1, 2, 3]).dtype == np.int32
    assert convert_list_to_numpy([1.0, 2.0, 3.0]).dtype == np.float64

    # listの要素にint, float以外のが含まれている場合場合，警告を出して変換しない
    with pytest.warns(UserWarning):
        assert convert_list_to_numpy(["a", "b", "c"]) == ["a", "b", "c"]
        assert convert_list_to_numpy([1, 2.0, "c"]) == [1, 2.0, "c"]

    # listの要素にfloatが含まれる場合，float型のnumpy配列に変換する
    assert convert_list_to_numpy([1, 2.0, 3]).dtype == np.float64


def test_convert_numpy_to_list():
    # numpy配列がlistに変換できるか
    assert convert_numpy_to_list(np.array([1, 2, 3])) == [1, 2, 3]
    assert convert_numpy_to_list(np.array([1.0, 2.0, 3.0])) == [1.0, 2.0, 3.0]
    assert convert_numpy_to_list(np.array(["a", "b", "c"])) == ["a", "b", "c"]