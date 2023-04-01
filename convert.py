import numpy as np
import warnings

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

