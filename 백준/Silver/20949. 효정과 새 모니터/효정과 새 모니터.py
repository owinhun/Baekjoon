n = int(input())

li = []

for i in range(n):
    w,h = map(int, input().split())
    li.append([w*w + h*h, i])

for i in sorted(li, key = lambda x : (-x[0], x[1])):
    print(i[1] + 1)
