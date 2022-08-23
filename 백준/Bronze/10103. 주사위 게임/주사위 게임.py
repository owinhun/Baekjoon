n = int(input())
chang = 100
shang = 100

for i in range(n):
    one, two = map(int, input().split())
    
    if one > two:
        shang = shang - one
        
    elif one == two:
        chang = chang
        shang = shang
    
    else:
        chang = chang - two
        
print(chang)
print(shang)