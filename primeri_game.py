from random import*
from time import*
v = 0
p =0
c=0
while v<10:
    a = randint(1,20)
    print(a)
    
    b = randint(1,20)
    
    g =randint(1,4)
    if g==1:
        c=a+b
        print("+")
        
    if g==2:
        print("-")
        c=a-b
        
    if g==3:
        print("/")
        c=a//b
        
    if g==4:
        print("*")
        c=a*b


    print(b)
    t=time()
    d =int(input())
    l= time()-t
    if d == c and l<200:
        print("верно")
        p=p+1
        v=v+1
    else:
        print("неверно")
        v=v+1
print("правельно", p,"из", v)
input()
