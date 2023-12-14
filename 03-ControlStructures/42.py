for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()

print()
i = 7
while i > 0:
    [print(x+i, end=' ') for x in range(3)]
    print()
    i -= 3