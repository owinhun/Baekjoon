def solution(num_list):
    odd_n = ''.join([str(num) for num in num_list if num % 2 == 1])
    odd_e = ''.join([str(num) for num in num_list if num % 2 == 0])
    
    odd = int(odd_n) if odd_n else 0
    even = int(odd_e) if odd_e else 0
    
    
    return odd + even