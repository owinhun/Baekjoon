x = int(input())
x_ = 64
cnt = 0

while (1):
    if x < x_:
        x_ = x_ // 2
    else:
        x = x - x_
        cnt += 1
        if(x == 0):
            break
print(cnt)