# Calculate grade average based on course credits

"""
Discrete Math : 3
Calculus:   3
Python: 3
 中文 : 2
歷史: 2     
"""
import os

"""Open a file with correct encoding"""

def predict_encoding(file_path):
    '''Predict a file's encoding using chardet'''
    import chardet
    import os
    encoding = ''
    bytes = min(1024, os.path.getsize(file_path))

    # Open the file as binary data
    raw = open(file_path, 'rb').read(bytes)

    result = chardet.detect(raw)
    encoding = result['encoding']
    print(f'\n{file_path}: {encoding}')

    if not encoding or encoding == 'ISO-8859-1': #  Extended ASCII
        encoding = None # as default
    
    return encoding

dirname = "files"         # 檔案所在資料夾
filename = 'credits.txt'  # 學分檔
filepath = os.path.join(dirname, filename)
   
#encoding_str = predict_encoding(filepath)

credits_dict = {}

with open(filepath, encoding=predict_encoding(filepath)) as f:
    for line in f:
        words = line.strip().split(":")
        k = words[0].strip()
        v = words[1].strip()
        credits_dict[k] = int(v)

print(credits_dict)

# get grades and calculate average
filename = 'grades.csv'   # 成績檔
filepath = os.path.join(dirname, filename)

#encoding_str = predict_encoding(filepath)
avg_list = []

with open(filepath, encoding=predict_encoding(filepath)) as f:
    lines = f.readlines()
    top = lines[0]
    courses = top.strip('\n').split(',')[1:]
    print(courses)
    credits = [credits_dict[c] for c in courses]
    print(credits)
    print()
    
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
    
    # group averages by range
    group_dict= {}
    
    for avg in sorted(avg_list):
        k = int(avg // 10) * 10
        group_dict.setdefault(k, 0)
        group_dict[k] = group_dict[k] + 1
    
    print(list(group_dict.items()))