def f(r1,r2):
    return sum([x for x in range(r1,r2+1) if x%2==0 and x%3==0 and x%4!=0])
