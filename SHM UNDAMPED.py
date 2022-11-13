#SHM UNDAMPED X_AXIX vs TIME

import numpy as np
import matplotlib.pyplot as plt

omega=1

def acceleration(velocity,displacement,time):
    return -(omega**2*displacement)


steps=100000
displacement=np.zeros(steps+1)
velocity=np.zeros(steps+1)
time=np.zeros(steps+1)

time[0]=0.0
time[steps]=50.0

displacement[0]=0.0
velocity[0]=10.0

dt=(time[steps]-time[0])/steps

for i in range(steps):
    displacement[i+1]=displacement[i]+velocity[i]*dt
    velocity[i+1]=velocity[i]+acceleration(velocity[i],displacement[i],time[i])*dt
    time[i+1]=time[i]+dt
    
plt.plot(time,displacement,'--',color='blue',label='displacement')
plt.xlabel('TIME')
plt.ylabel("DISPLACEMENT")
plt.title('SIMPLE HERMONIC MOTION (UNDAMPED) by Tuhin Bidyanta')
plt.grid()
plt.legend(loc='lower left')
plt.show()
