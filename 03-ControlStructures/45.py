N = 100
primes = [x for x in range(2,N) if not [y for y in range(2,(x//2)+1) if x%y==0]]
print(primes)