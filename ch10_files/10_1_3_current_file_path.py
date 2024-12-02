import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file absolute path (since Python 3.4)")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
dirpath, filename = os.path.split(full_path)
print(dirpath + ' --> ' + filename + "\n")

print("This file's directory only")
print(os.path.dirname(full_path))

# Second test

def print_my_path():
    print('cwd:     {}'.format(os.getcwd()))
    print('__file__:{}'.format(__file__))
    print('abspath: {}'.format(os.path.abspath(__file__)))

print()
print("---- Second filepath test ----")
print_my_path()

os.chdir('..')
print()
print_my_path()