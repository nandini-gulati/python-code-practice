#Experiment 6
n=int(input("Enter number of elements: "))
lst=[]
for i in range(n):
    a=int(input("Enter number : "))
    b=a*a*a
    lst=lst+[b]
for i in range(len(lst)):
    print( "[",lst[i],end=",", "]" )
