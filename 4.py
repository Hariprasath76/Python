#if-elif-else:

""" 
a =20
b= 15
if a>b:
    print(a, "is bigger than", b)
else:
    print(a, "is smaller than", b)
"""
#Age calculator:
""" 
a=int(input("please enter the age: "))

if a > 18:
    print("yes for vote")
else:
    print("no for vote")
"""

#If-Elif-Else:
""" 
a=int(input("please enter the value: "))
if a>20:
    print(a, "is bigger than 20")
elif a==20:
    print(a,"is equal to 20")
else:
    print("please enter the valid number")
"""

#Nested If Else:
""" 
Drink=input("Please enter \"C\" or \"T\" Choose Coffee or Tea: ")

if Drink == "C":
    print("Coffee is Selected")
    Sugar=input("do you want sugar Yes/No :")
    if Sugar == "Yes":
        print("Coffee is getting prepared with sugar")
    elif Sugar == "No":
        print("Coffee is getting prepared without sugar")
    else:
        print("please give the valid input")

elif Drink == "T":
    print("Tea is Selected")
    Sugar=input("do you want sugar Yes/No :")
    if Sugar == "Yes":
        print("Tea is getting prepared with sugar")
    elif Sugar == "No":
        print("Tea is getting prepared without sugar")
    else:
        print("please give the valid input")

else:
    print("please give a valid input")
"""

#Get 2 inputs from the User And find the greatest number between them:
""" 
a = int(input("Please Enter a number of a: "))
b = int(input("Please Enter a number of b: "))

if a>b:
    print(a, "is bigger then", b)
elif a==b:
    print(a, "is equal then", b)
elif a<b:
    print(b, "is bigger then", a)
else:
    print(a, "is smaller than", b)
"""


#Get 3 Input from the user and find the greatest number between then:

""" 
a = int(input("please enter a number for a: "))
b = int(input("please enter a number for b: "))
c = int(input("please enter a number for c: "))

if a>b and a>c:
    print(a, "is bigger then both of b & c")
elif b>a and b>c:
    print(b, "is bigger then both of a & c")
elif c>a and c>b:
    print(c, "is bigger then both of a & b")
else:
    print("thank you")
"""


    
