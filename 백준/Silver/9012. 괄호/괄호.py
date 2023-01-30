t = int(input())

for i in range(t):
    a = input()
    li = list(a)
    sum_count = 0
    for i in li:
        if i == '(':
            sum_count += 1

        elif i == ')':
            sum_count -= 1

        if sum_count < 0:
            print('NO')
            break
    if sum_count > 0:
        print('NO')
    elif sum_count == 0:
        print('YES')
