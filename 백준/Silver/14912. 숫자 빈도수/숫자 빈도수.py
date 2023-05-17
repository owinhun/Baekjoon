n, digit = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    st = str(i)
    cnt += st.count(str(digit))

print(cnt)