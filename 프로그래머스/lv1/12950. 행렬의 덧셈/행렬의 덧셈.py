def solution(arr1, arr2):
    import numpy as np
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    # result = sum(arr1, arr2, axis = 1)
    result = arr1+arr2
    result = result.tolist()
    # print(result)
    # return sum(arr1, arr2)
    return result