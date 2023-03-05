n, m = map(int, input().split())

nums = list(map(int, input().split()))

height = max(nums)
cnt = 1

while cnt <= height:
    middle = (cnt + height) // 2

    tree = 0
    for i in nums:
        if i >= middle:
            tree += i - middle
    if tree >= m:
        cnt = middle + 1

    else:
        height = middle - 1

print(height)
