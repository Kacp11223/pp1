import json
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\dzejsonik.json") as f:
    data = json.load(f)

for key,value in data.items():
    print(f"{key} : {value}")