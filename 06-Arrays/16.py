def oodCount(arr):
    return sum([sum([y for y in x if y%2!=0]) for x in arr])

print(oodCount([[3,9,2],[2,4,5],[7,1,6],[0,4,8]]))