from cProfile import label
# from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt

omega_not_sqr=100

def double_derivative_current(derivative_current,current,charge,time):
    return -(current/omega_not_sqr)


steps=1000
current=np.zeros(steps+1)
charge=np.zeros(steps+1)
derivative_current=np.zeros(steps+1)
time=np.zeros(steps+1)


time[0]=0.0
time[steps]=100.0


derivative_current[0]=10.0
current[0]=5.0
charge[0]=0.0

dt=(time[steps]-time[0])/steps


for j in range(steps):
    charge[j+1]=charge[j]+current[j]*dt
    current[j+1]=current[j]+derivative_current[j]*dt
    derivative_current[j+1]=derivative_current[j]+double_derivative_current(derivative_current[j],current[j],charge[j],time[j])*dt
    time[j+1]=time[j]+dt
    

# p=charge[current<0]
# t2=time[current<0]

# print(p)
# print(t2)


plt.plot(time,charge,'--' ,color='green',lw="2",label='current positive')
plt.plot(time,current,'--',color='red',label='current negative')
plt.xlabel('time')
plt.ylabel('CHARGE')
plt.title('DC LC circuit by tuhin bidyanta',color='red',fontsize='20')
plt.legend(loc='best')
plt.show()