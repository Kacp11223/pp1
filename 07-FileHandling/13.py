movie = ["Indianna Balls","Pirates of Somalia: at 3'rd world'end","Chris Chan: Rape Hour","MotherFucking Snakes on the Motherfucking Plane","Die Hard: 9/11"]
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\movieTtiles.txt",'w+')as f:
    for x in movie:
        f.write(x+"\n")

f.close()
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\movieTtiles.txt",'r')as f:
    print(f.read())