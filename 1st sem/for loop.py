# use of for loop 
for i in range(2,10,2):
    print(i)
for i in range(2,10):
    print(i)
for i in range(-10,2,2):
    print(i)
# -----------------------------------------------------------------------------------

# ---------------------------------------appending a value --------------------------
a=[]
for i in range(4):
    a.append(i)
print(a)
#in array we can not cange the size
# ---------------------------------------------------------------------------------------

#------------------- input data in 2d array using a function ----------------------------
import numpy as tuhin
m= int(input("ENTER THE NUMBER OF ROWS \t"))
n = int (input("ENTER THE NUMBER OF COLUMNS \t"))
column_1 = []
for i in range(m):
    column_1.append([])
    
for i in range(m):
    for j in range(n):
        column_1[i].append(j)
        column_1[i][j] = 1
# print("\?n")
for i in range(m):
    for j in range(n):
        column_1[i][j] = 2*(i+j)
c11 = tuhin.array(column_1)
print(column_1,"\n",c11)
