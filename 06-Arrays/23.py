arr = [-15, 8, -31, 47, -2, 19]

def rangeOf(arr):
    min = arr[0]
    max = arr[0]
    for x in arr:
        if min < x:
            continue
        else:
            min = x
    for x in arr:
        if max > x:
            continue
        else:
            max = x
    return min, max

print(rangeOf(arr))