import sys

n = int(input())
s = []

for i in range(n):
    method = sys.stdin.readline().split()

    if method[0] == 'push':
        s.append(method[1])

    elif method[0] == 'pop':
        if len(s) == 0:
            print(-1)

        else:
            result = s.pop()
            print(result)

    elif method[0] == 'size':
        print(len(s))

    elif method[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)

    elif method[0] == 'top':
        if len(s) == 0:
            print(-1)

        else:
            print(s[-1])

