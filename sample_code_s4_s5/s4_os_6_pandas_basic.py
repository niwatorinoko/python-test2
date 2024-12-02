# -*- Coding: utf-8 -*-

import os
import pandas as pd

data = [
    ['s1101234', 90, 90, 80],
    ['s1101266', 85, 90, 80],
    ['s1101299', 99, 99, 99],
    ]
# Write to a new file
folder = 'result'
filename = "grades_test.csv"
filepath  = os.path.join(folder, filename)   
filepath2 = os.path.join(folder, "grades_test.xlsx") 
os.makedirs(folder, exist_ok= True)

# Using Pandas
df = pd.DataFrame(data, columns = ["學號", '科目1', '科目2','科目3'])
df.to_csv(filepath, encoding='utf-8-sig', index=None)
# engine: 'openpyxl' or 'xlsxwriter' 
df.to_excel(filepath2, sheet_name="Grades", engine="xlsxwriter", index=None)
print("\nGrades saved to cvs file successfully.\n")