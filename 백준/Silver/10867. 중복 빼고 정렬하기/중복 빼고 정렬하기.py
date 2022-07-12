n = int(input())

nums = list(map(int, input().split()))
    
for i in sorted(list(set(nums))):
    print(i, end = " ")