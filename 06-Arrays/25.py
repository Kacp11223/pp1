arr = [15, 8, 31, 47, 2, 19]

length = len(arr)
suma = 0

while arr:
    suma += arr.pop()
    
suma /= length
print(suma)

