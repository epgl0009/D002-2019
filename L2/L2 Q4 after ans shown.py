a=0
max=0
for a in range(0,61):
    for b in range(0,60-a+1):
        for c in range(0,100-a-b+1):
        d=60-a-b-c
        value= a*b+b*c+c*d
        if value > max:
            max = value
            print(a,b,c,d,max)
print("Max product is %d" % max)
