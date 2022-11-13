 

from cProfile import label
# from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt

omega_not=0.19
v0=10
omega_not_square=0.03

def double_derivative_current(derivative_current,current,time):
    return -(current*(omega_not_square))+(v0*(np.sin(omega_not*time)))


steps=10000
current=np.zeros(steps+1)
derivative_current=np.zeros(steps+1)
time=np.zeros(steps+1)


time[0]=0.0
time[steps]=500.0


derivative_current[0]=10.0
current[0]=0.0

dt=(time[steps]-time[0])/steps


for j in range(steps):
    current[j+1]=current[j]+derivative_current[j]*dt
    derivative_current[j+1]=derivative_current[j]+double_derivative_current(derivative_current[j],current[j],time[j])*dt
    time[j+1]=time[j]+dt
    

# p=current[current<0]
# t2=time[current<0]

# print(p)
# print(t2)


plt.plot(time,current,'--' ,color='red',lw=".7",label='current')
# plt.plot(t2,p,'.',color='red',label='current negative')
plt.xlabel('time')
plt.ylabel('current')
plt.title('AC LC circuit by Tuhin Bidyanta',color='green',fontsize='20')
plt.legend()
plt.show()