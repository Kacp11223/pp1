def diagonal(n):
    return [[1 if y==i else 0 for y in range(n)] for i in range(n)]

print(diagonal(5))