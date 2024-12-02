# -*- coding: utf-8 -*-

import json

json_str = '{"s1071176": {"Calculus": 70, "Physics": 80, "Economics": 90, "Biology": 80, "Networks": 60, "Chemistry": 80}}'

print(type(json_str))

# json.loads(): from json string to dict (json object)
d = json.loads(json_str)
print(type(d))
print(d.items())
print()

# json.dumps(): from dict back to json string
s = json.dumps(d)
print(s)