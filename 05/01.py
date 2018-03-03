import json

student = {}
student["id"] = "17BD110336"
student["first_name"] = "Aziz"

print(json.dumps(student))

data = json.load(open('a.json'))
print(data)
