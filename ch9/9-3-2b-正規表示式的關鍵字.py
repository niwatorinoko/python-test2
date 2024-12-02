import re


"""
^ と $ を使った行頭・行末の検索。
文字クラス [ ] を使った特定文字の検索。
\W を使った非単語文字の検索。
特定のパターン（黃鶴樓\W や 黃鶴.\W）を検索する方法。
否定文字クラス [^ ] を使って特定の文字を除外して検索する方法。
"""

s='昔人已乘黃鶴去，此地空余黃鶴樓。\
黃鶴一去不復返，白雲千載空悠悠。'
print(s)
ans = re.findall('^昔人',s)
print(ans)
ans = re.findall('空悠悠。$',s)
print(ans)
ans = re.findall('[黃白]',s)
print(ans)
ans = re.findall('\W',s)
print(ans)
ans = re.findall('黃鶴樓\W',s)
print(ans)
ans = re.findall('黃鶴.\W',s)
print(ans)
ans = re.findall('[^黃鶴]',s)
print(ans)