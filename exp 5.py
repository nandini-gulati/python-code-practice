#Experiment 5: String and Sets 

#Write a program to count and display the number of capital letters in a given string. 
'''s=input("enter a string:")
count=0
for i in s:
    if i.isupper():
        count+=1
print("Number of capital letters are:",count)'''

#Count total number of vowels in a given string.
'''s=input("enter a string:")
count=0
for i in s:
    if i in 'AEIOUaeiou':
        count+=1
print("total number of vowels are:",count)'''

#Input a sentence and print words in separate lines.
'''s=input("enter a sentence:")
r=s.split()
for i in r:
    print(i)'''


#WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 
'''Sample Input 
ABCDCDC 
CDC 
Sample Output 
2'''
s=input("enter a string:")
sb=input("enter a substring:")
count=0
if sb in s:
    count+=1
print ("number of times subtring is present in string:",count)

#Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same. 
'''Sample Input 
ABaBCbGc 
Sample Output
2A 
3B 
2C 
1G'''

#Program to count number of unique words in a given sentence using sets. 

#Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
#a) Fruits which are in both sets s1 and s2 
#b) Fruits only in s1 but not in s2 
#c) Count of all fruits from s1 and s2 

#Take two sets and apply various set operations on them : 
#S1 = {Red ,yellow, orange , blue } 
#S2 = {violet, blue , purple}
