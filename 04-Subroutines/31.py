def evenNegative(n,p):
    count = 0
    for x in range(1,-n+1):
        if x%2==0:
            count += 1
    return count

print(evenNegative(-1,11))