arr = [15,38,7,23,14]

def occur(n,arr):
    return True if n in arr else False

print(occur(int(input("number: ")), arr))