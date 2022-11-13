# WE ARE PLOTTING THE CURRENT VS TIME DIAGRAM OF DC LCR CIRCUITS
#THIS CURVE LOOK LIKE THE DAMPED OSLLITION WHEN (B<w0)
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt


steps=10000
time=np.zeros(steps+1)
current=np.zeros(steps+1)
derivative_current=np.zeros(steps+1)


#remember that (cay_constant=sqr.root of  (omega_not_square))
decay_constant=0.17
omega_not_square=0.0289




def double_derivative_current(derivative_current,current,time):
    return -(decay_constant*derivative_current + omega_not_square*current)


time[0]=0.0
time[steps]=21.15

current[0]=0.0
derivative_current[0]=10

dx=(time[steps]-time[0])/steps



for i in range(steps):
    current[i+1]=current[i]+derivative_current[i]*dx
    derivative_current[i+1]=derivative_current[i]+ double_derivative_current(derivative_current[i],current[i],time[i])*dx
    time[i+1]=time[i]+dx
#THIS CURVE LOOK LIKE THE DAMPED OSLLITION WHEN (B<w0)


#remember that (cay_constant>sqr.root of  (omega_not_square))

time1=np.zeros(steps+1)
current1=np.zeros(steps+1)
derivative_current1=np.zeros(steps+1)


decay_constant1=0.4
omega_not_square1=0.0289




def double_derivative_current1(derivative_current1,current1,time1):
    return -(decay_constant1*derivative_current1 + omega_not_square1*current1)


time1[0]=0.0
time1[steps]=50.0

current1[0]=0.0
derivative_current1[0]=10

dx1=(time1[steps]-time1[0])/steps



for j in range(steps):
    current1[j+1]=current1[j]+derivative_current1[j]*dx1
    derivative_current1[j+1]=derivative_current1[j]+ double_derivative_current1(derivative_current1[j],current1[j],time1[j])*dx1
    time1[j+1]=time1[j]+dx1



   
plt.plot(time1,current1,'--',color='purple',lw='1',ms='2',label='overdamped')
plt.plot(time,current,'--',color='red',lw='01',ms='2',label='critical damping')
plt.xlabel('TIME(sec)')
plt.ylabel('CURRENT(ampere)')
plt.title('LCR DC CIRCUITS CRITICAL AND LARGE DAMPING')
plt.legend()
plt.show()
