with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\RowRowFightThePowah.txt",'w') as f:
    for x in range(1,10):
        f.write(f'{x}, {x**2}, {x**3}')
        f.write("\n")