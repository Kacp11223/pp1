import json
student = {
    "name":"John",
    "surname":"Jones",
    "age":20,
    "grade":3.5,
    "classes":["operating systems","IT fundemantals","workshop"],
    "part-time":True,
    "contact":{"mail":"topG@gmail.com","phone":"12346969420","Instagram":"YoouzTruli"}
}

with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\student.json","w") as f:
    json.dump(student,f,indent=4)