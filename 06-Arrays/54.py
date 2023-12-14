"""
1 2 3
4 5 6
6 7 8

1 4 6
2 5 7
3 6 8
"""

def transXD(arr):
    trans = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return [(print(x),print()) for x in trans]

transXD([[1,2,3],[4,5,6],[7,8,9]])
transXD([[1,2,3,4,5],[6,7,8,9,0]])
transXD([[5,6,7,8]])



'''
1 6
2 7
3 8
4 9
5 0
'''