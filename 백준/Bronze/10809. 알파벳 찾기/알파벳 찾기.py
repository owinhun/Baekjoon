S = list(input())
ahp = 'abcdefghijklmnopqrstuvwxyz'

for i in ahp:
    if i in S:
        print(S.index(i), end = " ")
    else:
        print(-1, end = " ")