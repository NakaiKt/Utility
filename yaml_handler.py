"""
yamlファイルを操作するUtility郡
"""

import yaml


def load_yaml(yaml_path: str, mode:str = "r") -> dict:
    """yamlファイルを読み込む関数

    Args:
        yaml_path (str): yamlファイルのパス
        mode (str, optional): ファイルの読み込みモード. Defaults to "r".

    Returns:
        dict: yamlファイルの内容
    """
    with open(yaml_path, mode) as f:
        return yaml.load(f, Loader=yaml.FullLoader)
    
def write_yaml(yaml_path: str, content: dict) -> None:
    """
    yamlファイルの内容を書き換える関数

    Args:
        yaml_path (str): yamlファイルのパス
        content (dict): yamlファイルに書き込む内容
    """
    # yamlをreadモードで取り込み
    with open(yaml_path, "r") as f:
        # yamlファイルの内容を取得
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        # yamlファイルの内容と引数の内容をマージ
        content = {**yaml_content, **content}
    
    # yamlをwriteモードで取り込み
    with open(yaml_path, "w") as f:
        # yamlファイルに書き込み
        yaml.dump(content, f)

def delete_content_yaml(yaml_path: str, content: list) -> None:
    """yamlの項目を削除する

    Args:
        yaml_path (str): yamlファイルのパス
        content (list): 削除する項目のリスト
    """
    # yamlをreadモードで取り込み
    with open(yaml_path, "r") as f:
        # yamlファイルの内容を取得
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        # yamlファイルの内容から引数の内容を削除
        for key in content:
            yaml_content.pop(key)
    
    # yamlをwriteモードで取り込み
    with open(yaml_path, "w") as f:
        # yamlファイルに書き込み
        yaml.dump(yaml_content, f)