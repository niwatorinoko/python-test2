import re

# 検証する台湾身分証番号のリスト
twids = [
    'B342232223', '0123456789', 'A21234567', 'A212345678', 'O212345678',
    'J122356789', 'a212345678', 'A11234567a', 'N1205667899', 'N820566789',
    'F928567899'
]

# TWID形式を検証する関数
def is_valid_tw_id(twid):
    # 台湾の身分証番号形式に一致する正規表現パターン：
    # - 大文字アルファベット（A-Z）で始まる
    # - その後に9桁の数字が続く
    # - 2桁目の数字は1または2
    # - 合計で10文字
    pattern = r'^[A-Z][1-2]\d{8}$'
    return bool(re.match(pattern, twid))

# 有効なTWIDをフィルタリングして出力
valid_twids = [twid for twid in twids if is_valid_tw_id(twid)]

# 有効なTWIDを出力
for valid_id in valid_twids:
    print(valid_id)
