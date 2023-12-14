import re
with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\gists.txt",'r') as f:
    boobie = f.read()
    
boobie = re.findall("\\b\w{6,100}\\b",boobie)
print(boobie)