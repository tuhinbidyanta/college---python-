#list
#type of list (1)1d list (2)2d list or matrix (3)nd list
# example of 1d list is [1,2,5,5,3,5,8]
#  example of 2d list is [[1,2],[5,5]] this is known as 2x2 matrix

#---------------------
# 1d list manipulation
#---------------------

# -------------------------------------length of list---------------------------------------

#length of list using len() function
a=[1,2,5,5,3,5,8]
length = len(a)
print("length of list usin len() funtion is",length)
#length of list without using len() function
a=[1,2,5,5,3,5,8]
length1 = 0
for i in a:
    length1 = length1 + 1
print("length of list without using len() function is",length1)
#---------------------------------------------------------------------------------------

#-----------------------------------maximum value of list---------------------------------------

#maximum value of list using max() function
a=[1,2,5,9,3,5,8]
max_value = max(a)
print("the maximum value of list using max() function is",max_value)
#macimum value of list without using max() function
a=[1,2,5,9,3,5,8]
max_value = 0
for i in a:
    if i>max_value:
        max_value = i
print("the maximum value of list without using max() function is",max_value)
#---------------------------------------------------------------------------------------------

#-----------------------------------minimum value of list---------------------------------------

#minimum value of list using min() function
a=[1,2,0,5,3,5,8]
min_value = min(a)
print("the minimum value of list using min() function is",min_value)
#minimum value of list without using min() function
a=[1,2,0,5,3,5,8]
min_value = a[0]
for i in a:
    if i<min_value:
        min_value = i
print("the minimum value of list without using min() function is",min_value)
#---------------------------------------------------------------------------------------------

#-------------------------appending value into a list ----------------------------------------
a=[1,2,0,5,3,5,8]
a.append(19) # now the value appended into list
print("after appending the value into list",a)
#---------------------------------------------------------------------------------------------

#------------------------removing a value from list-------------------------------------------
a=[1,2,0,5,3,5,8]
a.remove(2) #it remove the element 2
print("after removing the element 2 the list is",a)
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------list slicing------------------------
#this is the most important part in list 
#naturally the index of list starts from 0
a=[1,2,0,5,3,5,8] 
#1 element has index 0
#2 element has index 1
# same way
print("the value of index 0 ",a[0])
print("the value of index 1 ",a[1])
print("the value of index 2 ",a[2])
print("the value of index 3 ",a[3])
# list slicing
print(a[0:3])
print(a[:3])
print(a[3:])
# -----------------------------------------------------------------------------------------------

#--------------------------------------------------------array ----------------------------------
a=[1,2,0,5,3,5,8] 
import numpy as np
# to know about numpy in details visit numpy official website 
# to know about all numpy function import numpy and then print(dir(numpy))
array = np.array(a)
print(array) # the comma will not apear in array
#you can apply any list operation in array and many more
#-------------------------------------------------------------------------------------------------



