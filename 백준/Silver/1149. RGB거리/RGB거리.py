n = int(input())
k = []

for i in range(n):
    rgb = list(map(int, input().split()))
    k.append(rgb)

for j in range(1, n):
    k[j][0] = min(k[j - 1][1], k[j - 1][2]) + k[j][0]
    k[j][1] = min(k[j - 1][0], k[j - 1][2]) + k[j][1]
    k[j][2] = min(k[j - 1][0], k[j - 1][1]) + k[j][2]

print(min(k[n-1][0], k[n-1][1], k[n-1][2]))