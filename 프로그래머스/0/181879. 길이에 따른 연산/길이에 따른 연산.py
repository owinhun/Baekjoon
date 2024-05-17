def solution(num_list):
    result = 0
    mul = 1
    
    if len(num_list) >= 11:
        result = sum(num_list)
        return result
        
    else:
        for i in num_list:
            mul *= i
            
        result = mul
        return result
    