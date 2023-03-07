import numpy as np
import matplotlib.pyplot as plt



n=100000
y=t=np.zeros(n+1)
N=np.linspace(10,0,n+1)
print(N)
lmd=4
def f(N,t):
     return -lmd*N
y=f(N,t)

dt=(100-0)/n
t[0]=0
y[0]=0

for i in range (n):
	y[i+1]=y[i]+dt*f(N[i],t[i])
	t[i+1]=t[i]+dt


plt.plot(t,y,color='red',label='N vs Time')
plt.title('RADIOACTIVE DECAY by Tuhin Bidyanta')
plt.legend()
plt.show()