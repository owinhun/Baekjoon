import sys

n = int(sys.stdin.readline())
l1 = []

for i in range(n):
    l1.append(list(map(int, sys.stdin.readline().split())))
l1.sort(key=lambda x : (x[0], x[1]))

for i in l1:
    print(i[0],i[1])