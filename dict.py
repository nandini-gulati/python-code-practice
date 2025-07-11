'''d={}
n=int(input("enter number of key value pairs you want:"))
for i in range n:
    k=int(input("enter keys:"))
    v=int(input("enter values:"))
    d[k]=v
print(d)
sum=0
for j in range n:
    sum=sum+v
print(sum)'''

#create dictionnary of n students where key is rollno and value is cgpa
#a) display all student details
#b) display topper roll no
#c) find average cgpa of all students
#d) find stuents with cgpa <5.0,reduce their cgpa by 1.0 and display updated dictionary
'''d={}
s=0
n=int(input("enter number of students:"))
for i in range (n):
    k=int(input("enter roll number:"))
    nm=input("enter name:")
    v=float(input("enter cgpa:"))
    d[k]=(nm,v)
print(d)
for j in range (n):
    s=s+v
    avg=s/n
print("average cgpa of all students:",avg)
for a in d:
    if d[[a]==sorted(d.values())[-1]:
         print(a)'''


#store details of n movies in a dictionary by taking input from the user. each movie must store details like name, year,director name,production cost, collection made(earning) and perform the following: 
#a) print all movie details
#b) display names of movies released before 2015
#c) print movies that made a profit
#d) print movies directed by a particular director
d={}
n=int(input("enter number of movies:"))
for i in range (n) :
    mn=input("enter movie name:")
    y=int(input("enter year:"))
    dn=input("enter director name:")
    p=int(input("enter production cost: "))
    e=int(input("earning made:"))
    t={"YEAR":y,"DIRECTOR NAME":dn,"PRODUCTION COST":p,"EARNINGS":e}
    d.update({mn:t})
print(d)
print("Movies released before 2015:")
for x in d:
    if d[x]["YEAR"]<2015:
        print(x)
print("Movies that made profit")
for i in d:
    if d[i]["EARNINGS"]>d[i]["PRODUCTION COST"]:
        print(i)

    





    
