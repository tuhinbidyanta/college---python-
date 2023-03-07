 

from cProfile import label
# from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt

inductance = 100*10**-3
capacitance = 10*10**-6

def double_derivative_current(derivative_current,current,time):
    return -(current/(inductance*capacitance))


steps=10000
current=np.zeros(steps+1)
derivative_current=np.zeros(steps+1)
time=np.zeros(steps+1)


time[0]=0.0
time[steps]=.01


derivative_current[0]=0.1
current[0]=0.0

dt=(time[steps]-time[0])/steps


for j in range(steps):
    current[j+1]=current[j]+derivative_current[j]*dt
    derivative_current[j+1]=derivative_current[j]+double_derivative_current(derivative_current[j],current[j],time[j])*dt
    time[j+1]=time[j]+dt
    

p=current[current<0]
t2=time[current<0]


t3 = time[((current <= 0.0000001) & (current >= -0.0000001))]
p1 = np.zeros(len(t3))
# print(t_0,p1)
# p1 = np.zeros(10000)
# print(p)
# print(t2)


plt.plot(time,current ,color='green',lw="2",label='current positive')
plt.plot(t2,p,'.',color='red',label='current negative')
plt.scatter(t3,p1)
for i in range(len(t3)):
    plt.text(t3[i],p1[i],f'({round(t3[i],5)} , 0)')
plt.text(time[current == max(current)] , max(current) , f'I_max = {round(max(current),7)}')
plt.xlabel('time')
plt.ylabel('current')
plt.title('DC LC circuit by Tuhin Bidyanta',color='red',fontsize='20')
plt.legend()
plt.show()