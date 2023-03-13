#지역 갯수 10만, nlogn의 시간복잡도를 가지도록 
#시간 초과, 각 소스별로 dst까지 각각 최단거리를 구하는중 

from collections import deque
def solution(n, roads, sources, destination):
    answer = []  #0번 지역구를 제외하니 
    roads_2 = [[] for _ in range(n+1)] #지역의 번호는 1~n, 0은 걍 냅둠
    #양방향
    for r in roads:
        roads_2[r[0]].append(r[1])
        roads_2[r[1]].append(r[0])

    for i in sources:
        if i == destination:
            answer.append(0)
            continue
        visited = [0 for _ in range(n+1)]
        q = deque()
        q.append(i) #i는 시작점
        dist = [0 for _ in range(n+1)] #i에서 해당 인덱스까지 거리 
        nx = 0

        while q:
            x = q.popleft()
            for nx in roads_2[x]:
                if visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    dist[nx] = dist[x] + 1

                    if nx == destination:
                        answer.append(dist[nx])
                        break
            if nx == destination:
              break
        if nx != destination:
          answer.append(-1)

    return answer