def create2Darr(a,b):
    return [[0 for y in range(b)] for x in range(a)]

[print(x) for x in create2Darr(300,100)]