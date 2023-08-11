def solution(t, p):
    len_p = len(p)
    n_t = []
    n_n_t = []
    for i in range(len(t)):
        if len(t[i:len_p+i]) == len_p:
            n_t.append(t[i:len_p+i])

    for j in range(len(n_t)):
        if n_t[j] <= p:
            n_n_t.append(n_t[j])

    return len(n_n_t)