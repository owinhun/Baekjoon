import sys
input = sys.stdin.readline

n = int(input())
ju = list(map(int, input().split()))
j_th = 0
i_th = 0

for i in range(n - 1, -1, -1):
    j_th = max(j_th, ju[i])
    i_th = max(i_th, j_th - ju[i])

print(i_th)