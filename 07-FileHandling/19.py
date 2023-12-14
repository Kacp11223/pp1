with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\gists.txt",'r') as f, open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\copy.txt",'w') as copy:
    for line in f:
        copy.write(line)