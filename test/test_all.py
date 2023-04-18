import ast
import os

# すべての関数に対してテストコードが書かれているか確認する
def test_all():
    # テスト対象ファイルは../にあるすべての.pyファイル
    test_target = [f.replace(".py", "") for f in os.listdir("./") if f.endswith(".py")]

    for target in test_target:
        with open("./" + target + ".py", encoding="utf-8", mode="r") as f:
            tree = ast.parse(f.read())

        # テスト対象ファイルの関数一覧を取得
        # importで取得したクラス，関数は除く
        func_names = []
        import_names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                import_names.append(node.names[0].name)
            if isinstance(node, ast.ImportFrom):
                import_names.append(node.module)
            if isinstance(node, ast.FunctionDef):
                func_names.append(node.name)
        test_func_list = list(set(func_names) - set(import_names))

        # test_func_listから__で始まる関数を除く
        test_func_list = [func for func in test_func_list if not func.startswith("__")]

        # テスト対象ファイルの関数一覧に対してテストコードが書かれているか確認
        # テストコードは./test_ファイル名.py
        # 関数名はtest_関数名
        for func in test_func_list:
            test_file_path = "./test/test_" + target + ".py"
            test_func_name = "test_" + func
            assert test_func_name in open(test_file_path, encoding="utf-8", mode="r").read(), f"{test_file_path}に{test_func_name}がありません"