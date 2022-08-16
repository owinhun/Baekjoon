x = int(input())
n = int(input())

sums = 0

for i in range(n):
    price, cnt = map(int, input().split())
    
    sums += price*cnt

if sums == x:
    print('Yes')

else:
    print('No')