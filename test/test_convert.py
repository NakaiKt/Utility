# test for convert.py
# use pytest

import pytest

from convert import convert_str_to_list


def test_convert_str_to_list():
    assert convert_str_to_list("1,2,3", "int") == [1, 2, 3]
    assert convert_str_to_list("1.0,2.0,3.0", "float") == [1.0, 2.0, 3.0]
    assert convert_str_to_list("a,b,c", "str") == ["a", "b", "c"]
