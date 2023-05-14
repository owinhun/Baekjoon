n = int(input())

fibo = [1, 1, 1]

for i in range(3, n + 1):
    fibo.append(fibo[i - 1] + fibo[i - 3])

print(fibo[n - 1])