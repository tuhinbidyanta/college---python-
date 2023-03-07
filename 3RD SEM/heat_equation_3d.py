
import matplotlib.pyplot as plt
import numpy as np
L = 100
x = np.arange(0, L)
t = np.arange(0, L)
x, t = np.meshgrid(x, t)
c=3*10**8
h = 0.01
V = np.zeros((L,L),float)
for i in range(0,L-1):
	for j in range(0,L-1):
		V[0,j] = 1
		V[i, j] = 0.5*(V[i+1, j] + V[i-1, j] ) - (h/(0.25*c**2))*(V[i, j+1] + V[i, j-1])

ax=plt.axes(projection ='3d')
ax.plot_surface(x,t,V , cmap = "plasma")
ax.set_title("solution of poissons equation by Tuhin Bidyanta",color = "red")
ax.set_xlabel("x points" ,color = "purple" )
ax.set_xticks([])
ax.set_ylabel("y points",color = "purple")
ax.set_yticks([])
ax.set_zlabel("wave equation" , color = "indigo" ,fontsize ="20")
ax.set_zticks([])
plt.show()