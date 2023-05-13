n = int(input())

nums = list(map(int, input().split()))
new_nums = []

for i in range(1, n + 1):
    new_nums.insert(len(new_nums)-nums[i - 1], i)

for j in range(n):
    print(new_nums[j], end=' ')