import argparse
import logging

# コマンドライン引数のヘルプにデフォルトを表示するためのフォーマットクラス
class HelpFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

def setting_logging_config():
    """loggingの設定を行う関数
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s :%(message)s"
    )