person = {
    "name" : "Marek",
    "surname" : "Banach",
    "age" : 25,
    "hobby" : ["swimming", "excursion"],
    "married" : True,
    "Phone" : {"landline" : "123444321", "mobile":"777888999"}
}

print(person)
print()
print(person["name"])
print(person["hobby"])
person["surname"] = "Nowak"
print(person["surname"])
person["married"] = False
print(person["married"])
person["gender"] = "male"
print(person)
person["hobby"].append("bicycle")
print(person["hobby"])
person["Phone"]["work"] = "313131444"
print(person["Phone"])
print(person)