
import numpy as np
# row , columm = [int(x) for x in input("give me the row and column row and column  ").split()]
row = columm = int (input("give me the row or column of the matrix  "))




a = [float(a) for a in input(f"give me the {row*columm} elements of first matrix ").split() ]
matrix=np.array(a).reshape(row,columm)
row = len(matrix)

print("your given matrix is \n",matrix)

# print(np.linalg.inv(matrix))
# A=np.array([[2,5,6,8],[7,10,5,4],[1,3,4,8],[4,8,9,12]],float)


inv_matrix=np.zeros((row,row),float)
for i in range(0,row):
	inv_matrix[i][i]=1.0
	
for j in range(0,row):
	for i in range(0,row):
		if (i!=j):
		
			r=matrix[i][j]/matrix[j][j]
			for k in range(0,row):
				matrix[i][k]=matrix[i][k]-matrix[j][k]*r
				inv_matrix[i][k]=inv_matrix[i][k]-inv_matrix[j][k]*r
# print(matrix,inv_matrix)
for i in range(0,row):
	for j in range(0,row):
		inv_matrix[i][j]=inv_matrix[i][j]/matrix[i][i]
print("inverse matrix of your given matrix is \n",inv_matrix)
