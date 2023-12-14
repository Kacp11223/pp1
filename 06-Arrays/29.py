arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

def content(arr1,arr2):
    for x in arr1:
        if x in arr2:
            arr1.remove(x)
    return arr1

print(content(arr1,arr2))