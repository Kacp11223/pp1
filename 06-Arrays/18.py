def opposite(arr):
    return [[not y for y in x] for x in arr]

print(opposite([[True,False],[True,True],[False,False]]))