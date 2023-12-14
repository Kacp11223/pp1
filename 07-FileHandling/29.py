import re
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\studentGrades.txt",'r') as f:
    boobie = f.read()

grades = re.findall("\\b\d[.]\d\\b", boobie)
grades = [float(x) for x in grades]
mean = sum(grades)/len(grades)
print(mean)
    