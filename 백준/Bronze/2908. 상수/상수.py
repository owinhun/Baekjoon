a, b = map(str, input().split())

for i in range(3):
    r_a = a[i:] + a[i-1:2] + a[:-2]
    b_a = b[i:] + b[i-1:2] + b[:-2]

if r_a > b_a:
    print(r_a)
        
else:
    print(b_a)