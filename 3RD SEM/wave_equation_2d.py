
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

plt.contourf(x,t,V , cmap ="Accent")
plt.colorbar()
plt.title("SOLUTION OF WAVE EQUATION" , color = "red")
plt.xlim(0,30)
plt.ylim(20)
plt.show()