#set is mutable but elements of set are immutable
#set cannot have mutable things
#ques6
'''s=set()
str=input("Enter a sentence : ")
print(set(s))
a=str.split()
print(set(a))

#ques7
s1=set()
s2=set()
n1=int(input("Enter number of elements in SET 1 : "))
n2=int(input("Enter number of elements in SET 2 : "))
for i in range(n1):
    a=input("Enter fruit name for SET 1: ")
    s1.add(a)
for j in range(n2):
    b=input("Enter fruit name for SET 2 : ")
    s2.add(b)
print(" ")
x=(s1&s2)
print("Fruits which are in both s1 and s2 : ",x)
print(" ")
y=s1-s2
print("Fruits only in s1 not in s2 :",y)
print(" ")
z=(s1|s2)
count=len(z)
print("Count of all fruits from s1 and s2 : ",count)

#ques 8
S1={"Red","yellow","orange","blue"}
S2={"violet","blue","purple"}
print(S1^S2)
{'purple', 'Red', 'orange', 'violet', 'yellow'}
print(S1|S2)
{'orange', 'violet', 'purple', 'blue', 'yellow', 'Red'}
print(S1&S2)
{'blue'}'''

#create a set of n int elements and create another set where 


