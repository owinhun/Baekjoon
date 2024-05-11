import sys

n = int(input())
q = []

for i in range(n):
    method = sys.stdin.readline().split()

    if method[0] == 'push':
        q.append(method[1])

    elif method[0] == 'pop':
        if len(q) == 0:
            print(-1)

        else:
            result = q.pop(0)
            print(result)

    elif method[0] == 'size':
        print(len(q))

    elif method[0] == 'empty':
        if len(q) == 0:
            print(1)

        else:
            print(0)

    elif method[0] == 'front':
        if len(q) == 0:
            print(-1)

        else:
            print(q[0])

    elif method[0] == 'back':
        if len(q) == 0:
            print(-1)

        else:
            print(q[-1])