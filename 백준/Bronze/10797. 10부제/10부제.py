one = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(5):
    if one == nums[i]:
        cnt += 1

print(cnt)