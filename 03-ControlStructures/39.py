a = 15
b = 15
for each in range(a):
    if each == range(a)[0] or each == range(a)[-1]:
        [print("*",end="") for x in range(b)]#b
    
    else:
        [print("*",end="") if x == 0 or x == 14 else print(" ", end="") for x in range(b)]
    print('')