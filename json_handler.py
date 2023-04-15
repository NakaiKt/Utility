import json

def load_json(file_path: str, mode: str = 'r') -> dict:
    """
    JSONファイルを読み込む

    Args:
        file_path (str): JSONファイルのパス
        mode (str, optional): ファイルを開くモード. Defaults to 'r'.

    Returns:
        dict: JSONファイルの内容
    """
    return json.load(open(file_path, mode))