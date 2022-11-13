
import numpy as np
import matplotlib.pyplot as plt



x1=[]
y1=[]
z1=[]
t=0.0
while t<100:
    
    x=t
    y=t
    z=t
    x1.append(x)
    y1.append(y)
    z1.append(z)
    t=t+.1

plt.axes(projection="3d").plot(x1,y1,z1)
plt.show()