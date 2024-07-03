def get_prize(dice):
    dice.sort()
    count = [0] * 7
    for d in dice:
        count[d] += 1
    
    if 4 in count:
        i = count.index(4)
        return 50000 + i * 5000
    elif 3 in count:
        i = count.index(3)
        return 10000 + i * 1000
    elif 2 in count and count.count(2) == 2:
        i = count.index(2)
        j = count.index(2, i+1)
        return 2000 + i * 500 + j * 500
    elif 2 in count:
        i = count.index(2)
        return 1000 + i * 100
    else:
        return max(dice) * 100

N = int(input())
max_prize = 0
for _ in range(N):
    dice = list(map(int, input().split()))
    prize = get_prize(dice)
    max_prize = max(max_prize, prize)

print(max_prize)