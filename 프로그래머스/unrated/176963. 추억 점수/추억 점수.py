def solution(name, yearning, photo):
    sum_list = []
    dict = {}
    for i, j in zip(name, yearning):
        dict[i] = j
    for names in photo:
        sum_count = 0
        for inside in names:
            try:
                sum_count += dict[inside]
            except KeyError:
                pass
        sum_list.append(sum_count)
    return sum_list