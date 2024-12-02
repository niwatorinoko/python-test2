import os
import glob
from datetime import datetime, timedelta

# Set file path
outfolder = 'output'
filename = 's11016xx'
filepath = f'{outfolder}/{filename}'
CWD = os.getcwd()

outpath = os.path.join(CWD, outfolder)           
os.makedirs(outpath, exist_ok=True)     # 建立備份目錄
fmt = '%Y%m%d_%H%M%S'
target_file = filepath + '_test02_' + datetime.now().strftime(fmt) + '.zip'


# Set time frame 
n = 7
now = datetime.now()
n_days_before = now - timedelta(days=n)

# Find recent changed python files under current working directory  
files = []
print("起始時間:", n_days_before)
print("現在時間:", now)
print()
for file in glob.glob(CWD+'/*.py'):
    mt = os.stat(file).st_mtime
    mtime = datetime.fromtimestamp(mt)
    if mtime >= n_days_before:
       files.append(os.path.basename(file)) 

# Find max filename length
max_len = max([len(file) for file in files])

# Compress qualified files
# https://www.dotnetperls.com/7-zip-examples
# https://cects.com/using-the-winrar-command-line-tools-in-windows/
for fn in files:
  # print(fn)
  # zipcmd=  'C:\\"Program Files"\\WinRAR\\WinRAR.exe a {0} {1}'.format(target_file, fn)
  zipcmd = 'C:\\"Program Files"\\7-Zip\\7z.exe a -tzip -bso0 {0} {1}'.format(target_file, fn) 
  # print(zipcmd)
  if os.system(zipcmd) == 0:
    print(f'{fn:{max_len}s} -> archive succeeds.')
  else:
    print(f'{fn:{max_len}s} -> archive fails.')
    

# 