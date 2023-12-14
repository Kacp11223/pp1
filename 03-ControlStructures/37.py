[([print("*", end=" ") for y in range(x)],print("")) for x in range(6)]
[([print("*", end=" ") for y in range(x)],print("")) for x in range(4,0,-1)]
"""
for x in range(5):
    for y in range(x):
        print("*",end=" ")
    print("\n")
"""