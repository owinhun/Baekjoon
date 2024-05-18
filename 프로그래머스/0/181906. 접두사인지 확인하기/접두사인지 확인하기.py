def solution(my_string, is_prefix):
    
    if len(is_prefix) > len(my_string):
        return 0
    
    
    if my_string[:len(is_prefix)] == is_prefix:
        return 1

    else:
        return 0