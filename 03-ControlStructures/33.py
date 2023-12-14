decimal = 12

remainders = []

while decimal > 0:
    remainders.append(decimal%2)
    decimal //= 2

binary = ''.join([str(x) for x in remainders[::-1]])

print(decimal)
print(remainders)
print("0b"+binary)
