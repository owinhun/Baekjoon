n = int(input())
nnums = list(map(int, input().split()))

m = int(input())
mnums = list(map(int, input().split()))

di = {}

for num in nnums:
    if num in di:
        di[num] += 1

    else:
        di[num] = 1

result = []

for q in mnums:
    if q in di:
        result.append(di[q])

    else:
        result.append(0)

print(" ".join(map(str, result)))
