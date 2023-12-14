name = "Kacper Kosek"
university = "Auschwitz Birkenau"
field = "Applied Informatics"
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\student.txt",'w+')as f:
    f.write(name+"\n"+university+"\n"+field)

f.close()
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\student.txt",'r')as f:
    print(f.read())
    
