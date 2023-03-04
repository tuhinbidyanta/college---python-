#average using function
list1 = [1,2,3,4,5,6]
avg1 = sum(list1)/len(list1) #len() function helps to find the number of element of any list
print(f"the average of the list is {avg1}")

# average with out using a function

# simple approach
list2 = [1,2,3,4,5,6]
avg2 = 0
length = 6
for i in range(6):
    avg2 = avg2 + list2[i]
avg2 = avg2/length
print("the average of the list without function in simple aproach",avg2)

#complex approach
list3 = [1,2,3,4,5,6]
avg3 = 0
length = 0
for i in list3:
    avg3 = avg3 +i
    length += 1
avg3 = avg3/length
print(f"the average of the list without function complax approatch {avg3}")


