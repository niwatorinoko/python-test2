# validating an email, one email at a time
import re

emails = ['asss@',  '_test@mail.yzu.edu.tw', '.bbb@nec.co.jp','test@.edu.tw', 
'John..Doe@example.com', 'john@example.com.','ase2ss.xxx.go',  
'test2.yzu@mis-.goto.com', 'test2.yzu@-server.goto.com', 'test2.yzu@mis-server.goto.com',
'aaa@xxx.kr', 'yzu.python@gmail.com', 'John.Doe@example.com', 'join_me@yzu.edu.tw']

# Simple regex
print("First Try:")
regex = '[a-zA-Z0-9]+@[a-zA-Z0-9\.]+'
"""
[a-zA-Z0-9]+: アルファベットまたは数字を1文字以上
@: 固定文字で "@"
[a-zA-Z0-9\.]+: ドメイン部分はアルファベット・数字・ピリオドを1文字以上含む。
"""
for email in emails:
  match = re.search(regex, email)
  if match:
    print(email)
print()


# More elaborated regex
# regex 1 fail at '_test@mail.yzu.edu.tw', '.bbb@nec.co.jp', 
# 'John..Doe@example.com', 'john@example.com.', 'test2.yzu@mis-.goto.com', 'test2.yzu@-server.goto.com', 
regex1 = r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
"""
^[a-zA-Z0-9_\.]+: 先頭にアルファベット・数字・アンダースコア・ピリオドを許可。
@[a-zA-Z0-9-]+: @ の後にドメイン部分。ハイフンを許可。
\.[a-zA-Z0-9.]+$: ドメインに少なくとも1つのドットを含む。
"""

# regex 2 fails at 'john@example.com.', 'test2.yzu@mis-.goto.com',
# 'test2.yzu@-server.goto.com'
regex2 = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
"""
[\._]?: アンダースコアまたはピリオドを1つだけ許可（ただしオプション）。
名前部分（@ より前）の連続したピリオドを防ぐ。
"""

# regex 3 fails at 'test2.yzu@mis-.goto.com', 'test2.yzu@-server.goto.com'
regex3 = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@([a-zA-Z0-9-]+[\.]){1,3}\w{2,}$'
"""
([a-zA-Z0-9-]+[\.]){1,3}: ドットを含むサブドメインを最大3回まで許可。
\w{2,}$: ドメイン末尾（トップレベルドメイン）が2文字以上でなければ無効。
"""

# \w but without _: [^\W_], [a-zA-Z0-9]
regex4 = r'^[^\W_]+[\._]?[^\W_]+@([^\W_]+[-]?[a-zA-Z0-9]+[\.]){1,3}\w{2,}$'
"""
[^\W_]: アンダースコア (_) を除く英数字のみを許可。
[-]?[a-zA-Z0-9]+: ドメイン部分でハイフンの隣に文字がなければ無効。
全体の構造: ハイフンやドットが連続しない形式を保証。
"""

# print(s)
print("Second Try:")
for email in emails:
  match = re.search(regex4, email)
  if match:
    print(email)

