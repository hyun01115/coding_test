T = int(input())

for _ in range(T):
    N= input()
    
    reverse = N[::-1]
    sum= str(int(N)+int(reverse))
    if sum == sum[::-1]:
        print("YES")
    else:
        print("NO")