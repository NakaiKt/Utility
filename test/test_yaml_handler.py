# test fof yaml_handler.py
# use pytest
"""
defaultのyamlファイル内容

test: test
bool: True
int: 100
float: 3.33

"""

import pytest
from yaml_handler import *


def test_write_yaml():
    contents = {
        "test": "test2",
        "bool": False,
        "test_write": "test2"
    }
    # yamlファイルの内容を書き換える
    write_yaml("./test/test.yaml", contents)
    assert load_yaml("test/test.yaml") == {
        "test": "test2",
        "bool": False,
        "int": 100,
        "float": 3.33,
        "test_write": "test2"
    }

    # yamlファイルの内容をdefaultに戻す
    contents = {
        "test": "test",
        "bool": True,
        "test_write": None
    }
    write_yaml("./test/test.yaml", contents)
    delete_content_yaml("./test/test.yaml", ["test_write"])

    assert load_yaml("./test/test.yaml") == {
        "test": "test",
        "bool": True,
        "int": 100,
        "float": 3.33,
    }

def test_delete_content_yaml():
    pass

def test_load_yaml():
    assert load_yaml("./test/test.yaml") == {
        "test": "test",
        "bool": True,
        "int": 100,
        "float": 3.33,
    }

def test_load_yaml():
    pass

def test_delete_content_yaml():
    pass

def test_failed_load_yaml():
    with pytest.raises(FileNotFoundError):
        load_yaml("./test/test2.yaml")

def test_failed_write_yaml():
    with pytest.raises(FileNotFoundError):
        write_yaml("./test/test2.yaml", {"test": "test"})

def test_failed_delete_content_yaml():
    with pytest.raises(FileNotFoundError):
        delete_content_yaml("./test/test2.yaml", ["test"])
    
    with pytest.raises(KeyError):
        delete_content_yaml("./test/test.yaml", ["test2"])