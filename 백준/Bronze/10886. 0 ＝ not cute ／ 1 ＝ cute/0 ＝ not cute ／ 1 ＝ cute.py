n = int(input())

li = []
result = ''

for i in range(0,n):
    n = int(input())
    li.append(n)
    
    if li.count(1) > li.count(0):
        result = 'Junhee is cute!'
    else:
        result = 'Junhee is not cute!'
        
print(result)