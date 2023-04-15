# test for list_handler.py
# use pytest

import pytest

from list_handler import *

def test_list_value_distribution():
    test_list = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    assert list_value_distribution(test_list) == {1: 2, 2: 1, 3: 3, 4: 4}