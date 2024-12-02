import glob

# path = 'f:\\teach\\python'
path = '..'

python_files = glob.glob(path+'/*.py')

for filename in python_files:
    print('檔案:' + filename)
    # 使用with open(filepath, mode, encoding=...) as f:
    with open(filename) as f:
        for line in f:
            print(line.rstrip())
    print()
