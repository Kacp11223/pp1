def f(n):
    fib = [0,1]
    for i in range(n):
        aux = fib[i+1] + fib[i]
        fib.append(aux)
    return fib[n-1],fib

print(f(5))