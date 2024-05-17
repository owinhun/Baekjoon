def solution(arr):
    n_arr = []
    
    for i in arr:
        if i >= 50 and i % 2 == 0:
            i = i // 2
            n_arr.append(i)
            
        elif i < 50 and i % 2 == 1:
            i = i * 2
            n_arr.append(i)
            
        elif i < 50 and i % 2 == 0:
            i = i
            n_arr.append(i)
            
        else:
            n_arr.append(i)
            
    
    return n_arr