from collections import deque

n, k = map(int, input().split())

n_li = []
q = deque()

for i in range(1, n + 1):
    q.append(i)

while q:
    for i in range(k - 1):
        q.append(q.popleft())
    n_li.append(q.popleft())

print('<', end = "")
print(", ".join(map(str, n_li)), end = "")
print('>')