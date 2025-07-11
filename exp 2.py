#Experiment 2: Use of input statements, operators

#Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, perform addition, multiplication, division and subtraction on these two variables and Print out the result.
'''x=9
y=7
z=x+y
print("Sum of",x,"and",y,"is",z)
z=x-y
print("Subtraction of",x,"and",y,"is",z)
z=x*y
print("Multiplication of",x,"and",y,"is",z)
z=x/y
print("Division of",x,"and",y,"is",z)'''


#Write a Program where the radius is taken as input to compute the area of a circle.
'''a=int(input("Enter the radius: "))
area=3.14*a*a
print("Area of circle = ",area)'''

#Write a Python program to solve (x+y)*(x+y)
'''x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
a=(x+y)**2
print(a)'''

#Write a program to compute the length of the hypotenuse of a right triangle using Pythagoras theorem.
'''p=int(input("Enter the value of perpendicular: "))
b=int(input("Enter the value of base: "))
h=((p*2)+(b2))*0.5
print("Hypotenuse of triangle =",h)'''

#Write a program to find simple interest.
'''a=int(input("Enter the value of principle: "))
b=int(input("Enter the value of rate: "))
c=int(input("Enter the value of time: "))
si=(a*b*c)/100
print("Simple Interest =",si)'''

#Write a program to find area of triangle when length of sides are given.
'''b=int(input("Enterthe base of triangle : "))
h=int(input("Enter the height of triangle : "))
area=0.5*b*h
print("The area of triangle =",area)'''

#Write a program to convert given seconds into hours, minutes and remaining seconds.
'''sec=int(input("Enter number of seconds : "))
hour=sec//3600
rem=sec%3600
minute=rem//60
sec=rem-60
print("Number of hours =",hour)
print("Number of minutes =",minute)
print("Number of seconds =",sec)'''

#Write a program to swap two numbers without taking additional variable.
'''x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("First number :",x)
print("second number :",y)
x,y=y,x
print("After swapping ;")
print("--------------")
print("First number :",x)
print("second number :",y)'''

#Write a program to find sum of first n natural numbers.
'''n=int(input("Enter a number : "))
sum=0
for i in range(0,n+1):
    sum=sum+i
print("Sum of n natural numbers =",sum)'''

#Write a program to print truth table for bitwise operators( & , | and ^ operators)
'''print("Truth Table for Bitwise AND (&):")
print("0 & 0 =", 0&0)
print("0 & 1 =", 0&1)
print("1 & 0 =", 1&0)
print("1 & 1 =", 1&1)

print("\nTruth Table for Bitwise OR (|):")
print("0 | 0 =", 0|0)
print("0 | 1 =", 0|1)
print("1 | 0 =", 1|0)
print("1 | 1 =", 1|1)

print("\nTruth Table for Bitwise XOR (^):")
print("0 ^ 0 =", 0^0)
print("0 ^ 1 =", 0^1)
print("1 ^ 0 =", 1^0)
print("1 ^ 1 =", 1^1)'''

#Write a program to find left shift and right shift values of a given number.


#Using membership operator find whether a given number is in sequence (10,20,56,78,89)



#Using membership operator find whether a given character is in a string.
'''string=input("Enter a string : ")
char=input("Enter a character : ")
if char in string:
    print("The character",char,"is present in the string")
else:
    print("The character",char,"is not present in the string")'''
