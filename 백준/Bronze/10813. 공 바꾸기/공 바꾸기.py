n, m = map(int, input().split())

ba = [k+1 for k in range(n)]

for _ in range(m):
    i, j = map(int, input().split())

    ba[i-1], ba[j-1] = ba[j-1], ba[i-1]

for ba_ in ba:
    print(ba_)