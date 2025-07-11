

passw=input("enter your password:")

l=0
u=0
s=0
for i in passw:
    if i.islower():
        l+=1
if l<2:
    print("password should contain atleast 2 lowercase characters")
else:
    for j in passw:
        if j.isupper():
            u+=1
if u<2:
    print("password should contain atleast 2 uppercase characters")
else:
    for k in passw:
        if k.isdigit():
            s+=1
if s<1:
    print("password should contain atleast 1 digit")
elif(len(passw)<=8):
    print("Weak Password: Password should not have less than 8 characters")
elif (len(passw)>8 and len(passw)<=10):
    print("medium level password")
elif (len(passw)>10):
    print("strong Password")

    

        

    
    


    

