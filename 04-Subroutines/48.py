def f(s):
    sum = int(s[0]) + int(s[1]) + int(s[2])
    sum %= 7
    if sum == int(s[3]):
        return True
    else:
        return False


print(f("7071"))