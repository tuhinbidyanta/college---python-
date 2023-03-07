#TRANSPOSE OF MATRIX BY TUHIN BIDYANTA
import numpy as np

row1 = int(input("give me the row matrix\t"))
columm1 = int(input("give me the row matrix\t"))

print(f"give me the {row1*columm1} elements of first matrix\n")
a = np.zeros(row1*columm1)
for a1 in range(row1*columm1):
    a[a1]=float(input())
matrix_1 =a.reshape(row1,columm1)
print("your given matrix is \n", matrix_1)

transpose = np.zeros((row1,columm1),float)

for i in range(row1):
    for j in range(columm1):
        transpose[i,j] = matrix_1[j,i]

print("transpose of your given matrix is \n",transpose)