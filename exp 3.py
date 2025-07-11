#Check whether given number is divisible by 3 and 5 both.
'''n=int(input("enter a number:"))
if (n%3==0 and n%5==0):
    print (n,"is divisible by 3 and 5 both")
else:
    print (n,"is not divisible by 3 and 5 both")'''

#Check whether a given number is multiple of five or not
'''n=int(input("enter a number:"))
if n%5==0:
    print (n,"is a multiple of 5")
else:
    print (n,"is not a multiple of 5")'''

#Find the greatest among two numbers. If numbers are equal than print “numbers are equal”
'''n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if n1>n2:
    print (n1,"is geater than",n2)
elif n2>n1:
    print (n2,"is geater than",n1)
    
else:
    print ("numbers are equal")'''

#Find the greatest among three numbers assuming no two values are same.
'''n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print (n1,"is the greatest number")
elif n2>n1 and n2>n3:
    print (n2,"is the greatest number")
else:
    print (n3,"is the greatest number")'''

#Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
'''import cmath
a =int(input("enter coefficient of x^2:"))
b =int(input("enter coefficient of x:"))
c =int(input("enter constant value:"))
print("The quadratic equation is:",a,"x^2 +",b,"x +",c,"=0")
d= (b**2)-(4*a*c)
if d>0:
    print("roots are real")
else:
    print("roots are imaginary")
ans1 = (-b-cmath.sqrt(d))/(2 * a)
ans2 = (-b + cmath.sqrt(d))/(2 * a)
print('The roots are',ans1,"and",ans2)'''


#Find whether a given year is a leap year or not.
'''y=int(input("enter year:"))
if (y%4==0 and y%100!=0 or y%400==0):
    print (y,"is a leap year")
else:
    print (y,"is not a leap year")'''

#Write a program which takes any date as input and display next date of the calendar e.g. I/P: day=20 month=9 year=2005 O/P: day=21 month=9 year 2005
'''day=int(input("Enter the day :"))
month=int(input("Enter the month :"))
year=int(input("Enter the year :"))
print("\n")
print("Entered date : ")
print("Day =",day," ","Month =",month," ","Year =",year)
if month in(1,3,5,7,8,10):
    if day==31:
        day=1
        month=month+1
    else:
        day=day+1
elif month in(4,6,9,11):
    if day==30:
        day=1
        month=month+1
    else:
        day=day+1
elif month==2:
    if (year%4==0 and year%100!=0 or year%400==0):
        if day==29:
            day=1
            month=month+1
        else:
            day=day+1
    else:
        if day==28:
            day=1
            month=month+1
        else:
            day=day+1
elif month==12:
    if day==31:
        day=1
        month=1
        year=year+1
    else:
        day=day+1
else:
    print("Values entered are invalid")
print("updated Date : ")
print("Day =",day," ","Month =",month," ","Year =",year)'''

#Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
'''name=input("Enter name: ")
roll=input("Enter Roll number: ")
sap=int(input("Enter SAP ID: "))
sem=int(input("Enter semester: "))
course=input("Enter the course: ")
total=0
n1=int(input("Enter marks in DSA:"))
n2=int(input("Enter marks in Python:"))
n3=int(input("Enter marks in Computer Organisation:"))
n4=int(input("Enter marks in Maths:"))
n5=int(input("Enter marks in Physics:"))
total=n1+n2+n3+n4+n5
per=total/5
cgpa=per/10
if cgpa>=0 and cgpa<=3.4:
    grade="F"
elif cgpa>=3.5 and cgpa<=5.0:
    grade="C+"
elif cgpa>=5.1 and cgpa<=6:
    grade="B"
elif cgpa>=6.1 and cgpa<=7:
    grade="B+"
elif cgpa>=7.1 and cgpa<=8:
    grade="A"
elif cgpa>=8.1 and cgpa<=9:
    grade="A+"
elif cgpa>=9.1 and cgpa<=10:
    grade="O (Outstanding)"
else:
    print("Invalid data")
print("\n")
print("GRADESHEET")
print("Name :",name)
print("Roll Number :",roll)
print("SAP ID :",sap)
print("Semester :",sem)
print("Course :",course)
print("\n")
print("Subject name:"," ","Marks")
print("DSA:"," ",n1)
print("Python:"," ",n2)
print("Computer organisation:"," ",n3)
print("Maths:"," ",n4)
print("Physics:"," ",n5)
print("Percentage :",per,"%")
print("CGPA :",cgpa)
print("GRADE :",grade)'''
