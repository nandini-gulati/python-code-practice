'''def simple_int(p,r,t):
    si=p*r*t
    return si
x=int(input("Enter principle : "))
y=int(input("Enter Rate : "))
z=int(input("Enter Time :"))
a=simple_int(x,y,z)
print(a)'''

#write a fnction which will take list of integers as input then output will be square of those integers
def square_integers(input_list):
    squared_list = [num ** 2 for num in input_list]
    return squared_list
def square(lst):
    for i in lst:
        a=i**2
        l2.append(a)
        return l2
l1=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    b=int(input("Enter number :"))
    l1.append(b)
l2=[]
def square(lst):
    for i in lst:
        a=i**2
        l2.append(a)
    return l2
l1=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    b=int(input("Enter number :"))
    l1.append(b)
print(l1)
print("New list :",square(l1))
