A, B =input().split()

max= int(A.replace('5','6')) + int(B.replace('5','6'))
min= int(A.replace("6","5")) + int(B.replace("6","5"))

print(min,max)