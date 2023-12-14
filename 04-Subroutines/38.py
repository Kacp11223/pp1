def f(p):
    for i in range(len(p)):
        if p[i] != p[-i-1]:
            return False
    return True

print(f("book"))