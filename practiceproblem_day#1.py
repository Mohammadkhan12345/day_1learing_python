
        #**print "HELLO WORLD"**
print("hello world")


        #**add two numbers**
a=int(input("enter your first number"))
b=int(input("enter your second number"))
sum = a+b
print("The sum of two numbers is ",sum)



        #**program to find square root** 
import math
num =int(input("enter a number here: "))
square_root = math.sqrt(num)
print(square_root)
    #second method 
num = int(input("enter a number here: "))
sr = num**(0.5)     #you can also use num**(1/2)
print("the square root of the given number is" ,sr)



        #**calculate area of rectangle**
l = int(input("enter the length of rectangle: "))
b = int(input("enter the breadth of rectangle: "))
area = l*b
print("the area of rectangle is ",area)



        #**calculate area of triangle**
height = float(input("please enter your height value"))
base = float(input("please enter your base value"))
area = 0.5*height*base
print("the area of triangle is ",area)



        #**Swap two variables**
x = int(input("enter the value of X "))
y = int(input("enter the value of Y "))
temp = x
x = y
y = temp
print("The values have been swaped")
print("the value of X is ",x)
print("the value of Y is ",y)

    #second method 
x = int(input("enter the value of X "))
y = int(input("enter the value of Y "))
x,y = y,x
print("The values have been swaped")
print("the value of X is ",x)
print("the value of Y is ",y)



        #**kiloimeters to miles converter**
km = float(input("enter your km value "))
miles = km * (0.621371)
print(km,"kilometers in miles will be",miles,"miles") 



        #**program to check is a number positive or negative or zero?**
a=int(input("enter your number to check its state "))
if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
elif a==0:
    print("the given number is zero")
else:
    print("Invalid input!")



        #**program to check is a number EVEN OR ODD**
num = int(input("please enter your number to check whether even or odd "))
if num % 2 == 0:
    print("This number(",num,") is even")
else:
    print("This number(",num,") is odd")