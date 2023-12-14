from math import sqrt
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
s = (a+b+c)/2
tArea = sqrt(s*(s-a)*(s-b)*(s-c))
print(tArea)
tCircum = s*2
print(tCircum)
