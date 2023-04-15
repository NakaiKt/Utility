# test for format.py
# use pytest

import logging

import pytest
import sys
sys.path.append("../")
from format import *

def test_setting_logging_config():
    """loggingの設定を行う関数のテスト
    """

    # ログの設定
    setting_logging_config(log_name = "test")

    # ログの設定が正しく行われているか確認
    # log_nameが正しいか確認
    logger = logging.getLogger("test")
    assert logger.name == "test"
    # ログレベルが正しいか確認
    assert logger.level == logging.DEBUG
    # ログのフォーマットが正しいか確認
    assert logger.handlers[0].formatter._fmt == "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

def test_HelpFormatter():
    pass

def test_TypeWarning():
    pass

if __name__ == "__main__":
    test_setting_logging_config()