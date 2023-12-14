with open(r'C:\\Users\\melko\\Desktop\\pp1\\07-FileHandling\\countries.txt','r') as file:
    i = 1
    for line in file:
        print(f'{i}.{line}',end='')
        i += 1

