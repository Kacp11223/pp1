n = [int(input()) for x in range(3)]

def isDifferent(n):
    return True if n[0] != n[1] and n[0] != n[2] and n[1] != n[2] else False

print(isDifferent(n))