#revesing a tuple without using colon
'''n=int(input("enter number of elements you want in tuple:"))
t1=()
for i in range (n):
    a=int(input("enter element:"))
    t1=t1+(a,)
print(t1)
t2=()
for i in t1:
    t2=(i,)+t2
print(t2)'''

#concatenate tuple 1 and 2
'''t1=()
t2=()
t3=()
n1=int(input("enter number of elements you want in tuple1:"))
for i in range (n1):
    a=int(input("enter element:"))
    t1=t1+(a,)
print("tuple 1:",t1)
n2=int(input("enter number of elements you want in tuple2:"))
for j in range (n2):
    b=int(input("enter element:"))
    t2=t2+(b,)
print("tuple 2:",t2)
t3=t1+t2
print("tuple 3:",t3)'''

'''t1=()
t2=()
t3=()
n1=int(input("Enter number of elements in first tuple : "))
n2=int(input("Enter number of elements in second tuple : "))
for i in range(n1):
    a=int(input("Enter element for first tuple : "))
    t1=t1+(a,)
print("First Tuple : ",t1)
for i in range(n2):
    b=int(input("Enter element for second tuple : "))
    t2=t2+(b,)
print("Second Tuple : ",t2)
t3=t1+t2
print("Third tuple : ",t3)
ten_count=0
pos_count=0
neg_count=0
zero_count=0
for i in t3:
    if i>=10:
        ten_count=ten_count+1
for i in t3:
    if i>0:
        pos_count+=1
    elif i<0:
        neg_count+=1
    else:
        zero_count+=1
print("Numbers greater than 10 : ",ten_count)
print("Positive numbers : ",pos_count)
print("Negative numbers : ",neg_count)
print("Number of zero : ",zero_count'''

t=(10,20,-30,40,-12,4,-6,7,8,-90)
cneg=len([x for x in t if x<0])


