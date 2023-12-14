import random
arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]

arr10 = [4,0,3]
arr11 = [0 for x in range(15)]
arr12 = [x for x in range(1,31)]
arr13 = [random.randint(0,1) for x in range(20)]
arr14 = [[False,False] for x in range(5)]

print(arr1,"\n",arr2,"\n",arr3,"\n",arr4,"\n",arr5,"\n",arr6,"\n",arr7)
print(arr8,"\n",arr9,"\n",arr10,"\n",arr11,"\n",arr12,"\n",arr13,"\n",arr14,"\n")