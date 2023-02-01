from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = []

for _ in range(m):
    st, en = map(int, input().split())
    graph[st].append(en)

#x에서 모든 도시에 대한 최단거리, 방문여부도 확인가능 
distance = [-1 for _ in range(n+1)]
distance[x] = 0 #자기자신까지 거리는 0

#bfs
q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

for i in range(n+1):
    if distance[]
    


