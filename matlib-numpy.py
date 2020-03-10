import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for i in np.arange(-2, 2, .1):
    x.append(i)
    y.append(i**2)

plt.plot(x,y, "bo")
plt.plot(x,y,"r-", linewidth=2)
plt.grid(True)
plt.axis([-2,2,-1,6])
plt.title("Quadratic")
plt.xlabel("X")
plt.ylabel("X^2")
plt.show()
