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