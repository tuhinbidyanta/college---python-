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
