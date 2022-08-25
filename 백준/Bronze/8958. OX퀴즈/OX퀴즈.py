t = int(input())

for i in range(t):
    OX = list(input())
    
    sum = 0
    cnt = 1
    
    for i in OX:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)