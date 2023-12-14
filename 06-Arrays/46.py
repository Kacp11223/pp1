arr = [[1,2],[3,4],[5,6],[7,8]]

#rows
[([print(y,end=" ") for y in x],print()) for x in arr]
print('\n')
#columns all subs are equal
[([print(arr[arr.index(x)][i],end=" ") for x in arr],print()) for i in range(len(arr[0]))]