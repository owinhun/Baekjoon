n = int(input())

for i in range(n):
    strings = input().split(' ')
    re_strings = ' '.join(strings[::-1])

    print(f'Case #{i + 1}:', ''.join(re_strings))
