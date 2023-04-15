import argparse
import logging


# コマンドライン引数のヘルプにデフォルトを表示するためのフォーマットクラス
class HelpFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

# 想定していた型と異なる場合の警告クラス
class TypeWarning(Warning):
    pass

def setting_logging_config(log_name: str, log_save_path = None, log_level = logging.DEBUG):
    """loggingの設定を行う関数

    Args:
        log_name (str): ログの名前
        log_save_path (str): ログの保存先
        log_level (str): ログレベル
    """
    # もしlog_save_pathがNoneの場合は，今日の日付をファイル名にする
    if log_save_path is None:
        import datetime
        log_save_path = datetime.datetime.now().strftime("%Y%m%d") + ".log"

    # ログの設定
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)
    # ログのフォーマット
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    # ログの出力先
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formatter)
    fh = logging.FileHandler(log_save_path)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    # ログの設定
    logger.addHandler(sh)
    logger.addHandler(fh)