#Arithmetic Operation [Maths]
"""
print(10+10) 
print(10-10)
print(10*10)
print(10/10) 

print(10 ** 3) #10 power of 3 = 10x10x10 =1000
print(10 // 3) #Quotient
print(10 % 3) #Remainder"
"""

#Assignment Operation
#=, += , -=, /=, *=, **=, //=, %=
"""
a=10
print(a)  #10

a += 5   #a =a +5  = 10+5 = 15
print(a) #a=15

a *= 2  #a = a*5 = 15*2 =30
print(a) #a = 30

a %=4
print(a)

a **=a
print(a)
"""

#Comparision operators:
# ==, !=, >, <, >=, <=
"""
a =5
b=5
print(a==b)

print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
"""

#Logical Operators:
# and, or, not
"""
print(10==10 and 5<6)
print(10==10 and 5>6)
print(10!=10 or 5==6)
print(not 10==10)
print(not 5==10)
"""

#Python Collection:
#list[], turple(), set{} , Dictionary{Key:Value}
#list - ordered & Chargeable & duplicated
#turple - ordered & Unchargeable & duplicated
#set - unordered & unindexed & no Duplicated
#Dictionary - unordered & indexed & No Duplicated


#List[]
"""
a=[1,2,3,4,5,5,5]
print(a, type(a))

print(a[0])  #Ordered
a[0]= "hari" #chargeable
print(a)

print(a)  #allows duplicate 5555
""" 

#Turple
"""
a = (1,2,3,4,5)
print(a,type(a))
print(a[1]) #ordered
print(a) # allows_duplication
a[1]=99 #unchargeable it will be a error --> TypeError: 'tuple' object does not support item assignment
""" 

#Set
"""
a={1,2,"hari",1,1,1,2,2,2,3,3,2,1}
print(a,type(a))

#print(a[2]) #Unordered TypeError: 'set' object is not subscriptable
#No_Duplication
#No_Indexing
"""

#Dictionary --> #unordered, idexed
""" 
a={"Name":"Hari",
   "Office":"GroupPal",
   "Age": 21}
print(a)

a={"Name":"Sara"} #Changeable
print(a , type(a))
"""



#Mutable && Immutable
#Mutable --> List, Set, Dict
#Immutable --> int, float, bool, str, turple

#Immutable
"""
a=1
b=1
print(id(a)) #If you are giving the same value means -> Memory address is same. 
print(id(b)) # Same data store in same location.
"""

#Mutable
"""
a=[10,20,30]
b=[10]
print(id(a)) #If you are giving the same value means ->Memory address is different.
print(id(b)) #Same data store in different location.
""" 

#Identity Operator:
#is , not is 
"""
#Immutable
a=10
b=10
print(a==b)
print(a is b)  #Is means its check the memory location is same or not [Same means True]

c=20
print(a is c) #Not means False
"""

#Mutable
""" 
a=[10,20,30]
b=[10,20,30]

print(a==b)
print(a is b)
"""

#Membership Operation:
#in , not in
""" 
a=[1,2,3,4,5]
b=3
print( b in a)
print(3 in a)
print(1 not in a)
print(3 in [1,2,3,4,5])
"""

#BitWise Operator:
#10 --> 0000 1010 
#2  --> 0000 0010
#        ---------

print(10 & 2) # & - AND
print(10 | 2) # | OR
print(10 ^ 2) # ^ EXOR