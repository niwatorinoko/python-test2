# Convert a text file with row A:B to a dict
"""
Discrete Math : 3
Calculus:   3
Python: 3
English: 2
'历史': 2   
"""

'''Predict a file's encoding using chardet'''
def predictEncoding(file_path):
    import chardet
    import os
    encoding = ''
    bytes = min(1024, os.path.getsize(file_path))

    # Open the file as binary data
    raw = open(file_path, 'rb').read(bytes)

    result = chardet.detect(raw)
    encoding = result['encoding']

    return encoding


filename = 's4_credits2.txt'

encoding_str = predictEncoding(filename)
print('\n', encoding_str)

# set specific encoding to None
if not encoding_str or encoding_str in ['ISO-8859-1', 'big5', 'cp950']:
    encoding_str = None

my_dict = {}

with open(filename, "r", encoding=encoding_str) as f: 
    for line in f:
        words = line.strip().split(":")
        k = words[0].strip()
        v = words[1].strip()
        my_dict[k] = int(v)

print(my_dict, '\n')
      