arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

def maxLen(n):
    return sorted([(len(x),x) for x in arr])[-1][1]

print(maxLen(arr))