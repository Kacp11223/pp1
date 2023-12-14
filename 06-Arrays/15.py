arr = [[1,3,5],[8,7,2]]
print(sum([arr[0][0],arr[-1][-1]]))
print(sum([x[int(len(x)//2)] for x in arr]))
print(sum(arr[-1]))