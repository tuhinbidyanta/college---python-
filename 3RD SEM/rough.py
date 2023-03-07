#ac LCR
import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z):
    return(-y)
N=10000
x=np.zeros(N+1)
y=np.zeros(N+1)
z=np.zeros(N+1)
x[0]=0.0
x[N]=500.0
y[0]=0
z[0]=10.0
h=(x[N]-x[0])/N
for i in range(N):
    y[i+1]=y[i]+h*z[i]
    z[i+1]=(z[i]+h*f(x[i],y[i],z))
    x[i+1]=x[i]+h
plt.plot(x,y,'--',lw='01',ms='2',color='blue')
plt.xlabel('time[t]')
plt.ylabel('current[i]')
plt.title('LCR(ac)circuit')
plt.show()