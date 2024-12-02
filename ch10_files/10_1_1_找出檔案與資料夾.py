import os

# os.chdir(path)
# os.getcwd()
# os.listdir(path)
# os.path.isdir(path)


os.chdir('c:\\')      # Change directory
cur_dir = os.getcwd() # get current directory

# os.listdir(path) 列出路徑下的檔案與資料夾
fds = os.listdir(cur_dir)

for f in fds:
    # print(f)
    if os.path.isdir(f): # 判斷是否為資料夾
        print('資料夾:', f)
    else:
        print('檔案:', f)