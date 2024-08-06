a=[]

for i in range(5):
    b=int(input())
    a.append(b)

for i in range(5):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

average= sum(a)//len(a)
middle= a[2]

print(average)
print(middle)