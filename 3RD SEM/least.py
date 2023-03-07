import numpy as np
import matplotlib.pyplot as plt


# sum of xk*yk

xk1=[1.0,3.0,5.0,7.0,9.0]
yk1=[.7,12.1,15.2,17.6,19.9]

xk=np.array([1.0,3.0,5.0,7.0,9.0])
yk=np.array([.7,12.1,15.2,17.6,19.9])
# print(yk[1])

sum_xk_yk=np.zeros(len(xk))
sum_xk=np.zeros(len(xk))
sum_yk=np.zeros(len(xk))
square_sum_xk=sum_xk**2
sum_square_xk=np.zeros(len(xk))

sum_xk_yk[0]=0.0
sum_xk[0]=0.0
sum_yk[0]=0.0

for i in range(len(xk)):
    sum_xk_yk=sum_xk_yk+xk[i]*yk[i]
    sum_yk=sum_yk+yk[i]
    sum_xk=sum_xk+xk[i]
    sum_square_xk=sum_square_xk+xk[i]*xk[i]
    
    
a=(len(xk)*sum_xk_yk-sum_xk*sum_yk)/(len(xk)*sum_square_xk-sum_xk**2)
    

y=a*xk



plt.scatter(yk,xk,color = 'r',marker = '*')



plt.plot(y,xk, color = "purple")
plt.xlabel("x axis",fontsize = "15")
plt.ylabel("y axis",fontsize = "15")
plt.title("least square fit by TUHIN BIDYANTA ",color = "red",fontsize = "20") 
plt.xlim(-5,25)
plt.ylim(-2,11)
plt.show()   
    
    
    

    