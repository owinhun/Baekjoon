def solution(n):
    n_sqrt = n ** (1 / 2)

    if n % n_sqrt == 0:
        n__1 = int((n_sqrt + 1) ** 2)
        return n__1

    else:
        return -1