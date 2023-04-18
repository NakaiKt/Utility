# test for json handler
# use pytest

import pytest
from json_handler import *

def test_load_json():
    """JSONファイルを読み込む関数のテスト
    jsonファイルはtest.jsonを用いる

    test.jsonの内容
    {
    "name": "jquery-1.7.2.js",
    "version": "1.7.2",
    "description": "jQuery JavaScript Library v1.7.2",
    "main": "jquery-1.7.2.js",
    "directories": {
        "example": "examples"
    }
}
    """
    # test.jsonのパス
    test_json_path = './test/test.json'
    # test.jsonの内容
    test_json_content = {
        "name": "jquery-1.7.2.js",
        "version": "1.7.2",
        "description": "jQuery JavaScript Library v1.7.2",
        "main": "jquery-1.7.2.js",
        "directories": {
            "example": "examples"
        }
    }
    # test.jsonを読み込む
    test_json = load_json(test_json_path)
    # test.jsonの内容が正しいか確認
    assert test_json == test_json_content