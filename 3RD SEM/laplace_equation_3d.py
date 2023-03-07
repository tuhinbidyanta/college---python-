#PDEWaveEqn3D
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.tri as tri
import matplotlib.pyplot as plt
import numpy as np
L = 100
x = np.arange(0, L)
t = np.arange(0, L)
x, t = np.meshgrid(x, t)

v = np.zeros((L,L),float)
for i in range(0,L-1):
	for j in range(0,L-1):
		v[1,j]=100
		v[i,j]=0.25*(v[i+1,j]+v[i-1,j]+v[i,j+1]+v[i,j-1])
# fig=plt.figure()
ax=plt.axes(projection='3d')
# surf=ax.plot_wireframe(x,t,v)
# surf=ax.plot_trisurf(x,t,v , cmap = "cool" , triangles = tri.triangles)
# surf=ax.contourf3D(x,t,v)
ax.plot_surface(x,t,v, cmap = "plasma")
ax.set_title("solution of laplace equation by Tuhin Bidyanta",color = "red")
ax.set_xlabel("x points" ,color = "purple")
ax.set_ylabel("y points",color = "purple")
ax.set_zlabel("solutio of laplace equation in 3d" , color = "indigo")
plt.show()