n = int(input())
asw = 0

for i in range(0,n):
    f,s,t = map(int, input().split())
    
    if (f == s == t):
        asw = max(asw, 10000+f*1000)
    elif (f == s):
        asw = max(asw, 1000+f*100)
    elif (f == t):
        asw = max(asw, 1000+f*100)
    elif (s == t):
        asw = max(asw, 1000+s*100)
    else:
        asw = max(asw, 100*max(f,s,t))
        
print(asw)