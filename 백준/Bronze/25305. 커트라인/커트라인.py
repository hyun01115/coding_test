n,k=map(int,input().split())
a=list(map(int, input().split()))



for i in range(n):
    for j in range(len(a)-1-i):
        if a[j]<a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

cutline = a[k-1]

print(cutline)



