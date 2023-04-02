# test for file_handler.py
# use pytest

import os
import pytest
import urllib

from file_handler import *

def test_download_file_from_url():
    """テスト手順
    1. download_file_from_url()を実行してファイルダウンロード
    2. ダウンロードしたファイルのbasename, extension, filenameを取得, それぞれの値が正しいことを確認
    3. ダウンロードしたファイルを削除
    4. basename, extensionを指定せずにダウンロード
    5. ダウンロードしたファイルのbasename, extension, filenameを取得, それぞれの値が正しいことを確認
    6. ダウンロードしたファイルを削除
    """
    url = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
    save_path = 'test'
    basename = 'google'
    extension = 'jpg'
    download_file_from_url(url, save_path, basename, extension)
    
    get_basename("./test/google.png") == "google"
    get_extension("./test/google.png") == "jpg"
    get_filename("./test/google.png") == "google.jpg"
    os.remove("./test/google.jpg")
    os.rmdir("./test")

    download_file_from_url(url, save_path)
    get_basename("./test/googlelogo_color_272x92dp.png") == "googlelogo_color_272x92dp"
    get_extension("./test/googlelogo_color_272x92dp.png") == "png"
    get_filename("./test/googlelogo_color_272x92dp.png") == "googlelogo_color_272x92dp.png"
    os.remove("./test/googlelogo_color_272x92dp.png")
    os.rmdir("./test")


def test_failed_download_file_from_url():
    """テスト手順
    1. 存在しないURLを指定してdownload_file_from_url()を実行
    2. FileNotFoundErrorが発生することを確認
    """

    url = 'https://sssssssfsfdsfsfsafassfsd.png'
    save_path = 'test'
    basename = 'google'
    extension = 'png'
    with pytest.raises(urllib.error.URLError):
        download_file_from_url(url, save_path, basename, extension)
    os.rmdir("./test")