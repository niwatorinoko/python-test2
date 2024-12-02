import glob, os

path = '..'
CWD = os.getcwd()

# glob.glob(): finds all the filenames matching a specified pattern
# Wildcards *： zero or more characters
for name in glob.glob(CWD+'/*.py'):
    print(name)
print()

for file in glob.glob(path+"/*.py"):
    print(file)
print()

# Single character wildcard: ?
for name in glob.glob(CWD+'/*csv?.py'):
    print(name)
print()

# Character Ranges
for name in glob.glob(CWD+'/*[0-9].*'):
    print(name)