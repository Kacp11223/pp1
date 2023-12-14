with open(r"C:\\Users\\melko\\Desktop\\3436572afde8ce9e3faf5b7b95356a49-6b25895fce480713560829dec31ac8220ffe5272\\numbers.txt",'r') as file:
    sum = 0
    for line in file:
        sum += int(line)

print(sum)