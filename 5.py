#While Loop 
#Run & Debug activate for step by step excution.
"""
a=1 #Initilization
while a<5: #Condition
    print(a) 
    a += 1 #Increasement
    print("Hello_World!")

print("loop endded")
""" 

#While Loop (inifinity loop)
""" 
a=1
while a > 0:
    print(a)
    a = a+1
"""



#While loop + Break :
""" 
a=1
while a<=10:
    print(a)
    if a==5:
        break
    a+=1
"""


#While + Continue:
"""
a=1
while a<=10:
    a+=1
    if a==5 or a==7:
        continue
    print(a)
print("Loop Over")
""" 

#While Else:
""" 
a=1
while a<4:
    print(a)
    if a==7:
        break
    a+=1
else:
    print(a,"is no longer than 6")
"""




#For Loop: String/List/number Range()
#Syntax:
    #For <variable> in <iterables>:
    #For <variable> in <string/list/turple/set/dict/range()>:

#For + List:
""" 
fruit =["apple", "bannana", "grape"]
for i in fruit:
    print(i)
"""

#For + String:
""" 
for  i in "apple" :
    print(i)
"""

#For + Range:
#Start from 0 to 9:
""" 
for i in range(10):
    print(i)
"""

#Start from 10 to 49
""" 
for i in range(10,50):
    print(i)
"""

#Start from 10 to 50 (5 increment 10,15,20 ----45)
"""
for i in range(10,50,5):
    print(i)
"""

#For + Break:
"""
fruits =["apple","bannana","grape"]
for i in fruits:
    if i=="bannana":
        break
    print(i)
"""
#For +Continue:
"""
fruits =["apple","bannana","grape"]
for i in fruits:
    if i=="bannana":
        continue
    print(i)
""" 


#For +Else:
""" 
fruits = ["apple","bannana","grape"]
for i in fruits:
    if i == "Bannana":
        break
    print(i)
else:
    print("for loop run successfully fillend")
"""


#Nested Loop:
""" 
colour = ["black","red","yellow"]
object =["car","bike"]

for i in colour:
    for j in object:
        print(i,j)
"""

""" 
rows = 27

for i in range(rows):
    print("#", end=" ")
    for j in range(i):
        print(chr(97 + j), end=" ")
    print()
"""


rows = 4

for i in range(1, rows + 1):
    print("#" * i )



