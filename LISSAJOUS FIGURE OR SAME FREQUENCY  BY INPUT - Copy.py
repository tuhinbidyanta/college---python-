import numpy as np
import matplotlib.pyplot as plt
# import random as rn
a=100
b=100

value=[]


#when delta =0

x1=[]
y1=[]
print('the value of delta =aπ/b')
a=float(input('give me the value of a \t'))
b=float(input('give me the value of b \t'))
delta1=(a*np.pi)/b
print('type 1 or lissjous figure \n type 2 for same frequency oscillation')
p=int(input())
t=0.00    
while t<10:
    if p==1:
        y=a*np.cos(2*t+delta1)
    elif p==2:
        y=a*np.cos(t+delta1)
    x=b*np.cos(t)
    x1.append(x)
    y1.append(y)
    t=t+.01
# plt.subplsot(6,5,1)
tuhin=plt.subplot(1,1,1)
plt.title("ACCORDING TO THE GIVEN VALUE OF DELTA YOUR GRAPH IS",c='r')
plt.plot(x1,y1,'.')
tuhin.axes.set_xticks([])
tuhin.axes.set_yticks([])
plt.xlabel(f'the value of delta=({a}/{b})π')
plt.show()