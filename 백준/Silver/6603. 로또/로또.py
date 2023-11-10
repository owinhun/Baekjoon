
def dfs(d, idx):
    if d == 6:
        print(*result)
        return

    for i in range(idx, cnt):
        result.append(nums[i])
        dfs(d + 1, i + 1)
        result.pop()

while True:
    lotto = list(map(int, input().split()))
    cnt = lotto[0]
    nums = lotto[1:]

    result = []
    dfs(0, 0)
    if cnt == 0:
        break

    print()
