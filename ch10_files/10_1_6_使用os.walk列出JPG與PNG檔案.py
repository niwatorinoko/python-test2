import os

# path = "f:\\python"
path = os.getcwd()
exts = ['.jpg', '.jpeg', '.png', '.tif']
matches = []

   
for root, dirs, files in os.walk(path):
    for filename in files:
      # Checking for filename matching any suffix
      if filename.endswith(('.jpg', '.jpeg', '.png', '.tif')):
      # if filename.endswith(tuple(exts)):  
        matches.append(os.path.join(root, filename))

for image in matches:
    print(image, '\n')


# Alternative solution

# import fnmatch

# exts  = ['*.jpg', '*.jpeg', '*.png', '*.tif']
# path, file = os.path.split(path_and_file)
# fname,fext = os.path.splitext(path)
# for root, dirs, files in os.walk(path):
    # for ext in exts:
        # # Return the subset of the list of names that match pattern. 
        # # It is the same as [n for n in names if fnmatch(n, pattern)],
        # for file in fnmatch.filter(files, ext):
            # matches.append(os.path.join(root, file))

# for image in matches:
    # print(image)