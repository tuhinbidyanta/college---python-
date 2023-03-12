# conditions means if else statement

age = int(input("write down your age here"))

if age < 10:
    print("choti bacchi ho tum")
elif(age>=10)&(age<18):
    print("jao bacche pogo dekho")
elif ((age >= 18)&(age <60)): # here we used and operator
    print("adult ho gaye ho tum")
else:
    print("buddha sala jake aram karo")

