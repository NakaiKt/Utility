# test for validation.py
# use pytest

import pytest
from validation import validate_in_list


def test_validate_in_list():
    assert validate_in_list("a", ["a", "b", "c"]) == True
    assert validate_in_list("d", ["a", "b", "c"]) == False
    assert validate_in_list(1, [1, 2, 3]) == True
    assert validate_in_list(4, [1, 2, 3]) == False
    assert validate_in_list(1.0, [1.0, 2.0, 3.0]) == True
    assert validate_in_list(4.0, [1.0, 2.0, 3.0]) == False
