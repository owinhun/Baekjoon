def solution(name, yearning, photo):
    sum_list = []
    dict_ = dict(zip(name, yearning))

    for names in photo:
        sum_count = 0
        for in_ in names:
            if in_ in dict_:
                sum_count += dict_[in_]

        sum_list.append(sum_count)
    return sum_list