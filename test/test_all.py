import importlib


# すべての関数に対してテストコードが書かれているか確認する
def test_all():
    # テスト対象ファイル
    test_target = ["convert", "csv_handler", "file_handler", "format", "image_handler", "list_handler", "number_handler", "validation"]

    for target in test_target:
        # テスト対象ファイルのimport
        test_module = importlib.import_module(target)

        # テスト対象ファイルの関数一覧を取得
        test_func_list = [func for func in dir(test_module) if callable(getattr(test_module, func)) and not func.startswith("__")]

        # テスト対象ファイルの関数一覧に対してテストコードが書かれているか確認
        # テストコードは./test_ファイル名.py
        # 関数名はtest_関数名
        for func in test_func_list:
            test_file_path = "./test_" + target + ".py"
            test_func_name = "test_" + func
            assert test_func_name in open(test_file_path, encoding="utf-8", mode="r").read(), f"{test_file_path}に{test_func_name}がありません"