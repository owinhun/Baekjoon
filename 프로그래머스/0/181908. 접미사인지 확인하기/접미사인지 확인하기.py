def solution(my_string, is_suffix):
    
    if len(is_suffix) > len(my_string):
        return 0
    
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    else:
        return 0