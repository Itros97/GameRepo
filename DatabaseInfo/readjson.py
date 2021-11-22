import json

with open("/home/inigo/GameRepo/DatabaseInfo/config.json") as json_data_file:
    data = json.load(json_data_file)
print(data)
