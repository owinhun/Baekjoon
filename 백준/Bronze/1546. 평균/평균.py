n = int(input())
m = list(map(int, input().split()))
max_ = max(m)

for i in range(n):
    m[i] = m[i]/max_*100
print("%.2f" %(sum(m)/n))