def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        m_arr = min(arr)
        arr.remove(m_arr)
        return arr