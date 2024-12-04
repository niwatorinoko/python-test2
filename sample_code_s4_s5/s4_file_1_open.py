# -*- coding: utf-8 -*-
"""
file open
"r" - Read - デフォルトモード。読み取り専用
"t" - Text - デフォルトモード。テキストモード
"b" - Binary - バイナリモード（例: 画像）
"a" - Append - 追記モード。存在しない場合は新規作成
"w" - Write - 書き込みモード。存在しない場合は新規作成
"x" - Create - 新規作成モード。ファイルが既に存在する場合はエラー
"""

# file_object  = open("filename", "mode")
import os

dirpath = os.path.dirname(__file__)

# Read content: file_object.read()
filename= "s4_demofile.txt"
f = open(os.path.join(dirpath, filename), "rb")
print(f.read())
print()

# Read only parts of the file: file_object.read(n): 
f = open(os.path.join(dirpath, filename), "r", encoding='utf-8')
print(f.read(10)) # 10 characters
print()

# Read one line: file_object.readline(): 
f = open(os.path.join(dirpath, filename), "r", encoding='utf-8')
print(f.readline())
print()

# Loop through the file line by line:
f = open(os.path.join(dirpath, filename), "r", encoding='utf-8')
for line in f:
  print(line.strip('\n'))
print()
  
# Read Lines: file_object.readlines(): 
# The with statement creates a context manager and it will automatically 
# close the file handler for you when you are done with it
filename = "s4_test4.csv"
with open(os.path.join(dirpath, filename), "r", encoding='cp950') as f:
  print(f.readlines())