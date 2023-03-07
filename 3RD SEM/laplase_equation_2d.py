import numpy as np
import matplotlib.pyplot as plt
L= 100
x=np.arange(0,L)
y=np.arange(0,L)
x,y=np.meshgrid(x,y)
v= np.zeros((L,L),float)
for i in range(0,L-1):
	for j in range(0,L-1):
		
			v[1,j]=100
			v[i,j]=0.25*(v[i+1,j]+v[i-1,j]+v[i,j+1]+v[i,j-1])
plt.contourf(x,y,v , cmap ="hot")
plt.colorbar()
plt.title("laplace equation by Tuhin Bidyanta" ,color = "green")
plt.ylim(0,3.5)
plt.show()