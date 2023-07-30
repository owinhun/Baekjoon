def solution(array, commands):
    arrays = []
    for i in commands:
        n_array = array[i[0] - 1 : i[1]]
        n_array = sorted(n_array)
        n_array = n_array[i[2] - 1]
        arrays.append(n_array)
        
    return arrays
