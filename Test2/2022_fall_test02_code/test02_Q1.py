import os
import glob
from datetime import datetime, timedelta
import subprocess

# Set file path
dirpath = '.' # os.path.dirname(__file__)
outfolder = 'output'
filename = 's11116xx'
outpath = os.path.join(dirpath, outfolder)
filepath = f'{outpath}{os.sep}{filename}'

os.makedirs(outpath, exist_ok=True)     # 建立備份目錄
fmt = '%Y%m%d_%H%M%S'
target_file = filepath + '_test02_' + datetime.now().strftime(fmt) + '.zip'


# Set time frame 
n = 100
now = datetime.now()
n_days_before = now - timedelta(hours=n)

# Find recent changed python files under current working directory  
matches = []
print("起始時間:", n_days_before)
print("現在時間:", now)
print()

for file in glob.glob(dirpath+'/**/*.py', recursive=True):
    mt = os.stat(file).st_mtime
    mtime = datetime.fromtimestamp(mt)
    if mtime >= n_days_before:
        # print(os.path.relpath(file))
        matches.append(os.path.relpath(file)) 

# # Alternative using os.walk()
# for root, dirs, files in os.walk(dirpath):
#     filenames = [os.path.join(root, f) for f in files if f.endswith('.py')]
#     filenames.sort()
#     for file in filenames: 
#         mt = os.stat(file).st_mtime
#         mtime = datetime.fromtimestamp(mt)
#         if mtime >= n_days_before:
#           # print(file)
#           matches.append(os.path.relpath(file)) 


# Find max filename length
max_len = max([len(file) for file in matches])

# Compress qualified files
# https://www.dotnetperls.com/7-zip-examples
# https://cects.com/using-the-winrar-command-line-tools-in-windows/
for fn in matches:
  # print(fn)
  # zipcmd=  'C:\\"Program Files"\\WinRAR\\WinRAR.exe a {0} {1}'.format(target_file, fn)
  zipcmd = '7z a -bso0 {0} {1}'.format(target_file, fn) 
  # change os.system(zipcmd) to subprocess.call(zipcmd, shell=True)
  if subprocess.call(zipcmd, shell=True) == 0:
    print(f'{fn:{max_len}s} -> archive succeeds.')
  else:
    print(f'{fn:{max_len}s} -> archive fails.')

print(f'\n==> compressed file saved as {target_file}')