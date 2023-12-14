import matplotlib.pyplot as plt
import math
x =[]
y = []
for n in range(0,int(20*math.pi)+1):
    x = x + [n]
    y = y + [math.sin(n)]

plt.plot(x,y)
plt.show()