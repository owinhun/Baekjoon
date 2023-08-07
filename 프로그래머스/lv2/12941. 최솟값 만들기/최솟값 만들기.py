def solution(a, b):
    sum_a_b = 0
    a.sort()
    b.sort(reverse=True)

    for i in range(len(a)):
        result = a[i] * b[i]

        if a[i] == a[0]:
            sum_a_b += result

        else:
            sum_a_b += result

    return sum_a_b