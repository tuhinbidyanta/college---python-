import numpy as np 

# matrix multiplication of any 

row1 = int(input("give me the row number of first matrix "))
columm1 =row2 = int(input("give me the column number of first matrix = row number of 2nd matrix  " ))
column2 = int(input("give me the column number of 2nd matrix  "))


a = [float(a) for a in input(f"give me the {row1*columm1} elements of first matrix ").split() ]
matrix_1 =np.array(a).reshape(row1,columm1)
print("your given first matrix is \n",matrix_1)


b = [float(b) for b in input(f"give me the {row2*column2} elements of secoend matrix ").split()]

matrix_2 = np.array(b).reshape(row2,column2)
print("your given secoend matrix is \n", matrix_2)

c=np.zeros(row1*column2).reshape(row1,column2)

for i in range(row1):
    
    for j in range(column2):
        ans = 0.0
        for k in range(row2):
            ans += (matrix_1[i][k])*(matrix_2[k][j])
            c[i][j] = ans

print("the multiplication of two matrix is \n",c)
