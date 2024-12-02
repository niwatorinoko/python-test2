import os

home = os.path.expanduser("~")

from pathlib import Path
home = str(Path.home())

path = 'D:\\users\\public' # 絕對路徑
# path = '..'   # 相對路徑

def find_dir(dir):
    fds = os.listdir(dir)
    for fd in fds:
        fd_path = os.path.join(dir, fd) # 絕對路徑
        if os.path.isdir(fd_path):
            print('資料夾:',fd_path)
            find_dir(fd_path) # Recursive call
        else:
            print('  檔案:', fd_path)

 
find_dir(path)