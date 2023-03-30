# test for csv_handler.py
# use pytest

import pytest

from csv_handler import get_column

def test_get_column():
    # get_columnの正常テスト
    assert get_column(key_column="key", key=1, csv_file_path="test.csv")[0] == "5"
    assert get_column(key_column="key", key="a", csv_file_path="test.csv")[0] == "b"
    assert get_column(key_column="key", key=3.0, csv_file_path="test.csv")[0] == "4.0"

def test_get_column_fault():
    # get_columnの異常テスト
    with pytest.raises(IndexError):
        get_column(key_column="key", key=3, csv_file_path="test.csv")