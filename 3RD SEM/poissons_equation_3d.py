import numpy as np
import matplotlib.pyplot as plt
L= 100
p=0.5
h=0.1
e=8.854187817 *10**-12
x=np.arange(0,L)
y=np.arange(0,L)
x,y=np.meshgrid(x,y)
v= np.zeros((L,L),float)
for i in range(0,L-1):
    for j in range(0,L-1):
        v[1,j]=100
        v[i,j]=0.25*(v[i+1,j]+v[i-1,j]+v[i,j+1]+v[i,j-1] +(p*h**2)/e)

ax=plt.axes(projection ='3d')
ax.plot_surface(x,y,v , cmap = "plasma")
ax.set_title("solution of poissons equation by Tuhin Bidyanta",color = "red")
ax.set_xlabel("x points" ,color = "purple" )
ax.set_xticks([])
ax.set_ylabel("y points",color = "purple")
ax.set_yticks([])
ax.set_zlabel("poissons eqution" , color = "indigo" ,fontsize ="20")
ax.set_zticks([])
plt.show()