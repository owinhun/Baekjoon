n = int(input())

max_prize = 0

for i in range(n):
    dice = list(map(int, input().split()))
    dice_count = [0] * 7

    for d in dice:
        dice_count[d] += 1

    prize = 0
    for j in range(1, 7):
        if dice_count[j] == 4:
            prize = 50000 + j * 5000
            break

    if prize == 0:
        for j in range(1, 7):
            if dice_count[j] == 3:
                prize = 10000 + j * 1000
                break

    if prize == 0:
        for j in range(1, 7):
            if dice_count[j] == 2:
                for k in range(1, 7):
                    if k != j and dice_count[k] == 2:
                        prize = 2000 + j * 500 + k * 500
                        break
                if prize != 0:
                    break
        if prize == 0:
            for j in range(1, 7):
                if dice_count[j] == 2:
                    prize = 1000 + j * 100
                    break

    if prize == 0:
        max_dice = max(dice)
        prize = max_dice * 100

    if prize > max_prize:
        max_prize = prize

print(max_prize)