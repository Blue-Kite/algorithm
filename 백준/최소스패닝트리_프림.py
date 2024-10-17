from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range((n+1))] #방문여부 
answer = 0 #최소 스패닝트리의 가중치합 
cnt = 0 
q = deque([])

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([w,b])
    graph[b].append([w,a])

q.append([0, 1]) # [본인 가중치, 1번노드]

while q:
    w, v = q.popleft()
    
    if not visited[v]:
        visited[v] = 1
        answer += w

        for nxt in graph[v]:
            q.append([nxt[0], nex[1]])
return answer

