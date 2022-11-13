from ast import While
import math
import numpy as np
k=int(input("choose 2 for binary\n\t8 for octal\n\t16 for hexa-decimal\n\t\t\t"))
x=float(input("give me the value of after points number\t\t\t\t"))
def f(x):
    return x*k
p=f(x)
# print(p)
# s=float
# while s==0.0:
for i in range(20):
    if p>0.00:
        s=int(p)
        p=p-float(s)
        p=p*k
        print(s,p)
    else:
        p=p*k
        print(p)