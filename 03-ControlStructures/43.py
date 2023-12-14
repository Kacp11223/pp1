fib = [0,1]
sum = 0
for x in range(20):
    sum = fib[1+x] + fib[0+x]
    fib.append(sum)
print(' '.join([str(x) for x in fib]))