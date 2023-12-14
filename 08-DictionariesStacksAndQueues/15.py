basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}


for key,value in advanced_data.items():
    basic_data[key] = value

person = basic_data

for item in person.items():
    print(item)