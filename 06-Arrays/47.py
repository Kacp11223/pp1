arr1 = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7],[8,7,1,1,5]]

def lastCol(arr):
    return [[arr[arr.index(x)][i] for x in arr] for i in range(len(arr[0]))][-1]

print(sum(lastCol(arr1)))