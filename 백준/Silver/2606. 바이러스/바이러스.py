def dfs(t, s, v):
    v[s] = True
    count = 0
    for i in t[s]:
        if not v[i]:
            count += dfs(t, i, v) + 1
    return count

com = int(input())
connected_com = int(input())

tree = [[] for i in range(com + 1)]

for j in range(connected_com):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited_t = [0] * (com + 1)
result = dfs(tree, 1, visited_t)
print(result)