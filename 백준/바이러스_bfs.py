from collections import deque
n = int(input())
m = int(input())
visited = [ 0 for _ in range(n+1)]
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([])
q.append(1)

while q:
    v = q.popleft()

    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = 1

print(sum(visited))