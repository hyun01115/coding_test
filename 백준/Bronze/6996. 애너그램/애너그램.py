case=int(input())

for _ in range(case):
    a,b=input().split()
    A=sorted(a)
    B=sorted(b)

    if A==B:
        print(a,'&',b,"are anagrams.")
    else:
        print(a,"&",b,"are NOT anagrams.")