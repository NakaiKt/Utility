def validate_in_list(input, list):
    """入力がリストの中にあるか確認する関数

    Args:
        input (str): 確認する文字列
        list (list): 確認するリスト

    Returns:
        bool: 確認結果
    """
    if input in list:
        return True
    else:
        return False