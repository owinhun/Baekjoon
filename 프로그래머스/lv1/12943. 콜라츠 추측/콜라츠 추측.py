def solution(num):
    cnt = 0
        
    if num == 1:
        return 0
    
    while True:
        if num % 2 == 0:
            num = num / 2
            cnt += 1

            if num == 1:
                break

            elif cnt >= 500:
                return -1

        elif num % 2 == 1:
            num = num*3 + 1
            cnt += 1
            if num == 1:
                break

            elif cnt >= 500:
                return -1
                
    return cnt