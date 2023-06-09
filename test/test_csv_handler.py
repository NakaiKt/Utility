# test for csv_handler.py
# use pytest

import pytest

from csv_handler import * 

def test_get_column():
    # get_columnの正常テスト
    assert get_column(key_column="key", key=1, csv_file_path="test/test.csv")[0] == "5"
    assert get_column(key_column="key", key="a", csv_file_path="test/test.csv")[0] == "b"
    assert get_column(key_column="key", key=3.0, csv_file_path="test/test.csv")[0] == "4.0"

def test_get_column_fault():
    # get_columnの異常テスト
    with pytest.raises(IndexError):
        get_column(key_column="key", key=3, csv_file_path="test/test.csv")

def test_get_column_value_list():
    # get_column_value_listの正常テスト
    assert get_column_value_list(column_name="key", csv_file_path="test/test.csv") == ['1', "a", '3.0']