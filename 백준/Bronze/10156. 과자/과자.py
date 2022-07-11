k, n, m = map(int, input().split())

result = (k*n) - m

if result > 0:
    print(result)
else:
    print(0)