import random
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\randomNum.txt",'w') as f:
    for x in range(50):
        f.write(str(random.randint(100,999)))
        f.write("\n")