def solution(my_strings, parts):
    result = []
    
    for i in range(len(my_strings)):
        s, e = parts[i]
        
        result.append(my_strings[i][s:e+1])
        
    return ''.join(result)
        