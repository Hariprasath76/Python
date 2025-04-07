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

symbol = str(input("Enter a Symbol: "))
num = int(input("Enter a number: "))

for i in range(num):  #OuterLoop
    for j in range(num): #InnerLoop
        print(symbol, end="")
    print() #newLine












