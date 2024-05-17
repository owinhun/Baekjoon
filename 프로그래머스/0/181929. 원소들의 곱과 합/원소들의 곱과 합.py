def solution(num_list):
    mul = 1
    sum_ = 0
    
    for i in num_list:
        mul *= i
        sum_ += i
        
    if mul < sum_**2:
        return 1
    
    else:
        return 0

    