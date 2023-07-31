def solution(price, money, count):
    s_cnt = 0

    for i in range(1, count+1):
        s_cnt += i * price

    if money >= s_cnt:
        return 0

    else:
        result = s_cnt - money
    return result