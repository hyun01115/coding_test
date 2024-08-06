n=int(input())
a=[]

for i in range(n):
    b=int(input())
    a.append(b)

for i in range(n):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

for number in a:
    print(number)