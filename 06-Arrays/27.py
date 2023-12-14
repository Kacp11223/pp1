arr = [12,6,4,9,10]

def star(n):
    return [([print("*",end="") for y in range(x)],print("")) for x in arr]

star(arr)