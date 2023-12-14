def f(n):
    n = list(map(int,str(n)))
    sum = 0
    counters = []
    for x in range(10):
        counters.append(n.count(x))
    for i in range(len(counters)):
        if counters[i] > 1:
            sum += i*counters[i]
    return sum



print(f(513553007))