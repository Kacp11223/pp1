file_name = input("type file name: ")
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\"+file_name,'r') as f:
    counter = 0
    for line in f:
        counter += 1
    print("number of lines " + str(counter))