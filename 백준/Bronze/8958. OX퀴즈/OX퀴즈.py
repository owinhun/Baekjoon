t = int(input())

for i in range(t):
    OX = input()
    s = list(OX)
    sum = 0
    cnt = 1
    for i in s:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)