from math import *
y=int(input("Enter a year "))
if(y%4==0 and y%100!=0):
      print("Yes, it is a leap year" )
elif(float(y%400)==0):
      print("Yes, it is a leap year" )
else:
      print("No, it is not a leap year" )
      
