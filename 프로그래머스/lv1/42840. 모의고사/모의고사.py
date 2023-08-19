def solution(an):
    person1 = [1, 2, 3, 4, 5]*len(an)
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]*len(an)
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(an)
    result = []

    cnt = [0, 0, 0]

    for i in range(1, len(an)+1):
        if an[i-1] == person1[i - 1]:
            cnt[0] += 1

        if an[i-1] == person2[i - 1]:
            cnt[1] += 1

        if an[i-1] == person3[i - 1]:
            cnt[2] += 1

    for i, cntt in enumerate(cnt):
        if max(cnt) == cntt:
            result.append(i+1)

    return result