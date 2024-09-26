from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

result = 0
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

q = deque([])
for i in range(1, n+1):
    if not visited[i]:
        q.append(i)
        visited[i] = 1

        while q:
            v = q.popleft()
            for j in graph[v]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = 1
        result += 1
                    
print(result)    