# -*- coding: utf-8 -*-

import random 

for id in ids:
  sid = 's' + str(id)
  stu_dict = {}
  num = random.randint(5,9)
  print(num)
  stu_scores = random.choices(scores, k=num)
  ext_scores = random.choices(non_scores, k=8-num)
  stu_scores = stu_scores + ext_scores
  random.shuffle(stu_scores)
  stu_courses = random.sample(courses, 8)
  for c, s in zip(stu_courses, stu_scores):
    stu_dict[c] = s
  grade_dict[sid] = stu_dict 

print(grade_dict)
# import math
# for k,v in grade_dict.items():
  # for k2, v2 in v.items():
    # if isinstance(v2, float) and math.isnan(float(v2)):
    #  print(f'{k}: {v}')