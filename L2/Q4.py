from math import *
#a+b=10
a=0
b=10
while(a!=b):
    if(a<b):
        a=a+1
        b=b-1
    if(a>b):
        b=b+1
        break
print(a,b)
#a+b+c=20
c=20
while(a+b!=c):
    if(a+b<c):
        c=c-1
while(a+b+c==20):
    break
print(a,b,c)
#a+b+c+d=60
d=60
while(a+b+c!=d):
    if(a+b+c<d):
        d=d-1
while(a+b+c+d==60):
    break
print(a,b,c,d)
print(a*b+b*c+c*d)