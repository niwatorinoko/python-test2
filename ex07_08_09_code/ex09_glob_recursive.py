import glob
import os

dir_path = '.'

# For one extension
files = glob.glob(dir_path+'/**/*.py', recursive=True)

for f in files:
  print(f)

print()

# For multiple extensions
extensions = ['py', 'ipynb']

# Solution 1: Using glob.glob()
print("Using glob.glob()")
# Note that golb.glob() returns a list, so files_grabbed is a list of lists
files_grabbed = [glob.glob(f'./**/*.{ext}', recursive=True) for ext in extensions]
files_flattened = sum(files_grabbed, [])  # Flatten the nested lists

for file in files_flattened:
   print(file)

print()

# Solution 2: Using os.walk()
print("Using os.walk()")
matches = []

for root, dirs, files in os.walk(dir_path):
    print("Directory Path: ", root)
    for file in files:
        if file.endswith(tuple(extensions)):
            matches.append(os.path.join(root, file))

for m in matches:
    print(m)
