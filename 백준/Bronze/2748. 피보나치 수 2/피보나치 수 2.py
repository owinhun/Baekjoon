n = int(input())
fib = [i for i in range(n+1)]
fib[1] = 1

for i in range(2, n+1) :
    fib[i] = fib[i-1] + fib[i-2]
    
print(fib[-1])