import os

if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
  print("myfile.txt removed\n")
else:
  print("The file does not exist.")