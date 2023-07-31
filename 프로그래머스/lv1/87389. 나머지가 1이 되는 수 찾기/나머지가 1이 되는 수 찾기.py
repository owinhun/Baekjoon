def solution(n):
    x = n - 1
    n_x = []
    if n % x == 1:
        for i in range(1, x + 1):
            if x % i == 0:
                n_x.append(i)
        return n_x[1]