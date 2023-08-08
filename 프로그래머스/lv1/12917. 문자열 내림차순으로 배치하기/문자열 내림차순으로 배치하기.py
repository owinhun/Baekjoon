def solution(s):
    s = [i for i in s]
    s.sort(reverse=True)
    s = ''.join(s)
    return s