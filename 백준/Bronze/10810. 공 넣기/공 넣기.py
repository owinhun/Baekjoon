n, m = map(int, input().split())

ba = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())

    for num in range(i-1, j):
        ba[num] = k

for ba_ in ba:
    print(ba_)
