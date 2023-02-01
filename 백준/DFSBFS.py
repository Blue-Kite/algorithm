from collections import deque
def bfs(graph, v, visited):
  que = deque()
  que.append(v)
  visited[v] = True

  while que:
    vertex = que.popleft()
    print(vertex, end = ' ')

    for i in graph[vertex]:
      if not visited[i]:
        que.append(i)
        visited[i] = True

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end =' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(graph.copy(), v, visited.copy())
print()
bfs(graph.copy(), v, visited.copy())
    



