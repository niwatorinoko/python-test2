# validating local phone number, one number at a time
import re

# all the following formats are valid
phones = [
'(02) 2345-8738',
'(03) 463-8800',
'(03) 463 8800',
'(03) 4638800',
'02-2456-1009',
'02-26272389',
'02 2290 0318',
'03 435-2077',
'05 534 2601',
'06-2757575',
'08-723-4406',
'(082) 313-304',
'089-318855'
]

# Simple regex
print("First Try:")

regex = r'^\(?\d{2,3}\)? ?\d{4} ?\d{3,4}$'
"""
^: 行の先頭にマッチ。
\(?: 開き括弧 ( があってもなくてもよい（任意）。
\d{2,3}: 2～3桁の数字にマッチ。
\)?: 閉じ括弧 ) があってもなくてもよい（任意）。
?: 空白（スペース）が0個または1個ある場合にマッチ。
\d{4}: 4桁の数字にマッチ。
?: 再び、空白が0個または1個ある場合にマッチ。
\d{3,4}: 3～4桁の数字にマッチ。
$: 行の末尾にマッチ。
"""

for phone in phones:
  match = re.search(regex, phone)
  if match:
    print(phone)
print()


# More elaborated regex
# https://regex101.com/r/32Ucr3/1
regex2 = r'^\(?\d{2,3}\)?[- ]?\d{3,4}[- ]?\d{3,4}$'
"""
^: 行の先頭にマッチ。
\(?: 開き括弧 ( があってもなくてもよい（任意）。
\d{2,3}: 2～3桁の数字にマッチ。
\)?: 閉じ括弧 ) があってもなくてもよい（任意）。
[- ]?: ハイフンまたはスペースが0個または1個ある場合にマッチ。
\d{3,4}: 3～4桁の数字にマッチ。
[- ]?: 再び、ハイフンまたはスペースが0個または1個ある場合にマッチ。
\d{3,4}: 3～4桁の数字にマッチ。
$: 行の末尾にマッチ。
"""

# print(s)
print("Second Try:")
for phone in phones:
  match = re.search(regex2, phone)
  if match:
    print(phone)

