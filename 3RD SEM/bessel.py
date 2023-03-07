import numpy as np
import matplotlib.pyplot as plt
# the value of points must integers

def bessel_funtion(n,x):
    if (n==0):
        return np.sin(x)/x
    if (n==1):
        return (np.sin(x)/x**2)-(np.cos(x)/x)
    else:
        return (bessel_funtion(n-2,x)-((2*n-1)/x)*bessel_funtion(n-1,x))
            
x=np.linspace(0,2000,100)
# print(x)
for i in range(1,6):
        plt.plot(x,bessel_funtion(i,x) ,label = f"the value of n = {i}")          
plt.xlabel("value of points",color = "blue", fontsize = "12") 
plt.ylabel("value of BESSEL function",color = "blue", fontsize = "12") 
plt.title("BESSEL function by TUHIN BIDYANTA ",color = "red", fontsize = "19") 
plt.legend() 
# plt.xlim(0,275)

plt.show()        

