arr = [15, 8, 31, 47, 2, 19]

def mean(n):
    return sum(n)/len(n)

print(mean(arr))

def plus(n):
    return "+".join([str(x) for x in n])

print(plus(arr))