arr = [2,3,2,5,8,1,9,8]

def unique(n):
    for x in n:
        if n.count(x) > 1:
            n = [i for i in n if i != x]
    return n

print(unique(arr))
