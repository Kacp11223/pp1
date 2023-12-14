import shutil
import os

with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\MeatAndFish.txt",'r') as f1,open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\GrainsAndBread.txt",'r') as f2,open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\AllProducts.txt",'w') as fin:
    shutil.copyfileobj(f1,fin)
    #f1.seek(-len(os.linesep),2)
    #if f1.read() != os.linesep:
       # fin.write(os.linesep)
    fin.write('\n')
    shutil.copyfileobj(f2, fin)




