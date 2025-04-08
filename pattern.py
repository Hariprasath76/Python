#Pattern Printing:

#Square Loop Using While loop:
"""
symbol = str(input("Enter a Symbol: "))
num = int(input("Enter a number: "))
b =1
while b<=num:       #OuterLoop , No.of rows
    a=1
    while a<=num:   #innerLoop , No.of Colum
        print(symbol, end ="")
        a=a+1

    print()     #Empty Line
    b =b+1
"""

#Square Loop Using For loop:

"""
symbol = str(input("Enter a Symbol: "))
num = int(input("Enter a number: "))

for i in range(num):  #OuterLoop
    for j in range(num): #InnerLoop
        print(symbol, end="")
    print() #newLine
"""


#Print a Left handed Triangle pattern:
#While Loop:
#
# #
# # #

"""num =3
symbol ="#"

counter=1
b=1
while b<=num:
    a=1
    while a<=counter:
        print(symbol, end="")
        a+=1
    print()
    b+=1
    counter+=1
"""

#For Loop:

"""
symbol = str(input("Enter a Symbol: "))
num = int(input("Enter a number: "))

for j in range(1,num+1):
    for i in range(j):
        print(symbol,end="")
    print()
"""



#Right handed Triangle: for loop
"""
num =int(input("Enter a num: "))
symbol = str(input("Enter a symbol: "))

white_space = num -1

for i in range(1, num+1):

    for j in range(white_space):
        print(" ", end ="")
    white_space -= 1

    for k in range(i):
        print(symbol, end="")
    print()
"""


#While Loop - Right handed triange:
"""
num =int(input("Enter a num: "))
symbol = str(input("Enter a symbol: "))

white_space = num -1

i=0
while i<=num:
    j=0
    while j<=white_space:
        print(" ",end ="")
        j +=1
    white_space -= 1

    k= 0
    while k<i:
        print(symbol, end="")
        k+=1
    print()
    i +=1
"""


#Equal Triagle ->
""" 
    *
   * *
  * * * 
 * * * *
* * * * *
"""
"""
num =int(input("Enter a num: "))
symbol = str(input("Enter a symbol: "))

white_space = num -1

for i in range(1, num+1): #start from 1 , num +1 

    for j in range(white_space):
        print(" ", end ="") # Emtpy space.
    white_space -= 1

    for k in range(1,i*2):  #start from 1 , i* by 2.
        print(symbol, end="")
    print()
"""


"""
# Diamond Pattern using while loop
n = 3  # height of upper half (excluding middle)
i = 0
# Upper half
while i < n:
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
    i += 1
i = n - 2
# Lower half
while i >= 0:
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
    i -= 1
"""



# Diamond Pattern using for loop
n = 3  # height of upper half (excluding the middle line)

# Upper half including middle line
for i in range(n):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# Lower half
for i in range(n - 2, -1, -1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)






