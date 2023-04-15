# test for convert.py
# use pytest

import cv2
import numpy as np
import cv2
from convert import *
from format import TypeWarning


def test_convert_str_to_list():
    """文字列をリストに変換する関数のテスト

    testパターンにはint, float, strの3パターンを用意
    """
    assert convert_str_to_list("1,2,3", "int") == [1, 2, 3]
    assert convert_str_to_list("1.0,2.0,3.0", "float") == [1.0, 2.0, 3.0]
    assert convert_str_to_list("a,b,c", "str") == ["a", "b", "c"]

def test_failed_convert_str_to_list():
    """文字列をリストに変換する関数のFailedテスト
    """
    with pytest.raises(AttributeError):
        convert_str_to_list(3, "int")
    with pytest.raises(ValueError):
        convert_str_to_list("1.2.3", "float")
    with pytest.raises(ValueError):
        convert_str_to_list("1,2,3", "double")

def test_convert_list_to_numpy():
    """リストをnumpy配列に変換する関数のテスト
    """
    # listがnumpy配列に変換できるか
    assert convert_list_to_numpy([1, 2, 3]).dtype == np.int32
    assert convert_list_to_numpy([1.0, 2.0, 3.0]).dtype == np.float64

    # listの要素にint, float以外のが含まれている場合場合，警告を出して変換しない
    with pytest.warns(TypeWarning):
        assert convert_list_to_numpy(["a", "b", "c"]) == ["a", "b", "c"]
        assert convert_list_to_numpy([1, 2.0, "c"]) == [1, 2.0, "c"]

    # listの要素にfloatが含まれる場合，float型のnumpy配列に変換する
    assert convert_list_to_numpy([1, 2.0, 3]).dtype == np.float64

def test_failed_convert_list_to_numpy():
    """リストをnumpy配列に変換する関数のFailedテスト
    """
    with pytest.raises(TypeError):
        convert_list_to_numpy(4)

    with pytest.warns(TypeWarning):
        convert_list_to_numpy("abc")


def test_convert_numpy_to_list():
    # numpy配列がlistに変換できるか
    assert convert_numpy_to_list(np.array([1, 2, 3])) == [1, 2, 3]
    assert convert_numpy_to_list(np.array([1.0, 2.0, 3.0])) == [1.0, 2.0, 3.0]
    assert convert_numpy_to_list(np.array(["a", "b", "c"])) == ["a", "b", "c"]

def test_failed_convert_numpy_to_list():
    """numpy配列をリストに変換する関数のFailedテスト
    """
    with pytest.raises(AttributeError):
        convert_numpy_to_list(4)

    with pytest.raises(AttributeError):
        convert_numpy_to_list("abc")

def test_convert_dict_to_json():
    """dictをjsonに変換する関数のテスト
    """
    assert convert_dict_to_json({"a": 1, "b": 2, "c": 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert convert_dict_to_json({"a":"a", "b":3.0, "c":[1, 2, 3]}) == '{"a": "a", "b": 3.0, "c": [1, 2, 3]}'

    with pytest.warns(TypeWarning):
        convert_dict_to_json(4)

def test_convert_json_to_dict():
    """jsonをdictに変換する関数のテスト
    """
    json_text = convert_dict_to_json({"a": 1, "b": 2, "c": 3})
    assert convert_json_to_dict(json_text) == {"a": 1, "b": 2, "c": 3}

    with pytest.raises(AssertionError):
        assert json_text == {"a": 1, "b": 2, "c": 3}

def test_convert_numpy_to_base64():
    """画像読み込み(np.array) -> base64変換 -> np.array変換
    """
    image = cv2.imread("./images/lena.jpg")
    image_width, image_height = image.shape[1], image.shape[0]
    image_base64 = convert_numpy_to_base64(image)

    assert isinstance(image_base64, str)

    image_recover = convert_base64_to_numpy(image_base64, width=image_width, height=image_height)

    assert isinstance(image_recover, np.ndarray)
    assert image_recover.shape == image.shape
    assert image_recover.all() == image.all()

def test_convert_base64_to_numpy():
    pass

def test_failed_convert_image_to_base64():
    """convert_numpy_to_base64でnp.array以外の入力を入れる
    """
    image = cv2.imread("./images/lena.jpg")
    image_base64 = convert_numpy_to_base64(image)

    with pytest.raises(TypeError):
        convert_numpy_to_base64("a")

    with pytest.raises(TypeError):
        convert_numpy_to_base64(1)

    with pytest.raises(TypeError):
        convert_numpy_to_base64([1, 2, 3])

    with pytest.raises(TypeError):
        convert_numpy_to_base64(image_base64)