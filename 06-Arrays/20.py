arr = [34,7,19,4,21,8]
def oodCounter(n):
    i = 0
    counter = 0
    while i < len(n):
        if n[i]%2==0:
            counter += 1
        i += 1
    return counter

print(oodCounter(arr))