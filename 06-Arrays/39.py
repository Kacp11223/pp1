def apartheid(arr):
    even = [x for x in arr if x%2==0]
    odd = [x for x in arr if x%2!=0]
    even.extend(odd)
    return even

arr1 = [1,2,3,4,5,6,7,8,9]

print(apartheid(arr1))