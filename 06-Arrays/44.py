import matplotlib.pyplot as plt

x =[]
y = []
for n in range(-100,101):
    x = x + [n]
    y = y + [(n**2)-3]

# create y values
#for n in x:
   # y = (n**2)+3

plt.plot(x,y)

plt.show()

