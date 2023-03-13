#목적지는 1개
#목적지에서 각 시작점까지의 최단거리를 구함.

from collections import deque
def solution(n, roads, sources, destination):
    answer = []  #0번 지역구를 제외하니 
    roads_2 = [[] for _ in range(n+1)] #지역의 번호는 1~n, 0은 걍 냅둠
    visited = [0 for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)] #i에서 해당 인덱스까지 거리, 초기화는 경로없는 -1

    #양방향
    for r in roads:
        roads_2[r[0]].append(r[1])
        roads_2[r[1]].append(r[0])

    q = deque()
    q.append(destination)
    visited[destination] = 1 #목적지 방문처리
    dist[destination] = 0    #시작점과 목적지 동일하니 0으로 처리 
    
    while q:
        x = q.popleft()
        for nx in roads_2[x]:
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = 1
                dist[nx] = dist[x] + 1
    
    for i in sources:
        answer.append(dist[i])
        
    return answer