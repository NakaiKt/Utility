import json
import os
from urllib import request


def download_file_from_url(url: str, save_path: str, basename: str = None, extension: str = None):
    """
    URLからファイルをダウンロードする

    Args:
        url (str): ダウンロードするファイルのURL
        save_path (str): ダウンロードしたファイルを保存するパス
        basename (str, optional): ダウンロードしたファイルの名前. Defaults to None.
        extension (str, optional): ダウンロードしたファイルの拡張子. Defaults to None.
    """

    # file_nameが指定されていない場合はURLからファイルのbasenameを取得する
    if basename is None:
        basename = os.path.basename(url).split('.')[0]

    # extensionが指定されていない場合はURLから拡張子を取得する
    if extension is None:
        extension = url.split('.')[-1]

    # ダウンロードしたファイルのパス
    file_path = os.path.join(save_path, basename + '.' + extension)

    # ダウンロードしたファイルを保存するディレクトリが存在しない場合は作成する
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # ダウンロードしたファイルを保存する
    request.urlretrieve(url, file_path)

def get_basename(path: str):
    """
    パスからファイルのbasenameを取得する
    basenameには拡張子が含まれない

    Args:
        path (str): パス

    Returns:
        str: ファイルのbasename
    """
    return os.path.basename(path).split('.')[0]

def get_extension(path: str):
    """
    パスからファイルの拡張子を取得する

    Args:
        path (str): パス

    Returns:
        str: ファイルの拡張子
    """
    return path.split('.')[-1]

def get_filename(path: str):
    """
    パスからファイルの名前を取得する
    ファイル名には拡張子が含まれる

    Args:
        path (str): パス

    Returns:
        str: ファイルの名前
    """
    return os.path.basename(path)

def load_json(path: str):
    """
    JSONファイルを読み込む

    Args:
        path (str): JSONファイルのパス

    Returns:
        dict: 読み込んだJSONファイル
    """

    with open(path, 'r') as f:
        return json.load(f)