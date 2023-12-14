arr1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

arr1 = [[(j+1)*(i+1) for j in range(len(arr1[i]))] for i in range(len(arr1))]

print(arr1)