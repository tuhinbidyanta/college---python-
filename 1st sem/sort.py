#sorting in accending order

#using sort() function
a1 = [3,8,7,5,6,2]
a1.sort()
print("sorting in accending order using function ",a1)

#without using sort() funtion 
a2 = [3,8,7,5,6,2]
a2_result = []
length = 6 #this is the number of element of a2 list
for j in range(6):
    tuhin = a2[0]
    for i in a2:
        if(i<tuhin):
            tuhin = i 
    a2_result.append(tuhin)
    a2.remove(tuhin)            
print("sorting in accending order without using function ",a2_result)

# sorting in decending order

#using sort() function
d1 = [3,8,7,5,6,2]
d1.sort()
d1.reverse()
print("sorting in decending order using function ",d1)

#without using sort() funtion 
d2 = [3,8,7,5,6,2]
d2_result = []
length = 6 #this is the number of element of a2 list
for j in range(6):
    tuhin = d2[0]
    for i in d2:
        if(i>tuhin):
            tuhin = i 
    d2_result.append(tuhin)
    d2.remove(tuhin)            
print("sorting in decending order without using function ",d2_result)





