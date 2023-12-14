import csv
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\Studentslist.txt", newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    students_under_30 = [row for row in reader if int(row['age']) < 30]

    print("first_name\tlast_name\temail")
    for student in students_under_30:
        print(f"{student['first_name']}\t\t{student['last_name']}\t\t{student['email']}")