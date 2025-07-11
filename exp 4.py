#Experiment 4: Loops

# Find a factorial of given number.
'''n=int(input("enter number:"))
fact=1
if n>1:
    for i in range(1,n+1):
       fact= fact*i
    print("The factorial of",n,"is",fact)
else:
   print("invalid input")'''


# Find whether the given number is Armstrong number.
'''n=int(input("enter number:"))
order = len(str(n))
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")'''


# Print Fibonacci series up to given term.
'''num= int(input("enter number of terms:"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")'''

# Write a program to find if given number is prime number or not.
'''n=int(input("enter a number:"))
if n==1:
   print(n,"is neither a prime number nor a composite number")
elif n>1:
   for i in range (2,int(n/2)+1):
      if(n%i)==0:
         print(n,"is not a prime number")
         break
   else:
      print(n,"is a prime number")
      
else:
   print("enter a positive numer")'''


# Check whether given number is palindrome or not.
'''n=int(input("enter a number:"))
sum=0
originaln=n
while n>0:
   rem=n%10
   sum=sum*10+rem
   n=n//10
if originaln==sum:
   print("number is a palindrome")
else:
   print("number is not a palindrome")'''

   

# Write a program to print sum of digits.
'''n=int(input("enter a number:"))
sum=0
while n>0:
   rem=n%10
   sum+=rem
   n=n//10
print(sum)'''

# Count and print all numbers divisible by 5 or 7 between 1 to 100.
'''count=0
for i in range (1,101):
   if i%5==0 or i%7==0:
      count+=1
      print(i,end=" ")
print("\ntotal:",count)'''


# Convert all lower cases to upper case in a string.
s=" "
st=input("Enter a string : ")
for i in st:
    if i>='a' and i<='z':
        c=chr(ord(i)-32)
        s+=c
    else:
        s+=i
print("UPDATED OUTPUT : ",s)

# Print all prime numbers between 1 and 100.
'''for i in range (1,101):
      if i>0 :
         for j in range (2,int(i/2)+1):
            if i%j==0:
               break
            else:
               print(i,end=" ")'''

# Print the table for a given number
'''n=int(input("display multiplication of:"))
for i in range (1,11):
   a=n*i
   print(n,"*",i,"=",a)'''
