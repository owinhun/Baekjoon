n1 = int(input())
n2 = int(input())

a = n2 // 100
b = n2 // 10
b_1 = b % 10
c = n2 % 10

n_a = n1 * a
n_b = n1 * b_1
n_c = n1 * c
result = (100 * n_a) + (10 * n_b) + n_c

print(n_c)
print(n_b)
print(n_a)
print(result)