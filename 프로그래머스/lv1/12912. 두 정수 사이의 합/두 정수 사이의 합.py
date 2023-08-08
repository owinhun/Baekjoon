def solution(a, b):
    if b > a:
        nums = [int(i) for i in range(a, b+1)]
        s_num = 0

        for i in nums:
            s_num += i
        return s_num

    else:
        nums = [int(i) for i in range(b, a + 1)]
        s_num = 0

        for i in nums:
            s_num += i
        return s_num