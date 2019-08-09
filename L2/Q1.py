from math import *
n=int(input("Enter a positive integer "))
x=2
while n>x:
     if(n%x==0):
        print("It is not a prime number")
        break
     else:
        x=x+1
        print("n %d,x %d" % (n,x))
     if(n%x!=0):
        print("It is a prime number")
        break
while n<0:
      print("It is not a prime number")
      break
