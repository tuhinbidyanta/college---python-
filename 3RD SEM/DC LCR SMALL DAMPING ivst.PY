# WE ARE PLOTTING THE CURRENT VS TIME DIAGRAM OF DC LCR CIRCUITS
#THIS CURVE LOOK LIKE THE DAMPED OSLLITION WHEN (B<w0)
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt


steps=10000
time=np.zeros(steps+1)
current=np.zeros(steps+1)
derivative_current=np.zeros(steps+1)

#remember that (cay_constant< sqr.root of  (omega_not_square))
decay_constant=0.17
omega_not_square=1




def double_derivative_current(derivative_current,current,time):
    return -(decay_constant*derivative_current + omega_not_square*current)


time[0]=0.0
time[steps]=50.0

current[0]=0.0
derivative_current[0]=10

dx=(time[steps]-time[0])/steps



for i in range(steps):
    current[i+1]=current[i]+derivative_current[i]*dx
    derivative_current[i+1]=derivative_current[i]+ double_derivative_current(derivative_current[i],current[i],time[i])*dx
    time[i+1]=time[i]+dx
    
y=0.0*time

plt.plot(time,current,color='purple',lw='1',ms='2' ,label='Small Damping')
plt.plot(time,y,color='red',lw='.5',ms='2')

plt.xlabel('TIME(sec)')
plt.ylabel('CURRENT(ampere)')
plt.title('LCR DC CIRCUITS SMALL DAMPING')
plt.legend()
plt.show()












