import numpy as np


def round_number(input: float, digit: int) -> float:
    """小数点以下を四捨五入する関数
    第二引数で指定した桁数で四捨五入する
    
    Args:
        input (float): 四捨五入する数値
        digit (int): 四捨五入する桁数
    
    Returns:
        float: 四捨五入後の数値
    """
    return round(input, digit)

def floor_number(input: float, digit: int) -> float:
    """指定した桁数以下を切り捨てる関数
    第二引数で指定した桁数で切り捨てる
    
    Args:
        input (float): 切り捨てる数値
        digit (int): 切り捨てる桁数
        
        Returns:
            float: 切り捨て後の数値
    """

    return np.floor(input * 10 ** digit) / 10 ** digit

def ceil_number(input: float, digit: int) -> float:
    """指定した桁数以上で切り上げる関数
    第二引数で指定した桁数で切り上げる

    Args:
        input (float): 切り上げる数値
        digit (int): 切り上げる桁数

    Returns:
        float: 切り上げ後の数値
    """
    return np.ceil(input * 10 ** digit) / 10 ** digit

