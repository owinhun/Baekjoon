import sys
sys.setrecursionlimit(10**3)

def dfs(st, visited):
    stack = [st]
    
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(graph[v])
            

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
cnt = 0
vi = set()

for i in range(1, n + 1):
    if i not in vi:
        dfs(i, vi)
        cnt += 1
        
print(cnt)
        