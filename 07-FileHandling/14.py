with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\shopping.txt",'r+') as f:
    counter = 0

    for line in f:
        counter += 1

    read_product = True

    while read_product:
        product = input("Enter product name: ")
        if product != "":
            counter += 1
            f.write("\n" + str(counter) + ". " + product)
        else:
            read_product = False
f.close()