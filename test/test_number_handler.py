# test for number_handler.py
# use pytest

import pytest

import numpy as np

from number_handler import *

def test_round_number():
    # 小数点以下を四捨五入できるか
    assert round_number(1.234, 2) == 1.23
    assert round_number(1.235, 2) == 1.24

    # 第二引数で指定した桁数で四捨五入できるか
    assert round_number(1.234, 1) == 1.2
    assert round_number(1.235, 1) == 1.2

def test_floor_number():
    # 小数点以下を切り捨てできるか
    assert floor_number(1.234, 2) == 1.23
    assert floor_number(1.235, 2) == 1.23

    # 第二引数で指定した桁数で切り捨てできるか
    assert floor_number(1.234, 1) == 1.2
    assert floor_number(1.235, 1) == 1.2

def test_ceil_number():
    # 小数点以下を切り上げできるか
    assert ceil_number(1.234, 2) == 1.24
    assert ceil_number(1.235, 2) == 1.24

    # 第二引数で指定した桁数で切り上げできるか
    assert ceil_number(1.234, 1) == 1.3
    assert ceil_number(1.235, 1) == 1.3