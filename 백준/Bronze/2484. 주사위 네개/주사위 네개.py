n = int(input())

max_prize = 0
for i in range(n):
    n_li = [0 for j in range(7)]
    nums = list(map(int, input().split()))

    for d in nums:
        n_li[d] += 1

    result = 0
    for j in range(1, 7):
        if n_li[j] == 4:
            result = 50000 + j * 5000
        elif n_li[j] == 3:
            result = 10000 + j * 1000
        elif n_li[j] == 2:
            for j in range(1, 7):
                if n_li[j] == 2:
                    for k in range(1, 7):
                        if k != j and n_li[k] == 2:
                            result = 2000 + j * 500 + k * 500
                            break
                    if result != 0:
                        break
            if result == 0:
                for j in range(1, 7):
                    if n_li[j] == 2:
                        result = 1000 + j * 100
                        break

        elif n_li[j] == 2:
            result = 1000 + j * 100

    if result == 0:
        max_dice = max(nums)
        result = max_dice * 100

    max_prize = max(max_prize, result)

print(max_prize)