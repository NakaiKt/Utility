import pandas as pd


# csvから指定したcolumn取得
def get_column(key_column: str, key: str, csv_file_path: str) -> list:
    """csvファイルから指定したcolumnを取得

    Args:
        key_column (str): keyとなるcolumn名
        key (str): key名
        csv_file_path (str): csvファイルのパス

    Returns:
        list: columnの要素リスト
    """
    key=str(key)
    df = pd.read_csv(csv_file_path, dtype={key_column: str})
    return df[df[key_column] == key].values.tolist()[0][1:]

def get_column_value_list(column_name: str, csv_file_path: str) -> list:
    """csvファイルから指定したcolumnの要素リストを取得

    Args:
        key_column (str): keyとなるcolumn名
        csv_file_path (str): csvファイルのパス

    Returns:
        list: columnの要素リスト
    """
    df = pd.read_csv(csv_file_path)
    return df[column_name].values.tolist()