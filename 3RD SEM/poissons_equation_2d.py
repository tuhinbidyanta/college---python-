import numpy as np
import matplotlib.pyplot as plt
L= 100
p=0.5
h=0.01
e=8.854187817 *10**-12
x=np.arange(0,L)
y=np.arange(0,L)
x,y=np.meshgrid(x,y)
v= np.zeros((L,L),float)
for i in range(0,L-1):
    for j in range(0,L-1):
        v[1,j]=100
        v[i,j]=0.25*(v[i+1,j]+v[i-1,j]+v[i,j+1]+v[i,j-1] +(p*h**2)/e)

plt.contourf(x,y,v , cmap ="hot")
plt.colorbar()
plt.title("SOLUTION OF POISSONS EQUATION by TUHIN BIDYANTA" , color = "red")
# plt.xlim(0,30)
plt.ylim(0,8)
plt.show()