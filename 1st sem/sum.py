# sum using function
list1 = [1,2,3,4,5,6]
add1 = sum(list1)
print("sum with using a function ",add1)

# with out function
list2 = [1,2,3,4,5,6]
temp = 0
length = 6 #this is the number of element of list 2
for i in range(length):
    temp = temp + list2[i]
print(f"sum without using a functon {temp}") #this is the formatted printing type