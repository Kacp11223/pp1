arr1 = [34,4,6,84,1,45,-43,223,-3]

def bubbleSort(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i]<arr[i+1]:
            i += 1
            continue
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i = 0
    return arr

print(bubbleSort(arr1))
