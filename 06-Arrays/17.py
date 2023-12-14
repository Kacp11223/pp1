def diagonal(n):
    return [[1 if y==i else n[i][y] for y in range(len(n[i]))] for i in range(len(n))]

print(diagonal([[0,0,0],[0,0,0],[0,0,0]]))