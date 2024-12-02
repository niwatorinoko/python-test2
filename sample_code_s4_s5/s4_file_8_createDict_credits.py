# Convert a text file with row A:B to a dict

"""
Discrete Math : 3
Calculus:   3
Python: 3
English: 2
History: 2   
"""

my_dict = {}

with open('s4_credits.txt', "r", encoding="utf-8") as f:
    for line in f:
        words = line.strip().split(":")
        k = words[0].strip()
        v = words[1].strip()
        my_dict[k] = int(v)

from pprint import pprint
# add sort_dicts=False since python 3.8
pprint(my_dict,sort_dicts=False)

# conda install -c conda-forge rich
from rich import print
print(my_dict)

import json
print(json.dumps(my_dict, indent=2))
    