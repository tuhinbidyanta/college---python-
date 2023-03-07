#linear equation solve by matrix
import numpy as np

variable = int( input  ( "give me the number of variable "))
# variable = 5


print("suppose a linear equation ")

numeric = ["A","B","C","D",'E',"F",'G','H','I','J','K','L','M','N','O','P','Q']
# numeric1 = numeric[:variable]
# numeric2 = np.array(numeric1*variable).reshape(variable,variable)

name_variable  = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12']
name_variable1 = np.array(name_variable[:variable]).reshape(1,variable)

constant = numeric[variable]

for i in range(variable):
    print(f"eq({i+1})", end=' ')
    for j in range(variable):
        if (j  == variable-1):
            print(f" {numeric[j]}{i}.{name_variable[j]} ",end=' ')
        else:
            print(f" {numeric[j]}{i}.{name_variable[j]} ",end='+')
        
    print(f"=  {constant}{i}")

matrix = np.zeros((variable,variable),float)
constant_matrix=np.zeros((variable,1),float)

for i in range(variable):
    for j in range(variable):
        matrix[i,j] = float(input (f"give me the value of {numeric[j]}{i}\t:"))
    constant_matrix[i,0] = float(input(f"give me the value of {constant}{i}\t:"))
    




B=np.zeros((variable,variable),float)
P=np.zeros((variable,1),float)
for i in range(variable):
	B[i,i]=1.0
	
for j in range(variable):
	for i in range(variable): 
		if (i!=j):
		
			r=matrix[i,j]/matrix[j,j]
			for k in range(variable):
				matrix[i,k]=matrix[i,k]-(matrix[j,k]*r)
				B[i,k]=B[i,k]-(B[j,k]*r)
for i in range(variable):
	for j in range(variable):
		B[i,j]=B[i,j]/matrix[i,i]
		
for i in range(variable):
	for j in range(1):
		for k in range(variable):
			P[i,j]=P[i,j]+B[i,k]*constant_matrix[k,j]
			
# print(P)
for i  in range(variable):
    print(f"the value of X{i+1} =  " ,P[i,0])