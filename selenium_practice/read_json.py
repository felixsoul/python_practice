import json

with open("./data/data.json", "r") as json_file:
    data = json_file.read()

users = json.loads(data)
print(users)