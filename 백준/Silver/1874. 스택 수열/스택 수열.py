
n = int(input())

se = []
for i in range(n):
    se.append(int(input()))

s_li = []
result = []
cu = 1
pp = True

for n in se:
    if cu <= n:
        while cu <= n:
            s_li.append(cu)
            result.append('+')
            cu += 1
        s_li.pop()
        result.append('-')

    else:
        if s_li and s_li[-1] == n:
            s_li.pop()
            result.append('-')

        else:
            pp = False
            break

if pp:
    print("\n".join(result))

else:
    print('NO')
