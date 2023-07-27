def solution(k, m, score):
    cnt = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        if i + m <= len(score):
            cnt += score[i + m - 1]
        
    cnt = cnt * m

    return cnt