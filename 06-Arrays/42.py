import random
def rand_elem(arr):
    return arr[random.randint(0,len(arr)-1)]

arr1 = [1,2,3,4,5,7,8,20,300]

print(rand_elem(arr1))