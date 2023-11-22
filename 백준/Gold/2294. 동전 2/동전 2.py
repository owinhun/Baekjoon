n, k = map(int, input().split())
sset = set()

for i in range(n):
    sset.add(int(input()))

inf = k + 1
dp = [inf]*(k+1)
dp[0] = 0

for coin in sset:
    for j in range(1, k + 1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j-coin] + 1)

ans = dp[k]

if ans == inf:
    ans = -1

print(ans)