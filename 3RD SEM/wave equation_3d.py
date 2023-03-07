
import matplotlib.pyplot as plt
import numpy as np
L = 100
x = np.arange(0, L)
t = np.arange(0, L)
x, t = np.meshgrid(x, t)
c=3*10**8
V = np.zeros((L,L),float)
for i in range(0,L-1):
	for j in range(0,L-1):
		V[i, 0] = np.sin(np.pi*i)
		V[i, j] = (1/(2*(1+c**2)))*(c**2*V[i+1, j] + c**2*V[i-1, j] - V[i, j+1] - V[i, j-1])
# fig=plt.figure(figsize=(5,4))
ax=plt.axes(projection='3d')
surf=ax.plot_surface(x,t,V , cmap = "brg")
ax.set_title("solution of wave equation by Tuhin Bidyanta",color = "red")
ax.set_xlabel("x points" ,color = "purple")
ax.set_xticks([])
ax.set_ylabel("y points",color = "purple")
ax.set_yticks([])
ax.set_zlabel("wave equation" , color = "indigo")
ax.set_zticks([])
plt.show()