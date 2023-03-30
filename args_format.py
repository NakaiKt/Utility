import argparse

# コマンドライン引数のヘルプにデフォルトを表示するためのフォーマットクラス
class HelpFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass