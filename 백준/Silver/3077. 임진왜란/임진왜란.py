n = int(input())
dab = input().split()
dict_ = {}

for i in range(n):
    dict_[dab[i]] = i

h_dab = input().split()
cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if dict_[h_dab[i]] < dict_[h_dab[j]]:
            cnt += 1
print(f"{cnt}/{n * (n - 1) // 2}")