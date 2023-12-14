import matplotlib.pyplot as plt
import numpy as np
'''
car = 25
pb = 19
gey = 32
byfoot = 7
'''
means = np.array(["car","public transport","gey","by foot"])
values = np.array([25,19,32,7])

plt.bar(means,values)

plt.title("Means of Transportation")

plt.show()