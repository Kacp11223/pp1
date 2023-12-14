import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
def secondLargest(arr):
    return sorted(arr)[-2]

def difference(arr):
    return max(arr)-min(arr)

def bubbleSort(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i]<=arr[i+1]:
            i += 1
            continue
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i = 0
    return arr

def median(arr):
    arr = bubbleSort(arr)
    if len(arr)%2==0:
        return sum([arr[(int(len(arr)/2)-1)],arr[int(len(arr)/2)]])/2
    else:
        return arr[len(arr)//2]
    

def twoList(arr):
    return [min(arr),max(arr)]


def negatedString(arr):
    return "-".join([str(x) for x in arr])


    

if __name__ == "__main__":
    print(median([3,4,3,5,6,7,8,9,10,12,10,4]))