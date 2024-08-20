n=int(input())
num=list(map(int, input().split()))

num.sort()
c=0
for i in range(n+1):
    c+=sum(num[:i])
print(c)