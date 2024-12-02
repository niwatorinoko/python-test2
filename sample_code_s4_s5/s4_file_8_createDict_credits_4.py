# Convert a text file with row A:B to a dict
"""
Discrete Math : 3
Calculus:   3
Python: 3
 中文 : 2
歷史: 2     
"""

import os


def open_file_with_encoding(file_path):
    """Open file with proper encoding"""
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError as e:
        print(file_path, "not encoded in utf-8.")
        with open(file_path, "r", encoding=None) as f:
            lines = f.readlines()
    return lines

dirname = "files"
  
# Get credits data   
filename1 = 'credits.txt'   
filepath = os.path.join(dirname, filename1)
credits_dict = {}

lines = open_file_with_encoding(filepath)
for line in lines:
    words = line.strip().split(":")
    k = words[0].strip()
    v = words[1].strip()
    credits_dict[k] = int(v)

print(credits_dict)

# get grade data
filename2 = 'grades.csv'
filepath = os.path.join(dirname, filename2)
avg_list = []

lines = open_file_with_encoding(filepath)
top = lines[0]
courses = top.strip('\n').split(',')[1:]
print(courses)
credits = [credits_dict[c] for c in courses]
print(credits)
   
for line in lines[1:]:
    data = line.strip('\n').split(',')
    # get student's id and grades
    sid = data[0]
    grades = data[1:]
    total_credits = 0
    total_scores = 0
        
    for i, grade in enumerate(grades):
        total_credits += credits[i]
        total_scores += int(grade) * credits[i]
        
    avg = total_scores/total_credits
    avg_list.append(avg)
    print("{}: {:.2f}".format(sid, avg))   
    
group_dict= {}
    
for avg in sorted(avg_list):
    k = int(avg // 10) * 10
    group_dict.setdefault(k, 0)
    group_dict[k] = group_dict[k] + 1
    
print(list(group_dict.items()))