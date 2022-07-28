n = int(input())

nums = list(map(int, input().split()))

mx_nums = max(nums)
mn_nums = min(nums)

print(mx_nums * mn_nums)
