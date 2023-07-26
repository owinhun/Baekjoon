def solution(number):
    cnt = 0
    l_number = len(number)
    for i in range(l_number):
        for j in range(i + 1, l_number):
            for k in range(j + 1, l_number):
                if number[i] + number[j] + number[k] == 0:
                    cnt += 1

    return cnt