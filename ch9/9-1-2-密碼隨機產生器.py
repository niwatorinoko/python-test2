import string
import random
chs = string.ascii_letters + string.digits
pwd=""
for x in range(random.randint(8,12)): #この値を元に、パスワードの長さがランダムに決定されます。
    pwd+=random.choice(chs) #random.choice(chs) は、chs に含まれる文字列から1文字をランダムに選びます。
print(pwd)