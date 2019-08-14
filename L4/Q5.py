def printer(secret, opened):
    i = 0
    x=[]
    while i < len(secret):
        for y in range(0,len(secret)):
            if i not in opened:
                x.append("_")
                i = i + 1
            elif i in opened:
                x.append(secret[i])
                i = i + 1            
    print(x, end="")
# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
