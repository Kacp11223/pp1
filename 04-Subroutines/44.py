def f(n):
    n = list(n)
    setn = set(n)
    return False if len(setn) < len(n) or len(n)<6 else True

print(f(""))