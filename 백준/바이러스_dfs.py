n = int(input())
m = int(input())
visited = [ 0 for _ in range(n+1)]
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    visited[i] = 1

    for j in graph[i]:
        if not visited[j]:
            dfs(j)

dfs(1)
print(sum(visited)-1)