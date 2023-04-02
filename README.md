# Utility
汎用的なUtility郡

## コード記述ルール
- pytestでテストを書く
- 既存コードの入出力の仕様は変えない（テストによって保証されている）
- Utilityは他のUtilityに依存しない
- テストケースにはfailedケースも含める