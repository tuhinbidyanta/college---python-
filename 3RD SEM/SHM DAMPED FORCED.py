#SHM FORCED UNDAMPED X_AXIX vs TIME

import numpy as np
import matplotlib.pyplot as plt

omega=.2
decay_constant=0.05
f0=10.0
#delta must be very small than omega square
delta=0.01


def acceleration(velocity,displacement,time):
    return -((omega**2+delta)*displacement)+f0*np.cos(omega*time)-(decay_constant*velocity)


steps=100000
displacement=np.zeros(steps+1)
velocity=np.zeros(steps+1)
time=np.zeros(steps+1)

time[0]=0.0
time[steps]=300.0

displacement[0]=0.0
velocity[0]=10.0

dt=(time[steps]-time[0])/steps

for i in range(steps):
    displacement[i+1]=displacement[i]+velocity[i]*dt
    velocity[i+1]=velocity[i]+acceleration(velocity[i],displacement[i],time[i])*dt
    time[i+1]=time[i]+dt
    
plt.plot(time,displacement,color='blue',label='displacement')
plt.xlabel('TIME' ,color='red',fontsize='15')
plt.ylabel("DISPLACEMENT",color='red',fontsize='15')
plt.title('SIMPLE HERMONIC MOTION (forced damped) by Tuhin Bidyanta',fontsize='13',color = "red")
plt.grid(lw='.2',color='blue')
plt.legend(loc='lower left')
plt.show()
