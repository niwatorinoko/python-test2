import os

# path = "f:\\python"
path = '..'

for root, dirs, files in os.walk(path):
    print(f'root: {root}, dirs:{dirs}')
    for file in files:
        if file.endswith(".py"):
            print(file)
            # print(os.path.join(root, file))