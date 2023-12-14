binary = "0110"
binary = binary[::-1]
print(binary)
sum=0
for i in range(len(binary)):
    sum += int(binary[i])*(2**(i))

print(sum)
