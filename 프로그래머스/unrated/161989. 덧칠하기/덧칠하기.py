def solution(n, m, section):
    cnt = 0
    sections = section[0] - 1
    for i in section:
        if sections < i:
            sections = m + i - 1
            cnt += 1


    return cnt