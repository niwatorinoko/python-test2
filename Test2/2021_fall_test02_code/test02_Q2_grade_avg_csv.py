# -*- Coding: utf-8 -*-

import os
import json

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
# courses = sorted(credits_dict.keys(), key=lambda x: x)
# print(courses)

# Read grades json file
jsonfile = "grades.json"
jsonpath = os.path.join(infolder, jsonfile)
grade_dict = {}

with open(jsonpath, encoding='utf-8') as f:
  data = f.read() # read all as string
  grade_dict = json.loads(data)

# print(grade_dict)

# Read data row by row
avg_list = []

for k, v in grade_dict.items():   
  total_scores = 0
  total_credits = 0 
  for c, s in v.items():
    if s >= 0:
      total_scores +=  int(s) * credits_dict.setdefault(c, 0)
      total_credits += credits_dict.setdefault(c, 0)
  
  avg = int((total_scores/total_credits) * 100) / 100
  # print('{0}: {1:.2f}'.format(k, avg))
  # print(f'{k}: {avg}')
  avg_list.append([k, avg])

avg_sorted = sorted(avg_list, key=lambda x: (-x[1], x[0]))
# print(avg_sorted)

print("\nTop 5 students:")
for item in avg_sorted[0:5]:
  print(f'{item[0]}: {item[1]:.2f}')
  
# Grouping avgs
g_dict = {} # a group dict {range: count}
r = 10 # the range
totals = len(avg_list)

for item in sorted(avg_list):
  q = int(item[1]//r) # quotient
  #g = q * r # range lowerbound
  g = str(q*r) + '-' +str((q+1)*r-1)
  g_dict.setdefault(g, 0)
  g_dict[g] += 1

print("\nGrouping by grade range:")
g_dict_sorted = sorted(g_dict.items(), key=lambda x: x[0])
for g, v in g_dict_sorted:
  print(f'{g}: {v:>2d}')