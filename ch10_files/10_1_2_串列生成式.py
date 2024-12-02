import os

path = "c:\\"   # 絕對路徑
# path = '..'   # 相對路徑

# os.listdir(path)
# os.path.join(path, path2)
# os.path.isdir(f)
# os.path.isfile(f)

# os.listdir(path): list files relative to the provided path
files = [f for f in os.listdir(path) if os.path.isfile(f)]
           #if os.path.isfile(os.path.join(path, f))]
dirs  = [d for d in os.listdir(path) if os.path.isdir(d) ]
           # if os.path.isdir(os.path.join(path, d))]

print(files)
print(dirs)