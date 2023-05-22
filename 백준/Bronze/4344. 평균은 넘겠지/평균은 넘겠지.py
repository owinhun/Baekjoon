c = int(input())

for i in range(c):
    nums = list(map(int, input().split()))
    sums = 0
    means = 0

    for j in range((len(nums) - 1)):
        sums += nums[j + 1]
    average = sums / nums[0]

    for k in nums[1:]:
        if k > average:
            means += 1
    re = means / nums[0]
    pc = re * 100

    print("{:.3f}%".format(pc))