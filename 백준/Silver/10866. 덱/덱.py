import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
q = deque()

for _ in range(n):
    command = input().split()

    if command[0] == 'push_front':
        q.appendleft(int(command[1]))

    elif command[0] == 'push_back':
        q.append(int(command[1]))

    elif command[0] == 'pop_front':
        if q:
            output(str(q.popleft()) + '\n')
        else:
            output('-1\n')

    elif command[0] == 'pop_back':
        if q:
            output(str(q.pop()) + '\n')
        else:
            output('-1\n')

    elif command[0] == 'size':
        output(str(len(q)) + '\n')

    elif command[0] == 'empty':
        if q:
            output('0\n')
        else:
            output('1\n')

    elif command[0] == 'front':
        if q:
            output(str(q[0]) + '\n')
        else:
            output('-1\n')

    elif command[0] == 'back':
        if q:
            output(str(q[-1]) + '\n')
        else:
            output('-1\n')
