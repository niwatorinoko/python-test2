# -*- Coding: utf-8 -*-

import os
import json
import csv


# Read credits.txt and create credits dic
infolder = "data"
outfolder = 'output'
filename = 'credits_all.txt'
filepath = os.path.join(infolder, filename)

credits_dict = {} # {course: credits}

with open(filepath, encoding='utf-8') as f: 
    for line in f:
        words = line.strip().split(":")
        # print(words)
        k = words[0].strip()
        v = words[1].strip()
        credits_dict[k] = int(v)

# print(credits_dict)

courses = sorted(credits_dict.keys())
print(courses, '\n')

# Read grades json file
jsonfile = "grades.json"
jsonpath = os.path.join(infolder, jsonfile)
grade_dict = {}

with open(jsonpath, encoding='utf-8') as f:
  data = f.read()
  grade_dict = json.loads(data) # data is a JSON string

# print(grade_dict)

# Read data row by row
datarows = []
avg_list = []

for k, v in grade_dict.items():
  sid = k
  #print(sid)
  row = [k]
  for i in range(len(courses)):
    row.append('')
    
  total_scores = 0
  total_credits = 0 
  for c, s in v.items():
    if s >= 0:
      total_scores +=  int(s) * credits_dict.setdefault(c, 0)
      total_credits += credits_dict[c]
    r_index = courses.index(c)
    row[r_index+1] = s     # course grade starts at 1
  #print(total_credits)
  
  avg = round((total_scores/total_credits) * 100)/100
  # print('{0}: {1:.2f}'.format(sid, avg))
  row.append(avg)
  avg_list.append([sid, float(f'{avg:.2f}')]) # 
  datarows.append(row)
  sorted_rows = sorted(datarows, key=lambda row: (-row[-1], row[0]))
  
print("Top five students:")
for row in sorted_rows[0:5]:
  print(f'{row[0]}: {row[-1]:.2f}')
  
# Write data to CSV file
savefile = "grades_avg" + ".csv"
savepath = os.path.join(outfolder, savefile)   
os.makedirs(outfolder, exist_ok= True)

with open(savepath, 'w', newline='', encoding='utf-8-sig') as f:
  writer = csv.writer(f)
  writer.writerow(["StudentId"] + courses + ["Average"])  # 寫入標題列
  writer.writerows(sorted_rows)                              # 寫入Data列

print("\nGrades and average saved to cvs file successfully.\n")
