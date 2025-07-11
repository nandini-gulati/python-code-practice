def add_details(student):
    f=open(student.txt,"w")
    n=input("Enter Name: ")
    s=int(input("Enter semester: "))
    m1=int(input("Enter Marks1: "))
    m2=int(input("Enter Marks2: "))
    m3=int(input("Enter Marks3: "))
    f.write(n+"\t"+s+"\t"+m1+"\t"+m2+"\t"+m3+"\n")
    f.close()
def update(student):
    f=open(student.txt,"w")
    x=i.readlines()
    l=input("enter student name to update semester:")
    for i in x:
        s=i.split("\t")
        if(s[0]==1):
            s[l]=str(int(s[1]+1))
            f.write(s)
    f.close()
def display(student):
    f=open(student.txt,"r")
    for i in f:
        print(i)
    f.close()
def add_avg(student):
  f=open(student,"w")
def main():
    while True:
        print("Menu:")
        print("1. Add Student details: ")
        print("2. Display Student details: ")
        print("3. calculate average marks :")
        print("4. Update semester: ")
        print("5. Exit")
        ch = input("Enter your choice: ")
        if ch == '1':
          add_details()
        elif ch == '2':
          display(student)
        elif ch == '3':
          add_avg(student)
        elif ch == '4':
          update(student)
        elif ch == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
