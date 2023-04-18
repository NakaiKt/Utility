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
    save_path = 'test_download'
    basename = 'google'
    extension = 'jpg'
    download_file_from_url(url, save_path, basename, extension)
    
    get_basename("./test/google.png") == "google"
    get_extension("./test/google.png") == "jpg"
    get_filename("./test/google.png") == "google.jpg"
    os.remove("./test_download/google.jpg")
    os.rmdir("./test_download")

    download_file_from_url(url, save_path)
    get_basename("./test/googlelogo_color_272x92dp.png") == "googlelogo_color_272x92dp"
    get_extension("./test/googlelogo_color_272x92dp.png") == "png"
    get_filename("./test/googlelogo_color_272x92dp.png") == "googlelogo_color_272x92dp.png"
    os.remove("./test_download/googlelogo_color_272x92dp.png")
    os.rmdir("./test_download")

def test_get_basename():
    """テスト手順
    1. get_basename()を実行してbasenameを取得
    2. basenameが正しいことを確認
    """
    path = './test/google.png'
    get_basename(path) == "google"

def test_get_extension():
    """テスト手順
    1. get_extension()を実行してextensionを取得
    2. extensionが正しいことを確認
    """
    path = './test/google.png'
    get_extension(path) == "png"

def test_get_filename():
    """テキタウト手順
    1. get_filename()を実行してfilenameを取変
    2. filenameが正しいこのを確認
    """
    path = './test/google.png'
    get_filename(path) == "google.png"

def test_failed_download_file_from_url():
    """テスト手順
    1. 存在しないURLを指定してdownload_file_from_url()を実行
    2. FileNotFoundErrorが発生することを確認
    """

    url = 'https://sssssssfsfdsfsfsafassfsd.png'
    save_path = 'test_download'
    basename = 'google'
    extension = 'png'
    with pytest.raises(urllib.error.URLError):
        download_file_from_url(url, save_path, basename, extension)
    os.rmdir("./test_download")

def test_load_json():
    """テスト手順
    1. load_json()を実行してjsonファイルを読み込む
    2. jsonファイルの内容が正しいことを確認

    test.jsonの内容
        {
        "name": "jquery-1.7.2.js",
        "version": "1.7.2",
        "description": "jQuery JavaScript Library v1.7.2",
        "main": "jquery-1.7.2.js",
        "directories": {
            "example": "examples"
        }
    }
    """
    json_file = './test/test.json'
    json_data = load_json(json_file)
    assert json_data['name'] == "jquery-1.7.2.js"
    assert json_data['version'] == "1.7.2"
    assert json_data['description'] == "jQuery JavaScript Library v1.7.2"
    assert json_data['main'] == "jquery-1.7.2.js"
    assert json_data['directories']['example'] == "examples"
