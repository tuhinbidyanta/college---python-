from cProfile import label
import numpy as np
import matplotlib.pyplot as plt


steps=10000
time=np.zeros(steps+1)
current=np.zeros(steps+1)
derivative_current=np.zeros(steps+1)
charge=np.zeros(steps+1)

#remember that (cay_constant< sqr.root of  (omega_not_square))
decay_constant=0.17
omega_not_square=1




def double_derivative_current(derivative_current,current,charge,time):
    return -(decay_constant*derivative_current + omega_not_square*current)


time[0]=0.0
time[steps]=50.0

current[0]=2.0
charge[0]=0.0
derivative_current[0]=10

dt=(time[steps]-time[0])/steps



for j in range(steps):
    charge[j+1]=charge[j]+current[j]*dt
    current[j+1]=current[j]+derivative_current[j]*dt
    derivative_current[j+1]=derivative_current[j]+double_derivative_current(derivative_current[j],current[j],charge[j],time[j])*dt
    time[j+1]=time[j]+dt
        
y=0.0*time

plt.plot(time,current,'--',color='purple',lw='1',ms='2' ,label='current')
plt.plot(time,y,color='red',lw='.5',ms='2')
plt.plot(time,charge,'--',color='black',lw='1',ms='2' ,label='charge')

plt.xlabel('TIME(sec)')
plt.ylabel('CHARGE')
plt.title('LCR DC CIRCUITS SMALL DAMPING by Tuhin Bidyanta',color='green')
plt.legend()
plt.show()

