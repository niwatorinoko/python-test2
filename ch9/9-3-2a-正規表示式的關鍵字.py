import string
import re
pr=string.printable #string.printable は、Pythonで定義された「印刷可能なすべての文字列」を含む定数です。
"""
数字 (\d)
数字以外 (\D)
空白 (\s)
空白以外 (\S)
単語構成文字 (\w)
単語構成文字以外 (\W)
単語境界 (\b)
単語境界以外 (\B)
"""
print(re.findall('\d',pr))
print(re.findall('\D',pr))
print(re.findall('\s',pr))
print(re.findall('\S',pr))
print(re.findall('\w',pr))
print(re.findall('\W',pr))
print(re.findall(r'\b','abcd'))
print(re.findall('\B','abcd'))
