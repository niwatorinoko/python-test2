from datetime import datetime, timedelta
import os

n = 2
now = datetime.now()
n_days_before = now - timedelta(days=n)

# Find files under current directory  
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Print time range
print("Starting Time:", n_days_before)
print("Current  Time:", now)
print()

# Print qualified files
if files:
  # Find max filename length
  max_len = max(len(f) for f in files)

  # sort files by st_mtime
  sorted_files = sorted(files, key=lambda x: os.stat(x).st_mtime)

  for file in sorted_files:
    mtime = datetime.fromtimestamp(os.stat(file).st_mtime)
    if mtime >= n_days_before:
      print(f"{file:{max_len}s} {mtime}")

else:
  print("\n No files found.\n")