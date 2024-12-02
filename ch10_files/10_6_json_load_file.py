import json

with open("employee.json") as file:
    data = json.load(file)
    print(type(data))
   
print(json.dumps(data, indent=4))