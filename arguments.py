'''defs3 fun(l):
    return list(set(l))
l=[10,20,20,10,30,40,30,10,20]
res=fun(l)
print ("list:",res)
'''


'''def fun(a,*b):
    print(a,b)
    return True
res=fun(10,20,30,40,50)
print(res)


def fun(a,*b):
    print(a,b)
    return a+sum(b)
res=fun(10,20,30,40)
print(res)

def vol(r,h,pi):
    print(r,h)
    return pi*r*r*h
res=vol(20,10,3.14)
print(res)

def fun(a,b):
    return a+b, a-b, a*b, a/b
f=fun(10,20)
print("sum=",f[0])

def fun(l):
    
    return list(set(l))
l=[10,10,20,30,30,50]
res=fun(l)
print("list",res)

#recursion
def fun(n):#sum of first n natural numbers
    if n==1:
        return 1
    else:
        return n+fun(n-1)

print(fun(5))

def fun(n):
    if n<=1:
        return 1
    elif n%2==1:
        return n+fun(n-1)
    else:
        return n-fun(n-1)

print (fun(6))

#lamba function
si-lambda p,r,t:p*r*t/100
print(si(10,20,3))'''



