import sys
input = sys.stdin.readline

N = int(input())

AI = list(map(int, input().split()))

B, C = map(int, input().split())

re = 0

for i in AI:
    i -= B
    cnt = 1
    if i > 0:
        cnt += i // C
        if i % C != 0:
            cnt += 1
    re += cnt

print(re)