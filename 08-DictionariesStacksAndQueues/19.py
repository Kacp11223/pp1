import json

with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\students.json","r") as f:
    students_data = json.load(f)
    limited_data = [{'first_name':student["first_name"],'last_name':student['last_name'],'id':student["id"]} for student in students_data]

with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\limited.json","w") as limited_file:
    json.dump(limited_data,limited_file,indent=4)

    