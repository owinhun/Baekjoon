n = int(input())
x_y = []
a_x_y = []

for i in range(n):
    x, y = map(int, input().split())
    x_y.append((x, y))

for i in range(n):
    rank = 0
    for j in range(n):
        if x_y[i][0] < x_y[j][0] and x_y[i][1] < x_y[j][1]:
            rank += 1
    a_x_y.append(rank + 1)

for i in a_x_y:
    print(i, end = ' ')
