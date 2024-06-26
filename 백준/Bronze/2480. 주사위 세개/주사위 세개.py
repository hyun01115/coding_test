a,b,c=map(int,input().split())
if a==b==c:
    total = 10000+(a*1000)
    print(total)
elif a==b or b==c or c==a:
    if a==b:
        total = 1000+(a*100)
        print(total)
    elif b==c:
        total = 1000+(b*100)
        print(total)
    else:
        total = 1000+(c*100)
        print(total)
else:
    if a<c and b<c:
        total = c*100
        print(total)
    elif c<a and b<a:
        total = a*100
        print(total)
    elif a<b and c<b:
        total = b*100
        print(total)