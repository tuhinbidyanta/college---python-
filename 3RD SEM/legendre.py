import numpy as np
import matplotlib.pyplot as plt
# THE VALUE OF POINTS MUST IN BETWEEN -1 TO 1


def legendre_funtion(n,x):
        if (n==0):
            return 1
        if (n==1):
            return x
        else:
            return ((2*n-1)*x*legendre_funtion(n-1,x)-(n-1)*legendre_funtion(n-2,x))/n
            
x=np.linspace(-1,1,100)
for i in range(1,6):
        plt.plot(x,legendre_funtion(i,x) , label = f'value of n = {i}')   
plt.xlabel("value of points",color = "red", fontsize = "12") 
plt.ylabel("value of legendre function",color = "red", fontsize = "12") 
plt.title("LEGENDRE function by TUHIN BIDYANTA ",color = "red", fontsize = "19") 
plt.legend()      
plt.show()        

