
import numpy as np

# print("give me the row and column of both matrix")
row = int(input("give me the row of matrix\t"))
column = int(input("give me the column  of matrix\t"))

#define the matrix
matrix1 = np.zeros(row*column).reshape(row,column) #method 1
matrix2 = np.zeros((row,column),float)
sum_matrix = sub_matrix = np.zeros((row,column),float)



# taking the element of the matrix

print("give me the element of two matrix")
for i in range(row):
    for j in range(column):
        matrix1[i,j] = float(input())

print("your given first matrix is \n",matrix1)    

for i in range(row):
    for j in range(column):
        matrix2[i,j] = float(input())

print("your given first matrix is \n",matrix2)   

# addition of two matrix
for i in range(row):
    for j in range(column):
        sum_matrix[i,j] = matrix1[i,j] + matrix2[i,j]


print("sum of matrix 1 and matric 2 \n",sum_matrix) 

#substraction of two matrix 
for i in range(row):
    for j in range(column):
        sub_matrix[i,j] = matrix1[i,j] - matrix2[i,j]


print("substraction of matrix 1 and matric 2 \n",sub_matrix) 
