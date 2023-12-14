with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\gists.txt",'r') as f:
    counter = 1
    while True:
        print(f.readline())
        counter += 1
        if counter == 6:
            if input() == '':
                counter = 1
            else:
                break