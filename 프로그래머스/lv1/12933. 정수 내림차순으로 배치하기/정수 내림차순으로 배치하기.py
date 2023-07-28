def solution(n):
    n = str(n)
    list_n = [int(i) for i in n]
    list_n.sort()
    list_n = list_n[::-1]

    # print(list_n)
    # print(type(list_n))

    nums = ''.join(map(str, list_n))
    nums = int(nums)
    # print(nums)
    # print(type(nums))
    
    return nums