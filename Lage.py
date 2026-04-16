n = int(input())
for i in range(n):
    t = int(input())
    if t <= 4:
        print(1)
    else:
        if t%4==0:
            print(t//4)
        elif t%4 != 0 and t%4 < 2 :
            print(t//4)
        else:
            print((t//4)+1)       
