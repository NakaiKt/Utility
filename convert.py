import base64
import json
import warnings

import numpy as np


def convert_str_to_list(input: str, format="int") -> list:
    """文字列をリストに変換する関数

    Args:
        input (str): 変換する文字列
        format (str): 変換する型

    Returns:
        list: 変換後のリスト
    """
    if format == "int":
        return [int(i) for i in input.split(",")]
    elif format == "float":
        return [float(i) for i in input.split(",")]
    elif format == "str":
        return [str(i) for i in input.split(",")]
    else:
        raise ValueError("format must be int, float or str")
    
def convert_list_to_numpy(input: list) -> np.ndarray:
    """リストをnumpy配列に変換する関数

    Args:
        input (list): 変換するリスト

    Returns:
        np.ndarray: 変換後のnumpy配列
    """
    # listの要素にint, float以外の型が含まれる場合，警告を出して変換しない
    if not all(isinstance(i, (int, float)) for i in input):
        warnings.warn(UserWarning("list's element is not int or float"))
        return input

    # listの要素にfloatが含まれる場合，float型のnumpy配列に変換する
    elif isinstance(input[0], float) or any(isinstance(i, float) for i in input):
        return np.array(input, dtype=np.float64)

    return np.array(input)

def convert_numpy_to_list(input: np.ndarray) -> list:
    """numpy配列をリストに変換する関数

    Args:
        input (np.ndarray): 変換するnumpy配列

    Returns:
        list: 変換後のリスト
    """
    return input.tolist()

def convert_dict_to_json(input: dict) -> str:
    """辞書をjson文字列に変換する関数

    Args:
        input (dict): 変換する辞書

    Returns:
        str: 変換後のjson文字列
    """
    # inputがdictでない場合，警告を出す
    if not isinstance(input, dict):
        warnings.warn(UserWarning("input is not dict"))
    return json.dumps(input)

def convert_json_to_dict(input: str) -> dict:
    """json文字列を辞書に変換する関数

    Args:
        input (str): 変換するjson文字列

    Returns:
        dict: 変換後の辞書
    """
    return json.loads(input)

def convert_numpy_to_base64(input: np.ndarray) -> str:
    """画像をbase64文字列に変換する関数
    Args:
        input (np.ndarray): 変換する画像
    Returns:
        str: 変換後のbase64文字列
    """
    # inputがnumpy配列でない場合，TypeError
    if not isinstance(input, np.ndarray):
        raise TypeError(f"input is not numpy.ndarray. type: {type(input)}")

    return base64.b64encode(input).decode("utf-8")


def convert_base64_to_numpy(input: str, width: int, height: int, channel = 3) -> np.ndarray:
    """base64文字列を画像に変換する関数
    Args:
        input (str): 変換するbase64文字列
        height (int): 高さ
        width (int): 幅
        channel (int): カラーチャンネル数

    Returns:
        np.ndarray: 変換後の画像
    """
    if type(input) != str:
        raise TypeError(f"base64 -> ndarrayの変換の入力はstrである必要があります. 入力された型{type(input)}")
    image = base64.b64decode(input)
    # binary の imageをnumpy配列に変換する
    image = np.frombuffer(image, dtype=np.uint8)

    # numpy配列を画像にリサイズ
    image = image.reshape([height, width, channel])
    return image
