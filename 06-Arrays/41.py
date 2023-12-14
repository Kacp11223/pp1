arr1 = [1,2,3]
arr2 = [1,2,3,4,5,6]

if len([x for x in arr1 if x in arr2]) == len(arr1):
    print(True)
else:
    print(False)



