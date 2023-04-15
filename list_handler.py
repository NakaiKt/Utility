"""
list操作に関するUtility郡
"""

def list_value_distribution(list_data: list) -> dict:
    """リストの要素の分布を計算する

    Args:
        list_data (list): リスト

    Returns:
        dict: 要素とその出現回数の辞書
    """
    distribution = {}
    for value in list_data:
        if value in distribution:
            distribution[value] += 1
        else:
            distribution[value] = 1
    return distribution