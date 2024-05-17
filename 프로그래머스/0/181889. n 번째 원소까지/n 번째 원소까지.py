def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list)):
        if i < n:
            answer.append(num_list[i])
    
    return answer