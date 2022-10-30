cnt = 0
max_cnt = []

for i in range(4):
    out_n, in_n = map(int, input().split())

    if i == 0:
        cnt += in_n
        max_cnt.append(cnt)
    
    elif i == 1:
        cnt -= out_n
        cnt += in_n
        max_cnt.append(cnt)
    
    elif i == 2:
        cnt -= out_n
        cnt += in_n
        max_cnt.append(cnt)
        
    else:
        cnt -= out_n
        max_cnt.append(cnt)
        
print(max(max_cnt))