# f.readline()

fin  = open('poem.txt', 'rt', encoding='utf-8')
fout = open('poem2.txt','wt', encoding='utf-8')


line = fin.readline() # Read first line
while line:
    fout.write(line)
    line = fin.readline() # Read next line

fin.close()
fout.close()

# Alternative 1
import shutil
import os

source_file = "poem.txt"
dest_file = "poem2.txt"
dirpath = "files"

# Ignore the FileExistsError exceptions if the target directory
# already exists 
os.makedirs(dirpath, exist_ok=True) 

shutil.copy(source_file, os.path.join(dirpath, dest_file))

# Alternative 2
import pathlib

somepath = 'files/level2'
path = pathlib.Path(somepath)
path.mkdir(parents=True, exist_ok=True)

shutil.copy(source_file, os.path.join(path, dest_file))

