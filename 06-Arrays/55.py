def oneD(arr):
    newArr = []
    [newArr.extend(x) for x in arr]
    return newArr

print(oneD([[2,3],[1,5]]))
print(oneD([[5,0,3,7,5],[9,0,9,1,2]]))
print(oneD([[2,1],[3,5],[7,4],[2,6]]))