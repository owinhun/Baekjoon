from collections import deque

n = int(input())

nums = deque()

for i in range(1, n + 1):
    nums.append(i)

while nums:
    if len(nums) >= 2:
        first = nums.popleft()
        second = nums.popleft()
        nums.append(second)

    elif len(nums) == 1:
        print(nums[-1])
        break
