t = int(input())

for i in range(t):
    cnt = 0
    a, b = map(int, input().split())

    for j in range(a, b + 1):
        st = str(j)
        cnt += st.count('0')
    print(cnt)