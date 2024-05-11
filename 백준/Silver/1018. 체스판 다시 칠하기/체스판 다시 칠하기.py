n, m = map(int, input().split())

nemo = []
for k in range(n):
    nemo.append(input())

min_changes = float('inf')

for i in range(n-7):
    for j in range(m-7):
        h1 = 0
        h2 = 0
        for k in range(i, i + 8):
            for q in range(j, j + 8):
                if (k + q) % 2 == 0:
                    if nemo[k][q] == 'W':
                        h1 += 1
                    else:
                        h2 += 1
                else:
                    if nemo[k][q] == 'B':
                        h1 += 1
                    else:
                        h2 += 1
        min_changes = min(min_changes, h1, h2)

print(min_changes)