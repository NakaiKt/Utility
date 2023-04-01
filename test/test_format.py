# test for format.py
# use pytest

import logging

import pytest
import sys
sys.path.append("../")
from format import *

def setting_logging_config_sample():
    """loggingの設定を行う関数のテスト
    """

    # ログの設定
    setting_logging_config(log_name = "test")

    # ログの設定が正しく行われているか確認
    logger = logging.getLogger("test")
    logger.info("test")

if __name__ == "__main__":
    setting_logging_config_sample()