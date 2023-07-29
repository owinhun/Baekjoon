def solution(arr):
    if len(arr) == 1:
        # print('[-1]')
        return [-1]
    else:
        m_arr = min(arr)
        # print(arr)
        arr.remove(m_arr)
        # print(arr)
        return arr